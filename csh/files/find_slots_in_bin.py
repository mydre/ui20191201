def find_empty_space(ImageFile):
    with open(ImageFile, 'rb') as f:
        d = f.read().decode('latin1')

    total_space = 0
    index = 0
    while True:
        ret = d.find('\x00' * 0x100, index)
        if ret == -1:
            break

        length = 0x100
        while True:
            if d[ret + length] == '\x00':
                length += 1
            else:
                break

        if (ret + length) & 0xff <= 4:
            start = (ret + 0x30) & 0xfffffff0
            end = (ret + length) & 0xffffff00
            print('empty space:%s - %s, size=%s', hex(start-0x20+0xc0008000), hex(end+0xc0008000), hex(end - start))
            total_space += (end - start)
        else:
            # print hex(ret), hex(ret+len), hex(len), hex(ret+0xC0008000)
            pass

        index = ret + length

    print('findl total space: %s' % hex(total_space))

if __name__ == '__main__':
    find_empty_space('./csh/files/Image')

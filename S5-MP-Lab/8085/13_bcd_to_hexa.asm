; A S Nandanunni
; Reg No: 20219023
; CS - A
; BCD to Hexadecimal Conversion

LDA 0000h
MOV B, A
ANI 0FH
MOV C, A
MOV A, B
ANI F0H
RRC
RRC
RRC
RRC
MOV D, A
MVI E, 0AH
XRA A
LOOP: ADD D
DCR E
JNZ LOOP
ADD C
STA 0010H
HLT
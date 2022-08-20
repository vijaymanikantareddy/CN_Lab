4. Write a program for Hamming Code generation for error detection and correction.

Hamming code is popular error detection and error correction method in data communication. Hamming code can only detect 2-bit errors and correct a single-bit error which means it is unable to correct burst errors that may occur during the transmission of data.


Hamming code uses redundant bits (extra bits) which are calculated according to the below formula:-


2r ≥ m+r+1

Where r is the number of redundant bits required and m is the number of data bits.


R is calculated by putting r = 1, 2, 3 … until the above equation becomes true.


R1 bit is appended at position 20


R2 bit is appended at position 21


R3 bit is appended at position 22 and so on.


These redundant bits are then added to the original data for the calculation of error at the receiver’s end.

At the receiver’s end with the help of even parity (generally), the erroneous bit position is identified and since the data is in binary we take the complement of the erroneous bit position to correct the received data.


Respective index parity is calculated for r1, r2, r3, r4 and so on.


(https://www.thecrazyprogrammer.com/wp-content/uploads/2017/03/Hamming-Code-in-C-and-C.jpg?ezimgfmt=rs:638x479/rscb1/ng:webp/ngcb1)

INPUT FORMAT:


The first line contains the 7 bits data of 0's and 1's separated by spaces.

The second line contains the received 11 data bits of 0's and 1's separated by spaces.

OUTPUT FORMAT:

prints the error bit position or "no error" 

SAMPLE INPUT 1: 

1 0 1 0 1 0 1


1 0 1 0 0 1 0 1 1 0 1


SAMPLE OUTPUT 1:


2


SAMPLE INPUT 2: 


1 0 1 0 1 0 1


1 0 1 0 0 1 0 1 1 1 1



SAMPLE OUTPUT 2:


no error


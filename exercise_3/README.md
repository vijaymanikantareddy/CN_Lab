3. Write a Program to implement data link layer farming method checksum.

Checksum is the error detection method. This method makes the use of Checksum Generator on Sender side and Checksum Checker on Receiver side. 


At the Sender side, the data is divided into equal subunits of n bit length by the checksum generator. This bit is generally of 16-bit length. These subunits are then added together using one’s complement method. This sum is of n bits. The resultant bit is then complemented. This complemented sum which is called checksum is appended to the end of original data unit and is then transmitted to Receiver. 


The Receiver after receiving data + checksum passes it to checksum checker. Checksum checker divides this data unit into various subunits of equal length and adds all these subunits. These subunits also contain checksum as one of the subunits. The resultant bit is then complemented. If the complemented result is zero, it means the data is error-free. If the result is non-zero it means the data contains an error and Receiver rejects it.

![Bit_Byte_Stuffing_1](https://media.geeksforgeeks.org/wp-content/uploads/20200909115220/Checksum.png)

Example – 
If the data unit to be transmitted is 10101001 00111001, the following procedure is used at Sender site and Receiver site. 

Sender Site : 

 


10101001        subunit 1  

00111001        subunit 2        

11100010        sum (using 1s complement)       

00011101        checksum (complement of sum)

Data transmitted to Receiver is – 

![Bit_Byte_Stuffing_1](https://media.geeksforgeeks.org/wp-content/uploads/20200909115953/12.png)

Receiver Site : 

 

10101001        subunit 1  

00111001        subunit 2    

00011101        checksum 

11111111        sum

00000000        sum's complement


Result is zero, it means no error.

INPUT FORMAT:


The first line contains the length of the string.

The second line contains the string of 0's and 1's as subunit1.

The third line contains the string of 0's and 1's as subunit2.

OUTPUT FORMAT:

Contains a checksum of two subunits.

SAMPLE INPUT: 

8

1 0 1 0 1 0 0 1

0 0 1 1 1 0 0 1


SAMPLE OUTPUT:


0 0 0 1 1 1 0 1

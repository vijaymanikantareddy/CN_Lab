2. ii) Write a Program to implement the data link layer farming methods such as --> bit stuffing.

The new technique allows data frames to contain an arbitrary number of bits and allows character codes with an arbitrary no of bits per character. Each frame begins and ends with the special bit pattern, 01111110, called a flag byte. Whenever the sender's data link layer encounters five consecutive ones in the data, it automatically stuffs a 0 bit into the outgoing bit stream.

![Bit_Byte_Stuffing_1](https://media.geeksforgeeks.org/wp-content/uploads/Bit_Byte_Stuffing_2.jpg)

INPUT FORMAT:

The first line contains the frame size

The second line has the frame in the form of 0 or 1. 

OUTPUT FORMAT:

Contains a frame after bit stuffing.

SAMPLE INPUT:

5

1 1 1 1 1

SAMPLE OUTPUT:

111110

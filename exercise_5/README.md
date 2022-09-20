CRC or Cyclic Redundancy Check is a method of detecting accidental changes/errors in the communication channel. 

CRC uses Generator Polynomial which is available on both sender and receiver side. An example generator polynomial is of the form like x3 + x + 1. This generator polynomial represents key 1011. Another example is x2 + 1 that represents key 101. 


n : Number of bits in data to be sent 
    from sender side.  
    
k : Number of bits in the key obtained 
    from generator polynomial.
    
Sender Side (Generation of Encoded Data from Data and Generator Polynomial (or Key)): 


The binary data is first augmented by adding k-1 zeros in the end of the data

Use modulo-2 binary division to divide binary data by the key and store remainder of division.

Append the remainder at the end of the data to form the encoded data and send the same

 Receiver Side (Check if there are errors introduced in transmission)
 
Perform modulo-2 division again and if the remainder is 0, then there are no errors. 


In this article we will focus only on finding the remainder i.e. check word and the code word.


Modulo 2 Division:

The process of modulo-2 binary division is the same as the familiar division process we use for decimal numbers. Just that instead of subtraction, we use XOR here.


In each step, a copy of the divisor (or data) is XORed with the k bits of the dividend (or key).

The result of the XOR operation (remainder) is (n-1) bits, which is used for the next step after 1 extra bit is pulled down to make it n bits long.

When there are no bits left to pull down, we have a result. The (n-1)-bit remainder which is appended at the sender side.

Illustration:

Example 1 (No error in transmission): 


Data word to be sent - 100100
Key - 1101 
[ Or generator polynomial x3 + x2 + 1]

Sender Side:

sender

![](https://cdncontribute.geeksforgeeks.org/wp-content/uploads/rational1.jpg)


Therefore, the remainder is 001 and hence the encoded 

data sent is 100100001.


Receiver Side:

Code word received at the receiver side  100100001


receiver y![](https://cdncontribute.geeksforgeeks.org/wp-content/uploads/rational2.jpg)



Therefore, the remainder is all zeros. Hence, the data received has no error.

 
Example 2: (Error in transmission) 


Data word to be sent - 100100

Key - 1101



Sender Side:


sender![](https://cdncontribute.geeksforgeeks.org/wp-content/uploads/rational1.jpg)


Therefore, the remainder is 001 and hence the code word sent is 100100001.


Receiver Side

Let there be an error in transmission media Code word received at the receiver side - 100000001


receiver n![](https://cdncontribute.geeksforgeeks.org/wp-content/uploads/rational4.jpg)


Since the remainder is not all zeroes, the error is detected at the receiver side.


Today, CRC is widely used in various interconnection networks and software protocols. Three of the most commonly used generator polynomials are:

▪ CRC-12: G(x) = x12 + x11 + x3 + x2 + x1 +1

▪ CRC-16: G(x) = x16 + x15 + x2 + 1

▪ CRC-CCITT: G(x) = x16 + x12 + x5 + 1.

Now your task is to write a code to implement the above three generator polynomials and find if any data error is there or not.


INPUT FORMAT:

The first line contains an integer to choose one of the generator polynomials.

The second line contains the string of code word of binary data bits of 0's and 1's to be sent from the sender.

The third line contains the string of code word of binary data received at the receiver side.

OUTPUT FORMAT:

prints the message "frame error" if any error is found otherwise print "no error"

SAMPLE INPUT 1: 

1

1010101

1010101001000000010

Explanation:

the first line contains 1 which means the generator polynomial is taken as CRC-12

the second line contains the data frame of 7 bits which is the original data to be sent.

the third line contains the data frame received at the receiver ( 7 bits of original data + 12 bits of remainder appended i.e. (n-1) bits of generator polynomial)

SAMPLE OUTPUT 1:

no error

Explanation:

Perform modulo-2 division again and if the remainder is 0, then there are no errors. 

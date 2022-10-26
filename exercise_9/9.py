print("Enter bucket size, outgoing rate, number of inputs and incoming size")
bucketsize = int(input())
outgoing = int(input())
n = int(input())
incoming = int(input())
store=0
while n!= 0:
    print("Incoming size is ", incoming)
    if incoming <= (bucketsize-store):
        store += incoming
        print("Bucket buffer size is " , store ," out of " , bucketsize)
    else:
        print("Packet loss : " , (incoming-(bucketsize-store)))
        store=bucketsize
        print("Bucket buffer size is " ,store ," out of " , bucketsize)
    store -= outgoing;
    print("After outgoing: " ,store , " packets left out of ", bucketsize ,"inbuffer")
    n=n-1
a = 65534 #FF FE
b = 65535 #FF FF
c = 65536 #00 01 00 00
x = 2998302 #02 2D C0 1E

with open("binary2",'bw')as bin_file:
    #big indian format
    bin_file.write(a.to_bytes(2,'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(a.to_bytes(4, 'big'))
    bin_file.write(a.to_bytes(4 , 'big'))
    #little indian
    bin_file.write(a.to_bytes(4, 'little'))

with open('binary2','br')as bin_file:
    e = int.from_bytes(bin_file.read(2),'big')
    print(e)
    f= int.from_bytes(bin_file.read(2), 'big')
    print(f)
    g= int.from_bytes(bin_file.read(4), 'big')
    print(g)
    h= int.from_bytes(bin_file.read(4), 'big')
    print(h)
    i= int.from_bytes(bin_file.read(4), 'big')
    print(i)

f = open('flag.enc', 'rb').read()
b = bytearray(f)
i = len(b)-1
o = ''
while i>0:
    res = ((b[i]) + (b[i-1])) 
    b[i-1] = (((b[i]) + (b[i-1])) & 255)
    o += chr(res & 255)
    i-=1
open('flag.zip', 'wb').write(o[::-1])
import framebuf

def __init__(self, a,b,fb,i):
    self.conversion = conversion(a,b,fb,i)
    self.buf = bytearray(128 * 296 // 8)
    self.fb = framebuf.FrameBuffer(buf, 128, 296, framebuf.MONO_HLSB)

    
##each number has 32 pixels on xplan and 32 pixels on yplan
def space(a,b,fb):
    pass


def number_1(a,b,fb):
    for i in range(32):
        fb.hline(13+a,i+b, 6, 0)
        i+=1

def number_2(a,b,fb):
    for i in range(32):
        fb.hline(13+a,i+b, 6, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,13+i+b, 32, 0)
        i+=1

def number_3(a,b,fb):
    for i in range(32):
        fb.hline(13+a,i+b, 6, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,13+i+b, 32, 0)
        i+=1
    for i in range(32):
        fb.hline(1+a,i+b, 6, 0)
        i+=1

def number_4(a,b,fb):
    for i in range(32):
        fb.hline(13+a,i+b, 6, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,13+i+b, 32, 0)
        i+=1
    for i in range(32):
        fb.hline(1+a,i+b, 6, 0)
        i+=1
    for i in range(32):
        fb.hline(26+a,i+b, 6, 0)
        i+=1

def number_5(a,b,fb):
    for i in range(32):
        fb.hline(13+a,i+b, 6, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,13+i+b, 32, 0)
        i+=1
    for i in range(32):
        fb.hline(1+a,i+b, 6, 0)
        i+=1
    for i in range(32):
        fb.hline(26+a,i+b, 6, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,i+b, 32, 0)
        i+=1

def number_6(a,b,fb):
    for i in range(32):
        fb.hline(13+a,i+b, 6, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,13+i+b, 32, 0)
        i+=1
    for i in range(32):
        fb.hline(1+a,i+b, 6, 0)
        i+=1
    for i in range(32):
        fb.hline(26+a,i+b, 6, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,i+b, 32, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,26+i+b, 32, 0)
        i+=1

def number_7(a,b,fb):
    for i in range(32):
        fb.hline(13+a,i+b, 6, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,13+i+b, 32, 0)
        i+=1
    for i in range(32):
        fb.hline(1+a,i+b, 6, 0)
        i+=1
    for i in range(32):
        fb.hline(26+a,i+b, 6, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,i+b, 32, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,26+i+b, 32, 0)
        i+=1
    for i in range(32):
        fb.hline(45+a,i+b, 6, 0)
        i+=1

def number_8(a,b,fb):
    for i in range(32):
        fb.hline(13+a,i+b, 6, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,13+i+b, 32, 0)
        i+=1
    for i in range(32):
        fb.hline(1+a,i+b, 6, 0)
        i+=1
    for i in range(32):
        fb.hline(26+a,i+b, 6, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,i+b, 32, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,26+i+b, 32, 0)
        i+=1
    for i in range(32):
        fb.hline(45+a,i+b, 6, 0)
        i+=1
    for i in range(6):
        fb.hline(32+a,13+i+b, 32, 0)
        i+=1

def number_9(a,b,fb):
    for i in range(32):
        fb.hline(13+a,i+b, 6, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,13+i+b, 32, 0)
        i+=1
    for i in range(32):
        fb.hline(1+a,i+b, 6, 0)
        i+=1
    for i in range(32):
        fb.hline(26+a,i+b, 6, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,i+b, 32, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,26+i+b, 32, 0)
        i+=1
    for i in range(32):
        fb.hline(45+a,i+b, 6, 0)
        i+=1
    for i in range(6):
        fb.hline(32+a,13+i+b, 32, 0)
        i+=1
    for i in range(32):
        fb.hline(58+a,i+b, 6, 0)
        i+=1

def number_0(a,b,fb):
    for i in range(32):
        fb.hline(1+a,i+b, 6, 0)
        i+=1
    for i in range(32):
        fb.hline(26+a,i+b, 6, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,i+b, 32, 0)
        i+=1
    for i in range(6):
        fb.hline(1+a,26+i+b, 32, 0)
        i+=1
    

def conversion(a,b,fb,number):
    number = str(number)
    a = str(a)
    b = str(b)
    liste_noms_symbols = ["space", "point","number_0", "number_1", "number_2", "number_3", "number_4", "number_5", "number_6", "number_7", "number_8", "number_9"]
    liste_symbols = [" ", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in liste_symbols:
        if i == number:
            phrasi = liste_noms_symbols[liste_symbols.index(i)] + "(" + a + "," + b + "," + "fb" +")"   
    convert = eval(phrasi)
    return convert


import epaper4in2
from machine import I2C, Pin, SPI

###spi 2 on pyboard
sck = Pin('Y6')
miso = Pin('Y7')
mosi = Pin('Y8')
dc = Pin('Y4')
cs = Pin('Y5')
rst = Pin('Y3')
busy = Pin('Y2')
spi = SPI(2, baudrate=20000000, polarity=0, phase=0, bits=8)
e = epaper4in2.EPD(spi, cs, dc, rst, busy)
e.init()
w = 400
h = 300
x = 0
y = 0
import framebuf
buf = bytearray(w * h // 8)
fb = framebuf.FrameBuffer(buf, w, h, framebuf.MONO_HLSB)
black = 0
white = 1

def affichage(numbers,a,b):
    numbers = str(numbers)  
    sautx_8 = [" ", "/", "."]
    sautx_10 = [":"]
    sautx_11 = ["%", "C", "H", "M", "T", "V", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in numbers:
        i = str(i)
        if i in sautx_8:
            ft.conversion(a,b,fb,i)
            a += 8
        if i in sautx_10:
            ft.conversion(a,b,fb,i)
            a += 10
        if i in sautx_11:
            ft.conversion(a,b,fb,i)
            a += 11

fb.fill(white)

affichage("Test",15,40)
e.display_frame(buf)


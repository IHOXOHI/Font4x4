import epaper4in2
from machine import I2C, Pin, SPI
from time import sleep
import NewFont2 as ft

#SPI on Arduino Giga R1
sck = Pin('PH6')
miso = Pin('PJ11')
mosi = Pin('PJ10')
dc = Pin('PB9')
cs = Pin('PK1')
rst = Pin('PB8')
busy = Pin('PB4')
spi = SPI(1, baudrate=20000000, polarity=0, phase=0, bits=8)

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
    sautx_8 = [" ", "."]
    sautx_11 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in numbers:
        i = str(i)
        if i in sautx_8:
            ft.conversion(a,b,fb,i)
            a += 8
        if i in sautx_11:
            ft.conversion(a,b,fb,i)
            a += 70

while 1:
   
    fb.fill(white)
    affichage("1234",20,0)
    affichage("5",0,50)
    affichage("6",0,100)
    affichage("78",0,150)
    affichage("90",0,200)

    e.display_frame(buf)
    sleep(30)




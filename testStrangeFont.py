from machine import I2C
import sh1107


i2c = I2C(1,freq=400000)
display = sh1107.SH1107_I2C(128, 128, i2c, address=0x3c, rotate=90)


def test():  
    display.sleep(False)
    display.flip()
    display.invert()
    display.fill(0)
    b = 5
    for i in range(8):
        display.text(str(i), 5, b, 1)
        b += 15
    display.vline(1,1,128,1)
    display.hline(0,128,128,1)
    display.fill_rect(20, 20,80,50, 1)
    display.text('IHOXOHI', 25, 25, 0)
    for i in range(1,12,2):
        display.vline(30+i,40,30,0)
        display.hline(50,50+i,50,0)
    
    
    
    number_8(20,80,display)
    
    
    display.show()
    

def number_8(a,b,display):
    for i in range(32):
        display.hline(13+a,i+b, 6, 1)
        i+=1
    for i in range(6):
        display.hline(1+a,13+i+b, 32, 1)
        i+=1
    for i in range(32):
        display.hline(1+a,i+b, 6, 1)
        i+=1
    for i in range(32):
        display.hline(26+a,i+b, 6, 1)
        i+=1
    for i in range(6):
        display.hline(1+a,i+b, 32, 1)
        i+=1
    for i in range(6):
        display.hline(1+a,26+i+b, 32, 1)
        i+=1
    for i in range(32):
        display.hline(45+a,i+b, 6, 1)
        i+=1
    for i in range(6):
        display.hline(32+a,13+i+b, 32, 1)
        i+=1

        i+=1
        
test()

import serial.tools.list_ports
import pyautogui
import pydirectinput
import threading
x1=0
x2=0
y1=0
y2=0
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []
for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

serialInst.baudrate=9600
serialInst.port = "COM3"
serialInst.open()

def keyboardMove():
    if (int(linea) == 1):
            #print("w presionado")
            pydirectinput.keyDown("w")
    if (int(linea) == -1):
            #print("w no presionado")
            pydirectinput.keyUp("w")
    if (int(linea) == 2):
            #print("space presionado")
            pydirectinput.keyDown("space")
    if (int(linea) == -2):
            #print("space no presionado")
            pydirectinput.keyUp("space")

def mouseMove():
        global x1
        global x2
        global y1
        global y2
        if (int(linea) == 31):
            pydirectinput.mouseDown(button="left")
        elif (int(linea) == -3):
            pydirectinput.mouseUp(button="left")
        if (int(linea) == 4):
            #print("pulgar abajo")
            pydirectinput.moveRel(x1,0,relative=True,_pause=False)
            #print("x=",x," ","y=",y )
            x1=x1-1
            #print(x1)
        elif (int(linea) == -4):
            x1=0
        if (int(linea) == 5):
            #print("pulgar abajo")
            pydirectinput.moveRel(x2,0,relative=True,_pause=False)
            #print("x=",x," ","y=",y )
            x2=x2+1
        elif (int(linea) == -5):
            x2=0
        if (int(linea) == 6):
            #print("pulgar abajo")
            pydirectinput.moveRel(0,y1,relative=True,_pause=False)
            #print("x=",x," ","y=",y )
            y1=y1-1
        elif (int(linea) == -6):
            y1=0
        if (int(linea) == 7):
            #print("pulgar abajo")
            pydirectinput.moveRel(0,y2,relative=True,_pause=False)
            #print("x=",x," ","y=",y )
            y2=y2+1
        elif (int(linea) == -7):
            y2=0
while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        linea = packet.decode("utf-8")
        print(linea)
        keyboard = threading.Thread(target=keyboardMove,args=())
        mouse = threading.Thread(target=mouseMove,args=())
        keyboard.start()
        mouse.start()
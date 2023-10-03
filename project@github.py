import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

lcd_rs = 18
lcd_en = 19
lcd_d4 = 10
lcd_d5 = 11
lcd_d6 = 12
lcd_d7 = 13

ledA = 6
ledB = 7
ledC = 8
ledD = 9
ULT1 = 2
ULT2 = 3
ULT3 = 4
ULT4 = 5
fanA1 = 14
fanA2 = 15
fanB1 = 16
fanB2 = 17
cm1 = 0
cm2 = 0
cm3 = 0
cm4 = 0
A = 0
B = 0
C = 0
D = 0
E = 0

GPIO.setup(lcd_rs, GPIO.OUT)
GPIO.setup(lcd_en, GPIO.OUT)
GPIO.setup(lcd_d4, GPIO.OUT)
GPIO.setup(lcd_d5, GPIO.OUT)
GPIO.setup(lcd_d6, GPIO.OUT)
GPIO.setup(lcd_d7, GPIO.OUT)

GPIO.setup(ledA, GPIO.OUT)
GPIO.setup(ledB, GPIO.OUT)
GPIO.setup(ledC, GPIO.OUT)
GPIO.setup(ledD, GPIO.OUT)
GPIO.setup(ULT1, GPIO.OUT)
GPIO.setup(ULT2, GPIO.OUT)
GPIO.setup(ULT3, GPIO.OUT)
GPIO.setup(ULT4, GPIO.OUT)
GPIO.setup(fanA1, GPIO.OUT)
GPIO.setup(fanA2, GPIO.OUT)
GPIO.setup(fanB1, GPIO.OUT)
GPIO.setup(fanB2, GPIO.OUT)

def bacaULT1(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.002)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(pin, GPIO.LOW)
    GPIO.setup(pin, GPIO.IN)
    return GPIO.pulseIn(pin, GPIO.HIGH)

def bacaULT2(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.002)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(pin, GPIO.LOW)
    GPIO.setup(pin, GPIO.IN)
    return GPIO.pulseIn(pin, GPIO.HIGH)

def bacaULT3(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.002)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(pin, GPIO.LOW)
    GPIO.setup(pin, GPIO.IN)
    return GPIO.pulseIn(pin, GPIO.HIGH)
    cpp
import time

def bacaULT4(pin):
    pinMode(pin, OUTPUT)
    digitalWrite(pin, LOW)
    time.sleep(0.000002)
    digitalWrite(pin, HIGH)
    time.sleep(0.00001)
    digitalWrite(pin, LOW)
    pinMode(pin, INPUT)
    
    return pulseIn(pin, HIGH)

def setup():
    lcd.begin(16, 2)
    
    lcd.print("Bilik Tersedia:")
    pinMode(ULT1, INPUT)
    pinMode(ULT2, INPUT)
    pinMode(ULT3, INPUT)
    pinMode(ULT4, INPUT)
    pinMode(ledA, OUTPUT)
    pinMode(ledB, OUTPUT)
    pinMode(ledC, OUTPUT)
    pinMode(ledD, OUTPUT)
    pinMode(fanA1, OUTPUT)
    pinMode(fanA2, OUTPUT)
    pinMode(fanB1, OUTPUT)
    pinMode(fanB2, OUTPUT)
    Serial.begin(9600)

def loop():
    cm1 = 0.01723 * bacaULT1(ULT1)
    cm2 = 0.01723 * bacaULT1(ULT2)
    cm3 = 0.01723 * bacaULT1(ULT3)
    cm4 = 0.01723 * bacaULT1(ULT4)
    if cm1 <= 250:
        digitalWrite(ledA, HIGH)
        A = 1
    if cm1 >= 251:
        digitalWrite(ledA, LOW)
        A = 0
    if cm2 <= 250:
        digitalWrite(ledB, HIGH)
        B = 1
    if cm2 >= 251:
        digitalWrite(ledB, LOW)
        B = 0
    if cm3 <= 250:
        digitalWrite(ledC, HIGH)
        C = 1
    if cm3 >= 251:
        digitalWrite(ledC, LOW)
        C = 0
    if cm4 <= 250:
        digitalWrite(ledD, HIGH)
        D = 1
        if cm4 >= 251:
    digitalWrite(ledD, LOW)
    D = 0
E = A + B + C + D
if E == 1:
    digitalWrite(fanA1, HIGH)
    digitalWrite(fanA2, HIGH)
    digitalWrite(fanB1, HIGH)
    digitalWrite(fanB2, HIGH)
    lcd.setCursor(7, 1)
    lcd.print("3")
if E == 2:
    digitalWrite(fanA1, LOW)
    digitalWrite(fanA2, HIGH)
    digitalWrite(fanB1, HIGH)
    digitalWrite(fanB2, HIGH)
    lcd.setCursor(7, 1)
    lcd.print("2")
if E == 3:
    digitalWrite(fanA1, LOW)
    digitalWrite(fanA2, HIGH)
    digitalWrite(fanB1, HIGH)
    digitalWrite(fanB2, HIGH)
    lcd.setCursor(7, 1)
    lcd.print("1")
if E == 4:
    digitalWrite(fanA1, LOW)
    digitalWrite(fanA2, HIGH)
    digitalWrite(fanB1, LOW)
    digitalWrite(fanB2, HIGH)
    lcd.setCursor(7, 1)
    lcd.print("0")
if E == 0:
    digitalWrite(ledA, LOW)
    digitalWrite(ledB, LOW)
    digitalWrite(ledC, LOW)
    digitalWrite(ledD, LOW)
    digitalWrite(fanA1, HIGH)
    digitalWrite(fanA2, HIGH)
    digitalWrite(fanB1, HIGH)
    digitalWrite(fanB2, HIGH)
    lcd.setCursor(7, 1)
    lcd.print("4")
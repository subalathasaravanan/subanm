#include <LiquidCrystal.h>
LiquidCrystal lcd(18, 19, 10, 11, 12, 13);
int ledA = 6;
int ledB = 7;
int ledC = 8;
int ledD = 9;
int ULT1 = 2;
int ULT2 = 3;
int ULT3 = 4;
int ULT4 = 5;
int fanA1 = 14;
int fanA2 = 15;
int fanB1 = 16;
int fanB2 = 17;
int cm1 = 0;
int cm2 = 0;
int cm3 = 0;
int cm4 = 0;
int A,B,C,D,E;
long bacaULT1(int pin)
{
  pinMode(pin, OUTPUT);  // Clear the trigger
  digitalWrite(pin, LOW);
  delayMicroseconds(2);
  // Sets the pin on HIGH state for 10 micro seconds
  digitalWrite(pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(pin, LOW);
  pinMode(pin, INPUT);
  // Reads the pin, and returns the sound wave travel time in microseconds
  return pulseIn(pin, HIGH);
}
long bacaULT2(int pin)
{
  pinMode(pin, OUTPUT);  // Clear the trigger
  digitalWrite(pin, LOW);
  delayMicroseconds(2);
  digitalWrite(pin, HIGH);// Sets the pin on HIGH state for 10 microseconds
  delayMicroseconds(10);
  digitalWrite(pin, LOW);
  pinMode(pin, INPUT);
  // Reads the pin, and returns the sound wave travel time in microseconds
  return pulseIn(pin, HIGH);
}
long bacaULT3(int pin)
{
  pinMode(pin, OUTPUT);  // Clear the trigger
  digitalWrite(pin, LOW);
  delayMicroseconds(2);
  digitalWrite(pin, HIGH);// Sets the pin on HIGH state for 10 micro seconds
  delayMicroseconds(10);
  digitalWrite(pin, LOW);
  pinMode(pin, INPUT);
  // Reads the pin, and returns the sound wave travel time in microseconds
  return pulseIn(pin, HIGH);
}
long bacaULT4(int pin)
{
  pinMode(pin, OUTPUT);  // Clear the trigger
  digitalWrite(pin, LOW);
  delayMicroseconds(2);
  digitalWrite(pin, HIGH);// Sets the pin on HIGH state for 10 micro seconds
  delayMicroseconds(10);
  digitalWrite(pin, LOW);
  pinMode(pin, INPUT);
  // Reads the pin, and returns the sound wave travel time in microseconds
  return pulseIn(pin, HIGH);
}

void setup()
{
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("Bilik Tersedia:");
  pinMode(ULT1, INPUT);
  pinMode(ULT2, INPUT);
  pinMode(ULT3, INPUT);
  pinMode(ULT4, INPUT);
  pinMode(ledA, OUTPUT);
  pinMode(ledB, OUTPUT);
  pinMode(ledC, OUTPUT);
  pinMode(ledD, OUTPUT);
  pinMode(fanA1, OUTPUT);
  pinMode(fanA2, OUTPUT);
  pinMode(fanB1, OUTPUT);
  pinMode(fanB2, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  cm1 = 0.01723 * bacaULT1(ULT1); // measure the ping time in cm
  cm2 = 0.01723 * bacaULT1(ULT2);
  cm3 = 0.01723 * bacaULT1(ULT3);
  cm4 = 0.01723 * bacaULT1(ULT4);
  	if (cm1<=250)
    	{digitalWrite(ledA, HIGH);A=1;}
  	if (cm1>=251)
      	{digitalWrite(ledA, LOW);A=0;}
  	if (cm2<=250)
   		{digitalWrite(ledB, HIGH);B=1;}
  	if (cm2>=251)
   		{digitalWrite(ledB, LOW);B=0;}
  	if (cm3<=250)
    	{digitalWrite(ledC, HIGH);C=1;}
  	if (cm3>=251)
    	{digitalWrite(ledC, LOW);C=0;}
  	if (cm4<=250)
    	{digitalWrite(ledD, HIGH);D=1;}
  	if (cm4>=251)
    	{digitalWrite(ledD, LOW);D=0;}
  E=A+B+C+D;
    if (E==1){
       digitalWrite(fanA1,HIGH);
       digitalWrite(fanA2,HIGH);
       digitalWrite(fanB1,HIGH);
       digitalWrite(fanB2,HIGH);
       lcd.setCursor(7, 1);
       // Print a message to the LCD.
       lcd.print("3");}
  if (E==2){
       digitalWrite(fanA1,LOW);
       digitalWrite(fanA2,HIGH);
       digitalWrite(fanB1,HIGH);
       digitalWrite(fanB2,HIGH);
       lcd.setCursor(7, 1);
       // Print a message to the LCD.
       lcd.print("2");}
  if (E==3){
       digitalWrite(fanA1,LOW);
       digitalWrite(fanA2,HIGH);
       digitalWrite(fanB1,HIGH);
       digitalWrite(fanB2,HIGH);
       lcd.setCursor(7, 1);
       // Memunculkan Nilai Pada LCD
       lcd.print("1");}
  if (E==4){
       digitalWrite(fanA1,LOW);
       digitalWrite(fanA2,HIGH);
       digitalWrite(fanB1,LOW);
       digitalWrite(fanB2,HIGH);
       lcd.setCursor(7, 1);
       // Memunculkan Nilai Pada LCD
       lcd.print("0");}
  if (E==0){
       digitalWrite(ledA,LOW);
       digitalWrite(ledB,LOW);
       digitalWrite(ledC,LOW);
       digitalWrite(ledD,LOW);
       digitalWrite(fanA1,HIGH);
       digitalWrite(fanA2,HIGH);
       digitalWrite(fanB1,HIGH);
       digitalWrite(fanB2,HIGH);
       lcd.setCursor(7, 1);
       // Memunculkan Nilai Pada LCD
       lcd.print("4");}
}
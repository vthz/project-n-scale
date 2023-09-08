/*
snshohin@gmail.com
6th August 2023
*/

int serialByte = 0;
bool led1 = false;
bool led2 = false;
bool led3 = false;

int ledPin1 = 3;
int ledPin2 = 4;
int ledPin3 = 5;
int ledPin4 = 6;
int analogPin1 = A0;

void setup() {
    Serial.begin(9600);
    pinMode(ledPin1, OUTPUT);
    pinMode(ledPin2, OUTPUT);
    pinMode(ledPin3, OUTPUT);
    pinMode(ledPin4, OUTPUT);
}

void loop() {
    if(Serial.available()>0){
      serialByte = Serial.read();
    }
    
    switch(serialByte){
      case 0:
            if (led1==false){
              led1=true;
              digitalWrite(ledPin1, HIGH);
            }
            else if (led1==true){
              led1=false;
              digitalWrite(ledPin1, LOW);
            }
            break;
      case 1:
            if (led2==false){
              led2=true;
              digitalWrite(ledPin2, HIGH);
            }
            else if (led2==true){
              led2=false;
              digitalWrite(ledPin2, LOW);
            }
            break;
      case 2:
            if (led3==false){
              led3=true;
              digitalWrite(ledPin3, HIGH);
            }
            else if (led3==true){
              led3=false;
              digitalWrite(ledPin3, LOW);
            }
            break;
    }
    
    if (serialByte>=10 && serialByte <=20){
      int brightness = map(serialByte, 10, 20, 0, 255);
      analogWrite(ledPin4, brightness);
    }
}

#include <Servo.h>
int led1 = 52;
int led2 = 50;
int op;

Servo  servo;

String dataString = "";
bool dataComplete = true;
int data = 0;


void setup() {
  Serial.begin(9600);
  servo.attach(48);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  servo.write(0);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    op = Serial.read();
    if(op=='S'){
      autorizado();
    }
    if(op=='N'){
      N_autorizado();
    }
  }
}


void autorizado(){
  servo.write(95);
  digitalWrite(led1, HIGH);
  digitalWrite(led2, LOW);
  delay(2500);
  digitalWrite(led1, LOW);
  servo.write(0);
}

void N_autorizado(){
  digitalWrite(led1, LOW);
  digitalWrite(led2, HIGH);
  delay(2500);
  digitalWrite(led2, LOW);
}

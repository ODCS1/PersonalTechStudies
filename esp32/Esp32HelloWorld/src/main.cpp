#include <Arduino.h>

const int ledPinGeral = 12;
const int ledPinCampo = 21;

void setup() {

  pinMode(ledPinGeral, OUTPUT);
  pinMode(ledPinCampo, OUTPUT);
  Serial.begin(9600);
  Serial.println("Hello World!");
}

void loop() {

  digitalWrite(ledPinGeral, HIGH);
  digitalWrite(ledPinCampo, HIGH);
  Serial.println("Hello World!");
  delay(4000); 
  

  digitalWrite(ledPinGeral, LOW);
  digitalWrite(ledPinCampo, LOW);
  delay(4000); 
// }
}
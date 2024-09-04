#include <Arduino.h>

const int ledPin = 12;
const int blue = 21;
const int green = 22;

void setup() {

  pinMode(ledPin, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(green, OUTPUT);
  Serial.begin(9600);
  Serial.println("Hello World!");
}

void loop() {

  digitalWrite(ledPin, HIGH);
  digitalWrite(blue, HIGH);
  digitalWrite(green, LOW);
  Serial.println("Hello World!");
  delay(1000); 
  

  digitalWrite(ledPin, LOW);
  digitalWrite(blue, LOW);
  digitalWrite(green, HIGH);
  delay(1000); 
}
#include <Arduino.h>
#include <Servo.h>

// SERVO PORTÃO
Servo myServo;
const int servoPin = 11;

// VALORES PWM PARA CONTROLAR O ÂNGULO DO SERVO
const int stopSignal = 115;
const int openSignal = 180;
const int closeSignal = 115;

// VARIÁVEL PARA ARMAZENAR O ESTADO ATUAL (0 = FECHADO, 1 = ABERTO)
int currentState = 0;

void setup() {
  myServo.attach(servoPin);
  myServo.write(stopSignal);

  Serial.begin(9600);
  Serial.println("Digite 1 para abrir o portão ou 0 para fechar:");
}

void loop() {
  if (Serial.available() > 0) {
    int command = Serial.parseInt();

    // VALIDA O COMANDO E SE ESTÁ JÁ NO ESTADO DESEJADO
    if (command == 1 && currentState == 0) {
      // ABRIR
      Serial.println("Abrindo o portão...");
      myServo.write(openSignal); 
      currentState = 1;   
    } else if (command == 0 && currentState == 1) {

      Serial.println("Fechando o portão...");
      myServo.write(closeSignal);
      currentState = 0;
    } else {
      Serial.println("Comando inválido ou já está nesse estado.");
    }
  }
}

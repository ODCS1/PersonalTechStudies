#include <Arduino.h>
#include <Servo.h>

// SERVO PORTÃO

Servo myServo;
const int servoPin = 11;


// VALORES PWM PARA CONTROLE DO SERVO CONTINUO
const int stopSignal = 90;   // PARAR O SERVO
const int openSignal = 120;  // SENTIDO HORÁRIO PARA ABRIR
const int closeSignal = 50;  // SENTIDO ANTI-HORÁRIO PARA FECHAR


// VARIÁVEL PARA ARMAZENAR O ESTADO ATUAL (0 = FECHADO, 1 = ABERTO)
int currentState = 0;

// Tempo de rotação para 90°
// TEMPO DE ROTAÇÃO PARA 90°
const int openRotationTime = 350;
const int closeRotationTime = 250;

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
      delay(openRotationTime);
      myServo.write(stopSignal);
      currentState = 1;
    } else if (command == 0 && currentState == 1) {
      // Fechar o portão
      Serial.println("Fechando o portão...");
      myServo.write(closeSignal);
      delay(closeRotationTime);
      myServo.write(stopSignal);
      currentState = 0;
    } else {
      Serial.println("Comando inválido ou já está nesse estado.");
    }
  }
}
#include <Arduino.h>
const int led1 = 2; // jardim frente direita (OK)
const int led2 = 3; // jardim frente esquerda (OK)
const int led3 = 4; // jardim lateral (OK)
const int led4 = 5; // sala de estar   [FRACO]
const int led5 = 6; // lavanderia      [FRACO] 
const int led6 = 7; // sala de jantar  [FRACO]
const int led7 = 8; // lavabo          [FRACO]
const int led8 = 9; // cozinha         [MUITO FRACO]
const int led9 = 10; // sala tv (OK)
const int led10 = 11; // quarto 2 (MASTER) (OK)
const int led11 = 12; // banheiro (OK)
const int led12 = 13; // quarto 1 (OK)
const int led13 = A5; // jardim atrás (OK)

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(led6, OUTPUT);
  pinMode(led7, OUTPUT);
  pinMode(led8, OUTPUT);
  pinMode(led9, OUTPUT);
  pinMode(led10, OUTPUT);
  pinMode(led11, OUTPUT);
  pinMode(led12, OUTPUT);
  pinMode(led13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        char command = Serial.read();

        switch (command) {
            case '0':
                digitalWrite(led1, HIGH);
                break;
            case '1':
                digitalWrite(led1, LOW);
                break;
            case '2':
                digitalWrite(led2, HIGH);
                break;
            case '3':
                digitalWrite(led2, LOW);
                break;
            case '4':
                digitalWrite(led3, HIGH);
                break;
            case '5':
                digitalWrite(led3, LOW);
                break;
            case '6':
                digitalWrite(led4, HIGH);
                break;
            case '7':
                digitalWrite(led4, LOW);
                break;
            case '8':
                digitalWrite(led5, HIGH);
                break;
            case '9':
                digitalWrite(led5, LOW);
                break;
            case 'q':
                digitalWrite(led6, HIGH);
                break;
            case 'w':
                digitalWrite(led6, LOW);
                break;
            case 'e':
                digitalWrite(led7, HIGH);
                break;
            case 'r':
                digitalWrite(led7, LOW);
                break;
            case 't':
                digitalWrite(led8, HIGH);
                break;
            case 'y':
                digitalWrite(led8, LOW);
                break;
            case 'u':
                digitalWrite(led9, HIGH);
                break;
            case 'i':
                digitalWrite(led9, LOW);
                break;
            case 'o':
                digitalWrite(led10, HIGH);
                break;
            case 'p':
                digitalWrite(led10, LOW);
                break;
            case 'a':
                digitalWrite(led11, HIGH);
                break;
            case 's':
                digitalWrite(led11, LOW);
                break;
            case 'd':
                digitalWrite(led12, HIGH);
                break;
            case 'f':
                digitalWrite(led12, LOW);
                break;
            case 'g':
                analogWrite(led13, 180);
                break;
            case 'h':
                analogWrite(led13, 0);
                break;
            default:
                break;
        }
    }
}

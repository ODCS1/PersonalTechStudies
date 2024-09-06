#include <Arduino.h>

// 4 LEDS
// {blue, green, red}

int leds[4][3] = {
    {12, 13, 14},
    {27, 26, 25},
    {33, 32, 35},
    {21, 19, 18}
};

void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 4; i++){
    ledcAttachPin();
  }
}

void loop() {
  // put your main code here, to run repeatedly:
}

// put function definitions here:
void turnOnLedStyle(){

}
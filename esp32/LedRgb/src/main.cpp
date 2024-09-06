#include <Arduino.h>

const int redPin1 = 21;
const int greenPin1 = 19;
const int bluePin1 = 18;

const int redPin = 27;
const int greenPin = 26;
const int bluePin = 25;


const int redChannel1 = 0;
const int greenChannel1 = 1;
const int blueChannel1 = 2;

const int redChannel = 0;
const int greenChannel = 1;
const int blueChannel = 2;

const int freq1 = 40000;
const int freq = 500;
const int resolution = 8;

void setup() {
  // put your setup code here, to run once:

  ledcSetup(redChannel1, freq1, resolution);
  ledcSetup(greenChannel1, freq1, resolution);
  ledcSetup(blueChannel1, freq1, resolution);

  ledcAttachPin(redPin1, redChannel);
  ledcAttachPin(greenPin1, greenChannel);
  ledcAttachPin(bluePin1, blueChannel); 

  ledcSetup(redChannel, freq, resolution);
  ledcSetup(greenChannel, freq, resolution);
  ledcSetup(blueChannel, freq, resolution);

  ledcAttachPin(redPin, redChannel);
  ledcAttachPin(greenPin, greenChannel);
  ledcAttachPin(bluePin, blueChannel); 
}

void setColor(int red, int green, int blue){
  ledcWrite(redChannel1, red);
  ledcWrite(greenChannel1, green);
  ledcWrite(blueChannel1, blue);
  ledcWrite(redChannel, red);
  ledcWrite(greenChannel, green);
  ledcWrite(blueChannel, blue);
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:

  setColor(255, 0, 0); // RED
  setColor(0, 255, 0); // GREEN
  setColor(0, 0, 255); // BLUE

  setColor(255, 255, 0); // YELLOW
  setColor(80, 0, 80); // PURPLE
  setColor(0, 255, 255); // CYAN
}
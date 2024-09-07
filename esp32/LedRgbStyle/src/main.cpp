// #include <Arduino.h>

// // 4 LEDs
// // {blue, green, red}
// int leds[4][3] = {
//     {12, 13, 14},
//     {27, 26, 25},
//     {33, 32, 15},
//     {21, 19, 18}
// };

// int const led_Channels[4][3] = {
//     {0, 1, 2},
//     {3, 4, 5},
//     {6, 7, 8},
//     {9, 10, 11}
// };

// const int qtd_led = 4;
// const int freq = 20000;
// int resolution = 8;
// int intensidade_led = 255;

// void setup() {
//   Serial.begin(9600);

//   for (int i = 0; i < qtd_led; i++){
//     for (int j = 0; j < 3; j++){
//       pinMode(leds[i][j], OUTPUT);

//       ledcSetup(led_Channels[i][j], freq, resolution);

//       ledcAttachPin(leds[i][j], led_Channels[i][j]);
//     }
//   }
// }

// void apagar() {
//   // Turn off all LEDs
//   for (int i = 0; i < qtd_led; i++){
//     for (int j = 0; j < 3; j++){
//       ledcWrite(led_Channels[i][j], 0);
//     }
//   }
// }

// void natal() {
//   const int numCycles = 10;
//   const int delayTime = 300;

//   int colors[3][3] = {
//     {255, 0, 0},
//     {0, 255, 0},
//     {0, 0, 255} 
//   };

//   for (int i = 0; i < numCycles; i++) {

//     for (int colorIndex = 0; colorIndex < 3; colorIndex++) {
//       for (int intensity = 0; intensity <= 255; intensity += 5) {
//         for (int j = 0; j < qtd_led; j++) {
//           for (int k = 0; k < 3; k++) {
//             int pwmValue = map(intensity, 0, 255, 0, 255);
//             ledcWrite(led_Channels[j][k], pwmValue);
//           }
//         }


//         for (int j = 0; j < qtd_led; j++) {
//           ledcWrite(led_Channels[j][0], colors[colorIndex][0]);
//           ledcWrite(led_Channels[j][1], colors[colorIndex][1]); 
//           ledcWrite(led_Channels[j][2], colors[colorIndex][2]);
//         }

//         delay(delayTime / 10);
//       }

//       for (int intensity = 255; intensity >= 0; intensity -= 5) {
//         for (int j = 0; j < qtd_led; j++) {
//           for (int k = 0; k < 3; k++) {
//             int pwmValue = map(intensity, 0, 255, 0, 255);
//             ledcWrite(led_Channels[j][k], pwmValue);
//           }
//         }

//         for (int j = 0; j < qtd_led; j++) {
//           ledcWrite(led_Channels[j][0], colors[colorIndex][0]); // Red
//           ledcWrite(led_Channels[j][1], colors[colorIndex][1]); // Green
//           ledcWrite(led_Channels[j][2], colors[colorIndex][2]); // Blue
//         }

//         delay(delayTime / 10);
//       }
//     }
//   }

//   apagar();
// }



// void seguranca() {
//   for (int i = 0; i < qtd_led; i++) {
//     for (int j = 0; j < 3; j++) {
//       ledcWrite(led_Channels[i][j], 255);
//     }
//   }
// }



// void intensidade() {
//   Serial.println("Digite a intensidade de 0 a 100:");
  
//   while (Serial.available() == 0) {
//     // ESPERA UMA ENTRADA
//   }

//   String input = Serial.readStringUntil('\n');
//   int intensidade = input.toInt();

//   // TRANSFORMANDO PARA VALOR PWM
//   intensidade_led = map(intensidade, 0, 100, 0, 255);

//   for (int i = 0; i < qtd_led; i++) {
//     for (int j = 0; j < 3; j++) {
//       ledcWrite(led_Channels[i][j], intensidade_led);
//     }
//   }

//   Serial.print("Intensidade ajustada para: ");
//   Serial.println(intensidade_led);
// }

// void loop() {
//   Serial.println("Escolha a sua opção:");
//   Serial.println("[1] Natal - [2] Segurança - [3] Apagar - [4] Intensidade");

//   while (Serial.available() == 0) {
//     // ESPERA UMA ENTRADA
//   }

//   char opcao = Serial.read();

//   Serial.println("Você escolheu:");
//   switch (opcao) {
//     case '1':
//       Serial.println("Natal");
//       natal();
//       break;
//     case '2':
//       Serial.println("Segurança");
//       seguranca();
//       break;
//     case '3':
//       Serial.println("Apagar");
//       apagar();
//       break;
//     case '4':
//       Serial.println("Intensidade");
//       intensidade();
//       break;
//     default:
//       Serial.println("Opção inválida. Tente novamente.");
//       break;
//   }

//   delay(100);
// }


#include <Arduino.h>

// 4 LEDs
// {blue, green, red}
int leds[4][3] = {
    {12, 13, 14},
    {27, 26, 25},
    {33, 32, 15},
    {21, 19, 18}
};

int const led_Channels[4][3] = {
    {0, 1, 2},
    {3, 4, 5},
    {6, 7, 8},
    {9, 10, 11}
};

const int qtd_led = 4;
const int freq = 20000;
int resolution = 8;
int intensidade_led = 255;
TaskHandle_t natalTaskHandle = NULL;

bool natalRunning = false;

void setup() {
  Serial.begin(9600);

  for (int i = 0; i < qtd_led; i++){
    for (int j = 0; j < 3; j++){
      pinMode(leds[i][j], OUTPUT);

      ledcSetup(led_Channels[i][j], freq, resolution);

      ledcAttachPin(leds[i][j], led_Channels[i][j]);
    }
  }
}

void apagar() {
  for (int i = 0; i < qtd_led; i++){
    for (int j = 0; j < 3; j++){
      ledcWrite(led_Channels[i][j], 0);
    }
  }
}

void natal() {
  const int delayTime = 300;
  const int fadeTime = 10;
  int colors[3][3] = {
    {0, 0, 255},    // RED
    {0, 255, 0},    // GREEN
    {0, 215, 255}   // GOLD
  };

  while (natalRunning) {
    for (int colorIndex = 0; colorIndex < 3; colorIndex++) {

      for (int intensidade = 0; intensidade <= 255; intensidade += 5) {
        for (int j = 0; j < qtd_led; j++) {
          ledcWrite(led_Channels[j][0], (colors[colorIndex][0] * intensidade) / 255);
          ledcWrite(led_Channels[j][1], (colors[colorIndex][1] * intensidade) / 255);
          ledcWrite(led_Channels[j][2], (colors[colorIndex][2] * intensidade) / 255);
        }
        delay(fadeTime);
      }

      // FADE OUT
      for (int intensidade = 255; intensidade >= 0; intensidade -= 5) {
        for (int j = 0; j < qtd_led; j++) {
          ledcWrite(led_Channels[j][0], (colors[colorIndex][0] * intensidade) / 255);
          ledcWrite(led_Channels[j][1], (colors[colorIndex][1] * intensidade) / 255);
          ledcWrite(led_Channels[j][2], (colors[colorIndex][2] * intensidade) / 255);
        }
        delay(fadeTime);
      }

      delay(delayTime);
    }
  }
  apagar();
}

void startNatalTask() {
  natalRunning = true;
  xTaskCreatePinnedToCore(
    [](void *param) {
      natal();
      vTaskDelete(NULL);
    },
    "Natal Task", 4096, NULL, 1, &natalTaskHandle, 1
  );
}

void stopNatalTask() {
  natalRunning = false;
  if (natalTaskHandle != NULL) {
    vTaskDelete(natalTaskHandle);
    natalTaskHandle = NULL;
  }
  apagar();
}

void seguranca() {
  stopNatalTask();
  for (int i = 0; i < qtd_led; i++) {
    for (int j = 0; j < 3; j++) {
      ledcWrite(led_Channels[i][j], 255);
    }
  }
}

void intensidade() {
  stopNatalTask();
  Serial.println("Digite a intensidade de 0 a 100:");
  
  while (Serial.available() == 0) {
    // ESPERA UMA ENTRADA
  }

  String input = Serial.readStringUntil('\n');
  int intensidade = input.toInt();

  // TRANSFORMANDO PARA VALOR PWM
  intensidade_led = map(intensidade, 0, 100, 0, 255);

  for (int i = 0; i < qtd_led; i++) {
    for (int j = 0; j < 3; j++) {
      ledcWrite(led_Channels[i][j], intensidade_led);
    }
  }

  Serial.print("Intensidade ajustada para: ");
  Serial.println(intensidade_led);
}

void loop() {
  Serial.println("Escolha a sua opção:");
  Serial.println("[1] Natal - [2] Segurança - [3] Apagar - [4] Intensidade");

  while (Serial.available() == 0) {
    // ESPERA UMA ENTRADA
  }

  char opcao = Serial.read();

  Serial.println("Você escolheu:");
  switch (opcao) {
    case '1':
      Serial.println("Natal");
      if (natalTaskHandle == NULL) {
        startNatalTask();
      } else {
        Serial.println("O efeito de Natal já está rodando.");
      }
      break;
    case '2':
      Serial.println("Segurança");
      seguranca();
      break;
    case '3':
      Serial.println("Apagar");
      stopNatalTask();
      apagar();
      break;
    case '4':
      Serial.println("Intensidade");
      intensidade();
      break;
    default:
      Serial.println("Opção inválida. Tente novamente.");
      break;
  }

  delay(100);
}

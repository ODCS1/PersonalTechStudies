#define RXp2 16
#define TXp2 17

void setup() {
  // Inicializa a comunicação Serial padrão
  Serial.begin(115200);
  
  // Inicializa a comunicação Serial2 com os pinos e velocidade desejados
  Serial2.begin(9600, SERIAL_8N1, RXp2, TXp2);
}

void loop() {
  // Envia mensagem pela Serial padrão (USB)
  Serial.println("Message Received: ");
  
  // Lê dados da Serial2 e os imprime na Serial padrão
  if (Serial2.available()) {
    Serial.println(Serial2.readString());
  }
}

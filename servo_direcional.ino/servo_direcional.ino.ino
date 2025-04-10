#include <Servo.h>

Servo myservo;
int pos = 90; // Posição inicial (centro)
char ultimoComando = 'X'; // valor diferente dos comandos possíveis

void setup() {
  myservo.attach(9);
  Serial.begin(9600);
  myservo.write(pos);
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();

    if (comando != ultimoComando) {
      if (comando == 'E') {
        pos = 0;
      } else if (comando == 'D') {
        pos = 180;
      } else if (comando == 'C') {
        pos = 90;
      }
      myservo.write(pos);
      ultimoComando = comando;
    }
  }
}

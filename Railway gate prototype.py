#include <Servo.h>
Servo gate;
int sensor = 2;

void setup() {
  gate.attach(9);
  pinMode(sensor, INPUT_PULLUP);
  gate.write(90);
}

void loop() {
  if (digitalRead(sensor) == LOW)
    gate.write(0);   // Gate closed
  else
    gate.write(90);  // Gate open
}

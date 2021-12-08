

void setup() {
  pinMode(12, OUTPUT);

  // put your setup code here, to run once:
  Serial.begin(9600); //UART
  Serial.setTimeout(100);
}

int v;
void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available() > 0) {
    v = Serial.readString().toInt();

    digitalWrite(12, v);  //0     1

    Serial.println("Accion Aplicada");
  }


}

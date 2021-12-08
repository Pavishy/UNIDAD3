int Sensor1 = A0; 
int Sensor2 = A1;
int Sensor3 = A2;

int Actuador1 = 11;
int Actuador2 = 12;
int Actuador3 = 13;

void setup() {
  pinMode(Actuador1, OUTPUT);
  pinMode(Actuador2, OUTPUT);
  pinMode(Actuador3, OUTPUT);

  // put your setup code here, to run once:
  Serial.begin(9600); //UART
  Serial.setTimeout(100);
}

int v1, v2, v3;
void loop() {
  // put your main code here, to run repeatedly:

  v1 = analogRead(Sensor1); // X   XX  XXX   XXXX
  v2 = analogRead(Sensor2);
  v3 = analogRead(Sensor3);

  Serial.println("H" + String(v1) + "R" + String(v2) + "R" + String(v3) + "T"); //R <- 
  delay(100);

}

#include <WiFi.h>

float voltage;
float current;
float power;
float energy = 0;

void setup()
{
 Serial.begin(115200);
}

void loop()
{
 voltage = random(220,240);
 current = random(1,10);

 power = voltage * current;

 energy += power / 1000.0 / 3600.0;

 Serial.print("Voltage:");
 Serial.println(voltage);

 Serial.print("Current:");
 Serial.println(current);

 Serial.print("Power:");
 Serial.println(power);

 delay(1000);
}
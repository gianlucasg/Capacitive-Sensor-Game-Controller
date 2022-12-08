#include <CapacitiveSensor.h>

CapacitiveSensor   cs_4_2 = CapacitiveSensor(4,2);   
CapacitiveSensor   cs_4_3 = CapacitiveSensor(4,3); 
void setup() {
  cs_4_2.set_CS_AutocaL_Millis(0xFFFFFFFF);     // turn off autocalibrate on channel 1 - just as an example
  Serial.begin(9600);

}

void loop() {
  long start = millis();
  long total1 =  cs_4_2.capacitiveSensor(30);
  long total2 =  cs_4_3.capacitiveSensor(30);
  if (total1 > 500) {
    Serial.println(1);
  }
  else if (total1 < 499){
    Serial.println(-1);
  }
  if (total2 > 500) {
    Serial.println(5);
  }
  else if (total2 < 499){
    Serial.println(-5);
  }
}

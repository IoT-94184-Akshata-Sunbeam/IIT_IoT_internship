

const int MQ2_PIN = 34;    
const int GAS_THRESHOLD = 600;   

void setup() {
  Serial.begin(115200);
  delay(1000);

 
  pinMode(MQ2_PIN, INPUT);

  Serial.println("MQ-2 Gas Sensor test");
}

void loop() {
  int gasValue = analogRead(MQ2_PIN);   
  Serial.print("MQ-2 Sensor Value: ");
  Serial.println(gasValue);

  if (gasValue > GAS_THRESHOLD) {
    Serial.println("Gas Detected!");
  } else {
    Serial.println("No Gas Detected.");
  }

  Serial.println("------------------------");
  delay(1000);  
}

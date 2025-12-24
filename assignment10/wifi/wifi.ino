#include<WiFi.h>

const char *ssid = "SUNBEAM";
const char *password ="1234567890";

void setup() {
    // put your setup code here, to run once:


  Serial.begin(115200);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid,password);

  Serial.print("connecting to wifi");
  while(WiFi.status()!= WL_CONNECTED){
    delay(500);
    Serial.print(".");

  }

  Serial.println("connected to wifi");
  Serial.print("IP Address:");
  Serial.println(WiFi.localIP());
}

void loop() {
  // put your main code here, to run repeatedly:

}

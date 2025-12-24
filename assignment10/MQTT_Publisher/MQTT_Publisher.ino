#include <WiFi.h>
#include <ArduinoMqttClient.h>
#include <DHT.h>

const char *ssid = "SUNBEAM";
const char *password = "1234567890";

const char *host = "172.18.4.146";
unsigned int port = 1883;

#define DHT_PIN 4
#define DHT_TYPE DHT11

DHT dht(DHT_PIN, DHT_TYPE);

void setup() {
  Serial.begin(115200);

  dht.begin();  // start DHT [web:26]

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi ");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected to WiFi");
  Serial.print("IP Address : ");
  Serial.println(WiFi.localIP());
}

void loop() {
  float temp = dht.readTemperature();  // temperature °C [web:26]
  float hum  = dht.readHumidity();     // humidity % [web:26]

  if (isnan(temp) || isnan(hum)) {
    Serial.println("Failed to read from DHT sensor!");
    delay(2000);
    return;
  }

  WiFiClient wifiClient;
  MqttClient publisher(wifiClient);

  if (publisher.connect(host, port)) {
    // publish temperature
    publisher.beginMessage("reading/temp");
    publisher.print(temp);
    publisher.endMessage();

    // publish humidity
    publisher.beginMessage("reading/hum");
    publisher.print(hum);
    publisher.endMessage();
  }

  delay(5000);
}

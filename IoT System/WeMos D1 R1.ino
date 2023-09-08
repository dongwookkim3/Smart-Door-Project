#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>
#include <Servo.h>
#define FIREBASE_HOST "iot-dormitory-door-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "wMUmeverLoUTy9QRfZIMVvlEwPLgYjRHnMaiHGTv"
#define WIFI_SSID "bssm_free"
#define WIFI_PASSWORD "bssm_free"
Servo servo;
int servoPin = D3;
void setup(){
    Serial.begin(115200);
    WiFi.begin(WIFI_SSID,WIFI_PASSWORD);
    Firebase.begin(FIREBASE_HOST,FIREBASE_AUTH);
    Firebase.setInt("On",0);
    servo.attach(servoPin);
}
void loop(){
    if (Firebase.getInt("On")==1) servo.write(25);
    else servo.write(85);
    delay(1000);
}
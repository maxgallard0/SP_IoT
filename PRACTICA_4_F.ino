#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DFRobot_DHT11.h>
#include <Ds1302.h>

#define DHT11_PIN 15
#define IR_SENSOR_PIN 2
#define MQ135_PIN 4
#define PIN_ENA 19
#define PIN_CLK 5
#define PIN_DAT 18
#define BUTTON1_PIN 14
#define BUTTON2_PIN 27

DFRobot_DHT11 dht11;
Ds1302 rtc(PIN_ENA, PIN_CLK, PIN_DAT);
LiquidCrystal_I2C lcd(0x27, 16, 2);

const static char* WeekDays[] = {
    "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
};

void setup() {
    Serial.begin(9600);
    pinMode(IR_SENSOR_PIN, INPUT);
    pinMode(BUTTON1_PIN, INPUT);
    pinMode(BUTTON2_PIN, INPUT);
    lcd.init();
    lcd.backlight();
    rtc.init();
    Ds1302::DateTime dt = {
        .year = 23,
        .month = Ds1302::MONTH_OCT,
        .day = 5,
        .hour = 9,
        .minute = 0,
        .second = 0,
        .dow = Ds1302::DOW_THU
    };
    rtc.setDateTime(&dt);
}

void loop() {
  dht11.read(DHT11_PIN);
  float temperature = dht11.temperature;
  float humidity = dht11.humidity;
  int mq135Value = analogRead(MQ135_PIN) / 10;
  int proximity = analogRead(IR_SENSOR_PIN);
    
  Serial.print("Temperatura: ");
  Serial.println(temperature);
      Serial.print("Humedad: ");
    Serial.println(humidity);
    Serial.print("MQ135: ");
    Serial.println(mq135Value);
    Serial.print("Proximity: ");
    Serial.println(proximity);
    int button1State = digitalRead(BUTTON1_PIN);
    int button2State = digitalRead(BUTTON2_PIN);

    lcd.clear();

    if (button1State == LOW && button2State == LOW) {
        Ds1302::DateTime now;
        rtc.getDateTime(&now);
        lcd.setCursor(0, 0);
        lcd.print("20");
        lcd.print(now.year);
        lcd.print("-");
        lcd.print(now.month);
        lcd.print("-");
        lcd.print(now.day);
        lcd.setCursor(0, 1);
        lcd.print(now.hour);
        lcd.print(":");
        lcd.print(now.minute);
        lcd.print(":");
        lcd.print(now.second);
    } else if (button1State == HIGH && button2State == LOW) {
        dht11.read(DHT11_PIN);
        lcd.setCursor(0, 0);
        lcd.print("Temp: ");
        lcd.print(dht11.temperature);
        lcd.print("C");
        lcd.setCursor(0, 1);
        lcd.print("Hum: ");
        lcd.print(dht11.humidity);
        lcd.print("%");
    } else if (button1State == LOW && button2State == HIGH) {
        int mq135Value = analogRead(MQ135_PIN) / 10;
        lcd.setCursor(0, 0);
        lcd.print("MQ135: ");
        lcd.print(mq135Value);
        lcd.setCursor(0, 1);
        if (mq135Value < 100) {
            lcd.print("Aire limpio");
        } else if (mq135Value < 200) {
            lcd.print("Niveles normales");
        } else {
            lcd.print("Aire contaminado");
        }
    } else if (button1State == HIGH && button2State == HIGH) {
        int proximity = analogRead(IR_SENSOR_PIN);
        lcd.setCursor(0, 0);
        lcd.print("Proximidad: ");
        lcd.print(proximity);
    }

    delay(500);
}
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
const unsigned int minHorizontal[] = {230, 120, 160, 200};
const unsigned int maxHorizontal[] = {630, 520, 580, 640};

// servo 0
//#define SERVOMIN  230 // this is the 'minimum' pulse length count (out of 4096)
//#define SERVOMAX  630 // this is the 'maximum' pulse length count (out of 4096)
// servo 1
//#define SERVOMIN  120 // this is the 'minimum' pulse length count (out of 4096)
//#define SERVOMAX  520 // this is the 'maximum' pulse length count (out of 4096)
// servo 2
//#define SERVOMIN  160 // this is the 'minimum' pulse length count (out of 4096)
//#define SERVOMAX  580 // this is the 'maximum' pulse length count (out of 4096)
// servo 3
//#define SERVOMIN  200 // this is the 'minimum' pulse length count (out of 4096)
//#define SERVOMAX  640 // this is the 'maximum' pulse length count (out of 4096)

// servo 12
//#define SERVOMIN  200 // this is the 'minimum' pulse length count (out of 4096)
//#define SERVOMAX  640 // this is the 'maximum' pulse length count (out of 4096)
// servo 13
//#define SERVOMIN  120 // this is the 'minimum' pulse length count (out of 4096)
//#define SERVOMAX  500 // this is the 'maximum' pulse length count (out of 4096)
// servo 14
//#define SERVOMIN  130 // this is the 'minimum' pulse length count (out of 4096)
//#define SERVOMAX  510 // this is the 'maximum' pulse length count (out of 4096)
// servo 15
//#define SERVOMIN  230 // this is the 'minimum' pulse length count (out of 4096)
//#define SERVOMAX  560 // this is the 'maximum' pulse length count (out of 4096)

//const unsigned int minVertical[] = {200, 120, 130, 230};
//const unsigned int maxVertical[] = {640, 500, 510, 560};
//const unsigned int midVertical[] = {420, 310, 320, 395};


const unsigned int minVertical[] = {200, 500, 130, 560};
const unsigned int maxVertical[] = {640, 120, 510, 230};
const unsigned int midVertical[] = {420, 310, 320, 395};

uint8_t servonum = 15;
//uint8_t servonum2 = servonum -12;

void setup() {
  Serial.begin(9600);
  Serial.println("16 channel Servo test!");

  pwm.begin();
  
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates

  //pwm.setPWM(servonum2, 0, (SERVOMAX + SERVOMIN)/2);
  
  //for(int i = 15; i >= 12; i--)
  //{
//    pwm.setPWM(i,0,minVertical[i]);
  //}
  /*
  for(int i = 12; i < 16; i++)
  {
    pwm.setPWM(i,0,(minVertical[i] + maxVertical[i]) / 2);
    delay(300);  
  }
  */
  
  for(int i = 12; i < 16; i++)
  {
    pwm.setPWM(i,0,midVertical[i-12]);
  } 
  for(int j = 0; j < 5; j++)
  {
  delay(500);
 
  for(int i = 12; i < 16; i++)
  {
    pwm.setPWM(i,0,midVertical[i-12] + 20);
  }
  delay(500);
 
  for(int i = 12; i < 16; i++)
  {
    pwm.setPWM(i,0,midVertical[i-12] - 30);
  }
  }
  
  for(int i = 12; i < 16; i++)
  {
    pwm.setPWM(i,0,midVertical[i-12]);
  }
}
void loop() {
    
}

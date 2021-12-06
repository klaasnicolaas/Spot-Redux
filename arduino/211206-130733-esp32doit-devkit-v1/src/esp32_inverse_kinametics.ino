#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#include <Math.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// Depending on your servo make, the pulse width min and max may vary, you 
// want these to be as small/large as possible without hitting the hard stop
// for max range. You'll have to tweak them as necessary to match the servos you
// have!
#define SERVOMIN  123 // This is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  614 // This is the 'maximum' pulse length count (out of 4096)
#define USMIN  600 // This is the rounded 'minimum' microsecond length based on the minimum pulse of 150
#define USMAX  2400 // This is the rounded 'maximum' microsecond length based on the maximum pulse of 600
#define SERVO_FREQ 50 // Analog servos run at ~50 Hz updates

uint8_t servoMidPoint = ((SERVOMAX - SERVOMIN)/2) + SERVOMIN;
uint8_t servonum = 0;
uint8_t timeBetweenPoints = 2000;
const float Pi = 3.14159; // To however many digits you want.

void setup() {
  Serial.begin(9600);
  //Serial.println("16 channel PWM test!");

  pwm.begin();
  
  pwm.setOscillatorFrequency(27000000);
  pwm.setPWMFreq(SERVO_FREQ);  // Analog servos run at ~50 Hz updates

  // if you want to really speed stuff up, you can go into 'fast 400khz I2C' mode
  // some i2c devices dont like this so much so if you're sharing the bus, watch
  // out for this!
  Wire.setClock(400000);

  delay(10);

  //resetLeg();

  delay(500);

  //calculatePositions(70, -130, 1);
}

void loop() {
 
  boolean forward = true;
 
  while(forward) {
     for (float x = -20; x <= 70; x++) {
      calculatePositions(x, -100, 1);
      delay(30);
    }
     for (float x = 70; x >= -20; x--) {
      calculatePositions(x, -100, 1);
      delay(30);
    } 
    forward = false;
  }
  
}

void calculatePositions(float x,float y,float z) {
  float lowerLeg = 115;
  float upperLeg = 100;
  float lowerLegOffset = 24.24;
  
  //y = y + lowerLegOffset

  //bit cheeky but eh
  if (y == 0) {
    y = 0.00001;
  }
  if (x == 0) {
    x = 0.00001;
  }
  
  float s;
  float upperLegAngle;
  float lowerLegAngle;
  float shoulderAngle;
  
  if(z == 0) {
    s = y;
    shoulderAngle = -0.5*Pi;
  } 
  else {
    s = sqrt((y*y) / (z*z));
    shoulderAngle = atan(y/z);
  }

  lowerLegAngle = acos((x*x + s*s - lowerLeg*lowerLeg - upperLeg*upperLeg)/(2*lowerLeg*upperLeg));
  upperLegAngle = atan(s/x) - atan((upperLeg*sin(lowerLegAngle)) / (lowerLeg+upperLeg*cos(lowerLegAngle)));

  upperLegAngle = 225 + ((upperLegAngle*180)/Pi);
  lowerLegAngle = 180 - ((lowerLegAngle*180)/Pi) + 5.5;
  shoulderAngle = 180 + ((shoulderAngle*180)/Pi);

  float diffUpperLeg = upperLegAngle - 90;
  lowerLegAngle = lowerLegAngle - diffUpperLeg;

  upperLegAngle = 180 - upperLegAngle;

  if(upperLegAngle <= 0){
    upperLegAngle = 180 + upperLegAngle;
  }

  if(lowerLegAngle <= 0) {
    lowerLegAngle = 180 + lowerLegAngle;
  }

  Serial.print(shoulderAngle);
  Serial.print(",");
  Serial.print(upperLegAngle);
  Serial.print(",");
  Serial.println(lowerLegAngle);
  setLeg(0, shoulderAngle);
  setLeg(1, upperLegAngle);
  setLeg(2, lowerLegAngle);
}

void setLeg(int servo, float deg) {
  int pulse = map(deg, 0, 180, 0, SERVOMAX);
  if (pulse <= SERVOMIN) {
    pulse = SERVOMIN;
  }
  pwm.setPWM(servo, 0, pulse);
}

void resetLeg() {
  int pulse = map(90, 0, 180, 0, SERVOMAX);
  if (pulse <= SERVOMIN) {
    pulse = SERVOMIN;
  }
  pwm.setPWM(0, 0, pulse);
  pwm.setPWM(1, 0, pulse);
  pwm.setPWM(2, 0, pulse);
}

void minLeg() {
  int pulse = map(0, 0, 180, 0, SERVOMAX);
  if (pulse <= SERVOMIN) {
    pulse = SERVOMIN;
  }
  pwm.setPWM(0, 0, pulse);
  pwm.setPWM(1, 0, pulse);
  pwm.setPWM(2, 0, pulse);
}

void maxLeg() {
  int pulse = map(180, 0, 180, 0, SERVOMAX);
  if (pulse <= SERVOMIN) {
    pulse = SERVOMIN;
  }
  pwm.setPWM(0, 0, pulse);
  pwm.setPWM(1, 0, pulse);
  pwm.setPWM(2, 0, pulse);
}

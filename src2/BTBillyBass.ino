#include "./libraries/MX1508/MX1508.h"
#include "./libraries/MX1508/MX1508.cpp"

MX1508 bodyMotor(9, 6); //Sets up an MX1508 controlled motor on PWM pins 9 and 6
MX1508 mouthMotor(5, 3); //Sets up an MX1508 controlled motor on PWM pins 5 and 3

int soundPin = A0; //Sound input

int silence = 20; //threshold for silence
int bodySpeed = 0; //initalize body motor speed to 0
int soundVolume = 0; //holds the audio value from soundPin
int state = 0; // indicates the state of Billy

bool talking = false; //indicates whether the fish should be talking or not

//variables used to schedule actions
long currentTime;
long mouthActionTime;
long bodyActionTime;
long lastActionTime;

void setup() {
//set motor speeds to zero
  bodyMotor.setSpeed(0); 
  mouthMotor.setSpeed(0);

//input mode for sound pin
  pinMode(soundPin, INPUT);
}

void loop() {
  currentTime = millis(); //updates the time
  updateSoundInput();
  BillyBass();
}

void BillyBass() {
  switch (state) {
    case 0: //start state
      if (soundVolume > silence) { //if detect audio
        if (currentTime > mouthActionTime) { //and if no scheduled mouth movement
          talking = true; //set talking to true and schedule the mouth movement
          mouthActionTime = currentTime + 100;
          state = 1; //jump to a talk state
        } }
      if (currentTime - lastActionTime > 1500) { //if Billy hasn't done anything in a while
        lastActionTime = currentTime + floor(random(30, 60)) * 1000L;
        state = 2; //jump to a flap state
      }
      break;

    case 1: //talk state
      if (currentTime < mouthActionTime) { //if scheduled mouthActionTime in the future
        if (talking) { //talking is true
          openMouth(); //open mouth and articulate body
          lastActionTime = currentTime;
          articulateBody(true);
        }
      }
      else { //close mouth set talking to false
        closeMouth();
        articulateBody(false);
        talking = false;
        state = 0; //jump back to start state
      }
      break;

    case 2: //flap state
      flap();
      state = 0;
      break;
  }
}

int updateSoundInput() {
  soundVolume = digitalRead(soundPin); //read input from soundPin
}

void openMouth() {
  mouthMotor.halt(); //stop the mouth motor
  mouthMotor.setSpeed(220); //set the mouth motor speed
  mouthMotor.forward(); //open the mouth
}

void closeMouth() {
  mouthMotor.halt(); //stop the mouth motor
  mouthMotor.setSpeed(180); //set the mouth motor speed
  mouthMotor.backward(); // close the mouth
}

void articulateBody(bool talking) { //function for articulating the body with random movement to simulate dancing
  if (talking) { //if Billy is talking
    if (currentTime > bodyActionTime) { // and if we don't have a scheduled body movement
      int r = floor(random(0, 8)); // create a random number between 0 and 7)
      if (r < 1) {
        bodySpeed = 150; //move the body at moderate speed
        bodyActionTime = currentTime + floor(random(500, 1000)); //schedule body action for .5 to 1 seconds from current time
        bodyMotor.forward(); //move the body motor to raise the head
        delay(550); //wait

      } else if (r < 3) {
        bodySpeed = 150; //move the body at moderate speed
        bodyActionTime = currentTime + floor(random(500, 1000)); //schedule body action for .5 to 1 seconds from current time
        bodyMotor.forward(); //move the body motor to raise the head
        delay(550); //wait
        bodyMotor.setSpeed(0); //set motor to stop
        bodyMotor.forward(); //call method to return tail to starting position

      } else if (r == 4) {
        bodySpeed = 200;  // move the body medium speed
        bodyActionTime = currentTime + floor(random(500, 1000)); //schedule body action for .5 to 1 seconds from current time
        bodyMotor.forward(); //move the body motor to raise the head
        delay(550); //wait
        bodyMotor.setSpeed(0); //set motor to stop
        bodyMotor.forward(); //call method to return head to starting position

      } else if ( r == 5 ) {
        bodySpeed = 0; //set body motor speed to 0
        bodyMotor.halt(); //stop the body motor (to keep from violent sudden direction changes)
        bodyMotor.setSpeed(255); //set the body motor to full speed
        bodyMotor.backward(); //move the body motor to raise the tail
        delay(550); //wait
        bodyMotor.setSpeed(0); //set motor to stop
        bodyMotor.forward(); //call method to return head to starting position
        bodyActionTime = currentTime + floor(random(500, 1000)); //schedule body  for .5 to 1 seconds from current time
      }
      else {
        bodySpeed = 255; // move the body full speed
        bodyMotor.forward(); //move the body motor to raise the head
        delay(550);
        bodyMotor.setSpeed(0); //set motor to stop
        bodyMotor.backward(); // call method to return tail to starting position
        bodyActionTime = currentTime + floor(random(500, 1000)); //schedule action time for .5 to 1 seconds from current time
      }
    }

    bodyMotor.setSpeed(bodySpeed); //set the body motor speed
  } else {
    if (currentTime > bodyActionTime) { //if we're beyond the scheduled body action time
      bodyMotor.halt(); //stop the body motor
      bodyActionTime = currentTime + floor(random(20, 50)); //set the next scheduled body action to current time plus .02 to .05 seconds
    }
  }
}

void flap() { //generalized flapping method for case 2
  bodyMotor.setSpeed(255); //set the body motor to full speed
  bodyMotor.forward(); //move the body motor to raise the head
  delay(400); //wait 
  bodyMotor.halt(); //halt the motor
  bodyMotor.setSpeed(0); //set motor to stop
  bodyMotor.forward(); // call method to return head to starting position
  delay(250); //wait
  bodyMotor.setSpeed(255); //set the body motor to full speed
  bodyMotor.backward(); //move the body motor to raise the tail
  delay(350); //wait
  bodyMotor.halt(); //halt the motor
  bodyMotor.setSpeed(0); //set motor to stop
  bodyMotor.backward(); // call method to return tail to starting position
  delay(500); //wait
}
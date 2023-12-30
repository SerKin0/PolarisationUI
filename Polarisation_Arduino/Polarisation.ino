#include "header.h"

#define LIGHT_SENSOR A3

int starting_time;
int abs_degree = 0;
int angle_of_rotation;
int delay_of_steps = 2;                                                 // время задержки между импульсами
int delt_time = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(in1, OUTPUT);                                                 // настройка пинов для управления мотором
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(A3, INPUT);
}

void loop()
{
  int count = 0;
  angle_of_rotation = int_read_consol();
  delay_of_steps = int_read_consol();

  Serial.println(analogRead(LIGHT_SENSOR));
  if (angle_of_rotation > 0 )               //Если число больше 0(положительное), то повернуть мотор против часовой стрелки
  {
    starting_time = millis();
    for (int i = 0; i < angle_of_rotation * steps_in_the_degree; i++){
      four_steps(StepperMotorWrite, delay_of_steps, true);
      count++;
      Serial.println(count);
      //Serial.println(analogRead(LIGHT_SENSOR));
    }
    delt_time = millis() - starting_time;
  }
  else if (angle_of_rotation < 0) //Если число больше 0 (отрицательным), то повернуть мотор по часовой стрелки
  {
    starting_time = millis();
    for (int i = 0; i < (-angle_of_rotation) * steps_in_the_degree; i++){
      four_steps(StepperMotorWrite, delay_of_steps, false);
      count--;
      Serial.println(count);
      // Serial.println(analogRead(LIGHT_SENSOR));
    }
    delt_time = millis() - starting_time;
  }
  abs_degree += angle_of_rotation;
  Serial.println("e");
  StepperMotorWrite (0, 0, 0, 0);
}

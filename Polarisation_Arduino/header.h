#define in1 9                                                           //порты для   
#define in2 10                                                           //подключения
#define in3 11                                                          //драйвера ULN2003
#define in4 12                                                          //к Arduino

#define reducer 63.68395                                                 //Передаточное число редуктора шагового мотора
#define simbols_after_comma 6                                           //Число символов после запятой

const double steps_in_the_degree = (((32 * reducer) / 360) / 4) * 3.5;  // 32 - шагов нужно (без редуктора), для полного поворота; /360 - определяем кол-во шагов для 1 градуса; /4 - кол-во обмоток шагового мотора

double speed_ (double StepDeg, double StepDel)
{
  return( 1 / ( 4 * StepDeg * StepDel) );
}

int int_read_consol()
{
  bool flag = true;
  int in_value;
  while (flag)
  {
    if (Serial.available()>0)
    {
      in_value = Serial.parseInt();
      if (in_value!=0) return(in_value);
    }
  }
}

char char_read_consol()
{
  while (Serial.available()<=0);
  return (Serial.read());
}

void StepperMotorWrite (int in1_val, int in2_val, int in3_val , int in4_val) // Функция для запуска мотора
{
  digitalWrite(in1, in1_val);
  digitalWrite(in2, in2_val);
  digitalWrite(in3, in3_val);
  digitalWrite(in4, in4_val);
}

void four_steps (void *StepperMotor(int, int, int, int), int DelStep, bool direction_rot)
{
  if (direction_rot)
  {
    StepperMotor (1, 0, 0, 1); //Запуск функций для поворота мотора против часовой стрелки
    delay(DelStep);
    StepperMotor (1, 1, 0, 0);
    delay(DelStep);
    StepperMotor (0, 1, 1, 0);
    delay(DelStep);
    StepperMotor (0, 0, 1, 1);
    delay(DelStep);
  }
  else
  {
    StepperMotor (0, 0, 1, 1); //Запуск функций для поврота мотора по часовй стрелки
    delay(DelStep);
    StepperMotor (0, 1, 1, 0);
    delay(DelStep);
    StepperMotor (1, 1, 0, 0);
    delay(DelStep);
    StepperMotor (1, 0, 0, 1);
    delay(DelStep);
  }
}
  
  

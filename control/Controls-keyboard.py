import keyboard
from gpiozero import PhaseEnableMotor
from time import sleep

motor1 = PhaseEnableMotor(23, 24, pwm=True) #Motor 1 (Direction, Speed)
    # Pi4 GPIO 23 (pin 16) ---> MDD10A pin DIR1
    # Pi4 GPIO 24 (pin 18) ---> MDD10A pin PWM1
motor2 = PhaseEnableMotor(17, 27, pwm=True) #Motor 2 (Direction, Speed)
    # Pi4 GPIO 17 (pin 11) ---> MDD10A pin DIR2
    # Pi4 GPIO 27 (pin 13) ---> MDD10A pin PWM2

    #Pi4 GND (pin 14) ---> MDD10A pin GND

max_duty_cycle = .70 # Percentage of max PWM duty cycle
min_duty_cycle = .10 # Percentage of min PWM duty cycle
speed_step = (max_duty_cycle-min_duty_cycle)/10 # Value to change speed
    #gives 10 even increments between low and high
speed = max_duty_cycle # Sets initial speed at maximum

try:    
    while True:
        if keyboard.is_pressed("q")
            motor1.stop()
            motor2.stop()
            break
        
        elif keyboard.is_pressed("up"):
            motor1.forward(speed)
            motor2.forward(speed)
            
        elif keyboard.is_pressed("down"):
            motor1.backward(speed)
            motor2.backward(speed)
            
        elif keyboard.is_pressed("left"):
            motor1.backward(speed)
            motor2.forward(speed)
            
        elif keyboard.is_pressed("right"):
            motor1.forward(speed)
            motor2.backward(speed)                
            
        else:
            motor1.stop()
            motor2.stop()
            
        if keyboard.is_pressed("a"):
            if speed < max_duty_cycle:
                speed += speed_step

        elif keyboard.is_pressed("z"):
            if speed > min_duty_cycle:
                speed -= speed_step

finally:
    # Stop Motors
    print('Stopping motor')
    motor1.stop()
    motor2.stop()
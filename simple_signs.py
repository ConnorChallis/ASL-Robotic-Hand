from __future__ import division
import time
import Adafruit_PCA9685


pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths for fingers
#higher number = closed grip
pos_close_thumb = 550
pos_open_thumb = 300
pos_close_pointer = 210
pos_open_pointer = 450
pos_close_middle = 600
pos_open_middle = 295
pos_close_ring = 580 #needs to be physically loosened
pos_open_ring = 305 #needs to be physically loosened
pos_close_pinky = 570
pos_open_pinky = 310

pos_right_wrist = 600
pos_left_wrist = 150

#Define the pins for different fingers
pin_thumb = 4
pin_pointer = 1
pin_middle = 2
pin_ring = 3
pin_pinky = 5
pin_wrist = 0

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

pwm.set_pwm_freq(60)

print ("Starting timer")
time.sleep(0.1)
print ("time.sleep(x) still works!")
active = True
help = False

while active == True:
    sign = raw_input("Input desired hand movement here: (type 'help' for help) \n")
    if sign == 'quit':
        active = False
    elif sign == 'help':
        help = True
        if help == True:
            print ("\nWelcome to help menu\nList of commands:\n'rock_on'\n'f_you'\n'fist'\n'hang_loose'\n'relax'\n'quit'")
    elif sign == 'rock_on':
        time.sleep(0.5)
        pwm.set_pwm(pin_thumb, 0, pos_open_thumb)
        pwm.set_pwm(pin_pointer, 0, pos_open_pointer)
        pwm.set_pwm(pin_middle, 0, pos_open_middle)
        pwm.set_pwm(pin_ring, 0, pos_open_ring)
        pwm.set_pwm(pin_pinky, 0, pos_open_pinky)
        time.sleep(2.0)
        pwm.set_pwm(pin_middle, 0, pos_close_middle)
        pwm.set_pwm(pin_ring, 0, pos_close_ring)
        time.sleep(0.5)
        pwm.set_pwm(pin_thumb, 0, pos_close_thumb)
        time.sleep(1.5)
    elif sign == 'relax':
        time.sleep(0.5)
        pwm.set_pwm(pin_thumb, 0, pos_open_thumb)
        pwm.set_pwm(pin_pointer, 0, pos_open_pointer)
        pwm.set_pwm(pin_middle, 0, pos_open_middle)
        pwm.set_pwm(pin_ring, 0, pos_open_ring)
        pwm.set_pwm(pin_pinky, 0, pos_open_pinky)
        time.sleep(0.5)
    elif sign == 'f_you':
        time.sleep(0.5)
        pwm.set_pwm(pin_thumb, 0, pos_open_thumb)
        pwm.set_pwm(pin_pointer, 0, pos_open_pointer)
        pwm.set_pwm(pin_middle, 0, pos_open_middle)
        pwm.set_pwm(pin_ring, 0, pos_open_ring)
        pwm.set_pwm(pin_pinky, 0, pos_open_pinky)
        time.sleep(2.0)
        pwm.set_pwm(pin_pointer, 0, pos_close_pointer)
        pwm.set_pwm(pin_middle, 0, pos_close_middle)
        pwm.set_pwm(pin_ring, 0, pos_close_ring)
        pwm.set_pwm(pin_pinky, 0, pos_close_pinky)
        time.sleep(1.0)
        pwm.set_pwm(pin_thumb, 0, pos_close_thumb)
        time.sleep(2.0)
        pwm.set_pwm(pin_middle, 0, pos_open_middle)
        time.sleep(0.5)
    elif sign == 'fist':
        time.sleep(0.5)
        pwm.set_pwm(pin_thumb, 0, pos_open_thumb)
        pwm.set_pwm(pin_pointer, 0, pos_open_pointer)
        pwm.set_pwm(pin_middle, 0, pos_open_middle)
        pwm.set_pwm(pin_ring, 0, pos_open_ring)
        pwm.set_pwm(pin_pinky, 0, pos_open_pinky)
        time.sleep(2.0)
        pwm.set_pwm(pin_pointer, 0, pos_close_pointer)
        pwm.set_pwm(pin_middle, 0, pos_close_middle)
        pwm.set_pwm(pin_ring, 0, pos_close_ring)
        pwm.set_pwm(pin_pinky, 0, pos_close_pinky)
        time.sleep(1.0)
        pwm.set_pwm(pin_thumb, 0, pos_close_thumb)
        time.sleep(1.0)

    elif sign == 'hang_loose':
        time.sleep(0.5)
        pwm.set_pwm(pin_thumb, 0, pos_open_thumb)
        pwm.set_pwm(pin_pointer, 0, pos_open_pointer)
        pwm.set_pwm(pin_middle, 0, pos_open_middle)
        pwm.set_pwm(pin_ring, 0, pos_open_ring)
        pwm.set_pwm(pin_pinky, 0, pos_open_pinky)
        time.sleep(2.0)
        pwm.set_pwm(pin_pointer, 0, pos_close_pointer)
        pwm.set_pwm(pin_middle, 0, pos_close_middle)
        pwm.set_pwm(pin_ring, 0, pos_close_ring)
        pwm.set_pwm(pin_pinky, 0, pos_close_pinky)
        time.sleep(1.0)
        pwm.set_pwm(pin_thumb, 0, pos_close_thumb)
        time.sleep(1.0)
        pwm.set_pwm(pin_thumb, 0, pos_open_thumb)
        pwm.set_pwm(pin_pinky, 0, pos_open_pinky)
        time.sleep(1.0)
    else:
        print (str(sign) + " not a known command. Type 'help' for help")
print ("End of program, Thanks for signing!")

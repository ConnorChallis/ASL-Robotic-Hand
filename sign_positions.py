from __future__ import division
import time
import sign_positions
import logging
import math
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()


# Configure min and max servo pulse lengths for fingers
#higher number = closed grip
pos_close_thumb = 550
pos_open_thumb = 300
pos_close_pointer = 210
pos_open_pointer = 450
pos_close_middle = 600
pos_open_middle = 280
pos_open_ring = 498 #needs to be physically loosened
pos_close_ring = 135 #needs to be physically loosened
pos_close_pinky = 570
pos_open_pinky = 265

pos_right_wrist = 600
pos_left_wrist = 150

#Define the pins for different fingers
pin_thumb = 4
pin_pointer = 1
pin_middle = 2
pin_ring = 3
pin_pinky = 5
pin_wrist = 0

# pause time inbetween signs in routine
routine_pause = 1.0

#List of currently available signs and routines
#signs_available = ['rock_on','f_you','fist','hang_loose','relax','love','1','2','3','4','5','6','7','8','9','quit']
#shows_available = ['cycle_all','numbers','random']

#Helper function to make setting a servo pulse width simpler.
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
def rock_on():
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
def relax():
    time.sleep(0.5)
    pwm.set_pwm(pin_thumb, 0, pos_open_thumb)
    pwm.set_pwm(pin_pointer, 0, pos_open_pointer)
    pwm.set_pwm(pin_middle, 0, pos_open_middle)
    pwm.set_pwm(pin_ring, 0, pos_open_ring)
    pwm.set_pwm(pin_pinky, 0, pos_open_pinky)
def f_you():
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
def fist():
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
def hang_loose():
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
def love():
    time.sleep(0.5)
    pwm.set_pwm(pin_thumb, 0, pos_open_thumb)
    pwm.set_pwm(pin_pointer, 0, pos_open_pointer)
    pwm.set_pwm(pin_middle, 0, pos_open_middle)
    pwm.set_pwm(pin_ring, 0, pos_open_ring)
    pwm.set_pwm(pin_pinky, 0, pos_open_pinky)
    time.sleep(1.0)
    pwm.set_pwm(pin_middle, 0, pos_close_middle)
    pwm.set_pwm(pin_ring, 0, pos_close_ring)
def sign_1():
    time.sleep(0.5)
    pwm.set_pwm(pin_thumb, 0, pos_open_thumb)
    pwm.set_pwm(pin_pointer, 0, pos_open_pointer)
    pwm.set_pwm(pin_middle, 0, pos_open_middle)
    pwm.set_pwm(pin_ring, 0, pos_open_ring)
    pwm.set_pwm(pin_pinky, 0, pos_open_pinky)
    time.sleep(2.0)
    pwm.set_pwm(pin_middle, 0, pos_close_middle)
    pwm.set_pwm(pin_ring, 0, pos_close_ring)
    pwm.set_pwm(pin_pinky, 0, pos_close_pinky)
    time.sleep(1.0)
    pwm.set_pwm(pin_thumb, 0, pos_close_thumb)
def sign_2():
    time.sleep(0.5)
    pwm.set_pwm(pin_thumb, 0, pos_open_thumb)
    pwm.set_pwm(pin_pointer, 0, pos_open_pointer)
    pwm.set_pwm(pin_middle, 0, pos_open_middle)
    pwm.set_pwm(pin_ring, 0, pos_open_ring)
    pwm.set_pwm(pin_pinky, 0, pos_open_pinky)
    time.sleep(2.0)
    pwm.set_pwm(pin_ring, 0, pos_close_ring)
    pwm.set_pwm(pin_pinky, 0, pos_close_pinky)
    time.sleep(1.0)
    pwm.set_pwm(pin_thumb, 0, pos_close_thumb)
def sign_3():
    time.sleep(0.5)
    pwm.set_pwm(pin_thumb, 0, pos_open_thumb)
    pwm.set_pwm(pin_pointer, 0, pos_open_pointer)
    pwm.set_pwm(pin_middle, 0, pos_open_middle)
    pwm.set_pwm(pin_ring, 0, pos_open_ring)
    pwm.set_pwm(pin_pinky, 0, pos_open_pinky)
    time.sleep(2.0)
    pwm.set_pwm(pin_ring, 0, pos_close_ring)
    pwm.set_pwm(pin_pinky, 0, pos_close_pinky)
def sign_4():
    time.sleep(0.5)
    pwm.set_pwm(pin_thumb, 0, pos_open_thumb)
    pwm.set_pwm(pin_pointer, 0, pos_open_pointer)
    pwm.set_pwm(pin_middle, 0, pos_open_middle)
    pwm.set_pwm(pin_ring, 0, pos_open_ring)
    pwm.set_pwm(pin_pinky, 0, pos_open_pinky)
    time.sleep(1.0)
    pwm.set_pwm(pin_thumb, 0, pos_close_thumb)
def sign_5():
    time.sleep(0.5)
    pwm.set_pwm(pin_thumb, 0, pos_open_thumb)
    pwm.set_pwm(pin_pointer, 0, pos_open_pointer)
    pwm.set_pwm(pin_middle, 0, pos_open_middle)
    pwm.set_pwm(pin_ring, 0, pos_open_ring)
    pwm.set_pwm(pin_pinky, 0, pos_open_pinky)

def sign_6():
    time.sleep(0.5)
    pwm.set_pwm(pin_thumb, 0, pos_open_thumb)
    pwm.set_pwm(pin_pointer, 0, pos_open_pointer)
    pwm.set_pwm(pin_middle, 0, pos_open_middle)
    pwm.set_pwm(pin_ring, 0, pos_open_ring)
    pwm.set_pwm(pin_pinky, 0, pos_open_pinky)
    time.sleep(2.0)
    pwm.set_pwm(pin_pinky, 0, pos_close_pinky)
    time.sleep(1.0)
    pwm.set_pwm(pin_thumb, 0, pos_close_thumb)
def sign_7():
    time.sleep(0.5)
    pwm.set_pwm(pin_thumb, 0, pos_open_thumb)
    pwm.set_pwm(pin_pointer, 0, pos_open_pointer)
    pwm.set_pwm(pin_middle, 0, pos_open_middle)
    pwm.set_pwm(pin_ring, 0, pos_open_ring)
    pwm.set_pwm(pin_pinky, 0, pos_open_pinky)
    time.sleep(2.0)
    pwm.set_pwm(pin_ring, 0, pos_close_ring)
    time.sleep(1.0)
    pwm.set_pwm(pin_thumb, 0, pos_close_thumb)
    time.sleep(1.0)
def sign_8():
    time.sleep(0.5)
    pwm.set_pwm(pin_thumb, 0, pos_open_thumb)
    pwm.set_pwm(pin_pointer, 0, pos_open_pointer)
    pwm.set_pwm(pin_middle, 0, pos_open_middle)
    pwm.set_pwm(pin_ring, 0, pos_open_ring)
    pwm.set_pwm(pin_pinky, 0, pos_open_pinky)
    time.sleep(2.0)
    pwm.set_pwm(pin_middle, 0, pos_close_middle)
    time.sleep(1.0)
    pwm.set_pwm(pin_thumb, 0, pos_close_thumb)
    time.sleep(1.0)
def sign_9():
    time.sleep(0.5)
    pwm.set_pwm(pin_thumb, 0, pos_open_thumb)
    pwm.set_pwm(pin_pointer, 0, pos_open_pointer)
    pwm.set_pwm(pin_middle, 0, pos_open_middle)
    pwm.set_pwm(pin_ring, 0, pos_open_ring)
    pwm.set_pwm(pin_pinky, 0, pos_open_pinky)
    time.sleep(2.0)
    pwm.set_pwm(pin_pointer, 0, pos_close_pointer)
    time.sleep(1.0)
    pwm.set_pwm(pin_thumb, 0, pos_close_thumb)
    time.sleep(1.0)

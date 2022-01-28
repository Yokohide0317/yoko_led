import time
from rpi_ws281x import PixelStrip, Color
import argparse
import random, subprocess

thunder_mp3 = "./music/thunder.mp3"
kaminari_mp3 = "./music/kaminari.mp3"

# LED strip configuration:
LED_COUNT = 293        # Number of LED pixels.
LED_PIN = 21         # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


# def of color
thunder = Color(255, 255, 125)
clear = Color(0, 0, 0)
red_color = Color(0, 0, 230)
yellow_color = Color(0, 0, 200)
blue_color = Color(0, 0, 255)
purple_color = Color(113, 0, 255)
cyan_color = Color(130, 10, 255)
pink_color = Color(255, 0, 255)
green_color = Color(0, 209, 240)
orange_color = Color(255, 130, 255)

parser = argparse.ArgumentParser()
args = parser.parse_args()

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()




# def of position
all_pos = list(range(0, strip.numPixels()))
pos1 = list(range(0, 30))
pos2 = list(range(31, 75))
pos3 = list(range(76, 108))
pos4 = list(range(137, 169))
pos5 = list(range(170, 201))
pos6 = list(range(202, 232))
pos7 = list(range(233, 263))
pos8 = list(range(264, 293))


def kaminari_sound():
    pass
#    subprocess.Popen(["mplayer", thunder_mp3])



def check_position():
    for pos in pos1:
        strip.setPixelColor(pos, red_color)
    for pos in pos2:
        strip.setPixelColor(pos, pink_color)
    for pos in pos3:
        strip.setPixelColor(pos, yellow_color)
    for pos in pos4:
        strip.setPixelColor(pos, purple_color)
    for pos in pos5:
        strip.setPixelColor(pos, cyan_color)
    for pos in pos6:
        strip.setPixelColor(pos, blue_color)
    for pos in pos7:
        strip.setPixelColor(pos, green_color)
    for pos in pos8:
        strip.setPixelColor(pos, orange_color)



    strip.show()
    time.sleep(1)



def inp_color(position, color_rgb):
    for pos in position:
        strip.setPixelColor(pos, color_rgb)

def before_set():
    for all_ in all_pos:
        strip.setPixelColor(all_, clear)


def clear_pos():
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, clear)
    strip.show()
    time.sleep(1)


class pikapika():

    def __init__(self, color_sequence):
        self.color_seq = color_sequence

    def frame1(self, light_time=0.5):
        before_set()
        inp_color(pos2[5:], self.color_seq[1])
        inp_color(pos3[1:6], self.color_seq[2])
        strip.show()
        time.sleep(light_time)

    def frame2(self, light_time=0.5):
        before_set()
        inp_color(pos1[4:], self.color_seq[0])
        inp_color(pos2, self.color_seq[1])
        inp_color(pos3, self.color_seq[2])
        inp_color(pos4, self.color_seq[3])
        inp_color(pos5[0:6], self.color_seq[4])
        
        strip.show()
        time.sleep(light_time)

    def frame3(self, light_time=0.5):
        before_set()
        inp_color(pos2[1:], self.color_seq[1])
        inp_color(pos3[0:], self.color_seq[2])
        strip.show()
        time.sleep(light_time)

    def frame4(self, light_time=0.5):
        before_set()
        inp_color(pos1, self.color_seq[0])
        inp_color(pos2, self.color_seq[1])
        inp_color(pos3, self.color_seq[2])
        inp_color(pos4, self.color_seq[3])
        inp_color(pos5, self.color_seq[4])
        inp_color(pos6, self.color_seq[5])
        inp_color(pos7, self.color_seq[6])
        inp_color(pos8, self.color_seq[7])      
        strip.show()
        time.sleep(light_time)

    def frame5(self, light_time=0.5):
        before_set()
        inp_color(pos7, self.color_seq[6])
        time.sleep(light_time)
   
    def frame6(self, light_time=0.5):
        before_set()
        inp_color(pos6[4:], self.color_seq[5])
        inp_color(pos7, self.color_seq[6])
        inp_color(pos8[:-4], self.color_seq[7])
        strip.show()
        time.sleep(light_time)

    def frame7(self, light_time=0.5):
        before_set()
        inp_color(pos6, self.color_seq[5])
        inp_color(pos7, self.color_seq[6])
        inp_color(pos8, self.color_seq[7])
        strip.show()
        time.sleep(light_time)

    def frame8(self, light_time=0.5):
        before_set()
        inp_color(pos8, self.color_seq[7])
        strip.show()
        time.sleep(light_time)

    def main1(self):
        kaminari_sound()
        self.frame1(0.3)
        self.frame2(0.1)
        self.frame3(0.1)
        self.frame1(0.1)
        self.frame3(0.1)
        self.frame1(0.2)
        self.frame2(0.2)
        self.frame4(0.4)    
        self.frame3(0.2)
        self.frame1(0.1)
        self.frame3(0.1)
        self.frame1(0.1)
        clear_pos()
        self.frame2(0.1)
        self.frame3(0.1)
        self.frame5(0.2)
        self.frame6(0.3)
        self.frame7(0.2)
        self.frame8(0.2)
        clear_pos()

def off_thunder(light_time=1.0):
    i = 0
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, clear)
    strip.show()
    time.sleep(light_time)




# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    print('Press Ctrl-C to quit.')
    clear_pos()
    while True:
        color_seq = [red_color, pink_color, yellow_color, purple_color, cyan_color, blue_color, green_color, orange_color]
        random.shuffle(color_seq)
        pika = pikapika(color_seq)
        pika.main1()

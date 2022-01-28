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
pos4 = list(range(109, 169))
pos5 = list(range(170, 184))
pos6 = list(range(185, 217))
pos7 = list(range(218, 262))
pos8 = list(range(263, 293))


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

    def frame_main(self, _pos1=pos1, _pos2=pos2, _pos3=pos3, _pos4=pos4, _pos5=pos5, _pos6=pos6, _pos7=pos7, _pos8=pos8, rm_pos=[], light_time=0.08):

        before_set()
        if "p1" not in rm_pos:
            inp_color(_pos1, self.color_seq[0])
        if "p2" not in rm_pos:
            inp_color(_pos2, self.color_seq[1])
        if "p3" not in rm_pos:
            inp_color(_pos3, self.color_seq[2])
        if "p4" not in rm_pos:
            inp_color(_pos4, self.color_seq[3])
        if "p5" not in rm_pos:
            inp_color(_pos5, self.color_seq[4])
        if "p6" not in rm_pos:
            inp_color(_pos6, self.color_seq[5])
        if "p7" not in rm_pos:
            inp_color(_pos7, self.color_seq[6])
        if "p8" not in rm_pos:
            inp_color(_pos8, self.color_seq[7])
        strip.show()
        time.sleep(light_time)



    def main1(self):
        """
        self.frame1()
        self.frame2()
        """
        self.frame_main()
        for i in range(5, 15):
            self.frame_main(_pos1=pos1[i:], _pos8=pos8[:i])
#        for i in range(15, 10, -1):
#            self.frame_main(_pos1=pos1[i:], _pos8=pos8[:i])
        for i in range(10, 30):
            self.frame_main(_pos1=pos1[i:], _pos8=pos8[:i])
        for i in range(30, 25, -1):
            self.frame_main(_pos1=pos1[i:], _pos8=pos8[:i])

        for i in range(5, 15):
            self.frame_main(_pos2=pos2[i:], _pos7=pos7[:i], rm_pos=["p1", "p8"])
        for i in range(30, 25, -1):
            self.frame_main(_pos2=pos2[i:], _pos7=pos7[:i], rm_pos=["p1", "p8"])

        for i in range(5, 15):
            self.frame_main(_pos3=pos3[i:], _pos6=pos6[:i], rm_pos=["p1", "p8"])
        for i in range(30, 25, -1):
            self.frame_main(_pos4=pos4[i:], _pos5=pos5[:i], rm_pos=["p1", "p8", "p2", "p7"])

        for i in range(5, 35):
            self.frame_main(_pos1=pos1[i:], _pos6=pos6[:i], rm_pos=["p8", "p7"])
        for i in range(1, 30):
            self.frame_main(_pos2=pos2[i:], _pos5=pos5[:i], rm_pos=["p1", "p8", "p7"])




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

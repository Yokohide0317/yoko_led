import time
from rpi_ws281x import PixelStrip, Color
import argparse

# LED strip configuration:
LED_COUNT = 135        # Number of LED pixels.
LED_PIN = 21         # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def colorWipe(strip, color, wait_ms=200):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def all_flash(strip, wait_ms=100):
    thunder = Color(255, 255, 125)
    clear = Color(0, 0, 0)
    
    def on_thunder(light_time=1.0):
        i = 0
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, thunder)
        strip.show()
        time.sleep(light_time)

    def off_thunder(light_time=1.0):
        i = 0
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, clear)
        strip.show()
        time.sleep(light_time)


    off_thunder(3)
    on_thunder(0.18)
    off_thunder(0.18)
    on_thunder(0.1)
    off_thunder(0.1)
    on_thunder(0.5)
    off_thunder(0.3)
    on_thunder(0.1)


def cloudWipe(strip, wait_ms=100):
    white = Color(127, 127, 127)
    clear = Color(0, 0, 0)
    feed =  5
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, white)
        if i > feed:
            strip.setPixelColor(i-feed, clear)
        else:
            pass
        strip.show()
        time.sleep(wait_ms / 1000.0)
    
    # clear end
    for i in range(feed):
        strip.setPixelColor(strip.numPixels()-(feed-i), clear)
        strip.show()
        time.sleep(wait_ms / 1000.0)



# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    print('Press Ctrl-C to quit.')
    while True:
        try:
            while True:
                #cloudWipe(strip)
                all_flash(strip)
        except KeyboardInterrupt:
             colorWipe(strip, Color(0, 0, 0), 10)

        except:
            colorWipe(strip, Color(0, 0, 0), 10)

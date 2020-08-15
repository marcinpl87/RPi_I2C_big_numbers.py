# RPi_I2C_big_numbers.py
To run this code put numbers.py file and RPi_I2C_driver.py file from https://gist.github.com/DenisFromHR/cc863375a6e19dce359d in one directory and run

```
$ python numbers.py
```

I created these functions to draw (in python) big numbers and time on 20x4 or 16x2 RPi_I2C LCD.
To create it I used these sources:
https://www.recantha.co.uk/blog/?p=4849
https://omerk.github.io/lcdchargen/
http://woodsgood.ca/projects/2015/02/17/big-font-lcd-characters/
but most of these articles are arduino related, and I didn't find anything RPI compatible in python, so I decided to write it by myself.

I tested it with Raspberry Pi and 20x4 LCD with I2C LCM1602 controller.

![big numbers](https://i.postimg.cc/5ysT0NX5/IMG-20200815-213945-1.jpg)
![time](https://i.postimg.cc/59Ks6rPm/IMG-20200815-213707-1.jpg)

import RPi_I2C_driver
from time import *
import time, sys

mylcd = RPi_I2C_driver.lcd()
mylcd.lcd_load_custom_chars([
    [0x1F, 0x1F, 0x1F, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x18, 0x1C, 0x1E, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F],
    [0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x0F, 0x07, 0x03],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x1F, 0x1F, 0x1F],
    [0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1E, 0x1C, 0x18],
    [0x1F, 0x1F, 0x1F, 0x00, 0x00, 0x00, 0x1F, 0x1F],
    [0x1F, 0x00, 0x00, 0x00, 0x00, 0x1F, 0x1F, 0x1F],
    [0x03, 0x07, 0x0F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F],
])

def bigDigit(digit, row, col):
    if row == 1:
        textRow = 1
    else:
        textRow = 3
    if digit == 0:
        mylcd.lcd_display_string_pos(chr(7), textRow, col)
        mylcd.lcd_display_string_pos(chr(0), textRow, col+1)
        mylcd.lcd_display_string_pos(chr(1), textRow, col+2)
        mylcd.lcd_display_string_pos(chr(2), textRow+1, col)
        mylcd.lcd_display_string_pos(chr(3), textRow+1, col+1)
        mylcd.lcd_display_string_pos(chr(4), textRow+1, col+2)
    elif digit == 1:
        mylcd.lcd_display_string_pos(chr(0), textRow, col)
        mylcd.lcd_display_string_pos(chr(1), textRow, col+1)
        mylcd.lcd_display_string_pos(chr(3), textRow+1, col)
        mylcd.lcd_display_string_pos(chr(255), textRow+1, col+1)
        mylcd.lcd_display_string_pos(chr(3), textRow+1, col+2)
    elif digit == 2:
        mylcd.lcd_display_string_pos(chr(5), textRow, col)
        mylcd.lcd_display_string_pos(chr(5), textRow, col+1)
        mylcd.lcd_display_string_pos(chr(1), textRow, col+2)
        mylcd.lcd_display_string_pos(chr(255), textRow+1, col)
        mylcd.lcd_display_string_pos(chr(6), textRow+1, col+1)
        mylcd.lcd_display_string_pos(chr(6), textRow+1, col+2)
    elif digit == 3:
        mylcd.lcd_display_string_pos(chr(0), textRow, col)
        mylcd.lcd_display_string_pos(chr(5), textRow, col+1)
        mylcd.lcd_display_string_pos(chr(1), textRow, col+2)
        mylcd.lcd_display_string_pos(chr(3), textRow+1, col)
        mylcd.lcd_display_string_pos(chr(6), textRow+1, col+1)
        mylcd.lcd_display_string_pos(chr(4), textRow+1, col+2)
    elif digit == 4:
        mylcd.lcd_display_string_pos(chr(2), textRow, col)
        mylcd.lcd_display_string_pos(chr(3), textRow, col+1)
        mylcd.lcd_display_string_pos(chr(255), textRow, col+2)
        mylcd.lcd_display_string_pos(chr(255), textRow+1, col+2)
    elif digit == 5:
        mylcd.lcd_display_string_pos(chr(2), textRow, col)
        mylcd.lcd_display_string_pos(chr(5), textRow, col+1)
        mylcd.lcd_display_string_pos(chr(5), textRow, col+2)
        mylcd.lcd_display_string_pos(chr(3), textRow+1, col)
        mylcd.lcd_display_string_pos(chr(6), textRow+1, col+1)
        mylcd.lcd_display_string_pos(chr(4), textRow+1, col+2)
    elif digit == 6:
        mylcd.lcd_display_string_pos(chr(7), textRow, col)
        mylcd.lcd_display_string_pos(chr(5), textRow, col+1)
        mylcd.lcd_display_string_pos(chr(5), textRow, col+2)
        mylcd.lcd_display_string_pos(chr(2), textRow+1, col)
        mylcd.lcd_display_string_pos(chr(6), textRow+1, col+1)
        mylcd.lcd_display_string_pos(chr(4), textRow+1, col+2)
    elif digit == 7:
        mylcd.lcd_display_string_pos(chr(0), textRow, col)
        mylcd.lcd_display_string_pos(chr(0), textRow, col+1)
        mylcd.lcd_display_string_pos(chr(1), textRow, col+2)
        mylcd.lcd_display_string_pos(chr(255), textRow+1, col+2)
    elif digit == 8:
        mylcd.lcd_display_string_pos(chr(7), textRow, col)
        mylcd.lcd_display_string_pos(chr(5), textRow, col+1)
        mylcd.lcd_display_string_pos(chr(1), textRow, col+2)
        mylcd.lcd_display_string_pos(chr(2), textRow+1, col)
        mylcd.lcd_display_string_pos(chr(6), textRow+1, col+1)
        mylcd.lcd_display_string_pos(chr(4), textRow+1, col+2)
    elif digit == 9:
        mylcd.lcd_display_string_pos(chr(7), textRow, col)
        mylcd.lcd_display_string_pos(chr(5), textRow, col+1)
        mylcd.lcd_display_string_pos(chr(1), textRow, col+2)
        mylcd.lcd_display_string_pos(chr(6), textRow+1, col)
        mylcd.lcd_display_string_pos(chr(6), textRow+1, col+1)
        mylcd.lcd_display_string_pos(chr(4), textRow+1, col+2)

def bigNumber(num, row, col):
    arr = []
    arr[:] = str(num)
    for digit in arr:
        bigDigit(int(digit), row, col)
        col = col + 4

def bigTime(row):
    if row == 1:
        textRow = 1
    else:
        textRow = 3
    bigNumber(time.strftime("%H"), row, 1)
    bigNumber(time.strftime("%M"), row, 11)
    mylcd.lcd_display_string_pos(chr(165), textRow, 9)
    mylcd.lcd_display_string_pos(chr(165), textRow+1, 9)

bigDigit(0, 1, 0)
bigDigit(1, 1, 4)
bigDigit(2, 1, 8)
bigDigit(3, 1, 12)
bigDigit(4, 1, 16)
bigDigit(5, 2, 0)
bigDigit(6, 2, 4)
bigDigit(7, 2, 8)
bigDigit(8, 2, 12)
bigDigit(9, 2, 16)
sleep(3)
mylcd.lcd_clear()

bigNumber(98765, 1, 0)
bigNumber(43210, 2, 0)
sleep(3)
mylcd.lcd_clear()

bigTime(1)
sleep(3)
mylcd.lcd_clear()

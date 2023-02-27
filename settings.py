import pygame as pg

class Settings:

    def __init__(self):
        #основное поле
        self.height = 600
        self.width = 900
        self.caption = "Nostromo service terminal"
        self.bg_color_1 = (1, 45, 113)
        self.bg_color_2 = (123, 34, 49)
        self.bg_color_3 = (3, 18, 34)
        self.bg_color_4 = (1, 47, 92)
        self.fps = 60

        #шрифт
        self.letter_size_open = 140
        self.letter_size_screen2 = 30

        #записи
        self.retro_font_1 = pg.font.Font('E:/Installed_programs_E/Sevastopol/fonts/BitPap.ttf', 36)
        self.screen1_font = pg.font.Font('E:/Installed_programs_E/Sevastopol/fonts/Berthold City Light Regular.otf', self.letter_size_open)
        self.screen2_font = pg.font.Font('E:/Installed_programs_E/Sevastopol/fonts/VT323-Regular.ttf', self.letter_size_screen2)

        self.text_colour_menu = (255, 255, 255)
        self.text_colour_screen_1 = (152, 216, 212)

        #логические переменные
        self.start_screen = True
        self.screen1 = False
        self.screen2 = False
        self.screen3 = False

        #время и таймер
        self.screen1_time = 0
        self.screen2_time = 0
        self.screen3_time = 0

        #указатель
        self.pointer_width = self.width
        self.pointer_height = 5

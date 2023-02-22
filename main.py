import sys
import threading
import pygame as pg
from settings import Settings

def run_pc():
    pg.init()
    settings = Settings()

    screen = pg.display.set_mode((settings.width, settings.height))
    pg.display.set_caption(settings.caption)
    clock = pg.time.Clock()

    def draw_menu(text):
        text_colour = settings.text_colour_screen_1
        letters = pg.font.Font('E:/Installed_programs_E/Sevastopol/fonts/VT323-Regular.ttf', 36)
        screen_text = letters.render(text, True, text_colour)
        text_rect = screen_text.get_rect(center=(settings.width / 2, settings.height / 2))
        screen.blit(screen_text, text_rect)

    def draw_nostromo(text, font, position):
        text_colour = settings.text_colour_screen_1
        screen_text = font.render(text, True, text_colour)
        text_rect = screen_text.get_rect(center=position)
        pg.draw.rect(screen, settings.text_colour_screen_1, text_rect, 8)
        screen.blit(screen_text, text_rect)

    def draw_screen2(text, font, position):
        text_colour = settings.text_colour_screen_1
        screen_text = font.render(text, True, text_colour)
        text_rect = screen_text.get_rect(center=position)
        text_rect.left = position[0]
        screen.blit(screen_text, text_rect)


    while True:
        clock.tick(settings.fps)
        time_event = threading.Event()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and start_screen:
                    settings.start_screen = False
                    settings.screen1 = True
                if event.key == pg.K_SPACE and screen1:
                    settings.screen1 = False
                    settings.screen2 = True

        start_screen = settings.start_screen
        screen1 = settings.screen1
        screen2 = settings.screen2

        if start_screen:
            screen.fill(settings.bg_color_1)
            draw_menu('Press SPACE to continue')

        if screen1:
            screen.fill(settings.bg_color_2)
            draw_nostromo('NOSTROMO', settings.screen1_font, (settings.width / 2, settings.height / 2 - settings.letter_size_open * 1.1))
            draw_nostromo('180924609', settings.screen1_font, (settings.width / 2, settings.height / 2))

        if screen2:
            screen.fill(settings.bg_color_3)
            draw_screen2('SHIP', settings.screen2_font, (settings.width * 0.7, settings.letter_size_screen2))
            draw_screen2('WEYLAND YUTANI', settings.screen2_font, (settings.width * 0.7, settings.letter_size_screen2 * 2))
            draw_screen2('NOSTROMO 180246', settings.screen2_font, (settings.width * 0.7, settings.letter_size_screen2 * 3))
            draw_screen2('FUNCTION', settings.screen2_font, (settings.width * 0.7, settings.letter_size_screen2 * 7))
            draw_screen2('TANKER/REFINERY', settings.screen2_font, (settings.width * 0.7, settings.letter_size_screen2 * 8))
            draw_screen2('CAPACITY', settings.screen2_font, (settings.width * 0.7, settings.letter_size_screen2 * 10))
            draw_screen2('200 000 000 TONNES', settings.screen2_font, (settings.width * 0.7, settings.letter_size_screen2 * 11))
            draw_screen2('GALACTIC POSITION', settings.screen2_font,  (settings.width * 0.7, settings.letter_size_screen2 * 13))
            draw_screen2('????????????????', settings.screen2_font, (settings.width * 0.7, settings.letter_size_screen2 * 14))

        pg.display.flip()

if __name__ == '__main__':
    run_pc()

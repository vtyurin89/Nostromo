import sys
import pygame as pg
from settings import Settings
from random import randint, choice, uniform

def run_pc():
    pg.init()
    settings = Settings()

    screen = pg.display.set_mode((settings.width, settings.height))
    pg.display.set_caption(settings.caption)
    clock = pg.time.Clock()

    screen1_time = settings.screen1_time
    screen2_time = settings.screen2_time
    screen3_time = settings.screen3_time
    time_05 = 0

    #указатель
    pointer = pg.rect.Rect(0, 0, settings.pointer_width, settings.pointer_height)
    pointer.left = 100
    pointer.bottom = 100

    #базы данных символов и координат на экране
    nostromo_letters = ['-', '=', '|', '.','||','|','*']
    first_list = list()
    lil_screen_list = list()
    check_list = list()
    show_num_list1 = list()
    show_num_list2 = list()
    show_num_list3 = list()
    show_num_list4 = list()
    show_num_list5 = list()
    num_list = []

    for i in range(150):
        rand_x = randint(0, 20) * 20
        rand_y = randint(0, 8) * settings.letter_size_screen2
        pair_xy = [rand_x, rand_y]
        if pair_xy not in check_list:
            check_list.append(pair_xy)
            first_list.append([choice(nostromo_letters), pair_xy])
        check_list.clear()
    show_list = first_list[:30]
    lil_screen_list = first_list[30:]
    first_list.clear()

    for i in range(120):
        num = uniform(11.1111, 9999.99)
        strnum = str(num)[:7]
        num_list.append(strnum)



    #функции отображения текста
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

    def draw_lil_screen(text, font, position):
        text_colour = settings.text_colour_screen_1
        screen_text = font.render(text, True, text_colour)
        text_rect = screen_text.get_rect(center=position)
        text_rect.left = position[0]
        text_rect.top = position[1]
        lil_screen.blit(screen_text, text_rect)



    def screen2_interface():
        screen.fill(settings.bg_color_3)
        draw_screen2('SHIP', settings.screen2_font,
                     (settings.width * 0.7, settings.letter_size_screen2))
        draw_screen2('WEYLAND YUTANI', settings.screen2_font,
                     (settings.width * 0.7, settings.letter_size_screen2 * 2))
        draw_screen2('NOSTROMO 180246', settings.screen2_font,
                     (settings.width * 0.7, settings.letter_size_screen2 * 3))
        draw_screen2('FUNCTION', settings.screen2_font,
                     (settings.width * 0.7, settings.letter_size_screen2 * 7))
        draw_screen2('TANKER/REFINERY', settings.screen2_font,
                     (settings.width * 0.7, settings.letter_size_screen2 * 8))
        draw_screen2('CAPACITY', settings.screen2_font,
                     (settings.width * 0.7, settings.letter_size_screen2 * 10))
        draw_screen2('200 000 000 TONNES', settings.screen2_font,
                     (settings.width * 0.7, settings.letter_size_screen2 * 11))
        draw_screen2('GALACTIC POSITION', settings.screen2_font,
                     (settings.width * 0.7, settings.letter_size_screen2 * 13))
        draw_screen2('270/RX683*', settings.screen2_font,
                     (settings.width * 0.7, settings.letter_size_screen2 * 14))
        draw_screen2('VELOCITY STATUS', settings.screen2_font,
                     (settings.width * 0.7, settings.letter_size_screen2 * 16))
        draw_screen2('58.09/ 5DL', settings.screen2_font,
                     (settings.width * 0.7, settings.letter_size_screen2 * 17))
        draw_screen2('COMPUTER         JER/12493.D', settings.screen2_font,
                     (settings.width * 0.05, settings.letter_size_screen2))
        draw_screen2('ACTUAL TIME:      3   JUN', settings.screen2_font,
                     (settings.width * 0.05, settings.letter_size_screen2 * 3))
        draw_screen2('FLIGHT TIME:      5   NOV', settings.screen2_font,
                     (settings.width * 0.05, settings.letter_size_screen2 * 4))
        pg.draw.rect(screen, settings.text_colour_screen_1,
                     pg.Rect(settings.width * 0.05, settings.letter_size_screen2 * 6.7, settings.width * 0.6,
                             settings.height * 0.53))

    def draw_pointer():
            pg.draw.rect(lil_screen, settings.text_colour_screen_1, pointer)

    def draw_scroll_text_box(surface, box_rect, show_num_list):
        surface.set_clip(box_rect)
        text_y = box_rect.bottom - settings.screen2_font.get_height() - 5
        for text_surf in reversed(show_num_list[:]):
            if text_y <= box_rect.top:
                show_num_list.remove(text_surf)
            else:
                surface.blit(text_surf, (box_rect.left + 10, text_y))
            text_y -= settings.screen2_font.get_height()
        pg.draw.rect(surface, (settings.bg_color_4), box_rect, 5)
        surface.set_clip(None)



    while True:
        clock.tick(settings.fps)

        start_screen = settings.start_screen
        screen1 = settings.screen1
        screen2 = settings.screen2
        screen3 = settings.screen3

        current_time = pg.time.get_ticks()


        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and start_screen:
                    settings.start_screen = False
                    settings.screen1 = True
                    screen1_time = pg.time.get_ticks()
                if event.key == pg.K_SPACE and screen1:
                    settings.screen1 = False
                    settings.screen2 = True
                    screen2_time = pg.time.get_ticks()
                if  event.key == pg.K_SPACE and screen2:
                    settings.screen2 = False
                    settings.screen3 = True
                    screen3_time = pg.time.get_ticks()


        #print(f'Current time: {current_time}, Time_tick: {time_tick}')


        if start_screen:
            screen.fill(settings.bg_color_1)
            draw_menu('Press SPACE to continue')


        if screen1:
            screen.fill((0, 13, 40))

        if screen1 and current_time - screen1_time > 500:
            screen.fill((0, 13, 40))
            pg.draw.rect(screen, (1, 152, 229),
                         pg.Rect(0, settings.height * 0.7, settings.width,
                                 settings.height * 0.53))
            pg.draw.line(screen, (0, 13, 40), [0, settings.height * 0.9],[settings.width, settings.height * 0.8], 10)


        if screen1 and current_time - screen1_time > 600:
            screen.fill(settings.bg_color_2)
            pg.draw.rect(screen, (0, 13, 40),
                         pg.Rect(0, 0, settings.width,
                                 settings.height * 0.2))
            draw_nostromo('NOSTROMO', settings.screen1_font,
                          (settings.width / 2, settings.height / 2 - settings.letter_size_open * 1.3))
            draw_nostromo('180924609', settings.screen1_font,
                          (settings.width / 2, settings.height / 1.9))


        if screen1 and current_time - screen1_time > 700:
            screen.fill(settings.bg_color_2)
            draw_nostromo('NOSTROMO', settings.screen1_font,
                          (settings.width / 2, settings.height / 2 - settings.letter_size_open * 1.1))
            draw_nostromo('180924609', settings.screen1_font,
                          (settings.width / 2, settings.height / 2))


        if screen2 and current_time - screen2_time < 500:
            screen2_interface()
            lil_screen = pg.Surface((settings.width * 0.56, settings.height * 0.45))
            lil_screen.fill(settings.bg_color_3)
            for j in range(len(show_list)):
                draw_lil_screen(show_list[j][0], settings.screen2_font, show_list[j][1])
            screen.blit(lil_screen, (settings.width * 0.07, settings.letter_size_screen2 * 7.5))
            draw_pointer()
            time_05 = current_time / 1000

        if screen2 and current_time - screen2_time > 1000:
            time_tick = pg.time.get_ticks()/1000
            screen2_interface()
            lil_screen = pg.Surface((settings.width * 0.56, settings.height * 0.45))
            lil_screen.fill(settings.bg_color_3)
            for index, value in enumerate(show_list):
                draw_lil_screen(show_list[index][0], settings.screen2_font, show_list[index][1])
                if time_05 < time_tick and len(lil_screen_list) > 0:
                    time_05 = time_05 + 0.2
                    item = lil_screen_list.pop(-1)
                    show_list.append(item)
                    pointer.left = item[1][0]
                    pointer.bottom = item[1][1] + settings.letter_size_screen2
                draw_pointer()
            screen.blit(lil_screen, (settings.width * 0.07, settings.letter_size_screen2 * 7.5))


        if screen3 and current_time - screen3_time < 2000:
            time_05 = current_time / 1000
            screen.fill(settings.bg_color_3)

        if screen3 and current_time - screen3_time > 2000:
            text_box_rect1 = pg.Rect(20, 20, settings.width/5 - 20, settings.height - 40)
            text_box_rect2 = pg.Rect(20*2 + text_box_rect1.width*1, 20, text_box_rect1.width, settings.height - 40)
            text_box_rect3 = pg.Rect(20*3 + text_box_rect1.width*2, 20, text_box_rect1.width, settings.height - 40)
            text_box_rect4 = pg.Rect(20*4 + text_box_rect1.width*3, 20, text_box_rect1.width, settings.height - 40)
            text_box_rect5 = pg.Rect(20*5 + text_box_rect1.width*4, 20, text_box_rect1.width, settings.height - 40)
            time_tick = pg.time.get_ticks() / 1000
            screen.fill(settings.bg_color_4)

            if time_05 < time_tick:
                show_number = settings.screen2_font.render(choice(num_list), True, (settings.text_colour_screen_1))
                show_number2 = settings.screen2_font.render(choice(num_list), True, (settings.text_colour_screen_1))
                show_number3 = settings.screen2_font.render(choice(num_list), True, (settings.text_colour_screen_1))
                show_number4 = settings.screen2_font.render(choice(num_list), True, (settings.text_colour_screen_1))
                show_number5 = settings.screen2_font.render(choice(num_list), True, (settings.text_colour_screen_1))
                show_num_list1.append(show_number)
                show_num_list2.append(show_number2)
                show_num_list3.append(show_number3)
                show_num_list4.append(show_number4)
                show_num_list5.append(show_number5)

                time_05 = time_05 + 0.25

            draw_scroll_text_box(screen, text_box_rect1, show_num_list1)
            draw_scroll_text_box(screen, text_box_rect2, show_num_list2)
            draw_scroll_text_box(screen, text_box_rect3, show_num_list3)
            draw_scroll_text_box(screen, text_box_rect4, show_num_list4)
            draw_scroll_text_box(screen, text_box_rect5, show_num_list5)

        pg.display.flip()



if __name__ == '__main__':
    run_pc()

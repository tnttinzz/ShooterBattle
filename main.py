import pygame
import sys
from pygame.locals import *

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((900, 700))
    intro_screen = pygame.image.load('pictures/introScreen.png')
    game_screen = pygame.image.load('pictures/select.png')
    current_screen = 'intro'  # Ban đầu, màn hình là intro

    button_rect = pygame.Rect(350, 588, 200, 50)  # Tạo hình chữ nhật đại diện cho nút
    button_hover = False  # Biến để kiểm tra xem chuột có hover trên nút không

    # Load font từ file đã tải về
    font = pygame.font.Font('fonts/VT323-Regular.ttf', 50)

    while True:
        if current_screen == 'intro':
            show_intro_screen(DISPLAYSURF, intro_screen, button_rect, button_hover, font)
        elif current_screen == 'game':
            show_game_screen(DISPLAYSURF, game_screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                # Kiểm tra xem chuột có di chuyển vào hình chữ nhật không
                mouse_x, mouse_y = event.pos
                button_hover = button_rect.collidepoint(mouse_x, mouse_y)

            elif event.type == MOUSEBUTTONDOWN:
                if current_screen == 'intro':
                    # Kiểm tra xem người dùng có click vào nút không
                    mouse_x, mouse_y = event.pos
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        current_screen = 'game'
                        # Chuyển sang màn hình game khi click
                elif current_screen == 'game':
                    # Xử lý sự kiện click trong màn hình game nếu cần
                    pass

        pygame.display.update()

def show_intro_screen(DISPLAYSURF, intro_screen, button_rect, button_hover, font):
    DISPLAYSURF.blit(intro_screen, (0, 0))
    # Tạo một hình chữ nhật với góc được bo tròn và thay đổi màu viền khi chuột hover
    if button_hover:
        pygame.draw.rect(DISPLAYSURF, (128, 128, 128), button_rect, border_radius=10)
    else:
        pygame.draw.rect(DISPLAYSURF, (255, 255, 255), button_rect, border_radius=8, width=2)

    # Tạo một đối tượng văn bản từ font
    text = font.render('OPTIONS', True, (255, 255, 255))
    # Tính toán vị trí để văn bản nằm ở giữa hình chữ nhật
    text_rect = text.get_rect(center=button_rect.center)
    # Vẽ văn bản lên hình chữ nhật
    DISPLAYSURF.blit(text, text_rect.topleft)

    pygame.display.set_caption('Shooter Battle')

def show_game_screen(DISPLAYSURF, game_screen):
    DISPLAYSURF.blit(game_screen, (0, 0))
    pygame.display.set_caption('Game Screen')

if __name__ == "__main__":
    main()

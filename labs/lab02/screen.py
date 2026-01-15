import pygame

pygame.init()

screen_width = 800
screen_height = 600
window_size = (screen_width, screen_height)

screen = pygame.display.set_mode(window_size)  # Создаем окно

bg_color = (255, 255, 255)
screen.fill(bg_color)

font = pygame.font.SysFont(None, 75)
text = font.render("Hello appsec world*", True, (0, 255, 0))
text_rect = text.get_rect()
text_rect.center = (400, 300)
screen.blit(text, text_rect)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

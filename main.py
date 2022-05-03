import game
import pygame
import sys

game = game.Game()
player = 1
game_over = False
pygame.init()
screen = pygame.display.set_mode((game.WIDTH, game.HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(game.BG_COLOR)
game.draw_lines()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // game.SQUARE_SIZE)
            clicked_col = int(mouseX // game.SQUARE_SIZE)

            if game.available_square(clicked_row, clicked_col):

                game.mark_square(clicked_row, clicked_col, player)
                if game.check_win(player):
                    game_over = True
                player = player % 2 + 1

                game.draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game.restart()
                player = 1
                game_over = False

    pygame.display.update()

import pygame
pygame.init()
pygame.mixer.music.load('tiro-perfeito.mp3')
pygame.mixer.music.play()
input("Pressione Enter para terminar a reprodução...")
pygame.mixer.quit()


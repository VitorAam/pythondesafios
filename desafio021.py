import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('rock.mp3')
print('\033[34mBatida bacana essa ein!\033[m')
pygame.mixer.music.play()
pygame.event.wait()

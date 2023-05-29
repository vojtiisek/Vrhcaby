import tkinter as tk
from tkinter import *
import pygame

pygame.mixer.init()
move_sound = pygame.mixer.Sound("move-self.mp3")
capture_sound = pygame.mixer.Sound("capture.mp3")
throw_sound = pygame.mixer.Sound("throw.mp3")
import pyautogui, time, os, logging, sys, random, copy

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.DEBUG) # uncomment to block debug log messages


# Food order constants (don't change these: the image filenames depend on these specific values)
ONIGIRI = 'onigiri'
GUNKAN_MAKI = 'gunkan_maki'
CALIFORNIA_ROLL = 'california_roll'
SALMON_ROLL = 'salmon_roll'
SHRIMP_SUSHI = 'shrimp_sushi'
UNAGI_ROLL = 'unagi_roll'
DRAGON_ROLL = 'dragon_roll'
COMBO = 'combo'
ALL_ORDER_TYPES = (ONIGIRI, GUNKAN_MAKI, CALIFORNIA_ROLL, SALMON_ROLL, SHRIMP_SUSHI, UNAGI_ROLL, DRAGON_ROLL, COMBO)
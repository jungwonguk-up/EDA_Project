import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

path = 'c:/Windows/Fonts/malgun.ttf'

if platform.system() == 'Darwin':
    print('Hangul ok in your mac')
    rc('font', family = 'Arial Unicode MS')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    print('hangul ok in your windows')
    rc('font', family=font_name)


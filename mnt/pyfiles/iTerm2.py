import matplotlib
matplotlib.use("module://imgcat")
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
plt.style.use('../mplstyle/iTerm2.mplstyle')


# font monaco install & setup
fonts = fm.findSystemFonts()
if "/usr/share/fonts/truetype/ttf-monaco/Monaco_Linux.ttf" not in fonts:
    print('Install Font "monaco" ... ')
    import os
    os.system("mkdir -p /usr/share/fonts/truetype/ttf-monaco")
    os.system('wget https://gist.github.com/rogerleite/b50866eb7f7b5950da01ae8927c5bd61/raw/862b6c9437f534d5899e4e68d60f9bf22f356312/mfont.ttf -O - > /usr/share/fonts/truetype/ttf-monaco/Monaco_Linux.ttf')
fm.fontManager.addfont("/usr/share/fonts/truetype/ttf-monaco/Monaco_Linux.ttf")

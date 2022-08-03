import matplotlib
matplotlib.use("module://imgcat")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# font monaco install & setup
fonts = fm.findSystemFonts()
if "/usr/share/fonts/truetype/ttf-monaco/Monaco_Linux.ttf" not in fonts:
    print('Install Font "monaco" ... ')
    import os
    os.system("mkdir -p /usr/share/fonts/truetype/ttf-monaco")
    os.system('wget https://gist.github.com/rogerleite/b50866eb7f7b5950da01ae8927c5bd61/raw/862b6c9437f534d5899e4e68d60f9bf22f356312/mfont.ttf -O - > /usr/share/fonts/truetype/ttf-monaco/Monaco_Linux.ttf')
fm.fontManager.addfont("/usr/share/fonts/truetype/ttf-monaco/Monaco_Linux.ttf")
plt.rcParams["font.family"] = "Monaco"

def setenv(color = "#feffff"):

    plt.rcParams["font.family"] = "Monaco"
    plt.rcParams["font.size"] = 10

    fig = plt.figure(dpi = 300)
    fig.patch.set_alpha(0)

    ax = plt.subplot(1,1,1)

    ax.patch.set_alpha(0)

    # lables colors
    ax.xaxis.label.set_color(color)
    ax.yaxis.label.set_color(color)

    # title colors
    ax.title.set_color(color)

    # axis color
    ax.spines['top'].set_color(color)
    ax.spines['bottom'].set_color(color)
    ax.spines['left'].set_color(color)
    ax.spines['right'].set_color(color)
    ax.tick_params(axis = 'x', colors =color)
    ax.tick_params(axis = 'y', colors = color)

    return fig, ax

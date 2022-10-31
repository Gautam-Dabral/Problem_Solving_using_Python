import pyfiglet
from termcolor import colored

mssg = input('what would you like to print? ')
colour = input('specify a color : ')
color_list = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta','cyan', 'white']

ascii_art = pyfiglet.figlet_format(mssg)

if colour not in color_list:
    colour = 'magenta'
    print(colored_ascii_art)
else:
    print(colored_ascii_art)


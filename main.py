##### Abdominal Provocation Task #####
# This script is used to run the abdominal provocation task 
# Modified from Opdensteinen, K. D., Rach, H., Gruszka, P., Schaan, L., Adolph, D., Melzig, C. A., ... & Hechler, T. (2025). Interoceptive threat in adolescents with chronic pain: Evidence for fear responses during anticipation and provocation of internal bodily sensations. The Journal of Pain, 105449.
# by Sigrid Agersnap Bom Nielsen, PhD-student at Aarhus University, Denmark
# Contact: sigrid@clin.au.dk

# Date: 2025-11-20

# comments / last changes:
#-
#-
#-

# ------------------------------
#    PACKAGES AND FUNCTIONS
# ------------------------------

from helper_functions import *
from instructions import *
from parameters import *
from tutorial import *
from experiment import *

from datetime import datetime
from psychopy import visual, core, gui#, event, sound
# if you have issues installing psychopy, install the packages from dependencies.txt


# ------------------------------
#              GUI
# ------------------------------
# Create a graphical user interface to collect participant info
g = gui.Dlg(title = 'Abdominal Provocation Task')
g.addField('Participant (record ID):', required=True)
g.addField('Group:', choices = ['HC', 'FAPD', 'IBD'], required=True)
g.addField('Tutorial', initial = 'yes', choices = ['yes', 'no'], required=True)
g.show()

# Check whether the user pressed cancel
if not g.OK:
    core.quit()   # or sys.exit() if preferred

participant_id = g.data[0]
participant_group = g.data[1]
show_tutorial = g.data[2]

# ------------------------------
#          MAIN PROGRAM
# ------------------------------
win = visual.Window(fullscr=True, color = default_color, units="pix")
experiment_start = datetime.now()

# Run tutorial if selected, else only run main program
if show_tutorial == 'yes':
    tutorial_data = run_tutorial(win = win)
    experiment_data = run_experiment(win = win)
else:
    tutorial_data = [] 
    show_text_screen(break_text2, allow_skip=True, win = win)  # Welcome screen
    experiment_data = run_experiment(win = win)

# end of experiment
experiment_end = datetime.now()

save_data(
    participant_id,
    participant_group,
    tutorial_data, 
    experiment_data, 
    experiment_start, 
    experiment_end)

win.close()
core.quit()


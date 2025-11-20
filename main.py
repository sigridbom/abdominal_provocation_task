##### Abdominal Tensing Task #####
# This script is used to run the abdominal provocation task 
# Created by: Sigrid Agersnap Bom Nielsen, PhD-student at Aarhus University, Denmark
# Date: 2025-11-20

# comments / last changes:
#-
#-
#-

#------------------------- PACKAGES AND FUNCTIONS -------------------------#

from helper_functions import *
from instructions import *
from parameters import *
from tutorial import *
from experiment import *

from datetime import datetime
from psychopy import visual, core#, event, sound
# if you have issues installing psychopy, install the packages from dependencies.txt

## ------------------USER INPUT ------------------ ##
def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input in ('0', '1'):
            return int(user_input)
        print("Invalid input. Please enter 1 (yes) or 0 (no).")



show_tutorial = get_yes_no_input("Tutorial (1 = yes / 0 = no)?: ")
#participant_ID = input("Participant ID:").strip()

while True:
    participant_id = input("Participant ID:").strip()
    if " " in participant_id:
        print("Invalid ID: spaces are not allowed. Please try again.")
    elif participant_id == "":
        print("Invalid ID: input cannot be empty. Please try again.")
    else:
        break



# ------------------------------
#          MAIN PROGRAM
# ------------------------------
win = visual.Window(fullscr=True, color = default_color, units="pix")
experiment_start = datetime.now()
tutorial_data = []
experiment_data = []


# Run tutorial if selected, else only run main program
if show_tutorial == 1:
    run_tutorial(tutorial_data, participant_id, win = win)
    run_experiment(experiment_data, participant_id, win = win)
else:
    show_text_screen(break_text2, allow_skip=True, win = win)  # Welcome screen
    run_experiment(experiment_data, participant_id, win = win)


# end of experiment
experiment_end = datetime.now()

save_data(
    participant_id, 
    tutorial_data, 
    experiment_data, 
    experiment_start, 
    experiment_end)

win.close()
core.quit()


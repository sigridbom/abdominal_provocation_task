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
from psychopy import visual, core, gui

# ------------------------------
#          MAIN FUNCTION
# ------------------------------
def main():
    # ------------------------------
    #              GUI
    # ------------------------------
    g = gui.Dlg(title='Abdominal Provocation Task')
    g.addField('Participant (record ID):', required=True)
    g.addField('Group:', choices=['HC', 'FAPD', 'IBD'], required=True)
    g.addField('Tutorial:', initial='yes', choices=['yes', 'no'], required=True)
    g.show()

    if not g.OK:
        core.quit()  # Exit cleanly if cancelled

    participant_id = g.data[0]
    group = g.data[1]
    show_tutorial = g.data[2]

    # ------------------------------
    #          CREATE WINDOW
    # ------------------------------
    win = visual.Window(fullscr=True, color=default_color, units="pix")

    try:
        # ------------------------------
        #          RUN EXPERIMENT
        # ------------------------------
        if show_tutorial == 'yes':
            tutorial_data = run_tutorial(win=win)
            run_experiment(participant_id, group, tutorial_data, win=win)
        else:
            tutorial_data = []
        #    show_text_screen(break_text2, allow_skip=True, win=win)  # Welcome screen
            run_experiment(participant_id, group, tutorial_data, win=win)

    finally:
        # Ensure window closes even if experiment crashes
        win.close()
        core.quit()


# ------------------------------
#       EXECUTE MAIN
# ------------------------------
if __name__ == "__main__":
    main()

from helper_functions import *
from instructions import *
from parameters import *
from datetime import datetime
#from psychopy import visual, core, event, sound

def run_tutorial(win = None):
    """
    Displays tutorial text screens and runs practice trials for each trial type.

    Parameters:
    - win: psychopy Window

    Returns:
    - tutorial_data_list: list of dictionaries with tutorial trial data
    """
    tutorial_data_list = []
    tutorial_start_time = datetime.now().strftime("%H:%M:%S")

    for i, text in enumerate(tutorial_texts):
        print(f"Tutorial screen {i+1} of {len(tutorial_texts)}")  # Optional debug
        show_text_screen(text, allow_skip=True, win = win)#, centered=False) 


    for i, trial_type in enumerate(tutorial_trial_types):
        print(f"Running Trial {i+1} — {trial_type.capitalize()}")

        # Get the current template
        practice_phases = trial_templates[trial_type]

        # get trial specific background color
        bg_color = trial_colors[trial_type]  

        show_text_with_countdown(practice_phases["anticipation"], countdown_seconds=anticipation_duration, background_color=bg_color, win = win)

        duration_sec, start_time, end_time = run_provocation_phase_with_timing(
            text=practice_phases["provocation"],
            max_duration=tutorial_provoke_duration,
            background_color=bg_color,
            win = win
        )
        print(f"Practice {trial_type} duration: {duration_sec} seconds")

        show_text_screen(practice_phases["recovery"], wait_time=recovery_duration, win = win)

        question_ratings = run_question_block(questions_exp[trial_type], win)

        if save_tutorial_data:
            # Prepare trial data dictionary
            trial_data = {
                "trial_number": (f"tutorial_{trial_type}_{i + 1}"),
                "trial_type": trial_type,
                "provocation_duration_sec": duration_sec
            #    "provocation_start_time": start_time,
            #    "provocation_end_time": end_time
            }

            # Add VAS ratings to trial data
            trial_data.update(question_ratings)
            tutorial_data_list.append(trial_data)

        show_text_screen(break_text0, wait_time= random_break, win= win) # intertrial interval

    # outro from tutorial text
    show_text_screen(break_text1, allow_skip=True, win = win) 

    return tutorial_data_list

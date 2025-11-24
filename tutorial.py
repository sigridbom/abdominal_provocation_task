from helper_functions import *
from instructions import *
from parameters import *
from datetime import datetime
#from psychopy import visual, core, event, sound

def run_tutorial(win = None):
    """
    Displays tutorial text screens and runs practice trials for each trial type.

    Parameters:
    - tutorial_data_list (list): List to store data.
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

        #questions
        question_ratings = {}
        for idx in questions_exp[trial_type]:
            question = idx.get("question")
            labels = idx.get("labels") or []
            #left_label = idx.get("left_label") or []
            #right_label = idx.get("right_label") or []
            scale_type = idx.get("scale", "VAS")

            rating, rt = show_rating(idx["question"], 
                                 labels=labels,
                            #    left_label = left_label,
                            #    right_label = right_label,
                                scale_type=scale_type,
                                win= win)
            
            # # Convert discrete ratings (e.g., NRS) to integers only
            # if idx.get("scale", "VAS") == "NRS" and rating is not None:
            #     rating = int(round(rating))

            # If rating is a float but represents a whole number, convert to int
            # if isinstance(rating, float) and rating.is_integer():
            #     rating = int(rating)

            question_ratings[idx["type"]] = rating
            question_ratings[f"{idx['type']}_rt"] = rt

            print(f"Response [{trial_type}]: {idx['type']} = {rating}, RT = {rt:.3f}s")


        if save_tutorial_data:
            # Prepare trial data dictionary
            trial_data = {
                "trial_number": (f"tutorial_{trial_type}_{i + 1}"),
                "trial_type": trial_type,
                "provocation_duration_sec": duration_sec,
                "provocation_start_time": start_time,
                "provocation_end_time": end_time
            }

            # Add VAS ratings to trial data
            trial_data.update(question_ratings)
            tutorial_data_list.append(trial_data)
            #save_data(experiment_data, tutorial_data, question_ratings_end) # tilføjelse

   
        show_text_screen(break_text0, wait_time= random_break, win= win) # intertrial interval

    # outro from tutorial text
    show_text_screen(break_text1, allow_skip=True, win = win) 

    return tutorial_data_list

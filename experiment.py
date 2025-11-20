
from helper_functions import *
from instructions import *
from parameters import *

def run_experiment(experiment_data_list, participant_id, trial_types, win = None):
    """
    Runs the main experiment, displaying text screens (with or without countdowns),
    and collecting VAS ratings for each trial type.

    Parameters:
    - experiment_data_list (list): List to store trial data.
    - participant_id (str): From input variable
    - trial_types (list): List of trial types for the experiment, randomized by other function
    - win: PsychoPy window object, is passed when function is called
    
    Returns:
    - experiment_data_list (list): Updated list with trial data.
    """
    
    show_text_screen(break_text3, wait_time=3, win = win)

    for i, trial_type in enumerate(trial_types):
        print(f"Running Trial {i+1} — {trial_type.capitalize()}")

        # Get the current template
        phases = trial_templates[trial_type]

        # get color
        bg_color = trial_colors[trial_type]  # Get the trial-specific color


        # Show anticipation, provocation, recovery
        show_text_with_countdown(phases["anticipation"], countdown_seconds=anticipation_duration, background_color=bg_color, win = win)

        #show_text_with_countdown(phases["provocation"], countdown_seconds=60, allow_skip=True, background_color=bg_color)

        # Run provocation and record timing
        duration_sec, start_time, end_time = run_provocation_phase_with_timing(
            text=phases["provocation"],
            max_duration=exp_provoke_duration,
            background_color=bg_color,
            win = win
        )

        print(f"Trial {i+1} — {trial_type.capitalize()} Duration: {duration_sec} seconds")

        show_text_screen(phases["recovery"], wait_time=recovery_duration, win = win)

        # questions
        question_ratings = {}
        for idx in questions_exp[trial_type]:
            rating, rt = show_rating(idx["question"], idx["labels"], scale_type=idx.get("scale", "VAS"), win = win)
            # Save rating and RT separately
            question_ratings[idx["type"]] = rating
            question_ratings[f"{idx['type']}_rt"] = rt
    
            print(f"Response [{trial_type}]: {idx['type']} = {rating}, RT = {rt:.3f}s")

        # Prepare trial data dictionary
        trial_data = {
            "participant_ID": participant_id,
            "trial_number": i + 1,
            "trial_type": trial_type,
            "provocation_duration_sec": duration_sec,
            "provocation_start_time": start_time,
            "provocation_end_time": end_time
        }

        # Add ratings to trial data
        trial_data.update(question_ratings)
        experiment_data_list.append(trial_data)

        show_text_screen(break_text0, wait_time=random_break, win = win)  # ITI

    return(experiment_data_list)

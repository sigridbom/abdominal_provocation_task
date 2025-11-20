
from helper_functions import *
from instructions import *
from parameters import *

def run_experiment(experiment_data_list, participant_id, win = None):
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

    trial_types = generate_trials(trials_number)

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

        # Collect trial questions using the generic helper - to replace aobve
        #question_ratings = run_question_block(questions_exp[trial_type], win)


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

    
    # ============================
    # END-OF-EXPERIMENT QUESTIONS
    # ============================
    question_ratings_end = {}

    # ------------------------------
    # 1a. Manipulation check #1: Hands
    # ------------------------------
    hands_mc_list = [q for q in questions_manipulation_check if "hands" in q["type"]]
    hands_mc_results = run_question_block(hands_mc_list, win)
    question_ratings_end.update(hands_mc_results)

    # get rating
    hands_mc_rating = hands_mc_results["hands_sensation"]

    # ------------------------------
    # 1b. Hands intensity (conditional)
    # ------------------------------

    intensity_hands = [q for q in questions_intensity if "hands" in q["type"]]
    
    if hands_mc_rating == "Ja":
        intensity_results = run_question_block(intensity_hands, win)
    else:
        intensity_results = {
            intensity_hands[0]["type"]: None,
            f"{intensity_hands[0]['type']}_rt": None
        }

    question_ratings_end.update(intensity_results)

    # ------------------------------
    # 2a. Manipulation check #2: Hands other sensation 
    # ------------------------------

    hands_other_list = [q for q in questions_other_sensation if "hands" in q["type"]]
    hands_other_results = run_question_block(hands_other_list, win)
    question_ratings_end.update(hands_other_results)

    # get rating
    rating = hands_other_results["hands_sensation_other"]

    # ------------------------------
    # 2b. Hands other sensation location (conditional)
    # ------------------------------

    hands_location = [q for q in questions_other_sensation_location if "hands" in q["type"]]

    if rating == "Ja":
        location_results = run_question_block(hands_location, win)
    else:
        location_results = {
            hands_location[0]["type"]: None,
            f"{hands_location[0]['type']}_rt": None
        }

    question_ratings_end.update(location_results)

    # ------------------------------
    # 3. End of experiment questions: Hands
    # ------------------------------

    end_hands_results = run_question_block(questions_end_hands, win)
    question_ratings_end.update(end_hands_results) 

    # ------------------------------
    # 4a.  Manipulation check #1: Abdominal
    # ------------------------------

    abdominal_mc_list = [q for q in questions_manipulation_check if "abdominal" in q["type"]]
    abdominal_mc_results = run_question_block(abdominal_mc_list, win)
    question_ratings_end.update(abdominal_mc_results)

    # get rating
    abdominal_mc_rating = abdominal_mc_results["abdominal_sensation"]
    print(abdominal_mc_rating)

    # ------------------------------
    # 4b. Abdominal intensity (conditional)
    # ------------------------------

    intensity_abdominal = [q for q in questions_intensity if "abdominal" in q["type"]]

    if abdominal_mc_rating == "Ja":
        intensity_results = run_question_block(intensity_abdominal, win)
    else:
        intensity_results = {
            intensity_abdominal[0]["type"]: None,
            f"{intensity_abdominal[0]['type']}_rt": None
        }

    question_ratings_end.update(intensity_results)

    # ------------------------------
    # 5a. Manipulation check #2: Abdominal other sensation 
    # ------------------------------
    abdominal_other_list = [q for q in questions_other_sensation if "abdominal" in q["type"]]
    abdominal_other_results = run_question_block(abdominal_other_list, win)
    question_ratings_end.update(abdominal_other_results)

    # get rating
    rating = abdominal_other_results["abdominal_sensation_other"]

    # ------------------------------
    # 5b. Abdomnial other sensation location (conditional)
    # ------------------------------

    abdominal_location = [q for q in questions_other_sensation_location if "abdominal" in q["type"]]

    if rating == "Ja":
        location_results = run_question_block(abdominal_location, win)
    else:
        location_results = {
            abdominal_location[0]["type"]: None,
            f"{abdominal_location[0]['type']}_rt": None
        }

    question_ratings_end.update(location_results)

    # ------------------------------
    # 6. End of experiment questions: Abdominal
    # ------------------------------

    end_abdominal_results = run_question_block(questions_end_abdominal, win)
    question_ratings_end.update(end_abdominal_results) 

    # ------------------------------
    # 7. Experience questions
    # ------------------------------

    exp_questions = run_question_block(questions_end, win)
    question_ratings_end.update(exp_questions)

    # ------------------------------
    # Save into experiment_data_list
    # ------------------------------
    experiment_data_list.append({
        "participant_ID": participant_id,
        "trial_number": "end",
        "trial_type": "end_questions",
        **question_ratings_end
        })
    
    #End screen
    show_text_screen(end_text, allow_skip=True, win = win)

    return experiment_data_list

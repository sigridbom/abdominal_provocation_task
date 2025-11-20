##### Abdominal Tensing Task #####
# This script is used to run the abdominal tensing task experiment
# Created by: Sigrid Agersnap Bom Nielsen, PhD-student at Aarhus University, Denmark
# Date: 2025-11-20

# comments / last changes:
#-
#-
#-

#------------------------- PACKAGES -------------------------#

from helper_functions import *
from instructions import *
from parameters import *
from tutorial import *
from experiment import *

# importing packages
#import sys, random, os
from datetime import datetime
import pandas as pd
#import pygame
from psychopy import visual, core#, event, sound
# if you have issues installing psychopy, install the packages from dependencies.txt

###### ----------------- Create window and define quit with esc ------------------ ######

def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input in ('0', '1'):
            return int(user_input)
        print("Invalid input. Please enter 1 (yes) or 0 (no).")



##### ----------------- generate random trial sequence------------------ ######

trial_types = generate_trials(trials_number)
print(trial_types) # test
#### ----------------- TEXT ------------------ ######


## ------------------USER INPUT ------------------ ##

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


# --------- MAIN PROGRAM ----------
# # Create a window
win = visual.Window(fullscr=True, color = default_color, units="pix")

experiment_start = datetime.now()

tutorial_data = []
experiment_data = []

# Run tutorial if selected, else only run main program
if show_tutorial == 1:
    run_tutorial(tutorial_data, participant_id, win = win)
    run_experiment(experiment_data, participant_id, trial_types, win = win)
else:
    show_text_screen(break_text2, allow_skip=True, win = win)  # Welcome screen
    run_experiment(experiment_data, participant_id, trial_types, win = win )

# Collect end-of-experiment questions
question_ratings_end = {}

# First: Hands manipulation check
hands_mc = [q for q in questions_manipulation_check if "hands" in q["type"]][0]
rating, rt = show_rating(hands_mc["question"], hands_mc["labels"], scale_type=hands_mc["scale"], win = win)
question_ratings_end[hands_mc["type"]] = rating
question_ratings_end[f"{hands_mc['type']}_rt"] = rt
print(f"Response: {hands_mc['type']} = {rating}, RT = {rt:.3f}s")

# If “Yes”: ask hands intensity
if rating == "Ja":
    hands_intensity_q = [q for q in questions_intensity if "hands" in q["type"]][0]
    rating_int, rt = show_rating(hands_intensity_q["question"], hands_intensity_q["labels"], scale_type=hands_intensity_q["scale"], win = win)
    question_ratings_end[hands_intensity_q["type"]] = rating_int
    question_ratings_end[f"{hands_intensity_q['type']}_rt"] = rt
    print(f"Response: {hands_intensity_q['type']} = {rating_int}, RT = {rt:.3f}s")
elif rating == "Nej":
    hands_intensity_q = [q for q in questions_intensity if "hands" in q["type"]][0]
    rating_int = None
    question_ratings_end[hands_intensity_q["type"]] = rating_int
    question_ratings_end[f"{hands_intensity_q['type']}_rt"] = None
    print(f"Response: {hands_intensity_q['type']} = {rating_int}, RT = None")

# Ask about other sensations
hands_other = [q for q in questions_other_sensation if "hands" in q["type"]][0]
rating_other, rt = show_rating(hands_other["question"], hands_other["labels"], scale_type=hands_other["scale"], win = win)
question_ratings_end[hands_other["type"]] = rating_other
question_ratings_end[f"{hands_other['type']}_rt"] = rt
print(f"Response: {hands_other['type']} = {rating_other}, RT = {rt:.3f}s")

# If “Yes”: ask location
if rating_other == "Ja":
    hands_loc = [q for q in questions_other_sensation_location if "hands" in q["type"]][0]
    rating_loc, rt = show_rating(hands_loc["question"], hands_loc["labels"], scale_type=hands_loc["scale"], win = win)
    question_ratings_end[hands_loc["type"]] = rating_loc
    question_ratings_end[f"{hands_loc['type']}_rt"] = rt
    print(f"Response: {hands_loc['type']} = {rating_loc}, RT = {rt:.3f}s")
elif rating == "Nej":
    hands_loc = [q for q in questions_other_sensation_location if "hands" in q["type"]][0]
    rating_loc = None
    question_ratings_end[hands_loc["type"]] = rating_loc
    question_ratings_end[f"{hands_loc['type']}_rt"] = None
    print(f"Response: {hands_loc['type']} = {rating_loc}, RT = None")

# Ask the end-of-phase hands questions regardless
for q in questions_end_hands:
    rating, rt = show_rating(q["question"], q["labels"], scale_type=q.get("scale"), win = win)
    question_ratings_end[q["type"]] = rating
    question_ratings_end[f"{q['type']}_rt"] = rt
    print(f"Response: {q['type']} = {rating}, RT = {rt:.3f}s")


# Second: Abdominal manipulation check
abd_mc = [q for q in questions_manipulation_check if "abdominal" in q["type"]][0]
rating, rt = show_rating(abd_mc["question"], abd_mc["labels"], scale_type=abd_mc["scale"], win = win)
question_ratings_end[abd_mc["type"]] = rating
question_ratings_end[f"{abd_mc['type']}_rt"] = rt
print(f"Response: {abd_mc['type']} = {rating}, RT = {rt:.3f}s")

# If “Yes”: abdominal follow-ups
if rating == "Ja":
    abd_intensity_q = [q for q in questions_intensity if "abdominal" in q["type"]][0]
    rating_int, rt = show_rating(abd_intensity_q["question"], abd_intensity_q["labels"], scale_type=abd_intensity_q["scale"], win = win)
    question_ratings_end[abd_intensity_q["type"]] = rating_int
    question_ratings_end[f"{abd_intensity_q['type']}_rt"] = rt
    print(f"Response: {abd_intensity_q['type']} = {rating_int}, RT = {rt:.3f}s")
elif rating == "Nej":
    abd_intensity_q = [q for q in questions_intensity if "abdominal" in q["type"]][0]
    rating_int = None
    question_ratings_end[abd_intensity_q["type"]] = rating_int
    question_ratings_end[f"{abd_intensity_q['type']}_rt"] = None
    print(f"Response: {abd_intensity_q['type']} = {rating_int}, RT = None")

# Other sensations
abd_other = [q for q in questions_other_sensation if "abdominal" in q["type"]][0]
rating_other, rt = show_rating(abd_other["question"], abd_other["labels"], scale_type=abd_other["scale"], win = win)
question_ratings_end[abd_other["type"]] = rating_other
question_ratings_end[f"{abd_other['type']}_rt"] = rt
print(f"Response: {abd_other['type']} = {rating_other}, RT = {rt:.3f}s")

# Location if “Yes”
if rating_other == "Ja":
    abd_loc = [q for q in questions_other_sensation_location if "abdominal" in q["type"]][0]
    rating_loc, rt = show_rating(abd_loc["question"], abd_loc["labels"], scale_type=abd_loc["scale"], win = win)
    question_ratings_end[abd_loc["type"]] = rating_loc
    question_ratings_end[f"{abd_loc['type']}_rt"] = rt
    print(f"Response: {abd_loc['type']} = {rating_loc}, RT = {rt:.3f}s")
elif rating == "Nej":
    abd_loc = [q for q in questions_other_sensation_location if "abdominal" in q["type"]][0]
    rating_loc = None
    question_ratings_end[abd_loc["type"]] = rating_loc
    question_ratings_end[f"{abd_loc['type']}_rt"] = None
    print(f"Response: {abd_loc['type']} = {rating_loc}, RT = None")

# Ask end-of-phase abdominal questions regardless
for q in questions_end_abdominal:
    rating, rt = show_rating(q["question"], q["labels"], scale_type=q.get("scale"), win = win)
    question_ratings_end[q["type"]] = rating
    question_ratings_end[f"{q['type']}_rt"] = rt
    print(f"Response: {q['type']} = {rating}, RT = {rt:.3f}s")


# Final global questions
for q in questions_end:
    rating, rt = show_rating(q["question"], q["labels"], scale_type=q.get("scale"), win = win)
    question_ratings_end[q["type"]] = rating
    question_ratings_end[f"{q['type']}_rt"] = rt
    print(f"Response: {q['type']} = {rating}, RT = {rt:.3f}s")


# End screen
show_text_screen(end_text, allow_skip=True, win = win)


experiment_end = datetime.now()

# save data from experiment
save_data(
    participant_id, 
    experiment_data, 
    tutorial_data, 
    question_ratings_end, 
    experiment_start, 
    experiment_end)

win.close()
core.quit()


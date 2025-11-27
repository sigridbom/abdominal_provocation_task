# import packages
import random
import pygame

###### ----------------- setting variables ------------------ ######

trials_number = 6 # trial number in total - must be an even number for balanced randomization - default is 6
exp_provoke_duration = 60  # maximum duration for the provocation phase in the experiment in seconds
tutorial_provoke_duration = 30  # duration for the provocation phase in the tutorial in seconds
tutorial_trial_types = ["hands", "abdominal"]  # for the tutorial, we only use one of each type and we start with hands
anticipation_duration = 6 # anticipation duration in seconds before the provocation phase starts
recovery_duration = 5 # recovery duration in seconds after the provocation phase ends
random_break = random.randint(3, 7)  # Random break between 3 and 7 seconds - intertrial interval

# background colors for each trial type and default color
trial_colors = {
    "hands": "green",
    "abdominal": "blue"
}
default_color = "grey"

save_tutorial_data = True  # Set to True if you want to save tutorial data, False otherwise

####------------------ defining variables you shouldn't change ------------------####

# Define keys
SPACE_KEY = 'space'
ESC_KEY = 'escape'

# Initialize pygame mixer for sound stimulus
pygame.mixer.init()
beep_tone = pygame.mixer.Sound("stimuli/short_beep.wav")



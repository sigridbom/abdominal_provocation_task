import random, os, pandas as pd
from datetime import datetime
from psychopy import visual, core, event, sound

from parameters import *

# always close the window and quit the experiment on ESC key
def check_for_quit(keys, win):
    if ESC_KEY in keys:
        win.close()
        core.quit()

def generate_trials(num_trials):
    """
    Generates a balanced random sequence of trial types ('abdominal' and 'hands'), so that there's never more than two of the same type in a row.

    Parameters:
    - num_trials (int): Total number of trials (must be even).
    Returns:
    - list of str: Randomized trial types.
    """
    assert num_trials % 2 == 0, "Number of trials must be even."

    trial_types = ["abdominal", "hands"] * (num_trials // 2)

    valid = False
    while not valid:
        random.shuffle(trial_types)
        valid = True
        for i in range(2, num_trials):
            if trial_types[i] == trial_types[i-1] == trial_types[i-2]:
                valid = False
                break

    return trial_types


def show_text_screen(text, wait_time=None, allow_skip=False, background_color=None, win = None):
    """
    Shows text on the screen for a specified time or until spacebar is pressed.

    Parameters:
    - text (str): Text to display.
    - wait_time (int or None): Time in seconds to wait before proceeding. If None, waits indefinitely.
    - allow_skip (bool): If True, allows skipping by pressing spacebar
    - background_color (str): Background color for the screen.
    - win : PsychoPy window
    """
    if background_color:
        win.color = background_color
    else:
        win.color = default_color

    message = visual.TextStim(win, text=text, color="white", height=30, wrapWidth=1000)
    message.draw()
    win.flip()

    timer = core.Clock()

    while True:
        keys = event.getKeys()
        check_for_quit(keys, win)

        if SPACE_KEY in keys and allow_skip:
            break
        if wait_time is not None and timer.getTime() > wait_time:
            break


def show_text_with_countdown(text, countdown_seconds, allow_skip=False, background_color=None, win = None):
    """
    Shows text on the screen with countdown timer.

    Parameters:
    - text (str): Text to display.
    - countdown_seconds (int): Total countdown time in seconds.
    - allow_skip (bool): If True, allows skipping by pressing spacebar
    - background_color (str): Background color for the screen.
    - win : PsychoPy window
    """
    if background_color:
        win.color = background_color
    else:
        win.color = default_color

    timer = core.Clock()

    while True:
        elapsed = timer.getTime()
        remaining = countdown_seconds - elapsed
        if remaining <= 0:
            break

        main_text = visual.TextStim(win, text=text, pos=(0, 100), color="white", height=30, wrapWidth=1000)
        timer_text = visual.TextStim(win, text=f"{int(remaining)} sekunder", pos=(0, -60), color="white", height=30) #-100 før

        main_text.draw()
        timer_text.draw()
        win.flip()

        keys = event.getKeys()
        check_for_quit(keys, win)

        if allow_skip and SPACE_KEY in keys:
            break


def show_rating(question, labels, scale_type="VAS", win = None):
    """
    Displays a rating or free-text response depending on scale_type.
    Parameters:
        question (str): The question to display.
        labels (list of str): Labels for the scale.
        scale_type (str): One of "VAS", "NRS", "BINARY", "MULTIPLE", "FREE_TEXT".
        win : PsychoPy window
    Returns:
        response/rating (float, int, or str)
        reaction time (float, seconds)
    """
    scale_type = scale_type.upper()
    response_clock = core.Clock()
    response_clock.reset()
    response = None

    # Question text
    question_text = visual.TextBox2(
        win,
        text=question,
        pos=(0, 200),
        color="white",
        letterHeight=30,
        size=(1000, None),
        units="pix",
        alignment="center",
        bold=False
    )

    # ------------------- VAS -------------------
    if scale_type == "VAS":
        slider = visual.Slider(
            win, ticks=(0, 100), labels=labels,
            granularity=0, size=(600, 50), pos=(0, 0),
            labelHeight=25, style='rating', color='white',
            markerColor='red'
        )

        while response is None:
            question_text.draw()
            slider.draw()
            win.flip()
            keys = event.getKeys()
            check_for_quit(keys, win)
            if slider.getRating() is not None:
                response = round(slider.getRating(), 5)

        rt = round(response_clock.getTime(), 5)
        return response, rt

    # ------------------- NRS -------------------
    elif scale_type == "NRS":
        slider = visual.Slider(
            win, ticks=list(range(11)),
            labels=[str(i) for i in range(11)],
            granularity=1, size=(600, 50), pos=(0, 0),
            labelHeight=25, style='rating', color='white',
            markerColor='red'
        )

        left_label_stim = visual.TextStim(win, text=labels[0], pos=(-370, -95),
                                          height=25, color='white')
        right_label_stim = visual.TextStim(win, text=labels[1], pos=(400, -95),
                                           height=25, color='white')

        while response is None:
            question_text.draw()
            slider.draw()
            left_label_stim.draw()
            right_label_stim.draw()
            win.flip()
            keys = event.getKeys()
            check_for_quit(keys, win)
            if slider.getRating() is not None:
                response = slider.getRating()

        rt = round(response_clock.getTime(), 5)
        return response, rt

    # ------------------- BINARY -------------------
    elif scale_type == "BINARY":
        slider = visual.Slider(
            win, ticks=[1, 0], labels=labels,
            granularity=1, size=(400, 50), pos=(0, 0),
            labelHeight=25, style='radio',
            color='white', markerColor='red'
        )

        response_clock = core.Clock()
        response_clock.reset()
        response = None

        while response is None:
            question_text.draw()
            slider.draw()
            win.flip()
            keys = event.getKeys()
            check_for_quit(keys, win)

            val = slider.getRating()
            if val is not None:
                if val == labels[0]: # if answer is first option: 'Ja'
                    response = '1'
                elif val == labels[1]: # if answer is second option: 'Nej'
                    response = '0'
                #response = val  # directly take the label
        rt = round(response_clock.getTime(), 5)
        
        return response, rt


    # ------------------- MULTIPLE -------------------
    elif scale_type == "MULTIPLE":
        slider = visual.Slider(
            win, ticks=list(range(len(labels))), labels=labels,
            granularity=1, size=(400, 50), pos=(0, 0),
            labelHeight=24, style='radio', color='white',
            markerColor='red'
        )

        while response is None:
            question_text.draw()
            slider.draw()
            win.flip()
            keys = event.getKeys()
            check_for_quit(keys, win)
            if slider.getRating() is not None:
                idx = int(slider.getRating())
                response = labels[idx]  # return selected label

        rt = round(response_clock.getTime(), 5)
        return response, rt

    # ------------------- FREE_TEXT -------------------
    elif scale_type == "FREE_TEXT":
        event.clearEvents()  # clear previous keypresses
        response_box = visual.TextBox2(
            win,
            text="",
            pos=(0, -50),
            placeholder=labels or "Skriv dit svar her:",
            alignment="left",   # cursor starts on left
            letterHeight=28,
            size=(900, 120),
            color="white",
            borderColor="white",
            editable=True
        )

        submit_msg = visual.TextStim(
            win,
            text="Tryk ENTER for at fortsætte",
            pos=(0, -140),
            color="white",
            height=24
        )
        response = None

        while True:
            question_text.draw()
            response_box.draw()
#            text_input.draw()
            submit_msg.draw()
            win.flip()

            keys = event.getKeys()
            check_for_quit(keys, win)

            if "return" in keys:
                #typed = text_input.text.strip()
                typed = response_box.text.strip()
                if len(typed) > 0:  # do not allow empty response
                    response = typed
                    break

        rt = round(response_clock.getTime(), 5)
        return response, rt

    else:
        raise ValueError(f"Unknown scale_type: {scale_type}")

def run_question_block(question_list, win):
    """
    Presents each question in question_list and returns a dict containing
    ratings and RTs under keys '<type>' and '<type>_rt'.

    Parameters
    ----------
    question_list : list of dict
        Must include 'question', 'labels', 'type', and 'scale'.

    win : PsychoPy window

    Returns
    -------
    dict (results)
        {'<type>': rating, '<type>_rt': rt}
    """

    results = {}

    for q in question_list:
        rating, rt = show_rating(
            q["question"],
            q["labels"],
            scale_type=q.get("scale", "VAS"),
            win=win
        )

        qtype = q["type"]
        results[qtype] = rating
        results[f"{qtype}_rt"] = rt

        if rt is not None:
            print(f"Response: {qtype} = {rating}, RT = {rt:.5f}s")
        else:
            print(f"Response: {qtype} = {rating}, RT = None")

    return results


def run_provocation_phase_with_timing(text, max_duration, background_color=None, win = None):
    """
    Displays a provocation screen for a maximum duration.

    Parameters:
    - text (str): Instruction text displayed during provocation.
    - max_duration (int): Maximum duration of provocation in seconds.
    - background_color (str): Background color for the screen.
    - win : PsychoPy window
    Returns:
    - actual_duration (float): Actual duration of provocation in seconds
    - start_time (str): Start time as HH:MM:SS
    - end_time (str): End time as HH:MM:SS
    """
    if background_color:
        win.color = background_color
    else:
        win.color = default_color

    #play sound
    beep_tone.play()

    # Start clock and mark time
    provocation_timer = core.Clock()
    start_time = datetime.now()

    actual_duration = None

    while True:
        elapsed = round(provocation_timer.getTime(), 5)
        remaining = max_duration - elapsed
        if remaining <= 0:
            break

        # Draw provocation message (commented out timer text is with visible countdown)
        main_text = visual.TextStim(win, text=text, pos=(0, 100), color="white", height=30, wrapWidth=1000)
       # timer_text = visual.TextStim(win, text=f"{int(remaining)} sekunder", pos=(0, -60), color="white", height=30)

        main_text.draw()
      #  timer_text.draw()
        win.flip()

        keys = event.getKeys()
        check_for_quit(keys, win)

        if SPACE_KEY in keys:
            actual_duration = elapsed
            break

    end_time = datetime.now()
    beep_tone.play() #play at end of provocation phase

    # Calculate actual duration in seconds
    if actual_duration is None:
        actual_duration = max_duration

    return actual_duration, start_time.strftime("%H:%M:%S"), end_time.strftime("%H:%M:%S")

def save_data(participant_id, group, tutorial_data, experiment_data, exp_start, exp_end):
    '''
    Saves the combined tutorial and experiment data to a CSV file with metadata.
    Parameters:
    - participant_id (str): Participant identifier.
    - group (str): Participant group.
    - tutorial_data (list of dict): Data from the tutorial phase.
    - experiment_data (list of dict): Data from the experiment phase.
    - exp_start (datetime): Experiment start time.
    - exp_end (datetime): Experiment end time.    
    '''

    if save_tutorial_data:
        all_data = tutorial_data + experiment_data
    else:
        all_data = experiment_data

    #all_data = experiment_data
    df = pd.DataFrame(all_data)

    # Fix rating column types: convert floats that represent integers
    for col in df.columns:
        if col.endswith("_rt"):
            continue  # skip reaction time columns
        if pd.api.types.is_float_dtype(df[col]):
            # Convert if all non-missing values are integers
            col_values = df[col].dropna()
            if all(float(v).is_integer() for v in col_values):
                df[col] = df[col].astype("Int64")  # Nullable integer

    timestamp = exp_start.strftime('%Y%m%d_%H%M')

    # Add metadata columns
    df["experiment_date"] = exp_start.strftime("%Y-%m-%d")
    df["experiment_start_time"] = exp_start.strftime("%H:%M:%S")
    df["experiment_end_time"] = exp_end.strftime("%H:%M:%S")
    df['participant_id'] = participant_id
    df['group'] = group

    # rearrange columns
    first_columns = ['participant_id', 'group', 'experiment_date', 'experiment_start_time', 'experiment_end_time']
    new_order = first_columns + [col for col in df.columns if col not in first_columns]
    df = df.reindex(columns=new_order)

    # Determine path one level above the current script
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Ensure 'data' directory exists one level above
    data_folder = os.path.join(base_dir, "data")
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    # Save DataFrame to CSV
    filename = f"recordid_{participant_id}_{group}_provocation_{timestamp}.csv"
    filepath = os.path.join(data_folder, filename)
    df.to_csv(filepath, index=False)
    print(f"Data saved to {filename}")

# Abdominal provocation task

Simple version of the abdominal provocation task modified from Opdensteinen et al. (2025) to be used in the research project __Cognitive Bias and Interoception in Chronic Abdominal Pain in Youth - the CI-CAP youth project.__

Structure of repo:
```
├── README.md                  <- README file for project
├── scripts                    <- Folder with all scripts
|   └── ...
├── stimuli                    <- Folder with stimuli to run the task
|   └── ...
├── requirements.txt           <- A requirements file of the required packages.
├── run_abdominal.command      <- Clickable file to run task
├── run_abdominal.sh           <- Bash script to run task
├── run_abdominal.bat          <- Bat file to run task on Windows
└── setup_env.sh               <- Bash script to setup virtual environment to run the task
```

### Requirements
PsychoPy at the point of doesn't work with the newest version of Python, so the virtual environment install Python version 3.10.

### How to run on a Macbook
1. Run "chmod +x setup_env.sh" in terminal to make setup_env executionable (if it isn't already)
2. Run "source setup_env.sh" in terminal to create or activate virtual environment and install packages from requirements.txt in that environment
3. Run main by running "python main.py" in terminal or by using the command file (double-click it) or run run_abdominal.sh in the terminal.

### How to run on a Windows:
1. Double-click "setup_env.bat" or by calling it from the command prompt and install packages from requirements.txt
2. Activate the environment by running: call .test_env\Scripts\activate.bat


#### References

Opdensteinen, K. D., Rach, H., Gruszka, P., Schaan, L., Adolph, D., Melzig, C. A., ... & Hechler, T. (2025). Interoceptive threat in adolescents with chronic pain: Evidence for fear responses during anticipation and provocation of internal bodily sensations. The Journal of Pain, 105449.
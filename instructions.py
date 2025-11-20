tutorial_texts = [
        "Velkommen til mave-spændings-eksperimentet. \n\nTryk på mellemrumstasten for at fortsætte.", # screen 1 

        "I dette eksperiment skal du skiftevis knytte dine hænder\n eller spænde i dine mavemuskler. ", # screen 2
        
        "Du skal knytte dine hænder eller spænde dine mavemuskler\n i et minut ad gangen.\n\n"
        "Hvis du ikke kan gøre det så længe, tryk på mellemrumstasten for at vise,\n at du er stoppet.\n\n"
        "Du skal spænde hvad der svarer til 5 på en skala fra 0-10, hvor 0 er, at du slapper af, og 10 er, at du spænder så meget, som du overhovedet kan.\n\n"
        "Husk at trække vejret normalt.\n\n"
        "Du bedes derefter svare på nogle spørgsmål om, hvordan det føltes.\n\n Tryk på mellemrumstasten for at fortsætte.", # screen 3

        "Når skærmen er grøn, skal du knytte dine hænder.\n\nNår skærmen er blå, skal du spænde dine mavemuskler.\n\n" # screen 4
        "Det står altid på skærmen, hvad du skal gøre.\n\n"
        "Når du skal knytte dine hænder eller spænde dine mavemuskler, vil du høre en kort bip tone. Du hører lyden igen, når der er gået et minut, eller hvis du stopper før tid.\n\n",
        
        "Vi starter med en prøverunde.\n\n" # screen 5
        "I prøverunden skal du kun knytte dine hænder eller spænde dine mavemuskler i 30 sekunder.\n\n"
        "Hvis du har nogen spørgsmål, kan du stille dem til forsøgslederen nu.\n\n"
        "Tryk på mellemrumstasten for at starte prøverunden."
    ]

break_text0 = "+" # intertrial stimulus 
break_text1 = "Prøverunden er nu slut. I eksperimentet skal du prøve at spænde dine mavemuskler eller knytte dine hænder i et minut.\n\n" \
"Hvis du ikke kan gøre det så længe, så tryk på mellemrumstasten for at vise, at du er holdt op.\n\n" \
"Tryk på mellemrumstasten, når du er klar til at starte eksperimentet."
break_text2 = "Velkommen til mave-spændings-eksperimentet. \n\nTryk på mellemrumstasten for at fortsætte."
break_text3 = "Eksperimentet starter nu"
end_text = "Eksperimentet er nu slut.\n\nTak for din deltagelse!\n\nTryk på mellemrumstasten for at afslutte."


trial_templates = {
    "abdominal": {
        "anticipation": "Gør dig klar. Om lidt skal du spænde i dine mavemuskler.",
        "provocation": "Spænd i dine mavemuskler nu.\n\nHvis du ikke kan spænde mere, så tryk på mellemrumstasten.",
        "recovery": "Slap af i dine mavemuskler"
    },
    "hands": {
        "anticipation": "Gør dig klar. Om lidt skal du knytte dine hænder.",
        "provocation": "Knyt dine hænder nu.\n\nHvis du ikke kan knytte dine hænder længere, så tryk på mellemrumstasten.",
        "recovery": "Slap af i dine hænder"
    }
}

questions_exp = {
    "abdominal": [
        {
            "question": "Blev du bange, <i>før</i> du skulle spænde dine mavemuskler?",
            "labels": ["Slet ikke", "Meget bange"],
            "type": "fear_pre",
            "scale": "NRS"
        },
        {
            "question": "Blev du bange, <i>da</i> du spændte dine mavemuskler?",
            "labels": ["Slet ikke", "Meget bange"],
            "type": "fear_during",
            "scale": "NRS"
        },
        {
            #"question": "Hvor stærkt var dit ønske om at undgå at spænde dine mavemuskler?",
            #"labels": ["Ikke spor stærkt", "Meget stærkt"],
            "question": "Ville du gerne undgå at spænde dine mavemuskler?",
            "labels": ["Slet ikke", "Rigtig meget"],
            "type": "avoidance",
            "scale": "VAS"
        },
        {
            #"question": "Hvor stærkt var dit ønske om at stoppe med at spænde mavemusklerne før tid?",
            #"labels": ["Ikke spor stærkt", "Meget stærkt"],
            "question": "Ville du gerne stoppe med at spænde mavemusklerne før tid?",
            "labels": ["Slet ikke", "Rigtig meget"],
            "type": "leave_situation",
            "scale": "VAS"
        }
    ],
    "hands": [
        {
            "question": "Blev du bange, <i>før</i> du skulle knytte dine hænder?",
            "labels": ["Slet ikke", "Meget bange"],
            "type": "fear_pre",
            "scale": "NRS"
        },
        {
            "question": "Blev du bange, <i>da</i> du knyttede dine hænder?",
            "labels": ["Slet ikke", "Meget bange"],
            "type": "fear_during",
            "scale": "NRS"
        },
        {
            #"question": "Hvor stærkt var dit ønske om at undgå at knytte dine hænder?",
            #"labels": ["Ikke spor stærkt", "Meget stærkt"],
            "question": "Ville du gerne undgå at knytte dine hænder?",
            "labels": ["Slet ikke", "Rigtig meget"],
            "type": "avoidance",
            "scale": "VAS"
        },
        {
           # "question": "Hvor stærkt var dit ønske om at stoppe med at knytte hænderne før tid?",
           # "labels": ["Ikke spor stærkt", "Meget stærkt"],
            "question": "Ville du gerne stoppe med at knytte hænderne før tid?",
            "labels": ["Slet ikke", "Rigtig meget"],
            "type": "leave_situation",
            "scale": "VAS"
        }
    ]
}

questions_manipulation_check = [
    {
        "question": "Kunne du mærke dine hænder, da du knyttede dem?",
        "labels": ["Ja", "Nej"],
        "type": "hands_sensation",
        "scale": "BINARY"
    },
    {
        "question": "Kunne du mærke dine mavemuskler, da du spændte dem?",
        "labels": ["Ja", "Nej"],
        "type": "abdominal_sensation",
        "scale": "BINARY"
    }
]

questions_intensity= [
    {"question": "Hvor kraftig var denne fornemmelse i dine hænder?",
        "labels": ["Ikke spor kraftig", "Meget kraftig"],
        "type": "hands_intensity",
        "scale": "VAS"
    },
    {"question": "Hvor kraftig var denne fornemmelse i din mave?",
        "labels": ["Ikke spor kraftig", "Meget kraftig"],
        "type": "abdominal_intensity",
        "scale": "VAS"
    }
]

questions_other_sensation = [
    {"question": "Kunne du mærke noget et andet sted i din krop?",
        "labels": ["Ja", "Nej"],
        "type": "hands_sensation_other",
        "scale": "BINARY"
    },
    {"question": "Kunne du mærke noget et andet sted i din krop?",
        "labels": ["Ja", "Nej"],
        "type": "abdominal_sensation_other",
        "scale": "BINARY"
    },
]

questions_other_sensation_location = [
    {"question": "Hvor i din krop kunne du mærke denne fornemmelse?",
    "labels": "Skriv dit svar her",
    "type": "hands_localization",
    "scale": "FREE_TEXT"
    },
    {"question": "Hvor i din krop kunne du mærke denne fornemmelse?",
        "labels": "Skriv dit svar her",
        "type": "abdominal_localization",
        "scale": "FREE_TEXT"
    }
]

questions_end_hands = [
    {
        #"question": "Føles det at knytte dine hænder ligesom det, du normalt føler, før du får ondt?",
        "question": "Nogen gange kan man mærke noget i kroppen, lige før man får ondt.\nFøles det at knytte dine hænder på samme måde?",
        "labels": ["Slet ikke", "Rigtig meget"],
        "type": "hands_similarity",
        "scale": "VAS"
    },
     {
        "question": "Hvor ondt gjorde det, når du knyttede dine hænder?",
        "labels": ["Ingen smerter", "Værst tænkelige smerter"],
        "type": "hands_pain",
        "scale": "NRS"
    }
]

questions_end_abdominal = [
     {
       # "question": "Føles det at spænde dine mavemuskler ligesom det, du normalt føler, før du får ondt?",
        "question": "Nogen gange kan man mærke noget i kroppen, lige før man får ondt.\nFøles det at spænde maven på samme måde?",
        "labels": ["Slet ikke", "Rigtig meget"],
        "type": "abdominal_similarity",
        "scale": "VAS"
    },
    {
        "question": "Hvor ondt gjorde det, når du spændte dine mavemuskler?",
        "labels": ["Ingen smerter", "Værst tænkelige smerter"],
        "type": "abdomen_pain",
        "scale": "NRS"
    }
]

questions_end = [
    {
        "question": "Hvor svær, synes du, opgaven var?",
        "labels": ["Ikke svær", "Meget svær"],
        "type": "difficulty",
        "scale": "VAS"
    },
    {
        "question": "Hvor ubehagelig, synes du, opgaven var?",
        "labels": ["Ikke ubehagelig", "Meget ubehagelig"],
        "type": "discomfort",
        "scale": "VAS"
    }
]
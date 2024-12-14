# Variables used global
state = "startup"
current_language = "english"  #default language

#file paths for sounds
SOUNDS = {
    "intro": "resources/sounds/intro.mp3", # Key: "intro_english", Value: path to an English intro sound file,
    "outro": "resources/sounds/outro.mp3",
    "volume_up": "resources/sounds/volume_up.mp3",
    "volume_down": "resources/sounds/volume_down.mp3",
    "language_change": "resources/sounds/language_change.mp3"
}

#file paths 
PROMPTS = {
    "english": {
        #"It’s almost bedtime, but I have a fun idea! Want to make your very OWN bedtime story? You get to choose everything! Let’s do it together!
        "intro": "resources/sounds/eng_prompts/intro.mp3",
        #"Okay, little dreamer, it’s time for bed! Close your eyes, snuggle tight, and get ready for amazing dreams. Your next adventure starts tomorrow. Sweet dreams, and goodnight!"
        "goodnight": "resources/sounds/eng_prompts/goodnight.mp3",
        #"Who should be the hero of our story? An elephant? An octopus? Or a turtle? Tap your favorite buddy to get started!"
        "choose_main_character": "resources/sounds/eng_prompts/choose_main_character.mp3",
        #WOoh, where should our story happen? In a wild  jungle? Way up in outer space with stars and planets? Or inside a magical, sparkly castle? Pick your favourite place, and I’ll take you there!
        "choose_place": "resources/sounds/eng_prompts/choose_place.mp3",
        #Every story needs a mission! What should our hero do? Look for a treasure? Help a friend who needs a little extra help? Or go on a, fun adventure? Tap the adventure you want to start!
        "choose_mission": "resources/sounds/eng_prompts/choose_mission.mp3",
        #Every hero needs a buddy! Who should be the best friend in this story? An owl? A dolphin? Or a duck? Pick a friend for a main character
        "choose_friend": "resources/sounds/eng_prompts/choose_friend.mp3",
        #Ooooh, let’s make this story EXTRA special with a twist! What should we add? A big surprise?A secret talent nobody knew about? Or a jolly Christmas twist with snow and presents? Tap to pick your twist — it’s gonna be fun!
        "choose_twist": "resources/sounds/eng_prompts/choose_twist.mp3",
        #Whoa, that story was awesome! Want to keep going and see what happens next? Click yes or no button to decide.
        "continue_story": "resources/sounds/eng_prompts/continue_story.mp3",
        #Do you want to make another story with brand new adventures and characters? Click yes or no button to decide, little dreamer. 
        "new_story": "resources/sounds/eng_prompts/new_story.mp3"
    },
    "polish": {
        #Już prawie pora spać, ale mam super pomysł! Chcesz stworzyć swoją WŁASNĄ bajkę na dobranoc? Możesz wybrać wszystko! Zróbmy to razem!
        "intro": "resources/sounds/pol_prompts/intro.mp3",
        #No dobrze, mały marzycielu, czas do łóżka! Zamknij oczka, przytul się mocno i przygotuj na niesamowite sny. Twoja kolejna przygoda zaczyna się jutro. Słodkich snów i dobranoc!
        "goodnight": "resources/sounds/pol_prompts/goodnight.mp3",
        #Kto powinien być bohaterem naszej historii? Słonik? Ośmiornica? A może żółwik? Wybierz swojego ulubionego przyjaciela, aby zacząć!
        "choose_main_character": "resources/sounds/pol_prompts/choose_main_character.mp3",
        #Gdzie powinna dziać się nasza opowieść? W dzikiej dżungli? Wysoko w kosmosie, wśród gwiazd i planet? A może w magicznym zamku? Wybierz swoje ulubione miejsce, a ja cię tam zabiorę!
        "choose_place": "resources/sounds/pol_prompts/choose_place.mp3",
        #Każda opowieść potrzebuje misji! Co nasz bohater powinien zrobić? Szukać skarbu? Pomóc przyjacielowi, który potrzebuje pomocy? A może wyruszyć na pełną przygód wyprawę? Stuknij misję, którą chcesz rozpocząć!
        "choose_mission": "resources/sounds/pol_prompts/choose_mission.mp3",
        #Każdy bohater potrzebuje przyjaciela! Kto powinien być najlepszym kumplem w tej historii? Sowa? Delfin? A może kaczuszka? Wybierz przyjaciela dla głównego bohatera!
        "choose_friend": "resources/sounds/pol_prompts/choose_friend.mp3",
        #Dodajmy do historii coś wyjątkowego! Co to będzie? Zupełnie niespodziewany zwrot akcji? Ukryty talent, o którym nikt nie wiedział? A może pojawi się tajemniczy wróg? Stuknij, aby wybrać zwrot akcji — to będzie ekscytujące!
        "choose_twist": "resources/sounds/pol_prompts/choose_twist.mp3",
        #Wow, ta historia była niesamowita! Chcesz kontynuować i zobaczyć, co będzie dalej? Kliknij przycisk tak lub nie aby zadecydować.
        "continue_story": "resources/sounds/pol_prompts/continue_story.mp3",
        #Chcesz stworzyć nową opowieść z zupełnie nowymi przygodami i postaciami? Kliknij TAK, aby rozpocząć nową bajkę! Kliknij NIE, jeśli chcesz iść spać. Decyzja należy do ciebie, mały marzycielu!
        "new_story": "resources/sounds/pol_prompts/new_story.mp3"
    }
}

#default options (easily changeable for customization)
main_character = {22: "an elephant", 23: "a octopus", 24: "a turtle"}
place = {22: "jungle", 23: "space", 24: "castle"}
mission = {22: "finding treasure", 23: "helping friend", 24: "adventure"}
friend = {22: "an owl", 23: "a dolphin", 24: "a duck"}
twist = {22: "random twist", 23: "hidden talent", 24: "mysterious enemy"}

functional_pins = {
    'yes': 1,
    'play/pause': 7,
    'no': 8,
    'volume_down': 6,
    'volume_up': 5,
    'language': 17
}

button_event_map = {
    1 : 'yes',
    5 : 'volume_up',
    6 : 'volume_down',
    7 : 'play_pause',
    8 : 'no',
    17 : 'language',
    22 : 'select_option_row1',
    23 : 'select_option_row2',
    24 : 'select_option_row3',
}
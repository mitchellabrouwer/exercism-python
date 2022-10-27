TRANSLATOR = {3: "Pling", 5: "Plang", 7: "Plong"}


def convert(number):
    sounds = ""

    for [key, sound] in TRANSLATOR.items():
        if number % key == 0:
            sounds += sound

    return sounds if sounds else str(number)

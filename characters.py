CHARACTERS = {
        0 : ("akari", ["akari"])
        1 : ("kyoko", ["kyoko"])
        2 : ("tinatsu", ["tinatsu"])
        3 : ("titose", ["titose"])
        4 : ("ayano", ["ayano"])
        5 : ("sakurako", ["sakurako"])
        6 : ("himawari", ["himawari"])
        7 : ("other", [
            "other_yuri"
            ,"other_face"
            ,"other_other"
            ])
        }

def search(character):
    for id, characters in CHARACTERS:
        if character[1] in characters:
            return character
    return -1

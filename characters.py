CHARACTERS = {
        0 : ("akari", ["akari"]),
        1 : ("kyoko", ["kyoko"]),
        2 : ("tinatsu", ["tinatsu"]),
        3 : ("yui", ["yui"]),
        4 : ("titose", ["titose"]),
        5 : ("ayano", ["ayano"]),
        6 : ("sakurako", ["sakurako"]),
        7 : ("himawari", ["himawari"]),
        8 : ("tomoko", ["tomoko"]),
        9 : ("rise", ["rise"]),
        10 : ("mari", ["mari"]),
        11 : ("hanako", ["hanako"]),
        12 : ("kaede", ["kaede"]),
        13 : ("other", [
            "other_yuri"
            ,"other_face"
            ,"other_other"
            ,"other"
            ])
        }

def search_id(character):
    for id, characters in CHARACTERS.items():
        if character in characters[1]:
            return id 
    return -1

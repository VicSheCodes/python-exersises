def are_you_playing_banjo(name):
    if not name:
        return "Are you playing banjo?"
    if name and name[0].lower() == 'r':
        return name + " plays banjo"
    return name + " does not play banjo"


def test_are_you_playing_banjo():
    print(are_you_playing_banjo('Ryan'))
    print(are_you_playing_banjo('rYan'))
    print(are_you_playing_banjo('R2D2'))
    print(are_you_playing_banjo('Jabba'))
    print(are_you_playing_banjo(''))
    print(are_you_playing_banjo(None))

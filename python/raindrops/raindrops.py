
factors_raindrop_sound = {
    3: 'Pling',
    5: 'Plang',
    7: 'Plong'
}


def convert(number):
    result = []

    for factor, sound in factors_raindrop_sound.items():
        if number % factor == 0:
            result.append(sound)

    return ''.join(result) if len(result) > 0 else str(number)

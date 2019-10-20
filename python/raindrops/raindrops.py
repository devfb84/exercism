
FACTORS_RAINDROP_SOUND = [
    (3, 'Pling'),
    (5, 'Plang'),
    (7, 'Plong')
]


def convert(number):
    result = [sound for factor, sound in FACTORS_RAINDROP_SOUND
              if number % factor == 0]

    return ''.join(result) or str(number)

CARDINALS = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh",
             "twelfth"]
GIFTS = ["and a Partridge in a Pear Tree.", "two Turtle Doves", "three French Hens", "four Calling Birds",
         "five Gold Rings", "six Geese-a-Laying", "seven Swans-a-Swimming", "eight Maids-a-Milking",
         "nine Ladies Dancing", "ten Lords-a-Leaping", "eleven Pipers Piping", "twelve Drummers Drumming"]


def make_verse(verse_number):
    day = CARDINALS[verse_number]
    first_part = f"On the {day} day of Christmas my true love gave to me: "
    rest = ", ".join(reversed(GIFTS[:verse_number + 1]))
    verse = first_part + rest
    if verse_number == 0:
        verse = verse.replace('and ', '')
    return verse


def recite(start_verse, end_verse):
    return [make_verse(verses) for verses in range(start_verse - 1, end_verse)]

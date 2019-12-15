def response(hey_bob):
    hey_bob = hey_bob.strip(' \n\r\t')

    if hey_bob.isupper():
        if hey_bob.endswith("?"):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif hey_bob.endswith("?"):
        return "Sure."
    elif not hey_bob:
        return "Fine. Be that way!"
    else:
        return "Whatever."

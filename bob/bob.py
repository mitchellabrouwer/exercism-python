def response(message: str):
    message = message.strip()
    isShout = message.isupper()
    isQuestion = message.endswith("?")

    if not message:
        return "Fine. Be that way!"
    if isShout and isQuestion:
        return "Calm down, I know what I'm doing!"
    if isQuestion:
        return "Sure."
    if isShout:
        return "Whoa, chill out!"
    return "Whatever."

import re

TAGS = {
    "single": {
        "h1": r"^(#)\s(.*)$",
        "h2": r"^(#{2})\s(.*)$",
        "h3": r"^(#{3})\s(.*)$",
        "h4": r"^(#{4})\s(.*)$",
        "h5": r"^(#{5})\s(.*)$",
        "h6": r"^(#{6})\s(.*)$",
        "li": r"^(\*)\s(.*)$",
        "p": r"^([^<].*)$",
        "strong": r"(.*)__(.*)__(.*)",
        "em": r"(.*)_(.*)_(.*)",
    },
    "group": {
        "ul": r"(<li>.*</li>+)",
    },
}


def replace(tag):
    def replacer(match):
        matches = len(match.groups())
        if matches == 1:
            return f"<{tag}>{match.group(1)}</{tag}>"
        if matches == 2:
            return f"<{tag}>{match.group(2)}</{tag}>"
        elif matches == 3:
            return f"{match.group(1)}<{tag}>{match.group(2)}</{tag}>{match.group(3)}"

    return replacer


def convert(line, tags):
    html = line
    for tag, pattern in tags.items():
        html = re.sub(pattern, replace(tag), html)
    return html


def parse(markdown):
    html = ""
    lines = markdown.splitlines()
    for line in lines:
        html += convert(line, TAGS["single"])

    return convert(html, TAGS["group"])

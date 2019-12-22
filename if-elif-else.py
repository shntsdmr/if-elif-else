text = "sahin asdemir"
if text.endswith("asdemir"):
    text = text.replace("asdemir","tasdemir")
text = text.title()
text = "-".join(list(text))
print(text)

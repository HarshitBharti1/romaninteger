#rule: add each letter's value, but if a letter is smaller than the letter after it.

Values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def roman_to_int(text):
    """Return value steps or none 0 for empty text or a letter that is not Roman."""
    text = text.strip().upper()
    if text == "":
        return None, 0
    total = 0
    steps = 0
    for i in range(len(text)):
        value = Values[text[i]]
        if i + 1 < len(text) and value < Values[text[i + 1]]:
            total = total - value
        else:
            total = total + value
        steps = steps + 1
    return total, steps

def show(text):
    value, steps, = roman_to_int(text)
    if value is None:
        print(f"  '{text}' is not a roman numeral")
    else:
        print(f"{text:>10} = {value:<5} steps = {steps}")

for numeral in ["III", "IX", "LVIII", "LXXV11", "MCMXCIV", "xiv"]:
    show(numeral)

print()
try:
    typed = input("Type a roman numeral or press enter to finish").strip()
except EOFError:
    typed = ""
if typed == "":
    print("No numeral checked.")
else:
    show(typed)
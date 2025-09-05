text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)

words = text.split()  # делим на слова
fin_text = []

for word in words:
    if word.endswith((".", ",")):
        fin_text.append(word[:-1] + "ing" + word[-1])  # вернули знак обратно
    else:
        fin_text.append(word + "ing")

print(" ".join(fin_text))

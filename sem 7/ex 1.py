
def check_rhythm(poem):
    words = poem.split()
    syllables = []
    for word in words:
        syllable_count = word.count('а') + word.count('е') + word.count('ё') + word.count('и') + word.count('о') + word.count('у') + word.count('ы') + word.count('э') + word.count('ю') + word.count('я')
        syllables.append(syllable_count)
    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

poem = input("Введите стихотворение Винни-Пуха: ")

result = check_rhythm(poem)
print(result)
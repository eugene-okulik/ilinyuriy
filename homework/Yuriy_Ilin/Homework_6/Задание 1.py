s = ('''Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
Integer urna nisl, facilisis vitae semper at, dignissim vitae libero''')

lst_words = s.split()

lst_mod = []
for i in lst_words:
    if i[-1] not in ".,":  # Можно расширить список символов, которые должны быть оставлены в конце слова
        lst_mod.append(i + 'ing')
    else:
        lst_mod.append(i[:-1] + 'ing' + i[-1])

print(' '.join(lst_mod))

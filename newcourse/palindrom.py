word = 'racecar'
word_length = len(word)

p_flag = True

for x in range(word_length):
    if word[x] != word[word_length-1-x]:
        p_flag =False
        print(f'{word} is not palondrom')
        break
    else:
        p_flag = True
        print(f'{word} is a palondrom')
        break
        
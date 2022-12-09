
export function oneword(word) {
    if (word.includes(' ')) {
        return word.split(' ')[0]
    } else {
        return word
    }
}

// if ' ' not in word:
// return word
// else:
// splitted = word.split(" ")
// one_word = splitted[0]
// return one_word

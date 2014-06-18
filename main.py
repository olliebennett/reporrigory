from weightings import levenshtein


def load_datfile(filename):

    return open(filename).read().splitlines()


def get_best_weighting(string1, string2):
    """
    Get minimum weighting, between any combination of words in two strings.
    """

    min_score = -1
    for word1 in string1.split(" "):
        for word2 in string2.split(" "):
            lev = levenshtein(word1, word2)
            if lev < min_score or min_score == -1:
                min_score = lev

    return min_score


def findBestFoodMatch(food, bands):
    maxVal = -1
    maxId = 0
    for j in range(len(bands)):
        curVal = get_best_weighting(''.join(food), ''.join(bands[j]))
        if (curVal < maxVal or maxVal == -1):
            maxVal = curVal
            maxId = j
    return maxId


def get_weighting(word1, word2):

    return "hello"


if __name__ == "__main__":
    foods = load_datfile('data/foodlist.txt')
    bands = load_datfile('data/bands.txt')
    for i in range(len(foods)):
        matchid = findBestFoodMatch(foods[i], bands)
        print((foods[i], bands[matchid]))



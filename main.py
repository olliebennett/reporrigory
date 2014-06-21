# Float division (ala Python 3)
from __future__ import division
from weightings import levenshtein, metaphone


def load_datfile(filename):

    return open(filename).read().splitlines()


def get_best_weighting(string1, string2):
    """
    Get minimum weighting, between any combination of words in two strings.
    """

    min_score = -1
    for word1 in string1.split(" "):
        for word2 in string2.split(" "):
            score = get_weighting(word1, word2)
            if score < min_score or min_score == -1:
                min_score = score
    if min_score is -1:
        print('Something went wrong, min_score = -1')
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

def levScore(word1,word2):
    lev = levenshtein(word1, word2)
    if min(len(word1),len(word2)) is 0:
        return 0
    lev_ratio = lev / min(len(word1), len(word2))

    return max(0, 1 - lev_ratio)

def metaphoneScore(word1,word2):
    met1 = metaphone(word1)
    met2 = metaphone(word2)
    return levScore(met1,met2)
    
def get_weighting(word1, word2):
    """
    Return a weighting between 0 (no rhyme) and 1 (identical).
    """
    metscore = metaphoneScore(word1,word2)
    levscore = levScore(word1,word2)
    # Levenshtein Distance (per character)
    return (levscore + metscore/3)/1.333

def show_all(min_score):
    """
    Show all pairs of words above a specified minimum score.
    """
    foods = load_datfile('data/foodlist.txt')
    bands = load_datfile('data/bands.txt')
    for food in foods:
        # print("Processing food:", food)
        for food_word in food.split(" "):
            for band in bands:
                # print("Processing band:", band)
                for band_word in band.split(" "):
                    wt = get_weighting(food_word, band_word)
                    if wt < 0.7 or wt >= 0.925 or abs(wt - 0.813) < 0.001:
                        continue
                    print("%-8s | %-8s | %.3f (%s + %s)" % (food_word, band_word, wt, food, band))


def get_top(n):
    """
    Show only the top n matching pairs (in best-first order).
    """
    foods = load_datfile('data/foodlist.txt')
    bands = load_datfile('data/bands.txt')
    for i in range(len(foods)):
        matchid = findBestFoodMatch(foods[i], bands)
        print((foods[i], bands[matchid]))


if __name__ == "__main__":

    show_all(0.5)

    #get_top(5)

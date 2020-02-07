import numpy as np

def count_specific_word(specific_word, list_words):
    specific_word_count = 0
    for word in list_words:
        if specific_word == word:
            specific_word_count += 1

    return specific_word_count

def count_probability(specific_word_count, all_words_count):
    probability_word = specific_word_count / all_words_count
    return probability_word


def measure_entropy_specific_word(probability_specific_word):
    return probability_specific_word * np.log2(probability_specific_word)


def calculate_entropy_for_all_words(list_words):
    words_calculated = []
    sum_entropies = 0
    amount_tokens = len(list_words)
    for specific_word in list_words:
        if specific_word not in words_calculated:
            specific_word_count = count_specific_word(specific_word, list_words)
            probability_word = count_probability(specific_word_count, amount_tokens)
            entropy_specific_word = measure_entropy_specific_word(probability_word)
            sum_entropies += entropy_specific_word
            words_calculated.append(specific_word)
    return -sum_entropies, amount_tokens
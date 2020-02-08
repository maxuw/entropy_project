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


## ENTROPY RATE

def find_L_value_for_word(word_position, text):
    places_word_in_list = find_word_in_list(text[word_position], text)
    #     print(places_word_in_list)
    #     print(type(places_word_in_list))
    #     print(len(places_word_in_list))

    if len(places_word_in_list) < 2:
        L = 1

    elif places_word_in_list[0] == word_position:
        L = 1

    else:
        places_before = [i for i in places_word_in_list if i < word_position]

        if len(places_before) < 2:

            #             print("places before list:")
            #             print(places_before)

            before_word_max = places_before[0]


        else:
            before_word_max = max(places_before)

        #         print("before_word_max: " + str(before_word_max))
        L = word_position - before_word_max + 1

    return L

def find_word_in_list(word, text):
    return [i for i, x in enumerate(text) if x == word]

def entropy_rate_calculate(text):
    # L_values = []
    right_side = []
    for i in range(len(text)):
        if i == 0:
            pass
        else:
            log2_i = np.log2(i + 1)
            L = find_L_value_for_word(i, text)

            # L_values.append(L)

            right_side.append(log2_i / L)

    sum_right_side = sum(right_side)
    full_equation = sum_right_side / len(text)

    return full_equation
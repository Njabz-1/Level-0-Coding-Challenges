def vowels(string):
    vowels = "aeiouAEIOU"
    vowel_list = []
    for x in string:
        if x in vowels:
            vowel_list.append(x)
    return vowel_list

vowels("the quick brown fox called Ardo")
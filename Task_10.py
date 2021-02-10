def common_letters(word1,word2):
    common = []
    for x in word1:
        if x in word2:
            common.append(x)
    return common
common_letters("peaches","apples")
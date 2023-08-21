# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, lisst):
        initialiazed_word = list(self.word)
        new_list = list()
        new_list2 = list()
        initialiazed_word.sort()
        for word in lisst:
            put_word_in_list = list(word)

            put_word_in_list.sort()
            if put_word_in_list == initialiazed_word:
                new_list.append(word)
            else:
                new_list2.append(word)

        if len(new_list) > 0:
            if new_list[0] in lisst:
                return new_list
        else:
            return []

        # for i in range(0, len(put_word_in_list)):
        # if i < len(put_word_in_list) and i < len(initialiazed_word):
        #     if put_word_in_list[i] == initialiazed_word[i] and len(
        #         put_word_in_list
        #     ) == len(initialiazed_word):
        #         return new_list.append(word)
        #     else:
        #         return new_list


listen = Anagram("listen")
# => ['inlets']
print(listen.match(["google", "enlists", "inlets", "banana"]))

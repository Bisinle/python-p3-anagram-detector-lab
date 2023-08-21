# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, lisst):
        initialiazed_word = list(self.word)
        new_list = list()
        for word in lisst:
            put_word_in_list = list(word)
            if sorted(put_word_in_list) == sorted(initialiazed_word):
                new_list.append(word)

        return new_list if len(new_list) > 0 and new_list[0] in lisst else []


listen = Anagram("listen")
# => ['inlets']
print(listen.match(["google", "enlists", "inlets", "banana"]))

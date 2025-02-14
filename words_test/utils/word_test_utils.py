

class Word_Utils():
    def nombre_mot(self,phrase):
        words = []
        for word in phrase.split():
            words.extend(word.split("'"))
        return words, len(words)

    def nombre_char(self,words):
        nombre_char = 0
        for word in words:
            if "’" in word:
                print(word)
                l = list(word)
                l.remove("’")
                word = ''.join(l)
                print(word)
            nombre_char += len(word)
        return nombre_char

    def occurence_frequency(self,words):
        occurence = {}
        for word in words:
            word = word.lower()
            if word not in occurence:
                occurence[word] = 1
            else:
                occurence[word] += 1

        l = {}
        for i in range(3):
            max = 0
            max_key = ''
            for key, value in occurence.items():
                if value > max:
                    max = value
                    max_key = key
            l[max_key] = max
            occurence.pop(max_key)
        return l

    def to_json(self, phrase):
        words, nbr = self.nombre_mot(phrase)
        char = self.nombre_char(words)
        l = self.occurence_frequency(words)
        my_dict = {
            'nombre de mots': nbr,
            'nombre de char': char,
            'les 3 mots les plus fréquents': l
        }
        return my_dict


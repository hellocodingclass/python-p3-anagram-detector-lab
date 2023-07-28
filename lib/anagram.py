class Anagram:
    def __init__(self, anagram):
        self.anagram=anagram


    def match(self,words):
            anagrams=[]
            for word in words:
                if sorted(word.lower())==sorted(self.anagram.lower()) and word.lower() != self.anagram.lower():
                    anagrams.append(word)
            return anagrams
 
               





listen=Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
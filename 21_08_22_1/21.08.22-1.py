import re
class Morph:
    def __init__(self, *args):
        a = str(args)
        a=a[2:-3]
        input_group = []
        for word in a.split(", "):
            input_group.append(word)
        self.arr = input_group

    def __eq__(self, other):
        if not isinstance(other, str):
            return False
        a = any(map(lambda x: x == other.lower(), self.arr))
        return a

    def __ne__(self, other):
        if not isinstance(other, str):
            return False
        a = all(map(lambda x: x != other.lower(), self.arr))
        return a


    def add_word(self, word):
        if word[:-2] in self.arr[1][:-2] or word[:-3] in self.arr[1][:-2]:
            print("add_works")
            self.arr.append(word)

    def get_words(self):
        return tuple(self.arr)


mw = Morph(
    "программирование, программированию, программированием, программировании, "
    "программирования, программированиям, программированиями, программированиях")

#print(mw.get_words())
####################mw.add_word("прога")
d1 = Morph("связь, связи, связью, связей, связям, связями, связях")
d2 = Morph(" формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах")
d3 = Morph("вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах")
d4 = Morph(" эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах")
d5 = Morph("день, дня, дню, днем, дне, дни, дням, днями, днях")

dict_words = [mw, d1, d2, d3, d4, d5]
text= input()
text = re.sub(r'[–?!,.;"]', "", text)
count=0
for obj in dict_words:
    for word in (text.lower()).split():
        if word in obj.get_words():
            #print(word)
            count+=1

print(count)

print(d1 == "СВЯЗ")

# flash card

class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return f"{self.word}({self.meaning})"

flash = []
while True:
    word = input("enter the word")
    meaning = input("enter the meaning")
    flash.append(flashcard(word,meaning))
    choice = input("do you want to continue ? (y/n)")
    if choice.lower() == 'n':
        break

for i in flash:
    print(i)

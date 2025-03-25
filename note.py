from usableItem import usableItem

class note(usableItem):

    __text = r"""
               .--._.--.
              ( O     O )
              /   . .   \
             .`._______.'.
            /(           )\
          _/  \  \   /  /  \_
       .~   `  \  \ /  /  '   ~.
      {    -.   \  V  /   .-    }
    _ _`.    \  |  |  |  /    .'_ _
    >_       _} |  |  | {_       _<
     /. - ~ ,_-'  .^.  `-_, ~ - .\
             '-'|/   \|`-`
             """

    def __init__(self, itemName, volume, weight):
        super().__init__(itemName, volume, weight)

    def __read(self):
        if(self.__text is not None):
            print("The text of the note is:")
            print(self.__text)
        else:
            print("The note is empty.")

    def __scribble(self, text):
        self.__text = text

    def __clear(self):
        self.__text = None

    def use(self):
        print("What do you want to do with the note?\n1. read, 2. scribble, 3. clear")
        action = int(input())
        match action:
            case 1:
                self.__read()
            case 2:
                print("Input text to write to the note:")
                text = input()
                self.__scribble(text)
            case 3:
                self.__clear()
            
            case _:
                print("Wrong option")
        
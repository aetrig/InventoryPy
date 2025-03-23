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

    def use(self):
        if(self.__text is not None):
            print("The text of the note is:")
            print(self.__text)
        else:
            print("The note is empty.")

    def scribble(self, text):
        self.__text = text

    def clear(self):
        self.__text = None

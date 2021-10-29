from P1 import GuessNumberGameVer1
import random


class GuessNumberGameVer2(GuessNumberGameVer1):

    def __init__(self, *args, **kwargs):
        super(GuessNumberGameVer2, self).__init__(*args, **kwargs)
        self._guesses: list[int] = []
        self._numGuesses: int = 0

    def playGame(self) -> None:
        print(f'GuessNumberGame with min number as {self._minNum}'
              f', max number as {self._maxNum}, max num of tries as {self._maxTries}')
        currentTries = self.getMaxTries()
        win = False
        while currentTries > 0 and not win:
            playerGuess = int(input(f'Please enter a guess between {self._minNum, self._maxNum}:'))
            self._guesses.append(playerGuess)
            self._numGuesses += 1
            if playerGuess == self._correctNum:  # PlayerGuess is correct
                print('Congratulations! That\'s correct')
                win = True
            elif playerGuess > self._correctNum:
                currentTries -= 1
                print(f'Please type a lower number! the number of remaining tries is {currentTries}')
            else:  # PlayerGuess is lower than the answer
                currentTries -= 1
                print(f'Please type a higer number! the number of remaining tries is {currentTries}')
        if not win:
            print('Sorry that you run out of the number of tries')

    def showSpecify(self) -> None:
        order = int(input(f'Enter which guess is in the range [1, {len(self._guesses)}]:'))
        print(self._guesses[order - 1])  # index = order - 1

    def showGuesses(self) -> None:
        print(self._guesses)

    def setNewGame(self) -> None:
        self._guesses = []
        self._numGuesses = 0
        self._correctNum = random.randint(self._minNum, self._maxNum)

    def playGames(self) -> None:
        self.playGame()
        while True:
            print('If you want to play again? type \'y\' to continue or type \'q\' to quit.')
            command = input('Type \'a\' to see all your guesses or \'g\' to see guess on specify play:')
            if command == 'y':
                self.setNewGame()
                self.playGames()
            elif command == 'q':
                exit()
            elif command == 'a':
                self.showGuesses()
            elif command == 'g':
                self.showSpecify()


#                        _oo0oo_
#                       o8888888o
#                       88" . "88
#                       (| -_- |)
#                       0\  =  /0
#                     ___/`---'\___
#                   .' \|     |// '.
#                  / \|||  :  |||// \
#                 / _||||| -:- |||||- \
#                |   | \\  -  /// |   |
#                | \_|  ''\---/''  |_/ |
#                \  .-\__  '-'  ___/-. /
#              ___'. .'  /--.--\  `. .'___
#           ."" '<  `.___\_<|>_/___.' >' "".
#          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#          \  \ `_.   \_ __\ /__ _/   .-` /  /
#      =====`-.____`.___ \_____/___.-`___.-'=====
#                        `=---='

if __name__ == '__main__':
    gng = GuessNumberGameVer2(1, 20, 5)
    gng.playGames()

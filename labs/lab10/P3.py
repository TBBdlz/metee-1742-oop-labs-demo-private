from P2 import GuessNumberGameVer2


class GuessNumberGameVer3(GuessNumberGameVer2):

    def __int__(self, *args, **kwargs):
        super(GuessNumberGameVer2, self).__init__(*args, **kwargs)

    def playGames(self) -> None:
        super().playGame()
        while True:
            print('If you want to play again? type \'y\' to continue or type \'q\' to quit.')
            print('Type \'a\' to see all your guesses or \'g\' to see guess on specify play.')
            print('Type \'v\' to see average or \'m\' to see minimum or \'x\' to see maximum of all your guesses.')
            command = input()
            if command == 'y':
                self.setNewGame()
                self.playGames()
            elif command == 'q':
                exit()
            elif command == 'a':
                self.showGuesses()
            elif command == 'g':
                self.showSpecify()
            elif command == 'x':
                self.guessMax()
            elif command == 'v':
                self.guessAverage()
            elif command == 'm':
                self.guessMin()

    def guessAverage(self) -> None:
        total: int = 0
        for guess in self._guesses:
            total += guess
        average: float = total / len(self._guesses)
        print(f'average guess = {average:.4f}')

    def guessMin(self) -> None:
        print(f'min guess = {min(self._guesses)}')

    def guessMax(self) -> None:
        print(f'max guess = {max(self._guesses)}')


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
    gng = GuessNumberGameVer3(1, 20, 5)
    gng.playGames()

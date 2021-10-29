"""
    GuessNumberGame is fun math game!
    The only rule is to guess correct number within interval
    GuessNumberGameVer1 provide basic function and constructor
    author: Metee Yingyongwatthanakit
    date: 28 October 2021
"""

import random


class GuessNumberGameVer1:

    _numOfGames: int = 0

    def __init__(self, minNum: int = 1, maxNum: int = 10, maxTries: int = 3) -> None:
        self._minNum: int = minNum
        self._maxNum: int = maxNum
        self._maxTries: int = maxTries
        self._correctNum: int = int(random.random() * (maxNum - minNum))
        GuessNumberGameVer1._numOfGames += 1

    def getMinNum(self) -> int:
        return self._minNum

    def setMinNum(self, newMin) -> None:
        self._minNum = newMin
        # set new correct num because min num is now shifted
        self._correctNum = random.randint(self._minNum, self._maxNum)

    def getMaxNum(self) -> int:
        return self._maxNum

    def setMaxNum(self, newMax) -> None:
        self._maxNum = newMax
        # set new correct num because max num is now shifted
        self._correctNum = random.randint(self._minNum, self._maxNum)

    def getMaxTries(self) -> int:
        return self._maxTries

    def setMaxTries(self, newMaxTries) -> None:
        self._maxTries = newMaxTries

    def playGame(self) -> None:
        print(f'GuessNumberGame with min number as {self._minNum}'
              f', max number as {self._maxNum}, max num of tries as {self._maxTries}')
        currentTries = self.getMaxTries()
        win = False
        while currentTries > 0 and not win:
            playerGuess = int(input(f'Please enter a guess between {self._minNum, self._maxNum}:'))
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

    def __str__(self) -> str:
        return f'Guess Number Game:({self._minNum}, {self._maxNum}, {self._maxTries})'

    @classmethod
    def getNumOfGames(cls) -> int:
        return cls._numOfGames


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
    gng1 = GuessNumberGameVer1()
    gng2 = GuessNumberGameVer1(3, 8)
    gng3 = GuessNumberGameVer1(1, 100, 8)
    gng3.playGame()

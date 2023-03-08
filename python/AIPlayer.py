####################################################
# CS4386 Semester B, 2022-2023
# Assignment 1
# Name: CHENG Yin
# Student ID: 56614557
####################################################

import copy
from math import inf as infinity
import random


class AIPlayer(object):
    def __init__(self, name, symbole, isAI=False):
        self.name = name
        self.symbole = symbole
        self.isAI = isAI
        self.score = 0

    def stat(self):
        return self.name + " won " + str(self.won_games) + " games, " + str(self.draw_games) + " draw."

    def __str__(self):
        return self.name

    def get_isAI(self):
        return self.isAI

    def get_symbole(self):
        return self.symbole

    def get_score(self):
        return self.score

    def add_score(self, score):
        self.score += score

    def available_cells(self, state, player):
        cells = []

        for x, row in enumerate(state):
            for y, cell in enumerate(row):
                if (cell is None):
                    cells.append([x, y])
        return cells

    def get_move(self, state, player):
        '''
        Description:
        1. Find available cells from the state using the given function available_cells()
        2. Obtain the Valid Moves for AI that it will only select its valid cells (black or white depends on player)
        3. For each cell in Valid move, count its neigbors
            3.1 if number of neigbor = 2 or 5, -> select the cell
            3.2 if number of neigbor != 2 and != 5 -> find valid move from its neigbors using the function get_neigbor()
                then select random cells in the obtained neigbor array
        '''

        ##########################################################
        print("\nBoard: \n", state)
        ##########################################################

        # Array: Get Valid Move
        def valid_move(games):
            correct_cells = []
            for i in games:
                if (i[0] + i[1]) % 2 == 0:
                    if (player == 'X'):
                        correct_cells.append(i)
                else:
                    if (player == 'O'):
                        correct_cells.append(i)

            ##########################################################
            print("\nCorrect Moves: \n", correct_cells)
            ##########################################################

            return correct_cells

        def get_neigbor(state, valid_move):

            hasNeigbor = []

            for i in valid_move:
                if (i[0] != 0 and i[1] != 0 and i[0] != 5 and i[1] != 5):
                    if (state[i[0]-1][i[1]] != None) or (state[i[0]][i[1]-1] != None) or (state[i[0]+1][i[1]] != None) or (state[i[0]][i[1]+1] != None):
                        hasNeigbor.append(i)
                elif i[0] == 0 and i[1] == 0:
                    if (state[i[0]+1][i[1]] != None) or (state[i[0]][i[1]+1] != None):
                        hasNeigbor.append(i)
                elif i[0] == 0 and i[1] != 0:
                    if (i[1] < 5):
                        if (state[i[0]][i[1]-1] != None) or (state[i[0]+1][i[1]] != None) or (state[i[0]][i[1]+1] != None):
                            hasNeigbor.append(i)
                    else:
                        if (state[i[0]][i[1]-1] != None) or (state[i[0]+1][i[1]] != None):
                            hasNeigbor.append(i)
                elif i[0] != 0 and i[1] == 0:
                    if (i[0] < 5):
                        if (state[i[0]-1][i[1]] != None) or (state[i[0]+1][i[1]] != None) or (state[i[0]][i[1]+1] != None):
                            hasNeigbor.append(i)
                    else:
                        if (state[i[0]-1][i[1]] != None) or (state[i[0]][i[1]+1] != None):
                            hasNeigbor.append(i)

            return hasNeigbor

        def countNeigbor(state, validMoves):

            pos_h_v = []

            for i in validMoves:

                vertical_cnt = 0
                horizontal_cnt = 0

                x = i[0]
                y = i[1]

                for k in range(x-1, -1, -1):
                    if (state[k][y] != None):
                        horizontal_cnt += 1
                    else:
                        break
                for k in range(x + 1, 6):
                    if (state[k][y] != None):
                        horizontal_cnt += 1
                    else:
                        break

                for k in range(y-1, -1, -1):
                    if (state[x][k] != None):
                        vertical_cnt += 1
                    else:
                        break
                for k in range(y + 1, 6):
                    if (state[x][k] != None):
                        vertical_cnt += 1
                    else:
                        break

                pos_h_v.append((i, horizontal_cnt, vertical_cnt))

            return pos_h_v

        def chooseBestMove(neigborCount):
            bestMove = None
            for i in neigborCount:
                if i[1] == 5 or i[2] == 5:
                    bestMove = i[0]
                    ##########################################################
                    print("Best Move with 5: ", bestMove)
                    ##########################################################
                    break
                elif i[1] == 2 or i[2] == 2:
                    bestMove = i[0]
                    ##########################################################
                    print("Best Move with 2: ", bestMove)
                    ##########################################################
                    break
            if bestMove == None:
                for i in neigborCount:
                    if (i[1] != 1 and i[2] != 1):
                        bestMove = i[0]
            return bestMove

        games = self.available_cells(state, player)
        validMoves = valid_move(games)
        neigborCount = countNeigbor(state, validMoves)

        #####################################
        print("\nPOS HORIZONTAL VERTICAL: \n")
        for i in neigborCount:
            print(i)
        #####################################

        bestMove = chooseBestMove(neigborCount)

        if bestMove == None:
            goodMove = get_neigbor(state, validMoves)
            if (len(goodMove) == 0):
                bestMove = random.choice(validMoves)
            else:
                bestMove = random.choice(goodMove)
            ##########################################################
            print("Best Move with random: ", bestMove)
            ##########################################################

        return bestMove

class GameOver(Exception):
    def __str__(self):
        print('Gameover')


class EnemyDown(Exception):
    def __str__(self):
        print('You WIN!!!')


class Score:
    def __init__(self, score):
        self.score = score

        with open('score.txt') as sorter:
            lines = [line.split('Scores: ') for line in sorter]
        file = open("score.txt", 'w')

        for line in sorted(lines, key=lambda x: int(x[1]), reverse=True)[:10]:
            file.write('Scores: '.join(line))
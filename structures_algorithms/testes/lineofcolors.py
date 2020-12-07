
from random import choice

class LineOfColors(object):

    COLORS_INFORM = {
        'Vermelho': {
            'Count': 0,
            'value': 2,
        },
        'Amarelo': {
            'Count': 0,
            'value': 3,
        },
        'Verde': {
            'Count': 0,
            'value': 4,
        },
        'Azul': {
            'Count': 0,
            'value': 5,
        }
    }

    NUM_POSITIONS = 10

    def play(self):
        points = 0
        c = 0
        previous_var = ""
        current_counting_color = ""
        lista = eval("['Azul', 'Verde', 'J', 'Vermelho', 'Amarelo', 'Verde', 'J', 'Verde', 'Verde', 'Verde']")
        for idx, choice_ in enumerate(lista):
            if choice_ == 'J':
                c += 1

                current_counting_color = choice_ if choice_ != 'J' else current_counting_color
                if c >= 3 and current_counting_color:
                    if not points:
                        points = self.COLORS_INFORM[current_counting_color]['value']
                    else:
                        self.COLORS_INFORM[current_counting_color]['Count'] += points + self.COLORS_INFORM[current_counting_color]['value']
            else:
                points = 0
                c = 0

            previous_var = choice_

        total = 0
        for k, v in self.COLORS_INFORM.items():
            total += v['Count']

        #import pdb; pdb.set_trace()

        return total


t = LineOfColors()

print(t.play())

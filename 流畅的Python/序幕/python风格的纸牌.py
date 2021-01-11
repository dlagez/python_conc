# @Time      :2021/1/9 20:44
# @Author    :RocZhang(dlage)
import collections
Card = collections.namedtuple("Card", ['rank', 'suit'])
class FrenchDeck:
    # 这里直接定义了52张牌
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')

    # split()分割函数，以空格为分割符
    suits = 'spades diamonds clubs hearts'.split()
    # suits
    # Out[11]: ['spades', 'diamonds', 'clubs', 'hearts']


    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')

deck = FrenchDeck()
len(deck)  # Out[12]: 52

for d in deck:
    print(d)
# Card(rank='2', suit='spades')
# Card(rank='3', suit='spades')
# Card(rank='4', suit='spades')
# Card(rank='5', suit='spades')
# Card(rank='6', suit='spades')

from random import choice
choice(deck)  # 随机抽一张牌
# Out[18]: Card(rank='9', suit='diamonds')

# 查看一摞牌最上面 3 张
deck[0: 3]
# 先抽出索引是 12 的那张牌，然后每隔 13 张牌拿 1 张：
deck[12::13]

# 用in运算符就会按顺序进行一次迭代
Card('Q', 'hearts') in deck  # True

# 排序
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
# suit_values Out[26]: {'spades': 3, 'hearts': 2, 'diamonds': 1, 'clubs': 0}
# len(suit_values) 4
def spades_high(card):
    # FrenchDeck.ranks
    # Out[24]: ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    # 这里是返回每张牌的索引值
    rank_value = FrenchDeck.ranks.index(card.rank)
    # print("rank_value", rank_value)
    # 本身的值 * 4 + （spades=3, hearts=2, diamonds=1, clubs=0）其中之一
    # print(len(suit_values)) 恒为4
    return rank_value * len(suit_values) + suit_values[card.suit]

# 这里是先循环完，计算出排序的值再输出排序后的结果
for card in sorted(deck, key=spades_high):
    print(card)

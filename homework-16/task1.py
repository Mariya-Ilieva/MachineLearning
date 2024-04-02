# def generate_deck():
#     suits = ['H', 'S', 'C', 'D']
#     ranks = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#
#     deck = []
#
#     for suit in suits:
#         for rank in ranks:
#             card_code = suit + rank
#
#             if rank == 'A':
#                 card_value = 1
#             elif rank in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
#                 card_value = int(rank)
#             else:
#                 card_value = 10
#
#             card_tuple = (card_code, card_value)
#             deck.append(card_tuple)
#
#     return deck

def generate_deck():
    suits = ['H', 'S', 'C', 'D']
    ranks = {'A': 1, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

    deck = []

    for suit in suits:
        for rank, value in ranks.items():
            deck.append((suit + rank, value))

    return deck

cards = generate_deck()
for card in cards:
    print(card)

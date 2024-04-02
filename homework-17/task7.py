suits = 'HSCD'
ranks = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

deck = [(suit + rank, 1 if rank in ['A', '1'] else int(rank) if rank.isdigit() else 10) for suit in suits for rank in ranks]

for card in deck:
    print(card)

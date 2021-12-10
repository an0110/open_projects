x = [
	{'fn': 1, 'fp': 11, 'tp': 10},
	{'fn': 2, 'fp': 22, 'tp': 20},
	{'fn': 3, 'fp': 33, 'tp': 30},
	{'fn': 4, 'fp': 44, 'tp': 40}
 ]

y = [
	{'fn': 0, 'fp': 1, 'tp': 0},
	{'fn': 0, 'fp': 1, 'tp': 0},
	{'fn': 0, 'fp': 1, 'tp': 0},
	{'fn': 0, 'fp': 1, 'tp': 0}
]

from pprint import pprint
pprint (x)
x[0]["fp"] = 741
pprint (x[0]["fp"])



pprint (x)
c = int(input('capital do produto~> '))

i = float(input('taxa de juros~> ')) / 100

t = int(input('tempo, quantidade de meses que sera pago~> '))

# juros
j = c * i * t

# montante
m = c + j

print('juros~> {0}', j)

print('total montante~> {0}', m)

# descobrir o tempo, fazer depois
# M = C . (1 + i . t) → 480 = 400 . (1 + 0,04 . t) → 480 = 400 + 16 . t → 480 - 400 = 16 .t
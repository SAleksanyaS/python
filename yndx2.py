n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Создаем словарь для подсчета количества каждой карты в a и b
count_a = {}
count_b = {}

for card in a:
    count_a[card] = count_a.get(card, 0) + 1

for card in b:
    count_b[card] = count_b.get(card, 0) + 1

stack = []

for card in a:
    stack.append(card)

    # Пока стек не пуст и верхняя карта в стеке совпадает с текущей картой из b
    while stack and count_b.get(stack[-1, 0]) > 0:
        count_b[stack[-1]] -= 1
        stack.pop()

# Если стек пуст, значит, Джо смог получить выигрышную последовательность
if not stack:
    print("YES")
else:
    print("NO")

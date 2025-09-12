macas = int(input('quantas maçãs foram vendidas?'))
bananas = int(input('quantas bananas foram vendidas?'))

if bananas > macas:
    print('Foram vendidas mais bananas')
elif macas > bananas:
    print('Foram vendidas mais maçãs')
else:
    print('As duas venderam igual')
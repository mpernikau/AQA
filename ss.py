N_max = int(input("Определите размер очереди:"))

queue = [0 for _ in range(N_max)]  # инициализируем список с нулевыми элементами
order = 0  # будем хранить сквозной номер задачи
head = 0  # указатель на начало очереди
tail = 0  # указатель на элемент следующий за концом очереди

while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", size())
    elif cmd == "add":
        if size() != N_max:
            add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if is_empty():
            print("Очередь пустая")
        else:
            show()
    elif cmd == "do":
        if is_empty():
            print("Очередь пустая")
        else:
            do()
    elif cmd == "exit":
        for _ in range(size()):
            do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")


def add():  # добавляем задачу в очередь
    global tail, order
    order += 1  # увеличиваем порядковый номер задачи
    queue[tail] = order  # добавляем его в очередь
    print("Задача №%d добавлена" % (queue[tail]))

    # увеличиваем указатель на 1 по модулю максимального числа элементов
    # для зацикливания очереди в списке
    tail = (tail + 1) % N_max

def show(): # выводим приоритетную задачу
    print("Задача №%d в приоритете" % (queue[head]))

def do(): # выполняем приоритетную задачу
    global head
    print("Задача №%d выполнена" % (queue[head]))
    queue[head] = 0 # после выполнения зануляем элемент по указателю
    head = (head + 1) % N_max # и циклично перемещаем указатель

with open("input.txt", encoding='utf-8') as in_file:
    reader = in_file.readlines()
    size = int(reader[0])
    reader = reader[1:]
    a = []
    for line in reader:
        line = list(map(float, line.split()))
        a.append(line)

begin_index = int(input("Введите начальную точку:")) - 1
end = int(input("Введите конечную точку:")) - 1


d = 0


def round1(num):
    return round(num, 2)


def init_vertices_and_distance():
    global d
    # Инициализация вершин и расстояний
    d = [10000] * size  # минимальное расстояние
    v = [1] * size  # посещенные вершины

    d[begin_index] = 0
    min_index = 0
    # Шаг алгоритма
    while min_index < 10000:
        min_index = 10000
        min = 10000
        for i in range(size):
            # Если вершину ещё не обошли и вес меньше min
            if v[i] == 1 and d[i] < min:
                min = d[i]
                min_index = i

        # Добавляем найденный минимальный вес к текущему весу вершины
        # и сравниваем с текущим минимальным весом вершины
        if min_index != 10000:
            for i in range(size):
                if a[min_index][i] > 0:
                    temp = min + a[min_index][i]
                    if temp < d[i]:
                        d[i] = temp
            v[min_index] = 0


init_vertices_and_distance()

# Вывод кратчайших расстояний до вершин
print("Кратчайшие расстояния до вершин:")
print(*list(map(round1, d)))


for i in range(size):
    a[i] = list(map(int, a[i]))

init_vertices_and_distance()
# Восстановление пути
ver = [0] * size  # список посещенных вершин
ver[0] = end + 1  # начальный элемент - конечная вершина
k = 1  # индекс предыдущей вершины
weight = d[end]  # вес конечной вершины
while end != begin_index:  # пока не дошли до начальной вершины
    for i in range(size):  # просматриваем все вершины
        if a[i][end] != 0:  # если связь есть
            temp = weight - a[i][end]  # определяем вес пути из предыдущей вершины
            if temp == d[i]:  # если вес совпал с рассчитанным
                # значит из этой вершины и был переход
                weight = temp  # сохраняем новый вес
                end = i  # сохраняем предыдущую вершину
                ver[k] = i + 1  # и записываем ее в список
                k += 1
print("Вывод кратчайшего пути:")
print(*ver[:k][::-1])

import matplotlib.pyplot as plt

from queue import Queue

def change(rect, m, n):
    c = rect[4 * m]
    rect[4 * m] = rect[4 * n]
    rect[4 * n] = c
    c = rect[4 * m + 1]
    rect[4 * m + 1] = rect[4 * n + 1]
    rect[4 * n + 1] = c
    c = rect[4 * m + 2]
    rect[4 * m + 2] = rect[4 * n + 2]
    rect[4 * n + 2] = c
    c = rect[4 * m + 3]
    rect[4 * m + 3] = rect[4 * n + 3]
    rect[4 * n + 3] = c

#ДЛЯ ПРАВИЛЬНОЙ РБАОТЫ -- ПОДПРАВИТЬ КОНСТАНТУ 1000
def compare(a1, b1, c1, d1, a2, b2, c2, d2):
    #print(a1, b1, c1, d1, a2, b2, c2, d2)

    r1 = 0
    r2 = 0
    if a1 < b1:
        if a2 < b2:
            if a1 < a2 and b1 > b2:
                r1 = 1    
    else:
        if a2 < b2:
            if a2 > a1 or b2 < b1:
                r1 = 1
        else:
            if a2 > a1 and b2 < b1:
                r1 = 1

    if c2 < d2:
        if c1 < d1:
            if c2 < c1 and d2 > d1:
                r2 = 1    
    else:
        if c1 < d1:
            if c1 > c2 or d1 < d2:
                r2 = 1
        else:
            if c1 > c2 and d1 < d2:
                r2 = 1

    return r1 * r2

def sort_rect(rect, size, sign):
    for i in range(size):
        for j in range(size - 1):
            if compare(rect[4 * j + 0], rect[4 * j + 1], rect[4 * j + 2], rect[4 * j + 3],
            rect[4 * (j + 1) + 0], rect[4 * (j + 1) + 1], rect[4 * (j + 1) + 2], rect[4 * (j + 1) + 3]) == 0:
            #    print(compare(rect[4 * i + 0], rect[4 * i + 1], rect[4 * i + 2], rect[4 * i + 3],
            #rect[4 * j + 0], rect[4 * j + 1], rect[4 * j + 2], rect[4 * j + 3]))
            #    print(i, j)
                change(rect, j, j + 1)
                t = sign[j]
                sign[j] = sign[j + 1]
                sign[j + 1] = t

def show_must_go_on(rect, sign, size):
    for i in range(size - 1, -1, -1):
        if (sign[i] == - 1): plt.fill([rect[4 * i], rect[4 * i], rect[4 * i + 1], rect[4 * i + 1]], [rect[4 * i + 2], rect[4 * i + 3], rect[4 * i + 3], rect[4 * i + 2]], color = [1., 0., 1.])
        if (sign[i] == + 1): plt.fill([rect[4 * i], rect[4 * i], rect[4 * i + 1], rect[4 * i + 1]], [rect[4 * i + 2], rect[4 * i + 3], rect[4 * i + 3], rect[4 * i + 2]], color = [0., 0., 1.])

def mutant(rect, sign, size, delta):
    #new_rect = (4 * size) * [0]
    new_rect = []
    for i in range(size):
        if rect[4 * i] == 0:
            new_rect.append(0)
            new_rect.append(0)
            new_rect.append(0)
            new_rect.append(0)

            continue
        if sign[i] == +1:
            new_rect.append(rect[ 4 * i + 0] + delta)
            new_rect.append(rect[ 4 * i + 1] - delta)
            new_rect.append(rect[ 4 * i + 2] - delta)
            new_rect.append(rect[ 4 * i + 3] + delta)
        else:
            new_rect.append(rect[ 4 * i + 0] - delta)
            new_rect.append(rect[ 4 * i + 1] + delta)
            new_rect.append(rect[ 4 * i + 2] + delta)
            new_rect.append(rect[ 4 * i + 3] - delta)
    #print(new_rect)
    return new_rect

def merge(rect, mut, size):
    for i in range(4 * size):
        rect.append(mut[i])

def free_vert(a, n):
    vert = []
    for i in range(n):
        vert.append([a[4 * i + 0], a[4 * i + 2]])
        vert.append([a[4 * i + 0], a[4 * i + 3]])
        vert.append([a[4 * i + 1], a[4 * i + 2]])
        vert.append([a[4 * i + 1], a[4 * i + 3]])
    vert.sort()
    m = len(vert)
    for i in range(m - 1):
        if vert[i][0] == vert[i + 1][0] and vert[i][1] == vert[i + 1][1]:
            vert[i][0] = 0
            vert[i][1] = 0
            vert[i + 1][0] = 0
            vert[i + 1][1] = 0
    #vert.remove([0, 0])
    return vert
    #print(vert)

def not_free(a, n):
    vert = []
    for i in range(n):
        vert.append([a[4 * i + 0], a[4 * i + 2]])
        vert.append([a[4 * i + 0], a[4 * i + 3]])
        vert.append([a[4 * i + 1], a[4 * i + 2]])
        vert.append([a[4 * i + 1], a[4 * i + 3]])
    vert.sort()
    m = len(vert)
    if (vert[0][0] == vert[1][0] and vert[0][1] == vert[1][1]):
        pass
    else:
        vert[0][0] = 0
        vert[0][1] = 0
    if (vert[m - 1][0] == vert[m - 2][0] and vert[m - 1][1] == vert[m - 2][1]):
        pass
    else:
        vert[m - 1][0] = 0
        vert[m - 1][1] = 0
    for i in range(1, m - 1):
        if (vert[i][0] != vert[i + 1][0] or vert[i][1] != vert[i + 1][1]) and (vert[i][0] != vert[i - 1][0] or vert[i][1] != vert[i - 1][1]):
            vert[i][0] = 0
            vert[i][1] = 0
    return vert

    #ОСТАНОВИЛСЯ ТУТОЧКИ. ЦЕЛЬ --- СДЕЛАТЬ МАССИВ НЕСВОБОДНЫХ ВЕРШИН

def vertices(a, n):
    vert = []
    for i in range(n):
        if a[4 * i + 0] == 0 or a[4 * i + 1] == 0 or a[4 * i + 2] == 0 or a[4 * i + 3] == 0:
            continue
        vert.append([a[4 * i + 0], a[4 * i + 2]])
        vert.append([a[4 * i + 0], a[4 * i + 3]])
        vert.append([a[4 * i + 1], a[4 * i + 2]])
        vert.append([a[4 * i + 1], a[4 * i + 3]])
    vert.sort()
    return vert

def only_vertices(a, n):
    vert = []
    for i in range(n):
        if a[4 * i + 0] == 0 or a[4 * i + 1] == 0 or a[4 * i + 2] == 0 or a[4 * i + 3] == 0:
            continue
        if not ([a[4 * i + 0], a[4 * i + 2]] in vert):
            vert.append([a[4 * i + 0], a[4 * i + 2]])
        if not([a[4 * i + 0], a[4 * i + 3]] in vert):
            vert.append([a[4 * i + 0], a[4 * i + 3]])
        if not ([a[4 * i + 1], a[4 * i + 2]] in vert):
            vert.append([a[4 * i + 1], a[4 * i + 2]])
        if not([a[4 * i + 1], a[4 * i + 3]] in vert):
            vert.append([a[4 * i + 1], a[4 * i + 3]])
    vert.sort()
    return vert

def new_edges(a, sign, n, delta, down_e, up_e, left_e, right_e):
    vert = free_vert(a, n)
    ld = 0
    lu = 0
    rd = 0
    ru = 0
    #print(vert)
    delta_2 = delta * 0.5
    delta_plus = delta_2
    delta_minus = -delta_2

    for i in range(n):
        if a[4 * i] == 0:
            continue
        ld = 0
        lu = 0
        rd = 0
        ru = 0
        if [a[4 * i], a[4 * i + 2]] in vert:
            ld = 1
        if [a[4 * i], a[4 * i + 3]] in vert:
            lu = 1        
        if [a[4 * i + 1], a[4 * i + 2]] in vert:
            rd = 1        
        if [a[4 * i + 1], a[4 * i + 3]] in vert:
            ru = 1
        # print(a[4 * i], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3])
        # print(ld, lu, rd, ru)
        if lu:
            #y
            down_e.append(a[4 * i + 3] + delta)
            #x1
            down_e.append(a[4 * i] - delta)
            #x2
            down_e.append(a[4 * i] + delta)
        if ru:
            #y
            down_e.append(a[4 * i + 3] + delta)
            #x1
            down_e.append(a[4 * i + 1] - delta)
            #x2
            down_e.append(a[4 * i + 1] + delta)
        if ld:
            #y
            up_e.append(a[4 * i + 2] - delta)
            #x1
            up_e.append(a[4 * i] - delta)
            #x2
            up_e.append(a[4 * i] + delta)
        if rd:
            #y
            up_e.append(a[4 * i + 2] - delta)
            #x1
            up_e.append(a[4 * i + 1] - delta)
            #x2
            up_e.append(a[4 * i + 1] + delta)
        if ld:
            #x
            right_e.append(a[4 * i] - delta)
            #y1
            right_e.append(a[4 * i + 2] - delta)
            #y2
            right_e.append(a[4 * i + 2] + delta)
        if lu:
            #x
            right_e.append(a[4 * i] - delta)
            #y1
            right_e.append(a[4 * i + 3] - delta)
            #y2
            right_e.append(a[4 * i + 3] + delta)

        if rd:
            #x
            left_e.append(a[4 * i + 1] + delta)
            #y1
            left_e.append(a[4 * i + 2] - delta)
            #y2
            left_e.append(a[4 * i + 2] + delta)
        if ru:
            #x
            left_e.append(a[4 * i + 1] + delta)
            #y1
            left_e.append(a[4 * i + 3] - delta)
            #y2
            left_e.append(a[4 * i + 3] + delta)
        if sign[i] == +1:
            delta_s = delta_plus
        else:
            delta_s = delta_minus
        
        delta_plus_plus = delta_2 + delta_s
        delta_plus_minus = delta_2 - delta_s
        delta_minus_plus = -delta_2 + delta_s
        delta_minus_minus =  -delta_2 - delta_s

        if lu:    
            #y
            up_e.append(a[4 * i + 3] + delta_minus_minus)
            #x1
            up_e.append(a[4 * i] + delta_minus_minus)
            #x2
            up_e.append(a[4 * i]  + delta_plus_minus)
        if ru:
            #y
            up_e.append(a[4 * i + 3] + delta_minus_minus)
            #x1
            up_e.append(a[4 * i + 1] + delta_minus_plus)
            #x2
            up_e.append(a[4 * i + 1]  + delta_plus_plus)
        if ld:
            #y
            down_e.append(a[4 * i + 2]  + delta_plus_plus)
            #x1
            down_e.append(a[4 * i] + delta_minus_minus)
            #x2
            down_e.append(a[4 * i]  + delta_plus_minus)
        if rd:
            #y
            down_e.append(a[4 * i + 2]  + delta_plus_plus)
            #x1
            down_e.append(a[4 * i + 1]  + delta_minus_plus)
            #x2
            down_e.append(a[4 * i + 1]  + delta_plus_plus)

        if ld:
            #x
            left_e.append(a[4 * i]  + delta_plus_minus)
            #y1
            left_e.append(a[4 * i + 2] + delta_minus_plus)
            #y2
            left_e.append(a[4 * i + 2]  + delta_plus_plus)
        if lu:
            #x
            left_e.append(a[4 * i]  + delta_plus_minus)
            #y1
            left_e.append(a[4 * i + 3] + delta_minus_minus)
            #y2
            left_e.append(a[4 * i + 3]  + delta_plus_minus)

        if rd:
            #x
            right_e.append(a[4 * i + 1] + delta_minus_plus)
            #y1
            right_e.append(a[4 * i + 2]  + delta_minus_plus)
            #y2
            right_e.append(a[4 * i + 2]  + delta_plus_plus)
        if ru:
            #x
            right_e.append(a[4 * i + 1] + delta_minus_plus)
            #y1
            right_e.append(a[4 * i + 3] + delta_minus_minus)
            #y2
            right_e.append(a[4 * i + 3]  + delta_plus_minus)

def cook_rectangles(new_rect, size, down_e, up_e, left_e, right_e, sign):
    #print(size, len(down_e), len(up_e), len(left_e), len(right_e))
    for i in range(size):
        for j in range(size):
            if (down_e[3 * i + 1] == up_e[3 * j + 1] and down_e[3 * i + 2] == up_e[3 * j + 2]):
                new_rect.append(down_e[3 * i + 1])
                new_rect.append(down_e[3 * i + 2])
                new_rect.append(down_e[3 * i])
                new_rect.append(up_e[3 * j])
                sign.append(-1)
                break
    for i in range(size):
        for j in range(size):
            if (left_e[3 * i + 1] == right_e[3 * j + 1] and left_e[3 * i + 2] == right_e[3 * j + 2]):
                new_rect.append(left_e[3 * i])
                new_rect.append(right_e[3 * j])
                new_rect.append(left_e[3 * i + 1])
                new_rect.append(left_e[3 * i + 2])
                sign.append(+1)
                break  

def comparator(mut, i, j):
    #j выше но уже
    if compare(mut[4 * i], mut[4 * i + 1], mut[4 * i + 2], mut[4 * i + 3], mut[4 * j], mut[4 * j + 1], mut[4 * j + 2], mut[4 * j + 3]):
        return 1
    else:
        return 0

def check_vert_rect(x1, x2, y1, y2, vert):
    if x1 < x2 and  y1 < y2:
        for i in range(len(vert)):
            if vert[i] == [0, 0]:
                continue
            if (vert[i][0] > x1 and vert[i][0] < x2 and vert[i][1] > y1 and vert[i][1] < y2):
                #print(x1,x2, y1, y2, vert[i][0], vert[i][1])
                return 0
        return 1
    if x1 > x2 and  y1 < y2:
        for i in range(len(vert)):
            if vert[i] == [0, 0]:
                continue
            if (vert[i][0] > x1 or vert[i][0] < x2) and vert[i][1] > y1 and vert[i][1] < y2:
                #print(x1,x2, y1, y2, vert[i][0], vert[i][1])
                return 0
        return 1
    if x1 < x2 and  y1 > y2:
        for i in range(len(vert)):
            if vert[i] == [0, 0]:
                continue
            if (vert[i][0] > x1 and vert[i][0] < x2 and (vert[i][1] > y1 or vert[i][1] < y2)):
                #print(x1,x2, y1, y2, vert[i][0], vert[i][1])
                return 0
        return 1
    if x1 > x2 and  y1 > y2:
        for i in range(len(vert)):
            if vert[i] == [0, 0]:
                continue
            if (vert[i][0] > x1 or vert[i][0] < x2) and (vert[i][1] > y1 or vert[i][1] < y2):
                #print(x1,x2, y1, y2, vert[i][0], vert[i][1])
                return 0
        return 1    

def flype(a, n, sign):
    #ГИГАНТСКОЕ ТОРМОЖЕНИЕ ТУТ!!!
    vert = vertices(a, n)
    f_vert = free_vert(a, n)
    not_free_vert = not_free(a, n)
    #draw_rect(a)
    for i in range(n):
        if a[4 * i] == 0:
            continue
        for j in range(n):
            if a[4 * j] == 0:
                continue
            if sign[i]  == + 1 and sign[j] == -1 and comparator(a, i, j):
                #print(1)
                #print('candidates:', a[4 * i], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3], a[4 * j], a[4 * j + 1], a[4 * j + 2], a[4 * j + 3])
                #j выше но уже
                #нужно найти еще вершинок
                #ТУТ ПРОВЕРКА НА ТО, ЧТО ЭТО РЕАЛЬНО ФЛАЙП. ОСТАЛОСЬ НАЙТИ ВЕРШИНЫ С НЕКОТОРЫМИ УСЛОВИЯМ.
                #check_vert_rect -- не написана
                #порядок прямоугольников может быть обратный, хз

                #вершины флайпа слева снизу
                if [a[4 * i], a[4 * j + 2]] in not_free_vert and [a[4 * i], a[4 * i + 2]] in not_free_vert and [a[4 * j], a[4 * j + 2]] in not_free_vert and check_vert_rect(a[4 * i], a[4 * j], a[4 * j + 2], a[4 * i + 2], vert):
                    print('case LD', a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3], a[4 * j + 0], a[4 * j + 1], a[4 * j + 2], a[4 * j + 3], sign[i], sign[j])
                    r1 = -1
                    r2 = -1
                    for l in range(n):
                        if a[4 * l] == 0:
                            continue
                        if a[4 * l + 1] == a[4 * i] and a[4 * l + 2] == a[4 * j + 2] and a[4 * l + 3] == a[4 * i + 2]:
                            r1 = l
                        if a[4 * l + 3] == a[4 * j + 2] and a[4 * l] == a[4 * i] and a[4 * l + 1] == a[4 * j]:
                            r2 = l
                    if r1 == -1 or r2 == -1:
                        pass
                    else:
                        a[4 * r2 + 3] = a[4 * i + 3]
                        a[4 * r1 + 1] = a[4 * j + 1]
                        a[4 * i] = a[4 * j + 1]
                        a[4 * j + 2] = a[4 * i + 3]
                        return 0
                #вершины флайпа слева сверху
                elif   [a[4 * i], a[4 * j + 3]] in not_free_vert and [a[4 * i], a[4 * i + 3]] in not_free_vert and [a[4 * j], a[4 * j + 3]] in not_free_vert and check_vert_rect(a[4 * i], a[4 * j], a[4 * i + 3], a[4 * j + 3], vert):
                    print('case LU', a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3], a[4 * j + 0], a[4 * j + 1], a[4 * j + 2], a[4 * j + 3], sign[i], sign[j])
                    r1 = -1
                    r2 = -1
                    for l in range(n):
                        if a[4 * l] == 0:
                            continue
                        # if l == i or l == j:
                        #     continue
                        if a[4 * l + 1] == a[4 * i] and a[4 * l + 2] == a[4 * i + 3] and a[4 * l + 3] == a[4 * j + 3]:
                            r1 = l
                        if a[4 * l + 2] == a[4 * j + 3] and a[4 * l] == a[4 * i] and a[4 * l + 1] == a[4 * j]:
                            r2 = l
                    if r1 == -1 or r2 == -1:
                        pass
                    else:
                        print('r1 = ', a[4 * r1 + 0], a[4 * r1 + 1], a[4 * r1 + 2], a[4 * r1 + 3], sign[r1])
                        print('r2 = ', a[4 * r2 + 0], a[4 * r2 + 1], a[4 * r2 + 2], a[4 * r2 + 3], sign[r2])
                        a[4 * r2 + 2] = a[4 * i + 2]
                        a[4 * r1 + 1] = a[4 * j + 1]
                        a[4 * i] = a[4 * j + 1]
                        a[4 * j + 3] = a[4 * i + 2]
                        return 0

                #вершины флайпа справа снизу
                elif  [a[4 * i + 1], a[4 * j + 2]] in not_free_vert and [a[4 * i + 1], a[4 * i + 2]] in not_free_vert and [a[4 * j  + 1], a[4 * j + 2]] in not_free_vert and check_vert_rect(a[4 * j + 1], a[4 * i + 1], a[4 * j + 2], a[4 * i + 2], vert):
                    print('case RD', a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3], a[4 * j + 0], a[4 * j + 1], a[4 * j + 2], a[4 * j + 3], sign[i], sign[j])                        
                    r1 = -1
                    r2 = -1
                    for l in range(n):
                        if a[4 * l] == 0:
                            continue
                        # if l == i or l == j:
                        #     continue
                        if a[4 * l] == a[4 * i + 1] and a[4 * l + 2] == a[4 * j + 2] and a[4 * l + 3] == a[4 * i + 2]:
                            r1 = l
                        if a[4 * l + 3] == a[4 * j + 2] and a[4 * l] == a[4 * j + 1] and a[4 * l + 1] == a[4 * i + 1]:
                            r2 = l
                    if r1 == -1 or r2 == -1:
                        pass
                    else:
                        print('r1 = ', a[4 * r1 + 0], a[4 * r1 + 1], a[4 * r1 + 2], a[4 * r1 + 3], sign[r1])
                        print('r2 = ', a[4 * r2 + 0], a[4 * r2 + 1], a[4 * r2 + 2], a[4 * r2 + 3], sign[r2])
                        a[4 * r2 + 3] = a[4 * i + 3]
                        a[4 * r1] = a[4 * j]
                        a[4 * i + 1] = a[4 * j]
                        a[4 * j + 2] = a[4 * i + 3]
                        return 0
                    
                #вершины флайпа справа сверху НЕ ПЕРЕДЕЛАНО
                if [a[4 * i + 1], a[4 * j + 3]] in not_free_vert and [a[4 * i + 1], a[4 * i + 3]] in not_free_vert and [a[4 * j + 1], a[4 * j + 3]] in not_free_vert and check_vert_rect(a[4 * j + 1], a[4 * i + 1], a[4 * i + 3], a[4 * j + 3], vert):
                    print('case RU', a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3], a[4 * j + 0], a[4 * j + 1], a[4 * j + 2], a[4 * j + 3], sign[i], sign[j])
                    r1 = -1
                    r2 = -1
                    for l in range(n):
                        if a[4 * l] == 0:
                            continue
                        # if l == i or l == j:
                        #     continue
                        if a[4 * l] == a[4 * i + 1] and a[4 * l + 2] == a[4 * i + 3] and a[4 * l + 3] == a[4 * j + 3]:
                            r1 = l
                        if a[4 * l + 2] == a[4 * j + 3] and a[4 * l] == a[4 * j + 1] and a[4 * l + 1] == a[4 * i + 1]:
                            r2 = l
                    if r1 == -1 or r2 == -1:
                        pass
                    else:
                        a[4 * r2 + 2] = a[4 * i + 2]
                        a[4 * r1] = a[4 * j]
                        a[4 * i + 1] = a[4 * j]
                        a[4 * j + 3] = a[4 * i + 2]
                        return 0
    return 1

def collapse(a, n, sign):
    vert = vertices(a, n)
    #draw_rect(a)
    for i in range(n):
        if a[4 * i] == 0 or a[4 * i + 1] == 0 or a[4 * i + 2] == 0 or a[4 * i + 3] == 0:
            continue
        r1 = -1
        r2 = -1
        for j in range(n):
            if a[4 * i] == a[4 * j + 1] and a[4 * i + 2] == a[4 * j + 3] and a[4 * i + 3] == a[4 * j + 2]:
                r1 = j
                #left
            if a[4 * i + 1] == a[4 * j] and a[4 * i + 2] == a[4 * j + 3] and a[4 * i + 3] == a[4 * j + 2]:
                r2 = j
        if sign[i] == + 1 and r1 != -1 and r2 != -1 and check_vert_rect(a[4 * r1 + 1], a[4 * r2], a[4 * r1 + 2], a[4 * r1 + 3], vert):
            print('here s candeidates, but ---1', a[4 * r1 + 0], a[4 * r1 + 1], a[4 * r1 + 2], a[4 * r1 + 3])
            print(a[4 * r2 + 0], a[4 * r2 + 1], a[4 * r2 + 2], a[4 * r2 + 3])
            print(a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3])
            a[4 * r1 + 1] = a[4 * r2 + 1]
            a[4 * i] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            a[4 * r2] = 0
            a[4 * r2 + 1] = 0
            a[4 * r2 + 2] = 0
            a[4 * r2 + 3] = 0
            return 0
        r1 = -1
        r2 = -1
        for j in range(n):
            if a[4 * i + 3] == a[4 * j + 2] and a[4 * i] == a[4 * j + 1] and a[4 * i + 1] == a[4 * j]:
                r1 = j
                #up
            if a[4 * i + 2] == a[4 * j + 3] and a[4 * i] == a[4 * j + 1] and a[4 * i + 1] == a[4 * j]:
                r2 = j
        if a[4 * i] == 1.9 and a[4 * i + 1] == 1.1:
            print('i = ', a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3])
            print('ALARM r2 = ', a[4 * r2 + 0], a[4 * r2 + 1], a[4 * r2 + 2], a[4 * r2 + 3])
            print('r1 = ', a[4 * r1 + 0], a[4 * r1 + 1], a[4 * r1 + 2], a[4 * r1 + 3])
            print('sign р1 р2 ', sign[i], r1, r2)
        if sign[i] == -1 and r1  != -1 and r2 != -1 and check_vert_rect(a[4 * r2], a[4 * r2 + 1], a[4 * r2 + 3], a[4 * r1 + 2], vert):
            print('here s candeidates, but ---1', a[4 * r1 + 0], a[4 * r1 + 1], a[4 * r1 + 2], a[4 * r1 + 3])
            print(a[4 * r2 + 0], a[4 * r2 + 1], a[4 * r2 + 2], a[4 * r2 + 3])
            print(a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3])
            a[4 * r1 + 2] = a[4 * r2 + 2]
            a[4 * i] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            a[4 * r2] = 0
            a[4 * r2 + 1] = 0
            a[4 * r2 + 2] = 0
            a[4 * r2 + 3] = 0
            return 0
    return 1     

def collapse_many(a, n, sign):
    vert = vertices(a, n)
    for i in range(n):
        if a[4 * i] == 0:
            continue
        if sign[i] == +1 and check_vert_rect(a[4 * i], a[4 * i + 1], a[4 * i + 3], a[4 * i + 2], vert):
            train = []
            train_r1 = []
            train_r2 = []
            start = i
            current = i
            flag = 1
            #ищем продолжение поезда
            while flag and True:
                r1 = -1
                r2 = -1
                #ищем р1 р2
                for j in range(n):
                    if a[4 * current] == a[4 * j + 1] and a[4 * current + 2] == a[4 * j + 3]:
                        r1 = j
                        #left
                    if a[4 * current + 1] == a[4 * j] and a[4 * current + 2] == a[4 * j + 3]:
                        r2 = j
                        #right
                #r1 r2 идут вниз от i-ого
                if r1 != -1 and r2 != -1 and a[4 * r1 + 2] == a[4 * r2 + 2]:
                    train_r1.append(r1)
                    train_r2.append(r2)
                    train.append(current)
                    current = -1
                    for l in range(n):
                        if a[4 * l] == a[4 * r1 + 1] and a[4 * l + 3] == a[4 * r1 + 2] and a[4 * l + 1] == a[4 * r2]:
                            current = l
                            break
                    if  current == -1:
                        flag = 0
                        break
                else:
                    flag = 0
                    break
                if current == start:
                    #COLLAPSE
                    print('Collapse')
                    for i in range(len(train_r1)):
                        a[4 * train_r1[i] + 1] = a[4 * train_r2[i] + 1]
                        a[4 * train_r2[i]] = 0
                        a[4 * train_r2[i] + 1] = 0
                        a[4 * train_r2[i] + 2] = 0
                        a[4 * train_r2[i] + 3] = 0
                        a[4 * train[i]] = 0
                        a[4 * train[i] + 1] = 0
                        a[4 * train[i] + 2] = 0
                        a[4 * train[i] + 3] = 0
                    return 0
        if sign[i] == -1 and check_vert_rect(a[4 * i + 1], a[4 * i], a[4 * i + 2], a[4 * i + 3], vert):
            train = []
            train_r1 = []
            train_r2 = []
            start = i
            current = i
            flag = 1
            #ищем продолжение поезда
            while flag and True:
                r1 = -1
                r2 = -1
                #ищем р1 р2
                for j in range(n):
                    if a[4 * current] == a[4 * j + 1] and a[4 * current + 3] == a[4 * j + 2]:
                        r1 = j
                        #up
                    if a[4 * current] == a[4 * j + 1] and a[4 * current + 2] == a[4 * j + 3]:
                        r2 = j
                        #down
                #r1 r2 идут влево от i-ого
                if r1 != -1 and r2 != -1 and a[4 * r1] == a[4 * r2]:
                    train_r1.append(r1)
                    train_r2.append(r2)
                    train.append(current)
                    current = -1
                    for l in range(n):
                        if a[4 * l + 1] == a[4 * r1] and a[4 * l + 3] == a[4 * r1 + 2] and a[4 * l + 2] == a[4 * r2 + 3]:
                            current = l
                            break
                    if  current == -1:
                        flag = 0
                        break
                else:
                    flag = 0
                    break
                if current == start:
                    #COLLAPSE
                    print('Collapse')
                    for i in range(len(train_r1)):
                        a[4 * train_r1[i] + 2] = a[4 * train_r2[i] + 2]
                        a[4 * train_r2[i]] = 0
                        a[4 * train_r2[i] + 1] = 0
                        a[4 * train_r2[i] + 2] = 0
                        a[4 * train_r2[i] + 3] = 0
                        a[4 * train[i]] = 0
                        a[4 * train[i] + 1] = 0
                        a[4 * train[i] + 2] = 0
                        a[4 * train[i] + 3] = 0
                    return 0
    return 1

def simplify(a, n):
    vert = free_vert(a, n)
    hor = []
    ver = []
    for i in vert:
        hor.append(i[0])
        ver.append(i[1])
    hor = list(set(hor))
    ver = list(set(ver))
    for i in range(n):
        if a[4 * i] == 0:
            continue
        if [a[4 * i], a[4 * i + 2]] in vert and [a[4 * i], a[4 * i + 3]] in vert and [a[4 * i + 1], a[4 * i + 2]] in vert:
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            print('destabilization - 1')
            return 0
        if [a[4 * i], a[4 * i + 2]] in vert and [a[4 * i], a[4 * i + 3]] in vert and [a[4 * i + 1], a[4 * i + 3]] in vert:
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            print('destabilization - 2')
            return 0
        if [a[4 * i + 1], a[4 * i + 2]] in vert and [a[4 * i + 1], a[4 * i + 3]] in vert and [a[4 * i], a[4 * i + 2]] in vert:
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            print('destabilization - 3')
            return 0
        if [a[4 * i + 1], a[4 * i + 2]] in vert and [a[4 * i + 1], a[4 * i + 3]] in vert and [a[4 * i], a[4 * i + 3]] in vert:
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            print('destabilization - 4')
            return 0
        if not(a[4 * i] in hor) and [a[4 * i + 1], a[4 * i + 2]] in vert and [a[4 * i + 1], a[4 * i + 3]] in vert:
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            return 0
        if not(a[4 * i + 1] in hor) and [a[4 * i], a[4 * i + 2]] in vert and [a[4 * i], a[4 * i + 3]] in vert:
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            return 0
        if not(a[4 * i + 2] in ver) and [a[4 * i], a[4 * i + 3]] in vert and [a[4 * i + 1], a[4 * i + 3]] in vert:
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            return 0
        if not(a[4 * i + 3] in ver) and [a[4 * i], a[4 * i + 2]] in vert and [a[4 * i + 1], a[4 * i + 2]] in vert:
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            return 0
    return 1
   
def delete(a, n):
    for i in range(n):
        if(a[4 * i] == a[4 * i + 1] or a[4 * i + 2] == a[4 * i + 3]):
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0

def rotate(a, n, sign):
    n = len(a) // 4
    while(True):
        print('Genus = ', genus(a, n))
        delete(a, n)
        # if check_orient(a, n, sign) == 0:
        #     return
        if flype(a, n, sign):
            break
    
    print('flype phase ends')
    #СХЛОПЫВАНИЯ
    i = 0
    while(True):
        i = i + 1
        print('Genus = ', genus(a, n), 'i = ', i)
        #draw_rect(a)
        delete(a, n)
        if collapse_many(a, n, sign):
            break

def simplification(a, n):
    while True:
        #draw_rect(a)
        if simplify(a, n):
            break
        
    while True:
        #draw_rect(a)
        if collapse_many(a, n, sign):
            break
    check_orient(a, n, sign)
    print('simplifying ends')

def orientate(a, n, sign):
    for i in range(len(a)):
        a[i] = a[i] + 1
    sign[0] = 1
    while(True):
        for i in range(n):
            for j in range(n):
                if sign[i] == 0:
                    continue
                if (a[4 * i] == a[4 * j + 1] and a[4 * i + 3] == a[4 * j + 2]) or (a[4 * i] == a[4 * j + 1] and a[4 * i + 2] == a[4 * j + 3]) or (a[4 * i + 1] == a[4 * j] and a[4 * i + 3] == a[4 * j + 2]) or (a[4 * i + 1] == a[4 * j] and a[4 * i + 2] == a[4 * j + 3]):
                    sign[j] = - sign[i]
        flag = 0
        for i in range(n):
            if sign[i] == 0:
                flag = 1
        if flag == 0:
            return

    # print(sign)
       
def genus(a, n):
    sum_1 = 0
    #количество 2-клеток
    for i in range(n):
        if a[4 * i] != 0 and a[4 * i + 1] != 0 and a[4 * i + 2] != 0 and a[4 * i + 3] != 0:
            sum_1 = sum_1 + 1
    b =  vertices(a, n)
    #количество ребер
    for j in range(len(b) - 1):
        if b[j][0] != 0 and b[j][1] != 0and (b[j][0] != b[j + 1][0] or b[j][1] != b[j + 1][1]):
            sum_1 = sum_1 - 1
    sum_1 = sum_1 - 1
    #b = vertices(a, n)
    hor = []
    ver = []
    #вершины = количество уровней
    for i in range(len(b)):
        if b[i][0] != 0:
            hor.append(b[i][0])
        if b[i][1] != 0:
            ver.append(b[i][1])
    hor.sort()
    ver.sort()
    sum_1 = sum_1 + len(list(set(hor)))
    sum_1 = sum_1 + len(list(set(ver)))
    #1 --- потому что еще диск надо вклеить
    return (1 - sum_1) // 2

def draw_rect(a):
    plt.figure(figsize = (20, 10))
    y_min = 0
    x_min = 0
    x_max = 1
    y_max = 1
    e = 0.05
    for i in range(len(a) // 4):
        if a[4 * i] > x_max:
            x_max = a[4 * i]
        if a[4 * i + 1] > x_max:
            x_max = a[4 * i + 1]
        if a[4 * i + 2] > y_max:
            y_max = a[4 * i + 2]
        if a[4 * i + 3] > y_max:
            y_max = a[4 * i + 3]
    x_max = x_max + 2
    y_max = y_max + 2       
    for i in range(len(a) // 4):
        c = [0.2, 0.2, 0.45 + 0.3 * sign[i], 0.5]
        white = [0.8, 0.2, 1., 0.8]
        whiteindex = 0
        if a[4 * i + 2] > a[4 * i + 3] and a[4 * i] > a[4 * i + 1]:
            # правильная отрисовка
            if whiteindex:
                plt.fill([a[4 * i] - e, a[4 * i] - e, x_max, x_max], [a[4 * i + 2], y_max, y_max, a[4 * i + 2]], color =  white)
                plt.fill([a[4 * i + 1] + e, a[4 * i + 1] + e, x_min, x_min], [a[4 * i + 2], y_max, y_max, a[4 * i + 2]], color =  white)
                plt.fill([a[4 * i] - e, a[4 * i] - e, x_max, x_max], [a[4 * i + 3], y_min, y_min, a[4 * i + 3]], color =  white)
                plt.fill([a[4 * i + 1] + e, a[4 * i + 1] + e, x_min, x_min], [a[4 * i + 3], y_min, y_min, a[4 * i + 3]], color =  white)

            plt.fill([a[4 * i], a[4 * i], x_max, x_max], [a[4 * i + 2], y_max, y_max, a[4 * i + 2]], color =  c)
            plt.fill([a[4 * i + 1], a[4 * i + 1], x_min, x_min], [a[4 * i + 2], y_max, y_max, a[4 * i + 2]], color =  c)
            plt.fill([a[4 * i], a[4 * i], x_max, x_max], [a[4 * i + 3], y_min, y_min, a[4 * i + 3]], color = c)
            plt.fill([a[4 * i + 1], a[4 * i + 1], x_min, x_min], [a[4 * i + 3], y_min, y_min, a[4 * i + 3]], color = c)
            continue
        if a[4 * i + 2] < a[4 * i + 3] and a[4 * i] < a[4 * i + 1]:
            if whiteindex:
                plt.fill([a[4 * i] - e, a[4 * i] - e, a[4 * i + 1] + e, a[4 * i + 1] + e], [a[4 * i + 2], a[4 * i + 3], a[4 * i + 3], a[4 * i + 2]], color = white)
            
            plt.fill([a[4 * i], a[4 * i], a[4 * i + 1], a[4 * i + 1]], [a[4 * i + 2], a[4 * i + 3], a[4 * i + 3], a[4 * i + 2]], color = c)
        if a[4 * i + 2] > a[4 * i + 3]:
            if whiteindex:
                plt.fill([a[4 * i] - e, a[4 * i] - e, a[4 * i + 1] + e, a[4 * i + 1] + e], [a[4 * i + 2], y_max, y_max, a[4 * i + 2]], color =  white)
                plt.fill([a[4 * i] - e, a[4 * i] - e, a[4 * i + 1] + e, a[4 * i + 1] + e], [y_min, a[4 * i + 3], a[4 * i + 3], y_min], color =  white)

            plt.fill([a[4 * i], a[4 * i], a[4 * i + 1], a[4 * i + 1]], [a[4 * i + 2], y_max, y_max, a[4 * i + 2]], color =  c)
            plt.fill([a[4 * i], a[4 * i], a[4 * i + 1], a[4 * i + 1]], [y_min, a[4 * i + 3], a[4 * i + 3], y_min], color =  c)
        if a[4 * i] > a[4 *i + 1]:
            if whiteindex:
                plt.fill([x_min, x_min, a[4 * i + 1] + e, a[4 * i + 1] + e], [a[4 * i + 2], a[4 * i + 3], a[4 * i + 3], a[4 * i + 2]], color =  white)
                plt.fill([a[4 * i] - e, a[4 * i] - e, x_max, x_max], [a[4 * i + 2], a[4 * i + 3], a[4 * i + 3], a[4 * i + 2]], color =  white)

            plt.fill([x_min, x_min, a[4 * i + 1], a[4 * i + 1]], [a[4 * i + 2], a[4 * i + 3], a[4 * i + 3], a[4 * i + 2]], color =  c)
            plt.fill([a[4 * i], a[4 * i], x_max, x_max], [a[4 * i + 2], a[4 * i + 3], a[4 * i + 3], a[4 * i + 2]], color =  c)
    b = free_vert(a, len(a) // 4)
    for i in range(len(b)):
        if b[i][0] != 0:
            plt.scatter(b[i][0], b[i][1], marker = 'o')
    plt.show()
    return

def rescale(a, size):
    hor = []
    ver = []
    for i in range(size):
        if a[4 * i] in hor or a[4 * i + 0] == 0:
            pass
        else:
            hor.append(a[4 * i])
        if a[4 * i + 1] in hor or a[4 * i + 1] == 0:
            pass
        else:
            hor.append(a[4 * i + 1])
        if a[4 * i + 2] in ver or a[4 * i + 2] == 0:
            pass 
        else:
            ver.append(a[4 * i + 2])
        if a[4 * i + 3] in ver or a[4 * i + 3] == 0:
            pass
        else:
            ver.append(a[4 * i + 3])
    hor.sort()
    ver.sort()
    for i in range(size):
        if a[4 * i + 0] == 0 or a[4 * i + 1] == 0 or a[4 * i + 2] == 0 or a[4 * i + 3] == 0:
            continue
        a[4 * i + 0] = hor.index(a[4 * i + 0]) + 1
        a[4 * i + 1] = hor.index(a[4 * i + 1]) + 1
        a[4 * i + 2] = ver.index(a[4 * i + 2]) + 1
        a[4 * i + 3] = ver.index(a[4 * i + 3]) + 1

def check_orient(a, n, sign):
    for i in range(n):
        if a[4 * i] == 0 :
            continue
        for j in range(n):
            if  a[4 * j] == 0:
                continue
            if (a[4 * i] == a[4 * j + 1] and a[4 * i + 3] == a[4 * j + 2]) or (a[4 * i] == a[4 * j + 1] and a[4 * i + 2] == a[4 * j + 3]) or (a[4 * i + 1] == a[4 * j] and a[4 * i + 3] == a[4 * j + 2]) or (a[4 * i + 1] == a[4 * j] and a[4 * i + 2] == a[4 * j + 3]):
                if (sign[i] * sign[j]) == +1:
                    print(' wrong orientation!!')
                    return 0

def fill_adjecent(a, n):
    adj = [-1] * (4 * n)
    for i in range(n):
        if a[4 * i] == 0:
            continue
        for j in range(n):
            if a[4 * j] == 0:
                continue
            #лево - верх
            if (a[4 * i] == a[4 * j + 1] and a[4 * i + 3] == a[4 * j + 2]):
                adj[4 * i + 0] = j
            
            #право верх
            if (a[4 * i + 1] == a[4 * j] and a[4 * i + 3] == a[4 * j + 2]):
                adj[4 * i + 1] = j

            #право низ
            if (a[4 * i + 1] == a[4 * j] and a[4 * i + 2] == a[4 * j + 3]):
                adj[4 * i + 2] = j

            #лево низ
            if (a[4 * i] == a[4 * j + 1] and a[4 * i + 2] == a[4 * j + 3]):
                adj[4 * i + 3] = j
    return adj

def clever_rotation(a, n, sign):
    adj = fill_adjecent(a, n)
    counter = 0
    q = []
    for i in range(n):
        q.append(i)
    attempts = 0
    vert =  only_vertices(a, n)
    #draw_rect(a)
    #ПЕРЕДЕЛЫВАНИЕ ВЕРШИН БУДЕТ ТРУДНО ПРОВЕРИТЬ. ВИЖУ ТУТ ОПАСНОСТЬы
    while attempts < n:
        counter = counter + 1
        cur_1 = q[0]
        flag = 0
        for i in range(4):
            cur_2 = adj[4 * cur_1 + i]
            if flag or cur_2 == -1:
                continue
            for j in range(4):
                cur_3 = adj[4 * cur_2 + j]
                if flag or cur_3 == -1:
                    continue
                for k in range(4):
                    cur_4 = adj[4 * cur_3 + k]
                    if flag or cur_4 == -1:
                        continue
                    if sign[cur_1]  == + 1 and sign[cur_4] == -1 and comparator(a, cur_1, cur_4):
                        if [i, j, k] == [0, 1, 2] and check_vert_rect(a[4 * cur_1 + 0], a[4 * cur_4 + 0], a[4 * cur_1 + 3], a[4 * cur_4 + 3], vert):
                            print('1st case', a[4 * cur_1 + 0], a[4 * cur_1 + 1], a[4 * cur_1 + 2], a[4 * cur_1 + 3], a[4 * cur_4 + 0], a[4 * cur_4 + 1], a[4 * cur_4 + 2], a[4 * cur_4 + 3])

                            vert.remove([a[4 * cur_2 + 1], a[4 * cur_2 + 2]])
                            vert.remove([a[4 * cur_3 + 1], a[4 * cur_3 + 2]])
                            vert.remove([a[4 * cur_2 + 1], a[4 * cur_3 + 2]])
                            
                            vert.append([a[4 * cur_4 + 0], a[4 * cur_1 + 2]])
                            vert.append([a[4 * cur_4 + 1], a[4 * cur_1 + 2]])
                            vert.append([a[4 * cur_4 + 1], a[4 * cur_1 + 3]])
                            
                            a[4 * cur_1 + 0] = a[4 * cur_4 + 1]
                            a[4 * cur_2 + 1] = a[4 * cur_4 + 1]
                            a[4 * cur_3 + 2] = a[4 * cur_1 + 2]
                            a[4 * cur_4 + 3] = a[4 * cur_1 + 2]
                            if adj[4 * cur_1 + 3] == -1:
                                print('ANOTHER ALARM')
                            else:
                                adj[4 * adj[4 * cur_1 + 3] + 1] = cur_3
                            if adj[4 * cur_4 + 1] == -1:
                                print('ANOTHER ALARM')
                            else:
                                adj[4 * adj[4 * cur_4 + 1] + 3] = cur_2
                            adj[4 * cur_2 + 1] = adj[4 * cur_4 + 1]
                            adj[4 * cur_3 + 3] = adj[4 * cur_1 + 3]
                            adj[4 * cur_1 + 3] = cur_4
                            adj[4 * cur_4 + 1] = cur_1
                            #draw_rect(a)
                            flag = 1
                            # print('cur2, cur3 =', a[4 * cur_2 + 0], a[4 * cur_2 + 1], a[4 * cur_2 + 2], a[4 * cur_2 + 3], a[4 * cur_3 + 0], a[4 * cur_3 + 1], a[4 * cur_3 + 2], a[4 * cur_3 + 3])
                            # for i in range(n):
                            #     print("i = ", i, '[', a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3], ']', adj[4 * i + 0],adj[4 * i + 1],adj[4 * i + 2],adj[4 * i + 3])
                            # print(cur_1, cur_2, cur_3, cur_4)
                            # draw_rect(a)
                            
                            

                            continue
                        if [i, j, k] == [1, 0, 3] and check_vert_rect(a[4 * cur_4 + 1], a[4 * cur_1 + 1], a[4 * cur_1 + 3], a[4 * cur_4 + 3], vert):
                            vert.remove([a[4 * cur_2 + 0], a[4 * cur_2 + 2]])
                            vert.remove([a[4 * cur_3 + 0], a[4 * cur_3 + 2]])
                            vert.remove([a[4 * cur_2 + 0], a[4 * cur_3 + 2]])
                            
                            vert.append([a[4 * cur_4 + 1], a[4 * cur_1 + 2]])
                            vert.append([a[4 * cur_4 + 0], a[4 * cur_1 + 2]])
                            vert.append([a[4 * cur_4 + 0], a[4 * cur_1 + 3]])
                            
                            a[4 * cur_1 + 1] = a[4 * cur_4 + 0]
                            a[4 * cur_2 + 0] = a[4 * cur_4 + 0]
                            a[4 * cur_3 + 2] = a[4 * cur_1 + 2]
                            a[4 * cur_4 + 3] = a[4 * cur_1 + 2]
                            if adj[4 * cur_1 + 2] == -1:
                                print('hehehe')
                            else:
                                adj[4 * adj[4 * cur_1 + 2] + 0] = cur_3
                            if adj[4 * cur_4 + 0] == -1:
                                print('hehehe')
                            else:
                                adj[4 * adj[4 * cur_4 + 0] + 2] = cur_2
                            
                            adj[4 * cur_2 + 0] = adj[4 * cur_4 + 0]
                            adj[4 * cur_3 + 2] = adj[4 * cur_1 + 2]
                            adj[4 * cur_1 + 2] = cur_4
                            adj[4 * cur_4 + 0] = cur_1
                            flag = 1
                            # print('2nd case', a[4 * cur_1 + 0], a[4 * cur_1 + 1], a[4 * cur_1 + 2], a[4 * cur_1 + 3], a[4 * cur_4 + 0], a[4 * cur_4 + 1], a[4 * cur_4 + 2], a[4 * cur_4 + 3])
                            # print('cur2, cur3 =', a[4 * cur_2 + 0], a[4 * cur_2 + 1], a[4 * cur_2 + 2], a[4 * cur_2 + 3], a[4 * cur_3 + 0], a[4 * cur_3 + 1], a[4 * cur_3 + 2], a[4 * cur_3 + 3])
                            # for i in range(n):
                            #     print("i = ", i, '[', a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3], ']', adj[4 * i + 0],adj[4 * i + 1],adj[4 * i + 2],adj[4 * i + 3])
                            # print(cur_1, cur_2, cur_3, cur_4)
                            # draw_rect(a)
                            
                            continue
                        if [i, j, k] == [3, 2, 1] and check_vert_rect(a[4 * cur_1 + 0], a[4 * cur_4 + 0], a[4 * cur_4 + 2], a[4 * cur_1 + 2], vert):
                            vert.remove([a[4 * cur_2 + 1], a[4 * cur_2 + 3]])
                            vert.remove([a[4 * cur_3 + 1], a[4 * cur_3 + 3]])
                            vert.remove([a[4 * cur_2 + 1], a[4 * cur_3 + 3]])
                            
                            vert.append([a[4 * cur_4 + 0], a[4 * cur_1 + 3]])
                            vert.append([a[4 * cur_4 + 1], a[4 * cur_1 + 3]])
                            vert.append([a[4 * cur_4 + 1], a[4 * cur_1 + 2]])
                            
                            a[4 * cur_1 + 0] = a[4 * cur_4 + 1]
                            a[4 * cur_2 + 1] = a[4 * cur_4 + 1]
                            a[4 * cur_3 + 3] = a[4 * cur_1 + 3]
                            a[4 * cur_4 + 2] = a[4 * cur_1 + 3]
                            if adj[4 * cur_1 + 0] == -1:
                                print('emmmm')
                            else:
                                adj[4 * adj[4 * cur_1 + 0] + 2] = cur_3
                            if adj[4 * cur_4 + 2] == -1:
                                print('emmm')
                            else:
                                adj[4 * adj[4 * cur_4 + 2] + 0] = cur_2
                            adj[4 * cur_2 + 2] = adj[4 * cur_4 + 2]
                            adj[4 * cur_3 + 0] = adj[4 * cur_1 + 0]
                            adj[4 * cur_1 + 0] = cur_4
                            adj[4 * cur_4 + 2] = cur_1
                            flag = 1
                            # print('cur2, cur3 =', a[4 * cur_2 + 0], a[4 * cur_2 + 1], a[4 * cur_2 + 2], a[4 * cur_2 + 3], a[4 * cur_3 + 0], a[4 * cur_3 + 1], a[4 * cur_3 + 2], a[4 * cur_3 + 3])
                            # for i in range(n):
                            #     print("i = ", i, '[', a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3], ']', adj[4 * i + 0],adj[4 * i + 1],adj[4 * i + 2],adj[4 * i + 3])
                            # print(cur_1, cur_2, cur_3, cur_4)
                            # print('3rd case', a[4 * cur_1 + 0], a[4 * cur_1 + 1], a[4 * cur_1 + 2], a[4 * cur_1 + 3], a[4 * cur_4 + 0], a[4 * cur_4 + 1], a[4 * cur_4 + 2], a[4 * cur_4 + 3])
                            # draw_rect(a)
                            
                            continue
                        if [i, j, k] == [2, 3, 0] and check_vert_rect(a[4 * cur_4 + 1], a[4 * cur_1 + 1], a[4 * cur_4 + 2], a[4 * cur_1 + 2], vert):
                            vert.remove([a[4 * cur_2 + 0], a[4 * cur_2 + 3]])
                            vert.remove([a[4 * cur_3 + 0], a[4 * cur_3 + 3]])
                            vert.remove([a[4 * cur_2 + 0], a[4 * cur_3 + 3]])
                            
                            vert.append([a[4 * cur_4 + 0], a[4 * cur_1 + 2]])
                            vert.append([a[4 * cur_4 + 0], a[4 * cur_1 + 3]])
                            vert.append([a[4 * cur_4 + 1], a[4 * cur_1 + 3]])

                            a[4 * cur_1 + 1] = a[4 * cur_4 + 0]
                            a[4 * cur_2 + 0] = a[4 * cur_4 + 0]
                            a[4 * cur_3 + 3] = a[4 * cur_1 + 3]
                            a[4 * cur_4 + 2] = a[4 * cur_1 + 3]
                            if adj[4 * cur_1 + 1]  == -1:
                                print('ommmm')
                            else:
                                adj[4 * adj[4 * cur_1 + 1] + 3] = cur_3
                            if adj[4 * cur_4 + 3] == -1:
                                print('ommmm')
                            else:
                                adj[4 * adj[4 * cur_4 + 3] + 1] = cur_2                          
                            adj[4 * cur_2 + 3] = adj[4 * cur_4 + 3]
                            adj[4 * cur_3 + 1] = adj[4 * cur_1 + 1]
                            adj[4 * cur_1 + 1] = cur_4
                            adj[4 * cur_4 + 3] = cur_1
                            flag = 1
                            # print('cur2, cur3 =', a[4 * cur_2 + 0], a[4 * cur_2 + 1], a[4 * cur_2 + 2], a[4 * cur_2 + 3], a[4 * cur_3 + 0], a[4 * cur_3 + 1], a[4 * cur_3 + 2], a[4 * cur_3 + 3])
                            # for i in range(n):
                            #     print("i = ", i, '[', a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3], ']', adj[4 * i + 0],adj[4 * i + 1],adj[4 * i + 2],adj[4 * i + 3])
                            # print(cur_1, cur_2, cur_3, cur_4)
                            # print('4th case', a[4 * cur_1 + 0], a[4 * cur_1 + 1], a[4 * cur_1 + 2], a[4 * cur_1 + 3], a[4 * cur_4 + 0], a[4 * cur_4 + 1], a[4 * cur_4 + 2], a[4 * cur_4 + 3])
                            # draw_rect(a)
                            
                            continue
        # if flag == 1:
        #     print('Im drawing here')
        #     draw_rect(a)
        if flag == 0:
            attempts = attempts + 1
            q.pop(0)
            q.append(cur_1)
        else:
            attempts = 0
    print('COUNTER = ', counter, len(a) // 4, n)
    #draw_rect(a)
    print('flype phase ends')
    #СХЛОПЫВАНИЯ
    #delete_zeroes(a, n, sign)
    n = len(a) // 4
    #adj = fill_adjecent(a, n)
    print('len a', len(a) // 4, 'len adj', len(adj) // 4, 'n = ', n)
    fast_simplify(a, n, sign, adj)

def delete_zeroes(a, n, sign):
    #ЧТО ПЛОХО: В ADJ номера надо менять для корректной работы. а ведь же можно просто рефилл запустить...
    deleted = 0
    i = 0
    while i < n:
        if a[4 * (i - deleted)] == 0:
            del a[4 * (i - deleted) : 4 * (i - deleted) + 4]
            del sign[i - deleted]
            deleted = deleted + 1
        i = i + 1
    # print(a, sign)
    # print('adj = ', adj)
    # print('len a', len(adj) // 4, 'len adj', len(adj) // 4)


    # 1 2 3
    # 2 1 4
    # 4 3 2
    # 3 4 1

def destabilizations(a, n, sign, adj, flag_simp):
    q = []
    n = len(a) // 4
    # for i in range(n):
    #     print(a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3], adj[4 * i + 0], adj[4 * i + 1], adj[4 * i + 2], adj[4 * i + 3])
    for i in range(n):
        q.append(i)
    attempts = 0
    print(q)
    v = free_vert(a, n)
    hor = []
    vert = []
    
    for i in v:
        if not (i[0] in vert):
            vert.append(i[0])
        if not (i[1] in hor):
            hor.append(i[1])

    while(attempts < n):
        i = q[0]
        # if attempts == 0:
        #     draw_rect(a)
        if a[4 * i + 0] == 0:
            q.pop(0)
            q.append(i)
            attempts = attempts + 1
            continue
        if adj[4 * i + 0] == -1 and adj[4 * i + 1] == -1 and adj[4 * i + 2] == -1:
            for k in range(n):
                print(a[4 * k + 0], a[4 * k + 1], a[4 * k + 2], a[4 * k + 3], adj[4 * k + 0], adj[4 * k + 1], adj[4 * k + 2], adj[4 * k + 3])
            for k in range(n):
                print(a[4 * k + 0], a[4 * k + 1], a[4 * k + 2], a[4 * k + 3])
            print(vert)
            print(hor)
            print(i)

            vert.remove(a[4 * i + 1])
            hor.remove(a[4 * i + 3])
            #ПОХОДУ ТУТ НАДО ДОБАВИТЬ УРОВЕНЬ ЕСЛИ Я ВООБЩЕ ПРАВИЛЬНО
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            adj[4 * adj[4 * i + 3] + 1] = -1
            adj[4 * i + 3] = -1
            print('destab - 3')
            attempts = 0
            q.pop(0)
            q.append(i)
            continue
        if adj[4 * i + 0] == -1 and adj[4 * i + 1] == -1 and adj[4 * i + 3] == -1:
            vert.remove(a[4 * i + 0])
            hor.remove(a[4 * i + 3])
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            adj[4 * adj[4 * i + 2] + 0] = -1
            adj[4 * i + 2] = -1
            print('destab - 2')
            attempts = 0
            q.pop(0)
            q.append(i)
            continue
        if adj[4 * i + 0] == -1 and adj[4 * i + 2] == -1 and adj[4 * i + 3] == -1:
            vert.remove(a[4 * i + 0])
            hor.remove(a[4 * i + 2])
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            adj[4 * adj[4 * i + 1] + 3] = -1
            adj[4 * i + 1] = -1
            print('destab - 1')
            attempts = 0
            q.pop(0)
            q.append(i)
            continue
        if adj[4 * i + 3] == -1 and adj[4 * i + 1] == -1 and adj[4 * i + 2] == -1:
            vert.remove(a[4 * i + 1])
            hor.remove(a[4 * i + 2])
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            adj[4 * adj[4 * i + 0] + 2] = -1
            adj[4 * i + 0] = -1
            print('destab - 0')
            attempts = 0
            q.pop(0)
            q.append(i)
            continue
        if flag_simp:
            if adj[4 * i + 0] == -1 and adj[4 * i + 1] == -1 and not (a[4 * i + 2] in hor):
                hor.remove(a[4 * i + 3])
                hor.append(a[4 * i + 2])
                a[4 * i + 0] = 0
                a[4 * i + 1] = 0
                a[4 * i + 2] = 0
                a[4 * i + 3] = 0
                adj[4 * adj[4 * i + 2] + 0] = -1
                adj[4 * adj[4 * i + 3] + 1] = -1
                adj[4 * i + 2] = -1
                adj[4 * i + 3] = -1
                print('destab - 01')
                attempts = 0
                q.pop(0)
                q.append(i)
                continue
            if adj[4 * i + 0] == -1 and adj[4 * i + 3] == -1 and not (a[4 * i + 1] in vert):
                draw_rect(a)
                print('to delete', a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3])
                print(hor)
                print(vert)
                vert.remove(a[4 * i + 0])
                vert.append(a[4 * i + 1])
                a[4 * i + 0] = 0
                a[4 * i + 1] = 0
                a[4 * i + 2] = 0
                a[4 * i + 3] = 0
                adj[4 * adj[4 * i + 1] + 3] = -1
                adj[4 * adj[4 * i + 2] + 0] = -1
                adj[4 * i + 1] = -1
                adj[4 * i + 2] = -1
                print('destab - 03')
                attempts = 0
                q.pop(0)
                q.append(i)
                continue

            if adj[4 * i + 1] == -1 and adj[4 * i + 2] == -1 and not (a[4 * i + 0] in vert):
                vert.remove(a[4 * i + 1])
                vert.append(a[4 * i + 0])
                a[4 * i + 0] = 0
                a[4 * i + 1] = 0
                a[4 * i + 2] = 0
                a[4 * i + 3] = 0
                adj[4 * adj[4 * i + 0] + 2] = -1
                adj[4 * adj[4 * i + 3] + 1] = -1
                adj[4 * i + 0] = -1
                adj[4 * i + 3] = -1
                print('destab - 12')
                attempts = 0
                q.pop(0)
                q.append(i)
                continue
            if adj[4 * i + 2] == -1 and adj[4 * i + 3] == -1 and not (a[4 * i + 3] in hor):
                hor.remove(a[4 * i + 2])
                hor.append(a[4 * i + 3])
                a[4 * i + 0] = 0
                a[4 * i + 1] = 0
                a[4 * i + 2] = 0
                a[4 * i + 3] = 0
                adj[4 * adj[4 * i + 0] + 2] = -1
                adj[4 * adj[4 * i + 1] + 3] = -1
                adj[4 * i + 0] = -1
                adj[4 * i + 1] = -1
                print('destab - 23')
                attempts = 0
                q.pop(0)
                q.append(i)
                continue
        q.pop(0)
        q.append(i)
        attempts = attempts + 1


def fast_simplify(a, n, sign, adj):
    q = []
    counter = 0
    for i in range(n):
        q.append(i)
    attempts = 0
    vert = only_vertices(a, n)
    while attempts < n:
        #print(counter)
        counter = counter + 1
        start = q[0]
        flag = 1
        if a[4 * q[0] + 0] == 0:
            attempts = attempts + 1
            q.pop(0)
            q.append(start)
            continue
        # print('q = ', q[0], sign[q[0]], a[4 * start + 0], a[4 * start + 1], a[4 * start + 2], a[4 * start + 3], 'adj', adj[4 * start + 0], adj[4 * start + 1], adj[4 * start + 2], adj[4 * start + 3])
        if sign[q[0]] == +1:
            cur = start
            left = []
            right = []
            mid = []
            while True:
                l = adj[4 * cur + 0]
                r = adj[4 * cur + 1]
                if l == -1 or r == -1:
                    cur = -1
                    # print('break due lr -1')
                    break
                if adj[4 * l + 1] == adj[4 * r + 0] and adj[4 * r + 0] != -1:
                    left.append(l)
                    right.append(r)
                    mid.append(cur)
                    cur = adj[4 * l + 1]
                else:
                    # print('break due fucking fuck')
                    cur = -1
                    break
                if cur == start:
                    break
            # print('first case', cur == start)
            # print('and second case', check_vert_rect(a[4 * cur + 0], a[4 * cur + 1], a[4 * cur + 3], a[4 * cur + 2], vert))
            # print('cur = ', start, a[4 * start + 0], a[4 * start + 1], a[4 * start + 2], a[4 * start + 3], vert)
            if cur == start and check_vert_rect(a[4 * cur + 0], a[4 * cur + 1], a[4 * cur + 3], a[4 * cur + 2], vert) == 0 and len(left) == 1:
                print("Сначала было слово и слово будет в конце")
            if cur == start and check_vert_rect(a[4 * cur + 0], a[4 * cur + 1], a[4 * cur + 3], a[4 * cur + 2], vert):
                print('simplify 1')
                for i in range(len(left)):
                    # print(a[4 * left[i] + 1], a[4 * left[i] + 2], a[4 * left[i] + 3], a[4 * left[i] + 0], [a[4 * right[i] + 0], a[4 * right[i] + 3]])
                    vert.remove([a[4 * left[i] + 1], a[4 * left[i] + 2]])
                    vert.remove([a[4 * left[i] + 1], a[4 * left[i] + 3]])
                    vert.remove([a[4 * right[i] + 0], a[4 * right[i] + 2]])
                    vert.remove([a[4 * right[i] + 0], a[4 * right[i] + 3]])

                    if left[i] == right[i]:
                        a[4 * left[i] + 0] = 0
                        a[4 * left[i] + 1] = 0
                        a[4 * left[i] + 2] = 0
                        a[4 * left[i] + 3] = 0 
                    else:
                        a[4 * left[i] + 1] = a[4 * right[i] + 1]
                    a[4 * right[i] + 0] = 0
                    a[4 * right[i] + 1] = 0
                    a[4 * right[i] + 2] = 0
                    a[4 * right[i] + 3] = 0
                    a[4 * mid[i] + 0] = 0
                    a[4 * mid[i] + 1] = 0
                    a[4 * mid[i] + 2] = 0
                    a[4 * mid[i] + 3] = 0
                    adj[4 * left[i] + 1] = adj[4 * right[i] + 1]
                    adj[4 * left[i] + 2] = adj[4 * right[i] + 2]

                    if adj[4 * right[i] + 2] == -1:
                        # print('ALARM')
                        pass
                    else:
                        adj[4 * adj[4 * right[i] + 2] + 0] = left[i]

                    if adj[4 * right[i] + 1] == -1:
                        pass
                    else:
                        adj[4 * adj[4 * right[i] + 1] + 3] = left[i]
                
                # print('case 1')
                flag = 0
                # draw_rect(a)
        else:
            cur = start
            up = []
            down = []
            mid = []
            while True:
                u = adj[4 * cur + 0]
                d = adj[4 * cur + 3]
                if u == -1 or d == -1:
                    cur = -1
                    break
                if adj[4 * u + 3] == adj[4 * d + 0] and adj[4 * d + 0] != -1:
                    up.append(u)
                    down.append(d)
                    mid.append(cur)
                    cur = adj[4 * u + 3]
                else:
                    cur = -1
                    break
                if cur == start:
                    break

            # for i in range(len(left)):
            #     print(a[4 * [i] + 0], a[4 * left[i] + 1], a[4 * left[i] + 2], a[4 * left[i] + 3], a[4 * right[i] + 0], a[4 * right[i] + 1], a[4 * right[i] + 2],a[4 * right[i] + 3])
            # print('cur = ', cur, start, a[4 * start + 0], a[4 * start + 1], a[4 * start + 2], a[4 * start + 3])
            if cur == start and check_vert_rect(a[4 * cur + 1], a[4 * cur + 0], a[4 * cur + 2], a[4 * cur + 3], vert):
                print('simplify 2')                
                for i in range(len(up)):
                    # print('up', a[4 * up[i] + 0], a[4 * up[i] + 1], a[4 * up[i] + 2], a[4 * up[i] + 3], 'down', a[4 * down[i] + 0], a[4 * down[i] + 1], a[4 * down[i] + 2], a[4 * down[i] + 3])
                    vert.remove([a[4 * up[i] + 0], a[4 * up[i] + 2]])
                    vert.remove([a[4 * up[i] + 1], a[4 * up[i] + 2]])
                    vert.remove([a[4 * down[i] + 0], a[4 * down[i] + 3]])
                    vert.remove([a[4 * down[i] + 1], a[4 * down[i] + 3]])

                    if up[i] == down[i]:
                        a[4 * up[i] + 0] = 0
                        a[4 * up[i] + 1] = 0
                        a[4 * up[i] + 2] = 0
                        a[4 * up[i] + 3] = 0
                    else:
                        a[4 * up[i] + 2] = a[4 * down[i] + 2]
                    a[4 * down[i] + 0] = 0
                    a[4 * down[i] + 1] = 0
                    a[4 * down[i] + 2] = 0
                    a[4 * down[i] + 3] = 0
                    a[4 * mid[i] + 0] = 0
                    a[4 * mid[i] + 1] = 0
                    a[4 * mid[i] + 2] = 0
                    a[4 * mid[i] + 3] = 0
                    adj[4 * up[i] + 2] = adj[4 * down[i] + 2]
                    adj[4 * up[i] + 3] = adj[4 * down[i] + 3]
                    if adj[4 * down[i] + 3] == -1:
                        # print('ALARM')
                        pass
                    else:
                        adj[4 * adj[4 * down[i] + 3] + 1] = up[i]
                        
                    if adj[4 * down[i] + 2] == -1:
                        pass
                    else:
                        adj[4 * adj[4 * down[i] + 2] + 0] = up[i]

                flag = 0
                # print('cimpl case 2')
                #draw_rect(a)

        q.pop(0)
        q.append(start)
        if flag:
            attempts = attempts + 1
        else:
            #draw_rect(a)
            attempts = 0
    print('att = ', attempts, 'counter = ', counter)
    # print(q)
    # for i in range(n):
    #     print(i, a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3], 'adj', adj[4 * i + 0], adj[4 * i + 1], adj[4 * i + 2], adj[4 * i + 3], 'sign', sign[i])
    destabilizations(a, n, sign, adj, 1)
  



# rect = [1, 2, 1, 3, 2, 3, 3, 1, 3, 4, 1, 2]
#rect = [x1,x2, y1, y2, ...] size = 4n 
# sign = [1, -1, 1]
#sign = [sign(r1), sign(r2), ...] size = n

# rect = [1, 2, 1, 3, 2, 3, 3, 1, 3, 4, 1, 2]
# sign = [1, -1, 1]
# size = 3










# for i in range(size):
#     print("i = ", i, '[', rect[4 * i + 0], rect[4 * i + 1], rect[4 * i + 2], rect[4 * i + 3], ']', adj[4 * i + 0],adj[4 * i + 1],adj[4 * i + 2],adj[4 * i + 3])
# draw_rect(rect)

# size = len(sign)
# for i in range(len(rect)):
#     rect[i] = rect[i] + 1

sign = []

myflag = 14

if myflag == 1:
    rect = [43, 44, 7, 17, 44, 45, 17, 19, 44, 46, 860, 7, 1081, 1083, 860, 7, 1082, 1083, 746, 859, 1083, 1084, 7, 746, 1084, 1086, 746, 7, 1085, 1086, 744, 745, 1086, 1087, 745, 746, 1083, 1088, 859, 860, 1389, 1391, 744, 7, 1390, 1391, 10, 16, 1392, 1393, 14, 15, 1391, 1393, 16, 744, 1393, 1394, 15, 16, 1393, 1395, 744, 14, 1391, 1396, 7, 10, 1404, 1405, 756, 804, 1405, 1407, 804, 756, 1406, 1407, 802, 803, 1407, 1408, 803, 804, 1395, 1409, 14, 744, 1407, 1409, 756, 802, 1409, 1410, 744, 756, 1409, 1411, 802, 14, 2467, 2468, 9, 12, 2468, 2469, 12, 14, 2468, 2470, 802, 9, 2487, 2488, 5, 8, 2488, 2489, 8, 9, 2488, 2490, 802, 5, 2491, 2492, 2, 4, 2490, 2492, 5, 802, 2492, 2493, 4, 5, 2492, 2494, 802, 2, 2880, 2882, 802, 2, 2881, 2882, 755, 800, 2882, 2883, 800, 802, 2896, 2898, 755, 2, 2897, 2898, 742, 754, 2898, 2899, 754, 755, 2898, 2900, 2, 742, 2900, 2902, 742, 2, 2901, 2902, 739, 741, 2902, 2903, 741, 742, 3100, 3102, 739, 2, 3101, 3102, 718, 737, 3102, 3103, 737, 739, 3116, 3118, 718, 2, 3117, 3118, 713, 717, 3118, 3119, 717, 718, 3118, 3120, 2, 713, 3120, 3122, 713, 2, 3121, 3122, 710, 712, 3122, 3123, 712, 713, 3307, 3308, 721, 723, 3308, 3309, 710, 721, 3308, 3310, 723, 2, 3310, 3311, 2, 723, 3311, 3313, 723, 2, 3312, 3313, 699, 722, 3313, 3314, 722, 723, 3320, 3322, 699, 2, 3321, 3322, 689, 698, 3322, 3323, 698, 699, 3322, 3324, 2, 689, 3324, 3326, 689, 2, 3325, 3326, 686, 688, 3326, 3327, 688, 689, 3399, 3400, 773, 794, 3400, 3402, 794, 773, 3401, 3402, 792, 793, 3402, 3403, 793, 794, 3407, 3408, 764, 772, 3402, 3408, 773, 792, 3408, 3409, 772, 773, 3408, 3410, 792, 764, 3411, 3412, 761, 763, 3410, 3412, 764, 792, 3412, 3413, 763, 764, 3412, 3414, 792, 761, 3415, 3416, 729, 731, 3416, 3417, 686, 729, 3416, 3418, 731, 2, 3418, 3419, 2, 731, 3419, 3421, 731, 2, 3420, 3421, 728, 730, 3421, 3422, 730, 731, 3427, 3428, 813, 826, 3428, 3430, 826, 813, 3429, 3430, 824, 825, 3430, 3431, 825, 826, 3414, 3432, 761, 792, 3430, 3432, 813, 824, 3432, 3433, 792, 813, 3432, 3434, 824, 761, 3443, 3444, 747, 759, 3444, 3445, 759, 761, 3444, 3446, 824, 747, 3421, 3460, 2, 728, 3460, 3461, 728, 747, 3460, 3462, 824, 2, 3767, 3768, 829, 838, 3768, 3769, 824, 829, 3768, 3770, 838, 2, 3942, 3944, 838, 2, 3943, 3944, 809, 837, 3944, 3945, 837, 838, 3951, 3953, 809, 2, 3952, 3953, 785, 808, 3953, 3954, 808, 809, 3953, 3955, 2, 785, 3955, 3957, 785, 2, 3956, 3957, 782, 784, 3957, 3958, 784, 785, 3979, 3980, 807, 843, 3980, 3982, 843, 807, 3981, 3982, 841, 842, 3982, 3983, 842, 843, 3982, 3984, 807, 841, 3984, 3985, 782, 807, 3984, 3986, 841, 2, 4011, 4013, 841, 2, 4012, 4013, 806, 840, 4013, 4014, 840, 841, 4020, 4022, 806, 2, 4021, 4022, 780, 805, 4022, 4023, 805, 806, 4022, 4024, 2, 780, 4024, 4026, 780, 2, 4025, 4026, 777, 779, 4026, 4027, 779, 780, 4026, 4028, 2, 777, 4028, 4030, 777, 2, 4029, 4030, 607, 609, 4030, 4031, 2, 607, 4032, 4033, 606, 608, 4030, 4033, 609, 777, 4033, 4034, 608, 609, 4033, 4035, 777, 606, 4035, 4036, 606, 777, 2459, 2463, 802, 14, 2470, 2471, 9, 802, 2471, 2475, 802, 9, 2483, 2488, 9, 802, 2479, 2483, 802, 9, 2458, 2459, 14, 802, 2456, 2458, 802, 14, 2463, 2464, 14, 802, 2466, 2468, 14, 802, 2464, 2466, 802, 14, 2475, 2476, 9, 802, 2478, 2479, 9, 802, 2476, 2478, 802, 9, 3684, 3686, 824, 2, 35, 39, 860, 19, 46, 47, 7, 860, 47, 51, 860, 7, 55, 59, 860, 7, 1368, 1372, 744, 7, 34, 35, 19, 860, 32, 34, 860, 19, 39, 40, 19, 860, 42, 44, 19, 860, 40, 42, 860, 19, 51, 52, 7, 860, 54, 55, 7, 860, 52, 54, 860, 7, 1372, 1373, 7, 744, 1373, 1375, 744, 7, 3645, 3651, 824, 2, 3665, 3671, 824, 2, 3683, 3684, 2, 824, 3677, 3683, 824, 2, 3708, 3714, 824, 2, 3644, 3645, 2, 824, 3640, 3644, 824, 2, 3651, 3652, 2, 824, 3652, 3656, 824, 2, 3664, 3665, 2, 824, 3660, 3664, 824, 2, 3671, 3672, 2, 824, 3676, 3677, 2, 824, 3672, 3676, 824, 2, 3714, 3715, 2, 824, 3715, 3719, 824, 2, 3731, 3735, 824, 2, 3847, 3851, 838, 2, 3858, 3862, 838, 2, 3866, 3870, 838, 2, 3846, 3847, 2, 838, 3844, 3846, 838, 2, 3851, 3852, 2, 838, 3852, 3854, 838, 2, 3854, 3855, 2, 838, 3857, 3858, 2, 838, 3855, 3857, 838, 2, 3862, 3863, 2, 838, 3865, 3866, 2, 838, 3863, 3865, 838, 2, 3926, 3928, 838, 2, 3592, 3596, 824, 2, 3608, 3612, 824, 2, 3616, 3620, 824, 2, 3620, 3621, 2, 824, 3621, 3625, 824, 2, 3591, 3592, 2, 824, 3589, 3591, 824, 2, 3596, 3597, 2, 824, 3597, 3599, 824, 2, 3607, 3608, 2, 824, 3605, 3607, 824, 2, 3612, 3613, 2, 824, 3615, 3616, 2, 824, 3613, 3615, 824, 2, 3625, 3626, 2, 824, 3626, 3628, 824, 2, 3628, 3629, 2, 824, 3629, 3631, 824, 2, 163, 171, 860, 7, 191, 199, 860, 7, 207, 215, 860, 7, 383, 391, 860, 7, 162, 163, 7, 860, 156, 162, 860, 7, 171, 172, 7, 860, 172, 178, 860, 7, 190, 191, 7, 860, 184, 190, 860, 7, 199, 200, 7, 860, 206, 207, 7, 860, 200, 206, 860, 7, 391, 392, 7, 860, 392, 398, 860, 7, 416, 422, 860, 7, 2831, 2835, 802, 2, 2847, 2851, 802, 2, 2859, 2880, 2, 802, 2855, 2859, 802, 2, 2830, 2831, 2, 802, 2828, 2830, 802, 2, 2835, 2836, 2, 802, 2836, 2838, 802, 2, 2846, 2847, 2, 802, 2844, 2846, 802, 2, 2851, 2852, 2, 802, 2854, 2855, 2, 802, 2852, 2854, 802, 2, 3083, 3085, 739, 2, 2698, 2702, 802, 2, 2766, 2770, 802, 2, 2697, 2698, 2, 802, 2695, 2697, 802, 2, 2702, 2703, 2, 802, 2703, 2705, 802, 2, 2770, 2771, 2, 802, 2771, 2773, 802, 2, 2787, 2789, 802, 2, 1940, 1948, 802, 14, 1968, 1976, 802, 14, 1984, 1992, 802, 14, 2213, 2221, 802, 14, 1939, 1940, 14, 802, 1933, 1939, 802, 14, 1948, 1949, 14, 802, 1949, 1955, 802, 14, 1967, 1968, 14, 802, 1961, 1967, 802, 14, 1976, 1977, 14, 802, 1983, 1984, 14, 802, 1977, 1983, 802, 14, 2221, 2222, 14, 802, 2222, 2228, 802, 14, 2246, 2252, 802, 14, 1620, 1628, 802, 14, 1652, 1660, 802, 14, 1668, 1676, 802, 14, 1892, 1900, 802, 14, 1619, 1620, 14, 802, 1613, 1619, 802, 14, 1628, 1629, 14, 802, 1629, 1635, 802, 14, 1651, 1652, 14, 802, 1645, 1651, 802, 14, 1660, 1661, 14, 802, 1667, 1668, 14, 802, 1661, 1667, 802, 14, 1900, 1901, 14, 802, 1901, 1907, 802, 14, 100, 106, 860, 7, 120, 126, 860, 7, 132, 138, 860, 7, 231, 237, 860, 7, 324, 330, 860, 7, 99, 100, 7, 860, 95, 99, 860, 7, 106, 107, 7, 860, 107, 111, 860, 7, 119, 120, 7, 860, 115, 119, 860, 7, 126, 127, 7, 860, 131, 132, 7, 860, 127, 131, 860, 7, 237, 238, 7, 860, 238, 242, 860, 7, 330, 331, 7, 860, 331, 335, 860, 7, 347, 351, 860, 7, 3918, 3922, 838, 2, 3928, 3929, 2, 838, 3929, 3933, 838, 2, 3941, 3942, 2, 838, 3937, 3941, 838, 2, 3962, 3966, 782, 2, 3966, 3967, 2, 782, 3967, 3971, 782, 2, 3917, 3918, 2, 838, 3915, 3917, 838, 2, 3922, 3923, 2, 838, 3925, 3926, 2, 838, 3923, 3925, 838, 2, 3933, 3934, 2, 838, 3936, 3937, 2, 838, 3934, 3936, 838, 2, 3957, 3959, 2, 782, 3961, 3962, 2, 782, 3959, 3961, 782, 2, 3971, 3972, 2, 782, 3974, 3984, 2, 782, 3972, 3974, 782, 2, 3995, 3997, 841, 2, 3044, 3050, 739, 2, 3064, 3070, 739, 2, 3082, 3083, 2, 739, 3076, 3082, 739, 2, 3208, 3214, 710, 2, 3214, 3215, 2, 710, 3215, 3221, 710, 2, 3553, 3559, 824, 2, 3043, 3044, 2, 739, 3039, 3043, 739, 2, 3050, 3051, 2, 739, 3051, 3055, 739, 2, 3063, 3064, 2, 739, 3059, 3063, 739, 2, 3070, 3071, 2, 739, 3075, 3076, 2, 739, 3071, 3075, 739, 2, 3207, 3208, 2, 710, 3203, 3207, 710, 2, 3221, 3222, 2, 710, 3226, 3308, 2, 710, 3222, 3226, 710, 2, 3559, 3560, 2, 824, 3560, 3564, 824, 2, 3576, 3580, 824, 2, 2727, 2733, 802, 2, 2747, 2753, 802, 2, 2765, 2766, 2, 802, 2759, 2765, 802, 2, 2803, 2809, 802, 2, 2726, 2727, 2, 802, 2722, 2726, 802, 2, 2733, 2734, 2, 802, 2734, 2738, 802, 2, 2746, 2747, 2, 802, 2742, 2746, 802, 2, 2753, 2754, 2, 802, 2758, 2759, 2, 802, 2754, 2758, 802, 2, 2809, 2810, 2, 802, 2810, 2814, 802, 2, 2814, 2815, 2, 802, 2815, 2819, 802, 2, 1825, 1835, 802, 14, 1861, 1871, 802, 14, 1891, 1892, 14, 802, 1881, 1891, 802, 14, 2126, 2136, 802, 14, 1824, 1825, 14, 802, 1816, 1824, 802, 14, 1835, 1836, 14, 802, 1836, 1844, 802, 14, 1860, 1861, 14, 802, 1852, 1860, 802, 14, 1871, 1872, 14, 802, 1880, 1881, 14, 802, 1872, 1880, 802, 14, 2136, 2137, 14, 802, 2137, 2145, 802, 14, 2169, 2177, 802, 14, 496, 502, 860, 7, 516, 522, 860, 7, 528, 534, 860, 7, 604, 610, 860, 7, 672, 678, 860, 7, 495, 496, 7, 860, 491, 495, 860, 7, 502, 503, 7, 860, 503, 507, 860, 7, 515, 516, 7, 860, 511, 515, 860, 7, 522, 523, 7, 860, 527, 528, 7, 860, 523, 527, 860, 7, 610, 611, 7, 860, 611, 615, 860, 7, 678, 679, 7, 860, 679, 683, 860, 7, 695, 699, 860, 7, 2599, 2605, 802, 2, 2619, 2625, 802, 2, 2631, 2637, 802, 2, 2992, 2998, 739, 2, 2598, 2599, 2, 802, 2594, 2598, 802, 2, 2605, 2606, 2, 802, 2606, 2610, 802, 2, 2618, 2619, 2, 802, 2614, 2618, 802, 2, 2625, 2626, 2, 802, 2630, 2631, 2, 802, 2626, 2630, 802, 2, 2998, 2999, 2, 739, 2999, 3003, 739, 2, 3015, 3019, 739, 2, 1469, 1475, 802, 14, 1493, 1499, 802, 14, 1505, 1511, 802, 14, 1745, 1751, 802, 14, 1468, 1469, 14, 802, 1464, 1468, 802, 14, 1475, 1476, 14, 802, 1476, 1480, 802, 14, 1492, 1493, 14, 802, 1488, 1492, 802, 14, 1499, 1500, 14, 802, 1504, 1505, 14, 802, 1500, 1504, 802, 14, 1751, 1752, 14, 802, 1752, 1756, 802, 14, 1776, 1780, 802, 14, 1733, 1739, 802, 14, 1756, 1757, 14, 802, 1757, 1763, 802, 14, 1775, 1776, 14, 802, 1769, 1775, 802, 14, 2034, 2040, 802, 14, 1732, 1733, 14, 802, 1728, 1732, 802, 14, 1739, 1740, 14, 802, 1744, 1745, 14, 802, 1740, 1744, 802, 14, 1763, 1764, 14, 802, 1768, 1769, 14, 802, 1764, 1768, 802, 14, 2040, 2041, 14, 802, 2041, 2045, 802, 14, 2057, 2061, 802, 14, 76, 82, 860, 7, 94, 95, 7, 860, 88, 94, 860, 7, 256, 262, 860, 7, 63, 67, 860, 7, 75, 76, 7, 860, 71, 75, 860, 7, 82, 83, 7, 860, 87, 88, 7, 860, 83, 87, 860, 7, 262, 263, 7, 860, 263, 267, 860, 7, 279, 283, 860, 7, 451, 455, 860, 7, 467, 471, 860, 7, 475, 479, 860, 7, 635, 639, 860, 7, 842, 846, 860, 7, 450, 451, 7, 860, 448, 450, 860, 7, 455, 456, 7, 860, 456, 458, 860, 7, 466, 467, 7, 860, 464, 466, 860, 7, 471, 472, 7, 860, 474, 475, 7, 860, 472, 474, 860, 7, 639, 640, 7, 860, 640, 642, 860, 7, 846, 847, 7, 860, 847, 849, 860, 7, 863, 865, 860, 7, 3986, 3987, 2, 841, 3987, 3991, 841, 2, 3997, 3998, 2, 841, 3998, 4002, 841, 2, 4010, 4011, 2, 841, 4006, 4010, 841, 2, 4013, 4015, 2, 806, 4019, 4020, 2, 806, 4015, 4019, 806, 2, 3991, 3992, 2, 841, 3994, 3995, 2, 841, 3992, 3994, 841, 2, 4002, 4003, 2, 841, 4005, 4006, 2, 841, 4003, 4005, 841, 2, 3784, 3790, 838, 2, 3804, 3810, 838, 2, 3816, 3822, 838, 2, 3879, 3885, 838, 2, 3783, 3784, 2, 838, 3779, 3783, 838, 2, 3790, 3791, 2, 838, 3791, 3795, 838, 2, 3803, 3804, 2, 838, 3799, 3803, 838, 2, 3810, 3811, 2, 838, 3815, 3816, 2, 838, 3811, 3815, 838, 2, 3885, 3886, 2, 838, 3886, 3890, 838, 2, 3902, 3906, 838, 2, 3462, 3463, 2, 824, 3463, 3467, 824, 2, 3479, 3483, 824, 2, 3487, 3491, 824, 2, 3467, 3468, 2, 824, 3468, 3470, 824, 2, 3478, 3479, 2, 824, 3476, 3478, 824, 2, 3483, 3484, 2, 824, 3486, 3487, 2, 824, 3484, 3486, 824, 2, 3508, 3510, 824, 2, 2514, 2522, 802, 2, 2542, 2550, 802, 2, 2558, 2566, 802, 2, 2927, 2935, 739, 2, 2513, 2514, 2, 802, 2507, 2513, 802, 2, 2522, 2523, 2, 802, 2523, 2529, 802, 2, 2541, 2542, 2, 802, 2535, 2541, 802, 2, 2550, 2551, 2, 802, 2557, 2558, 2, 802, 2551, 2557, 802, 2, 2935, 2936, 2, 739, 2936, 2942, 739, 2, 2960, 2966, 739, 2, 849, 850, 7, 860, 850, 854, 860, 7, 862, 863, 7, 860, 858, 862, 860, 7, 841, 842, 7, 860, 839, 841, 860, 7, 854, 855, 7, 860, 857, 858, 7, 860, 855, 857, 860, 7, 1080, 1081, 7, 860, 1078, 1080, 860, 7, 20, 26, 860, 19, 144, 150, 860, 7, 230, 231, 7, 860, 224, 230, 860, 7, 360, 366, 860, 7, 404, 410, 860, 7, 433, 439, 860, 7, 10, 14, 860, 19, 14, 15, 19, 860, 19, 20, 19, 860, 15, 19, 860, 19, 138, 139, 7, 860, 143, 144, 7, 860, 139, 143, 860, 7, 150, 151, 7, 860, 155, 156, 7, 860, 151, 155, 860, 7, 178, 179, 7, 860, 183, 184, 7, 860, 179, 183, 860, 7, 223, 224, 7, 860, 219, 223, 860, 7, 366, 367, 7, 860, 367, 371, 860, 7, 398, 399, 7, 860, 403, 404, 7, 860, 399, 403, 860, 7, 410, 411, 7, 860, 415, 416, 7, 860, 411, 415, 860, 7, 422, 423, 7, 860, 423, 427, 860, 7, 427, 428, 7, 860, 432, 433, 7, 860, 428, 432, 860, 7, 588, 592, 860, 7, 1288, 1296, 744, 7, 1316, 1324, 744, 7, 1332, 1340, 744, 7, 1635, 1636, 14, 802, 1644, 1645, 14, 802, 1636, 1644, 802, 14, 1287, 1288, 7, 744, 1281, 1287, 744, 7, 1296, 1297, 7, 744, 1297, 1303, 744, 7, 1315, 1316, 7, 744, 1309, 1315, 744, 7, 1324, 1325, 7, 744, 1331, 1332, 7, 744, 1325, 1331, 744, 7, 1676, 1677, 14, 802, 1677, 1683, 802, 14, 559, 563, 860, 7, 575, 579, 860, 7, 587, 588, 7, 860, 583, 587, 860, 7, 763, 767, 860, 7, 558, 559, 7, 860, 556, 558, 860, 7, 563, 564, 7, 860, 564, 566, 860, 7, 574, 575, 7, 860, 572, 574, 860, 7, 579, 580, 7, 860, 582, 583, 7, 860, 580, 582, 860, 7, 767, 768, 7, 860, 768, 770, 860, 7, 784, 786, 860, 7, 1177, 1187, 744, 7, 1213, 1223, 744, 7, 1233, 1243, 744, 7, 1545, 1555, 802, 14, 1176, 1177, 7, 744, 1168, 1176, 744, 7, 1187, 1188, 7, 744, 1188, 1196, 744, 7, 1212, 1213, 7, 744, 1204, 1212, 744, 7, 1223, 1224, 7, 744, 1232, 1233, 7, 744, 1224, 1232, 744, 7, 1555, 1556, 14, 802, 1556, 1564, 802, 14, 1588, 1596, 802, 14, 295, 299, 860, 7, 311, 315, 860, 7, 323, 324, 7, 860, 319, 323, 860, 7, 483, 487, 860, 7, 543, 547, 860, 7, 555, 556, 7, 860, 551, 555, 860, 7, 619, 623, 860, 7, 651, 655, 860, 7, 687, 691, 860, 7, 703, 707, 860, 7, 918, 922, 860, 7, 294, 295, 7, 860, 292, 294, 860, 7, 299, 300, 7, 860, 300, 302, 860, 7, 310, 311, 7, 860, 308, 310, 860, 7, 315, 316, 7, 860, 318, 319, 7, 860, 316, 318, 860, 7, 479, 480, 7, 860, 482, 483, 7, 860, 480, 482, 860, 7, 487, 488, 7, 860, 490, 491, 7, 860, 488, 490, 860, 7, 507, 508, 7, 860, 510, 511, 7, 860, 508, 510, 860, 7, 542, 543, 7, 860, 540, 542, 860, 7, 547, 548, 7, 860, 550, 551, 7, 860, 548, 550, 860, 7, 615, 616, 7, 860, 618, 619, 7, 860, 616, 618, 860, 7, 623, 624, 7, 860, 624, 626, 860, 7, 655, 656, 7, 860, 656, 658, 860, 7, 683, 684, 7, 860, 686, 687, 7, 860, 684, 686, 860, 7, 691, 692, 7, 860, 694, 695, 7, 860, 692, 694, 860, 7, 699, 700, 7, 860, 702, 703, 7, 860, 700, 702, 860, 7, 707, 708, 7, 860, 708, 710, 860, 7, 922, 923, 7, 860, 923, 925, 860, 7, 939, 941, 860, 7, 3434, 3435, 761, 824, 3435, 3439, 824, 761, 3446, 3447, 747, 824, 3447, 3451, 824, 747, 3459, 3460, 747, 824, 3455, 3459, 824, 747, 3527, 3531, 824, 2, 3540, 3544, 824, 2, 3552, 3553, 2, 824, 3548, 3552, 824, 2, 3770, 3771, 2, 838, 3771, 3775, 838, 2, 3831, 3835, 838, 2, 3843, 3844, 2, 838, 3839, 3843, 838, 2, 3870, 3871, 2, 838, 3871, 3875, 838, 2, 3894, 3898, 838, 2, 3914, 3915, 2, 838, 3910, 3914, 838, 2, 3944, 3946, 2, 809, 3950, 3951, 2, 809, 3946, 3950, 809, 2, 3439, 3440, 761, 824, 3442, 3444, 761, 824, 3440, 3442, 824, 761, 3451, 3452, 747, 824, 3454, 3455, 747, 824, 3452, 3454, 824, 747, 3526, 3527, 2, 824, 3524, 3526, 824, 2, 3539, 3540, 2, 824, 3537, 3539, 824, 2, 3544, 3545, 2, 824, 3547, 3548, 2, 824, 3545, 3547, 824, 2, 3775, 3776, 2, 838, 3778, 3779, 2, 838, 3776, 3778, 838, 2, 3795, 3796, 2, 838, 3798, 3799, 2, 838, 3796, 3798, 838, 2, 3830, 3831, 2, 838, 3828, 3830, 838, 2, 3835, 3836, 2, 838, 3838, 3839, 2, 838, 3836, 3838, 838, 2, 3875, 3876, 2, 838, 3878, 3879, 2, 838, 3876, 3878, 838, 2, 3890, 3891, 2, 838, 3893, 3894, 2, 838, 3891, 3893, 838, 2, 3898, 3899, 2, 838, 3901, 3902, 2, 838, 3899, 3901, 838, 2, 3906, 3907, 2, 838, 3909, 3910, 2, 838, 3907, 3909, 838, 2, 3344, 3350, 686, 2, 3361, 3367, 686, 2, 3379, 3416, 2, 686, 3373, 3379, 686, 2, 3343, 3344, 2, 686, 3339, 3343, 686, 2, 3350, 3351, 2, 686, 3351, 3355, 686, 2, 3355, 3356, 2, 686, 3360, 3361, 2, 686, 3356, 3360, 686, 2, 3367, 3368, 2, 686, 3372, 3373, 2, 686, 3368, 3372, 686, 2, 3491, 3492, 2, 824, 3492, 3496, 824, 2, 2006, 2012, 802, 14, 2283, 2289, 802, 14, 2295, 2301, 802, 14, 2506, 2507, 2, 802, 2500, 2506, 802, 2, 2575, 2581, 802, 2, 2593, 2594, 2, 802, 2587, 2593, 802, 2, 2902, 2904, 2, 739, 2904, 2910, 739, 2, 2948, 2954, 739, 2, 2972, 2978, 739, 2, 3122, 3124, 2, 710, 3124, 3130, 710, 2, 1992, 1993, 14, 802, 1993, 1997, 802, 14, 2005, 2006, 14, 802, 2001, 2005, 802, 14, 2270, 2274, 802, 14, 2282, 2283, 14, 802, 2278, 2282, 802, 14, 2289, 2290, 14, 802, 2294, 2295, 14, 802, 2290, 2294, 802, 14, 2494, 2495, 2, 802, 2499, 2500, 2, 802, 2495, 2499, 802, 2, 2529, 2530, 2, 802, 2534, 2535, 2, 802, 2530, 2534, 802, 2, 2574, 2575, 2, 802, 2570, 2574, 802, 2, 2581, 2582, 2, 802, 2586, 2587, 2, 802, 2582, 2586, 802, 2, 2910, 2911, 2, 739, 2911, 2915, 739, 2, 2942, 2943, 2, 739, 2947, 2948, 2, 739, 2943, 2947, 739, 2, 2954, 2955, 2, 739, 2959, 2960, 2, 739, 2955, 2959, 739, 2, 2966, 2967, 2, 739, 2971, 2972, 2, 739, 2967, 2971, 739, 2, 2978, 2979, 2, 739, 2979, 2983, 739, 2, 3130, 3131, 2, 710, 3131, 3135, 710, 2, 3147, 3151, 710, 2, 879, 885, 860, 7, 899, 905, 860, 7, 917, 918, 7, 860, 911, 917, 860, 7, 1094, 1100, 744, 7, 1109, 1115, 744, 7, 1121, 1127, 744, 7, 1441, 1447, 802, 14, 878, 879, 7, 860, 874, 878, 860, 7, 885, 886, 7, 860, 886, 890, 860, 7, 898, 899, 7, 860, 894, 898, 860, 7, 905, 906, 7, 860, 910, 911, 7, 860, 906, 910, 860, 7, 1086, 1089, 7, 744, 1093, 1094, 7, 744, 1089, 1093, 744, 7, 1108, 1109, 7, 744, 1104, 1108, 744, 7, 1115, 1116, 7, 744, 1120, 1121, 7, 744, 1116, 1120, 744, 7, 1447, 1448, 14, 802, 1448, 1452, 802, 14, 974, 982, 860, 7, 1002, 1010, 860, 7, 1018, 1026, 860, 7, 1152, 1160, 744, 7, 1256, 1264, 744, 7, 1280, 1281, 7, 744, 1272, 1280, 744, 7, 1511, 1512, 14, 802, 1512, 1520, 802, 14, 1572, 1580, 802, 14, 1612, 1613, 14, 802, 1604, 1612, 802, 14, 1800, 1808, 802, 14, 1907, 1908, 14, 802, 1908, 1916, 802, 14, 1932, 1933, 14, 802, 1924, 1932, 802, 14, 2093, 2101, 802, 14, 2153, 2161, 802, 14, 2185, 2193, 802, 14, 2378, 2386, 802, 14, 973, 974, 7, 860, 967, 973, 860, 7, 982, 983, 7, 860, 983, 989, 860, 7, 1001, 1002, 7, 860, 995, 1001, 860, 7, 1010, 1011, 7, 860, 1017, 1018, 7, 860, 1011, 1017, 860, 7, 1151, 1152, 7, 744, 1145, 1151, 744, 7, 1160, 1161, 7, 744, 1167, 1168, 7, 744, 1161, 1167, 744, 7, 1196, 1197, 7, 744, 1203, 1204, 7, 744, 1197, 1203, 744, 7, 1255, 1256, 7, 744, 1249, 1255, 744, 7, 1264, 1265, 7, 744, 1271, 1272, 7, 744, 1265, 1271, 744, 7, 1520, 1521, 14, 802, 1521, 1527, 802, 14, 1564, 1565, 14, 802, 1571, 1572, 14, 802, 1565, 1571, 802, 14, 1580, 1581, 14, 802, 1587, 1588, 14, 802, 1581, 1587, 802, 14, 1596, 1597, 14, 802, 1603, 1604, 14, 802, 1597, 1603, 802, 14, 1799, 1800, 14, 802, 1793, 1799, 802, 14, 1808, 1809, 14, 802, 1815, 1816, 14, 802, 1809, 1815, 802, 14, 1844, 1845, 14, 802, 1851, 1852, 14, 802, 1845, 1851, 802, 14, 1916, 1917, 14, 802, 1923, 1924, 14, 802, 1917, 1923, 802, 14, 2101, 2102, 14, 802, 2102, 2108, 802, 14, 2145, 2146, 14, 802, 2152, 2153, 14, 802, 2146, 2152, 802, 14, 2161, 2162, 14, 802, 2168, 2169, 14, 802, 2162, 2168, 802, 14, 2177, 2178, 14, 802, 2184, 2185, 14, 802, 2178, 2184, 802, 14, 2193, 2194, 14, 802, 2194, 2200, 802, 14, 2386, 2387, 14, 802, 2387, 2393, 802, 14, 2411, 2417, 802, 14, 1411, 1412, 14, 802, 1412, 1416, 802, 14, 1428, 1432, 802, 14, 1440, 1441, 14, 802, 1436, 1440, 802, 14, 1712, 1716, 802, 14, 2021, 2025, 802, 14, 2033, 2034, 14, 802, 2029, 2033, 802, 14, 2310, 2314, 802, 14, 2318, 2322, 802, 14, 2326, 2330, 802, 14, 2342, 2346, 802, 14, 2350, 2354, 802, 14, 2646, 2650, 802, 2, 2654, 2658, 802, 2, 2705, 2706, 2, 802, 2706, 2710, 802, 2, 2882, 2891, 2, 755, 2895, 2896, 2, 755, 2891, 2895, 755, 2, 2919, 2923, 739, 2, 2991, 2992, 2, 739, 2987, 2991, 739, 2, 3007, 3011, 739, 2, 3023, 3027, 739, 2, 3102, 3111, 2, 718, 3115, 3116, 2, 718, 3111, 3115, 718, 2, 3139, 3143, 710, 2, 3155, 3159, 710, 2, 3171, 3175, 710, 2, 3313, 3315, 2, 699, 3319, 3320, 2, 699, 3315, 3319, 699, 2, 1416, 1417, 14, 802, 1417, 1419, 802, 14, 1427, 1428, 14, 802, 1425, 1427, 802, 14, 1432, 1433, 14, 802, 1435, 1436, 14, 802, 1433, 1435, 802, 14, 1716, 1717, 14, 802, 1717, 1719, 802, 14, 1997, 1998, 14, 802, 2000, 2001, 14, 802, 1998, 2000, 802, 14, 2020, 2021, 14, 802, 2018, 2020, 802, 14, 2025, 2026, 14, 802, 2028, 2029, 14, 802, 2026, 2028, 802, 14, 2274, 2275, 14, 802, 2277, 2278, 14, 802, 2275, 2277, 802, 14, 2309, 2310, 14, 802, 2307, 2309, 802, 14, 2314, 2315, 14, 802, 2317, 2318, 14, 802, 2315, 2317, 802, 14, 2322, 2323, 14, 802, 2325, 2326, 14, 802, 2323, 2325, 802, 14, 2330, 2331, 14, 802, 2331, 2333, 802, 14, 2341, 2342, 14, 802, 2339, 2341, 802, 14, 2346, 2347, 14, 802, 2349, 2350, 14, 802, 2347, 2349, 802, 14, 2566, 2567, 2, 802, 2569, 2570, 2, 802, 2567, 2569, 802, 2, 2610, 2611, 2, 802, 2613, 2614, 2, 802, 2611, 2613, 802, 2, 2645, 2646, 2, 802, 2643, 2645, 802, 2, 2650, 2651, 2, 802, 2653, 2654, 2, 802, 2651, 2653, 802, 2, 2710, 2711, 2, 802, 2711, 2713, 802, 2, 2915, 2916, 2, 739, 2918, 2919, 2, 739, 2916, 2918, 739, 2, 2923, 2924, 2, 739, 2926, 2927, 2, 739, 2924, 2926, 739, 2, 2983, 2984, 2, 739, 2986, 2987, 2, 739, 2984, 2986, 739, 2, 3003, 3004, 2, 739, 3006, 3007, 2, 739, 3004, 3006, 739, 2, 3011, 3012, 2, 739, 3014, 3015, 2, 739, 3012, 3014, 739, 2, 3019, 3020, 2, 739, 3022, 3023, 2, 739, 3020, 3022, 739, 2, 3027, 3028, 2, 739, 3028, 3030, 739, 2, 3135, 3136, 2, 710, 3138, 3139, 2, 710, 3136, 3138, 710, 2, 3143, 3144, 2, 710, 3146, 3147, 2, 710, 3144, 3146, 710, 2, 3151, 3152, 2, 710, 3154, 3155, 2, 710, 3152, 3154, 710, 2, 3159, 3160, 2, 710, 3160, 3162, 710, 2, 3175, 3176, 2, 710, 3176, 3178, 710, 2, 3192, 3194, 710, 2, 3326, 3328, 2, 686, 3328, 3330, 686, 2, 724, 730, 860, 7, 744, 750, 860, 7, 762, 763, 7, 860, 756, 762, 860, 7, 803, 809, 860, 7, 820, 826, 860, 7, 838, 839, 7, 860, 832, 838, 860, 7, 955, 961, 860, 7, 1035, 1041, 860, 7, 1047, 1053, 860, 7, 1059, 1065, 860, 7, 1065, 1066, 7, 860, 1066, 1072, 860, 7, 1133, 1139, 744, 7, 1349, 1355, 744, 7, 1367, 1368, 7, 744, 1361, 1367, 744, 7, 1480, 1481, 14, 802, 1487, 1488, 14, 802, 1481, 1487, 802, 14, 1533, 1539, 802, 14, 1689, 1695, 802, 14, 1780, 1781, 14, 802, 1781, 1787, 802, 14, 2070, 2076, 802, 14, 2114, 2120, 802, 14, 2212, 2213, 14, 802, 2206, 2212, 802, 14, 2234, 2240, 802, 14, 2258, 2264, 802, 14, 2354, 2355, 14, 802, 2355, 2361, 802, 14, 2399, 2405, 802, 14, 2423, 2429, 802, 14, 2658, 2659, 2, 802, 2659, 2665, 802, 2, 723, 724, 7, 860, 719, 723, 860, 7, 730, 731, 7, 860, 731, 735, 860, 7, 743, 744, 7, 860, 739, 743, 860, 7, 750, 751, 7, 860, 755, 756, 7, 860, 751, 755, 860, 7, 802, 803, 7, 860, 798, 802, 860, 7, 809, 810, 7, 860, 810, 814, 860, 7, 814, 815, 7, 860, 819, 820, 7, 860, 815, 819, 860, 7, 826, 827, 7, 860, 831, 832, 7, 860, 827, 831, 860, 7, 954, 955, 7, 860, 950, 954, 860, 7, 961, 962, 7, 860, 966, 967, 7, 860, 962, 966, 860, 7, 989, 990, 7, 860, 994, 995, 7, 860, 990, 994, 860, 7, 1034, 1035, 7, 860, 1030, 1034, 860, 7, 1041, 1042, 7, 860, 1046, 1047, 7, 860, 1042, 1046, 860, 7, 1053, 1054, 7, 860, 1058, 1059, 7, 860, 1054, 1058, 860, 7, 1072, 1073, 7, 860, 1077, 1078, 7, 860, 1073, 1077, 860, 7, 1127, 1128, 7, 744, 1132, 1133, 7, 744, 1128, 1132, 744, 7, 1139, 1140, 7, 744, 1144, 1145, 7, 744, 1140, 1144, 744, 7, 1243, 1244, 7, 744, 1248, 1249, 7, 744, 1244, 1248, 744, 7, 1303, 1304, 7, 744, 1308, 1309, 7, 744, 1304, 1308, 744, 7, 1348, 1349, 7, 744, 1344, 1348, 744, 7, 1355, 1356, 7, 744, 1360, 1361, 7, 744, 1356, 1360, 744, 7, 1527, 1528, 14, 802, 1532, 1533, 14, 802, 1528, 1532, 802, 14, 1539, 1540, 14, 802, 1544, 1545, 14, 802, 1540, 1544, 802, 14, 1683, 1684, 14, 802, 1688, 1689, 14, 802, 1684, 1688, 802, 14, 1695, 1696, 14, 802, 1696, 1700, 802, 14, 1787, 1788, 14, 802, 1792, 1793, 14, 802, 1788, 1792, 802, 14, 1955, 1956, 14, 802, 1960, 1961, 14, 802, 1956, 1960, 802, 14, 2076, 2077, 14, 802, 2077, 2081, 802, 14, 2108, 2109, 14, 802, 2113, 2114, 14, 802, 2109, 2113, 802, 14, 2120, 2121, 14, 802, 2125, 2126, 14, 802, 2121, 2125, 802, 14, 2200, 2201, 14, 802, 2205, 2206, 14, 802, 2201, 2205, 802, 14, 2228, 2229, 14, 802, 2233, 2234, 14, 802, 2229, 2233, 802, 14, 2240, 2241, 14, 802, 2245, 2246, 14, 802, 2241, 2245, 802, 14, 2252, 2253, 14, 802, 2257, 2258, 14, 802, 2253, 2257, 802, 14, 2264, 2265, 14, 802, 2269, 2270, 14, 802, 2265, 2269, 802, 14, 2361, 2362, 14, 802, 2362, 2366, 802, 14, 2393, 2394, 14, 802, 2398, 2399, 14, 802, 2394, 2398, 802, 14, 2405, 2406, 14, 802, 2410, 2411, 14, 802, 2406, 2410, 802, 14, 2417, 2418, 14, 802, 2422, 2423, 14, 802, 2418, 2422, 802, 14, 2429, 2430, 14, 802, 2430, 2434, 802, 14, 2443, 2447, 802, 14, 2665, 2666, 2, 802, 2666, 2670, 802, 2, 2682, 2686, 802, 2, 26, 27, 19, 860, 31, 32, 19, 860, 27, 31, 860, 19, 242, 243, 7, 860, 243, 247, 860, 7, 255, 256, 7, 860, 251, 255, 860, 7, 271, 275, 860, 7, 291, 292, 7, 860, 287, 291, 860, 7, 302, 303, 7, 860, 307, 308, 7, 860, 303, 307, 860, 7, 339, 343, 860, 7, 359, 360, 7, 860, 355, 359, 860, 7, 375, 379, 860, 7, 439, 440, 7, 860, 440, 444, 860, 7, 458, 459, 7, 860, 463, 464, 7, 860, 459, 463, 860, 7, 534, 535, 7, 860, 539, 540, 7, 860, 535, 539, 860, 7, 566, 567, 7, 860, 571, 572, 7, 860, 567, 571, 860, 7, 596, 600, 860, 7, 626, 627, 7, 860, 627, 631, 860, 7, 642, 643, 7, 860, 643, 647, 860, 7, 658, 659, 7, 860, 659, 663, 860, 7, 671, 672, 7, 860, 667, 671, 860, 7, 710, 711, 7, 860, 711, 715, 860, 7, 770, 771, 7, 860, 771, 775, 860, 7, 783, 784, 7, 860, 779, 783, 860, 7, 786, 787, 7, 860, 787, 791, 860, 7, 865, 866, 7, 860, 866, 870, 860, 7, 925, 926, 7, 860, 926, 930, 860, 7, 938, 939, 7, 860, 934, 938, 860, 7, 941, 942, 7, 860, 942, 946, 860, 7, 1375, 1376, 7, 744, 1376, 1380, 744, 7, 1388, 1389, 7, 744, 1384, 1388, 744, 7, 1419, 1420, 14, 802, 1424, 1425, 14, 802, 1420, 1424, 802, 14, 1456, 1460, 802, 14, 1711, 1712, 14, 802, 1707, 1711, 802, 14, 1719, 1720, 14, 802, 1720, 1724, 802, 14, 2012, 2013, 14, 802, 2017, 2018, 14, 802, 2013, 2017, 802, 14, 2049, 2053, 802, 14, 2069, 2070, 14, 802, 2065, 2069, 802, 14, 2085, 2089, 802, 14, 2301, 2302, 14, 802, 2306, 2307, 14, 802, 2302, 2306, 802, 14, 2333, 2334, 14, 802, 2338, 2339, 14, 802, 2334, 2338, 802, 14, 2370, 2374, 802, 14, 2442, 2443, 14, 802, 2438, 2442, 802, 14, 2455, 2456, 14, 802, 2451, 2455, 802, 14, 2637, 2638, 2, 802, 2642, 2643, 2, 802, 2638, 2642, 802, 2, 2674, 2678, 802, 2, 2694, 2695, 2, 802, 2690, 2694, 802, 2, 2713, 2714, 2, 802, 2714, 2718, 802, 2, 2773, 2774, 2, 802, 2774, 2778, 802, 2, 2786, 2787, 2, 802, 2782, 2786, 802, 2, 2789, 2790, 2, 802, 2790, 2794, 802, 2, 2794, 2795, 2, 802, 2795, 2799, 802, 2, 2827, 2828, 2, 802, 2823, 2827, 802, 2, 2838, 2839, 2, 802, 2843, 2844, 2, 802, 2839, 2843, 802, 2, 3030, 3031, 2, 739, 3031, 3035, 739, 2, 3085, 3086, 2, 739, 3086, 3090, 739, 2, 3098, 3100, 2, 739, 3094, 3098, 739, 2, 3162, 3163, 2, 710, 3163, 3167, 710, 2, 3178, 3179, 2, 710, 3179, 3183, 710, 2, 3191, 3192, 2, 710, 3187, 3191, 710, 2, 3194, 3195, 2, 710, 3195, 3199, 710, 2, 3330, 3331, 2, 686, 3331, 3335, 686, 2, 3470, 3471, 2, 824, 3475, 3476, 2, 824, 3471, 3475, 824, 2, 3500, 3504, 824, 2, 3510, 3511, 2, 824, 3511, 3515, 824, 2, 3515, 3516, 2, 824, 3516, 3520, 824, 2, 3531, 3532, 2, 824, 3536, 3537, 2, 824, 3532, 3536, 824, 2, 3568, 3572, 824, 2, 3588, 3589, 2, 824, 3584, 3588, 824, 2, 3599, 3600, 2, 824, 3604, 3605, 2, 824, 3600, 3604, 824, 2, 3631, 3632, 2, 824, 3632, 3636, 824, 2, 3686, 3687, 2, 824, 3687, 3691, 824, 2, 3695, 3699, 824, 2, 3699, 3700, 2, 824, 3700, 3704, 824, 2, 3723, 3727, 824, 2, 3746, 3768, 2, 824, 3742, 3746, 824, 2, 3822, 3823, 2, 838, 3827, 3828, 2, 838, 3823, 3827, 838, 2, 0, 1, 19, 860, 1, 3, 860, 19, 3, 4, 19, 860, 4, 6, 860, 19, 6, 7, 19, 860, 9, 10, 19, 860, 7, 9, 860, 19, 59, 60, 7, 860, 62, 63, 7, 860, 60, 62, 860, 7, 67, 68, 7, 860, 70, 71, 7, 860, 68, 70, 860, 7, 111, 112, 7, 860, 114, 115, 7, 860, 112, 114, 860, 7, 215, 216, 7, 860, 218, 219, 7, 860, 216, 218, 860, 7, 247, 248, 7, 860, 250, 251, 7, 860, 248, 250, 860, 7, 267, 268, 7, 860, 270, 271, 7, 860, 268, 270, 860, 7, 275, 276, 7, 860, 278, 279, 7, 860, 276, 278, 860, 7, 283, 284, 7, 860, 286, 287, 7, 860, 284, 286, 860, 7, 335, 336, 7, 860, 338, 339, 7, 860, 336, 338, 860, 7, 343, 344, 7, 860, 346, 347, 7, 860, 344, 346, 860, 7, 351, 352, 7, 860, 354, 355, 7, 860, 352, 354, 860, 7, 371, 372, 7, 860, 374, 375, 7, 860, 372, 374, 860, 7, 379, 380, 7, 860, 382, 383, 7, 860, 380, 382, 860, 7, 444, 445, 7, 860, 447, 448, 7, 860, 445, 447, 860, 7, 592, 593, 7, 860, 595, 596, 7, 860, 593, 595, 860, 7, 600, 601, 7, 860, 603, 604, 7, 860, 601, 603, 860, 7, 631, 632, 7, 860, 634, 635, 7, 860, 632, 634, 860, 7, 647, 648, 7, 860, 650, 651, 7, 860, 648, 650, 860, 7, 663, 664, 7, 860, 666, 667, 7, 860, 664, 666, 860, 7, 715, 716, 7, 860, 718, 719, 7, 860, 716, 718, 860, 7, 735, 736, 7, 860, 738, 739, 7, 860, 736, 738, 860, 7, 775, 776, 7, 860, 778, 779, 7, 860, 776, 778, 860, 7, 791, 792, 7, 860, 792, 794, 860, 7, 794, 795, 7, 860, 797, 798, 7, 860, 795, 797, 860, 7, 870, 871, 7, 860, 873, 874, 7, 860, 871, 873, 860, 7, 890, 891, 7, 860, 893, 894, 7, 860, 891, 893, 860, 7, 930, 931, 7, 860, 933, 934, 7, 860, 931, 933, 860, 7, 946, 947, 7, 860, 949, 950, 7, 860, 947, 949, 860, 7, 1026, 1027, 7, 860, 1029, 1030, 7, 860, 1027, 1029, 860, 7, 1100, 1101, 7, 744, 1103, 1104, 7, 744, 1101, 1103, 744, 7, 1340, 1341, 7, 744, 1343, 1344, 7, 744, 1341, 1343, 744, 7, 1380, 1381, 7, 744, 1383, 1384, 7, 744, 1381, 1383, 744, 7, 1452, 1453, 14, 802, 1455, 1456, 14, 802, 1453, 1455, 802, 14, 1460, 1461, 14, 802, 1463, 1464, 14, 802, 1461, 1463, 802, 14, 1700, 1701, 14, 802, 1701, 1703, 802, 14, 1703, 1704, 14, 802, 1706, 1707, 14, 802, 1704, 1706, 802, 14, 1724, 1725, 14, 802, 1727, 1728, 14, 802, 1725, 1727, 802, 14, 2045, 2046, 14, 802, 2048, 2049, 14, 802, 2046, 2048, 802, 14, 2053, 2054, 14, 802, 2056, 2057, 14, 802, 2054, 2056, 802, 14, 2061, 2062, 14, 802, 2064, 2065, 14, 802, 2062, 2064, 802, 14, 2081, 2082, 14, 802, 2084, 2085, 14, 802, 2082, 2084, 802, 14, 2089, 2090, 14, 802, 2092, 2093, 14, 802, 2090, 2092, 802, 14, 2366, 2367, 14, 802, 2369, 2370, 14, 802, 2367, 2369, 802, 14, 2374, 2375, 14, 802, 2377, 2378, 14, 802, 2375, 2377, 802, 14, 2434, 2435, 14, 802, 2437, 2438, 14, 802, 2435, 2437, 802, 14, 2447, 2448, 14, 802, 2450, 2451, 14, 802, 2448, 2450, 802, 14, 2670, 2671, 2, 802, 2673, 2674, 2, 802, 2671, 2673, 802, 2, 2678, 2679, 2, 802, 2681, 2682, 2, 802, 2679, 2681, 802, 2, 2686, 2687, 2, 802, 2689, 2690, 2, 802, 2687, 2689, 802, 2, 2718, 2719, 2, 802, 2721, 2722, 2, 802, 2719, 2721, 802, 2, 2738, 2739, 2, 802, 2741, 2742, 2, 802, 2739, 2741, 802, 2, 2778, 2779, 2, 802, 2781, 2782, 2, 802, 2779, 2781, 802, 2, 2799, 2800, 2, 802, 2802, 2803, 2, 802, 2800, 2802, 802, 2, 2819, 2820, 2, 802, 2822, 2823, 2, 802, 2820, 2822, 802, 2, 3035, 3036, 2, 739, 3038, 3039, 2, 739, 3036, 3038, 739, 2, 3055, 3056, 2, 739, 3058, 3059, 2, 739, 3056, 3058, 739, 2, 3090, 3091, 2, 739, 3093, 3094, 2, 739, 3091, 3093, 739, 2, 3167, 3168, 2, 710, 3170, 3171, 2, 710, 3168, 3170, 710, 2, 3183, 3184, 2, 710, 3186, 3187, 2, 710, 3184, 3186, 710, 2, 3199, 3200, 2, 710, 3202, 3203, 2, 710, 3200, 3202, 710, 2, 3335, 3336, 2, 686, 3338, 3339, 2, 686, 3336, 3338, 686, 2, 3496, 3497, 2, 824, 3499, 3500, 2, 824, 3497, 3499, 824, 2, 3504, 3505, 2, 824, 3507, 3508, 2, 824, 3505, 3507, 824, 2, 3520, 3521, 2, 824, 3523, 3524, 2, 824, 3521, 3523, 824, 2, 3564, 3565, 2, 824, 3567, 3568, 2, 824, 3565, 3567, 824, 2, 3572, 3573, 2, 824, 3575, 3576, 2, 824, 3573, 3575, 824, 2, 3580, 3581, 2, 824, 3583, 3584, 2, 824, 3581, 3583, 824, 2, 3636, 3637, 2, 824, 3639, 3640, 2, 824, 3637, 3639, 824, 2, 3656, 3657, 2, 824, 3659, 3660, 2, 824, 3657, 3659, 824, 2, 3691, 3692, 2, 824, 3694, 3695, 2, 824, 3692, 3694, 824, 2, 3704, 3705, 2, 824, 3707, 3708, 2, 824, 3705, 3707, 824, 2, 3719, 3720, 2, 824, 3722, 3723, 2, 824, 3720, 3722, 824, 2, 3727, 3728, 2, 824, 3730, 3731, 2, 824, 3728, 3730, 824, 2, 3735, 3736, 2, 824, 3736, 3738, 824, 2, 3738, 3739, 2, 824, 3741, 3742, 2, 824, 3739, 3741, 824, 2, 8, 11, 30, 96, 5, 11, 98, 161, 11, 12, 96, 98, 11, 13, 161, 30, 28, 30, 161, 30, 29, 30, 33, 86, 30, 33, 30, 33, 69, 72, 413, 539, 72, 73, 539, 541, 72, 74, 685, 413, 2, 96, 227, 393, 96, 97, 393, 413, 96, 98, 685, 227, 113, 116, 168, 225, 116, 117, 225, 227, 116, 118, 685, 168, 30, 140, 86, 161, 140, 141, 161, 168, 140, 142, 685, 86, 217, 220, 44, 85, 220, 221, 85, 86, 220, 222, 685, 44, 239, 241, 685, 44, 240, 241, 391, 506, 241, 244, 44, 391, 244, 246, 391, 44, 245, 246, 388, 390, 246, 249, 390, 391, 241, 252, 506, 685, 252, 254, 685, 506, 253, 254, 602, 680, 264, 266, 602, 506, 265, 266, 582, 601, 266, 269, 601, 602, 266, 272, 506, 582, 272, 274, 582, 506, 273, 274, 579, 581, 274, 277, 581, 582, 274, 280, 506, 579, 280, 282, 579, 506, 281, 282, 526, 538, 285, 288, 536, 537, 282, 288, 538, 579, 288, 289, 537, 538, 288, 290, 579, 536, 282, 293, 506, 526, 246, 304, 44, 388, 304, 306, 388, 44, 305, 306, 355, 386, 306, 309, 386, 388, 332, 334, 355, 44, 333, 334, 337, 354, 334, 337, 354, 355, 334, 340, 44, 337, 340, 342, 337, 44, 341, 342, 334, 336, 342, 345, 336, 337, 342, 348, 44, 334, 348, 350, 334, 44, 349, 350, 167, 224, 353, 356, 222, 223, 350, 356, 224, 334, 356, 357, 223, 224, 356, 358, 334, 222, 368, 370, 167, 44, 369, 370, 159, 166, 370, 373, 166, 167, 370, 376, 44, 159, 376, 378, 159, 44, 377, 378, 156, 158, 378, 381, 158, 159, 254, 441, 680, 685, 441, 443, 685, 680, 442, 443, 683, 684, 443, 446, 684, 685, 443, 449, 680, 683, 290, 460, 536, 579, 460, 462, 579, 536, 461, 462, 546, 577, 462, 465, 577, 579, 462, 481, 536, 546, 358, 536, 222, 334, 536, 538, 334, 222, 537, 538, 246, 332, 538, 541, 332, 334, 538, 557, 222, 246, 568, 570, 156, 44, 569, 570, 111, 154, 570, 573, 154, 156, 570, 589, 44, 111, 589, 591, 111, 44, 590, 591, 104, 110, 591, 594, 110, 111, 591, 597, 44, 104, 597, 599, 104, 44, 598, 599, 102, 103, 599, 602, 103, 104, 625, 628, 284, 331, 628, 630, 331, 284, 629, 630, 329, 330, 630, 633, 330, 331, 641, 644, 545, 576, 644, 646, 576, 545, 645, 646, 574, 575, 646, 649, 575, 576, 657, 660, 534, 544, 646, 660, 545, 574, 660, 661, 544, 545, 660, 662, 574, 534, 665, 668, 531, 533, 662, 668, 534, 574, 668, 669, 533, 534, 668, 670, 574, 531, 709, 712, 350, 380, 712, 714, 380, 350, 713, 714, 378, 379, 714, 717, 379, 380, 630, 720, 284, 329, 714, 720, 350, 378, 720, 721, 329, 350, 720, 722, 378, 284, 737, 740, 245, 282, 740, 741, 282, 284, 740, 742, 378, 245, 769, 772, 220, 244, 772, 773, 244, 245, 772, 774, 378, 220, 777, 780, 217, 219, 774, 780, 220, 378, 780, 781, 219, 220, 780, 782, 378, 217, 785, 788, 140, 153, 788, 790, 153, 140, 789, 790, 151, 152, 790, 793, 152, 153, 790, 799, 140, 151, 796, 799, 162, 182, 799, 800, 151, 162, 799, 801, 182, 140, 599, 816, 44, 102, 816, 817, 102, 140, 816, 818, 182, 44, 864, 867, 597, 650, 867, 869, 650, 597, 868, 869, 648, 649, 869, 872, 649, 650, 670, 875, 531, 574, 869, 875, 597, 648, 875, 876, 574, 597, 875, 877, 648, 531, 892, 895, 522, 529, 895, 896, 529, 531, 895, 897, 648, 522, 924, 927, 499, 521, 927, 928, 521, 522, 927, 929, 648, 499, 932, 935, 496, 498, 929, 935, 499, 648, 935, 936, 498, 499, 935, 937, 648, 496, 940, 943, 406, 457, 943, 945, 457, 406, 944, 945, 455, 456, 945, 948, 456, 457, 782, 951, 217, 378, 945, 951, 406, 455, 951, 952, 378, 406, 951, 953, 455, 217, 1028, 1031, 189, 215, 1031, 1032, 215, 217, 1031, 1033, 455, 189, 1055, 1056, 182, 189, 1055, 1057, 455, 44, 1102, 1105, 471, 494, 1105, 1106, 494, 496, 1105, 1107, 648, 471, 1129, 1130, 455, 471, 1129, 1131, 648, 44, 1342, 1345, 32, 42, 1345, 1346, 42, 44, 1345, 1347, 648, 32, 1374, 1377, 28, 31, 1377, 1378, 31, 32, 1377, 1379, 648, 28, 1382, 1385, 25, 27, 1379, 1385, 28, 648, 1385, 1386, 27, 28, 1385, 1387, 648, 25, 1387, 1421, 25, 648, 1421, 1423, 648, 25, 1422, 1423, 596, 646, 1423, 1426, 646, 648, 1449, 1451, 596, 25, 1450, 1451, 572, 595, 1451, 1454, 595, 596, 1451, 1457, 25, 572, 1457, 1459, 572, 25, 1458, 1459, 569, 571, 1459, 1462, 571, 572, 1697, 1699, 569, 25, 1698, 1699, 39, 41, 1699, 1702, 25, 39, 1705, 1708, 38, 40, 1699, 1708, 41, 569, 1708, 1709, 40, 41, 1708, 1710, 569, 38, 1718, 1721, 594, 645, 1721, 1723, 645, 594, 1722, 1723, 643, 644, 1723, 1726, 644, 645, 1710, 1729, 38, 569, 1723, 1729, 594, 643, 1729, 1730, 569, 594, 1729, 1731, 643, 38, 2014, 2016, 643, 38, 2015, 2016, 593, 641, 2016, 2019, 641, 643, 2042, 2044, 593, 38, 2043, 2044, 567, 592, 2044, 2047, 592, 593, 2044, 2050, 38, 567, 2050, 2052, 567, 38, 2051, 2052, 564, 566, 2052, 2055, 566, 567, 2052, 2058, 38, 564, 2058, 2060, 564, 38, 2059, 2060, 467, 488, 2063, 2066, 486, 487, 2060, 2066, 488, 564, 2066, 2067, 487, 488, 2066, 2068, 564, 486, 2078, 2080, 467, 38, 2079, 2080, 448, 466, 2080, 2083, 466, 467, 2080, 2086, 38, 448, 2086, 2088, 448, 38, 2087, 2088, 445, 447, 2088, 2091, 447, 448, 2068, 2303, 486, 564, 2303, 2305, 564, 486, 2304, 2305, 514, 562, 2305, 2308, 562, 564, 2305, 2324, 486, 514, 2335, 2337, 445, 38, 2336, 2337, 399, 443, 2337, 2340, 443, 445, 2363, 2365, 399, 38, 2364, 2365, 366, 398, 2365, 2368, 398, 399, 2365, 2371, 38, 366, 2371, 2373, 366, 38, 2372, 2373, 363, 365, 2373, 2376, 365, 366, 2431, 2433, 363, 38, 2432, 2433, 117, 204, 2436, 2439, 202, 203, 2433, 2439, 204, 363, 2439, 2440, 203, 204, 2439, 2441, 363, 202, 2433, 2444, 38, 117, 2444, 2446, 117, 38, 2445, 2446, 115, 116, 2446, 2449, 116, 117, 2446, 2452, 38, 115, 2452, 2454, 115, 38, 2453, 2454, 47, 57, 2454, 2457, 38, 47, 2441, 2639, 202, 363, 2639, 2641, 363, 202, 2640, 2641, 340, 361, 2641, 2644, 361, 363, 2667, 2669, 340, 202, 2668, 2669, 312, 339, 2669, 2672, 339, 340, 2669, 2675, 202, 312, 2675, 2677, 312, 202, 2676, 2677, 309, 311, 2677, 2680, 311, 312, 2677, 2683, 202, 309, 2683, 2685, 309, 202, 2684, 2685, 234, 266, 2688, 2691, 264, 265, 2685, 2691, 266, 309, 2691, 2692, 265, 266, 2691, 2693, 309, 264, 2685, 2696, 202, 234, 2712, 2715, 338, 360, 2715, 2717, 360, 338, 2716, 2717, 358, 359, 2717, 2720, 359, 360, 2693, 2723, 264, 309, 2717, 2723, 338, 358, 2723, 2724, 309, 338, 2723, 2725, 358, 264, 2740, 2743, 233, 262, 2743, 2744, 262, 264, 2743, 2745, 358, 233, 2772, 2775, 200, 232, 2775, 2776, 232, 233, 2775, 2777, 358, 200, 2780, 2783, 197, 199, 2777, 2783, 200, 358, 2783, 2784, 199, 200, 2783, 2785, 358, 197, 2454, 2791, 57, 115, 2788, 2791, 122, 124, 2791, 2792, 115, 122, 2791, 2793, 124, 57, 2793, 2796, 57, 124, 2796, 2798, 124, 57, 2797, 2798, 121, 123, 2798, 2801, 123, 124, 2816, 2818, 358, 197, 2817, 2818, 231, 261, 2821, 2824, 259, 260, 2818, 2824, 261, 358, 2824, 2825, 260, 261, 2824, 2826, 358, 259, 2818, 2829, 197, 231, 2798, 2840, 57, 121, 2840, 2842, 121, 57, 2841, 2842, 81, 119, 2842, 2845, 119, 121, 3029, 3032, 394, 427, 3032, 3034, 427, 394, 3033, 3034, 425, 426, 3034, 3037, 426, 427, 2826, 3040, 259, 358, 3034, 3040, 394, 425, 3040, 3041, 358, 394, 3040, 3042, 425, 259, 3057, 3060, 230, 257, 3060, 3061, 257, 259, 3060, 3062, 425, 230, 3084, 3087, 195, 229, 3087, 3088, 229, 230, 3087, 3089, 425, 195, 3092, 3095, 193, 194, 3089, 3095, 195, 425, 3095, 3096, 194, 195, 3095, 3097, 425, 193, 3161, 3164, 510, 556, 3164, 3166, 556, 510, 3165, 3166, 554, 555, 3166, 3169, 555, 556, 3177, 3180, 479, 509, 3166, 3180, 510, 554, 3180, 3181, 509, 510, 3180, 3182, 554, 479, 3185, 3188, 476, 478, 3182, 3188, 479, 554, 3188, 3189, 478, 479, 3188, 3190, 554, 476, 3193, 3196, 433, 437, 3196, 3198, 437, 433, 3197, 3198, 435, 436, 3198, 3201, 436, 437, 3097, 3204, 193, 425, 3198, 3204, 433, 435, 3204, 3205, 425, 433, 3204, 3206, 435, 193, 3329, 3332, 585, 630, 3332, 3334, 630, 585, 3333, 3334, 628, 629, 3334, 3337, 629, 630, 3190, 3340, 476, 554, 3334, 3340, 585, 628, 3340, 3341, 554, 585, 3340, 3342, 628, 476, 3357, 3358, 435, 476, 3357, 3359, 628, 193, 3472, 3474, 628, 193, 3473, 3474, 584, 626, 3474, 3477, 626, 628, 3474, 3493, 193, 584, 3493, 3495, 584, 193, 3494, 3495, 552, 583, 3495, 3498, 583, 584, 3495, 3501, 193, 552, 3501, 3503, 552, 193, 3502, 3503, 550, 551, 3503, 3506, 551, 552, 3503, 3512, 193, 550, 3509, 3512, 623, 625, 3512, 3513, 550, 623, 3512, 3514, 625, 193, 3514, 3517, 193, 625, 3517, 3519, 625, 193, 3518, 3519, 622, 624, 3519, 3522, 624, 625, 3519, 3533, 193, 622, 3533, 3535, 622, 193, 3534, 3535, 432, 620, 3535, 3538, 620, 622, 3561, 3563, 432, 193, 3562, 3563, 422, 431, 3563, 3566, 431, 432, 3563, 3569, 193, 422, 3569, 3571, 422, 193, 3570, 3571, 419, 421, 3571, 3574, 421, 422, 3571, 3577, 193, 419, 3577, 3579, 419, 193, 3578, 3579, 228, 256, 3582, 3585, 254, 255, 3579, 3585, 256, 419, 3585, 3586, 255, 256, 3585, 3587, 419, 254, 3579, 3590, 193, 228, 2842, 3601, 57, 81, 3601, 3603, 81, 57, 3602, 3603, 69, 79, 3603, 3606, 79, 81, 3630, 3633, 74, 78, 3633, 3635, 78, 74, 3634, 3635, 76, 77, 3635, 3638, 77, 78, 3603, 3641, 57, 69, 3635, 3641, 74, 76, 3641, 3642, 69, 74, 3641, 3643, 76, 57, 3658, 3661, 46, 55, 3661, 3662, 55, 57, 3661, 3663, 76, 46, 3685, 3688, 36, 45, 3688, 3689, 45, 46, 3688, 3690, 76, 36, 3693, 3696, 34, 35, 3690, 3696, 36, 76, 3696, 3697, 35, 36, 3696, 3698, 76, 34, 3698, 3701, 34, 76, 3701, 3703, 76, 34, 3702, 3703, 73, 75, 3703, 3706, 75, 76, 3716, 3718, 73, 34, 3717, 3718, 67, 72, 3718, 3721, 72, 73, 3718, 3724, 34, 67, 3724, 3726, 67, 34, 3725, 3726, 64, 66, 3726, 3729, 66, 67, 3726, 3732, 34, 64, 3732, 3734, 64, 34, 3733, 3734, 52, 54, 3734, 3737, 34, 52, 3740, 3743, 51, 53, 3734, 3743, 54, 64, 3743, 3744, 53, 54, 3743, 3745, 64, 51, 3587, 3824, 254, 419, 3824, 3826, 419, 254, 3825, 3826, 287, 417, 3826, 3829, 417, 419, 3826, 3845, 254, 287, 3745, 3856, 51, 64, 3643, 3646, 57, 76, 3646, 3650, 76, 57, 3663, 3666, 46, 76, 3666, 3670, 76, 46, 3682, 3688, 46, 76, 3678, 3682, 76, 46, 3703, 3709, 34, 73, 3713, 3716, 34, 73, 3709, 3713, 73, 34, 3650, 3653, 57, 76, 3655, 3661, 57, 76, 3653, 3655, 76, 57, 3670, 3673, 46, 76, 3675, 3678, 46, 76, 3673, 3675, 76, 46, 164, 170, 685, 86, 192, 198, 685, 86, 214, 220, 86, 685, 208, 214, 685, 86, 378, 384, 44, 156, 384, 390, 156, 44, 161, 164, 86, 685, 157, 161, 685, 86, 170, 173, 86, 685, 173, 177, 685, 86, 189, 192, 86, 685, 185, 189, 685, 86, 198, 201, 86, 685, 205, 208, 86, 685, 201, 205, 685, 86, 390, 393, 44, 156, 393, 397, 156, 44, 417, 421, 156, 44, 1941, 1947, 643, 38, 1969, 1975, 643, 38, 1991, 2014, 38, 643, 1985, 1991, 643, 38, 2214, 2220, 445, 38, 1938, 1941, 38, 643, 1934, 1938, 643, 38, 1947, 1950, 38, 643, 1950, 1954, 643, 38, 1966, 1969, 38, 643, 1962, 1966, 643, 38, 1975, 1978, 38, 643, 1982, 1985, 38, 643, 1978, 1982, 643, 38, 2220, 2223, 38, 445, 2223, 2227, 445, 38, 2247, 2251, 445, 38, 1621, 1627, 569, 25, 1653, 1659, 569, 25, 1669, 1675, 569, 25, 1893, 1899, 643, 38, 1618, 1621, 25, 569, 1614, 1618, 569, 25, 1627, 1630, 25, 569, 1630, 1634, 569, 25, 1650, 1653, 25, 569, 1646, 1650, 569, 25, 1659, 1662, 25, 569, 1666, 1669, 25, 569, 1662, 1666, 569, 25, 1899, 1902, 38, 643, 1902, 1906, 643, 38, 98, 101, 227, 685, 101, 105, 685, 227, 118, 121, 168, 685, 121, 125, 685, 168, 137, 140, 168, 685, 133, 137, 685, 168, 236, 239, 44, 685, 232, 236, 685, 44, 306, 325, 44, 355, 329, 332, 44, 355, 325, 329, 355, 44, 105, 108, 227, 685, 110, 116, 227, 685, 108, 110, 685, 227, 125, 128, 168, 685, 130, 133, 168, 685, 128, 130, 685, 168, 3042, 3045, 259, 425, 3045, 3049, 425, 259, 3062, 3065, 230, 425, 3065, 3069, 425, 230, 3081, 3087, 230, 425, 3077, 3081, 425, 230, 3206, 3209, 193, 435, 3209, 3213, 435, 193, 3213, 3216, 193, 435, 3216, 3220, 435, 193, 3535, 3554, 193, 432, 3558, 3561, 193, 432, 3554, 3558, 432, 193, 3049, 3052, 259, 425, 3054, 3060, 259, 425, 3052, 3054, 425, 259, 3069, 3072, 230, 425, 3074, 3077, 230, 425, 3072, 3074, 425, 230, 3220, 3223, 193, 435, 3225, 3357, 193, 435, 3223, 3225, 435, 193, 2725, 2728, 264, 358, 2728, 2732, 358, 264, 2745, 2748, 233, 358, 2748, 2752, 358, 233, 2764, 2775, 233, 358, 2760, 2764, 358, 233, 2785, 2804, 197, 358, 2804, 2808, 358, 197, 2732, 2735, 264, 358, 2737, 2743, 264, 358, 2735, 2737, 358, 264, 2752, 2755, 233, 358, 2757, 2760, 233, 358, 2755, 2757, 358, 233, 2808, 2811, 197, 358, 2813, 2816, 197, 358, 2811, 2813, 358, 197, 1826, 1834, 643, 38, 1862, 1870, 643, 38, 1890, 1893, 38, 643, 1882, 1890, 643, 38, 2127, 2135, 445, 38, 1823, 1826, 38, 643, 1817, 1823, 643, 38, 1834, 1837, 38, 643, 1837, 1843, 643, 38, 1859, 1862, 38, 643, 1853, 1859, 643, 38, 1870, 1873, 38, 643, 1879, 1882, 38, 643, 1873, 1879, 643, 38, 2135, 2138, 38, 445, 2138, 2144, 445, 38, 2170, 2176, 445, 38, 1470, 1474, 569, 25, 1494, 1498, 569, 25, 1506, 1510, 569, 25, 1746, 1750, 643, 38, 1459, 1465, 25, 569, 1467, 1470, 25, 569, 1465, 1467, 569, 25, 1474, 1477, 25, 569, 1477, 1479, 569, 25, 1491, 1494, 25, 569, 1489, 1491, 569, 25, 1498, 1501, 25, 569, 1503, 1506, 25, 569, 1501, 1503, 569, 25, 1750, 1753, 38, 643, 1753, 1755, 643, 38, 1777, 1779, 643, 38, 1731, 1734, 38, 643, 1734, 1738, 643, 38, 1755, 1758, 38, 643, 1758, 1762, 643, 38, 1774, 1777, 38, 643, 1770, 1774, 643, 38, 2016, 2035, 38, 593, 2039, 2042, 38, 593, 2035, 2039, 593, 38, 1738, 1741, 38, 643, 1743, 1746, 38, 643, 1741, 1743, 643, 38, 1762, 1765, 38, 643, 1767, 1770, 38, 643, 1765, 1767, 643, 38, 74, 77, 413, 685, 77, 81, 685, 413, 93, 96, 413, 685, 89, 93, 685, 413, 254, 257, 506, 602, 261, 264, 506, 602, 257, 261, 602, 506, 61, 64, 541, 685, 66, 72, 541, 685, 64, 66, 685, 541, 81, 84, 413, 685, 86, 89, 413, 685, 84, 86, 685, 413, 25, 28, 30, 161, 21, 25, 161, 30, 142, 145, 86, 685, 145, 149, 685, 86, 222, 225, 44, 685, 229, 232, 44, 685, 225, 229, 685, 44, 350, 361, 44, 167, 365, 368, 44, 167, 361, 365, 167, 44, 405, 409, 156, 44, 438, 568, 44, 156, 434, 438, 156, 44, 13, 16, 30, 161, 18, 21, 30, 161, 16, 18, 161, 30, 149, 152, 86, 685, 154, 157, 86, 685, 152, 154, 685, 86, 177, 180, 86, 685, 182, 185, 86, 685, 180, 182, 685, 86, 397, 400, 44, 156, 402, 405, 44, 156, 400, 402, 156, 44, 409, 412, 44, 156, 414, 417, 44, 156, 412, 414, 156, 44, 421, 424, 44, 156, 424, 426, 156, 44, 426, 429, 44, 156, 431, 434, 44, 156, 429, 431, 156, 44, 1289, 1295, 648, 44, 1317, 1323, 648, 44, 1339, 1345, 44, 648, 1333, 1339, 648, 44, 1634, 1637, 25, 569, 1643, 1646, 25, 569, 1637, 1643, 569, 25, 1286, 1289, 44, 648, 1282, 1286, 648, 44, 1295, 1298, 44, 648, 1298, 1302, 648, 44, 1314, 1317, 44, 648, 1310, 1314, 648, 44, 1323, 1326, 44, 648, 1330, 1333, 44, 648, 1326, 1330, 648, 44, 1675, 1678, 25, 569, 1678, 1682, 569, 25, 1178, 1186, 648, 44, 1214, 1222, 648, 44, 1234, 1242, 648, 44, 1546, 1554, 569, 25, 1175, 1178, 44, 648, 1169, 1175, 648, 44, 1186, 1189, 44, 648, 1189, 1195, 648, 44, 1211, 1214, 44, 648, 1205, 1211, 648, 44, 1222, 1225, 44, 648, 1231, 1234, 44, 648, 1225, 1231, 648, 44, 1554, 1557, 25, 569, 1557, 1563, 569, 25, 1589, 1595, 569, 25, 3342, 3345, 476, 628, 3345, 3349, 628, 476, 3359, 3362, 193, 628, 3362, 3366, 628, 193, 3378, 3472, 193, 628, 3374, 3378, 628, 193, 3349, 3352, 476, 628, 3354, 3357, 476, 628, 3352, 3354, 628, 476, 3366, 3369, 193, 628, 3371, 3374, 193, 628, 3369, 3371, 628, 193, 877, 880, 531, 648, 880, 884, 648, 531, 897, 900, 522, 648, 900, 904, 648, 522, 916, 927, 522, 648, 912, 916, 648, 522, 1099, 1105, 496, 648, 1095, 1099, 648, 496, 1107, 1110, 471, 648, 1110, 1114, 648, 471, 1126, 1129, 471, 648, 1122, 1126, 648, 471, 1423, 1442, 25, 596, 1446, 1449, 25, 596, 1442, 1446, 596, 25, 884, 887, 531, 648, 889, 895, 531, 648, 887, 889, 648, 531, 904, 907, 522, 648, 909, 912, 522, 648, 907, 909, 648, 522, 937, 1090, 496, 648, 1092, 1095, 496, 648, 1090, 1092, 648, 496, 1114, 1117, 471, 648, 1119, 1122, 471, 648, 1117, 1119, 648, 471, 975, 981, 455, 217, 1003, 1009, 455, 217, 1025, 1031, 217, 455, 1019, 1025, 455, 217, 1153, 1159, 648, 44, 1257, 1263, 648, 44, 1279, 1282, 44, 648, 1273, 1279, 648, 44, 1510, 1513, 25, 569, 1513, 1519, 569, 25, 1573, 1579, 569, 25, 1611, 1614, 25, 569, 1605, 1611, 569, 25, 1801, 1807, 643, 38, 1906, 1909, 38, 643, 1909, 1915, 643, 38, 1931, 1934, 38, 643, 1925, 1931, 643, 38, 2088, 2094, 38, 445, 2094, 2100, 445, 38, 2154, 2160, 445, 38, 2186, 2192, 445, 38, 2373, 2379, 38, 363, 2379, 2385, 363, 38, 972, 975, 217, 455, 968, 972, 455, 217, 981, 984, 217, 455, 984, 988, 455, 217, 1000, 1003, 217, 455, 996, 1000, 455, 217, 1009, 1012, 217, 455, 1016, 1019, 217, 455, 1012, 1016, 455, 217, 1150, 1153, 44, 648, 1146, 1150, 648, 44, 1159, 1162, 44, 648, 1166, 1169, 44, 648, 1162, 1166, 648, 44, 1195, 1198, 44, 648, 1202, 1205, 44, 648, 1198, 1202, 648, 44, 1254, 1257, 44, 648, 1250, 1254, 648, 44, 1263, 1266, 44, 648, 1270, 1273, 44, 648, 1266, 1270, 648, 44, 1519, 1522, 25, 569, 1522, 1526, 569, 25, 1563, 1566, 25, 569, 1570, 1573, 25, 569, 1566, 1570, 569, 25, 1579, 1582, 25, 569, 1586, 1589, 25, 569, 1582, 1586, 569, 25, 1595, 1598, 25, 569, 1602, 1605, 25, 569, 1598, 1602, 569, 25, 1798, 1801, 38, 643, 1794, 1798, 643, 38, 1807, 1810, 38, 643, 1814, 1817, 38, 643, 1810, 1814, 643, 38, 1843, 1846, 38, 643, 1850, 1853, 38, 643, 1846, 1850, 643, 38, 1915, 1918, 38, 643, 1922, 1925, 38, 643, 1918, 1922, 643, 38, 2100, 2103, 38, 445, 2103, 2107, 445, 38, 2144, 2147, 38, 445, 2151, 2154, 38, 445, 2147, 2151, 445, 38, 2160, 2163, 38, 445, 2167, 2170, 38, 445, 2163, 2167, 445, 38, 2176, 2179, 38, 445, 2183, 2186, 38, 445, 2179, 2183, 445, 38, 2192, 2195, 38, 445, 2195, 2199, 445, 38, 2385, 2388, 38, 363, 2388, 2392, 363, 38, 2412, 2416, 363, 38, 722, 725, 284, 378, 725, 729, 378, 284, 742, 745, 245, 378, 745, 749, 378, 245, 761, 772, 245, 378, 757, 761, 378, 245, 801, 804, 140, 182, 804, 808, 182, 140, 818, 821, 44, 182, 821, 825, 182, 44, 837, 1055, 44, 182, 833, 837, 182, 44, 953, 956, 217, 455, 956, 960, 455, 217, 1033, 1036, 189, 455, 1036, 1040, 455, 189, 1052, 1055, 189, 455, 1048, 1052, 455, 189, 1057, 1060, 44, 455, 1060, 1064, 455, 44, 1064, 1067, 44, 455, 1067, 1071, 455, 44, 1131, 1134, 44, 648, 1134, 1138, 648, 44, 1347, 1350, 32, 648, 1350, 1354, 648, 32, 1366, 1377, 32, 648, 1362, 1366, 648, 32, 1479, 1482, 25, 569, 1486, 1489, 25, 569, 1482, 1486, 569, 25, 1534, 1538, 569, 25, 1694, 1697, 25, 569, 1690, 1694, 569, 25, 1779, 1782, 38, 643, 1782, 1786, 643, 38, 2060, 2071, 38, 467, 2075, 2078, 38, 467, 2071, 2075, 467, 38, 2115, 2119, 445, 38, 2211, 2214, 38, 445, 2207, 2211, 445, 38, 2235, 2239, 445, 38, 2259, 2263, 445, 38, 2337, 2356, 38, 399, 2360, 2363, 38, 399, 2356, 2360, 399, 38, 2400, 2404, 363, 38, 2428, 2431, 38, 363, 2424, 2428, 363, 38, 2641, 2660, 202, 340, 2664, 2667, 202, 340, 2660, 2664, 340, 202, 729, 732, 284, 378, 734, 740, 284, 378, 732, 734, 378, 284, 749, 752, 245, 378, 754, 757, 245, 378, 752, 754, 378, 245, 808, 811, 140, 182, 813, 816, 140, 182, 811, 813, 182, 140, 825, 828, 44, 182, 830, 833, 44, 182, 828, 830, 182, 44, 960, 963, 217, 455, 965, 968, 217, 455, 963, 965, 455, 217, 988, 991, 217, 455, 993, 996, 217, 455, 991, 993, 455, 217, 1040, 1043, 189, 455, 1045, 1048, 189, 455, 1043, 1045, 455, 189, 1071, 1074, 44, 455, 1076, 1129, 44, 455, 1074, 1076, 455, 44, 1138, 1141, 44, 648, 1143, 1146, 44, 648, 1141, 1143, 648, 44, 1242, 1245, 44, 648, 1247, 1250, 44, 648, 1245, 1247, 648, 44, 1302, 1305, 44, 648, 1307, 1310, 44, 648, 1305, 1307, 648, 44, 1354, 1357, 32, 648, 1359, 1362, 32, 648, 1357, 1359, 648, 32, 1526, 1529, 25, 569, 1531, 1534, 25, 569, 1529, 1531, 569, 25, 1538, 1541, 25, 569, 1543, 1546, 25, 569, 1541, 1543, 569, 25, 1682, 1685, 25, 569, 1687, 1690, 25, 569, 1685, 1687, 569, 25, 1786, 1789, 38, 643, 1791, 1794, 38, 643, 1789, 1791, 643, 38, 1954, 1957, 38, 643, 1959, 1962, 38, 643, 1957, 1959, 643, 38, 2107, 2110, 38, 445, 2112, 2115, 38, 445, 2110, 2112, 445, 38, 2119, 2122, 38, 445, 2124, 2127, 38, 445, 2122, 2124, 445, 38, 2199, 2202, 38, 445, 2204, 2207, 38, 445, 2202, 2204, 445, 38, 2227, 2230, 38, 445, 2232, 2235, 38, 445, 2230, 2232, 445, 38, 2239, 2242, 38, 445, 2244, 2247, 38, 445, 2242, 2244, 445, 38, 2251, 2254, 38, 445, 2256, 2259, 38, 445, 2254, 2256, 445, 38, 2263, 2266, 38, 445, 2268, 2335, 38, 445, 2266, 2268, 445, 38, 2392, 2395, 38, 363, 2397, 2400, 38, 363, 2395, 2397, 363, 38, 2404, 2407, 38, 363, 2409, 2412, 38, 363, 2407, 2409, 363, 38, 2416, 2419, 38, 363, 2421, 2424, 38, 363, 2419, 2421, 363, 38, 721, 726, 305, 329, 726, 728, 329, 305, 727, 728, 327, 328, 728, 733, 328, 329, 741, 746, 284, 304, 728, 746, 305, 327, 746, 747, 304, 305, 746, 748, 327, 284, 753, 758, 281, 283, 748, 758, 284, 327, 758, 759, 283, 284, 758, 760, 327, 281, 800, 805, 148, 151, 805, 807, 151, 148, 806, 807, 149, 150, 807, 812, 150, 151, 817, 822, 140, 147, 807, 822, 148, 149, 822, 823, 147, 148, 822, 824, 149, 140, 829, 834, 138, 139, 824, 834, 140, 149, 834, 835, 139, 140, 834, 836, 149, 138, 952, 957, 349, 378, 957, 959, 378, 349, 958, 959, 376, 377, 959, 964, 377, 378, 760, 969, 281, 327, 959, 969, 349, 376, 969, 970, 327, 349, 969, 971, 376, 281, 992, 997, 243, 279, 997, 998, 279, 281, 997, 999, 376, 243, 1032, 1037, 217, 242, 1037, 1038, 242, 243, 1037, 1039, 376, 217, 1044, 1049, 214, 216, 1039, 1049, 217, 376, 1049, 1050, 216, 217, 1049, 1051, 376, 214, 836, 1061, 138, 149, 1056, 1061, 180, 182, 1061, 1062, 149, 180, 1061, 1063, 182, 138, 1063, 1068, 138, 182, 1068, 1070, 182, 138, 1069, 1070, 179, 181, 1070, 1075, 181, 182, 1130, 1135, 405, 455, 1135, 1137, 455, 405, 1136, 1137, 453, 454, 1137, 1142, 454, 455, 1051, 1147, 214, 376, 1137, 1147, 405, 453, 1147, 1148, 376, 405, 1147, 1149, 453, 214, 1246, 1251, 188, 212, 1251, 1252, 212, 214, 1251, 1253, 453, 188, 1070, 1283, 138, 179, 1283, 1284, 179, 188, 1283, 1285, 453, 138, 1306, 1311, 50, 136, 1311, 1312, 136, 138, 1311, 1313, 453, 50, 1346, 1351, 44, 49, 1351, 1352, 49, 50, 1351, 1353, 453, 44, 1358, 1363, 41, 43, 1353, 1363, 44, 453, 1363, 1364, 43, 44, 1363, 1365, 453, 41, 1365, 1483, 41, 453, 1483, 1485, 453, 41, 1484, 1485, 404, 451, 1485, 1490, 451, 453, 1523, 1525, 404, 41, 1524, 1525, 374, 403, 1525, 1530, 403, 404, 1525, 1535, 41, 374, 1535, 1537, 374, 41, 1536, 1537, 371, 373, 1537, 1542, 373, 374, 1679, 1681, 371, 41, 1680, 1681, 48, 135, 1686, 1691, 133, 134, 1681, 1691, 135, 371, 1691, 1692, 134, 135, 1691, 1693, 371, 133, 1681, 1698, 41, 48, 1778, 1783, 402, 450, 1783, 1785, 450, 402, 1784, 1785, 448, 449, 1785, 1790, 449, 450, 1693, 1795, 133, 371, 1785, 1795, 402, 448, 1795, 1796, 371, 402, 1795, 1797, 448, 133, 1958, 1963, 61, 131, 1963, 1964, 131, 133, 1963, 1965, 448, 61, 2072, 2074, 448, 61, 2073, 2074, 401, 446, 2074, 2079, 446, 448, 2104, 2106, 401, 61, 2105, 2106, 369, 400, 2106, 2111, 400, 401, 2106, 2116, 61, 369, 2116, 2118, 369, 61, 2117, 2118, 366, 368, 2118, 2123, 368, 369, 2196, 2198, 366, 61, 2197, 2198, 184, 206, 2203, 2208, 204, 205, 2198, 2208, 206, 366, 2208, 2209, 205, 206, 2208, 2210, 366, 204, 2224, 2226, 184, 61, 2225, 2226, 172, 183, 2226, 2231, 183, 184, 2226, 2236, 61, 172, 2236, 2238, 172, 61, 2237, 2238, 169, 171, 2238, 2243, 171, 172, 2238, 2248, 61, 169, 2248, 2250, 169, 61, 2249, 2250, 115, 130, 2255, 2260, 128, 129, 2250, 2260, 130, 169, 2260, 2261, 129, 130, 2260, 2262, 169, 128, 2262, 2267, 128, 169, 2210, 2357, 204, 366, 2357, 2359, 366, 204, 2358, 2359, 342, 364, 2359, 2364, 364, 366, 2389, 2391, 342, 204, 2390, 2391, 315, 341, 2391, 2396, 341, 342, 2391, 2401, 204, 315, 2401, 2403, 315, 204, 2402, 2403, 312, 314, 2403, 2408, 314, 315, 2403, 2413, 204, 312, 2413, 2415, 312, 204, 2414, 2415, 235, 268, 2420, 2425, 266, 267, 2415, 2425, 268, 312, 2425, 2426, 267, 268, 2425, 2427, 312, 266, 2415, 2432, 204, 235, 2250, 2445, 61, 115, 2427, 2661, 266, 312, 2661, 2663, 312, 266, 2662, 2663, 294, 310, 2663, 2668, 310, 312, 2663, 2684, 266, 294, 1942, 1946, 448, 133, 1965, 1970, 61, 448, 1970, 1974, 448, 61, 1990, 2072, 61, 448, 1986, 1990, 448, 61, 2198, 2215, 61, 184, 2219, 2224, 61, 184, 2215, 2219, 184, 61, 1937, 1942, 133, 448, 1935, 1937, 448, 133, 1946, 1951, 133, 448, 1953, 1963, 133, 448, 1951, 1953, 448, 133, 1974, 1979, 61, 448, 1981, 1986, 61, 448, 1979, 1981, 448, 61, 1622, 1626, 371, 41, 1654, 1658, 371, 41, 1674, 1679, 41, 371, 1670, 1674, 371, 41, 1894, 1898, 448, 133, 1617, 1622, 41, 371, 1615, 1617, 371, 41, 1626, 1631, 41, 371, 1631, 1633, 371, 41, 1649, 1654, 41, 371, 1647, 1649, 371, 41, 1658, 1663, 41, 371, 1665, 1670, 41, 371, 1663, 1665, 371, 41, 1898, 1903, 133, 448, 1903, 1905, 448, 133, 1827, 1833, 448, 133, 1863, 1869, 448, 133, 1889, 1894, 133, 448, 1883, 1889, 448, 133, 2118, 2128, 61, 366, 2128, 2134, 366, 61, 1822, 1827, 133, 448, 1818, 1822, 448, 133, 1833, 1838, 133, 448, 1838, 1842, 448, 133, 1858, 1863, 133, 448, 1854, 1858, 448, 133, 1869, 1874, 133, 448, 1878, 1883, 133, 448, 1874, 1878, 448, 133, 2134, 2139, 61, 366, 2139, 2143, 366, 61, 2171, 2175, 366, 61, 1285, 1290, 138, 453, 1290, 1294, 453, 138, 1313, 1318, 50, 453, 1318, 1322, 453, 50, 1338, 1351, 50, 453, 1334, 1338, 453, 50, 1633, 1638, 41, 371, 1642, 1647, 41, 371, 1638, 1642, 371, 41, 1294, 1299, 138, 453, 1301, 1311, 138, 453, 1299, 1301, 453, 138, 1322, 1327, 50, 453, 1329, 1334, 50, 453, 1327, 1329, 453, 50, 1179, 1185, 453, 214, 1215, 1221, 453, 214, 1241, 1251, 214, 453, 1235, 1241, 453, 214, 1537, 1547, 41, 371, 1547, 1553, 371, 41, 1174, 1179, 214, 453, 1170, 1174, 453, 214, 1185, 1190, 214, 453, 1190, 1194, 453, 214, 1210, 1215, 214, 453, 1206, 1210, 453, 214, 1221, 1226, 214, 453, 1230, 1235, 214, 453, 1226, 1230, 453, 214, 1553, 1558, 41, 371, 1558, 1562, 371, 41, 1590, 1594, 371, 41, 971, 976, 281, 376, 976, 980, 376, 281, 999, 1004, 243, 376, 1004, 1008, 376, 243, 1024, 1037, 243, 376, 1020, 1024, 376, 243, 1149, 1154, 214, 453, 1154, 1158, 453, 214, 1253, 1258, 188, 453, 1258, 1262, 453, 188, 1278, 1283, 188, 453, 1274, 1278, 453, 188, 1485, 1514, 41, 404, 1518, 1523, 41, 404, 1514, 1518, 404, 41, 1574, 1578, 371, 41, 1610, 1615, 41, 371, 1606, 1610, 371, 41, 1797, 1802, 133, 448, 1802, 1806, 448, 133, 1905, 1910, 133, 448, 1910, 1914, 448, 133, 1930, 1935, 133, 448, 1926, 1930, 448, 133, 2074, 2095, 61, 401, 2099, 2104, 61, 401, 2095, 2099, 401, 61, 2155, 2159, 366, 61, 2191, 2196, 61, 366, 2187, 2191, 366, 61, 2359, 2380, 204, 342, 2384, 2389, 204, 342, 2380, 2384, 342, 204, 980, 985, 281, 376, 987, 997, 281, 376, 985, 987, 376, 281, 1008, 1013, 243, 376, 1015, 1020, 243, 376, 1013, 1015, 376, 243, 1158, 1163, 214, 453, 1165, 1170, 214, 453, 1163, 1165, 453, 214, 1194, 1199, 214, 453, 1201, 1206, 214, 453, 1199, 1201, 453, 214, 1262, 1267, 188, 453, 1269, 1274, 188, 453, 1267, 1269, 453, 188, 1562, 1567, 41, 371, 1569, 1574, 41, 371, 1567, 1569, 371, 41, 1578, 1583, 41, 371, 1585, 1590, 41, 371, 1583, 1585, 371, 41, 1594, 1599, 41, 371, 1601, 1606, 41, 371, 1599, 1601, 371, 41, 1806, 1811, 133, 448, 1813, 1818, 133, 448, 1811, 1813, 448, 133, 1842, 1847, 133, 448, 1849, 1854, 133, 448, 1847, 1849, 448, 133, 1914, 1919, 133, 448, 1921, 1926, 133, 448, 1919, 1921, 448, 133, 2143, 2148, 61, 366, 2150, 2155, 61, 366, 2148, 2150, 366, 61, 2159, 2164, 61, 366, 2166, 2171, 61, 366, 2164, 2166, 366, 61, 2175, 2180, 61, 366, 2182, 2187, 61, 366, 2180, 2182, 366, 61, 1088, 1401, 804, 859, 1401, 1403, 859, 804, 1402, 1403, 820, 848, 1403, 1404, 804, 820, 2863, 2864, 819, 846, 2864, 2865, 846, 848, 2864, 2866, 859, 819, 2883, 2884, 802, 818, 2884, 2885, 818, 819, 2884, 2886, 859, 802, 2887, 2888, 799, 801, 2886, 2888, 802, 859, 2888, 2889, 801, 802, 2888, 2890, 859, 799, 3103, 3104, 739, 752, 3099, 3104, 753, 769, 3104, 3105, 752, 753, 3104, 3106, 769, 739, 3107, 3108, 736, 738, 3106, 3108, 739, 769, 3108, 3109, 738, 739, 3108, 3110, 769, 736, 3230, 3231, 776, 797, 3231, 3232, 797, 799, 3231, 3233, 859, 776, 3110, 3247, 736, 769, 3247, 3248, 769, 776, 3247, 3249, 859, 736, 3258, 3259, 723, 734, 3259, 3260, 734, 736, 3259, 3261, 859, 723, 3280, 3282, 859, 723, 3281, 3282, 775, 796, 3283, 3284, 794, 795, 3282, 3284, 796, 859, 3284, 3285, 795, 796, 3284, 3286, 859, 794, 3292, 3294, 775, 723, 3293, 3294, 767, 774, 3294, 3295, 774, 775, 3294, 3296, 723, 767, 3296, 3298, 767, 723, 3297, 3298, 764, 766, 3298, 3299, 766, 767, 3298, 3300, 723, 764, 3300, 3302, 764, 723, 3301, 3302, 724, 733, 3303, 3304, 731, 732, 3302, 3304, 733, 764, 3304, 3305, 732, 733, 3304, 3306, 764, 731, 3302, 3307, 723, 724, 3286, 3380, 794, 859, 3380, 3382, 859, 794, 3381, 3382, 836, 838, 3388, 3390, 836, 794, 3389, 3390, 834, 835, 3390, 3391, 835, 836, 3390, 3392, 794, 834, 3392, 3394, 834, 794, 3393, 3394, 814, 828, 3395, 3396, 826, 827, 3394, 3396, 828, 834, 3396, 3397, 827, 828, 3396, 3398, 834, 826, 3394, 3399, 794, 814, 3306, 3404, 731, 764, 3404, 3406, 764, 731, 3405, 3406, 748, 762, 3406, 3407, 762, 764, 3406, 3415, 731, 748, 3398, 3423, 826, 834, 3423, 3425, 834, 826, 3424, 3425, 830, 833, 3425, 3426, 833, 834, 3425, 3427, 826, 830, 3382, 3747, 838, 859, 3747, 3749, 859, 838, 3748, 3749, 857, 858, 3749, 3750, 858, 859, 3756, 3758, 857, 838, 3757, 3758, 855, 856, 3758, 3759, 856, 857, 3758, 3760, 838, 855, 3760, 3762, 855, 838, 3761, 3762, 839, 845, 3763, 3764, 843, 844, 3762, 3764, 845, 855, 3764, 3765, 844, 845, 3764, 3766, 855, 843, 3762, 3767, 838, 839, 3766, 3975, 843, 855, 3975, 3977, 855, 843, 3976, 3977, 849, 854, 3977, 3978, 854, 855, 3977, 3979, 843, 849, 3249, 3250, 736, 859, 3250, 3254, 859, 736, 3261, 3262, 723, 859, 3262, 3266, 859, 723, 3270, 3274, 859, 723, 3282, 3287, 723, 775, 3291, 3292, 723, 775, 3287, 3291, 775, 723, 3254, 3255, 736, 859, 3257, 3259, 736, 859, 3255, 3257, 859, 736, 3266, 3267, 723, 859, 3269, 3270, 723, 859, 3267, 3269, 859, 723, 3233, 3234, 776, 859, 3234, 3238, 859, 776, 3246, 3247, 776, 859, 3242, 3246, 859, 776, 3274, 3275, 723, 859, 3279, 3280, 723, 859, 3275, 3279, 859, 723, 3382, 3383, 794, 836, 3387, 3388, 794, 836, 3383, 3387, 836, 794, 2890, 3227, 799, 859, 3229, 3231, 799, 859, 3227, 3229, 859, 799, 3238, 3239, 776, 859, 3241, 3242, 776, 859, 3239, 3241, 859, 776, 2866, 2867, 819, 859, 2867, 2871, 859, 819, 2879, 2884, 819, 859, 2875, 2879, 859, 819, 3749, 3751, 838, 857, 3755, 3756, 838, 857, 3751, 3755, 857, 838, 1403, 2860, 848, 859, 2862, 2864, 848, 859, 2860, 2862, 859, 848, 2871, 2872, 819, 859, 2874, 2875, 819, 859, 2872, 2874, 859, 819, 1410, 1413, 673, 744, 1413, 1415, 744, 673, 1414, 1415, 742, 743, 1415, 1418, 743, 744, 1426, 1429, 648, 672, 1415, 1429, 673, 742, 1429, 1430, 672, 673, 1429, 1431, 742, 648, 1434, 1437, 645, 647, 1431, 1437, 648, 742, 1437, 1438, 647, 648, 1437, 1439, 742, 645, 1439, 1713, 645, 742, 1713, 1715, 742, 645, 1714, 1715, 671, 707, 1715, 1718, 645, 671, 1999, 2002, 670, 705, 2002, 2003, 705, 707, 2002, 2004, 742, 670, 2019, 2022, 643, 669, 2022, 2023, 669, 670, 2022, 2024, 742, 643, 2027, 2030, 640, 642, 2024, 2030, 643, 742, 2030, 2031, 642, 643, 2030, 2032, 742, 640, 2276, 2279, 591, 638, 2279, 2280, 638, 640, 2279, 2281, 742, 591, 2308, 2311, 564, 590, 2311, 2312, 590, 591, 2311, 2313, 742, 564, 2316, 2319, 561, 563, 2313, 2319, 564, 742, 2319, 2320, 563, 564, 2319, 2321, 742, 561, 2324, 2327, 465, 486, 2327, 2329, 486, 465, 2328, 2329, 484, 485, 2329, 2332, 485, 486, 2340, 2343, 445, 464, 2329, 2343, 465, 484, 2343, 2344, 464, 465, 2343, 2345, 484, 445, 2348, 2351, 442, 444, 2345, 2351, 445, 484, 2351, 2352, 444, 445, 2351, 2353, 484, 442, 2568, 2571, 513, 559, 2571, 2572, 559, 561, 2571, 2573, 742, 513, 2353, 2595, 442, 484, 2595, 2596, 484, 513, 2595, 2597, 742, 442, 2612, 2615, 397, 440, 2615, 2616, 440, 442, 2615, 2617, 742, 397, 2644, 2647, 363, 396, 2647, 2648, 396, 397, 2647, 2649, 742, 363, 2652, 2655, 360, 362, 2649, 2655, 363, 742, 2655, 2656, 362, 363, 2655, 2657, 742, 360, 2657, 2707, 360, 742, 2707, 2709, 742, 360, 2708, 2709, 395, 427, 2709, 2712, 360, 395, 2709, 2892, 427, 742, 2892, 2894, 742, 427, 2893, 2894, 720, 740, 2894, 2897, 740, 742, 2912, 2914, 720, 427, 2913, 2914, 716, 719, 2914, 2917, 719, 720, 2914, 2920, 427, 716, 2920, 2922, 716, 427, 2921, 2922, 713, 715, 2922, 2925, 715, 716, 2980, 2982, 713, 427, 2981, 2982, 512, 558, 2985, 2988, 556, 557, 2982, 2988, 558, 713, 2988, 2989, 557, 558, 2988, 2990, 713, 556, 3000, 3002, 512, 427, 3001, 3002, 482, 511, 3002, 3005, 511, 512, 3002, 3008, 427, 482, 3008, 3010, 482, 427, 3009, 3010, 479, 481, 3010, 3013, 481, 482, 3010, 3016, 427, 479, 3016, 3018, 479, 427, 3017, 3018, 434, 439, 3021, 3024, 437, 438, 3018, 3024, 439, 479, 3024, 3025, 438, 439, 3024, 3026, 479, 437, 3018, 3029, 427, 434, 2990, 3112, 556, 713, 3112, 3114, 713, 556, 3113, 3114, 701, 711, 3114, 3117, 711, 713, 3132, 3134, 701, 556, 3133, 3134, 692, 700, 3134, 3137, 700, 701, 3134, 3140, 556, 692, 3140, 3142, 692, 556, 3141, 3142, 689, 691, 3142, 3145, 691, 692, 3142, 3148, 556, 689, 3148, 3150, 689, 556, 3149, 3150, 586, 632, 3153, 3156, 630, 631, 3150, 3156, 632, 689, 3156, 3157, 631, 632, 3156, 3158, 689, 630, 3150, 3161, 556, 586, 3026, 3172, 437, 479, 3172, 3174, 479, 437, 3173, 3174, 460, 477, 3174, 3177, 477, 479, 3174, 3193, 437, 460, 3158, 3316, 630, 689, 3316, 3318, 689, 630, 3317, 3318, 662, 687, 3318, 3321, 687, 689, 3318, 3329, 630, 662, 2597, 2600, 442, 742, 2600, 2604, 742, 442, 2617, 2620, 397, 742, 2620, 2624, 742, 397, 2636, 2647, 397, 742, 2632, 2636, 742, 397, 2982, 2993, 427, 512, 2997, 3000, 427, 512, 2993, 2997, 512, 427, 2604, 2607, 442, 742, 2609, 2615, 442, 742, 2607, 2609, 742, 442, 2624, 2627, 397, 742, 2629, 2632, 397, 742, 2627, 2629, 742, 397, 2515, 2521, 742, 561, 2543, 2549, 742, 561, 2565, 2571, 561, 742, 2559, 2565, 742, 561, 2922, 2928, 427, 713, 2928, 2934, 713, 427, 2512, 2515, 561, 742, 2508, 2512, 742, 561, 2521, 2524, 561, 742, 2524, 2528, 742, 561, 2540, 2543, 561, 742, 2536, 2540, 742, 561, 2549, 2552, 561, 742, 2556, 2559, 561, 742, 2552, 2556, 742, 561, 2934, 2937, 427, 713, 2937, 2941, 713, 427, 2961, 2965, 713, 427, 2004, 2007, 670, 742, 2011, 2022, 670, 742, 2007, 2011, 742, 670, 2281, 2284, 591, 742, 2284, 2288, 742, 591, 2300, 2311, 591, 742, 2296, 2300, 742, 591, 2505, 2508, 561, 742, 2501, 2505, 742, 561, 2573, 2576, 513, 742, 2576, 2580, 742, 513, 2592, 2595, 513, 742, 2588, 2592, 742, 513, 2894, 2905, 427, 720, 2909, 2912, 427, 720, 2905, 2909, 720, 427, 2949, 2953, 713, 427, 2977, 2980, 427, 713, 2973, 2977, 713, 427, 3114, 3125, 556, 701, 3129, 3132, 556, 701, 3125, 3129, 701, 556, 1715, 1994, 707, 742, 1996, 2002, 707, 742, 1994, 1996, 742, 707, 2032, 2271, 640, 742, 2273, 2279, 640, 742, 2271, 2273, 742, 640, 2288, 2291, 591, 742, 2293, 2296, 591, 742, 2291, 2293, 742, 591, 2321, 2496, 561, 742, 2498, 2501, 561, 742, 2496, 2498, 742, 561, 2528, 2531, 561, 742, 2533, 2536, 561, 742, 2531, 2533, 742, 561, 2580, 2583, 513, 742, 2585, 2588, 513, 742, 2583, 2585, 742, 513, 2941, 2944, 427, 713, 2946, 2949, 427, 713, 2944, 2946, 713, 427, 2953, 2956, 427, 713, 2958, 2961, 427, 713, 2956, 2958, 713, 427, 2965, 2968, 427, 713, 2970, 2973, 427, 713, 2968, 2970, 713, 427, 970, 977, 303, 327, 977, 979, 327, 303, 978, 979, 325, 326, 979, 986, 326, 327, 998, 1005, 281, 302, 979, 1005, 303, 325, 1005, 1006, 302, 303, 1005, 1007, 325, 281, 1014, 1021, 278, 280, 1007, 1021, 281, 325, 1021, 1022, 280, 281, 1021, 1023, 325, 278, 1148, 1155, 348, 376, 1155, 1157, 376, 348, 1156, 1157, 374, 375, 1157, 1164, 375, 376, 1023, 1171, 278, 325, 1157, 1171, 348, 374, 1171, 1172, 325, 348, 1171, 1173, 374, 278, 1200, 1207, 241, 276, 1207, 1208, 276, 278, 1207, 1209, 374, 241, 1252, 1259, 214, 240, 1259, 1260, 240, 241, 1259, 1261, 374, 214, 1268, 1275, 211, 213, 1261, 1275, 214, 374, 1275, 1276, 213, 214, 1275, 1277, 374, 211, 1277, 1515, 211, 374, 1515, 1517, 374, 211, 1516, 1517, 347, 372, 1517, 1524, 372, 374, 1559, 1561, 347, 211, 1560, 1561, 323, 346, 1561, 1568, 346, 347, 1561, 1575, 211, 323, 1575, 1577, 323, 211, 1576, 1577, 320, 322, 1577, 1584, 322, 323, 1577, 1591, 211, 320, 1591, 1593, 320, 211, 1592, 1593, 239, 275, 1600, 1607, 273, 274, 1593, 1607, 275, 320, 1607, 1608, 274, 275, 1607, 1609, 320, 273, 1593, 1616, 211, 239, 1796, 1803, 345, 371, 1803, 1805, 371, 345, 1804, 1805, 369, 370, 1805, 1812, 370, 371, 1609, 1819, 273, 320, 1805, 1819, 345, 369, 1819, 1820, 320, 345, 1819, 1821, 369, 273, 1848, 1855, 238, 271, 1855, 1856, 271, 273, 1855, 1857, 369, 238, 1904, 1911, 209, 237, 1911, 1912, 237, 238, 1911, 1913, 369, 209, 1920, 1927, 206, 208, 1913, 1927, 209, 369, 1927, 1928, 208, 209, 1927, 1929, 369, 206, 1929, 2096, 206, 369, 2096, 2098, 369, 206, 2097, 2098, 344, 367, 2098, 2105, 367, 369, 2140, 2142, 344, 206, 2141, 2142, 318, 343, 2142, 2149, 343, 344, 2142, 2156, 206, 318, 2156, 2158, 318, 206, 2157, 2158, 315, 317, 2158, 2165, 317, 318, 2158, 2172, 206, 315, 2172, 2174, 315, 206, 2173, 2174, 236, 270, 2181, 2188, 268, 269, 2174, 2188, 270, 315, 2188, 2189, 269, 270, 2188, 2190, 315, 268, 2174, 2197, 206, 236, 2190, 2381, 268, 315, 2381, 2383, 315, 268, 2382, 2383, 295, 313, 2383, 2390, 313, 315, 2383, 2414, 268, 295, 1821, 1828, 273, 369, 1828, 1832, 369, 273, 1857, 1864, 238, 369, 1864, 1868, 369, 238, 1888, 1911, 238, 369, 1884, 1888, 369, 238, 2098, 2129, 206, 344, 2133, 2140, 206, 344, 2129, 2133, 344, 206, 1832, 1839, 273, 369, 1841, 1855, 273, 369, 1839, 1841, 369, 273, 1868, 1875, 238, 369, 1877, 1884, 238, 369, 1875, 1877, 369, 238, 1173, 1180, 278, 374, 1180, 1184, 374, 278, 1209, 1216, 241, 374, 1216, 1220, 374, 241, 1240, 1259, 241, 374, 1236, 1240, 374, 241, 1517, 1548, 211, 347, 1552, 1559, 211, 347, 1548, 1552, 347, 211, 1184, 1191, 278, 374, 1193, 1207, 278, 374, 1191, 1193, 374, 278, 1220, 1227, 241, 374, 1229, 1236, 241, 374, 1227, 1229, 374, 241, 876, 881, 543, 574, 881, 883, 574, 543, 882, 883, 572, 573, 883, 888, 573, 574, 896, 901, 531, 542, 883, 901, 543, 572, 901, 902, 542, 543, 901, 903, 572, 531, 908, 913, 528, 530, 903, 913, 531, 572, 913, 914, 530, 531, 913, 915, 572, 528, 1091, 1096, 520, 527, 915, 1096, 528, 572, 1096, 1097, 527, 528, 1096, 1098, 572, 520, 1106, 1111, 496, 519, 1098, 1111, 520, 572, 1111, 1112, 519, 520, 1111, 1113, 572, 496, 1118, 1123, 493, 495, 1113, 1123, 496, 572, 1123, 1124, 495, 496, 1123, 1125, 572, 493, 1125, 1443, 493, 572, 1443, 1445, 572, 493, 1444, 1445, 518, 570, 1445, 1450, 570, 572, 1445, 1466, 493, 518, 2003, 2008, 707, 708, 1995, 2008, 709, 716, 2008, 2009, 708, 709, 2008, 2010, 716, 707, 2280, 2285, 640, 667, 2272, 2285, 668, 697, 2285, 2286, 667, 668, 2285, 2287, 697, 640, 2292, 2297, 637, 639, 2287, 2297, 640, 697, 2297, 2298, 639, 640, 2297, 2299, 697, 637, 2497, 2502, 704, 706, 2010, 2502, 707, 716, 2502, 2503, 706, 707, 2502, 2504, 716, 704, 2299, 2509, 637, 697, 2504, 2509, 704, 716, 2509, 2510, 697, 704, 2509, 2511, 716, 637, 2532, 2537, 589, 635, 2537, 2538, 635, 637, 2537, 2539, 716, 589, 2572, 2577, 561, 588, 2577, 2578, 588, 589, 2577, 2579, 716, 561, 2584, 2589, 558, 560, 2579, 2589, 561, 716, 2589, 2590, 560, 561, 2589, 2591, 716, 558, 2591, 2906, 558, 716, 2906, 2908, 716, 558, 2907, 2908, 703, 714, 2908, 2913, 714, 716, 2938, 2940, 703, 558, 2939, 2940, 695, 702, 2940, 2945, 702, 703, 2940, 2950, 558, 695, 2950, 2952, 695, 558, 2951, 2952, 692, 694, 2952, 2957, 694, 695, 2952, 2962, 558, 692, 2962, 2964, 692, 558, 2963, 2964, 587, 634, 2969, 2974, 632, 633, 2964, 2974, 634, 692, 2974, 2975, 633, 634, 2974, 2976, 692, 632, 2964, 2981, 558, 587, 2976, 3126, 632, 692, 3126, 3128, 692, 632, 3127, 3128, 663, 690, 3128, 3133, 690, 692, 3128, 3149, 632, 663, 2511, 2516, 637, 716, 2516, 2520, 716, 637, 2539, 2544, 589, 716, 2544, 2548, 716, 589, 2564, 2577, 589, 716, 2560, 2564, 716, 589, 2908, 2929, 558, 703, 2933, 2938, 558, 703, 2929, 2933, 703, 558, 2520, 2525, 637, 716, 2527, 2537, 637, 716, 2525, 2527, 716, 637, 2548, 2553, 589, 716, 2555, 2560, 589, 716, 2553, 2555, 716, 589, 3341, 3346, 508, 554, 3346, 3348, 554, 508, 3347, 3348, 552, 553, 3348, 3353, 553, 554, 3358, 3363, 476, 507, 3348, 3363, 508, 552, 3363, 3364, 507, 508, 3363, 3365, 552, 476, 3370, 3375, 474, 475, 3365, 3375, 476, 552, 3375, 3376, 475, 476, 3375, 3377, 552, 474, 3377, 3494, 474, 552, 3433, 3436, 771, 792, 3436, 3438, 792, 771, 3437, 3438, 790, 791, 3438, 3441, 791, 792, 3445, 3448, 761, 770, 3438, 3448, 771, 790, 3448, 3449, 770, 771, 3448, 3450, 790, 761, 3453, 3456, 758, 760, 3450, 3456, 761, 790, 3456, 3457, 760, 761, 3456, 3458, 790, 758, 3525, 3528, 659, 757, 3458, 3528, 758, 790, 3528, 3529, 757, 758, 3528, 3530, 790, 659, 3538, 3541, 622, 658, 3530, 3541, 659, 790, 3541, 3542, 658, 659, 3541, 3543, 790, 622, 3546, 3549, 619, 621, 3543, 3549, 622, 790, 3549, 3550, 621, 622, 3549, 3551, 790, 619, 3769, 3772, 812, 824, 3772, 3774, 824, 812, 3773, 3774, 822, 823, 3774, 3777, 823, 824, 3551, 3780, 619, 790, 3774, 3780, 812, 822, 3780, 3781, 790, 812, 3780, 3782, 822, 619, 3797, 3800, 430, 617, 3800, 3801, 617, 619, 3800, 3802, 822, 430, 3829, 3832, 419, 429, 3832, 3833, 429, 430, 3832, 3834, 822, 419, 3837, 3840, 416, 418, 3834, 3840, 419, 822, 3840, 3841, 418, 419, 3840, 3842, 822, 416, 3842, 3872, 416, 822, 3872, 3874, 822, 416, 3873, 3874, 811, 821, 3874, 3877, 821, 822, 3887, 3889, 811, 416, 3888, 3889, 788, 810, 3889, 3892, 810, 811, 3889, 3895, 416, 788, 3895, 3897, 788, 416, 3896, 3897, 785, 787, 3897, 3900, 787, 788, 3897, 3903, 416, 785, 3903, 3905, 785, 416, 3904, 3905, 428, 616, 3908, 3911, 614, 615, 3905, 3911, 616, 785, 3911, 3912, 615, 616, 3911, 3913, 785, 614, 3905, 3916, 416, 428, 3913, 3947, 614, 785, 3947, 3949, 785, 614, 3948, 3949, 654, 783, 3949, 3952, 783, 785, 3949, 3960, 614, 654, 3782, 3785, 619, 822, 3785, 3789, 822, 619, 3802, 3805, 430, 822, 3805, 3809, 822, 430, 3821, 3832, 430, 822, 3817, 3821, 822, 430, 3874, 3880, 416, 811, 3884, 3887, 416, 811, 3880, 3884, 811, 416, 3789, 3792, 619, 822, 3794, 3800, 619, 822, 3792, 3794, 822, 619, 3809, 3812, 430, 822, 3814, 3817, 430, 822, 3812, 3814, 822, 430, 293, 296, 412, 506, 296, 298, 506, 412, 297, 298, 504, 505, 298, 301, 505, 506, 309, 312, 388, 411, 298, 312, 412, 504, 312, 313, 411, 412, 312, 314, 504, 388, 317, 320, 385, 387, 314, 320, 388, 504, 320, 321, 387, 388, 320, 322, 504, 385, 481, 484, 525, 536, 484, 486, 536, 525, 485, 486, 534, 535, 486, 489, 535, 536, 322, 492, 385, 504, 486, 492, 525, 534, 492, 493, 504, 525, 492, 494, 534, 385, 509, 512, 353, 383, 512, 513, 383, 385, 512, 514, 534, 353, 541, 544, 334, 352, 544, 545, 352, 353, 544, 546, 534, 334, 549, 552, 331, 333, 546, 552, 334, 534, 552, 553, 333, 334, 552, 554, 534, 331, 612, 614, 534, 331, 613, 614, 351, 382, 617, 620, 380, 381, 614, 620, 382, 534, 620, 621, 381, 382, 620, 622, 534, 380, 614, 625, 331, 351, 622, 652, 380, 534, 652, 654, 534, 380, 653, 654, 524, 532, 654, 657, 532, 534, 680, 682, 524, 380, 681, 682, 502, 523, 682, 685, 523, 524, 682, 688, 380, 502, 688, 690, 502, 380, 689, 690, 499, 501, 690, 693, 501, 502, 690, 696, 380, 499, 696, 698, 499, 380, 697, 698, 407, 459, 701, 704, 457, 458, 698, 704, 459, 499, 704, 705, 458, 459, 704, 706, 499, 457, 698, 709, 380, 407, 706, 919, 457, 499, 919, 921, 499, 457, 920, 921, 472, 497, 921, 924, 497, 499, 921, 940, 457, 472, 494, 497, 385, 534, 497, 501, 534, 385, 514, 517, 353, 534, 517, 521, 534, 353, 533, 544, 353, 534, 529, 533, 534, 353, 554, 605, 331, 534, 609, 612, 331, 534, 605, 609, 534, 331, 654, 673, 380, 524, 677, 680, 380, 524, 673, 677, 524, 380, 501, 504, 385, 534, 506, 512, 385, 534, 504, 506, 534, 385, 521, 524, 353, 534, 526, 529, 353, 534, 524, 526, 534, 353, 1172, 1181, 301, 325, 1181, 1183, 325, 301, 1182, 1183, 323, 324, 1183, 1192, 324, 325, 1208, 1217, 278, 300, 1183, 1217, 301, 323, 1217, 1218, 300, 301, 1217, 1219, 323, 278, 1228, 1237, 275, 277, 1219, 1237, 278, 323, 1237, 1238, 277, 278, 1237, 1239, 323, 275, 1239, 1549, 275, 323, 1549, 1551, 323, 275, 1550, 1551, 299, 321, 1551, 1560, 321, 323, 1551, 1592, 275, 299, 557, 560, 165, 222, 560, 562, 222, 165, 561, 562, 220, 221, 562, 565, 221, 222, 573, 576, 156, 164, 562, 576, 165, 220, 576, 577, 164, 165, 576, 578, 220, 156, 581, 584, 153, 155, 578, 584, 156, 220, 584, 585, 155, 156, 584, 586, 220, 153, 586, 764, 153, 220, 764, 766, 220, 153, 765, 766, 163, 218, 766, 769, 218, 220, 766, 785, 153, 163, 1284, 1291, 146, 179, 1291, 1293, 179, 146, 1292, 1293, 177, 178, 1293, 1300, 178, 179, 1312, 1319, 138, 145, 1293, 1319, 146, 177, 1319, 1320, 145, 146, 1319, 1321, 177, 138, 1328, 1335, 135, 137, 1321, 1335, 138, 177, 1335, 1336, 137, 138, 1335, 1337, 177, 135, 1337, 1639, 135, 177, 1639, 1641, 177, 135, 1640, 1641, 144, 175, 1641, 1648, 175, 177, 1641, 1680, 135, 144, 17, 22, 95, 97, 12, 22, 98, 109, 22, 23, 97, 98, 22, 24, 109, 95, 141, 146, 114, 161, 146, 148, 161, 114, 147, 148, 159, 160, 148, 153, 160, 161, 24, 158, 95, 109, 148, 158, 114, 159, 158, 159, 109, 114, 158, 160, 159, 95, 181, 186, 88, 93, 186, 187, 93, 95, 186, 188, 159, 88, 221, 226, 86, 87, 226, 227, 87, 88, 226, 228, 159, 86, 228, 362, 86, 159, 362, 364, 159, 86, 363, 364, 113, 157, 364, 369, 157, 159, 394, 396, 113, 86, 395, 396, 107, 112, 396, 401, 112, 113, 396, 406, 86, 107, 406, 408, 107, 86, 407, 408, 104, 106, 408, 413, 106, 107, 408, 418, 86, 104, 418, 420, 104, 86, 419, 420, 90, 92, 420, 425, 86, 90, 430, 435, 89, 91, 420, 435, 92, 104, 435, 436, 91, 92, 435, 437, 104, 89, 437, 590, 89, 104, 160, 165, 95, 159, 165, 169, 159, 95, 188, 193, 88, 159, 193, 197, 159, 88, 213, 226, 88, 159, 209, 213, 159, 88, 364, 385, 86, 113, 389, 394, 86, 113, 385, 389, 113, 86, 169, 174, 95, 159, 176, 186, 95, 159, 174, 176, 159, 95, 197, 202, 88, 159, 204, 209, 88, 159, 202, 204, 159, 88, 1079, 1082, 725, 746, 2865, 2868, 848, 851, 2861, 2868, 852, 855, 2868, 2869, 851, 852, 2868, 2870, 855, 848, 2873, 2876, 845, 847, 2870, 2876, 848, 855, 2876, 2877, 847, 848, 2876, 2878, 855, 845, 2878, 3752, 845, 855, 3752, 3754, 855, 845, 3753, 3754, 850, 853, 3754, 3757, 853, 855, 3754, 3761, 845, 850, 3232, 3235, 799, 816, 3228, 3235, 817, 834, 3235, 3236, 816, 817, 3235, 3237, 834, 799, 3240, 3243, 796, 798, 3237, 3243, 799, 834, 3243, 3244, 798, 799, 3243, 3245, 834, 796, 3245, 3276, 796, 834, 3276, 3278, 834, 796, 3277, 3278, 815, 828, 3278, 3281, 796, 815, 3278, 3384, 828, 834, 3384, 3386, 834, 828, 3385, 3386, 831, 832, 3386, 3389, 832, 834, 3386, 3393, 828, 831, 3248, 3251, 751, 769, 3251, 3253, 769, 751, 3252, 3253, 767, 768, 3253, 3256, 768, 769, 3260, 3263, 736, 750, 3253, 3263, 751, 767, 3263, 3264, 750, 751, 3263, 3265, 767, 736, 3268, 3271, 733, 735, 3265, 3271, 736, 767, 3271, 3272, 735, 736, 3271, 3273, 767, 733, 3273, 3288, 733, 767, 3288, 3290, 767, 733, 3289, 3290, 749, 765, 3290, 3293, 765, 767, 3290, 3301, 733, 749, 848, 851, 678, 681, 840, 851, 682, 725, 851, 852, 681, 682, 851, 853, 725, 678, 856, 859, 675, 677, 853, 859, 678, 725, 859, 860, 677, 678, 859, 861, 725, 675, 861, 1079, 675, 725, 2510, 2517, 666, 697, 2517, 2519, 697, 666, 2518, 2519, 695, 696, 2519, 2526, 696, 697, 2538, 2545, 637, 665, 2519, 2545, 666, 695, 2545, 2546, 665, 666, 2545, 2547, 695, 637, 2554, 2561, 634, 636, 2547, 2561, 637, 695, 2561, 2562, 636, 637, 2561, 2563, 695, 634, 2563, 2930, 634, 695, 2930, 2932, 695, 634, 2931, 2932, 664, 693, 2932, 2939, 693, 695, 2932, 2963, 634, 664, 3461, 3464, 661, 728, 3464, 3466, 728, 661, 3465, 3466, 726, 727, 3466, 3469, 727, 728, 3477, 3480, 628, 660, 3466, 3480, 661, 726, 3480, 3481, 660, 661, 3480, 3482, 726, 628, 3485, 3488, 625, 627, 3482, 3488, 628, 726, 3488, 3489, 627, 628, 3488, 3490, 726, 625, 3490, 3509, 625, 726, 3781, 3786, 657, 790, 3786, 3788, 790, 657, 3787, 3788, 788, 789, 3788, 3793, 789, 790, 3801, 3806, 619, 656, 3788, 3806, 657, 788, 3806, 3807, 656, 657, 3806, 3808, 788, 619, 3813, 3818, 616, 618, 3808, 3818, 619, 788, 3818, 3819, 618, 619, 3818, 3820, 788, 616, 3820, 3881, 616, 788, 3881, 3883, 788, 616, 3882, 3883, 655, 786, 3883, 3888, 786, 788, 3883, 3904, 616, 655, 3985, 3988, 653, 782, 3988, 3990, 782, 653, 3989, 3990, 780, 781, 3990, 3993, 781, 782, 3996, 3999, 611, 652, 3990, 3999, 653, 780, 3999, 4000, 652, 653, 3999, 4001, 780, 611, 4004, 4007, 609, 610, 4001, 4007, 611, 780, 4007, 4008, 610, 611, 4007, 4009, 780, 609, 4009, 4016, 609, 780, 4016, 4018, 780, 609, 4017, 4018, 651, 778, 4018, 4021, 778, 780, 4018, 4029, 609, 651, 449, 452, 600, 680, 452, 454, 680, 600, 453, 454, 678, 679, 454, 457, 679, 680, 465, 468, 579, 599, 454, 468, 600, 678, 468, 469, 599, 600, 468, 470, 678, 579, 473, 476, 576, 578, 470, 476, 579, 678, 476, 477, 578, 579, 476, 478, 678, 576, 478, 636, 576, 678, 636, 638, 678, 576, 637, 638, 598, 650, 638, 641, 576, 598, 638, 843, 650, 678, 843, 845, 678, 650, 844, 845, 674, 676, 845, 848, 676, 678, 845, 864, 650, 674, 73, 78, 541, 548, 65, 78, 549, 582, 78, 79, 548, 549, 78, 80, 582, 541, 85, 90, 538, 540, 80, 90, 541, 582, 90, 91, 540, 541, 90, 92, 582, 538, 92, 258, 538, 582, 258, 260, 582, 538, 259, 260, 547, 580, 260, 265, 580, 582, 260, 281, 538, 547, 1730, 1735, 517, 569, 1735, 1737, 569, 517, 1736, 1737, 567, 568, 1737, 1742, 568, 569, 1754, 1759, 491, 516, 1737, 1759, 517, 567, 1759, 1760, 516, 517, 1759, 1761, 567, 491, 1766, 1771, 488, 490, 1761, 1771, 491, 567, 1771, 1772, 490, 491, 1771, 1773, 567, 488, 1773, 2036, 488, 567, 2036, 2038, 567, 488, 2037, 2038, 515, 565, 2038, 2043, 565, 567, 2038, 2059, 488, 515, 1466, 1471, 470, 493, 1471, 1473, 493, 470, 1472, 1473, 491, 492, 1473, 1478, 492, 493, 1490, 1495, 453, 469, 1473, 1495, 470, 491, 1495, 1496, 469, 470, 1495, 1497, 491, 453, 1502, 1507, 450, 452, 1497, 1507, 453, 491, 1507, 1508, 452, 453, 1507, 1509, 491, 450, 1509, 1747, 450, 491, 1747, 1749, 491, 450, 1748, 1749, 468, 489, 1749, 1754, 489, 491, 1749, 1778, 450, 468, 2596, 2601, 463, 484, 2601, 2603, 484, 463, 2602, 2603, 482, 483, 2603, 2608, 483, 484, 2616, 2621, 442, 462, 2603, 2621, 463, 482, 2621, 2622, 462, 463, 2621, 2623, 482, 442, 2628, 2633, 439, 441, 2623, 2633, 442, 482, 2633, 2634, 441, 442, 2633, 2635, 482, 439, 2635, 2994, 439, 482, 2994, 2996, 482, 439, 2995, 2996, 461, 480, 2996, 3001, 480, 482, 2996, 3017, 439, 461, 493, 498, 410, 504, 498, 500, 504, 410, 499, 500, 502, 503, 500, 505, 503, 504, 513, 518, 385, 409, 500, 518, 410, 502, 518, 519, 409, 410, 518, 520, 502, 385, 525, 530, 382, 384, 520, 530, 385, 502, 530, 531, 384, 385, 530, 532, 502, 382, 532, 606, 382, 502, 606, 608, 502, 382, 607, 608, 408, 459, 608, 613, 382, 408, 608, 674, 459, 502, 674, 676, 502, 459, 675, 676, 473, 500, 676, 681, 500, 502, 676, 697, 459, 473, 1820, 1829, 298, 320, 1829, 1831, 320, 298, 1830, 1831, 318, 319, 1831, 1840, 319, 320, 1856, 1865, 273, 297, 1831, 1865, 298, 318, 1865, 1866, 297, 298, 1865, 1867, 318, 273, 1876, 1885, 270, 272, 1867, 1885, 273, 318, 1885, 1886, 272, 273, 1885, 1887, 318, 270, 1887, 2130, 270, 318, 2130, 2132, 318, 270, 2131, 2132, 296, 316, 2132, 2141, 316, 318, 2132, 2173, 270, 296, 2724, 2729, 293, 309, 2729, 2731, 309, 293, 2730, 2731, 307, 308, 2731, 2736, 308, 309, 2744, 2749, 264, 292, 2731, 2749, 293, 307, 2749, 2750, 292, 293, 2749, 2751, 307, 264, 2756, 2761, 261, 263, 2751, 2761, 264, 307, 2761, 2762, 263, 264, 2761, 2763, 307, 261, 2763, 2805, 261, 307, 2805, 2807, 307, 261, 2806, 2807, 291, 306, 2807, 2812, 306, 307, 2807, 2817, 261, 291, 3041, 3046, 290, 358, 3046, 3048, 358, 290, 3047, 3048, 356, 357, 3048, 3053, 357, 358, 3061, 3066, 259, 289, 3048, 3066, 290, 356, 3066, 3067, 289, 290, 3066, 3068, 356, 259, 3073, 3078, 256, 258, 3068, 3078, 259, 356, 3078, 3079, 258, 259, 3078, 3080, 356, 256, 3080, 3210, 256, 356, 3205, 3210, 423, 425, 3210, 3211, 356, 423, 3210, 3212, 425, 256, 3212, 3217, 256, 425, 3217, 3219, 425, 256, 3218, 3219, 422, 424, 3219, 3224, 424, 425, 3219, 3555, 256, 422, 3555, 3557, 422, 256, 3556, 3557, 288, 420, 3557, 3562, 420, 422, 3557, 3578, 256, 288, 3916, 3919, 286, 416, 3919, 3921, 416, 286, 3920, 3921, 414, 415, 3921, 3924, 415, 416, 3927, 3930, 252, 285, 3921, 3930, 286, 414, 3930, 3931, 285, 286, 3930, 3932, 414, 252, 3935, 3938, 250, 251, 3932, 3938, 252, 414, 3938, 3939, 251, 252, 3938, 3940, 414, 250, 3940, 3963, 250, 414, 3960, 3963, 612, 614, 3963, 3964, 414, 612, 3963, 3965, 614, 250, 3965, 3968, 250, 614, 3968, 3970, 614, 250, 3969, 3970, 611, 613, 3970, 3973, 613, 614, 3970, 3996, 250, 611, 97, 102, 249, 393, 102, 104, 393, 249, 103, 104, 391, 392, 104, 109, 392, 393, 117, 122, 227, 248, 104, 122, 249, 391, 122, 123, 248, 249, 122, 124, 391, 227, 129, 134, 224, 226, 124, 134, 227, 391, 134, 135, 226, 227, 134, 136, 391, 224, 136, 233, 224, 391, 233, 235, 391, 224, 234, 235, 337, 389, 235, 240, 389, 391, 235, 326, 224, 337, 326, 328, 337, 224, 327, 328, 247, 335, 328, 333, 335, 337, 328, 349, 224, 247, 1616, 1623, 187, 211, 1623, 1625, 211, 187, 1624, 1625, 209, 210, 1625, 1632, 210, 211, 1648, 1655, 177, 186, 1625, 1655, 187, 209, 1655, 1656, 186, 187, 1655, 1657, 209, 177, 1664, 1671, 174, 176, 1657, 1671, 177, 209, 1671, 1672, 176, 177, 1671, 1673, 209, 174, 1673, 1895, 174, 209, 1895, 1897, 209, 174, 1896, 1897, 185, 207, 1897, 1904, 207, 209, 1897, 1936, 174, 185, 1936, 1943, 143, 174, 1943, 1945, 174, 143, 1944, 1945, 172, 173, 1945, 1952, 173, 174, 1964, 1971, 133, 142, 1945, 1971, 143, 172, 1971, 1972, 142, 143, 1971, 1973, 172, 133, 1980, 1987, 130, 132, 1973, 1987, 133, 172, 1987, 1988, 132, 133, 1987, 1989, 172, 130, 1989, 2216, 130, 172, 2216, 2218, 172, 130, 2217, 2218, 141, 170, 2218, 2225, 170, 172, 2218, 2249, 130, 141, 2696, 2699, 124, 202, 2699, 2701, 202, 124, 2700, 2701, 200, 201, 2701, 2704, 201, 202, 2701, 2767, 124, 200, 2767, 2769, 200, 124, 2768, 2769, 127, 198, 2769, 2772, 198, 200, 2769, 2788, 124, 127, 2829, 2832, 126, 197, 2832, 2834, 197, 126, 2833, 2834, 195, 196, 2834, 2837, 196, 197, 2845, 2848, 121, 125, 2834, 2848, 126, 195, 2848, 2849, 125, 126, 2848, 2850, 195, 121, 2853, 2856, 118, 120, 2850, 2856, 121, 195, 2856, 2857, 120, 121, 2856, 2858, 195, 118, 2858, 3084, 118, 195, 159, 166, 101, 109, 166, 168, 109, 101, 167, 168, 107, 108, 168, 175, 108, 109, 187, 194, 95, 100, 168, 194, 101, 107, 194, 195, 100, 101, 194, 196, 107, 95, 203, 210, 92, 94, 196, 210, 95, 107, 210, 211, 94, 95, 210, 212, 107, 92, 212, 386, 92, 107, 386, 388, 107, 92, 387, 388, 99, 105, 388, 395, 105, 107, 388, 419, 92, 99, 3590, 3593, 84, 193, 3593, 3595, 193, 84, 3594, 3595, 191, 192, 3595, 3598, 192, 193, 3606, 3609, 81, 83, 3595, 3609, 84, 191, 3609, 3610, 83, 84, 3609, 3611, 191, 81, 3614, 3617, 78, 80, 3611, 3617, 81, 191, 3617, 3618, 80, 81, 3617, 3619, 191, 78, 3619, 3622, 78, 191, 3622, 3624, 191, 78, 3623, 3624, 82, 190, 3624, 3627, 190, 191, 3624, 3630, 78, 82, 3845, 3848, 71, 254, 3848, 3850, 254, 71, 3849, 3850, 252, 253, 3850, 3853, 253, 254, 3856, 3859, 64, 70, 3850, 3859, 71, 252, 3859, 3860, 70, 71, 3859, 3861, 252, 64, 3864, 3867, 62, 63, 3861, 3867, 64, 252, 3867, 3868, 63, 64, 3867, 3869, 252, 62, 3869, 3927, 62, 252, 3642, 3647, 60, 69, 3647, 3649, 69, 60, 3648, 3649, 67, 68, 3649, 3654, 68, 69, 3662, 3667, 57, 59, 3649, 3667, 60, 67, 3667, 3668, 59, 60, 3667, 3669, 67, 57, 3674, 3679, 54, 56, 3669, 3679, 57, 67, 3679, 3680, 56, 57, 3679, 3681, 67, 54, 3681, 3710, 54, 67, 3710, 3712, 67, 54, 3711, 3712, 58, 65, 3712, 3717, 65, 67, 3712, 3733, 54, 58, 33, 36, 24, 30, 36, 38, 30, 24, 37, 38, 28, 29, 38, 41, 29, 30, 45, 48, 19, 23, 38, 48, 24, 28, 48, 49, 23, 24, 48, 50, 28, 19, 53, 56, 16, 18, 50, 56, 19, 28, 56, 57, 18, 19, 56, 58, 28, 16, 58, 1369, 16, 28, 1369, 1371, 28, 16, 1370, 1371, 22, 26, 1371, 1374, 26, 28, 1371, 1390, 16, 22, 2457, 2460, 21, 38, 2460, 2462, 38, 21, 2461, 2462, 36, 37, 2462, 2465, 37, 38, 2469, 2472, 14, 20, 2462, 2472, 21, 36, 2472, 2473, 20, 21, 2472, 2474, 36, 14, 2477, 2480, 11, 13, 2474, 2480, 14, 36, 2480, 2481, 13, 14, 2480, 2482, 36, 11, 2482, 3685, 11, 36, 1396, 1397, 0, 7, 1397, 1399, 7, 0, 1398, 1399, 5, 6, 1399, 1400, 6, 7, 1399, 2484, 0, 5, 2484, 2486, 5, 0, 2485, 2486, 1, 3, 2486, 2487, 3, 5, 2486, 4037, 0, 1, 4036, 4037, 604, 606, 4037, 4038, 1, 604, 4037, 4039, 606, 0, 4039, 4040, 0, 606, 4040, 4042, 606, 0, 4041, 4042, 603, 605, 4042, 4043, 605, 606, 4042, 4044, 0, 603]

if myflag == 2:
    rect = [700, 1415, 1095, 1106, 1447, 710, 959, 963, 1451, 1539, 925, 953, 1553, 1461, 906, 910, 1687, 1567, 868, 872, 1725, 1750, 1073, 1081, 1746, 1543, 936, 940, 1750, 1752, 1081, 1073, 2022, 1990, 1018, 1022, 2067, 2047, 1009, 1013, 1247, 1249, 6, 1, 1606, 1671, 1106, 925, 1711, 1717, 1106, 1001, 1539, 1545, 992, 925, 1910, 1912, 1106, 1085, 8, 12, 137, 142, 59, 66, 234, 321, 124, 165, 234, 436, 375, 273, 309, 313, 442, 337, 636, 640, 486, 493, 263, 303, 524, 531, 589, 630, 660, 667, 57, 62, 682, 25, 35, 39, 660, 842, 47, 55, 843, 117, 54, 58, 1376, 1340, 273, 277, 5, 1528, 109, 117, 1587, 1495, 600, 604, 1595, 297, 565, 596, 1824, 1833, 355, 387, 1873, 1874, 80, 82, 1874, 1876, 90, 80, 1878, 1880, 90, 77, 1880, 1893, 77, 90, 1893, 1895, 90, 77, 1868, 1874, 83, 90, 1876, 1878, 80, 90, 86, 90, 230, 137, 98, 102, 230, 123, 110, 114, 230, 123, 192, 196, 162, 119, 85, 86, 137, 230, 83, 85, 230, 137, 90, 91, 137, 230, 91, 93, 230, 137, 97, 98, 123, 230, 95, 97, 230, 123, 102, 103, 123, 230, 109, 110, 123, 230, 103, 109, 230, 123, 196, 197, 119, 162, 197, 199, 162, 119, 205, 207, 153, 119, 969, 973, 580, 192, 985, 989, 580, 84, 993, 997, 580, 84, 1108, 1112, 465, 84, 968, 969, 192, 580, 966, 968, 580, 192, 973, 974, 192, 580, 974, 980, 580, 192, 984, 985, 84, 580, 982, 984, 580, 84, 989, 990, 84, 580, 992, 993, 84, 580, 990, 992, 580, 84, 1112, 1113, 84, 465, 1113, 1115, 465, 84, 1129, 1131, 465, 84, 803, 807, 470, 57, 819, 823, 470, 57, 827, 831, 470, 57, 941, 945, 580, 192, 802, 803, 57, 470, 800, 802, 470, 57, 807, 808, 57, 470, 808, 810, 470, 57, 818, 819, 57, 470, 816, 818, 470, 57, 823, 824, 57, 470, 826, 827, 57, 470, 824, 826, 470, 57, 945, 946, 192, 580, 946, 948, 580, 192, 63, 65, 490, 323, 73, 122, 234, 490, 71, 73, 490, 234, 124, 125, 488, 490, 122, 124, 490, 234, 167, 176, 234, 346, 165, 167, 436, 234, 57, 63, 348, 490, 65, 66, 323, 490, 70, 71, 234, 490, 66, 70, 490, 234, 1518, 1519, 358, 388, 1519, 1521, 455, 358, 1523, 1525, 455, 355, 1525, 1599, 355, 455, 1599, 1601, 530, 355, 1601, 1602, 355, 530, 1602, 1604, 530, 355, 1822, 1824, 527, 355, 1513, 1519, 389, 455, 1604, 1822, 355, 527, 1361, 1362, 363, 391, 1362, 1364, 406, 363, 1368, 1388, 360, 406, 1388, 1390, 406, 360, 1356, 1362, 392, 406, 1364, 1366, 363, 406, 1390, 1392, 360, 390, 902, 908, 580, 192, 922, 928, 580, 192, 940, 941, 192, 580, 934, 940, 580, 192, 1061, 1067, 465, 84, 901, 902, 192, 580, 897, 901, 580, 192, 908, 909, 192, 580, 909, 913, 580, 192, 921, 922, 192, 580, 917, 921, 580, 192, 928, 929, 192, 580, 933, 934, 192, 580, 929, 933, 580, 192, 1067, 1068, 84, 465, 1068, 1072, 465, 84, 1084, 1088, 465, 84, 858, 860, 716, 664, 866, 868, 714, 623, 876, 1021, 584, 714, 874, 876, 714, 584, 1023, 1032, 584, 662, 1021, 1023, 714, 584, 860, 866, 664, 714, 868, 869, 623, 714, 873, 874, 584, 714, 869, 873, 714, 584, 46, 47, 688, 695, 47, 49, 729, 688, 53, 131, 685, 729, 133, 142, 685, 694, 131, 133, 729, 685, 8, 38, 47, 120, 17, 19, 158, 137, 75, 77, 230, 163, 119, 121, 230, 119, 121, 181, 119, 230, 183, 192, 119, 162, 181, 183, 230, 119, 201, 203, 156, 119, 214, 216, 153, 126, 16, 17, 137, 158, 12, 16, 158, 137, 77, 78, 163, 230, 82, 83, 163, 230, 78, 82, 230, 163, 8, 104, 130, 135, 199, 201, 119, 156, 207, 208, 119, 131, 208, 212, 131, 119, 212, 7, 119, 125, 207, 214, 133, 153, 631, 635, 585, 197, 647, 651, 585, 73, 655, 659, 585, 73, 810, 811, 57, 470, 815, 816, 57, 470, 811, 815, 470, 57, 630, 631, 197, 585, 628, 630, 585, 197, 635, 636, 197, 585, 636, 642, 585, 197, 646, 647, 73, 585, 644, 646, 585, 73, 651, 652, 73, 585, 654, 655, 73, 585, 652, 654, 585, 73, 831, 832, 57, 470, 832, 834, 470, 57, 564, 570, 585, 263, 584, 590, 585, 263, 596, 602, 585, 263, 764, 770, 470, 57, 563, 564, 263, 585, 559, 563, 585, 263, 570, 571, 263, 585, 571, 575, 585, 263, 583, 584, 263, 585, 579, 583, 585, 263, 590, 591, 263, 585, 595, 596, 263, 585, 591, 595, 585, 263, 770, 771, 57, 470, 771, 775, 470, 57, 787, 791, 470, 57, 1704, 1706, 699, 599, 1708, 1710, 699, 597, 1701, 1704, 655, 699, 427, 428, 678, 689, 428, 430, 719, 678, 432, 434, 719, 675, 521, 523, 719, 667, 528, 530, 719, 632, 536, 538, 719, 589, 538, 724, 589, 719, 726, 735, 589, 665, 724, 726, 719, 589, 422, 428, 690, 719, 530, 531, 632, 719, 535, 536, 589, 719, 531, 535, 719, 589, 461, 465, 475, 380, 473, 477, 475, 342, 481, 485, 475, 342, 551, 555, 585, 263, 611, 615, 585, 197, 627, 628, 197, 585, 623, 627, 585, 197, 751, 755, 503, 57, 779, 783, 470, 57, 799, 800, 57, 470, 795, 799, 470, 57, 889, 893, 580, 192, 948, 949, 192, 580, 949, 953, 580, 192, 965, 966, 192, 580, 961, 965, 580, 192, 1048, 1052, 500, 84, 1076, 1080, 465, 84, 1092, 1096, 465, 84, 1199, 1203, 441, 169, 460, 461, 380, 475, 458, 460, 475, 380, 465, 466, 380, 475, 466, 468, 475, 380, 472, 473, 342, 475, 470, 472, 475, 342, 477, 478, 342, 475, 480, 481, 342, 475, 478, 480, 475, 342, 550, 551, 263, 585, 548, 550, 585, 263, 555, 556, 263, 585, 558, 559, 263, 585, 556, 558, 585, 263, 575, 576, 263, 585, 578, 579, 263, 585, 576, 578, 585, 263, 610, 611, 197, 585, 608, 610, 585, 197, 615, 616, 197, 585, 622, 623, 197, 585, 616, 622, 585, 197, 755, 756, 57, 503, 756, 758, 503, 57, 775, 776, 57, 470, 778, 779, 57, 470, 776, 778, 470, 57, 783, 784, 57, 470, 786, 787, 57, 470, 784, 786, 470, 57, 791, 792, 57, 470, 794, 795, 57, 470, 792, 794, 470, 57, 888, 889, 192, 580, 886, 888, 580, 192, 893, 894, 192, 580, 896, 897, 192, 580, 894, 896, 580, 192, 913, 914, 192, 580, 916, 917, 192, 580, 914, 916, 580, 192, 953, 954, 192, 580, 960, 961, 192, 580, 954, 960, 580, 192, 1052, 1053, 84, 500, 1053, 1055, 500, 84, 1072, 1073, 84, 465, 1075, 1076, 84, 465, 1073, 1075, 465, 84, 1080, 1081, 84, 465, 1083, 1084, 84, 465, 1081, 1083, 465, 84, 1088, 1089, 84, 465, 1091, 1092, 84, 465, 1089, 1091, 465, 84, 1096, 1097, 84, 465, 1097, 1099, 465, 84, 1203, 1204, 169, 441, 1204, 1206, 441, 169, 1212, 1214, 411, 169, 360, 361, 383, 403, 361, 363, 426, 383, 392, 393, 199, 206, 393, 395, 208, 199, 399, 502, 197, 208, 397, 399, 208, 197, 367, 458, 380, 426, 454, 456, 477, 448, 490, 492, 475, 305, 500, 548, 263, 475, 498, 500, 475, 263, 502, 504, 261, 197, 504, 505, 197, 261, 505, 507, 261, 197, 540, 542, 585, 504, 664, 666, 585, 64, 672, 674, 585, 57, 742, 743, 556, 585, 740, 742, 585, 57, 760, 762, 473, 57, 834, 839, 57, 71, 836, 838, 470, 192, 878, 880, 580, 501, 997, 1037, 84, 580, 1039, 1048, 84, 500, 1037, 1039, 580, 84, 1057, 1059, 468, 84, 1107, 1108, 84, 465, 1105, 1107, 465, 84, 1121, 1123, 465, 84, 1137, 1139, 465, 169, 1144, 1188, 169, 465, 1190, 1199, 169, 441, 1188, 1190, 465, 169, 1208, 1210, 414, 169, 1214, 1219, 169, 334, 1216, 1218, 411, 365, 1322, 1331, 365, 393, 355, 361, 404, 426, 390, 393, 207, 208, 456, 458, 448, 475, 468, 470, 380, 475, 492, 493, 305, 475, 497, 498, 263, 475, 493, 497, 475, 263, 507, 508, 197, 261, 512, 603, 197, 261, 508, 512, 261, 197, 542, 543, 504, 585, 547, 548, 504, 585, 543, 547, 585, 504, 602, 603, 263, 585, 607, 608, 197, 585, 603, 607, 585, 197, 642, 644, 197, 585, 666, 667, 64, 585, 671, 672, 57, 585, 667, 671, 585, 57, 758, 760, 57, 473, 762, 764, 57, 470, 834, 836, 194, 470, 880, 881, 501, 580, 885, 886, 501, 580, 881, 885, 580, 501, 980, 982, 192, 580, 1055, 1057, 84, 468, 1059, 1060, 467, 468, 1059, 1061, 84, 465, 1099, 1100, 84, 465, 1104, 1105, 84, 465, 1100, 1104, 465, 84, 1115, 1116, 84, 465, 1120, 1121, 84, 465, 1116, 1120, 465, 84, 1123, 1124, 84, 465, 1128, 1129, 84, 465, 1124, 1128, 465, 84, 1131, 1132, 169, 465, 1136, 1137, 169, 465, 1132, 1136, 465, 169, 1139, 1140, 169, 465, 1140, 1144, 465, 169, 1206, 1208, 169, 414, 1210, 1211, 413, 414, 1210, 1212, 169, 411, 494, 377, 302, 306, 604, 617, 260, 296, 668, 117, 61, 65, 970, 972, 251, 202, 983, 986, 192, 201, 986, 988, 251, 192, 996, 1109, 189, 251, 1111, 1130, 189, 200, 1109, 1111, 251, 189, 967, 970, 202, 251, 972, 975, 202, 251, 975, 979, 251, 202, 814, 833, 194, 203, 658, 812, 194, 256, 903, 907, 468, 372, 923, 927, 468, 337, 935, 939, 468, 337, 1051, 1062, 255, 443, 1062, 1066, 443, 255, 900, 903, 372, 468, 898, 900, 468, 372, 907, 910, 372, 468, 910, 912, 468, 372, 920, 923, 337, 468, 918, 920, 468, 337, 927, 930, 337, 468, 932, 935, 337, 468, 930, 932, 468, 337, 1066, 1069, 255, 443, 1069, 1071, 443, 255, 1085, 1087, 414, 255, 645, 648, 197, 204, 648, 650, 256, 197, 656, 658, 256, 194, 812, 814, 256, 194, 634, 637, 205, 256, 637, 641, 256, 205, 565, 569, 473, 377, 585, 589, 473, 340, 597, 601, 473, 340, 765, 769, 446, 260, 562, 565, 377, 473, 560, 562, 473, 377, 569, 572, 377, 473, 572, 574, 473, 377, 582, 585, 340, 473, 580, 582, 473, 340, 589, 592, 340, 473, 594, 597, 340, 473, 592, 594, 473, 340, 769, 772, 260, 446, 772, 774, 446, 260, 788, 790, 419, 260, 471, 474, 380, 401, 474, 476, 424, 380, 482, 484, 424, 377, 484, 560, 377, 424, 552, 554, 475, 447, 612, 614, 473, 298, 624, 626, 473, 260, 626, 752, 260, 473, 754, 765, 260, 446, 752, 754, 473, 260, 780, 782, 422, 260, 790, 801, 260, 338, 796, 798, 419, 372, 890, 892, 470, 444, 950, 952, 468, 289, 962, 964, 468, 255, 1077, 1079, 417, 255, 1093, 1095, 414, 367, 1200, 1202, 414, 367, 464, 474, 402, 424, 554, 557, 474, 475, 554, 560, 447, 473, 574, 580, 377, 473, 614, 617, 298, 473, 621, 624, 260, 473, 617, 621, 473, 260, 774, 780, 260, 422, 782, 785, 421, 422, 782, 788, 260, 419, 892, 898, 444, 468, 912, 918, 372, 468, 952, 955, 289, 468, 959, 962, 255, 468, 955, 959, 468, 255, 1071, 1077, 255, 417, 1079, 1085, 255, 414, 1087, 1093, 369, 414, 1541, 1449, 952, 956, 1608, 1615, 1006, 1041, 1632, 1639, 939, 946, 1636, 1638, 1002, 948, 1644, 1646, 1002, 939, 1646, 1655, 939, 1002, 1632, 1745, 930, 937, 1655, 1657, 1002, 939, 1626, 1627, 974, 1002, 1627, 1631, 1002, 974, 1638, 1639, 948, 1002, 1643, 1644, 939, 1002, 1639, 1643, 1002, 939, 1612, 1614, 1081, 1043, 1622, 1647, 1006, 1081, 1620, 1622, 1081, 1006, 1649, 1650, 1006, 1062, 1647, 1649, 1081, 1006, 1715, 1720, 1075, 1078, 1713, 1715, 1081, 1075, 1614, 1615, 1043, 1081, 1619, 1620, 1006, 1081, 1615, 1619, 1081, 1006, 1420, 1421, 1095, 1098, 1421, 1423, 1102, 1095, 1425, 1427, 1102, 1092, 1427, 1915, 1092, 1102, 1915, 1917, 1102, 1092, 712, 714, 848, 1049, 730, 732, 719, 1049, 847, 852, 1049, 716, 848, 1745, 847, 866, 998, 1009, 1049, 841, 1145, 1160, 579, 711, 1258, 1308, 1049, 462, 1194, 1196, 465, 1049, 1326, 1328, 411, 1049, 1343, 1352, 1049, 408, 999, 1445, 925, 960, 1459, 1007, 913, 917, 1493, 1294, 607, 611, 1463, 1551, 901, 907, 1565, 1473, 875, 879, 1509, 1535, 530, 955, 1581, 1585, 568, 601, 1585, 1591, 701, 568, 1681, 1685, 830, 869, 1685, 1691, 701, 830, 1308, 1310, 462, 1049, 1009, 1011, 841, 1049, 1160, 1162, 711, 579, 1445, 1451, 457, 925, 1551, 1557, 530, 901, 852, 998, 841, 1049, 1027, 1029, 714, 1049, 1145, 1176, 1049, 576, 1176, 1178, 576, 1049, 618, 496, 295, 299, 956, 806, 286, 290, 919, 924, 372, 396, 924, 926, 417, 372, 938, 1063, 369, 417, 936, 938, 417, 369, 1065, 1086, 369, 395, 1063, 1065, 417, 369, 906, 924, 397, 417, 581, 586, 377, 399, 586, 588, 422, 377, 600, 766, 374, 422, 598, 600, 422, 374, 768, 789, 374, 398, 766, 768, 422, 374, 568, 586, 400, 422, 532, 444, 629, 633, 1001, 1003, 902, 962, 1148, 1150, 841, 962, 1008, 1013, 845, 962, 1166, 1168, 711, 962, 1259, 1280, 575, 708, 1259, 1296, 962, 572, 1346, 1441, 532, 962, 1261, 1457, 901, 914, 1471, 1266, 882, 886, 1559, 1563, 833, 876, 1563, 1569, 703, 833, 1280, 1282, 708, 575, 1457, 1463, 532, 901, 1810, 1812, 773, 1071, 1828, 1830, 527, 1071, 1929, 1953, 97, 524, 1988, 1939, 1025, 1029, 2016, 2020, 812, 1019, 2020, 2026, 519, 812, 1953, 1955, 524, 97, 153, 155, 513, 750, 175, 218, 433, 750, 218, 259, 229, 433, 335, 297, 643, 647, 418, 424, 799, 678, 436, 440, 592, 637, 440, 446, 799, 592, 259, 261, 433, 229, 275, 277, 226, 1107, 351, 357, 477, 383, 369, 373, 225, 310, 373, 379, 477, 225, 13, 7, 141, 145, 1411, 1337, 178, 186, 212, 7, 127, 131, 87, 89, 158, 150, 99, 101, 156, 137, 8, 211, 124, 128, 111, 113, 156, 130, 113, 193, 130, 156, 195, 206, 130, 148, 193, 195, 156, 130, 89, 99, 150, 156, 101, 104, 137, 156, 108, 111, 130, 156, 104, 108, 156, 130, 1616, 1606, 1040, 1044, 1640, 1543, 945, 949, 1270, 1279, 916, 736, 1290, 1453, 705, 916, 1465, 1469, 836, 883, 1469, 1475, 705, 836, 1781, 1783, 824, 1071, 1796, 1798, 699, 1071, 1941, 1943, 816, 1069, 1982, 1986, 815, 1026, 1986, 1992, 521, 815, 2061, 2065, 805, 1010, 2065, 2071, 3, 805, 225, 227, 747, 683, 307, 351, 383, 428, 870, 738, 620, 624, 862, 869, 584, 621, 1296, 1298, 572, 962, 1298, 1307, 962, 496, 1487, 1491, 571, 608, 1491, 1497, 703, 571, 247, 249, 509, 681, 249, 258, 681, 452, 265, 267, 433, 681, 255, 129, 508, 517, 303, 317, 479, 681, 329, 333, 595, 644, 333, 339, 479, 595, 67, 45, 320, 324, 939, 950, 337, 468, 942, 955, 255, 287, 1370, 1374, 185, 274, 1374, 1380, 164, 185, 1403, 1405, 179, 358, 105, 7, 134, 138, 1855, 4, 112, 264, 27, 29, 29, 121, 676, 680, 28, 36, 680, 686, 8, 28, 1253, 1255, 6, 80, 29, 30, 18, 29, 513, 517, 1107, 590, 516, 517, 967, 968, 1773, 1606, 993, 1007, 687, 688, 11, 26, 690, 692, 21, 15, 690, 691, 16, 17, 700, 701, 1051, 1067, 702, 704, 1051, 848, 703, 704, 1049, 1050, 706, 712, 1049, 848, 1237, 1238, 13, 22, 1251, 1253, 80, 6, 1251, 1252, 9, 10, 1255, 1257, 80, 3, 1255, 1256, 5, 6, 1429, 1431, 1049, 457, 1430, 1431, 978, 1047, 1432, 1433, 1049, 1065, 1440, 1445, 978, 457, 1447, 1449, 965, 931, 1448, 1449, 958, 964, 1535, 1537, 955, 530, 1536, 1537, 921, 954, 1538, 1539, 955, 975, 1546, 1551, 921, 530, 1545, 1606, 925, 992, 1553, 1555, 912, 902, 1554, 1555, 905, 911, 1671, 1672, 925, 929, 1673, 1675, 925, 902, 1673, 1674, 905, 924, 1676, 1678, 928, 701, 1677, 1678, 892, 927, 1671, 1711, 1001, 1106, 1680, 1685, 892, 701, 1676, 850, 901, 926, 1687, 1689, 874, 841, 1688, 1689, 867, 873, 1721, 1726, 1001, 1061, 1727, 1729, 1037, 1007, 1728, 1729, 1035, 1036, 1735, 1737, 1001, 998, 1735, 1736, 999, 1000, 1739, 1741, 993, 984, 1739, 1740, 986, 987, 1733, 1742, 939, 971, 1743, 1745, 939, 841, 1743, 1744, 867, 938, 1746, 1748, 942, 852, 1747, 1748, 935, 941, 1752, 1754, 1073, 1077, 1755, 1757, 1073, 994, 1756, 1757, 1071, 1072, 1717, 1910, 1085, 1106, 1759, 1765, 1071, 994, 1767, 1768, 982, 994, 1923, 1928, 1085, 1086, 2011, 2013, 1085, 519, 2012, 2013, 1056, 1084, 2015, 2020, 1056, 519, 2022, 2024, 1024, 820, 2023, 2024, 1017, 1023, 2036, 2038, 1090, 1096, 2039, 2041, 1090, 3, 2040, 2041, 1088, 1089, 2043, 2058, 1088, 3, 2057, 2058, 1053, 1087, 2060, 2065, 1053, 3, 2067, 2069, 1015, 820, 2068, 2069, 1008, 1014, 2072, 2073, 758, 803, 2007, 4, 21, 110, 2076, 2078, 1008, 757, 2076, 2077, 759, 760, 8, 10, 144, 33, 9, 10, 43, 143, 5, 7, 250, 48, 6, 7, 147, 220, 11, 12, 144, 158, 19, 83, 137, 158, 21, 27, 121, 29, 43, 45, 688, 864, 44, 45, 518, 686, 2, 4, 1107, 20, 3, 45, 326, 492, 59, 61, 323, 230, 60, 61, 233, 322, 62, 63, 323, 347, 115, 117, 119, 48, 116, 117, 67, 118, 118, 119, 119, 122, 127, 129, 653, 487, 127, 128, 489, 490, 2076, 1820, 802, 820, 135, 137, 859, 729, 135, 136, 752, 753, 139, 141, 859, 726, 139, 140, 728, 729, 143, 145, 685, 747, 144, 145, 683, 684, 143, 153, 750, 513, 155, 156, 485, 513, 169, 171, 750, 436, 169, 170, 453, 454, 173, 175, 750, 433, 173, 174, 435, 436, 177, 179, 319, 264, 178, 179, 317, 318, 185, 187, 234, 230, 185, 186, 231, 232, 189, 191, 222, 215, 189, 190, 217, 218, 1746, 710, 865, 931, 218, 219, 863, 864, 147, 225, 683, 747, 227, 228, 724, 747, 261, 262, 431, 433, 277, 278, 213, 226, 288, 290, 1107, 153, 288, 289, 159, 160, 292, 381, 1107, 151, 292, 293, 152, 153, 304, 305, 383, 430, 307, 308, 429, 430, 312, 313, 692, 723, 315, 316, 722, 723, 315, 321, 692, 721, 323, 325, 681, 721, 324, 325, 678, 680, 346, 347, 449, 479, 349, 351, 449, 477, 349, 350, 478, 479, 357, 359, 383, 477, 358, 359, 344, 381, 368, 373, 344, 477, 375, 377, 315, 264, 376, 377, 308, 314, 380, 381, 199, 223, 383, 7, 222, 235, 383, 384, 211, 212, 383, 386, 250, 210, 385, 386, 221, 249, 413, 414, 744, 801, 416, 418, 744, 799, 416, 417, 800, 801, 424, 426, 678, 799, 425, 426, 669, 676, 435, 440, 669, 799, 442, 444, 642, 596, 443, 444, 635, 641, 447, 448, 505, 590, 450, 452, 565, 560, 450, 451, 561, 562, 486, 488, 305, 261, 487, 488, 262, 304, 489, 490, 305, 341, 524, 526, 632, 585, 525, 526, 588, 631, 527, 528, 632, 666, 660, 662, 64, 8, 661, 662, 45, 63, 663, 664, 64, 72, 675, 680, 45, 8, 674, 740, 57, 585, 682, 684, 41, 33, 683, 684, 34, 40, 714, 715, 797, 848, 728, 730, 1049, 719, 728, 729, 742, 743, 732, 734, 1049, 716, 732, 733, 718, 719, 840, 842, 57, 33, 840, 841, 34, 56, 843, 845, 60, 48, 844, 845, 53, 59, 851, 852, 741, 841, 854, 856, 823, 794, 854, 855, 795, 796, 1011, 1012, 792, 841, 1025, 1027, 1049, 714, 1025, 1026, 739, 740, 1029, 1031, 1049, 711, 1029, 1030, 713, 714, 1033, 1035, 619, 596, 1034, 1035, 617, 618, 1041, 1043, 584, 580, 1041, 1042, 581, 582, 1045, 1047, 565, 550, 1045, 1046, 552, 553, 1162, 1163, 709, 711, 1178, 1179, 548, 576, 1192, 1194, 1049, 465, 1192, 1193, 497, 498, 1196, 1198, 1049, 462, 1196, 1197, 464, 465, 1220, 1222, 283, 264, 1221, 1222, 281, 282, 1225, 1227, 169, 166, 1225, 1226, 167, 168, 1229, 1235, 80, 22, 1310, 1311, 460, 462, 1324, 1326, 1049, 411, 1324, 1325, 438, 439, 1328, 1330, 1049, 408, 1328, 1329, 410, 411, 1332, 1334, 365, 164, 1333, 1334, 363, 364, 1336, 1342, 363, 164, 1347, 1348, 437, 459, 1350, 1352, 437, 457, 1350, 1351, 458, 459, 1358, 1360, 363, 164, 1359, 1360, 332, 361, 1369, 1374, 332, 164, 1376, 1378, 279, 264, 1377, 1378, 272, 278, 1381, 1382, 175, 183, 1332, 1130, 165, 170, 1385, 1387, 178, 174, 1385, 1386, 176, 177, 1393, 1395, 360, 179, 1394, 1395, 358, 359, 1397, 1403, 358, 179, 1405, 1406, 172, 179, 1504, 1505, 493, 532, 1507, 1509, 493, 530, 1507, 1508, 531, 532, 1515, 1517, 358, 108, 1516, 1517, 329, 356, 1526, 1528, 329, 108, 1530, 1532, 270, 264, 1531, 1532, 268, 269, 1576, 1577, 657, 703, 1579, 1580, 702, 703, 1579, 1585, 657, 701, 1587, 1589, 606, 596, 1588, 1589, 599, 605, 1592, 1593, 538, 566, 1595, 1597, 599, 540, 1595, 1596, 541, 542, 1692, 1693, 732, 828, 1695, 1697, 823, 779, 1695, 1696, 780, 781, 1703, 1704, 599, 654, 1783, 1784, 777, 824, 1794, 1796, 1071, 699, 1794, 1795, 730, 731, 1798, 1799, 698, 699, 1800, 1801, 774, 776, 1804, 1810, 1071, 773, 1804, 1805, 775, 776, 1812, 1813, 771, 773, 1826, 1828, 1071, 527, 1826, 1827, 536, 537, 1830, 1832, 1071, 524, 1830, 1831, 526, 527, 1834, 1836, 355, 113, 1835, 1836, 353, 354, 1838, 1844, 353, 113, 1974, 1903, 93, 98, 1846, 1847, 106, 113, 1859, 1860, 101, 110, 1862, 1864, 109, 103, 1862, 1863, 104, 105, 1870, 1872, 80, 3, 1871, 1872, 69, 78, 1881, 1883, 69, 3, 1885, 1887, 51, 48, 1886, 1887, 49, 50, 1890, 1892, 109, 100, 1890, 1891, 102, 103, 1897, 1899, 109, 90, 1897, 1898, 99, 100, 1901, 1903, 109, 87, 1901, 1902, 89, 90, 1895, 1904, 77, 81, 1905, 1906, 49, 75, 1905, 1908, 77, 48, 1907, 1908, 74, 76, 1955, 1956, 522, 524, 1929, 1969, 74, 94, 39, 45, 1107, 264, 40, 41, 688, 864, 352, 353, 404, 428, 355, 356, 427, 428, 363, 365, 383, 426, 364, 365, 380, 382, 387, 388, 207, 210, 390, 391, 209, 210, 395, 397, 199, 208, 396, 397, 197, 198, 453, 454, 448, 477, 456, 457, 476, 477, 469, 470, 342, 378, 485, 490, 342, 475, 494, 496, 308, 264, 495, 496, 301, 307, 501, 502, 247, 261, 509, 511, 250, 246, 509, 510, 248, 249, 539, 540, 504, 585, 544, 546, 565, 558, 544, 545, 559, 560, 604, 606, 298, 256, 605, 606, 259, 297, 609, 612, 298, 339, 643, 644, 73, 195, 659, 664, 73, 585, 668, 670, 67, 58, 669, 670, 60, 66, 758, 759, 502, 503, 762, 763, 472, 473, 835, 836, 192, 193, 877, 878, 501, 580, 882, 884, 565, 553, 882, 883, 554, 555, 981, 982, 84, 190, 1039, 1040, 551, 580, 1055, 1056, 499, 500, 1087, 1098, 255, 335, 1101, 1103, 285, 264, 1102, 1103, 283, 284, 1117, 1119, 255, 251, 1117, 1118, 252, 253, 1125, 1127, 250, 236, 1125, 1126, 238, 239, 1133, 1135, 189, 170, 1134, 1135, 187, 188, 1141, 1143, 250, 170, 1141, 1142, 187, 236, 1190, 1191, 463, 465, 1206, 1207, 440, 441, 1202, 1213, 367, 394, 1214, 1216, 367, 411, 1215, 1216, 365, 366, 1218, 1320, 365, 411, 1131, 1224, 84, 166, 1322, 1323, 409, 411, 519, 698, 1051, 1106, 1417, 1419, 1095, 1106, 1418, 1419, 1066, 1093, 1428, 1433, 1066, 1106, 1435, 1437, 1049, 1106, 1436, 1437, 1046, 1048, 1439, 1606, 1046, 1106, 1534, 1539, 976, 992, 1541, 1543, 958, 931, 1542, 1543, 951, 957, 1608, 1610, 1043, 1002, 1609, 1610, 1005, 1042, 1611, 1612, 1043, 1063, 1632, 1634, 948, 926, 1633, 1634, 928, 947, 1635, 1636, 948, 973, 1651, 1653, 1039, 1007, 1652, 1653, 1037, 1038, 1659, 1661, 1006, 1002, 1659, 1660, 1003, 1004, 1663, 1665, 993, 987, 1663, 1664, 989, 990, 1657, 1666, 939, 972, 1667, 1669, 944, 940, 1668, 1669, 942, 943, 1717, 1719, 1001, 1081, 1717, 1718, 1082, 1083, 1721, 1723, 1075, 1081, 1722, 1723, 1073, 1074, 1671, 1731, 939, 998, 1733, 1734, 985, 998, 1752, 1753, 1080, 1081, 1912, 1914, 1085, 1104, 1912, 1913, 1105, 1106, 1919, 1921, 1085, 1102, 1919, 1920, 1103, 1104, 1917, 1922, 1092, 1097, 1923, 1925, 1092, 1102, 1924, 1925, 1090, 1091, 1927, 2034, 1090, 1102, 1249, 2080, 1, 2, 2036, 2037, 1101, 1102, 702, 707, 851, 979, 708, 710, 967, 852, 709, 710, 965, 966, 714, 723, 1049, 743, 716, 718, 851, 848, 716, 717, 849, 850, 720, 722, 823, 796, 720, 721, 798, 799, 848, 850, 930, 841, 849, 850, 846, 900, 1003, 1004, 898, 902, 1011, 1020, 1049, 740, 1013, 1015, 962, 841, 1013, 1014, 844, 845, 1017, 1019, 823, 791, 1017, 1018, 793, 794, 1150, 1151, 789, 841, 1164, 1166, 962, 711, 1164, 1165, 737, 738, 1168, 1170, 962, 708, 1168, 1169, 710, 711, 1162, 1171, 579, 661, 1172, 1174, 617, 596, 1173, 1174, 615, 616, 1178, 1187, 1049, 498, 1180, 1182, 579, 576, 1180, 1181, 577, 578, 1184, 1186, 565, 547, 1184, 1185, 549, 550, 1282, 1283, 706, 708, 1298, 1299, 545, 572, 1310, 1319, 1049, 439, 1312, 1314, 962, 462, 1312, 1313, 495, 496, 1316, 1318, 962, 459, 1316, 1317, 461, 462, 1344, 1346, 962, 459, 1345, 1346, 494, 532, 1441, 1443, 962, 532, 1442, 1443, 923, 961, 1444, 1445, 962, 977, 1452, 1457, 923, 532, 1451, 1509, 955, 457, 1459, 1461, 919, 902, 1460, 1461, 912, 918, 1482, 1483, 659, 705, 1485, 1491, 659, 703, 1485, 1486, 704, 705, 1493, 1495, 613, 596, 1494, 1495, 606, 612, 1498, 1499, 539, 569, 1501, 1503, 565, 542, 1501, 1502, 543, 544, 1547, 1549, 909, 703, 1548, 1549, 894, 908, 1550, 1551, 909, 920, 1558, 1563, 894, 703, 1557, 1593, 901, 530, 1565, 1567, 881, 841, 1566, 1567, 874, 880, 1570, 1571, 733, 831, 1573, 1575, 823, 781, 1573, 1574, 782, 783, 1581, 1583, 603, 566, 1582, 1583, 567, 602, 1584, 1585, 603, 656, 1591, 1593, 568, 701, 1681, 1683, 871, 828, 1682, 1683, 829, 870, 1684, 1685, 871, 891, 1691, 1693, 830, 701, 459, 462, 402, 426, 464, 467, 425, 426, 476, 482, 380, 424, 479, 482, 377, 379, 549, 552, 447, 475, 577, 580, 340, 375, 601, 612, 340, 473, 618, 620, 301, 264, 619, 620, 294, 300, 754, 757, 471, 473, 774, 777, 445, 446, 790, 796, 374, 419, 793, 796, 372, 373, 887, 890, 444, 470, 892, 895, 469, 470, 915, 918, 337, 370, 956, 958, 292, 264, 957, 958, 285, 291, 1051, 1054, 466, 468, 1071, 1074, 442, 443, 1079, 1082, 416, 417, 1090, 1093, 367, 368, 1095, 1200, 367, 414, 1202, 1205, 412, 414, 419, 420, 690, 721, 422, 423, 720, 721, 430, 432, 678, 719, 431, 432, 675, 677, 434, 521, 675, 719, 520, 521, 667, 674, 523, 528, 667, 719, 532, 534, 635, 596, 533, 534, 628, 634, 726, 727, 717, 719, 1003, 1008, 962, 845, 999, 1001, 962, 902, 1005, 1007, 919, 902, 1005, 1006, 903, 904, 1150, 1159, 962, 738, 1146, 1148, 962, 841, 1152, 1154, 890, 841, 1152, 1153, 842, 843, 1156, 1158, 823, 788, 1156, 1157, 790, 791, 1261, 1268, 916, 837, 1261, 1262, 899, 900, 1270, 1271, 786, 837, 1284, 1286, 916, 708, 1284, 1285, 735, 736, 1288, 1290, 916, 705, 1288, 1289, 707, 708, 1453, 1455, 916, 705, 1454, 1455, 896, 915, 1456, 1457, 916, 922, 1464, 1469, 896, 705, 1463, 1499, 909, 532, 1471, 1473, 888, 841, 1472, 1473, 881, 887, 1476, 1477, 734, 834, 1479, 1481, 823, 783, 1479, 1480, 784, 785, 1559, 1561, 878, 831, 1560, 1561, 832, 877, 1562, 1563, 878, 893, 1569, 1571, 833, 703, 1698, 1699, 655, 701, 1701, 1702, 700, 701, 1706, 1708, 599, 699, 1707, 1708, 597, 598, 1710, 1793, 597, 699, 1755, 1760, 997, 1060, 1761, 1763, 1035, 1007, 1762, 1763, 1033, 1034, 1767, 1781, 1071, 824, 1769, 1771, 997, 994, 1769, 1770, 995, 996, 1773, 1775, 1033, 981, 1773, 1774, 983, 984, 1789, 517, 823, 852, 1807, 1809, 1033, 822, 1807, 1808, 980, 981, 1812, 1821, 1071, 537, 1814, 1816, 1033, 773, 1814, 1815, 821, 822, 1818, 1820, 1033, 770, 1818, 1819, 772, 773, 1929, 1930, 1071, 1076, 1931, 1933, 1071, 816, 1932, 1933, 1069, 1070, 1935, 1941, 1069, 816, 1943, 1944, 768, 816, 1929, 2005, 1085, 48, 1957, 1959, 1069, 524, 1957, 1958, 534, 535, 1961, 1963, 1069, 521, 1961, 1962, 523, 524, 1977, 1979, 1069, 521, 1978, 1979, 1058, 1068, 1981, 1986, 1058, 521, 1988, 1990, 1031, 820, 1989, 1990, 1024, 1030, 1993, 1994, 533, 813, 1996, 1998, 802, 765, 1996, 1997, 766, 767, 2016, 2018, 1021, 810, 2017, 2018, 811, 1020, 2019, 2020, 1021, 1055, 2026, 2028, 812, 519, 143, 148, 516, 673, 149, 151, 653, 517, 150, 151, 651, 652, 155, 164, 750, 454, 157, 159, 516, 513, 157, 158, 514, 515, 161, 163, 508, 484, 161, 162, 486, 487, 227, 236, 683, 693, 237, 239, 683, 509, 238, 239, 681, 682, 241, 247, 681, 509, 249, 250, 482, 509, 218, 275, 1107, 226, 263, 265, 681, 433, 263, 264, 451, 452, 267, 269, 681, 430, 267, 268, 432, 433, 298, 299, 450, 481, 301, 303, 450, 479, 301, 302, 480, 481, 317, 319, 681, 479, 318, 319, 671, 679, 320, 321, 681, 691, 328, 333, 671, 479, 327, 418, 678, 721, 335, 337, 649, 596, 336, 337, 642, 648, 340, 341, 506, 593, 343, 345, 565, 562, 343, 344, 563, 564, 436, 438, 639, 590, 437, 438, 591, 638, 439, 440, 639, 668, 446, 517, 592, 799, 561, 566, 400, 424, 568, 573, 423, 424, 588, 598, 377, 422, 593, 598, 374, 376, 768, 773, 420, 422, 261, 270, 229, 345, 271, 273, 317, 264, 272, 273, 315, 316, 277, 286, 1107, 160, 279, 281, 229, 226, 279, 280, 227, 228, 283, 285, 222, 212, 283, 284, 214, 215, 369, 371, 312, 223, 370, 371, 224, 311, 372, 373, 312, 343, 379, 381, 225, 477, 629, 632, 205, 256, 638, 640, 250, 244, 638, 639, 245, 246, 641, 648, 205, 256, 650, 656, 197, 256, 653, 656, 194, 196, 814, 817, 242, 256, 13, 15, 147, 138, 14, 15, 140, 146, 74, 75, 163, 230, 79, 81, 222, 218, 79, 80, 219, 220, 93, 95, 137, 230, 94, 95, 123, 136, 96, 99, 137, 149, 114, 119, 123, 230, 183, 184, 216, 230, 199, 200, 161, 162, 203, 205, 119, 153, 203, 204, 155, 156, 209, 211, 130, 120, 209, 210, 121, 129, 213, 214, 126, 132, 216, 287, 126, 153, 515, 517, 969, 1106, 1416, 1421, 1099, 1102, 1423, 1425, 1095, 1102, 1424, 1425, 1092, 1094, 1917, 1918, 1100, 1102, 1607, 1612, 1064, 1081, 1616, 1618, 1046, 1007, 1617, 1618, 1039, 1045, 1649, 1713, 1075, 1081, 1715, 1716, 1079, 1081, 1623, 1624, 974, 1002, 1628, 1630, 993, 990, 1628, 1629, 991, 992, 1631, 1636, 974, 1002, 1640, 1642, 951, 940, 1641, 1642, 944, 950, 1657, 1658, 988, 1002, 400, 448, 1107, 477, 401, 406, 861, 932, 408, 410, 857, 932, 409, 410, 854, 856, 412, 514, 854, 932, 1261, 1263, 840, 897, 1264, 1266, 890, 841, 1265, 1266, 888, 889, 1272, 1274, 840, 837, 1272, 1273, 838, 839, 1276, 1278, 823, 785, 1276, 1277, 787, 788, 1465, 1467, 885, 834, 1466, 1467, 835, 884, 1468, 1469, 885, 895, 1475, 1477, 836, 705, 1767, 1776, 827, 970, 1777, 1779, 935, 852, 1778, 1779, 933, 934, 1783, 1792, 1071, 731, 1785, 1787, 827, 824, 1785, 1786, 825, 826, 1789, 1791, 933, 776, 1789, 1790, 778, 779, 1798, 1801, 1071, 697, 1931, 1936, 819, 1059, 1937, 1939, 1033, 820, 1938, 1939, 1031, 1032, 1943, 1952, 1069, 535, 1945, 1947, 819, 816, 1945, 1946, 817, 818, 1949, 1951, 802, 767, 1949, 1950, 769, 770, 1982, 1984, 1028, 813, 1983, 1984, 814, 1027, 1985, 1986, 1028, 1057, 1992, 1994, 815, 521, 2039, 2044, 809, 1054, 2045, 2047, 1017, 820, 2046, 2047, 1015, 1016, 2050, 2052, 809, 806, 2050, 2051, 807, 808, 2054, 2056, 802, 760, 2054, 2055, 761, 762, 2061, 2063, 1012, 803, 2062, 2063, 804, 1011, 2064, 2065, 1012, 1052, 2071, 2073, 805, 3, 218, 220, 750, 862, 221, 223, 859, 751, 222, 223, 857, 858, 229, 231, 750, 747, 229, 230, 748, 749, 233, 235, 857, 723, 233, 234, 725, 726, 309, 311, 857, 723, 310, 311, 745, 801, 402, 404, 857, 801, 403, 404, 853, 855, 405, 406, 857, 860, 233, 141, 746, 751, 42, 47, 696, 729, 49, 51, 688, 729, 50, 51, 685, 687, 133, 134, 727, 729, 857, 858, 664, 716, 860, 861, 715, 716, 838, 886, 192, 470, 870, 872, 626, 596, 871, 872, 619, 625, 1023, 1024, 712, 714, 736, 738, 628, 596, 737, 738, 626, 627, 742, 751, 57, 503, 744, 746, 589, 585, 744, 745, 586, 587, 748, 750, 565, 555, 748, 749, 557, 558, 862, 864, 623, 580, 863, 864, 583, 622, 865, 866, 623, 663, 1282, 1291, 575, 660, 1292, 1294, 615, 596, 1293, 1294, 613, 614, 1300, 1302, 575, 572, 1300, 1301, 573, 574, 1304, 1306, 565, 544, 1304, 1305, 546, 547, 1487, 1489, 610, 569, 1488, 1489, 570, 609, 1490, 1491, 610, 658, 1497, 1499, 571, 703, 237, 242, 512, 672, 243, 245, 651, 517, 244, 245, 649, 650, 251, 253, 512, 509, 251, 252, 510, 511, 255, 257, 649, 481, 255, 256, 483, 484, 295, 297, 649, 481, 296, 297, 507, 564, 294, 303, 681, 430, 329, 331, 646, 593, 330, 331, 594, 645, 332, 333, 646, 670, 339, 341, 595, 479, 899, 904, 397, 419, 906, 911, 418, 419, 926, 936, 372, 417, 931, 936, 369, 371, 1065, 1070, 415, 417, 1353, 1354, 392, 408, 1356, 1357, 407, 408, 1365, 1366, 360, 362, 1390, 1391, 405, 406, 1510, 1511, 389, 457, 1513, 1514, 456, 457, 1521, 1523, 358, 455, 1522, 1523, 355, 357, 1598, 1599, 528, 530, 1604, 1605, 529, 530, 1824, 1825, 525, 527, 1999, 2000, 385, 521, 2002, 2003, 520, 521, 2002, 2005, 385, 519, 2007, 2009, 351, 3, 2008, 2009, 349, 350, 2027, 2028, 763, 810, 2031, 2033, 802, 762, 2031, 2032, 764, 765, 2039, 2049, 349, 806, 54, 55, 348, 492, 57, 58, 491, 492, 67, 69, 326, 264, 68, 69, 319, 325, 167, 168, 434, 436, 804, 806, 294, 264, 805, 806, 292, 293, 798, 898, 372, 419, 820, 822, 260, 256, 820, 821, 257, 258, 828, 830, 250, 241, 828, 829, 243, 244, 942, 944, 289, 251, 943, 944, 254, 288, 947, 950, 289, 336, 964, 1049, 255, 468, 976, 978, 250, 239, 976, 977, 240, 241, 979, 986, 202, 251, 988, 994, 192, 251, 991, 994, 189, 191, 1111, 1114, 237, 251, 1332, 1337, 250, 333, 1338, 1340, 281, 264, 1339, 1340, 279, 280, 1370, 1372, 276, 183, 1371, 1372, 184, 275, 1373, 1374, 276, 331, 1380, 1382, 185, 164, 1393, 1398, 182, 330, 1399, 1401, 272, 264, 1400, 1401, 270, 271, 1405, 1414, 358, 108, 1407, 1409, 182, 179, 1407, 1408, 180, 181, 1411, 1413, 250, 171, 1411, 1412, 173, 174, 1527, 1528, 250, 328, 84, 87, 150, 158, 89, 92, 157, 158, 105, 107, 140, 131, 106, 107, 133, 139, 195, 198, 154, 156, 1834, 1839, 116, 327, 1840, 1842, 268, 264, 1841, 1842, 266, 267, 1848, 1850, 116, 113, 1848, 1849, 114, 115, 1852, 1854, 109, 105, 1852, 1853, 107, 108, 1855, 1857, 266, 110, 1856, 1857, 111, 265, 1846, 1860, 353, 92, 1955, 1964, 97, 386, 1965, 1967, 353, 110, 1966, 1967, 351, 352, 1970, 1972, 97, 94, 1970, 1971, 95, 96, 1974, 1976, 109, 85, 1974, 1975, 86, 87, 2004, 2005, 109, 384, 1865, 1866, 83, 92, 1868, 1869, 91, 92, 1877, 1878, 77, 79, 1895, 1896, 88, 90, 21, 22, 32, 46, 23, 25, 43, 33, 24, 25, 41, 42, 29, 38, 121, 8, 31, 33, 32, 29, 31, 32, 30, 31, 35, 37, 21, 17, 35, 36, 19, 20, 676, 678, 38, 26, 677, 678, 27, 37, 679, 680, 38, 44, 686, 688, 28, 8, 1229, 1230, 25, 70, 1231, 1233, 53, 48, 1232, 1233, 51, 52, 1237, 1246, 80, 10, 1239, 1241, 25, 22, 1239, 1240, 23, 24, 1243, 1245, 21, 12, 1243, 1244, 14, 15, 1882, 1883, 21, 68, 693, 694, 1, 8, 696, 1247, 1, 6, 696, 697, 7, 8, 1249, 1250, 4, 6, 2079, 2080, 755, 757, 2083, 2084, 756, 757, 2083, 2085, 1, 754, 28, 29, 8, 18, 517, 519, 1106, 1107, 517, 708, 852, 967, 517, 518, 968, 969, 448, 513, 590, 1107, 688, 693, 8, 11, 692, 1243, 15, 21, 689, 690, 15, 16, 1883, 2007, 3, 21, 704, 706, 848, 1049, 704, 705, 1050, 1051, 1731, 1733, 998, 939, 1246, 1251, 10, 80, 1236, 1237, 10, 13, 1250, 1251, 6, 9, 1257, 1870, 3, 80, 1254, 1255, 3, 5, 1431, 1440, 457, 978, 1431, 1432, 1047, 1049, 1433, 1435, 1106, 1049, 1445, 1446, 977, 978, 1449, 1541, 956, 958, 1449, 1450, 964, 965, 1537, 1546, 530, 921, 1537, 1538, 954, 955, 1539, 1451, 953, 955, 1551, 1552, 920, 921, 1555, 1673, 902, 905, 1555, 1556, 911, 912, 1007, 1459, 902, 913, 1672, 1673, 924, 925, 1461, 1553, 902, 906, 1675, 999, 902, 925, 1678, 1680, 701, 892, 1678, 1679, 927, 928, 850, 1632, 926, 930, 1685, 1686, 891, 892, 1689, 1743, 841, 867, 1689, 1690, 873, 874, 1473, 1565, 841, 875, 1726, 1735, 1000, 1001, 1729, 1761, 1007, 1035, 1729, 1730, 1036, 1037, 1606, 1616, 1007, 1040, 1734, 1735, 998, 999, 1737, 1671, 998, 1001, 1741, 1773, 984, 993, 1738, 1739, 984, 986, 1742, 1743, 938, 939, 1567, 1687, 841, 868, 1745, 1632, 937, 939, 1748, 1777, 852, 935, 1748, 1749, 941, 942, 1757, 1759, 994, 1071, 1757, 1758, 1072, 1073, 1765, 1767, 994, 1071, 1766, 1767, 970, 982, 1928, 1929, 1076, 1085, 2005, 2011, 519, 1085, 2013, 2015, 519, 1056, 2013, 2014, 1084, 1085, 2020, 2021, 1055, 1056, 2024, 2045, 820, 1017, 2024, 2025, 1023, 1024, 1939, 1988, 820, 1025, 2038, 2039, 1054, 1090, 2041, 2043, 3, 1088, 2041, 2042, 1089, 1090, 2058, 2060, 3, 1053, 2058, 2059, 1087, 1088, 2065, 2066, 1052, 1053, 2069, 2076, 820, 1008, 2069, 2070, 1014, 1015, 2073, 2074, 3, 758, 2078, 2079, 757, 1008, 2075, 2076, 757, 759, 2047, 2067, 820, 1009, 4, 35, 20, 21, 1, 2, 20, 1107, 10, 23, 33, 43, 10, 11, 143, 144, 7, 13, 145, 147, 7, 79, 220, 222, 12, 8, 142, 144, 20, 21, 46, 121, 38, 209, 120, 121, 38, 660, 8, 47, 45, 54, 492, 518, 45, 46, 686, 688, 45, 67, 324, 326, 61, 74, 230, 233, 61, 62, 322, 323, 66, 59, 321, 323, 176, 185, 232, 234, 117, 668, 65, 67, 117, 118, 118, 119, 7, 115, 48, 119, 125, 127, 490, 653, 129, 161, 487, 508, 126, 127, 487, 489, 130, 135, 753, 859, 137, 139, 729, 859, 134, 135, 729, 752, 141, 233, 726, 746, 138, 139, 726, 728, 145, 147, 747, 683, 145, 146, 684, 685, 171, 173, 436, 750, 164, 169, 454, 750, 154, 155, 454, 485, 168, 169, 436, 453, 172, 173, 433, 435, 179, 271, 264, 317, 179, 180, 318, 319, 45, 67, 264, 320, 184, 185, 230, 231, 187, 59, 230, 234, 191, 283, 215, 222, 188, 189, 215, 217, 217, 218, 862, 863, 381, 400, 477, 1107, 226, 227, 693, 724, 260, 261, 345, 431, 286, 288, 160, 1107, 276, 277, 160, 213, 287, 288, 153, 159, 291, 292, 151, 152, 305, 307, 430, 383, 306, 307, 428, 429, 313, 315, 723, 692, 314, 315, 721, 722, 321, 322, 691, 692, 325, 327, 721, 678, 325, 326, 680, 681, 351, 352, 428, 449, 348, 349, 477, 478, 359, 368, 477, 344, 359, 360, 381, 383, 373, 374, 343, 344, 377, 494, 306, 308, 377, 378, 314, 315, 381, 392, 151, 199, 382, 383, 210, 211, 386, 387, 210, 221, 386, 509, 249, 250, 418, 419, 721, 744, 517, 720, 799, 823, 415, 416, 799, 800, 1019, 1156, 791, 823, 426, 435, 799, 669, 426, 427, 676, 678, 440, 441, 668, 669, 444, 532, 633, 635, 444, 445, 641, 642, 297, 335, 596, 643, 448, 453, 477, 505, 452, 544, 560, 565, 449, 450, 560, 561, 546, 748, 558, 565, 488, 501, 261, 262, 488, 489, 304, 305, 493, 486, 303, 305, 603, 486, 261, 263, 526, 539, 585, 588, 526, 527, 631, 632, 531, 524, 630, 632, 746, 524, 585, 589, 662, 675, 8, 45, 662, 663, 63, 64, 667, 660, 62, 64, 680, 681, 44, 45, 842, 8, 33, 47, 684, 840, 33, 34, 684, 685, 40, 41, 723, 728, 743, 1049, 713, 714, 743, 797, 727, 728, 719, 742, 734, 847, 716, 1049, 731, 732, 716, 718, 1170, 1259, 708, 962, 839, 840, 56, 57, 25, 682, 33, 35, 842, 660, 55, 57, 845, 1231, 48, 53, 845, 846, 59, 60, 117, 668, 58, 61, 852, 857, 716, 741, 856, 1017, 794, 823, 853, 854, 794, 795, 1278, 1479, 785, 823, 1020, 1025, 740, 1049, 1010, 1011, 740, 792, 1024, 1025, 714, 739, 1031, 1145, 711, 1049, 1028, 1029, 711, 713, 1032, 1041, 582, 584, 1035, 1172, 596, 617, 1035, 1036, 618, 619, 738, 870, 596, 620, 1040, 1041, 580, 581, 1047, 1184, 550, 565, 1044, 1045, 550, 552, 1161, 1162, 661, 709, 1187, 1192, 498, 1049, 1177, 1178, 498, 548, 1191, 1192, 465, 497, 1198, 1258, 462, 1049, 1195, 1196, 462, 464, 1219, 1225, 168, 169, 1222, 1338, 264, 281, 1222, 1223, 282, 283, 1224, 1225, 166, 167, 1227, 1131, 166, 169, 1228, 1229, 70, 80, 1235, 1237, 22, 80, 1319, 1324, 439, 1049, 1309, 1310, 439, 460, 1323, 1324, 411, 438, 1330, 1343, 408, 1049, 1327, 1328, 408, 410, 1331, 1332, 333, 365, 1334, 1336, 164, 363, 1334, 1335, 364, 365, 1352, 1353, 408, 437, 1352, 1429, 457, 1049, 1349, 1350, 457, 458, 1360, 1369, 164, 332, 1360, 1361, 361, 363, 1374, 1375, 331, 332, 1378, 1399, 264, 272, 1378, 1379, 278, 279, 1382, 1383, 164, 175, 1387, 1411, 174, 178, 1384, 1385, 174, 176, 1413, 1527, 171, 250, 1395, 1397, 179, 358, 1395, 1396, 359, 360, 1414, 1515, 108, 358, 1528, 1852, 108, 109, 1404, 1405, 108, 172, 1509, 1510, 457, 493, 1506, 1507, 530, 531, 1517, 1526, 108, 329, 1517, 1518, 356, 358, 1528, 1529, 328, 329, 1833, 1834, 327, 355, 1532, 1840, 264, 268, 1532, 1533, 269, 270, 1577, 1579, 703, 657, 1578, 1579, 701, 702, 1585, 1586, 656, 657, 1589, 1595, 596, 599, 1589, 1590, 605, 606, 1294, 1493, 596, 607, 1593, 1598, 530, 538, 1597, 1703, 540, 599, 1594, 1595, 540, 541, 1693, 1698, 701, 732, 1697, 1789, 779, 823, 1694, 1695, 779, 780, 1792, 1794, 731, 1071, 1782, 1783, 731, 777, 1793, 1794, 699, 730, 1797, 1798, 697, 698, 1801, 1802, 697, 774, 1820, 1949, 770, 802, 1816, 1818, 773, 1033, 1803, 1804, 773, 775, 1951, 1996, 767, 802, 1821, 1826, 537, 1071, 1811, 1812, 537, 771, 1825, 1826, 527, 536, 1832, 1929, 524, 1071, 1829, 1830, 524, 526, 1314, 1316, 462, 962, 1836, 1838, 113, 353, 1836, 1837, 354, 355, 1844, 1846, 113, 353, 1845, 1846, 92, 106, 1892, 1897, 100, 109, 1860, 1865, 92, 101, 1864, 1890, 103, 109, 1861, 1862, 103, 104, 1872, 1881, 3, 69, 1872, 1873, 78, 80, 1883, 1884, 68, 69, 1887, 1905, 48, 49, 1887, 1888, 50, 51, 1889, 1890, 100, 102, 1896, 1897, 90, 99, 1903, 1974, 98, 109, 1903, 1974, 87, 93, 1900, 1901, 87, 89, 1976, 2004, 85, 109, 1904, 1905, 75, 77, 1908, 1929, 48, 74, 1908, 1909, 76, 77, 1954, 1955, 386, 522, 41, 43, 864, 688, 45, 218, 864, 1107, 353, 355, 428, 404, 354, 355, 426, 427, 361, 362, 403, 404, 365, 367, 426, 380, 365, 366, 382, 383, 347, 349, 479, 449, 388, 390, 210, 207, 389, 390, 208, 209, 393, 394, 206, 207, 397, 398, 198, 199, 1337, 1411, 186, 250, 458, 459, 426, 448, 455, 456, 475, 476, 470, 471, 378, 380, 490, 491, 341, 342, 496, 618, 299, 301, 496, 499, 307, 308, 273, 375, 264, 309, 502, 503, 208, 247, 640, 828, 244, 250, 511, 638, 246, 250, 506, 509, 246, 248, 7, 383, 235, 250, 548, 549, 475, 504, 541, 544, 558, 559, 606, 629, 256, 259, 606, 609, 297, 298, 617, 604, 296, 298, 801, 820, 258, 260, 644, 645, 195, 197, 664, 665, 72, 73, 670, 843, 58, 60, 670, 673, 66, 67, 741, 742, 503, 556, 757, 758, 473, 502, 761, 762, 470, 472, 1318, 1344, 459, 962, 833, 834, 71, 194, 836, 837, 193, 194, 886, 887, 470, 501, 879, 882, 553, 554, 884, 1045, 553, 565, 982, 983, 190, 192, 1038, 1039, 500, 551, 1054, 1055, 468, 499, 257, 295, 481, 649, 1058, 1059, 465, 467, 1098, 1117, 253, 255, 1103, 1220, 264, 283, 1103, 1106, 284, 285, 806, 956, 264, 286, 1114, 1117, 251, 252, 1119, 942, 251, 255, 1127, 1141, 236, 250, 1122, 1125, 236, 238, 1130, 1332, 164, 165, 1135, 1141, 170, 187, 1135, 1138, 188, 189, 1130, 1133, 170, 189, 1189, 1190, 441, 463, 1205, 1206, 414, 440, 1209, 1210, 411, 413, 1213, 1214, 334, 367, 1216, 1217, 366, 367, 1320, 1322, 411, 365, 1321, 1322, 393, 409, 694, 696, 8, 1, 699, 700, 1067, 1095, 1415, 1417, 1106, 1095, 1419, 1428, 1106, 1066, 1419, 1420, 1093, 1095, 1433, 1434, 1065, 1066, 1437, 1439, 1106, 1046, 1437, 1438, 1048, 1049, 1348, 1350, 459, 437, 701, 702, 979, 1051, 1539, 1540, 975, 976, 1606, 1628, 992, 993, 1543, 1640, 949, 951, 1543, 1544, 957, 958, 710, 1447, 931, 959, 1610, 1623, 1002, 1005, 1610, 1611, 1042, 1043, 1615, 1608, 1041, 1043, 1650, 1659, 1004, 1006, 1634, 1676, 926, 928, 1634, 1635, 947, 948, 1639, 1632, 946, 948, 1653, 1727, 1007, 1037, 1653, 1654, 1038, 1039, 1658, 1659, 1002, 1003, 1661, 1608, 1002, 1006, 1665, 1739, 987, 993, 1662, 1663, 987, 989, 1820, 1937, 820, 1033, 1666, 1671, 929, 939, 1669, 1746, 940, 942, 1669, 1670, 943, 944, 1543, 1640, 940, 945, 1745, 848, 866, 930, 1712, 1717, 1083, 1085, 1716, 1717, 1081, 1082, 1723, 1725, 1081, 1073, 1723, 1724, 1074, 1075, 1720, 1721, 1061, 1075, 1754, 1755, 1060, 1073, 1732, 1733, 971, 985, 1751, 1752, 1077, 1080, 1914, 1919, 1104, 1085, 1911, 1912, 1104, 1105, 1918, 1919, 1102, 1103, 1922, 1923, 1086, 1092, 1925, 1927, 1102, 1090, 1925, 1926, 1091, 1092, 2034, 2036, 1102, 1090, 2035, 2036, 1096, 1101, 707, 716, 850, 851, 710, 1447, 963, 965, 710, 711, 966, 967, 715, 716, 848, 849, 718, 702, 848, 851, 722, 854, 796, 823, 719, 720, 796, 798, 850, 851, 841, 846, 850, 1261, 900, 901, 1745, 848, 841, 847, 1002, 1003, 845, 898, 1012, 1013, 841, 844, 1016, 1017, 791, 793, 1159, 1164, 738, 962, 1149, 1150, 738, 789, 1163, 1164, 711, 737, 1286, 1288, 708, 916, 1167, 1168, 708, 710, 1171, 1180, 578, 579, 1174, 1292, 596, 615, 1174, 1175, 616, 617, 1179, 1180, 576, 577, 1182, 1145, 576, 579, 1183, 1184, 547, 549, 1281, 1282, 660, 706, 1307, 1312, 496, 962, 1297, 1298, 496, 545, 1311, 1312, 462, 495, 1315, 1316, 459, 461, 1346, 1347, 459, 494, 1443, 1452, 532, 923, 1443, 1444, 961, 962, 1445, 999, 960, 962, 1457, 1458, 922, 923, 1505, 1507, 532, 493, 1461, 1553, 910, 912, 1461, 1462, 918, 919, 1007, 1459, 917, 919, 1483, 1485, 705, 659, 1484, 1485, 703, 704, 1491, 1492, 658, 659, 1495, 1587, 604, 606, 1495, 1496, 612, 613, 1499, 1504, 532, 539, 1503, 1595, 542, 565, 1500, 1501, 542, 543, 1549, 1558, 703, 894, 1549, 1550, 908, 909, 1551, 1463, 907, 909, 1563, 1564, 893, 894, 1593, 1676, 701, 901, 1567, 1687, 872, 874, 1567, 1568, 880, 881, 1266, 1471, 841, 882, 1571, 1576, 703, 733, 1572, 1573, 781, 782, 1575, 1695, 781, 823, 1583, 1592, 566, 567, 1583, 1584, 602, 603, 1585, 1581, 601, 603, 1593, 1581, 566, 568, 1683, 1692, 828, 829, 1683, 1684, 870, 871, 1685, 1681, 869, 871, 1693, 1681, 828, 830, 462, 464, 426, 402, 463, 464, 424, 425, 474, 475, 401, 402, 482, 483, 379, 380, 560, 561, 424, 447, 553, 554, 473, 474, 580, 581, 375, 377, 612, 613, 339, 340, 789, 790, 338, 374, 620, 804, 264, 294, 620, 625, 300, 301, 377, 494, 264, 302, 753, 754, 446, 471, 773, 774, 422, 445, 269, 294, 430, 681, 781, 782, 419, 421, 796, 797, 373, 374, 898, 899, 419, 444, 891, 892, 468, 469, 918, 919, 370, 372, 950, 951, 336, 337, 1086, 1087, 335, 369, 958, 1101, 264, 285, 958, 963, 291, 292, 1050, 1051, 443, 466, 1070, 1071, 417, 442, 1078, 1079, 414, 416, 1093, 1094, 368, 369, 1201, 1202, 394, 412, 420, 422, 721, 690, 421, 422, 719, 720, 428, 429, 689, 690, 432, 433, 677, 678, 521, 522, 674, 675, 528, 529, 666, 667, 534, 736, 596, 628, 534, 537, 634, 635, 337, 442, 596, 636, 725, 726, 665, 717, 1004, 1005, 902, 903, 1000, 1005, 904, 919, 1151, 1152, 841, 842, 1147, 1152, 843, 890, 1154, 1264, 841, 890, 1158, 1276, 788, 823, 1155, 1156, 788, 790, 1260, 1261, 897, 899, 1015, 1146, 841, 962, 1268, 1270, 837, 916, 1279, 1284, 736, 916, 1269, 1270, 736, 786, 1283, 1284, 708, 735, 1287, 1288, 705, 707, 1455, 1464, 705, 896, 1455, 1456, 915, 916, 1457, 1261, 914, 916, 1469, 1470, 895, 896, 1499, 1547, 703, 909, 1473, 1565, 879, 881, 1473, 1474, 887, 888, 1477, 1482, 705, 734, 1481, 1573, 783, 823, 1478, 1479, 783, 784, 1561, 1570, 831, 832, 1561, 1562, 877, 878, 1563, 1559, 876, 878, 1571, 1559, 831, 833, 1699, 1701, 701, 655, 1700, 1701, 699, 700, 1704, 1705, 654, 655, 1708, 1709, 598, 599, 1495, 1587, 596, 600, 1760, 1769, 996, 997, 1763, 1773, 1007, 1033, 1763, 1764, 1034, 1035, 1768, 1769, 994, 995, 1771, 1755, 994, 997, 1775, 1807, 981, 1033, 1772, 1773, 981, 983, 1809, 1814, 822, 1033, 1806, 1807, 822, 980, 1813, 1814, 773, 821, 1791, 1800, 776, 933, 1817, 1818, 770, 772, 1930, 1931, 1059, 1071, 1933, 1935, 816, 1069, 1933, 1934, 1070, 1071, 1959, 1961, 524, 1069, 1952, 1957, 535, 1069, 1942, 1943, 535, 768, 1956, 1957, 524, 534, 1963, 1977, 521, 1069, 1960, 1961, 521, 523, 1979, 1981, 521, 1058, 1979, 1980, 1068, 1069, 1986, 1987, 1057, 1058, 1990, 2022, 1022, 1024, 1990, 1991, 1030, 1031, 1994, 1999, 521, 533, 1998, 2031, 765, 802, 1995, 1996, 765, 766, 2018, 2027, 810, 811, 2018, 2019, 1020, 1021, 2020, 2016, 1019, 1021, 2028, 2016, 810, 812, 148, 157, 515, 516, 151, 243, 517, 651, 151, 152, 652, 653, 156, 157, 513, 514, 159, 143, 513, 516, 163, 255, 484, 508, 160, 161, 484, 486, 236, 237, 672, 683, 239, 241, 509, 681, 239, 240, 682, 683, 142, 143, 673, 685, 258, 263, 452, 681, 248, 249, 452, 482, 262, 263, 433, 451, 266, 267, 430, 432, 303, 304, 430, 450, 300, 301, 479, 480, 319, 328, 479, 671, 319, 320, 679, 681, 321, 323, 721, 681, 333, 334, 670, 671, 337, 442, 640, 642, 337, 338, 648, 649, 297, 335, 647, 649, 341, 346, 479, 506, 342, 343, 562, 563, 345, 450, 562, 565, 438, 447, 590, 591, 438, 439, 638, 639, 440, 436, 637, 639, 517, 436, 590, 592, 566, 568, 424, 400, 567, 568, 422, 423, 586, 587, 399, 400, 598, 599, 376, 377, 767, 768, 398, 420, 270, 279, 228, 229, 273, 375, 313, 315, 273, 274, 316, 317, 278, 279, 226, 227, 281, 218, 226, 229, 285, 383, 212, 222, 282, 283, 212, 214, 371, 380, 223, 224, 371, 372, 311, 312, 373, 369, 310, 312, 381, 369, 223, 225, 632, 634, 256, 205, 633, 638, 244, 245, 648, 649, 204, 205, 656, 657, 196, 197, 813, 814, 203, 242, 15, 105, 138, 140, 15, 18, 146, 147, 83, 84, 158, 163, 76, 79, 218, 219, 81, 189, 218, 222, 290, 292, 153, 1107, 95, 96, 136, 137, 104, 8, 135, 137, 119, 120, 122, 123, 182, 183, 162, 216, 198, 199, 156, 161, 202, 203, 153, 155, 206, 209, 129, 130, 211, 8, 120, 124, 211, 8, 128, 130, 214, 215, 132, 133, 7, 105, 131, 134, 7, 212, 125, 127, 514, 515, 932, 969, 1421, 1422, 1098, 1099, 1921, 1923, 1102, 1085, 1425, 1426, 1094, 1095, 1916, 1917, 1097, 1100, 1612, 1613, 1063, 1064, 1719, 1721, 1081, 1001, 1618, 1651, 1007, 1039, 1618, 1621, 1045, 1046, 1606, 1616, 1044, 1046, 1648, 1649, 1062, 1075, 1714, 1715, 1078, 1079, 1624, 1626, 1002, 974, 1625, 1628, 990, 991, 1630, 1663, 990, 993, 1636, 1637, 973, 974, 1642, 1667, 940, 944, 1642, 1645, 950, 951, 1449, 1541, 931, 952, 1656, 1657, 972, 988, 4, 39, 264, 1107, 406, 407, 860, 861, 710, 1746, 852, 865, 410, 412, 932, 854, 410, 411, 856, 857, 311, 402, 801, 857, 141, 221, 751, 859, 1263, 1272, 839, 840, 1266, 1471, 886, 888, 1266, 1267, 889, 890, 1271, 1272, 837, 838, 1274, 1261, 837, 840, 1275, 1276, 785, 787, 1801, 1804, 776, 1071, 1467, 1476, 834, 835, 1467, 1468, 884, 885, 1469, 1465, 883, 885, 1477, 1465, 834, 836, 1776, 1785, 826, 827, 1779, 1789, 852, 933, 1779, 1780, 934, 935, 1543, 1746, 931, 936, 1784, 1785, 824, 825, 1787, 1767, 824, 827, 1788, 1789, 776, 778, 1936, 1945, 818, 819, 1939, 1988, 1029, 1031, 1939, 1940, 1032, 1033, 1944, 1945, 816, 817, 1947, 1931, 816, 819, 1948, 1949, 767, 769, 2033, 2054, 762, 802, 1984, 1993, 813, 814, 1984, 1985, 1027, 1028, 1986, 1982, 1026, 1028, 1994, 1982, 813, 815, 2044, 2050, 808, 809, 2047, 2067, 1013, 1015, 2047, 2048, 1016, 1017, 1990, 2022, 820, 1018, 2049, 2050, 806, 807, 2052, 2039, 806, 809, 2053, 2054, 760, 761, 2056, 2076, 760, 802, 2063, 2072, 803, 804, 2063, 2064, 1011, 1012, 2065, 2061, 1010, 1012, 2073, 2061, 803, 805, 220, 229, 749, 750, 223, 233, 751, 857, 223, 224, 858, 859, 228, 229, 747, 748, 231, 143, 747, 750, 232, 233, 723, 725, 311, 312, 723, 745, 414, 416, 801, 744, 235, 309, 723, 857, 404, 413, 801, 853, 404, 405, 855, 857, 406, 408, 932, 857, 47, 48, 695, 696, 51, 53, 729, 685, 51, 52, 687, 688, 132, 133, 694, 727, 859, 860, 714, 715, 866, 867, 663, 664, 872, 1033, 596, 619, 872, 875, 625, 626, 1022, 1023, 662, 712, 735, 744, 587, 589, 738, 870, 624, 626, 738, 739, 627, 628, 444, 532, 596, 629, 743, 744, 585, 586, 750, 882, 555, 565, 747, 748, 555, 557, 1186, 1304, 547, 565, 864, 877, 580, 583, 864, 865, 622, 623, 869, 862, 621, 623, 1043, 862, 580, 584, 1291, 1300, 574, 575, 1294, 1493, 611, 613, 1294, 1295, 614, 615, 1299, 1300, 572, 573, 1302, 1259, 572, 575, 1306, 1501, 544, 565, 1303, 1304, 544, 546, 1489, 1498, 569, 570, 1489, 1490, 609, 610, 1491, 1487, 608, 610, 1499, 1487, 569, 571, 242, 251, 511, 512, 245, 255, 517, 649, 245, 246, 650, 651, 129, 149, 517, 653, 250, 251, 509, 510, 253, 237, 509, 512, 299, 301, 481, 450, 254, 255, 481, 483, 297, 298, 481, 507, 297, 343, 564, 565, 331, 340, 593, 594, 331, 332, 645, 646, 333, 329, 644, 646, 341, 329, 593, 595, 904, 906, 419, 397, 905, 906, 417, 418, 924, 925, 396, 397, 936, 937, 371, 372, 1064, 1065, 395, 415, 1354, 1356, 408, 392, 1355, 1356, 406, 407, 1362, 1363, 391, 392, 1366, 1368, 406, 360, 1366, 1367, 362, 363, 1342, 1358, 164, 363, 1389, 1390, 390, 405, 1511, 1513, 457, 389, 1512, 1513, 455, 456, 1519, 1520, 388, 389, 1523, 1524, 357, 358, 1392, 1393, 330, 360, 1599, 1600, 455, 528, 1603, 1604, 527, 529, 1823, 1824, 387, 525, 2000, 2002, 521, 385, 2001, 2002, 519, 520, 2005, 2006, 384, 385, 2009, 2039, 3, 349, 2009, 2010, 350, 351, 2028, 2029, 519, 763, 2030, 2031, 762, 764, 55, 57, 492, 348, 56, 57, 490, 491, 63, 64, 347, 348, 69, 177, 264, 319, 69, 72, 325, 326, 123, 124, 436, 488, 166, 167, 346, 434, 806, 956, 290, 292, 806, 809, 293, 294, 496, 618, 264, 295, 817, 820, 256, 257, 822, 604, 256, 260, 830, 976, 241, 250, 825, 828, 241, 243, 944, 967, 251, 254, 944, 947, 288, 289, 955, 942, 287, 289, 1049, 1051, 468, 255, 971, 976, 239, 240, 978, 1125, 239, 250, 986, 987, 201, 202, 994, 996, 251, 189, 994, 995, 191, 192, 1110, 1111, 200, 237, 1337, 1385, 177, 178, 1340, 1376, 277, 279, 1340, 1341, 280, 281, 1372, 1381, 183, 184, 1372, 1373, 275, 276, 1374, 1370, 274, 276, 1382, 1370, 183, 185, 1398, 1407, 181, 182, 1401, 1530, 264, 270, 1401, 1402, 271, 272, 1340, 1376, 264, 273, 1406, 1407, 179, 180, 1409, 1393, 179, 182, 1410, 1411, 171, 173, 1528, 5, 117, 250, 1143, 1332, 170, 250, 88, 89, 156, 157, 99, 100, 149, 150, 107, 207, 131, 133, 107, 112, 139, 140, 7, 13, 138, 141, 194, 195, 148, 154, 1839, 1848, 115, 116, 1842, 1855, 264, 266, 1842, 1843, 267, 268, 1847, 1848, 113, 114, 1850, 1834, 113, 116, 1854, 1862, 105, 109, 1851, 1852, 105, 107, 1899, 1901, 90, 109, 1857, 1859, 110, 111, 1857, 1858, 265, 266, 1860, 1965, 110, 353, 4, 1855, 110, 112, 1964, 1970, 96, 97, 1967, 2007, 110, 351, 1967, 1968, 352, 353, 1969, 1970, 94, 95, 1972, 1929, 94, 97, 1973, 1974, 85, 86, 2005, 5, 48, 109, 1866, 1868, 92, 83, 1867, 1868, 90, 91, 1874, 1875, 82, 83, 1878, 1879, 79, 80, 1894, 1895, 81, 88, 22, 31, 31, 32, 25, 682, 39, 41, 25, 26, 42, 43, 30, 31, 29, 30, 33, 21, 29, 32, 37, 690, 17, 21, 34, 35, 17, 19, 1245, 1882, 12, 21, 678, 687, 26, 27, 678, 679, 37, 38, 680, 676, 36, 38, 688, 676, 26, 28, 1230, 1239, 24, 25, 1233, 1885, 48, 51, 1233, 1234, 52, 53, 117, 843, 48, 54, 1238, 1239, 22, 23, 1241, 1229, 22, 25, 1242, 1243, 12, 14, 2080, 2083, 757, 1, 695, 696, 6, 7, 698, 700, 1106, 1051, 1248, 1249, 2, 4, 2080, 2081, 2, 755, 2082, 2083, 754, 756]

if myflag == 2:
    sign = [-1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

if myflag == 1:
    sign = [1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1]

if myflag == 3:
    rect = [5 , 6 , 7 , 9 ,4 , 6 , 10 , 15 ,6 , 7 , 9 , 10 ,6 , 8 , 15 , 7 ,12 , 13 , 3 , 5 ,13 , 14 , 5 , 7 ,13 , 15 , 15 , 3 ,29 , 30 , 1 , 2 ,30 , 31 , 2 , 3 ,30 , 32 , 15 , 1 ,32 , 33 , 1 , 15 ,33 , 35 , 15 , 1 ,34 , 35 , 13 , 14 ,35 , 36 , 14 , 15 ,35 , 37 , 1 , 13 , 15 , 16 , 3 , 15 ,16 , 20 , 15 , 3 ,28 , 30 , 3 , 15 ,24 , 28 , 15 , 3 ,8 , 9 , 7 , 15 ,11 , 13 , 7 , 15 ,9 , 11 , 15 , 7 ,20 , 21 , 3 , 15 ,23 , 24 , 3 , 15 ,21 , 23 , 15 , 3 ,14 , 17 , 7 , 11 ,10 , 17 , 12 , 13 ,17 , 18 , 11 , 12 ,17 , 19 , 13 , 7 ,22 , 25 , 4 , 6 ,19 , 25 , 7 , 13 ,25 , 26 , 6 , 7 ,25 , 27 , 13 , 4 ,27 , 34 , 4 , 13 ,0 , 1 , 0 , 10 ,1 , 3 , 10 , 0 ,2 , 3 , 1 , 8 , 3 , 4 , 8 , 10 ,3 , 29 , 0 , 1]


#У ЭТОГО УЗЛА РОД ДВА. ПРАВДА ЛИ ЭТО?
if myflag == 4:
    rect = [1 , 2 , 0 , 1 ,0 , 2 , 2 , 24 ,2 , 3 , 1 , 2 ,2 , 4 , 24 , 0 ,46 , 48 , 24 , 0 ,47 , 48 , 5 , 8 ,48 , 49 , 0 , 5 ,49 , 51 , 5 , 0 ,50 , 51 , 3 , 4 ,51 , 52 , 4 , 5 ,48 , 53 , 8 , 24 ,53 , 55 , 24 , 8 ,54 , 55 , 13 , 15 ,55 , 56 , 8 , 13 ,57 , 58 , 12 , 14 ,55 , 58 , 15 , 24 ,58 , 59 , 14 , 15 ,58 , 60 , 24 , 12 ,60 , 61 , 12 , 24 ,51 , 67 , 0 , 3 ,66 , 67 , 6 , 7 ,67 , 68 , 3 , 6 ,67 , 69 , 7 , 0 ,69 , 70 , 0 , 7 ,13 , 19 , 24 , 0 ,12 , 13 , 0 , 24 ,8 , 12 , 24 , 0 ,19 , 20 , 0 , 24 ,20 , 24 , 24 , 0 ,24 , 25 , 0 , 24 ,25 , 29 , 24 , 0 ,36 , 40 , 24 , 0 ,40 , 41 , 0 , 24 ,45 , 46 , 0 , 24 ,41 , 45 , 24 , 0 ,4 , 5 , 0 , 24 ,7 , 8 , 0 , 24 ,5 , 7 , 24 , 0 ,29 , 30 , 0 , 24 ,30 , 32 , 24 , 0 ,32 , 33 , 0 , 24 ,35 , 36 , 0 , 24 ,33 , 35 , 24 , 0 ,3 , 9 , 2 , 21 ,6 , 9 , 22 , 23 ,9 , 10 , 21 , 22 ,9 , 11 , 23 , 2 ,21 , 23 , 23 , 2 ,22 , 23 , 3 , 16 ,23 , 26 , 16 , 23 ,26 , 28 , 23 , 16 ,27 , 28 , 18 , 20 ,28 , 31 , 16 , 18 ,34 , 37 , 8 , 19 ,28 , 37 , 20 , 23 ,37 , 38 , 19 , 20 ,37 , 39 , 23 , 8 ,39 , 42 , 8 , 23 ,42 , 44 , 23 , 8 ,43 , 44 , 9 , 15 ,44 , 47 , 8 , 9 ,23 , 50 , 2 , 3 ,44 , 54 , 15 , 23 ,11 , 14 , 2 , 23 ,18 , 21 , 2 , 23 ,14 , 18 , 23 , 2 ,10 , 15 , 16 , 21 ,15 , 17 , 21 , 16 ,16 , 17 , 17 , 20 ,17 , 22 , 16 , 17 ,17 , 27 , 20 , 21 ,61 , 62 , 7 , 12 ,62 , 64 , 12 , 7 ,63 , 64 , 10 , 11 ,64 , 65 , 11 , 12 ,64 , 66 , 7 , 10]

if myflag == 5:
    rect = [1 , 2 , 0 , 1 ,0 , 2 , 2 , 8 ,2 , 3 , 1 , 2 ,2 , 4 , 8 , 0 ,10 , 12 , 8 , 0 ,11 , 12 , 6 , 7 ,12 , 13 , 7 , 8 ,12 , 14 , 0 , 6 ,14 , 16 , 6 , 0 ,15 , 16 , 3 , 5 ,16 , 17 , 5 , 6 ,16 , 18 , 0 , 3 ,4 , 5 , 0 , 8 ,9 , 10 , 0 , 8 ,5 , 9 , 8 , 0 ,3 , 6 , 2 , 6 ,6 , 8 , 6 , 2 ,7 , 8 , 3 , 4 ,8 , 11 , 4 , 6 ,8 , 15 , 2 , 3]
    sign = [1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1]

if myflag == 6:
    rect = [1, 2, 3, 4, 2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 6, 1, 1, 4, 1, 2, 5, 6, 3, 6, 6, 1, 2, 3]
    sign = [1, -1, 1, -1, 1, 1, -1]
    size = 7

if myflag == 7:
    rect = [65, 52, 32, 35, 34, 149, 79, 85, 135, 75, 69, 72, 138, 49, 31, 38, 44, 112, 106, 121, 48, 146, 75, 88, 48, 111, 100, 122, 146, 48, 61, 75, 149, 155, 60, 79, 41, 159, 7, 10, 106, 49, 125, 146, 95, 106, 159, 162, 49, 68, 169, 31, 9, 44, 101, 106, 111, 48, 122, 147, 52, 65, 143, 32, 48, 146, 44, 61, 112, 31, 121, 148, 146, 48, 23, 44, 122, 135, 31, 69, 92, 95, 162, 138, 49, 87, 155, 165, 65, 92, 138, 143, 49, 118, 38, 62, 68, 72, 31, 169, 75, 78, 133, 69, 26, 3, 49, 52, 114, 128, 159, 174, 103, 138, 91, 94, 121, 138, 38, 41, 37, 44, 121, 170, 41, 44, 171, 6, 152, 23, 82, 85, 146, 48, 88, 100, 72, 110, 169, 31, 49, 60, 66, 125, 37, 38, 3, 119, 69, 71, 30, 174, 111, 113, 151, 100, 114, 116, 30, 154, 121, 159, 19, 22, 146, 3, 13, 16, 81, 84, 97, 63, 165, 167, 7, 109, 117, 122, 69, 16, 9, 13, 46, 60, 117, 122, 23, 31, 155, 159, 46, 60, 55, 75, 130, 133, 103, 106, 97, 125, 49, 106, 146, 154, 12, 13, 7, 45, 135, 138, 169, 31, 131, 132, 3, 170, 125, 128, 30, 158, 3, 6, 16, 49, 52, 55, 35, 130, 159, 162, 10, 19, 106, 114, 154, 159, 128, 95, 158, 159, 149, 152, 85, 57, 87, 103, 165, 91, 122, 146, 16, 23, 44, 131, 170, 171, 23, 26, 52, 82, 48, 111, 147, 151, 60, 81, 63, 66, 48, 117, 16, 23, 38, 69, 174, 3, 31, 34, 148, 79, 71, 114, 174, 30, 113, 146, 100, 151, 110, 117, 31, 69, 84, 103, 94, 97, 31, 37, 119, 121, 13, 41, 6, 7, 13, 155, 45, 46, 118, 49, 62, 66, 118, 121, 22, 38, 138, 49, 165, 169, 159, 165, 109, 7, 60, 65, 125, 138, 159, 9, 60, 101, 159, 9, 22, 46, 167, 12, 109, 7, 116, 49, 154, 155, 138, 141, 41, 91, 132, 37, 170, 3, 128, 69, 29, 30] 
    sign = [-1, -1, -1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    size = len(sign)

if myflag == 8:
    rect = [0 , 1 , 1 , 14 , 1 , 3 , 14 , 1 , 2 , 3 , 2 , 4 , 3 , 4 , 1 , 2 , 3 , 5 , 4 , 14 , 5 , 7 , 14 , 4 , 6 , 7 , 5 , 7 , 7 , 8 , 4 , 5 , 7 , 12 , 7 , 14 , 12 , 14 , 14 , 7 , 13 , 14 , 8 , 10 , 14 , 15 , 7 , 8 , 14 , 19 , 10 , 14 , 19 , 21 , 14 , 10 , 20 , 21 , 11 , 13 , 21 , 22 , 10 , 11 , 21 , 26 , 13 , 14 , 4 , 9 , 0 , 1 , 8 , 9 , 3 , 4 , 9 , 10 , 1 , 3 , 9 , 11 , 4 , 0 , 11 , 16 , 0 , 4 , 15 , 16 , 6 , 7 , 16 , 17 , 4 , 6 , 16 , 18 , 7 , 0 , 18 , 23 , 0 , 7 , 22 , 23 , 9 , 10 , 23 , 24 , 7 , 9 , 23 , 25 , 10 , 0 , 25 , 27 , 0 , 10 , 26 , 27 , 12 , 13 , 27 , 28 , 10 , 12 , 27 , 29 , 13 , 0 , 29 , 30 , 0 , 13]

if myflag == 9:
    rect = [0 , 1 , 3 , 10 , 1 , 3 , 10 , 3 , 2 , 3 , 4 , 6 , 3 , 4 , 3 , 4 , 3 , 7 , 6 , 10 , 7 , 9 , 10 , 6 , 8 , 9 , 7 , 9 , 9 , 10 , 6 , 7 , 9 , 14 , 9 , 10 , 5 , 6 , 1 , 2 , 4 , 5 , 2 , 3 , 6 , 11 , 0 , 1 , 10 , 11 , 5 , 6 , 11 , 12 , 1 , 5 , 11 , 13 , 6 , 0 , 13 , 15 , 0 , 6 , 14 , 15 , 8 , 9 , 15 , 16 , 6 , 8 , 15 , 17 , 9 , 0 , 17 , 18 , 0 , 9]

#gen = 1
if myflag == 10:
    rect = [0 , 1 , 4 , 9 , 1 , 3 , 9 , 4 , 2 , 3 , 5 , 6 , 3 , 4 , 4 , 5 , 7 , 8 , 0 , 1 , 3 , 8 , 6 , 9 , 8 , 9 , 1 , 6 , 8 , 10 , 9 , 0 , 10 , 11 , 0 , 9 , 11 , 13 , 9 , 0 , 12 , 13 , 7 , 8 , 13 , 14 , 8 , 9 , 13 , 15 , 0 , 7 , 6 , 7 , 1 , 2 , 4 , 5 , 3 , 4 , 9 , 12 , 6 , 7 , 5 , 6 , 2 , 3]

#gen = 2
if myflag == 11:
    rect = [0 , 1 , 1 , 15 , 1 , 3 , 15 , 1 , 2 , 3 , 10 , 12 , 3 , 4 , 1 , 10 , 5 , 6 , 3 , 11 , 3 , 6 , 12 , 15 , 6 , 7 , 11 , 12 , 6 , 8 , 15 , 3 , 8 , 9 , 3 , 15 , 9 , 11 , 15 , 3 , 10 , 11 , 4 , 6 , 11 , 12 , 3 , 4 , 11 , 16 , 6 , 15 , 16 , 18 , 15 , 6 , 17 , 18 , 13 , 14 , 18 , 19 , 14 , 15 , 18 , 20 , 6 , 13 , 20 , 22 , 13 , 6 , 21 , 22 , 7 , 9 , 22 , 23 , 6 , 7 , 22 , 27 , 9 , 13 , 7 , 17 , 12 , 13 , 4 , 13 , 0 , 1 , 12 , 13 , 2 , 3 , 13 , 14 , 1 , 2 , 13 , 15 , 3 , 0 , 15 , 24 , 0 , 3 , 23 , 24 , 5 , 6 , 24 , 25 , 3 , 5 , 24 , 26 , 6 , 0 , 26 , 28 , 0 , 6 , 27 , 28 , 8 , 9 , 28 , 29 , 6 , 8 , 28 , 30 , 9 , 0 , 30 , 31 , 0 , 9]

#gen = 2
if myflag == 12:
    rect = [1 , 2 , 2 , 3 , 0 , 2 , 5 , 18 , 2 , 3 , 3 , 5 , 2 , 4 , 18 , 2 , 13 , 14 , 19 , 22 , 14 , 15 , 18 , 19 , 14 , 16 , 22 , 2 , 41 , 42 , 23 , 25 , 42 , 43 , 22 , 23 , 42 , 44 , 25 , 2 , 66 , 67 , 0 , 1 , 67 , 68 , 1 , 2 , 67 , 69 , 25 , 0 , 75 , 77 , 25 , 0 , 76 , 77 , 10 , 24 , 77 , 78 , 24 , 25 , 77 , 79 , 0 , 10 , 79 , 81 , 10 , 0 , 80 , 81 , 8 , 9 , 81 , 82 , 9 , 10 , 81 , 83 , 0 , 8 , 22 , 28 , 22 , 2 , 28 , 29 , 2 , 22 , 29 , 35 , 22 , 2 , 12 , 14 , 2 , 18 , 8 , 12 , 18 , 2 , 16 , 17 , 2 , 22 , 21 , 22 , 2 , 22 , 17 , 21 , 22 , 2 , 35 , 36 , 2 , 22 , 40 , 42 , 2 , 22 , 36 , 40 , 22 , 2 , 50 , 54 , 25 , 2 , 44 , 45 , 2 , 25 , 49 , 50 , 2 , 25 , 45 , 49 , 25 , 2 , 58 , 62 , 25 , 2 , 69 , 70 , 0 , 25 , 74 , 75 , 0 , 25 , 70 , 74 , 25 , 0 , 4 , 5 , 2 , 18 , 7 , 8 , 2 , 18 , 5 , 7 , 18 , 2 , 54 , 55 , 2 , 25 , 57 , 58 , 2 , 25 , 55 , 57 , 25 , 2 , 62 , 63 , 2 , 25 , 65 , 67 , 2 , 25 , 63 , 65 , 25 , 2 , 3 , 9 , 5 , 7 , 6 , 9 , 13 , 16 , 9 , 10 , 7 , 13 , 9 , 11 , 16 , 5 , 11 , 18 , 5 , 16 , 15 , 18 , 17 , 18 , 18 , 19 , 16 , 17 , 18 , 20 , 18 , 5 , 43 , 46 , 20 , 22 , 46 , 47 , 18 , 20 , 46 , 48 , 22 , 5 , 48 , 51 , 5 , 22 , 51 , 53 , 22 , 5 , 52 , 53 , 12 , 21 , 53 , 56 , 21 , 22 , 53 , 59 , 5 , 12 , 59 , 61 , 12 , 5 , 60 , 61 , 10 , 11 , 61 , 64 , 11 , 12 , 68 , 71 , 2 , 4 , 61 , 71 , 5 , 10 , 71 , 72 , 4 , 5 , 71 , 73 , 10 , 2 , 73 , 76 , 2 , 10 , 20 , 23 , 5 , 18 , 23 , 27 , 18 , 5 , 27 , 30 , 5 , 18 , 30 , 34 , 18 , 5 , 34 , 37 , 5 , 18 , 39 , 46 , 5 , 18 , 37 , 39 , 18 , 5 , 10 , 24 , 6 , 7 , 19 , 24 , 14 , 16 , 24 , 25 , 7 , 14 , 24 , 26 , 16 , 6 , 26 , 31 , 6 , 16 , 31 , 33 , 16 , 6 , 32 , 33 , 12 , 15 , 33 , 38 , 15 , 16 , 33 , 52 , 6 , 12]

#gen = 3
if myflag == 13:
    rect = [0 , 1 , 1 , 20 , 1 , 3 , 20 , 1 , 2 , 3 , 2 , 4 , 3 , 4 , 1 , 2 , 3 , 5 , 4 , 20 , 5 , 7 , 20 , 4 , 6 , 7 , 5 , 7 , 7 , 8 , 4 , 5 , 7 , 12 , 7 , 20 , 12 , 14 , 20 , 7 , 13 , 14 , 8 , 10 , 14 , 15 , 7 , 8 , 14 , 19 , 10 , 20 , 19 , 21 , 20 , 10 , 20 , 21 , 11 , 13 , 21 , 22 , 10 , 11 , 21 , 26 , 13 , 20 , 26 , 28 , 20 , 13 , 27 , 28 , 14 , 16 , 28 , 29 , 13 , 14 , 28 , 33 , 16 , 20 , 33 , 35 , 20 , 16 , 34 , 35 , 17 , 19 , 35 , 36 , 16 , 17 , 35 , 40 , 19 , 20 , 4 , 9 , 0 , 1 , 8 , 9 , 3 , 4 , 9 , 10 , 1 , 3 , 9 , 11 , 4 , 0 , 11 , 16 , 0 , 4 , 15 , 16 , 6 , 7 , 16 , 17 , 4 , 6 , 16 , 18 , 7 , 0 , 18 , 23 , 0 , 7 , 22 , 23 , 9 , 10 , 23 , 24 , 7 , 9 , 23 , 25 , 10 , 0 , 25 , 30 , 0 , 10 , 29 , 30 , 12 , 13 , 30 , 31 , 10 , 12 , 30 , 32 , 13 , 0 , 32 , 37 , 0 , 13 , 36 , 37 , 15 , 16 , 37 , 38 , 13 , 15 , 37 , 39 , 16 , 0 , 39 , 41 , 0 , 16 , 40 , 41 , 18 , 19 , 41 , 42 , 16 , 18 , 41 , 43 , 19 , 0 , 43 , 44 , 0 , 19]

#gen = 1
if myflag == 14:
    rect = [0 , 1 , 5 , 12 , 1 , 3 , 12 , 5 , 2 , 3 , 6 , 8 , 3 , 4 , 5 , 6 , 3 , 9 , 8 , 12 , 9 , 11 , 12 , 8 , 10 , 11 , 9 , 11 , 11 , 12 , 8 , 9 , 11 , 16 , 11 , 12 , 7 , 8 , 1 , 2 , 4 , 5 , 4 , 5 , 6 , 7 , 2 , 3 , 5 , 6 , 3 , 4 , 8 , 13 , 0 , 1 , 12 , 13 , 7 , 8 , 13 , 14 , 1 , 7 , 13 , 15 , 8 , 0 , 15 , 17 , 0 , 8 , 16 , 17 , 10 , 11 , 17 , 18 , 8 , 10 , 17 , 19 , 11 , 0 , 19 , 20 , 0 , 11]

#gen = 2
if myflag == 15:
    rect = [1 , 2 , 5 , 6 , 0 , 2 , 7 , 16 , 2 , 3 , 6 , 7 , 2 , 4 , 16 , 5 , 11 , 12 , 2 , 3 , 12 , 13 , 3 , 5 , 12 , 14 , 16 , 2 , 25 , 27 , 16 , 2 , 26 , 27 , 14 , 15 , 27 , 28 , 15 , 16 , 29 , 30 , 0 , 1 , 27 , 30 , 2 , 14 , 30 , 31 , 1 , 2 , 30 , 32 , 14 , 0 , 38 , 40 , 14 , 0 , 39 , 40 , 11 , 13 , 40 , 41 , 13 , 14 , 40 , 42 , 0 , 11 , 4 , 5 , 5 , 16 , 5 , 7 , 16 , 5 , 14 , 15 , 2 , 16 , 15 , 19 , 16 , 2 , 19 , 20 , 2 , 16 , 24 , 25 , 2 , 16 , 20 , 24 , 16 , 2 , 32 , 33 , 0 , 14 , 37 , 38 , 0 , 14 , 33 , 37 , 14 , 0 , 7 , 8 , 5 , 16 , 10 , 12 , 5 , 16 , 8 , 10 , 16 , 5 , 6 , 9 , 8 , 10 , 13 , 16 , 5 , 9 , 9 , 16 , 10 , 14 , 16 , 17 , 9 , 10 , 16 , 18 , 14 , 5 , 18 , 21 , 5 , 14 , 21 , 23 , 14 , 5 , 22 , 23 , 11 , 12 , 23 , 26 , 12 , 14 , 31 , 34 , 2 , 4 , 23 , 34 , 5 , 11 , 34 , 35 , 4 , 5 , 34 , 36 , 11 , 2 , 36 , 39 , 2 , 11 , 3 , 6 , 7 , 8]

#gen = 1
if myflag == 16:
    rect = [0 , 1 , 6 , 23 , 1 , 3 , 23 , 6 , 2 , 3 , 17 , 22 , 3 , 4 , 22 , 23 , 6 , 7 , 21 , 24 , 5 , 7 , 25 , 27 , 7 , 8 , 24 , 25 , 7 , 9 , 27 , 21 , 3 , 10 , 6 , 17 , 9 , 10 , 21 , 27 , 10 , 11 , 17 , 21 , 10 , 12 , 27 , 6 , 21 , 22 , 2 , 5 , 22 , 23 , 5 , 6 , 22 , 24 , 27 , 2 , 31 , 33 , 27 , 2 , 32 , 33 , 20 , 26 , 33 , 34 , 26 , 27 , 33 , 38 , 2 , 20 , 38 , 40 , 20 , 2 , 39 , 40 , 15 , 19 , 40 , 41 , 19 , 20 , 40 , 42 , 2 , 15 , 42 , 44 , 15 , 2 , 43 , 44 , 13 , 14 , 44 , 45 , 14 , 15 , 47 , 48 , 18 , 30 , 46 , 48 , 31 , 33 , 48 , 49 , 30 , 31 , 48 , 50 , 33 , 18 , 44 , 51 , 2 , 13 , 50 , 51 , 18 , 33 , 51 , 52 , 13 , 18 , 51 , 53 , 33 , 2 , 62 , 63 , 0 , 1 , 63 , 64 , 1 , 2 , 63 , 65 , 33 , 0 , 71 , 73 , 33 , 0 , 72 , 73 , 11 , 32 , 73 , 74 , 32 , 33 , 73 , 75 , 0 , 11 , 75 , 77 , 11 , 0 , 76 , 77 , 9 , 10 , 77 , 78 , 10 , 11 , 77 , 79 , 0 , 9 , 53 , 54 , 2 , 33 , 54 , 58 , 33 , 2 , 65 , 66 , 0 , 33 , 70 , 71 , 0 , 33 , 66 , 70 , 33 , 0 , 58 , 59 , 2 , 33 , 61 , 63 , 2 , 33 , 59 , 61 , 33 , 2 , 12 , 13 , 6 , 27 , 13 , 17 , 27 , 6 , 24 , 25 , 2 , 27 , 29 , 31 , 2 , 27 , 25 , 29 , 27 , 2 , 17 , 18 , 6 , 27 , 20 , 22 , 6 , 27 , 18 , 20 , 27 , 6 , 4 , 5 , 23 , 25 , 34 , 35 , 27 , 28 , 30 , 35 , 29 , 31 , 35 , 36 , 28 , 29 , 35 , 37 , 31 , 27 , 37 , 46 , 27 , 31 , 11 , 14 , 8 , 17 , 14 , 16 , 17 , 8 , 15 , 16 , 15 , 16 , 16 , 19 , 16 , 17 , 23 , 26 , 6 , 7 , 16 , 26 , 8 , 15 , 26 , 27 , 7 , 8 , 26 , 28 , 15 , 6 , 28 , 39 , 6 , 15 , 52 , 55 , 4 , 13 , 55 , 57 , 13 , 4 , 56 , 57 , 11 , 12 , 57 , 60 , 12 , 13 , 64 , 67 , 2 , 3 , 57 , 67 , 4 , 11 , 67 , 68 , 3 , 4 , 67 , 69 , 11 , 2 , 69 , 72 , 2 , 11]

#gen = 2
if myflag == 17:
    rect = [0 , 1 , 1 , 16 , 1 , 3 , 16 , 1 , 2 , 3 , 11 , 12 , 3 , 4 , 1 , 11 , 3 , 5 , 12 , 16 , 5 , 7 , 16 , 12 , 6 , 7 , 13 , 15 , 7 , 8 , 12 , 13 , 7 , 9 , 15 , 16 , 8 , 10 , 10 , 12 , 9 , 10 , 14 , 15 , 10 , 11 , 12 , 14 , 10 , 12 , 15 , 10 , 12 , 13 , 10 , 15 , 13 , 14 , 3 , 10 , 14 , 16 , 10 , 3 , 15 , 16 , 4 , 6 , 16 , 17 , 3 , 4 , 16 , 21 , 6 , 10 , 21 , 23 , 10 , 6 , 22 , 23 , 7 , 9 , 23 , 24 , 6 , 7 , 23 , 28 , 9 , 10 , 4 , 18 , 0 , 1 , 17 , 18 , 2 , 3 , 18 , 19 , 1 , 2 , 18 , 20 , 3 , 0 , 20 , 25 , 0 , 3 , 24 , 25 , 5 , 6 , 25 , 26 , 3 , 5 , 25 , 27 , 6 , 0 , 27 , 29 , 0 , 6 , 28 , 29 , 8 , 9 , 29 , 30 , 6 , 8 , 29 , 31 , 9 , 0 , 31 , 32 , 0 , 9]

#gen = 2
if myflag == 18:
    rect = [0 , 1 , 1 , 16 , 1 , 3 , 16 , 1 , 2 , 3 , 10 , 11 , 3 , 4 , 1 , 10 , 3 , 5 , 11 , 16 , 5 , 7 , 16 , 11 , 6 , 7 , 12 , 15 , 7 , 8 , 11 , 12 , 7 , 9 , 15 , 16 , 8 , 10 , 6 , 11 , 9 , 10 , 13 , 15 , 10 , 11 , 11 , 13 , 10 , 12 , 15 , 6 , 12 , 13 , 6 , 15 , 13 , 15 , 15 , 6 , 14 , 15 , 7 , 9 , 15 , 16 , 6 , 7 , 4 , 18 , 0 , 1 , 17 , 18 , 2 , 3 , 18 , 19 , 1 , 2 , 18 , 20 , 3 , 0 , 21 , 22 , 4 , 8 , 15 , 22 , 9 , 15 , 22 , 23 , 8 , 9 , 22 , 24 , 15 , 4 , 20 , 25 , 0 , 3 , 24 , 25 , 4 , 15 , 25 , 26 , 3 , 4 , 25 , 27 , 15 , 0 , 27 , 28 , 0 , 15 , 28 , 30 , 15 , 0 , 29 , 30 , 5 , 14 , 30 , 31 , 14 , 15 , 30 , 32 , 0 , 5 , 26 , 29 , 4 , 5 , 16 , 17 , 3 , 6]

#gen = 2
if myflag == 19:
    rect = [0 , 1 , 2 , 14 , 1 , 3 , 14 , 2 , 2 , 3 , 8 , 10 , 3 , 4 , 2 , 8 , 5 , 6 , 4 , 9 , 3 , 6 , 10 , 14 , 6 , 7 , 9 , 10 , 6 , 8 , 14 , 4 , 8 , 9 , 4 , 14 , 9 , 11 , 14 , 4 , 10 , 11 , 5 , 6 , 11 , 12 , 4 , 5 , 11 , 16 , 6 , 14 , 16 , 18 , 14 , 6 , 17 , 18 , 12 , 13 , 18 , 19 , 13 , 14 , 20 , 21 , 0 , 1 , 18 , 21 , 6 , 12 , 21 , 22 , 1 , 6 , 21 , 23 , 12 , 0 , 23 , 24 , 0 , 12 , 24 , 26 , 12 , 0 , 25 , 26 , 7 , 11 , 26 , 27 , 11 , 12 , 26 , 28 , 0 , 7 , 4 , 13 , 1 , 2 , 12 , 13 , 3 , 4 , 13 , 14 , 2 , 3 , 13 , 15 , 4 , 1 , 15 , 20 , 1 , 4 , 7 , 17 , 10 , 12 , 22 , 25 , 6 , 7]
size = len(rect) // 4

if sign == []:
    sign = [0] * size
    orientate(rect, size, sign)

for i in range(len(rect)):
    rect[i] = rect[i] + 1



#show_must_go_on(rect, sign, size)

#draw_rect(rect)

for i in range(size):
    sign[i] = - sign[i]


newcounter = 0
genprev = 0
gen = 0
maxcounter = 1
if 1:
    while True:
        n = len(rect) // 4
        adj = fill_adjecent(rect, n)
        fast_simplify(rect, n, sign, adj)
        size = len(rect) // 4
        if myflag == 0:
            draw_rect(rect)
        # rescale(rect, size)

        # draw_rect(rect)
        #print('GIENUS', genus(rect, len(rect) // 4))
        delta = 0.1


        rescale(rect, size)
        # draw_rect(rect)

        size = len(rect) // 4
        mut = mutant(rect, sign, size, delta)


        down_e = []
        up_e = []
        left_e = []
        right_e = []

        new_edges(rect, sign, size, delta, down_e, up_e, left_e, right_e)

        new_rect = []
        cook_rectangles(mut, len(down_e) // 3, down_e, up_e, left_e, right_e, sign)
        rescale(mut, len(mut) // 4)

        #adj = fill_adjecent(mut, len(mut) // 4)
        #print('len adj = ', len(adj))



        size = len(mut) // 4
        #draw_rect(mut)

        print('Its celver rotation used')
        clever_rotation(mut, size, sign)
        #rotate(mut, size, sign)
        #draw_rect(mut)
        gen = genus(mut, len(mut) // 4)
        print('GENUS = ', gen)
        print('max counter = ', maxcounter, 'counter = ', newcounter)

        size = len(mut) // 4
        print(len(mut) // 4, size)
        # draw_rect(mut)
        print('Finale')
        rescale(mut, size)
        #ТУТ УБРАЛ ДРОУ
        sort_rect(mut, size, sign)
        #draw_rect(mut)
        #print(mut, sign)
        delete_zeroes(mut, size, sign)
        size = len(mut) // 4
        adj = fill_adjecent(mut, size)
        #print('NEW MUT = ', mut, sign)
        draw_rect(mut)

        rect = mut
        if newcounter >=  maxcounter:
            for i in range(len(sign)):
                sign[i] = -sign[i]
            print('SIGN cHANGED')
            newcounter = 0
            if gen == genprev:
                maxcounter = maxcounter + 1
            else:
                maxcounter = 1
                destabilizations(mut, size, sign, adj, 1)
                fast_simplify(mut, size, sign, adj)
        else:
            newcounter = newcounter + 1
            if gen != genprev:
                destabilizations(mut, size, sign, adj, 1)
                fast_simplify(mut, size, sign, adj) 
        genprev = gen
from bdb import effective
from cmath import rect
from curses.textpad import rectangle
import re
from readline import append_history_file
from tkinter import E
from turtle import left
import matplotlib.pyplot as plt

x = [0]
Absolut_draw_flag = [0]

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
        if(a[4 * i] != 0 and a[4 * i + 1] != 0 and a[4 * i + 2] != 0 and a[4 * i + 3] != 0):
            vert.append([a[4 * i + 0], a[4 * i + 2]])
            vert.append([a[4 * i + 0], a[4 * i + 3]])
            vert.append([a[4 * i + 1], a[4 * i + 2]])
            vert.append([a[4 * i + 1], a[4 * i + 3]])
    vert.sort()

    m = len(vert)
    for i in range(m - 1):
        if vert[i] == vert[i + 1]:
            vert[i][0] = 0
            vert[i][1] = 0
            vert[i + 1][0] = 0
            vert[i + 1][1] = 0

    while [0, 0] in vert:
        vert.remove([0, 0])
    return vert

def free_vert_new(a, n, vert_orient, rect_v):
    vert = []
    n = len(a) // 4
    for i in range(n):
        if(a[4 * i] != 0 and a[4 * i + 1] != 0 and a[4 * i + 2] != 0 and a[4 * i + 3] != 0):
            vert.append([a[4 * i + 0], a[4 * i + 2]])
            vert.append([a[4 * i + 0], a[4 * i + 3]])
            vert.append([a[4 * i + 1], a[4 * i + 2]])
            vert.append([a[4 * i + 1], a[4 * i + 3]])
            vert_orient.append(3)
            vert_orient.append(0)
            vert_orient.append(2)
            vert_orient.append(1)

    m = len(vert)
    for i in range(m):
        for j in range(i + 1, m):
            if vert[i] == vert[j]:
                vert[i][0] = 0
                vert[i][1] = 0
                vert[j][0] = 0
                vert[j][1] = 0
                vert_orient[i] = -1
                vert_orient[j] = -1

    while [0, 0] in vert:
        vert.remove([0, 0])
    while -1 in vert_orient:
        vert_orient.remove(-1)
    # for i in range(len(vert)):
    #     print(i, vert[i], vert_orient[i])
    
    for v in vert:
        for i in range(n):
            if v in [[a[4 * i + 0], a[4 * i + 2]], [a[4 * i + 0], a[4 * i + 3]], [a[4 * i + 1], a[4 * i + 2]], [a[4 * i + 1], a[4 * i + 3]]]:
                rect_v.append(i)
                break
    
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
    #А не может ли тут быть ошибки? 
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
  
def check_vert_rect_modified(x1, x2, y1, y2, vert):
    #А не может ли тут быть ошибки? 
    if x1 < x2 and  y1 < y2:
        for i in range(len(vert)):
            if vert[i] == [0, 0]:
                continue
            if (vert[i][0] >= x1 and vert[i][0] <= x2 and vert[i][1] >= y1 and vert[i][1] <= y2) and not(vert[i] in [[x1,y1], [x1,y2], [x2, y1], [x2, y2]]):
                print(x1,x2, y1, y2, vert[i][0], vert[i][1])
                return 0
        return 1
    if x1 > x2 and  y1 < y2:
        for i in range(len(vert)):
            if vert[i] == [0, 0]:
                continue
            if (vert[i][0] >= x1 or vert[i][0] <= x2) and vert[i][1] >= y1 and vert[i][1] <= y2 and not(vert[i] in [[x1,y1], [x1,y2], [x2, y1], [x2, y2]]):
                print(x1,x2, y1, y2, vert[i][0], vert[i][1])
                return 0
        return 1
    if x1 < x2 and  y1 > y2:
        for i in range(len(vert)):
            if vert[i] == [0, 0]:
                continue
            if (vert[i][0] >= x1 and vert[i][0] <= x2 and (vert[i][1] >= y1 or vert[i][1] <= y2)) and not(vert[i] in [[x1,y1], [x1,y2], [x2, y1], [x2, y2]]):
                print(x1,x2, y1, y2, vert[i][0], vert[i][1])
                return 0
        return 1
    if x1 > x2 and  y1 > y2:
        for i in range(len(vert)):
            if vert[i] == [0, 0]:
                continue
            if (vert[i][0] >= x1 or vert[i][0] <= x2) and (vert[i][1] >= y1 or vert[i][1] <= y2)and not(vert[i] in [[x1,y1], [x1,y2], [x2, y1], [x2, y2]]):
                print(x1,x2, y1, y2, vert[i][0], vert[i][1])
                return 0
        return 1    
  
def delete(a, n):
    for i in range(n):
        if(a[4 * i] == a[4 * i + 1] or a[4 * i + 2] == a[4 * i + 3]):
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0


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
     
def genus(a, n):
    if a == []:
        return 0
    sum_1 = 0
    #количество 2-клеток
    for i in range(n):
        if a[4 * i] != 0 and a[4 * i + 1] != 0 and a[4 * i + 2] != 0 and a[4 * i + 3] != 0:
            sum_1 = sum_1 + 1
    b =  vertices(a, n)
    #количество ребер
    for j in range(len(b) - 1):
        if b[j][0] != 0 and b[j][1] != 0 and (b[j][0] != b[j + 1][0] or b[j][1] != b[j + 1][1]):
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

def draw_rect(a, sign):
    save_flag = 0
    print('GENUS = ', genus(a, len(a) // 4))
    a_cpy = a.copy()
    sign_cpy = sign.copy()
    if len(sign) != len(a) // 4:
        print('неверные длины!')
        print(a, sign)
        input()
    sort_rect(a_cpy, len(a) // 4, sign_cpy)

    #big_check_function(a_cpy, len(a) // 4, sign_cpy)
    plt.figure(figsize = (20, 10))
    y_min = 0
    x_min = 0
    x_max = 1
    y_max = 1
    e = 0.05
    for i in range(len(a_cpy) // 4):
        if a_cpy[4 * i] > x_max:
            x_max = a_cpy[4 * i]
        if a_cpy[4 * i + 1] > x_max:
            x_max = a_cpy[4 * i + 1]
        if a_cpy[4 * i + 2] > y_max:
            y_max = a_cpy[4 * i + 2]
        if a_cpy[4 * i + 3] > y_max:
            y_max = a_cpy[4 * i + 3]
    x_max = x_max + 2
    y_max = y_max + 2       
    for i in range(len(a_cpy) // 4):
        c = [0.7 + 0.2 * sign_cpy[i], 0.6, 0.3 + 0.2 * sign_cpy[i], 0.7]
        white = [1, 1, 1, 1]
        whiteindex = 1
        if a_cpy[4 * i + 2] > a_cpy[4 * i + 3] and a_cpy[4 * i] > a_cpy[4 * i + 1]:
            # правильная отрисовка
            if whiteindex:
                plt.fill([a_cpy[4 * i] - e, a_cpy[4 * i] - e, x_max, x_max], [a_cpy[4 * i + 2], y_max, y_max, a_cpy[4 * i + 2]], color =  white)
                plt.fill([a_cpy[4 * i + 1] + e, a_cpy[4 * i + 1] + e, x_min, x_min], [a_cpy[4 * i + 2], y_max, y_max, a_cpy[4 * i + 2]], color =  white)
                plt.fill([a_cpy[4 * i] - e, a_cpy[4 * i] - e, x_max, x_max], [a_cpy[4 * i + 3], y_min, y_min, a_cpy[4 * i + 3]], color =  white)
                plt.fill([a_cpy[4 * i + 1] + e, a_cpy[4 * i + 1] + e, x_min, x_min], [a_cpy[4 * i + 3], y_min, y_min, a_cpy[4 * i + 3]], color =  white)

            plt.fill([a_cpy[4 * i], a_cpy[4 * i], x_max, x_max], [a_cpy[4 * i + 2], y_max, y_max, a_cpy[4 * i + 2]], color =  c)
            plt.fill([a_cpy[4 * i + 1], a_cpy[4 * i + 1], x_min, x_min], [a_cpy[4 * i + 2], y_max, y_max, a_cpy[4 * i + 2]], color =  c)
            plt.fill([a_cpy[4 * i], a_cpy[4 * i], x_max, x_max], [a_cpy[4 * i + 3], y_min, y_min, a_cpy[4 * i + 3]], color = c)
            plt.fill([a_cpy[4 * i + 1], a_cpy[4 * i + 1], x_min, x_min], [a_cpy[4 * i + 3], y_min, y_min, a_cpy[4 * i + 3]], color = c)
            continue
        if a_cpy[4 * i + 2] < a_cpy[4 * i + 3] and a_cpy[4 * i] < a_cpy[4 * i + 1]:
            if whiteindex:
                plt.fill([a_cpy[4 * i] - e, a_cpy[4 * i] - e, a_cpy[4 * i + 1] + e, a_cpy[4 * i + 1] + e], [a_cpy[4 * i + 2], a_cpy[4 * i + 3], a_cpy[4 * i + 3], a_cpy[4 * i + 2]], color = white)
            
            plt.fill([a_cpy[4 * i], a_cpy[4 * i], a_cpy[4 * i + 1], a_cpy[4 * i + 1]], [a_cpy[4 * i + 2], a_cpy[4 * i + 3], a_cpy[4 * i + 3], a_cpy[4 * i + 2]], color = c)
        if a_cpy[4 * i + 2] > a_cpy[4 * i + 3]:
            if whiteindex:
                plt.fill([a_cpy[4 * i] - e, a_cpy[4 * i] - e, a_cpy[4 * i + 1] + e, a_cpy[4 * i + 1] + e], [a_cpy[4 * i + 2], y_max, y_max, a_cpy[4 * i + 2]], color =  white)
                plt.fill([a_cpy[4 * i] - e, a_cpy[4 * i] - e, a_cpy[4 * i + 1] + e, a_cpy[4 * i + 1] + e], [y_min, a_cpy[4 * i + 3], a_cpy[4 * i + 3], y_min], color =  white)

            plt.fill([a_cpy[4 * i], a_cpy[4 * i], a_cpy[4 * i + 1], a_cpy[4 * i + 1]], [a_cpy[4 * i + 2], y_max, y_max, a_cpy[4 * i + 2]], color =  c)
            plt.fill([a_cpy[4 * i], a_cpy[4 * i], a_cpy[4 * i + 1], a_cpy[4 * i + 1]], [y_min, a_cpy[4 * i + 3], a_cpy[4 * i + 3], y_min], color =  c)
        if a_cpy[4 * i] > a_cpy[4 *i + 1]:
            if whiteindex:
                plt.fill([x_min, x_min, a_cpy[4 * i + 1] + e, a_cpy[4 * i + 1] + e], [a_cpy[4 * i + 2], a_cpy[4 * i + 3], a_cpy[4 * i + 3], a_cpy[4 * i + 2]], color =  white)
                plt.fill([a_cpy[4 * i] - e, a_cpy[4 * i] - e, x_max, x_max], [a_cpy[4 * i + 2], a_cpy[4 * i + 3], a_cpy[4 * i + 3], a_cpy[4 * i + 2]], color =  white)

            plt.fill([x_min, x_min, a_cpy[4 * i + 1], a_cpy[4 * i + 1]], [a_cpy[4 * i + 2], a_cpy[4 * i + 3], a_cpy[4 * i + 3], a_cpy[4 * i + 2]], color =  c)
            plt.fill([a_cpy[4 * i], a_cpy[4 * i], x_max, x_max], [a_cpy[4 * i + 2], a_cpy[4 * i + 3], a_cpy[4 * i + 3], a_cpy[4 * i + 2]], color =  c)
    b = free_vert(a_cpy, len(a_cpy) // 4)
    for i in range(len(b)):
        if b[i][0] != 0:
            plt.scatter(b[i][0], b[i][1], marker = 'o', color = [1, 0, 0, 1])
    # print('rect = ', a)
    # print('sign = ', sign)
    # print(len(a), len(sign), len(adj))
    # for i in range(len(sign)):
    #     print(i, a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3], adj[4 * i + 0], adj[4 * i + 1], adj[4 * i + 2], adj[4 * i + 3])
    if save_flag:
        plt.savefig('rectpic/rect' + str(x[0]) + '.pdf', format = 'pdf')
        plt.savefig('rectpic/rect' + str(x[0]) + '.png', format = 'png')
        plt.clf()
        plt.close()

        f = open(str(x[0]) + '.txt', 'w')
        for j in a:
            f.write(str(j) + ' ')
        f.close()
        x[0] += 1
    if 0 and not save_flag:
        plt.show()
    else:
        #delete_zeroes(a, len(a) // 4, sign)
        print(a, sign)
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
    if len(a) != len(sign) * 4:
        print('что-то не то. длины не совпадают', len(a), len(sign))
        input()
    for i in range(n):
        if a[4 * i] == 0 :
            continue
        for j in range(n):
            if  a[4 * j] == 0:
                continue
            if (a[4 * i] == a[4 * j + 1] and a[4 * i + 3] == a[4 * j + 2]) or (a[4 * i] == a[4 * j + 1] and a[4 * i + 2] == a[4 * j + 3]) or (a[4 * i + 1] == a[4 * j] and a[4 * i + 3] == a[4 * j + 2]) or (a[4 * i + 1] == a[4 * j] and a[4 * i + 2] == a[4 * j + 3]):
                if (sign[i] * sign[j]) == +1:
                    print(' wrong orientation!!', a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3], a[4 * j + 0], a[4 * j + 1], a[4 * j + 2], a[4 * j + 3])
                    draw_rect(a, sign)
                    print('почему сюда не захожу то')
                    input()
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

def clever_rotation(a, n, sign, adj, effectiveness_flag):
    draw_flag = Absolut_draw_flag[0]
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

                            
                            continue
        if draw_flag:
            print('Im drawing here')
            draw_rect(a, sign)
        if flag == 0:
            attempts = attempts + 1
            q.pop(0)
            q.append(cur_1)
        else:
            effectiveness_flag[0] = 1
            attempts = 0
    print('COUNTER = ', counter, len(a) // 4, n)
    #draw_rect(a)
    print('flype phase ends')
    #СХЛОПЫВАНИЯ
    n = len(a) // 4
    #adj = fill_adjecent(a, n)
    print('len a', len(a) // 4, 'len adj', len(adj) // 4, 'n = ', n)

    adj = fast_simplify(a, n, sign, adj, effectiveness_flag)

def delete_zeroes(a, n, sign):
    #ЧТО ПЛОХО: В ADJ номера надо менять для корректной работы. а ведь же можно просто рефилл запустить...
    deleted = 0
    print('начали удалять нули')
    big_check_function(a, n, sign)
    i = 0
    while i < n:
        if a[4 * (i - deleted)] == 0 or a[4 * (i - deleted) + 1] == 0 or a[4 * (i - deleted) + 2] == 0 or a[4 * (i - deleted) + 3] == 0:
            del a[4 * (i - deleted) : 4 * (i - deleted) + 4]
            del sign[i - deleted]
            deleted = deleted + 1
        i = i + 1
    print('с длинами все нормально?', len(a), len(sign))
    return fill_adjecent(a, len(a) // 4)
    
#ВОТ ЭТА ФУНКЦИЯ НЕВЕРНО РАБОТАЕТ
def cmp_segments_A(s1, s2):
    #print("Тут будет функция, возвращает 1 если s2 содержится в s1")
    if s1[0][1] < s1[1][1]:
        if s2[0][1] < s2[1][1]:
            if s2[0][1] >= s1[0][1] and s2[1][1] <= s2[1][1]:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        if s2[0][1] < s2[1][1]:
            if s2[0][1] >= s1[0][1] or s2[1][1] <= s1[1][1]:
                return 1
            else:
                return 0
        else:
            if s2[0][1] >= s1[0][1] and s2[1][1] <= s1[1][1]:
                return 1
            else:
                return 0
        
def cmp_segments_B(s1, s2):
    #print("comparator B Тут будет функция, возвращает 1 если s2 содержится в s1")
    if s1[0][1] < s1[1][1]:
        if s2[0][1] < s2[1][1]:
            if s2[0][1] > s1[0][1] and s2[1][1] < s2[1][1]:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        if s2[0][1] < s2[1][1]:
            if s2[0][1] > s1[0][1] or s2[1][1] < s1[1][1]:
                return 1
            else:
                return 0
        else:
            if s2[0][1] > s1[0][1] and s2[1][1] < s1[1][1]:
                return 1
            else:
                return 0

def find_all_of_them(a, n, sign, znak, adj, effectiveness_flag):
#ищем довольно специфичные стабилизации
    drawflag = Absolut_draw_flag[0]
    vert_orientation = []
    rect_v = []
    free = free_vert_new(a, n, vert_orientation, rect_v)
    # верт_ориент -- ориентация каждой вершины
    # рест_в -- к какому прямоугольнику принадлежит вершина
    #print('странности:', len(vert_orientation), len(rect_v))
    notfree = only_vertices(a, n)
    len_free = len(free)

    #сортировка свободных вершин
    #блок проверен хотя бы на узле 12   
    for i in range(1, len_free - 1):
        #print(i)
        for j in range(len_free - i):
            if free[j][i % 2] == free[len_free - i][i % 2]:
                #print('hehehe', free, i, j)
                tmp0 = free[len_free - i - 1]
                free[len_free - i - 1]= free[j]
                free[j] = tmp0

                tmp2 = vert_orientation[j]
                vert_orientation[j] = vert_orientation[len_free - i - 1]
                vert_orientation[len_free - i - 1] = tmp2

                tmp3 = rect_v[j]
                rect_v[j] = rect_v[len_free - i - 1]
                rect_v[len_free - i - 1] = tmp3
                #print(free[len_free - i], i)
                break
    #print(free)
    # print('rect_v = ', rect_v)
    # for i in range(len(a) // 4):
    #     print(i, a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3])
    # print('vert_orinet', vert_orientation)


    # A = [[0, 1, 2, 3],
    #      [1, 2, 3, 0],
    #      [2, 3, 0, 1],
    #      [3, 0, 1, 2],
    #      [0, 3, 2, 1],
    #      [1, 0, 3, 2],
    #      [2, 1, 0, 3],
    #      [3, 2, 1, 0]]
    #похоже А был неверным чтоли?
    # A = [[0, 1, 2, 3],
    #      [1, 2, 3, 0],
    #      [3, 0, 1, 2],
    #      [2, 1, 0, 3]]

    #исправленный А
    A  = [[0, 3, 2, 1], [1, 2, 3, 0], [2, 1, 0, 3], [3, 0, 1, 2]]
    
    # B = [[0, 1, 3, 2],
    #     [1, 0, 3, 2],
    #     [3, 2, 0, 1],
    #     [2, 3, 0, 1],
    #     [3, 1, 2, 0],
    #     [1, 3, 0, 2],
    #     [2, 0, 3, 1],
    #     [0, 2, 1, 3]
    #     ]
    B = [[2, 1, 3, 0],
        [1, 2, 0, 3],
        [0, 3, 1, 2],
        [3, 0, 2, 1]]
    #почему нету 2 0 ... ????? ошибочка
    C = [
        [2, 0, 2, 2],
        [3, 1, 3, -1],
        [1, 3, 1, 1], 
        [0, 2, 0, 4]]

    #это новый вариант B. в народе(моем конспекте) называют В vertical
    D = [
        [0, 2, 3, 1],
        [1, 3, 2, 0],
        [3, 1, 0, 2],
        [2, 0, 1, 3]
    ]

    print('lenfree = ', len(free))
    print('FREEE = ', free[0], free[1])
    #следим за вертикальными ребрами
    if free[0][1] == free[1][1]:
        tmp = free[0]
        free.pop(0)
        free.append(tmp)
        tmp2 = vert_orientation[0]
        vert_orientation.pop(0)
        vert_orientation.append(tmp2)
        print('vert orientation тоже надо изменить!!')
        
        tmp3 = rect_v[0]
        rect_v.pop(0)
        rect_v.append(tmp3)
    if znak:
        rect_v = rect_v[::-1]
        free = free[::-1]
        vert_orientation = vert_orientation[::-1]
    print('FREEE = ', free[0], free[1])

    znak = 1

    # for i in range(len(free)):
    #     print('САЛАМ АЛЕЙКУМ', free[i], vert_orientation[i])

    # for i in range(len(a) // 4):
    #     print(a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3])
    # for j in range(len_free):
    #     print(free[j])
    

    #Гипотеза: cond2 нафиг не надо
    # print('отрисовка')
    # for i in range(len_free):
    #     print(free[i], vert_orientation[i])
    # print(vert_orientation)
    n = len(a) // 4
    
    #циклом проходимся и ищем нужную расстановку
    # znak очень странный персонаж
    for i in range(len_free // 2):
        # Case A --- simple destabilization
        comparator = [vert_orientation[2 * i], vert_orientation[(2 * i + 1) % len_free], vert_orientation[(2 * i + 2 * znak) % len_free], 6 - vert_orientation[2 * i] - vert_orientation[(2 * i + 1) % len_free] - vert_orientation[(2 * i + 2 * znak) % len_free]]
        cond1 = comparator in A
        # if vert_orientation[2 * i] in [0, 1]:
        #     cond2 = cmp_segments_A([free[2 * i], free[2 * i + 1]], [free[(2 * i + 3 * znak) % len_free], free[(2 * i + 2 * znak) % len_free]])
        # else:
        #     cond2 = cmp_segments_A([free[2 * i + 1], free[2 * i]], [free[(2 * i + 2 * znak) % len_free], free[(2 * i + 3 * znak) % len_free]])
        if cond1:
            print('я тут был', free[2 * i])
            if vert_orientation[2 * i] == 0 and check_vert_rect_modified(free[(2 * i + 2 * znak) % len_free][0], free[2 * i][0], free[2 * i][1], free[2 * i + 1][1], notfree):
                print('ПОБЕДА 1 0')   
                if drawflag:
                    draw_rect(a, sign)             
                #draw_rect(a, sign)
                a.extend([free[(2 * i + 2 * znak) % len_free][0], free[2 * i][0], free[2 * i][1], free[2 * i + 1][1]])
                adj[4 * rect_v[2 * i] + 0] = n
                adj[4 * rect_v[2 * i + 1] + 3] = n
                adj[4 * rect_v[(2 * i + 2) % len_free] + 2] = n
                adj.append(rect_v[(2 * i + 2) % len_free])
                adj.append(rect_v[2 * i + 1])
                adj.append(rect_v[2 * i])
                adj.append(-1)
                sign.append(-sign[rect_v[2 * i]])
                effectiveness_flag[0] = 1
                if drawflag:
                    draw_rect(a, sign)
                return 1
            if vert_orientation[2 * i] == 1 and check_vert_rect_modified(free[2 * i][0], free[(2 * i + 2 * znak) % len_free][0], free[2 * i][1], free[2 * i + 1][1], notfree):
                print('ПОБЕДА 1 1', free[2 * i][0], free[(2 * i + 2 * znak) % len_free][0], free[2 * i][1], free[2 * i + 1][1])
                if drawflag:
                    draw_rect(a, sign)    
                #draw_rect(a, sign)
                a.extend([free[2 * i][0], free[(2 * i + 2 * znak) % len_free][0], free[2 * i][1], free[2 * i + 1][1]])
                adj[4 * rect_v[2 * i] + 1] = n
                adj[4 * rect_v[2 * i + 1] + 2] = n
                adj[4 * rect_v[(2 * i + 2) % len_free] + 3] = n
                adj.append(rect_v[2 * i + 1])
                adj.append(rect_v[(2 * i + 2) % len_free])
                adj.append(-1)
                adj.append(rect_v[2 * i])
                sign.append(-sign[rect_v[2 * i]])
                effectiveness_flag[0] = 1
                if drawflag:
                    draw_rect(a, sign)
                return 1
            if vert_orientation[2 * i] == 2 and check_vert_rect_modified(free[2 * i][0], free[(2 * i + 2 * znak) % len_free][0], free[2 * i + 1][1], free[2 * i][1], notfree):
                print('ПОБЕДА 1 2') 
                if drawflag:
                    draw_rect(a, sign)   
                a.extend([free[2 * i][0], free[(2 * i + 2 * znak) % len_free][0], free[2 * i + 1][1], free[2 * i][1]])
                adj[4 * rect_v[2 * i] + 2] = n
                adj[4 * rect_v[2 * i + 1] + 1] = n
                adj[4 * rect_v[(2 * i + 2) % len_free] + 0] = n
                adj.append(rect_v[2 * i])
                adj.append(-1)
                adj.append(rect_v[(2 * i + 2) % len_free])
                adj.append(rect_v[2 * i + 1])
                sign.append(-sign[rect_v[2 * i]])
                effectiveness_flag[0] = 1
                if drawflag:
                    draw_rect(a, sign)
                return 1
            if vert_orientation[2 * i] == 3 and check_vert_rect_modified(free[(2 * i + 2 * znak) % len_free][0], free[2 * i][0], free[2 * i + 1][1], free[2 * i][1], notfree):
                print('ПОБЕДА 1 3', free[2 * i], free[2 * i + 1])   
                if drawflag:
                    draw_rect(a, sign) 
                #draw_rect(a, sign)
                a.extend([free[(2 * i + 2 * znak) % len_free][0], free[2 * i][0], free[2 * i + 1][1], free[2 * i][1]])
                adj[4 * rect_v[2 * i] + 3] = n
                adj[4 * rect_v[2 * i + 1] + 0] = n
                adj[4 * rect_v[(2 * i + 2) % len_free] + 1] = n
                adj.append(-1)
                adj.append(rect_v[2 * i])
                adj.append(rect_v[2 * i + 1])
                adj.append(rect_v[(2 * i + 2) % len_free])
                effectiveness_flag[0] = 1

                sign.append(-sign[rect_v[2 * i]])
                if drawflag:
                    draw_rect(a, sign)
                return 1
        # Case B --- simple destabilization
        cond1 = comparator in B
        # if vert_orientation[2 * i + 1] in [0, 1]:
        #     cond2 = cmp_segments_B([free[(2 * i + 3 * znak) % len_free], free[(2 * i + 2 * znak) % len_free]], [free[2 * i], free[2 * i + 1]])
        # else:
        #     cond2 = cmp_segments_B([free[(2 * i + 2 * znak) % len_free], free[(2 * i + 3 * znak) % len_free]], [free[2 * i + 1], free[2 * i]])
        if cond1:
            print('я тут был и тут [2]', free[2 * i])
            if vert_orientation[2 * i] == 0 and check_vert_rect_modified(free[(2 * i + 2 * znak) % len_free][0], free[2 * i][0], free[2 * i + 1][1], free[2 * i][1], notfree) and rect_v[2 * i] == rect_v[2 * i + 1]:
                print('нашлось 2 0')  
                print('Может есть еще случаи этой картинки??? когда расположение другое но формула ее не находит ')
                effectiveness_flag[0] = 1
                if drawflag:
                    draw_rect(a, sign)
                #draw_rect(a, sign)
                a[4 * rect_v[2 * i]] = free[(2 * i + 2 * znak) % len_free][0]
                adj[4 * rect_v[2 * i + 1] + 3] = rect_v[(2 * i + 2) % len_free]
                adj[4 * rect_v[(2 * i + 2) % len_free] + 1] = rect_v[2 * i + 1]
                if drawflag:
                    draw_rect(a, sign)
                return 1
            if vert_orientation[2 * i] == 1 and check_vert_rect_modified(free[(2 * i + 2 * znak) % len_free][0], free[2 * i][0], free[2 * i + 1][1], free[2 * i][1], notfree) and rect_v[2 * i] == rect_v[2 * i + 1]:
                print('нашлось2 1')  
                effectiveness_flag[0] = 1
                #draw_rect(a, sign)
                a[4 * rect_v[2 * i] + 1] = free[(2 * i + 2 * znak) % len_free][0]
                adj[4 * rect_v[2 * i + 1] + 2] = rect_v[(2 * i + 2) % len_free]
                adj[4 * rect_v[(2 * i + 2) % len_free] + 0] = rect_v[2 * i + 1]
                if drawflag:
                    draw_rect(a, sign)
                return 1
            # if vert_orientation[2 * i] == 1 and check_vert_rect_modified(free[2 * i][0], free[(2 * i + 2 * znak) % len_free][0], free[2 * i + 1][1], free[2 * i][1], notfree):
            #     print('нашлось2 1 нью') 

            #     draw_rect(a, sign)
            #     a[4 * rect_v[2 * i] + 1] = free[(2 *i  + 2) % len_free][0]
            #     if drawflag:
            #         draw_rect(a, sign)
            #     return 1
            if vert_orientation[2 * i] == 2 and check_vert_rect_modified(free[2 * i][0], free[(2 * i + 2 * znak) % len_free][0],  free[2 * i][1], free[2 * i + 1][1], notfree) and rect_v[2 * i] == rect_v[2 * i + 1]:
                print('нашлось 2 2') 
                effectiveness_flag[0] = 1
                if drawflag:
                    draw_rect(a, sign) 
                #draw_rect(a, sign)
                #print(len(rect_v), len(free))
                a[4 * rect_v[2 * i] + 1] = free[(2 * i + 2 * znak) % len_free][0]
                adj[4 * rect_v[2 * i + 1] + 1] = rect_v[(2 * i + 2) % len_free]
                adj[4 * rect_v[(2 * i + 2) % len_free] + 3] = rect_v[2 * i + 1]
                if drawflag:
                    draw_rect(a, sign)
                return 1
            if vert_orientation[2 * i] == 3 and check_vert_rect_modified(free[(2 * i + 2 * znak) % len_free][0], free[2 * i][0], free[2 * i][1], free[2 * i + 1][1], notfree) and rect_v[2 * i] == rect_v[2 * i + 1]:
                print('нашлось 2 3') 
                effectiveness_flag[0] = 1
                if drawflag:
                    draw_rect(a, sign) 
                #draw_rect(a, sign)
                a[4 * rect_v[2 * i] + 0] = free[(2 * i + 2 * znak) % len_free][0]
                adj[4 * rect_v[2 * i + 1] + 0] = rect_v[(2 * i + 2) % len_free]
                adj[4 * rect_v[(2 * i + 2) % len_free] + 2] = rect_v[2 * i + 1]
                print('here\'s a bag')
                if drawflag:
                    draw_rect(a, sign)
                return 1
        cond1 = comparator in C
        # print('We checked C condition')
        # print(len(free), len(a), i, rect_v[2 * i], len(adj))
        # if free[2 * i][0] == 5:
        #     print(cond1, vert_orientation[2 * i], vert_orientation[2 * i + 1], vert_orientation[2 * i + 2], 'alkfhslafjhalkfjdalwdkjalkwdjaldkjwldkjawldkjaldwkjalwkdjalkwdjlakdjlwakdjlakdwjlwakdjlawkdjlakdwjd\n', free[2 * i], free[2 * i + 1], cond1, 'vert', vert_orientation[2 * i] == 2, 'check1', check_vert_rect_modified(free[(2 * i + 2) % len_free][0], free[2 * i][0], free[2 * i][1], a[4 * rect_v[2 * i] + 3], notfree), 'check2', 
        # check_vert_rect_modified(free[(2 * i + 2) % len_free][0], free[2 * i][0], a[4 * rect_v[2 * i] + 3], free[2 * i + 1][1], notfree), 'cmp1', 
        # [[0, a[4 * rect_v[(2 * i + 2) % len_free] + 3]], free[(2 * i + 2) % len_free]], [free[2 * i], free[2 * i + 1]] 
        # , 'cmp2', [[0, a[4 * rect_v[2 * i]]], [0, a[4 * rect_v[2 * i] + 1]]], [[0, free[(2 * i + 2) % len_free][0]], [0,free[2 * i + 1][0]]])
        
        #ниже используеются абьюз в виде бесполезной перменной [0, ...]
        if (cond1 and vert_orientation[2 * i] == 2 and adj[4 * rect_v[2 * i] + 1] == rect_v[2 * i + 1] 
        and check_vert_rect_modified(free[(2 * i + 2) % len_free][0], free[2 * i][0], free[2 * i][1], a[4 * rect_v[2 * i] + 3], notfree) and
        check_vert_rect_modified(free[(2 * i + 2) % len_free][0], free[2 * i][0], a[4 * rect_v[2 * i] + 3], free[2 * i + 1][1], notfree) and 
        cmp_segments_A([[0, a[4 * rect_v[(2 * i + 2) % len_free] + 3]], free[(2 * i + 2) % len_free]], [free[2 * i], free[2 * i + 1]]) 
        and cmp_segments_A([[0, a[4 * rect_v[2 * i]]], [0, a[4 * rect_v[2 * i] + 1]]], [[0, free[(2 * i + 2) % len_free][0]], [0,free[2 * i + 1][0]]])):
            print('destab of type CССССССССССССС 2', 'COND1', cond1, free[2 * i], free[2 * i + 1], vert_orientation[2 * i], vert_orientation[2 * i + 1], comparator)
            effectiveness_flag[0] = 1
            if drawflag:
                draw_rect(a, sign)
            a[4 * rect_v[2 * i] + 1] = free[(2 * i + 2) % len_free][0]
            a[4 * rect_v[2 * i + 1] + 0] = free[(2 * i + 2) % len_free][0]
            adj[4 * rect_v[2 * i + 1] + 0] = rect_v[(2 * i + 2) % len_free]
            adj[4 * rect_v[(2 * i + 2) % len_free] + 2] = rect_v[2 * i + 1]
            print('destab of type CССССССССССС 2')
            if drawflag:
                draw_rect(a, sign)
            return 1
        if (cond1 and vert_orientation[2 * i] == 0 and 
        adj[4 * rect_v[2 * i] + 3] == rect_v[2 * i + 1] and
        check_vert_rect_modified(free[2 * i][0], free[(2 * i + 2) % len_free][0], a[4 * rect_v[2 * i] + 2], free[2 * i][1], notfree) and
        check_vert_rect_modified(free[2 * i][0], free[(2 * i + 2) % len_free][0], free[2 * i + 1][1], a[4 * rect_v[2 * i] + 2], notfree) and
        cmp_segments_A([free[(2 * i + 2) % len_free], [0, a[4 * rect_v[(2 * i + 2) % len_free] + 2]]], [free[2 * i + 1], free[2 * i]]) and
        cmp_segments_A([[0, free[2 * i][0]], [0, a[4 * rect_v[2 * i] + 1]]], [[0, free[2 * i + 1][0]], [0, free[(2 * i + 2) % len_free][0]]])):
            effectiveness_flag[0] = 1
            print('destab of type C 0', len(rect_v), len(free), len(a))
            if drawflag:
                draw_rect(a, sign)
            a[4 * rect_v[2 * i] + 0] = free[(2 * i + 2) % len_free][0]
            a[4 * rect_v[2 * i + 1]+ 1] = free[(2 * i + 2) % len_free][0]
            adj[4 * rect_v[2 * i + 1] + 2] = rect_v[(2 * i + 2) % len_free]
            adj[4 * rect_v[(2 * i + 2) % len_free] + 0] = rect_v[2 * i + 1]
            print('destab of type C 0')
            if drawflag:
                draw_rect(a, sign)
            return 1
        # if (free[2 * i][0] == 9):
        #     print(free[2 * i], free[2 * i + 1], 'cond1', cond1,
        #     'vert', vert_orientation[2 * i] == 1,
        #     'adj', adj[4 * rect_v[2 * i] + 2] == rect_v[2 * i + 1],
        #     'check1', check_vert_rect_modified(free[(2 * i + 2) % len_free][0], free[2 * i][0], a[4 * rect_v[2 * i] + 2], free[2 * i][1], notfree), 
        #     'check2', check_vert_rect_modified(free[(2 * i + 2) % len_free][0], free[2 * i][0], free[2 * i + 1][1], a[4 * rect_v[2 * i] + 2], notfree),
        #     'cmp1', cmp_segments_A([free[(2 * i + 2) % len_free], [0, a[4 * rect_v[(2 * i + 2) % len_free] + 2]]], [free[2 * i + 1], free[2 * i]]),
        #     'cmp2', cmp_segments_A([[0, free[(2 * i + 2) % len_free][0]], [0, free[2 * i + 1][0]]], [[0, a[4 * rect_v[2 * i]]], [0, free[2 * i][0]]]))
        if (cond1 and vert_orientation[2 * i] == 1 and 
        adj[4 * rect_v[2 * i] + 2] == rect_v[2 * i + 1] and
        check_vert_rect_modified(free[(2 * i + 2) % len_free][0], free[2 * i][0], a[4 * rect_v[2 * i] + 2], free[2 * i][1], notfree) and
        check_vert_rect_modified(free[(2 * i + 2) % len_free][0], free[2 * i][0], free[2 * i + 1][1], a[4 * rect_v[2 * i] + 2], notfree) and
        cmp_segments_A([free[(2 * i + 2) % len_free], [0, a[4 * rect_v[(2 * i + 2) % len_free] + 2]]], [free[2 * i + 1], free[2 * i]]) and
        cmp_segments_A([[0, a[4 * rect_v[2 * i]]], [0, free[2 * i][0]]], [[0, free[(2 * i + 2) % len_free][0]], [0, free[2 * i + 1][0]]])):
            effectiveness_flag[0] = 1
            print('destab of type C 1')
            if drawflag:
                draw_rect(a, sign)
            a[4 * rect_v[2 * i] + 1] = free[(2 * i + 2) % len_free][0]
            a[4 * rect_v[2 * i + 1] + 0] = free[(2 * i + 2) % len_free][0]
            adj[4 * rect_v[2 * i + 1] + 3] = rect_v[(2 * i + 2)% len_free]
            adj[4 * rect_v[(2 * i + 2) % len_free] + 1] = rect_v[2 * i + 1]
            print('destab of type C 1')
            if drawflag:
                draw_rect(a, sign)
            return 1

        if (
            cond1 and vert_orientation[2 * i] == 3 and
            adj[4 * rect_v[2 * i]] == rect_v[2 * i + 1] and
            check_vert_rect_modified(free[2 * i][0], free[(2 * i + 2) % len_free][0], free[2 * i][1], a[4 * rect_v[2 * i] + 3], notfree) and
            check_vert_rect_modified(free[2 * i][0], free[(2 * i + 2) % len_free][0], a[4 * rect_v[2 * i] + 3], free[2 * i + 1][1], notfree)  and
            cmp_segments_A([free[2 * i + 1], free[2 * i]], [free[(2 * i + 2) % len_free], [0, a[4 * rect_v[(2 * i + 2) % len_free] + 3]]]) and
            cmp_segments_A([[0, free[2 * i][0]], [0, a[4 * rect_v[2 * i] + 1]]], [[0, free[2 * i + 1][0]], [0, free[(2 * i + 2) % len_free][1]]])         
            ):
            effectiveness_flag[0] = 1
            print('destab of type C 3')
            if drawflag:
                draw_rect(a, sign)
            a[ 4 * rect_v[2 * i] + 0] = free[(2 * i + 2) % len_free][0]
            a[ 4 * rect_v[2 * i + 1] + 1] = free[(2 * i + 2) % len_free][0]
            adj[4 * rect_v[2 * i + 1] + 1] = rect_v[(2 * i + 2) % len_free]
            adj[4 * rect_v[(2 * i + 2) % len_free] + 3] = rect_v[2 * i + 1]
            print('destab of type C 3')
            if drawflag:
                draw_rect(a, sign)
            return 1
        
        xxxxx = (2 * i + 2) % len_free

        print('Пишу новый кусок для вертикальных дестабов')
        if free[2 * i][0] == 5:
            print('кейс 0 vertical')
        if (vert_orientation[2 * i] == 0 and
            cond1 and adj[4 * rect_v[2 * i + 1] + 3] == rect_v[(2 * i + 2) % len_free] and
            check_vert_rect_modified(free[xxxxx][0], a[4 * rect_v[xxxxx] + 1], free[2 * i][1], free[2 * i + 1][1], notfree) and
            check_vert_rect_modified(a[4 * rect_v[xxxxx] + 1], free[2 * i + 1][0], free[2 * i][1], free[2 * i + 1][1], notfree) and
            cmp_segments_A([[0, a[4 * rect_v[xxxxx] + 2]], free[xxxxx]], [free[2 * i], free[2 * i + 1]]) and
            cmp_segments_A([[0, free[2 * i][0]], [0, free[xxxxx][0]]], [[0, free[2 * i][0]], [0, a[4 * rect_v[2 * i] + 1]]])):
            effectiveness_flag[0] = 1
            print('destab of type C 0 vertical', free[2 * i], free[2 * i + 1], free[xxxxx], a[4 * rect_v[2 * i]], a[4 * rect_v[2 * i] + 1], a[4 * rect_v[2 * i] + 2], a[4 * rect_v[2 * i] + 3])
            if drawflag:
                draw_rect(a, sign)
            a[ 4 * rect_v[2 * i + 1] + 2] = free[2 * i][1]
            a[ 4 * rect_v[xxxxx] + 3] = free[2 * i][1]
            adj[4 * rect_v[2 * i + 1] + 2] = rect_v[2 * i]
            adj[4 * rect_v[2 * i] + 0] = rect_v[2 * i + 1]
            print('destab of type C')
            if drawflag:
                draw_rect(a, sign)
            return 1

        if free[2 * i][0] == 5:
            print('кейс 1')
        if (vert_orientation[2 * i] == 1 and
            cond1 and adj[4 * rect_v[2 * i + 1] + 2] == rect_v[xxxxx] and
            check_vert_rect_modified(free[2 * i + 1][0], a[4 * rect_v[2 * i + 1] + 1], free[2 * i][1], free[2 * i + 1][1], notfree) and
            check_vert_rect_modified(a[4 * rect_v[2 * i + 1] + 1] , free[xxxxx][0], free[2 * i][1], free[2 * i + 1][1], notfree) and
            cmp_segments_A([[0, a[4 * rect_v[xxxxx] + 2]], free[xxxxx]], [free[2 * i], free[2 * i + 1]]) and
            cmp_segments_A([[0, free[2 * i][0]], [0, free[xxxxx][0]]], [[0, free[2 * i + 1][0]], [0, free[xxxxx][0]]])):
            effectiveness_flag[0] = 1
            print('destab of type C 1 vertical', free[2 * i], free[2 * i + 1], free[xxxxx], a[4 * rect_v[2 * i]], a[4 * rect_v[2 * i] + 1], a[4 * rect_v[2 * i] + 2], a[4 * rect_v[2 * i] + 3])
            if drawflag:
                draw_rect(a, sign)
            a[ 4 * rect_v[2 * i + 1] + 2] = free[2 * i][1]
            a[ 4 * rect_v[xxxxx] + 3] = free[2 * i][1]
            adj[4 * rect_v[2 * i + 1] + 3] = rect_v[2 * i]
            adj[4 * rect_v[2 * i] + 1] = rect_v[2 * i + 1]
            print('destab of type C')
            if drawflag:
                draw_rect(a, sign)
            return 1

        if free[2 * i][0] == 5:
            print('кейс 2')
        if (vert_orientation[2 * i] == 2 and
            cond1 and adj[4 * rect_v[2 * i + 1] + 1] == rect_v[xxxxx] and
            check_vert_rect_modified(free[2 * i + 1][0], a[4 * rect_v[2 * i + 1] + 1], free[2 * i + 1][1], free[2 * i][1], notfree) and
            check_vert_rect_modified(a[4 * rect_v[2 * i + 1] + 1], free[xxxxx][0], free[2 * i + 1][1], free[2 * i][1], notfree) and
            cmp_segments_A([free[xxxxx], [0, a[4 * rect_v[xxxxx] + 3]]], [free[2 * i + 1], free[2 * i]]) and
            cmp_segments_A([[0, free[xxxxx][0]], [0, free[2 * i + 1][0]]], [[0, a[4 * rect_v[2 * i]]], [0, free[2 * i][0]]])):
            effectiveness_flag[0] = 1
            print('destab of type C 2 vertical', free[2 * i], free[2 * i + 1], free[xxxxx], a[4 * rect_v[2 * i]], a[4 * rect_v[2 * i] + 1], a[4 * rect_v[2 * i] + 2], a[4 * rect_v[2 * i] + 3])
            if drawflag:
                draw_rect(a, sign)
            a[ 4 * rect_v[2 * i + 1] + 3] = free[2 * i][1]
            a[ 4 * rect_v[xxxxx] + 2] = free[2 * i][1]
            adj[4 * rect_v[2 * i + 1] + 0] = rect_v[2 * i]
            adj[4 * rect_v[2 * i] + 2] = rect_v[2 * i + 1]
            print('destab of type C')
            if drawflag:
                draw_rect(a, sign)
            return 1

        if free[2 * i][0] == 5:
            print('кейс 3')
        if (vert_orientation[2 * i] == 3 and
            cond1 and adj[4 * rect_v[2 * i + 1] + 0] == rect_v[xxxxx] and
            check_vert_rect_modified(free[xxxxx][0], a[4 * rect_v[2 * i + 1]], free[2 * i + 1][1], free[2 * i][1], notfree) and
            check_vert_rect_modified(a[4 * rect_v[2 * i + 1]], free[2 * i + 1][0], free[2 * i + 1][1], free[2 * i][1], notfree) and
            cmp_segments_A([free[xxxxx], [0, a[4 * rect_v[xxxxx] + 3]]], [free[2 * i + 1], free[2 * i]]) and
            cmp_segments_A([[0, free[2 * i + 1][0]], [0, free[xxxxx][0]]], [[0, free[2 * i][0]], [0, a[4 * rect_v[2 * i] + 1]]])):
            effectiveness_flag[0] = 1
            print('destab of type C 3 vertical',  free[2 * i], free[2 * i + 1], free[xxxxx], a[4 * rect_v[2 * i]], a[4 * rect_v[2 * i] + 1], a[4 * rect_v[2 * i] + 2], a[4 * rect_v[2 * i] + 3])
            # print('Проверочная',
            # cond1 , adj[4 * rect_v[2 * i + 1] + 0] == rect_v[xxxxx] ,
            # free[xxxxx][0], a[4 * rect_v[2 * i + 1]], free[2 * i + 1][1], free[2 * i][1], notfree,
            # check_vert_rect(a[4 * rect_v[2 * i + 1]], free[2 * i + 1][0], free[2 * i + 1][1], free[2 * i][1], notfree) ,
            # cmp_segments_A([free[xxxxx], [0, a[4 * rect_v[xxxxx] + 3]]], [free[2 * i + 1], free[2 * i]]) ,
            # cmp_segments_A([[0, free[2 * i + 1][0]], [0, free[xxxxx][0]]], [[0, free[2 * i][0]], [0, a[4 * rect_v[2 * i] + 1]]]))
            if drawflag:
                draw_rect(a, sign)
            a[ 4 * rect_v[2 * i + 1] + 3] = free[2 * i][1]
            a[ 4 * rect_v[xxxxx] + 2] = free[2 * i][1]
            adj[4 * rect_v[2 * i + 1] + 1] = rect_v[2 * i]
            adj[4 * rect_v[2 * i] + 3] = rect_v[2 * i + 1]
            print('destab of type C')
            if drawflag:
                draw_rect(a, sign)
            return 1
        cond1 = comparator in D
        xxxxx = (2 * i + 2) % len_free
        if (
            cond1 and vert_orientation[2 * i] == 0 and
            check_vert_rect_modified(free[xxxxx][0], free[2 * i][0], free[2 * i][1], free[2 * i + 1][1], notfree)
        ):
            print('сработал флаг В вертикальный 0 можно сказат серия D', free[ 2 * i], free[2 * i + 1])
            effectiveness_flag[0] = 1
            if drawflag:
                draw_rect(a, sign)
            a[4 * rect_v[2 * i + 1] + 2] = free[2 * i][1]
            adj[4 * rect_v[2 * i] + 0] = rect_v[2 * i + 1]
            adj[4 * rect_v[2 * i + 1] + 2] = rect_v[2 * i]
            if drawflag:
                draw_rect(a, sign)
            return 1
        
        if (
            cond1 and vert_orientation[2 * i] == 1 and
            check_vert_rect_modified(free[2 * i][0], free[xxxxx][0], free[2 * i][1], free[2 * i + 1][1], notfree)
        ):
            print('сработал флаг В вертикальный 1 можно сказат серия D', free[ 2 * i], free[2 * i + 1])
            effectiveness_flag[0] = 1
            if drawflag:
                draw_rect(a, sign)
            a[4 * rect_v[2 * i + 1] + 2] =  free[2 * i][1]
            adj[4 * rect_v[2 * i] + 1] = rect_v[2 * i + 1]
            adj[4 * rect_v[2 * i + 1] + 3] = rect_v[2 * i]
            if drawflag:
                draw_rect(a, sign)
            return 1
        
        if (
            cond1 and vert_orientation[2 * i] == 2 and
            check_vert_rect_modified(free[2 * i][0], free[xxxxx][0], free[xxxxx][1], free[2 * i][1], notfree)
        ):
            print('сработал флаг В вертикальный22 можно сказат серия D', free[ 2 * i], free[2 * i + 1])
            effectiveness_flag[0] = 1
            if drawflag:
                draw_rect(a, sign)
            a[4 * rect_v[2 * i + 1] + 3] = free[2 * i][1]
            adj[4 * rect_v[2 * i] + 2] = rect_v[2 * i + 1]
            adj[4 * rect_v[2 * i + 1] + 0] = rect_v[2 * i]
            if drawflag:
                draw_rect(a, sign)
            return 1

        if (
            cond1 and vert_orientation[2 * i] == 3 and
            check_vert_rect_modified(free[xxxxx][0], free[2 * i][0], free[xxxxx][1], free[2 * i][1], notfree)
        ):
            print('сработал флаг В вертикальный 333 можно сказат серия D', free[ 2 * i], free[2 * i + 1])
            effectiveness_flag[0] = 1
            if drawflag:
                draw_rect(a, sign)
            a[4 * rect_v[2 * i + 1] + 3] = free[2 * i][1] 
            adj[4 * rect_v[2 * i] + 3] = rect_v[2 * i + 1]
            adj[4 * rect_v[2 * i + 1] + 2] = rect_v[2 * i]
            if drawflag:
                draw_rect(a, sign)
            return 1
        
def destabilizations(a, n, sign, adj, flag_simp, effectiveness_flag):
    #flag_simp = 0
    #забыл зачем мне это
    draw_flag = Absolut_draw_flag[0]
    index = [0]
    draw_knot_flag = 0
    q = []
    n = len(a) // 4
    # for i in range(n):
    #     print(a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3], adj[4 * i + 0], adj[4 * i + 1], adj[4 * i + 2], adj[4 * i + 3])
    for i in range(n):
        q.append(i)
    attempts = 0
    v = free_vert(a, n)
    hor = []
    vert = []
    
    for i in v:
        if not (i[0] in vert):
            vert.append(i[0])
        if not (i[1] in hor):
            hor.append(i[1])

    # print('before destab')
    # draw_rect(a)
    while(attempts < n):
        i = q[0]
        # if attempts == 0:
        #     draw_rect(a)
        if a[4 * i + 0] == 0 or a[4 * i + 1] == 0 or a[4 * i + 2] == 0 or a[4 * i + 3] == 0:
            q.pop(0)
            q.append(i)
            attempts = attempts + 1
            continue
        if adj[4 * i + 0] == -1 and adj[4 * i + 1] == -1 and adj[4 * i + 2] == -1:
            print('мы в плохом месте', a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3])
            if draw_flag:
                print(a)
                print('hard situation')
                draw_rect(a, sign)
            if not( a[4 * i + 1] in vert) or not (a[4 * i + 3] in hor):
                print(a)
                print('hard situation')
                print(hor, vert)
                draw_rect(a, sign)
                
            vert.remove(a[4 * i + 1])
            hor.remove(a[4 * i + 3])
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            if adj[4 * i + 3] != -1:
                adj[4 * adj[4 * i + 3] + 1] = -1
            adj[4 * i + 3] = -1
            print('destab - 3')
            attempts = 0
            effectiveness_flag[0] = 1
            q.pop(0)
            q.append(i)
            if draw_knot_flag:
                draw_knot(a, n, index)
            if draw_flag:
                draw_rect(a, sign)
            continue
        if adj[4 * i + 0] == -1 and adj[4 * i + 1] == -1 and adj[4 * i + 3] == -1:
            # print(vert)
            # draw_rect(a)
            vert.remove(a[4 * i + 0])
            hor.remove(a[4 * i + 3])
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            if adj[4 * i + 2] != -1:
                adj[4 * adj[4 * i + 2] + 0] = -1
            adj[4 * i + 2] = -1
            print('destab - 2')
            attempts = 0
            effectiveness_flag[0] = 1
            q.pop(0)
            q.append(i)
            if draw_knot_flag:
                draw_knot(a, n, index)
            if draw_flag:
                draw_rect(a, sign)
            continue
        if adj[4 * i + 0] == -1 and adj[4 * i + 2] == -1 and adj[4 * i + 3] == -1:
            # print(vert)
            # draw_rect(a)
            if not(a[4 * i + 1] in vert) or not(a[4 * i + 2] in hor):
                print('vert = ', vert)
                print('a = ', a)
                print('sign = ', sign)
                print('adj = ', adj)
                input()
            vert.remove(a[4 * i + 0])
            hor.remove(a[4 * i + 2])
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            if adj[4 * i + 1] != -1:
                adj[4 * adj[4 * i + 1] + 3] = -1
            adj[4 * i + 1] = -1
            print('destab - 1')
            attempts = 0
            effectiveness_flag[0] = 1
            q.pop(0)
            q.append(i)
            if draw_knot_flag:
                draw_knot(a, n, index)
            if draw_flag:
                draw_rect(a, sign)
            continue
        if adj[4 * i + 3] == -1 and adj[4 * i + 1] == -1 and adj[4 * i + 2] == -1:
            # print(vert)
            # draw_rect(a)
            
            vert.remove(a[4 * i + 1])
            hor.remove(a[4 * i + 2])
            a[4 * i + 0] = 0
            a[4 * i + 1] = 0
            a[4 * i + 2] = 0
            a[4 * i + 3] = 0
            if adj[4 * i + 0] != -1:
                print('OH NO')
                adj[4 * adj[4 * i + 0] + 2] = -1
            adj[4 * i + 0] = -1
            print('destab - 0')
            attempts = 0
            effectiveness_flag[0] = 1
            q.pop(0)
            q.append(i)
            if draw_knot_flag:
                draw_knot(a, n, index)
            if draw_flag:
                draw_rect(a, sign)
            continue
        if flag_simp:
            if adj[4 * i + 0] == -1 and adj[4 * i + 1] == -1  and sign[i] == -1:
                if not (a[4 * i + 2] in hor):
                    hor.remove(a[4 * i + 3])
                    hor.append(a[4 * i + 2])
                    a[4 * i + 0] = 0
                    a[4 * i + 1] = 0
                    a[4 * i + 2] = 0
                    a[4 * i + 3] = 0
                    if adj[4 * i + 2] != -1:
                        adj[4 * adj[4 * i + 2] + 0] = -1
                    if adj[4 * i + 3] != -1:
                        adj[4 * adj[4 * i + 3] + 1] = -1
                    adj[4 * i + 2] = -1
                    adj[4 * i + 3] = -1
                    print('destab - 01')
                    attempts = 0
                    effectiveness_flag[0] = 1
                    q.pop(0)
                    q.append(i)
                    
                    if draw_knot_flag:
                        draw_knot(a, n, index)
                    if draw_flag:
                        draw_rect(a, sign)
                    continue
                else:
                    a[4 * i + 3] = a[4 * i + 2] + 0.5
                    rescale(a, n)
                    vert = []
                    hor = []
                    v = free_vert(a, n)
                    for j in v:
                        if not (j[0] in vert):
                            vert.append(j[0])
                        if not (j[1] in hor):
                            hor.append(j[1])
                    if draw_flag:
                        draw_rect(a, sign)
                    
                    
            if adj[4 * i + 0] == -1 and adj[4 * i + 3] == -1  and sign[i] == 1:
                if not (a[4 * i + 1] in vert):
                    vert.remove(a[4 * i + 0])
                    vert.append(a[4 * i + 1])
                    a[4 * i + 0] = 0
                    a[4 * i + 1] = 0
                    a[4 * i + 2] = 0
                    a[4 * i + 3] = 0
                    if adj[4 * i + 1] != -1:
                        adj[4 * adj[4 * i + 1] + 3] = -1
                    print('Really')
                    if adj[4 * i + 2] != -1:
                        adj[4 * adj[4 * i + 2] + 0] = -1
                    adj[4 * i + 1] = -1
                    adj[4 * i + 2] = -1
                    print('destab - 03')
                    attempts = 0
                    q.pop(0)
                    q.append(i)
                    effectiveness_flag[0] = 1
                    if draw_knot_flag:
                        draw_knot(a, n, index)
                    if draw_flag:
                        draw_rect(a, sign)
                    continue
                else:
                    a[4 * i + 0] = a[4 * i + 1] - 0.5
                    rescale(a, n)
                    vert = []
                    hor = []
                    v = free_vert(a, n)
                    for j in v:
                        if not (j[0] in vert):
                            vert.append(j[0])
                        if not (j[1] in hor):
                            hor.append(j[1])
                    if draw_flag:
                        draw_rect(a, sign)
                    

            if adj[4 * i + 1] == -1 and adj[4 * i + 2] == -1 and sign[i] == 1:
                if not (a[4 * i + 0] in vert):
                    vert.remove(a[4 * i + 1])
                    vert.append(a[4 * i + 0])
                    a[4 * i + 0] = 0
                    a[4 * i + 1] = 0
                    a[4 * i + 2] = 0
                    a[4 * i + 3] = 0
                    if adj[4 * i + 0] != -1:
                        adj[4 * adj[4 * i + 0] + 2] = -1
                    if adj[4 * i + 3] != -1:
                        adj[4 * adj[4 * i + 3] + 1] = -1
                    adj[4 * i + 0] = -1
                    adj[4 * i + 3] = -1
                    print('destab - 12')
                    attempts = 0
                    q.pop(0)
                    q.append(i)
                    effectiveness_flag[0] = 1
                    if draw_knot_flag:
                        draw_knot(a, n, index)
                    if draw_flag:
                        draw_rect(a, sign)
                    continue
                else:
                    a[4 * i + 1] = a[4 * i + 0] + 0.5
                    rescale(a, n)
                    vert = []
                    hor = []
                    v = free_vert(a, n)
                    for j in v:
                        if not (j[0] in vert):
                            vert.append(j[0])
                        if not (j[1] in hor):
                            hor.append(j[1])
                    if draw_flag:
                        draw_rect(a, sign)
                    
            if adj[4 * i + 2] == -1 and adj[4 * i + 3] == -1 and  sign[i] == -1:
                if not (a[4 * i + 3] in hor):
                    hor.remove(a[4 * i + 2])
                    hor.append(a[4 * i + 3])
                    a[4 * i + 0] = 0
                    a[4 * i + 1] = 0
                    a[4 * i + 2] = 0
                    a[4 * i + 3] = 0
                    if adj[4 * i + 0] != -1:
                        adj[4 * adj[4 * i + 0] + 2] = -1
                    if adj[4 * i + 1] != -1:
                        adj[4 * adj[4 * i + 1] + 3] = -1
                    adj[4 * i + 0] = -1
                    adj[4 * i + 1] = -1
                    print('destab - 23')
                    attempts = 0
                    q.pop(0)
                    q.append(i)
                    effectiveness_flag[0] = 1
                    if draw_knot_flag:
                        draw_knot(a, n, index)
                    if draw_flag:
                        draw_rect(a, sign)
                    continue
                else:
                    a[4 * i + 2] = a[4 * i + 3] - 0.5
                    rescale(a, n)
                    vert = []
                    hor = []
                    v = free_vert(a, n)
                    for j in v:
                        if not (j[0] in vert):
                            vert.append(j[0])
                        if not (j[1] in hor):
                            hor.append(j[1])
                    if draw_flag:
                        draw_rect(a, sign)
                    
        q.pop(0)
        q.append(i)
        attempts = attempts + 1
    print('Было:', len(a), n, len(sign))
    big_check_function(a, n, sign)
    return delete_zeroes(a, n, sign)

def filt_hor(vert):
    ar = []
    for i in range(len(vert)):
        if(vert[i][1] == vert[(i + 1) % len(vert)][1]):
            ar.append([vert[i][1], vert[i][0], vert[(i + 1) % len(vert)][0]])
    return ar

def filt_vert(vert):
    ar = []
    for i in range(len(vert)):
        if(vert[i][0] == vert[(i + 1) % len(vert)][0]):
            ar.append([vert[i][0], vert[i][1], vert[(i + 1) % len(vert)][1]])
    return ar

def draw_knot(a, n, index):
    #plt.figure(figsize = (20, 10))
    n = len(a) // 4
    v = free_vert(a, n)
    v.sort(key = lambda x: x[1])
    hor_e = sorted(filt_hor(v), key = lambda x: x[0])
    v.sort(key = lambda x: x[0])
    vert_e = sorted(filt_vert(v), key = lambda x: x[0])

    for i in vert_e:
        plt.plot([i[0], i[0]], [i[1] ,i[2]], color = [1, 0, 0, 0.5])
    for i in hor_e:
        plt.plot([i[1], i[2]], [i[0] ,i[0]], color = [1, 0, 0, 0.5])
    plt.savefig('qwe', format = 'eps')
    #plt.savefig('qwe' + str(index[0]), format = 'eps')

    index[0] = index[0] + 1
    #plt.show()

def fast_simplify(a, n, sign, adj, effectiveness_flag):
    draw_flag = Absolut_draw_flag[0]
    q = []
    rescale(a, n)
    counter = 0
    print("ИЩЕМ СКЛАДОЧКИ")

    # draw_rect(a, adj)
    
    q = []
    for i in range(n):
        q.append(i)

    # print('После складочек')
    # draw_rect(a, adj)

    vert = only_vertices(a, n)
    # for i in range(n):
    #     q.append(i)
    attempts = 0
    while attempts < n:
        #print(counter)
        #КОСТЫЛЬ НИЖЕ ВЕРТ = ОНЛИ ВЕРТИСЕС
        #vert = only_vertices(a, n)
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
                if adj[4 * l + 1] == adj[4 * r + 0] and adj[4 * r + 0] != -1 and check_vert_rect(a[4 * cur + 0], a[4 * cur + 1], a[4 * cur + 3], a[4 * cur + 2], vert):
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
            

            if cur == start and check_vert_rect(a[4 * cur + 0], a[4 * cur + 1], a[4 * cur + 3], a[4 * cur + 2], vert):
                if len(left) > 1:
                    flag = 0
                    break
                #draw_rect(a)
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
                big_check_function(a, n, sign)
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
                if adj[4 * u + 3] == adj[4 * d + 0] and adj[4 * d + 0] != -1 and check_vert_rect(a[4 * cur + 1], a[4 * cur + 0], a[4 * cur + 2], a[4 * cur + 3], vert):
                    up.append(u)
                    down.append(d)
                    mid.append(cur)
                    cur = adj[4 * u + 3]
                else:
                    cur = -1
                    break
                if cur == start:
                    break

            if cur == start and check_vert_rect(a[4 * cur + 1], a[4 * cur + 0], a[4 * cur + 2], a[4 * cur + 3], vert):
                print('simplify 2')   
                if len(mid) > 1:
                    flag = 0     
                    break        
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

                big_check_function(a, n, sign)
                flag = 0
                # print('cimpl case 2')
                # draw_rect(a)

        q.pop(0)
        q.append(start)
        if flag:
            attempts = attempts + 1
        else:
            draw_rect(a, sign)
            effectiveness_flag[0] = 1
            attempts = 0

    q = []
    attempts = 0
    for i in range(n):
        q.append(i)


    while attempts < n:
        #тут добавилась очередь. раньше ее не было
        i = q[0]
        v = free_vert(a, n)
        vert = []
        hor = []
        for t in v:
            vert.append(t[0])
            hor.append(t[1])

        # if i >= 58:
        #     for i in range(n):
        #         print(i, a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3], adj[4 * i + 0], adj[4 * i + 1], adj[4 * i + 2], adj[4 * i + 3])
        #     print('34!!!')
        #     draw_rect(a, adj)

        if a[4 * i] != 0 and adj[4 * i + 0] != -1:
            # and a[4 * i] < a[4 * i + 1] and a[4 * adj[4 * i]] < a[4 * adj[4 * i] + 1]
            if  adj[4 * adj[4 * i + 0] + 1] == i  and (not (a[4 * i + 1] in vert) or not (a[4 * adj[4 * i + 0] + 0] in vert)):
                if adj[4 * adj[4 * i + 0] + 0] == i and adj[4 * adj[4 * i + 0] + 3] == i:
                    print('удаляем сферу')
                    if draw_flag:
                        draw_rect(a, sign)
                    a[4 * i + 0] = 0
                    a[4 * i + 1] = 0
                    a[4 * i + 2] = 0
                    a[4 * i + 3] = 0
                    a[4 * adj[4 * i + 0] + 0] = 0
                    a[4 * adj[4 * i + 0] + 1] = 0
                    a[4 * adj[4 * i + 0] + 2] = 0
                    a[4 * adj[4 * i + 0] + 3] = 0

                    #rescale(a, n)
                    #adj = delete_zeroes(a, n, sign)
                    #n = len(a) // 4
                    attempts = 0
                    q.pop(0)
                    q.append(i)
                    print('sphere deleted')
                    if draw_flag:
                        draw_rect(a, sign)
                    continue
                    
                print('нашлося')
                if  a[4 * adj[4 * i]] > a[4 * adj[4 * i] + 1]:
                    print('imhere', a[4 * adj[4 * i]], a[4 * adj[4 * i] + 1] )
                    print(a[4 * adj[4 * i] + 0], a[4 * adj[4 * i] + 1], a[4 * adj[4 * i] + 2], a[4 * adj[4 * i] + 3])
                    #draw_rect(a, sign)
                    left_edge = a[4 * adj[4 * i]]
                    m = 0
                    for u in range(len(vert)):
                        m = max(vert[u], m)
                    m += 2
                    for k in range(n):
                        if a[4 * k] == 0:
                            continue
                        if a[4 * k + 0] < left_edge:
                            a[4 * k + 0] = a[4 * k + 0] + m - left_edge + 1
                        else:
                            a[4 * k + 0] = a[4 * k + 0] - left_edge + 1
                        if a[4 * k + 1] < left_edge:
                            a[4 * k + 1] = a[4 * k + 1] + m - left_edge + 1
                        else:
                            a[4 * k + 1] = a[4 * k + 1] - left_edge + 1
                    # draw_rect(a, adj)
                elif  a[4 * i] > a[4 * i + 1]:
                    print('imhere -- 2')
                    left_edge = a[4 * i + 1]
                    m = 0
                    for u in range(len(vert)):
                        m = max(vert[u], m)
                    m += 2
                    for k in range(n):
                        if a[4 * k] == 0:
                            continue
                        if a[4 * k + 0] <= left_edge:
                            a[4 * k + 0] = a[4 * k + 0] + m - left_edge + 1
                        else:
                            a[4 * k + 0] = a[4 * k + 0] - left_edge + 1
                        if a[4 * k + 1] <= left_edge:
                            a[4 * k + 1] = a[4 * k + 1] + m - left_edge + 1
                        else:
                            a[4 * k + 1] = a[4 * k + 1] - left_edge + 1

                if draw_flag:
                    draw_rect(a, sign)
                theta_1 = a[4 * adj[4 * i] + 0]
                theta_2 = a[4 * i + 0]
                theta_3 = a[4 * i + 1]
                for p in range(n):
                    if a[4 * p + 0] < theta_2 and a[4 * p + 0] >= theta_1:
                        a[4 * p + 0] = a[4 * p + 0] - theta_2 + theta_3
                    elif a[4 * p + 0] > theta_2 and a[4 * p + 0] <= theta_3:
                        a[4 * p + 0] = a[4 * p + 0] - theta_2 + theta_1
                    if a[4 * p + 1] < theta_2 and a[4 * p + 1] >= theta_1:
                        a[4 * p + 1] = a[4 * p + 1] - theta_2 + theta_3
                    elif a[4 * p + 1] > theta_2 and a[4 * p + 1] <= theta_3:
                        a[4 * p + 1] = a[4 * p + 1] - theta_2 + theta_1
                if adj[4 * i + 1] > -1:
                    adj[4 * adj[4 * i + 1] + 3] = adj[4 * adj[4 * i + 0] + 3]
                if adj[4 * i + 2] > -1:
                    adj[4 * adj[4 * i + 2] + 0] = adj[4 * adj[4 * i + 0] + 0]
                #и ниже и выше могут быть ошибки

                if adj[4 * adj[4 * i + 0] + 0] > -1:
                    adj[4 * adj[4 * adj[4 * i + 0] + 0] + 2] = adj[4 * i + 2]
                if adj[4 * adj[4 * i + 0] + 3] > -1:
                    adj[4 * adj[4 * adj[4 * i + 0] + 3] + 1] = adj[4 * i + 1]


                a[4 * i + 0] = 0
                a[4 * i + 1] = 0
                a[4 * i + 2] = 0
                a[4 * i + 3] = 0
                a[4 * adj[4 * i] + 0] = 0
                a[4 * adj[4 * i] + 1] = 0
                a[4 * adj[4 * i] + 2] = 0
                a[4 * adj[4 * i] + 3] = 0
                adj[4 * adj[4 * i + 0] + 0] = -1
                adj[4 * adj[4 * i + 0] + 1] = -1
                adj[4 * adj[4 * i + 0] + 2] = -1
                adj[4 * adj[4 * i + 0] + 3] = -1
                adj[4 * i + 0] = -1
                adj[4 * i + 1] = -1
                adj[4 * i + 2] = -1
                adj[4 * i + 3] = -1
                rescale(a, n)

                attempts = 0
                q.pop(0)
                q.append(i)
                effectiveness_flag[0] = 1
                print('А ВОТ И НАШЛАСЬ ОДНА (вертикальная)')
                if draw_flag:
                    draw_rect(a, sign)
                big_check_function(a, n, sign)
                continue
                #draw_rect(a)
        if a[4 * i] != 0 and adj[4 * i + 3] != -1:
            if adj[4 * adj[4 * i + 3] + 0] == i and (not(a[4 * i + 3] in hor) or not (a[4 * adj[4 * i + 3] + 2] in hor)):
                if adj[4 * adj[4 * i + 3] + 2] == i and adj[4 * adj[4 * i + 3] + 3] == i:
                    a[4 * i + 0] = 0
                    a[4 * i + 0] = 0
                    a[4 * i + 0] = 0
                    a[4 * i + 0] = 0
                    a[4 * adj[4 * i + 3] + 0] = 0
                    a[4 * adj[4 * i + 3] + 1] = 0
                    a[4 * adj[4 * i + 3] + 2] = 0
                    a[4 * adj[4 * i + 3] + 3] = 0
                    attempts = 0
                    q.pop(0)
                    q.append(i)
                    print('sphere deleted hor')
                    if draw_flag:
                        draw_rect(a, sign)
                    continue
                #кусок по перетягиванию некоторых прямоугольников в видимую область
                if  a[4 * adj[4 * i + 3] + 2] > a[4 * adj[4 * i + 3] + 3]:
                    # draw_rect(a, adj)
                    left_edge = a[4 * adj[4 * i + 3] + 2] #left = down edge
                    m = 0
                    for u in range(len(hor)):
                        m = max(hor[u], m)
                    m += 2
                    for k in range(n):
                        if a[4 * k + 2] == 0:
                            continue
                        if a[4 * k + 2] < left_edge:
                            a[4 * k + 2] = a[4 * k + 2] + m - left_edge + 1
                        else:
                            a[4 * k + 2] = a[4 * k + 2] - left_edge + 1

                        if a[4 * k + 3] < left_edge:
                            a[4 * k + 3] = a[4 * k + 3] + m - left_edge + 1
                        else:
                            a[4 * k + 3] = a[4 * k + 3] - left_edge + 1
                    # draw_rect(a, adj)
                elif a[4 * i + 2] > a[4 * i + 3]:
                    print('imhere -- 2')
                    left_edge = a[4 * i + 3]
                    m = 0
                    for u in range(len(hor)):
                        m = max(hor[u], m)
                    m += 2
                    for k in range(n):
                        if a[4 * k + 2] == 0:
                            continue
                        if a[4 * k + 2] <= left_edge:
                            a[4 * k + 2] = a[4 * k + 2] + m - left_edge + 1
                        else:
                            a[4 * k + 2] = a[4 * k + 2] - left_edge + 1
                        if a[4 * k + 3] <= left_edge:
                            a[4 * k + 3] = a[4 * k + 3] + m - left_edge + 1
                        else:
                            a[4 * k + 3] = a[4 * k + 3] - left_edge + 1


                print('нашлося hor')
                # draw_rect(a)
                theta_1 = a[4 * adj[4 * i + 3] + 2]
                theta_2 = a[4 * i + 2]
                theta_3 = a[4 * i + 3]
                for p in range(n):
                    if a[4 * p + 2] < theta_2 and a[4 * p + 2] >= theta_1:
                        a[4 * p + 2] = a[4 * p + 2] - theta_2 + theta_3
                    elif a[4 * p + 2] > theta_2 and a[4 * p + 2] <= theta_3:
                        a[4 * p + 2] = a[4 * p + 2] - theta_2 + theta_1
                    if a[4 * p + 3] < theta_2 and a[4 * p + 3] >= theta_1:
                        a[4 * p + 3] = a[4 * p + 3] - theta_2 + theta_3
                    elif a[4 * p + 3] > theta_2 and a[4 * p + 3] <= theta_3:
                        a[4 * p + 3] = a[4 * p + 3] - theta_2 + theta_1
                if adj[4 * i + 0] > -1:
                    adj[4 * adj[4 * i + 0] + 2] = adj[4 * adj[4 * i + 3] + 2]
                if adj[4 * i + 1] > -1:
                    adj[4 * adj[4 * i + 1] + 3] = adj[4 * adj[4 * i + 3] + 3]
                #и ниже и выше могут быть ошибки

                if adj[4 * adj[4 * i + 3] + 2] > -1:
                    adj[4 * adj[4 * adj[4 * i + 3] +2] + 0] = adj[4 * i + 0]
                if adj[4 * adj[4 * i + 3] + 3] > -1:
                    adj[4 * adj[4 * adj[4 * i + 3] + 3] + 1] = adj[4 * i + 1]


                a[4 * i + 0] = 0
                a[4 * i + 1] = 0
                a[4 * i + 2] = 0
                a[4 * i + 3] = 0
                a[4 * adj[4 * i + 3] + 0] = 0
                a[4 * adj[4 * i + 3] + 1] = 0
                a[4 * adj[4 * i + 3] + 2] = 0
                a[4 * adj[4 * i + 3] + 3] = 0
                adj[4 * adj[4 * i + 3] + 0] = -1
                adj[4 * adj[4 * i + 3] + 1] = -1
                adj[4 * adj[4 * i + 3] + 2] = -1
                adj[4 * adj[4 * i + 3] + 3] = -1
                adj[4 * i + 0] = -1
                adj[4 * i + 1] = -1
                adj[4 * i + 2] = -1
                adj[4 * i + 3] = -1
                rescale(a, n)
                attempts = 0
                q.pop(0)
                q.append(i)
                effectiveness_flag[0] = 1
                print('А ВОТ И НАШЛАСЬ ОДНА (horizontal)')
                big_check_function(a, n, sign)
                continue
                #draw_rect(a)
        attempts += 1
        q.pop(0)
        q.append(i)
    adj = delete_zeroes(a, n, sign)
    n = len(a) // 4
    # print('after simplify')
    # draw_rect(a)
    print('att = ', attempts, 'counter = ', counter)
    # print(q)
    # for i in range(n):
    #     print(i, a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3], 'adj', adj[4 * i + 0], adj[4 * i + 1], adj[4 * i + 2], adj[4 * i + 3], 'sign', sign[i])
    if len(a) != len(adj):
        print('BEFORE DESTAB')
    adj = destabilizations(a, n, sign, adj, 1, effectiveness_flag)
    n = len(a) // 4
    big_check_function(a, n, sign)
    #input()
    if len(a) != len(adj):
        print('AFTER DESTAB')
    return adj
  
def big_check_function(a, n, sign):
    vert_orientation = []
    rect_v = []
    free = free_vert_new(a, n, vert_orientation, rect_v)
    len_free = len(free)
    #sort
    for i in range(1, len_free - 1):
        for j in range(len_free - i):
            
            if free[j][i % 2] == free[len_free - i][i % 2]:
                #print('hehehe', free, i, j)
                tmp0 = free[len_free - i - 1]
                free[len_free - i - 1]= free[j]
                free[j] = tmp0

                tmp2 = vert_orientation[j]
                vert_orientation[j] = vert_orientation[len_free - i - 1]
                vert_orientation[len_free - i - 1] = tmp2

                tmp3 = rect_v[j]
                rect_v[j] = rect_v[len_free - i - 1]
                rect_v[len_free - i - 1] = tmp3

                break
    if free[0][0] != free[len_free - 1][0] and free[0][1] != free[len_free - 1][1]:
        print('не узел, а зацепление подсунули')
        costyl = [0]
        draw_knot(a, n, costyl)


    #return
    rect
    r = []
    for i in range(len(a) // 4):
        r.append([a[4 * i + 0], a[4 * i + 2], a[4 * i + 1], a[4 * i + 3]])
    check_all([r], sign)
    check_orient(a, n, sign)

    v = vertices(a, n)
    for i in range(n):
        if check_vert_rect_modified(a[4 * i + 0], a[4 * i + 0], a[4 * i + 0], a[4 * i + 0], v) == 0:
            print("Всё очень плохо")
            if check_orient(a, n, sign):
                print('orientations is okey')
                input()
            else:
                print('Все еще хуже чем мы думали')
            print('a = ', a, n, 'sign = ', sign)
            input()
            return

#ТЯЖЕЛАЯ ФУНКЦИЯ НО МБ БОЛЕЕ НАДЕЖНАЯ
def check_all(r, sign):
    for i in r:
        for j in i:
            for k in r:
                for l in k:
                    result = 0
                    if l == j:
                        continue
                    if j[1] > j[3]:
                        if l[1] > l[3]:
                            if l[2] < j[0] or l[0] > j[2] or (l[0] < j[0] and l[2] > j[2] and l[1] > j[1] and l[3] < j[3]) or (j[0] < l[0] and j[2] > l[2] and j[1] > l[1] and j[3] < l[3]):
                                result = 1
                        else:
                            if (l[1] > j[3] and l[3] < j[1]) or l[2] < j[0] or l[0] > j[2]:
                                result = 1
                            #share verice or two
                            if (l[3] <= j[1] and l[1] >= j[3]) and (l[2] <= j[0] or l[0] >= j[2]):
                                result = 1
                            #good intersection
                            if (l[1] > j[1] or l[3] < j[3]) and l[0] < j[0] and l[2] > j[2]:
                                result = 1
                    else:
                        if l[1] > l[3]:
                            if (j[1] > l[3] and j[3] < l[1]) or j[2] < l[0] or j[0] > l[2]:
                                result = 1
                            #share verice or two
                            if (j[3] <= l[1] and j[1] >= l[3]) and (j[2] <= l[0] or j[0] >= l[2]):
                                result = 1
                            #good intersection
                            if (j[1] > l[1] or j[3] < l[3]) and j[0] < l[0] and j[2] > l[2]:
                                result = 1
                        else:
                            #dosent intersect
                            if l[2] < j[0] or l[0] > j[2] or j[1] > l[3] or j[3] < l[1]:
                                result = 1
                            #share a vertice
                            if ((l[0] >= j[2] or l[2] <= j[0]) and l[1] >= j[3]) or ((l[0] >= j[2] or l[2] <= j[0]) and l[3] <= j[1]):
                                result = 1
                            #good intersection
                            if j[0] < l[0] and j[2] > l[2] and j[1] > l[1] and j[3] < l[3]:
                                result = 1
                            if l[0] < j[0] and l[2] > j[2] and l[1] > j[1] and l[3] < j[3]:
                                result = 1
                    if result != 1:
                        
                        print('ahahaha')
                        print(l, j)
                        rects = []
                        for ppp in r:
                            for qqq in ppp:                                
                                rects.append(qqq[0])
                                rects.append(qqq[1])
                                rects.append(qqq[2])
                                rects.append(qqq[3])
                        print('rects = ', rects)
                        draw_rect(rects, sign)
                        #input()

def sharing_vertex(a, i, j):
    v = [[a[4 * i + 0], a[4 * i  + 2]],
        [a[4 * i + 0], a[4 * i  + 3]],
        [a[4 * i + 1], a[4 * i  + 2]],
        [a[4 * i + 1], a[4 * i  + 3]]]
    if [a[4 * j + 0], a[4 * j + 2]] in v:
        return 1
    if [a[4 * j + 0], a[4 * j + 3]] in v:
        return 1
    if [a[4 * j + 1], a[4 * j + 2]] in v:
        return 1
    if [a[4 * j + 1], a[4 * j + 3]] in v:
        return 1
    return 0

def sharing_pair_vertices(i1, j1, i2, j2, adj):
    if adj[4 * i1 + 0] == j2 and adj[4 * j1 + 0] == i2:
        return 0
    if adj[4 * i1 + 1] == j2 and adj[4 * j1 + 1] == i2:
        return 1
    if adj[4 * i1 + 2] == j2 and adj[4 * j1 + 2] == i2:
        return 2
    if adj[4 * i1 + 3] == j2 and adj[4 * j1 + 3] == i2:
        return 3
    return -1
def define_rect_graph(a, n, sign, adj):
    rect_graph = []
    for i in range(n):
        if sign[i] == -1:
            #завели массив, которые будут покрывать (или лежать под) i-ым
            covering_rects = []
            for j in range(n):
                if sign[j] == 1 and compare(a[4 * j + 0], a[4 * j + 1], a[4 * j + 2], a[4 * j + 3], a[4 * i + 0], a[4 * i + 1], a[4 * i+ 2], a[4 * i + 3]):
                    #проверяем, что между ничего нет. вместе с тем, если он сам не подходит, то мы его и не добавим
                    flag = 1
                    remove_list = []
                    for k in range(len(covering_rects)):
                        if compare(a[4 * covering_rects[k] + 0], a[4 * covering_rects[k] + 1], a[4 * covering_rects[k]+ 2], a[4 * covering_rects[k] + 3], a[4 * j + 0], a[4 * j + 1], a[4 * j + 2], a[4 * j + 3]):
                            remove_list.append(covering_rects[k])
                        if compare(a[4 * j + 0], a[4 * j + 1], a[4 * j + 2], a[4 * j + 3],a[4 * covering_rects[k] + 0], a[4 * covering_rects[k] + 1], a[4 * covering_rects[k]+ 2], a[4 * covering_rects[k] + 3]):
                            flag = 0
                    if flag:
                        covering_rects.append(j)
                    for k in remove_list:
                        covering_rects.remove(k)
            for j in range(n):
                if sign[j] == -1 and compare(a[4 * j + 0], a[4 * j + 1], a[4 * j+ 2], a[4 * j + 3], a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3]):
                    remove_list = []
                    for k in range(len(covering_rects)):
                        if compare(a[4 * covering_rects[k] + 0], a[4 * covering_rects[k] + 1], a[4 * covering_rects[k]+ 2], a[4 * covering_rects[k] + 3], a[4 * j + 0], a[4 * j + 1], a[4 * j + 2], a[4 * j + 3]):
                            remove_list.append(covering_rects[k])
                    for k in remove_list:
                        covering_rects.remove(k)
            for l in covering_rects:
                rect_graph.append([i, l])
                print(i, l)
                print(a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3])
                print(a[4 * l + 0], a[4 * l + 1], a[4 * l + 2], a[4 * l + 3])


    vertices = only_vertices(a, n)
    g = [[] for i in range(len(rect_graph))]
    for i in range(len(rect_graph)):
        for j in range(len(rect_graph)):
            if j >= i:
                continue
            s_p_v = sharing_pair_vertices(rect_graph[i][0], rect_graph[i][1], rect_graph[j][0], rect_graph[j][1], adj)
            if s_p_v != -1:
                if  s_p_v == 0 and check_vert_rect_modified(a[4 * rect_graph[i][1]], a[4 * rect_graph[i][0]],  a[4 * rect_graph[i][1] + 3], a[4 * rect_graph[i][0] + 3],  vertices):
                    g[i].append(j)
                    g[j].append(i)
                elif s_p_v == 1 and check_vert_rect_modified(a[4 * rect_graph[i][0] + 1], a[4 * rect_graph[i][1] + 1], a[4 * rect_graph[i][1] + 3], a[4 * rect_graph[i][0] + 3], vertices):
                    g[i].append(j)
                    g[j].append(i)
                elif s_p_v == 2 and check_vert_rect_modified(a[4 * rect_graph[i][0] + 1], a[4 * rect_graph[i][1] + 1], a[4 * rect_graph[i][0] + 2], a[4 * rect_graph[i][1] + 2], vertices):
                    g[i].append(j)
                    g[j].append(i)
                elif s_p_v == 3 and check_vert_rect_modified(a[4 * rect_graph[i][1] + 0], a[4 * rect_graph[i][0] + 0], a[4 * rect_graph[i][0] + 2], a[4 * rect_graph[i][1] + 2], vertices):
                    g[i].append(j)
                    g[j].append(i)
    return g, rect_graph

def dfs(v, cl, g, p, end, st):
    cl[v] = 1
    for i in range(len(g[v])):
        v_to = g[v][i]
        if p[v] == v_to:
            continue
        if (cl[v_to] == 0):
            p[v_to] = v
            if (dfs(v_to, cl, g, p, end, st) == 1):
                return 1
        elif (cl[v_to] == 1):
            end[0] = v
            st[0] = v_to
            return 1
    cl[v] = 2
    return 0

def dfs_components(v, used, comp, adj):
    used[v] = 1
    comp.append(v)
    for i in range(4):
        v_to = adj[4 * v + i]
        if v_to == -1:
            continue
        if used[v_to] == 0:
            dfs_components(v_to, used, comp, adj)

def draw_rect_graph(g, rect_graph, a, sign, adj):
    print('GENUS = ', genus(a, len(a) // 4))
    a_cpy = a.copy()
    sign_cpy = sign.copy()
    sort_rect(a_cpy, len(a) // 4, sign_cpy)
    #big_check_function(a_cpy, len(a) // 4, sign_cpy)
    plt.figure(figsize = (20, 10))
    y_min = 0
    x_min = 0
    x_max = 1
    y_max = 1
    e = 0.05
    for i in range(len(a_cpy) // 4):
        if a_cpy[4 * i] > x_max:
            x_max = a_cpy[4 * i]
        if a_cpy[4 * i + 1] > x_max:
            x_max = a_cpy[4 * i + 1]
        if a_cpy[4 * i + 2] > y_max:
            y_max = a_cpy[4 * i + 2]
        if a_cpy[4 * i + 3] > y_max:
            y_max = a_cpy[4 * i + 3]
    x_max = x_max + 2
    y_max = y_max + 2      

    for i in range(len(rect_graph)):
        a_cpy.append(a[4 * rect_graph[i][0] + 0])
        a_cpy.append(a[4 * rect_graph[i][0] + 1])
        a_cpy.append(a[4 * rect_graph[i][1] + 2])
        a_cpy.append(a[4 * rect_graph[i][1] + 3])
        sign_cpy.append(2)

    for i in range(len(a_cpy) // 4):
        if sign_cpy[i] in [1, -1]:
            c = [0.2, 0.2, 0.45 + 0.3 * sign_cpy[i], 0.5]
        else:
            c = [1, 1, 0, 0.5]
        white = [1, 1, 1, 1]
        whiteindex = 1
        if a_cpy[4 * i + 2] > a_cpy[4 * i + 3] and a_cpy[4 * i] > a_cpy[4 * i + 1]:
            # правильная отрисовка
            if whiteindex:
                plt.fill([a_cpy[4 * i] - e, a_cpy[4 * i] - e, x_max, x_max], [a_cpy[4 * i + 2], y_max, y_max, a_cpy[4 * i + 2]], color =  white)
                plt.fill([a_cpy[4 * i + 1] + e, a_cpy[4 * i + 1] + e, x_min, x_min], [a_cpy[4 * i + 2], y_max, y_max, a_cpy[4 * i + 2]], color =  white)
                plt.fill([a_cpy[4 * i] - e, a_cpy[4 * i] - e, x_max, x_max], [a_cpy[4 * i + 3], y_min, y_min, a_cpy[4 * i + 3]], color =  white)
                plt.fill([a_cpy[4 * i + 1] + e, a_cpy[4 * i + 1] + e, x_min, x_min], [a_cpy[4 * i + 3], y_min, y_min, a_cpy[4 * i + 3]], color =  white)

            plt.fill([a_cpy[4 * i], a_cpy[4 * i], x_max, x_max], [a_cpy[4 * i + 2], y_max, y_max, a_cpy[4 * i + 2]], color =  c)
            plt.fill([a_cpy[4 * i + 1], a_cpy[4 * i + 1], x_min, x_min], [a_cpy[4 * i + 2], y_max, y_max, a_cpy[4 * i + 2]], color =  c)
            plt.fill([a_cpy[4 * i], a_cpy[4 * i], x_max, x_max], [a_cpy[4 * i + 3], y_min, y_min, a_cpy[4 * i + 3]], color = c)
            plt.fill([a_cpy[4 * i + 1], a_cpy[4 * i + 1], x_min, x_min], [a_cpy[4 * i + 3], y_min, y_min, a_cpy[4 * i + 3]], color = c)
            continue
        if a_cpy[4 * i + 2] < a_cpy[4 * i + 3] and a_cpy[4 * i] < a_cpy[4 * i + 1]:
            if whiteindex:
                plt.fill([a_cpy[4 * i] - e, a_cpy[4 * i] - e, a_cpy[4 * i + 1] + e, a_cpy[4 * i + 1] + e], [a_cpy[4 * i + 2], a_cpy[4 * i + 3], a_cpy[4 * i + 3], a_cpy[4 * i + 2]], color = white)
            
            plt.fill([a_cpy[4 * i], a_cpy[4 * i], a_cpy[4 * i + 1], a_cpy[4 * i + 1]], [a_cpy[4 * i + 2], a_cpy[4 * i + 3], a_cpy[4 * i + 3], a_cpy[4 * i + 2]], color = c)
        if a_cpy[4 * i + 2] > a_cpy[4 * i + 3]:
            if whiteindex:
                plt.fill([a_cpy[4 * i] - e, a_cpy[4 * i] - e, a_cpy[4 * i + 1] + e, a_cpy[4 * i + 1] + e], [a_cpy[4 * i + 2], y_max, y_max, a_cpy[4 * i + 2]], color =  white)
                plt.fill([a_cpy[4 * i] - e, a_cpy[4 * i] - e, a_cpy[4 * i + 1] + e, a_cpy[4 * i + 1] + e], [y_min, a_cpy[4 * i + 3], a_cpy[4 * i + 3], y_min], color =  white)

            plt.fill([a_cpy[4 * i], a_cpy[4 * i], a_cpy[4 * i + 1], a_cpy[4 * i + 1]], [a_cpy[4 * i + 2], y_max, y_max, a_cpy[4 * i + 2]], color =  c)
            plt.fill([a_cpy[4 * i], a_cpy[4 * i], a_cpy[4 * i + 1], a_cpy[4 * i + 1]], [y_min, a_cpy[4 * i + 3], a_cpy[4 * i + 3], y_min], color =  c)
        if a_cpy[4 * i] > a_cpy[4 *i + 1]:
            if whiteindex:
                plt.fill([x_min, x_min, a_cpy[4 * i + 1] + e, a_cpy[4 * i + 1] + e], [a_cpy[4 * i + 2], a_cpy[4 * i + 3], a_cpy[4 * i + 3], a_cpy[4 * i + 2]], color =  white)
                plt.fill([a_cpy[4 * i] - e, a_cpy[4 * i] - e, x_max, x_max], [a_cpy[4 * i + 2], a_cpy[4 * i + 3], a_cpy[4 * i + 3], a_cpy[4 * i + 2]], color =  white)

            plt.fill([x_min, x_min, a_cpy[4 * i + 1], a_cpy[4 * i + 1]], [a_cpy[4 * i + 2], a_cpy[4 * i + 3], a_cpy[4 * i + 3], a_cpy[4 * i + 2]], color =  c)
            plt.fill([a_cpy[4 * i], a_cpy[4 * i], x_max, x_max], [a_cpy[4 * i + 2], a_cpy[4 * i + 3], a_cpy[4 * i + 3], a_cpy[4 * i + 2]], color =  c)
    b = free_vert(a_cpy, len(a) // 4)
    for i in range(len(g)):
        for j in range(len(g[i])):
            plt.plot([(a[4 * rect_graph[i][0] + 0] + a[4 * rect_graph[i][0] + 1])/2. if a[4 * rect_graph[i][0] + 0] < a[4 * rect_graph[i][0] + 1] else x_max, 
            (a[4 * rect_graph[g[i][j]][0] + 0] + a[4 * rect_graph[g[i][j]][0] + 1])/2. if a[4 * rect_graph[g[i][j]][0] + 0] < a[4 * rect_graph[g[i][j]][0] + 1] else x_max],
             [(a[4 * rect_graph[i][1] + 2] + a[4 * rect_graph[i][1] + 3])/2. if a[4 * rect_graph[i][1] + 2] < a[4 * rect_graph[i][1] + 3] else y_max, 
             (a[4 * rect_graph[g[i][j]][1] + 2] + a[4 * rect_graph[g[i][j]][1] + 3])/2. if a[4 * rect_graph[g[i][j]][1] + 2] < a[4 * rect_graph[g[i][j]][1] + 3] else y_max],
         'bo', linestyle="--")

    for i in range(len(b)):
        if b[i][0] != 0:
            plt.scatter(b[i][0], b[i][1], marker = 'o')
    # print('rect = ', a)
    # print('sign = ', sign)
    # print(len(a), len(sign), len(adj))
    # for i in range(len(sign)):
    #     print(i, a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], a[4 * i + 3], adj[4 * i + 0], adj[4 * i + 1], adj[4 * i + 2], adj[4 * i + 3])
    plt.savefig('rect_graph', format = 'eps')
    plt.show()
    return

def search_circle(a, n, sign, adj):
    draw_flag = Absolut_draw_flag[0]
    n = len(a) // 4
    g, rect_graph = define_rect_graph(a, n, sign, adj)
    #draw_rect(a, sign)
    #draw_rect_graph(g, rect_graph, a, sign, n)
    i = 0
    print("rectangl")
    # for i in range(len(rect_graph)):
    #     print(rect_graph[i][0], rect_graph[i][1], g[i])
    #     print(a[4 * rect_graph[i][0] + 0], a[4 * rect_graph[i][0] + 1], a[4 * rect_graph[i][0] + 2], a[4 * rect_graph[i][0] + 3])
    #     print(a[4 * rect_graph[i][1] + 0], a[4 * rect_graph[i][1] + 1], a[4 * rect_graph[i][1] + 2], a[4 * rect_graph[i][1] + 3])
    if draw_flag:
        draw_rect(a, sign)
    #input()
    i = 0
    while i < len(rect_graph):
        # print(i)
        cl = [0] * len(rect_graph)
        p = [-1] * len(rect_graph)
        end = [-1]
        st = [-1]
        if dfs(i, cl, g, p, end, st):
            print("We found it!")
            cur = end[0]
            # while cur != st[0]:
            #     print(cur, g[cur], p[cur])
            #     print(a[4 * rect_graph[cur][0] + 0], a[4 * rect_graph[cur][0] + 1], a[4 * rect_graph[cur][0] + 2], a[4 * rect_graph[cur][0] + 3])
            #     print(a[4 * rect_graph[cur][1] + 0], a[4 * rect_graph[cur][1] + 1], a[4 * rect_graph[cur][1] + 2], a[4 * rect_graph[cur][1] + 3])
            #     cur = p[cur]
            # print(cur, g[cur], p[cur])
            # print(a[4 * rect_graph[cur][0] + 0], a[4 * rect_graph[cur][0] + 1], a[4 * rect_graph[cur][0] + 2], a[4 * rect_graph[cur][0] + 3])
            # print(a[4 * rect_graph[cur][1] + 0], a[4 * rect_graph[cur][1] + 1], a[4 * rect_graph[cur][1] + 2], a[4 * rect_graph[cur][1] + 3])

            

            cur = end[0]
            p[st[0]] = end[0]
            left_neg = []
            right_neg = []
            top_pos = []
            bot_pos = []
            direction = sharing_pair_vertices(rect_graph[st[0]][0], rect_graph[st[0]][1], rect_graph[cur][0], rect_graph[cur][1], adj)
            #костыль
            fllag = 1
            vertices =  only_vertices(a, n)

            emergency_flag = 0

            while cur != end[0] or fllag:

                fllag = 0
                cur_neg = rect_graph[cur][0]
                cur_pos = rect_graph[cur][1]
                #l left r right b bottom t top
                #neg edges are vertical. pos are horizontal I hope
                neg_lb = [a[4 * cur_neg + 0], a[4 * cur_neg + 2], a[4 * cur_pos + 2]]
                neg_rb = [a[4 * cur_neg + 1], a[4 * cur_neg + 2], a[4 * cur_pos + 2]]
                neg_lt = [a[4 * cur_neg + 0], a[4 * cur_pos + 3], a[4 * cur_neg + 3]]
                neg_rt = [a[4 * cur_neg + 1], a[4 * cur_pos + 3], a[4 * cur_neg + 3]]

                pos_lb = [a[4 * cur_pos + 2], a[4 * cur_pos + 0], a[4 * cur_neg + 0]]
                pos_rb = [a[4 * cur_pos + 2], a[4 * cur_neg + 1], a[4 * cur_pos + 1]]
                pos_lt = [a[4 * cur_pos + 3], a[4 * cur_pos + 0], a[4 * cur_neg + 0]]
                pos_rt = [a[4 * cur_pos + 3], a[4 * cur_neg + 1], a[4 * cur_pos + 1]]
                direction_old = direction
                direction = sharing_pair_vertices(rect_graph[cur][0], rect_graph[cur][1], rect_graph[p[cur]][0], rect_graph[p[cur]][1], adj)
                
                direction_old = (2 + direction_old) % 4
                print(direction, direction_old)

                #убрал эмердженси на время теста
                if 0 in [direction, direction_old]:
                    if check_vert_rect(a[4 * cur_pos + 0], a[4 * cur_neg + 0], a[4 * cur_pos + 3], a[4 * cur_neg + 3] ,vertices)== 0:
                        emergency_flag = 1
                        break
                if 1 in [direction, direction_old]:
                    if check_vert_rect(a[4 * cur_neg + 1], a[4 * cur_pos + 1], a[4 * cur_pos + 3], a[4 * cur_neg + 3] ,vertices) == 0:
                        emergency_flag = 1
                        break

                if 2 in [direction, direction_old]:
                    if check_vert_rect(a[4 * cur_neg + 1], a[4 * cur_pos + 1], a[4 * cur_neg + 2], a[4 * cur_pos + 2] ,vertices) == 0:
                        emergency_flag = 1
                        break

                if 3 in [direction, direction_old]:
                    if check_vert_rect(a[4 * cur_pos + 0], a[4 * cur_neg + 0], a[4 * cur_neg + 2], a[4 * cur_pos + 2] ,vertices) == 0:
                        emergency_flag = 1
                        break

                
                if not (0 in [direction, direction_old]):
                    left_neg.append(neg_lt)
                    top_pos.append(pos_lt)
                if not (1 in [direction, direction_old]):    
                    right_neg.append(neg_rt)
                    top_pos.append(pos_rt)
                if not (2 in [direction, direction_old]):
                    right_neg.append(neg_rb)
                    bot_pos.append(pos_rb)
                if not (3 in [direction, direction_old]):                    
                    left_neg.append(neg_lb)
                    bot_pos.append(pos_lb)
                cur = p[cur]
            
            if 1 and emergency_flag:
                print('emergency_flag')
                i += 1
                continue
                
            print('neg = ', left_neg, right_neg)   
            print('pos = ', bot_pos, top_pos) 
            print('iterator = ', i)
            new_rects_neg = []
            for iterator in range(len(left_neg)):
                for j in range(len(right_neg)):
                    if left_neg[iterator][1] == right_neg[j][1] and left_neg[iterator][2] == right_neg[j][2]:
                        new_rects_neg.append([left_neg[iterator][0], right_neg[j][0], left_neg[iterator][1], left_neg[iterator][2]])
                        right_neg.remove(right_neg[j])
                        break
            new_rects_pos = []
            for iterator in range(len(top_pos)):
                for j in range(len(bot_pos)):
                    if top_pos[iterator][1] == bot_pos[j][1] and top_pos[iterator][2] == bot_pos[j][2]:
                        new_rects_pos.append([bot_pos[j][1], bot_pos[j][2], bot_pos[j][0], top_pos[iterator][0]])
                        bot_pos.remove(bot_pos[j])
                        break
            print(new_rects_neg, new_rects_pos)
            print(bot_pos, top_pos)
            if draw_flag:
                draw_rect(a, sign)
            cur = end[0]
            a_copy = a.copy()
            for iterator in range(len(left_neg)):
                a_copy[4 * rect_graph[cur][0] + 0] = new_rects_neg[iterator][0]
                a_copy[4 * rect_graph[cur][0] + 1] = new_rects_neg[iterator][1]
                a_copy[4 * rect_graph[cur][0] + 2] = new_rects_neg[iterator][2]
                a_copy[4 * rect_graph[cur][0] + 3] = new_rects_neg[iterator][3]

                a_copy[4 * rect_graph[cur][1] + 0] = new_rects_pos[iterator][0]
                a_copy[4 * rect_graph[cur][1] + 1] = new_rects_pos[iterator][1]
                a_copy[4 * rect_graph[cur][1] + 2] = new_rects_pos[iterator][2]
                a_copy[4 * rect_graph[cur][1] + 3] = new_rects_pos[iterator][3]
                cur = p[cur]


            print("Хотим проверить, что не добавили сфер i = ", i)

            new_adj = fill_adjecent(a_copy, len(a_copy) // 4)
            comp = []
            used = [0] * (len(a_copy) // 4)
            dfs_components(0, used, comp, new_adj)
            flag_sphere = 1
            print('genera = ', genus(a, len(a) // 4), genus(a_copy, len(a_copy) // 4))
            if genus(a, len(a) // 4) < genus(a_copy, len(a_copy) // 4):
                flag_sphere = 0
            for iterator in range(len(a_copy) // 4):
                if not (iterator in comp):
                    flag_sphere = 0
                    print(a_copy[4 * iterator + 0], a_copy[4 * iterator + 1], a_copy[4 * iterator + 2])
                    print('сфера таки есть', comp)
                    
                    
            if flag_sphere:

                print('а мы вообще здесь выходим?')
                cur = end[0]
                for iterator in range(len(left_neg)):
                    a[4 * rect_graph[cur][0] + 0] = new_rects_neg[iterator][0]
                    a[4 * rect_graph[cur][0] + 1] = new_rects_neg[iterator][1]
                    a[4 * rect_graph[cur][0] + 2] = new_rects_neg[iterator][2]
                    a[4 * rect_graph[cur][0] + 3] = new_rects_neg[iterator][3]

                    a[4 * rect_graph[cur][1] + 0] = new_rects_pos[iterator][0]
                    a[4 * rect_graph[cur][1] + 1] = new_rects_pos[iterator][1]
                    a[4 * rect_graph[cur][1] + 2] = new_rects_pos[iterator][2]
                    a[4 * rect_graph[cur][1] + 3] = new_rects_pos[iterator][3]
                    cur = p[cur]

                if draw_flag:
                    if emergency_flag:
                        print('хмммммммм')
                    print('а тут мы интересно были?')
                    
                    draw_rect(a, sign)
                return 1
            else:
                
                i += 1
                continue

        i += 1
    return 0

def remove_handle(a, n, sign, adj):
    for i in range(n):
        if a[4 * i] == 0:
            continue
        k = adj[4 * i]
        l = adj[4 * i + 1]
        if k == -1 or l == -1:
            continue
        if k == l:
            continue
        if adj[4 * k + 1] == -1 or adj[4 * l + 0] == -1:
            continue
        free = vertices(a, n)
        if adj[4 * k + 1] == adj[4 * l + 0] and check_vert_rect_modified(a[4 * k + 1], a[4 * l], a[4 * k + 2], a[4 * k + 3], free):
            print(a[4 * i + 0], a[4 * i + 1], a[4 * i + 2], 'а вот теперь к', k, a[4 * k + 0], a[4 * k + 1], a[4 * k + 2])
            m = adj[4 * k + 1]
            a[4 * i + 3] = a[4 * m + 3]
            a[4 * k + 1] = a[4 * l + 1]
            adj[4 * k + 1] = adj[4 * l + 1]
            adj[4 * k + 2] = adj[4 * l + 2]
            adj[4 * i + 0] = adj[4 * m + 0]
            adj[4 * i + 1] = adj[4 * m + 1]
            a[4 * m + 0] = 0
            a[4 * m + 1] = 0
            a[4 * m + 2] = 0
            a[4 * m + 3] = 0
            adj[4 * m + 0] = -1
            adj[4 * m + 1] = -1
            adj[4 * m + 2] = -1
            adj[4 * m + 3] = -1

            a[4 * l + 0] = 0
            a[4 * l + 1] = 0
            a[4 * l + 2] = 0
            a[4 * l + 3] = 0
            adj[4 * l + 0] = -1
            adj[4 * l + 1] = -1
            adj[4 * l + 2] = -1
            adj[4 * l + 3] = -1
            return 1
    return 0

def elementary_rotation(a, n, sign, adj):
    vert_orientation = []
    rect_v = []
    draw_flag = Absolut_draw_flag[0]

    quit_flag = 0

    free = free_vert_new(a, n, vert_orientation, rect_v)
    len_free = len(free)
    #sort
    for i in range(1, len_free - 1):
        #print(i)
        for j in range(len_free - i):
            if free[j][i % 2] == free[len_free - i][i % 2]:
                #print('hehehe', free, i, j)
                tmp0 = free[len_free - i - 1]
                free[len_free - i - 1]= free[j]
                free[j] = tmp0

                tmp2 = vert_orientation[j]
                vert_orientation[j] = vert_orientation[len_free - i - 1]
                vert_orientation[len_free - i - 1] = tmp2

                tmp3 = rect_v[j]
                rect_v[j] = rect_v[len_free - i - 1]
                rect_v[len_free - i - 1] = tmp3

                break
    #следим за вертикальными ребрами
    if free[0][1] == free[1][1]:
        tmp = free[0]
        free.pop(0)
        free.append(tmp)
        tmp2 = vert_orientation[0]
        vert_orientation.pop(0)
        vert_orientation.append(tmp2)
        print('vert orientation тоже надо изменить!!')
        
        tmp3 = rect_v[0]
        rect_v.pop(0)
        rect_v.append(tmp3)
    
    for i in range(len_free):
        if i % 2 == 0:
            if vert_orientation[i] == 1 and vert_orientation[i + 1] == 2 and sign[rect_v[i]] == 1:
                print('ротация произведена1 2')
                
                if draw_flag:
                    draw_rect(a, sign)
                a.append(a[4 * rect_v[i] + 1])
                a.append(a[4 * rect_v[i] + 1] + 0.5)
                a.append(a[4 * rect_v[i] + 3])
                a.append(a[4 * rect_v[i + 1] + 2])
                sign.append(-1)
                n = n + 1
                rescale(a, n)
                print('ротация произведена')
                if draw_flag:
                    draw_rect(a, sign)
                quit_flag = 1
                
            if vert_orientation[i] == 2 and vert_orientation[i + 1] == 1 and sign[rect_v[i]] == 1:
                print('ротация произведена  2 1')
                if draw_flag:
                    draw_rect(a, sign)
                a.append(a[4 * rect_v[i] + 1])
                a.append(a[4 * rect_v[i] + 1] + 0.5)
                a.append(a[4 * rect_v[i + 1] + 3])
                a.append(a[4 * rect_v[i] + 2])
                sign.append(-1)
                n = n + 1
                rescale(a, n)
                print('ротация произведена')
                if draw_flag:
                    draw_rect(a, sign)
                quit_flag = 1
            if vert_orientation[i] == 3 and vert_orientation[i + 1] == 0 and sign[rect_v[i]] == 1:
                print('ротация произведена 3 0')
                if draw_flag:
                    draw_rect(a, sign)
                a.append(a[4 * rect_v[i] + 0] - 0.5)
                a.append(a[4 * rect_v[i] + 0])
                a.append(a[4 * rect_v[i + 1] + 3])
                a.append(a[4 * rect_v[i] + 2])
                
                sign.append(-1)
                n = n + 1
                rescale(a, n)
                print('ротация произведена')
                if draw_flag:
                    draw_rect(a, sign)
                quit_flag = 1
            if vert_orientation[i] == 0 and vert_orientation[i + 1] == 3 and sign[rect_v[i]] == 1:
                print('ротация произведена 0 3')
                if draw_flag:
                    draw_rect(a, sign)
                a.append(a[4 * rect_v[i] + 0] - 0.5)
                a.append(a[4 * rect_v[i] + 0])
                a.append(a[4 * rect_v[i] + 3])
                a.append(a[4 * rect_v[i + 1] + 2])
                
                sign.append(-1)
                n = n + 1
                rescale(a, n)
                print('ротация произведена')
                if draw_flag:
                    draw_rect(a, sign)
                quit_flag = 1
        else:
            j = (i + 1) % len_free
            if vert_orientation[i] == 0 and vert_orientation[j] == 1 and sign[rect_v[i]] == -1:
                print('ротация произведена 0 1')
                if draw_flag:
                    draw_rect(a, sign)
                a.append(a[4 * rect_v[j] + 1])
                a.append(a[4 * rect_v[i] + 0])
                a.append(a[4 * rect_v[i] + 3])
                a.append(a[4 * rect_v[i] + 3] + 0.5)
                sign.append(1)
                n = n + 1
                rescale(a, n)
                print('ротация произведена 0 1')
                if draw_flag:
                    draw_rect(a, sign)
                quit_flag = 1
            if vert_orientation[i] == 1 and vert_orientation[j] == 0 and sign[rect_v[i]] == -1:
                print('ротация произведена 1 0')
                if draw_flag:
                    draw_rect(a, sign)
                a.append(a[4 * rect_v[i] + 1])
                a.append(a[4 * rect_v[j] + 0])
                a.append(a[4 * rect_v[i] + 3])
                a.append(a[4 * rect_v[i] + 3] + 0.5)
                sign.append(1)
                n = n + 1
                rescale(a, n)
                print('ротация произведена 1 0')
                if draw_flag:
                    draw_rect(a, sign)
                quit_flag = 1
            if vert_orientation[i] == 3 and vert_orientation[j] == 2 and sign[rect_v[i]] == -1:
                print('ротация произведена 3 2')
                if draw_flag:
                    draw_rect(a, sign)
                a.append(a[4 * rect_v[j] + 1])
                a.append(a[4 * rect_v[i] + 0])
                a.append(a[4 * rect_v[i] + 2] - 0.5)
                a.append(a[4 * rect_v[i] + 2])
                sign.append(1)
                n = n + 1
                rescale(a, n)
                print('ротация произведена 3 2')
                if draw_flag:
                    draw_rect(a, sign)
                quit_flag = 1
            if vert_orientation[i] == 2 and vert_orientation[j] == 3 and sign[rect_v[i]] == -1:
                print('ротация произведена 2 3')
                if draw_flag:
                    draw_rect(a, sign)
                a.append(a[4 * rect_v[i] + 1])
                a.append(a[4 * rect_v[j] + 0])
                a.append(a[4 * rect_v[i] + 2] - 0.5)
                a.append(a[4 * rect_v[i] + 2])
                sign.append(1)
                n = n + 1
                rescale(a, n)
                print('ротация произведена 2 3')
                if draw_flag:
                    draw_rect(a, sign)
                quit_flag = 1
        if quit_flag:
            print('quit flag is working')
            
            effectiveness_flag = [0]
            adj = fill_adjecent(a, n)
            clever_rotation(a, n, sign, adj, effectiveness_flag)
            if effectiveness_flag[0] == 1:
                print('эффективный ротейшн')
                input()
            n = len(a) // 4
            adj = fill_adjecent(a, n)
            find_all_of_them(a, n, sign, 1, adj, effectiveness_flag)
            n = len(a) // 4
            adj = fill_adjecent(a, n)
            find_all_of_them(a, n, sign, 0, adj, effectiveness_flag)
            if effectiveness_flag[0] == 1:
                print('эффективный файндолл')
                input()
            n = len(a) // 4
            adj = fill_adjecent(a, n)
            fast_simplify(a, n, sign, adj, effectiveness_flag)
            if effectiveness_flag[0] == 1:
                input()
                print('эффективный симплифай')
            n = len(a) // 4
            if search_circle(a, n, sign, adj):
                effectiveness_flag[0] = 1
                adj = fill_adjecent(a, len(a) // 4)
                n = len(a) // 4
                print('эффективный сёрч циркл')
            if effectiveness_flag[0] == 1:
                print('флагг был эффективный')
                input()
                return
            else:
                quit_flag = 0
                a.pop(-1)
                a.pop(-1)
                a.pop(-1)
                a.pop(-1)
                sign.pop(-1)
                
                
                n = n - 1




        

# остатки кода от поиска цикла 
# print(cur, g[cur], p[cur])
            # print(a[4 * rect_graph[cur][0] + 0], a[4 * rect_graph[cur][0] + 1], a[4 * rect_graph[cur][0] + 2], a[4 * rect_graph[cur][0] + 3])
            # print(a[4 * rect_graph[cur][1] + 0], a[4 * rect_graph[cur][1] + 1], a[4 * rect_graph[cur][1] + 2], a[4 * rect_graph[cur][1] + 3])
            # cur = p[cur]
            # draw_rect(a, sign)

            # cur_neg = rect_graph[end[0]][0]
            # cur_pos = rect_graph[end[0]][1]
            # print(a[4 * cur_neg + 0], a[4 * cur_neg + 1], a[4 * cur_neg + 2], a[4 * cur_neg + 3])
            # direction = sharing_pair_vertices(cur_neg, cur_pos, rect_graph[p[end[0]]][0], rect_graph[p[end[0]]][1], adj)
            # print('dir = ', direction)
            # if  direction in [0, 1]:
            #     start_neg = [a[4 * cur_neg + 0], a[4 * cur_neg + 1], a[4 * cur_neg + 2], a[4 * cur_pos + 2]]
            #     a[4 * cur_neg + 2] = a[4 * cur_pos + 3]
            # if direction  in [2, 3]:
            #     start_neg = [a[4 * cur_neg + 0], a[4 * cur_neg + 1],  a[4 * cur_pos + 3], a[4 * cur_neg + 3]]
            #     a[4 * cur_neg + 3] = a[4 * cur_pos + 2]

            # if direction  in [1, 2]:
            #     start_pos = [a[4 * cur_pos + 0], a[4 * cur_neg + 0], a[4 * cur_pos + 2], a[4 * cur_pos + 3]]
            #     a[4 * cur_pos + 0] = a[4 * cur_neg + 1]
            # if direction  in [3, 0]:
            #     start_pos = [a[4 * cur_neg + 1], a[4 * cur_pos + 1], a[4 * cur_pos + 2], a[4 * cur_pos + 3]]
            #     a[4 * cur_pos + 1] = a[4 * cur_neg + 0]
            # print(a[4 * cur_neg + 0], a[4 * cur_neg + 1], a[4 * cur_neg + 2], a[4 * cur_neg + 3])
            # print("мы в цикле. отсюда нет выхода_старт")
            # draw_rect(a, sign)
            
            # cur = end[0]
            # while cur != st[0]:
            #     direction_old = direction
            #     direction = sharing_pair_vertices(rect_graph[cur][0], rect_graph[cur][1], rect_graph[p[cur]][0], rect_graph[p[cur]][1], adj)
            #     cur_neg = rect_graph[cur][0]
            #     cur_pos = rect_graph[cur][1]
            #     if (direction in [0, 1] and direction_old in [2, 3]) or (direction in [2, 3] and direction_old in [0, 1]):
            #         change(a, cur_neg, rect_graph[prev][0])
            #     if (direction in [0, 3] and direction_old in [1, 2]) or (direction in [1, 2] and direction_old in [0, 3]):
            #         change(a, cur_pos, rect_graph[prev][1])
                
                
            #     if direction in [0, 3]:
            #         a[4 * cur_neg + 0] = a[4 * rect_graph[p[cur]][0] + 0]
            #     if direction in [1, 2]:
            #         a[4 * cur_neg + 1] = a[4 * rect_graph[p[cur]][0] + 1]
            #     if direction in [0, 1]:
            #         a[4 * cur_pos + 3] = a[4 * rect_graph[p[cur]][1] + 3]
            #     if direction in [2, 3]:
            #         a[4 * cur_pos + 2] = a[4 * rect_graph[p[cur]][1] + 2]
            #     prev = cur
            #     cur = p[cur]
            #     print('промежуточный dir = ', direction, 'dirold', direction_old)
            #     draw_rect(a, sign)
                
                

            #     if  direction in [0, 1]:
            #         a[4 * rect_graph[cur][0] + 2] = a[4 * rect_graph[cur][1] + 3]
            #     if direction  in [2, 3]:
            #         a[4 * rect_graph[cur][0] + 3] = a[4 * rect_graph[cur][1] + 2]

            #     if direction  in [1, 2]:
            #         a[4 * rect_graph[cur][1] + 0] = a[4 * rect_graph[cur][0] + 1]
            #     if direction  in [3, 0]:
            #         a[4 * rect_graph[cur][1] + 1] = a[4 * rect_graph[cur][0] + 0]
            #     print("dir = ", direction, "мы в цикле. отсюда нет выхода")
            #     draw_rect(a, sign)

            # #по выходе из цикла
            # direction_old = direction
            # direction = sharing_pair_vertices(rect_graph[cur][0], rect_graph[cur][1], rect_graph[end[0]][0], rect_graph[end[0]][1], adj)
            # cur_neg = rect_graph[cur][0]
            # cur_pos = rect_graph[cur][1]
            # if (direction in [0, 1] and direction_old in [2, 3]) or (direction in [2, 3] and direction_old in [0, 1]):
            #     change(a, cur_neg, rect_graph[prev][0])
            # if (direction in [0, 3] and direction_old in [1, 2]) or (direction in [1, 2] and direction_old in [0, 3]):
            #     change(a, cur_pos, rect_graph[prev][1])
            
            
            # if direction in [0, 3]:
            #     a[4 * cur_neg + 0] = start_neg[0]
            # if direction in [1, 2]:
            #     a[4 * cur_neg + 1] = start_neg[1]
            # if direction in [0, 1]:
            #     a[4 * cur_pos + 3] = start_pos[3]
            # if direction in [2, 3]:
            #     a[4 * cur_pos + 2] = start_pos[2]
            # print('ПО ВЫХОДЕ МЫ ТАКИ direction = ', direction)
            # draw_rect(a, sign)

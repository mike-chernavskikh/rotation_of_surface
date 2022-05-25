import imp
import knots_surfaces
#По сравнению с версией за июль удалил разных функций и кусков кода
#Добавил такую штуку: рокировку можно делать, если прямоугольник хочет сжаться. 


rect = []
sign = []

#ЦИКЛИТСЯ НА 16 !!!!!! 
#21 22 работают переклейка

#2000003
myflag = 50000020
slow_flag = 0
rect, sign = knots_surfaces.return_rect(myflag)
if 0:
    print('тут я поменял знак')
    input()

    for i in range(len(sign)):
        sign[i] = -sign[i]
imp.delete_zeroes(rect, len(rect) // 4, sign)
#imp.draw_rect(rect,sign)
#imp.big_check_function(rect, len(rect) // 4, sign)
#imp.draw_rect(rect, sign)

# r = []
# for i in range(len(rect)//4):
#     r.append([rect[4 * i + 0], rect[4 * i + 2], rect[4 * i + 1], rect[4 * i + 3]])
# imp.check_all([r])
print('check all finished')
if slow_flag:
    input()
#imp.check_orient(rect, len(rect)//4, sign)

#двадцатый флаг работает!!!  или нет...

print('LEN = ', len(rect) // 4)

size = len(rect) // 4
if 4 * len(sign) != len(rect):
    print('НЕПРАВИЛЬНЫЕ ДЛИНЫ')
    input()


if 4 * len(sign) != len(rect):
    sign = [0] * size
    print('we orienteate')
    imp.orientate(rect, size, sign)

for i in range(len(rect)):
    rect[i] = rect[i] + 1


#show_must_go_on(rect, sign, size)

#draw_rect(rect)

imp.check_orient(rect, len(rect) // 4, sign)
if slow_flag:
    input()


newcounter = 0
genprev = 0
gen = 0
maxcounter = 1
#ТЕЛО ПРОГРАММЫ
if 1:
    while True:
        imp.check_orient(rect, size, sign)

        
        adj = imp.fill_adjecent(rect, len(rect) // 4)
        #print('ПОИСК ПЕРЕСТРОЙКИ ЗАКОММЕНТИРОВАН')
        while imp.search_circle(rect, len(rect) // 4, sign, adj):
            imp.big_check_function(rect, len(rect) // 4, sign)
            adj = imp.fill_adjecent(rect, len(rect) // 4)
            print('circling')
            #imp.draw_rect(rect, sign)

        #Переставил местами симплифай и эту строку выше
        effectiveness_flag = [0]

        while imp.find_all_of_them(rect, len(rect) // 4, sign, 1, adj, effectiveness_flag) == 1:
            print('это мы запускаем чек-функшн во время find_all')
            #imp.big_check_function(rect, len(rect) // 4, sign)
            print('find all is working')
        print('We change orientations of arrows\n')
        while imp.find_all_of_them(rect, len(rect) // 4, sign, 0, adj, effectiveness_flag) == 1:
            #imp.big_check_function(rect, len(rect) // 4, sign)
            print('minus find all is working')
        print('after find all of them v2')
        imp.big_check_function(rect, len(rect) // 4, sign)
        n = len(rect) // 4
        
        # for i in range(len(rect) // 4):
        #     if sign[i] == 1:
        #         print(rect[4 * i + 0], rect[4 * i + 1], rect[4 * i + 1], rect[4 * i + 3])
        
        # print('minus')
        # for i in range(len(rect) // 4):
        #     if sign[i] == -1:
        #         print(rect[4 * i + 0], rect[4 * i + 2], rect[4 * i + 1], rect[4 * i + 3])

        #imp.draw_rect(rect, sign)
        # a = input()

        n = len(rect) // 4
        print('before delete zeroes')
        imp.big_check_function(rect, len(rect) // 4, sign)
        adj = imp.delete_zeroes(rect, len(rect) // 4, sign)

        print('after delete zeroes')
        imp.big_check_function(rect, len(rect) // 4, sign)

        adj = imp.fast_simplify(rect, len(rect) // 4, sign, adj, effectiveness_flag)
        imp.big_check_function(rect, len(rect) // 4, sign)


        size = len(rect) // 4

        delta = 0.1


        imp.rescale(rect, size)
        # draw_rect(rect)

        size = len(rect) // 4
        mut = imp.mutant(rect, sign, size, delta)


        if 0:
        #####   ПОДКРУТКА ПОВЕРХНОСТИ ОКОЛО УЗЛА
        
            down_e = []
            up_e = []
            left_e = []
            right_e = []

            imp.new_edges(rect, sign, size, delta, down_e, up_e, left_e, right_e)
            new_rect = []
            imp.cook_rectangles(mut, len(down_e) // 3, down_e, up_e, left_e, right_e, sign)
            imp.rescale(mut, len(mut) // 4)
            size = len(mut) // 4
            rect = mut.copy()
        #####   КОНЕЦ ПОДКРУТКИ ПОВЕРХНОСТИ ОКОЛО УЗЛА

        else:
        #####  подкрутка на 1
            print('we r here')
            imp.elementary_rotation(rect, len(rect) // 4, sign, adj)
            size = len(rect) // 4
            adj = imp.fill_adjecent(rect, size)
            size = len(rect) // 4
        ## конец подкрути на 1
        

        print('картинка после подкрутки')
        input()
        imp.draw_rect(rect, sign)

        print('Its celver rotation used')
        adj = imp.fill_adjecent(rect, size)
        imp.clever_rotation(rect, size, sign, adj, effectiveness_flag)
        print('clever rotation finished')
        imp.big_check_function(rect, len(rect) // 4, sign)
        
        gen = imp.genus(rect, len(rect) // 4)
        
        print(rect, sign)
        print('\n\n\n\n\n')
        for i in range(len(rect) // 4):
            if sign[i] == 1:
                print(rect[4 * i + 0], rect[4 * i + 1], rect[4 * i + 1], rect[4 * i + 3])
        
        print('minus')
        for i in range(len(rect) // 4):
            if sign[i] == -1:
                print(rect[4 * i + 0], rect[4 * i + 2], rect[4 * i + 1], rect[4 * i + 3])
        print('end')
        adj = imp.fill_adjecent(rect, len(rect) // 4)
        while imp.remove_handle(rect, len(rect) // 4, sign, adj):
            imp.big_check_function(rect, len(rect) // 4, sign)
            print("УДАЛИЛИ РУЧКУ!")
            # imp.draw_rect(rect, sign)
            # input()
        print('GENUS = ', gen)
        print('max counter = ', maxcounter, 'counter = ', newcounter)
        imp.big_check_function(rect, len(rect) // 4, sign)
        imp.draw_rect(rect, sign)
        imp.draw_knot(rect, sign, [0])
        a = input()
        input()

        size = len(rect) // 4
        print(len(rect) // 4, size)
        # draw_rect(mut)
        print('Finale')
        imp.rescale(rect, size)
        #закомментил строчку ниже 07.09.2021
        #draw_rect(mut)
        #print(mut, sign)
        adj = imp.delete_zeroes(rect, size, sign)
        size = len(rect) // 4

        #print('NEW MUT = ', mut, sign)
        print(len(rect), len(adj), 'ok ne ok:????')
        #imp.draw_rect(mut, sign)
        index = [0]
        #draw_knot(mut, n, index)


        # if newcounter >=  maxcounter:
        #     for i in range(len(sign)):
        #         sign[i] = -sign[i]
        #     print('SIGN cHANGED')
        #     newcounter = 0
        #     if gen == genprev:
        #         maxcounter = maxcounter + 1
        #     else:
        #         maxcounter = 1
        #         adj = imp.destabilizations(mut, size, sign, adj, 0)
        #         adj = fast_simplify(mut, size, sign, adj)
        # else:
        #     newcounter = newcounter + 1
        #     if gen != genprev:
        #         maxcounter = 1
        #         adj = imp.destabilizations(mut, size, sign, adj, 0)
        #         adj = fast_simplify(mut, size, sign, adj) 
        # genprev = gen
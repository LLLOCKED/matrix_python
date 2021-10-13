import matplotlib.image as img
import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from tkinter.filedialog import askopenfilename
from tkinter import *
from functools import partial
import matplotlib.colors as col


def binaryMatrix(binary):

    newWindow = Toplevel()
    newWindow.title("Binary")
    newWindow.geometry("710x600")

    label = Text(newWindow, bg='white', fg='black')
    for i in range(len(binary)):
        for k in range(len(binary)):
            label.insert(END, str(binary[i][k]))
        label.insert(END, '\n')

    label.place(height= 600, width=710)

def matrixImage(matrix):
    newWindow = Toplevel()
    newWindow.title("Matrix")
    newWindow.geometry("710x600")

    label = Text(newWindow, bg='white', fg='black')
    for i in range(len(matrix)):
        for k in range(len(matrix)):
            label.insert(END, str(matrix[i][k]) + ' ')
        label.insert(END, '\n')

    label.place(height= 600, width=710)

def tableNeighbor(ev, ev2, binary1, binary2):

    newWindow = Toplevel()
    newWindow.title("Neighbor Vector")
    newWindow.geometry("300x300")

    d = 0
    sk_1 = []
    sk_2 = []
    sk_3 = []
    sk_4 = []

    for i in range(len(ev)):
        if(ev[i]!=ev2[i]):
            d +=1

    poetry = "Растаяние между ev1 и ev2 = " + str(d)

    def sk(ev_f, binary_f, sk_f):
        for i in range (len(ev_f)):
            c = 0
            for k in range (len(binary_f[0])):
                if (ev_f[i]!=binary_f[i][k]):
                    c +=1
            sk_f.append(c)

    sk(ev, binary1, sk_1)
    sk(ev, binary2, sk_2)
    sk(ev2, binary1, sk_3)
    sk(ev2, binary2, sk_4)

    print(sk_3)
    

    label = Label(newWindow, text=poetry, fg="#eee", bg="#333")

    label.place(height= 300, width=300)
def sk(ev_f, binary_f, sk_f):
        for i in range (len(ev_f)):
            c = 0
            for k in range (len(binary_f[0])):
                if (ev_f[i]!=binary_f[i][k]):
                    c +=1
            sk_f.append(c)

def etalonVector(vector):
    newWindow = Toplevel()
    newWindow.title("Etalon Vector")
    newWindow.geometry("800x100")

    label = Text(newWindow, bg='white', fg='black')
    for k in range(len(vector)):
        label.insert(END, str(vector[k]))


    label.place(height= 100, width=800)

def vector(binary, evmat):
    for k in range(len(binary)):
        ev = 0
        for i in range(len(binary[k])):
            if (binary[i][k] == 1):
                ev +=1
        if (ev>50):
            evmat.append(1)
        else:
            evmat.append(0)


def main (image, image_2):
    image = img.imread(image)
    matrix = np.array(image)

    image_2 = img.imread(image_2)
    matrix2 = np.array(image_2)

    np.set_printoptions(threshold=sys.maxsize)

    avg_matrix = []
    for k in range(len(matrix)):
        j=0
        for i in range(len(matrix[0])):
            j += matrix[i][k]

        avg_matrix.append(round(j/100))

    plus_delta_matrix = []
    minus_delta_matrix = []

    for i in range(len(avg_matrix)):
        plus = avg_matrix[i]+40
        minus = avg_matrix[i]-40

        plus_delta_matrix.append(plus)
        minus_delta_matrix.append(minus)


    binary_matrix = []
    ev_mat = []

    for k in range(len(matrix)):
        ev = 0
        sub_binary_matrix = []
        for i in range(len(matrix[k])):
            if (plus_delta_matrix[i]>=matrix[k][i]>=minus_delta_matrix[i]):
                sub_binary_matrix.append(1)
                ev +=1
            else:
                sub_binary_matrix.append(0)
        binary_matrix.append(sub_binary_matrix)

    binary_matrix_2 = []
    ev_mat_2 = []

    for k in range(len(matrix2)):
        ev = 0
        sub_binary_matrix = []
        for i in range(len(matrix2[k])):
            if (plus_delta_matrix[i]>=matrix2[k][i]>=minus_delta_matrix[i]):
                sub_binary_matrix.append(1)
                ev +=1
            else:
                sub_binary_matrix.append(0)
        binary_matrix_2.append(sub_binary_matrix)


    vector(binary_matrix, ev_mat)
    vector(binary_matrix_2, ev_mat_2)



    show_ev_1 = []
    show_ev_2 = []
    for i in range(15):
        show_ev_1.append(ev_mat)
        show_ev_2.append(ev_mat_2)
        
    fig = plt.figure()

    ax = fig.add_subplot(2,3,1)
    m = ax.imshow(image, cmap='gray')
    fig.colorbar(m, ax=ax,shrink = 0.5)
    ax.set_title('Оригинал')

    ax = fig.add_subplot(2,3,4)
    m2 = ax.imshow(image_2, cmap='gray')
    fig.colorbar(m2, ax=ax,shrink = 0.5)
    ax.set_title('Оригинал 2')

    ax = fig.add_subplot(2,3,2)
    m3 = ax.imshow(binary_matrix,cmap='binary')
    fig.colorbar(m3, ax=ax, shrink = 0.5)
    ax.set_title('Бинарная матрица')

    ax = fig.add_subplot(2,3,5)
    m4 = ax.imshow(binary_matrix_2,cmap='binary')
    fig.colorbar(m4, ax=ax, shrink = 0.5)
    ax.set_title('Бинарная матрица 2')


    ax = fig.add_subplot(2,3,3)
    m5 = ax.imshow(show_ev_1,cmap='gray')
    ax.set_title('Эталонный вектор')
    ax.set_yticklabels([])
    plt.yticks([])

    ax = fig.add_subplot(2,3,6)
    m6= ax.imshow(show_ev_2,cmap='binary')
    ax.set_title('Эталонный вектор 2')
    ax.set_yticklabels([])
    def sk(ev_f, binary_f, sk_f):
        for i in range (len(ev_f)):
            c = 0
            for k in range (len(binary_f[0])):
                if (ev_f[i]!=binary_f[i][k]):
                    c +=1
            sk_f.append(c)
    plt.yticks([])



    B = Button(text ="Binary matrix 1", command = partial(binaryMatrix, binary_matrix))
    B2 = Button(text ="Binary matrix 2", command = partial(binaryMatrix, binary_matrix_2))
    B3 = Button(text ="Matrix 1", command = partial(matrixImage, matrix))
    B4 = Button(text ="Matrix 2", command = partial(matrixImage, matrix2))
    B5 = Button(text ="Neighbor", command = partial(tableNeighbor, ev_mat, ev_mat_2, binary_matrix,binary_matrix_2))
    B6 = Button(text ="EV 1", command = partial(etalonVector, ev_mat))
    B7 = Button(text ="EV 2", command = partial(etalonVector, ev_mat_2))

    B3.pack(side=LEFT)
    B.pack(side=LEFT)
    B4.pack(side=LEFT)
    B2.pack(side=LEFT)
    B6.pack(side=LEFT)
    B7.pack(side=LEFT)
    B5.pack(side=LEFT)


    # label2 = Text(bg='white', fg='black')
    # label2.insert(END, binary_matrix_3)
    # label2.place(relx=.5, rely=.5, height= 200)
    
    plt.draw()


if __name__ == '__main__':

    main('1.bmp', '2.bmp')
        
    plt.show()





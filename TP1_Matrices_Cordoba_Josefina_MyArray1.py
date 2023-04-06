# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:16:34 2023

@author: Win10
"""


class myarray:
    
    def __init__(self, elems: list, r: int, c: int, by_row: bool):
        self.elems  = elems
        self.r      = r
        self.c      = c
        self.by_row = by_row
        
    def get_pos(self,j,k):
        """Esta función está pensada para usar las coordenadas como las lee Python:
            Es decir, si queres el elemento en lo que sería la coordenada (1,1) matemática-
            mente, j tiene que ser 0 y k tiene que ser 0."""
        
        if j > self.r or k > self.c:
            """Esto es para validar que la coordenada que se quiere buscar esté verdadera-
            mente en la matriz. Si se ingresa un número de fila (j) o un número de columna (k)
            mayor a los de la matriz, se devuelve None"""
            salida = None
        else:
           if self.by_row == True:
               pos = j * self.c + k
               """Si la condición by_row == True se cumple, la posición del elemento va 
               a ser igual a la j ingresada, por el número de columnas de la matriz más k.
               Por ejemplo, en el caso de una matriz [1,2,3,4,5,6,7,8,9]:
               [1, 2, 3,
                4, 5, 6,
                7, 8, 9]
               la posición del elemento en la coordenada (0,0) = 0 * 3 + 0 = 0
               Esta relación se cumple para el resto de las coordenadas:
               (0,1) = 0 * 3 + 1 = 1 (índex en la lista)
               (0,2) = 0 * 3 + 2 = 2 (índex en la lista).
               Así sucesivamente"""
               salida = pos
           else:
               """En cambio, en el caso de que by_row == False, la misma lista [1,2,3,4,5,6,7,8,9]
               se leería así:
                   [1, 4, 7,
                    2, 5, 8,
                    3, 6, 9], 
               Por lo tanto, la relación entre las coordenadas dadas y la posición de cada 
               elemento en la listaes k, por el número de filas de la matriz, más j:
                   (0,0) = 0 * 3 + 0 = 0
                   (1,0) = 0 * 3 + 1 = 1
                   (1,1) = 1 * 3 + 1 = 4
                    """
               pos = k * self.r + j
               salida = pos
        print(salida)
        return salida

    def get_coords(self, m):
        
        """El propósito de esta función va a ser, dada una posición ó índice m, se van a 
        devolver las coordenadas de esa posición en la matriz, una vez más arrancando desde 0
        como lo lee Python."""

        if self.by_row == True:
            """El método comienza comprobando si la matriz se almacena por filas o columnas."""
            j = m // self.c
            k = m % self.c
            """Dado que la condición by_row == True, se busca j, que va a ser igual al cociente 
            de la división enetera de la posición m por la cantidad de columnas. Por otro lado, 
            k va a ser igual al resto de dividir m por la cantidad de columnas. Por ejeplo, para
            la matriz 
            [1, 2, 3,
             4, 5, 6,
             7, 8, 9]
            Si m = 0 --> j = 0 // 3 = 0
                         k = 0 % 3 = 0
            Si m = 2 --> j = 2 // 3 = 0
                         K = 2 % 3 = 2
            Finalemente, se devuelve una tupla de la coordenada correspondiente a la posición
            ingresada"""
            salida = (j, k)
        else:
            """En el caso de que by_row == False, sucede la misma lógica, nada más que se 
            utiliza el número de filas en lugar del número de columnas"""
            j = m // self.r
            k = m % self.r
            salida = (j, k)
        
        print(salida)    
        return (salida)

        
    def switch(self):
        """El objetivo de esta función es que, dada la instancia de clase
        by_row = True ó by_row = False, esta se cambie, para así cambiar el orden de
        cómo se almacenan los elementos en la lista 'elems'. Primero, se crea una lista vacía,
        'elems2'"""
        elems2 = []
        if self.by_row == True:
            """Se itera sobre cada fila de la matriz,agregando todos los elementos de esa 
            fila a elems2, en orden. la clave de esta función es que, si bien se mantiene 
            el orden de la lista, sus elementos se concatenan de forma diferente.
            Una vez que todos los elementos se han agregado a elems2, 
            el método establece self.elems igual a elems2, reemplazando 
            el orden original de los elementos en self.elems con el nuevo orden. 
            Finalmente, el método cambia el valor de self.by_row, para 
            que la próxima vez que se llame al cambio, los elementos se reorganicen en el 
            orden opuesto al dado.
                        
            Por ejemplo,
            para la matriz 
            [1, 2, 3,
             4, 5, 6,
             7, 8, 9]
            si by_row es False, la función devuelve 
            [1, 4, 7,
             2, 5, 8,
             3, 6, 9]"""
            for i in range(self.c):
                for j in range(self.r):
                    elems2.append(self.elems[i * self.c + j])
        else:
            for i in range(self.r):
                for j in range(self.c):
                    elems2.append(self.elems[j * self.r +i])
        print(elems2)
        return elems2
            
        # if self.c != self.r:
        #     if self.by_row == False:
        #         for i in range(self.c):
        #             for j in range(0,len(self.elems),self.c):
        #                elems2.append(self.elems[i+j]) 
        #         salida = elems2
        #         # print(salida)
        #     elif self.by_row == True:
        #         for i in range(self.r):
        #             for j in range(0,len(self.elems),self.r):
        #                elems2.append(self.elems[i+j])
        #         salida = elems2
        #         # print(salida)            
        # elif self.c == self.r:
        #     if self.by_row == False:
        #         for i in range(self.c):
        #             for j in range(0,len(self.elems),self.c):
        #                elems2.append(self.elems[i+j]) 
        #         salida = elems2
        #         # print(salida)
        #     if self.by_row == True:
        #         salida = self.elems
        #         print(self.elems)
        # return salida
    
    def get_row(self, j):
        """Esta función devuelve una fila de la matriz, con el parámetro j especificando que
        fila devolver. Primero, el código controla que si la matriz está almacenada por 
        fila (by_row == True), y además, si la j ingresada es mayor a la cantidad de filas que
        tiene la matriz: si ese es el caso, devuelve None. 
        Observación --> se debe ingresar una j que considera a la fila 0 como la primera fila.
        Funciona siguiendo la lógica de Python.
        """
        
        if self.by_row == True:
            if j > self.r:
                salida = None
            else:
                """En el caso de que la j ingresada sea un valor válido, la variable empieza
                va a tomar el valor de j multiplicado por la cantidad de columnas. La variable
                termina va a tener el valor de empieza más la cantidad de columnas. """
                empieza = j * self.c
                termina = empieza + self.c
                """Estos valores de salida y entrada se utilizan para realizar el slicing,
                que devuelve los elementos de elems desde el índice 'empieza' hasta uno
                antes que el valor 'termina'."""
                salida  = self.elems[empieza:termina]
        else:
            """Si la matriz está almacenada por columnas, se utiliza la misma lógica excepto
            que en lugar de multiplicar y sumar el número de columnas, la cuentas se realizan
            con el número de filas."""
            if j > self.r:
                salida = None
            else:
                empieza = j * self.r
                termina = empieza + self.r
                salida  = self.elems[empieza:termina]
        # print(salida)
        return salida
    
    def get_col(self, k):
        """
        Esta función tiene como objetivo devolver la columna número k de la matriz.
        
        Observación --> hay que pasarle un valor 'k' como lo lee Python: es decir, empezando
        a contar las columnas desde 0. Por ejemplo, en el caso de una matriz 3x3, si queres agarrar
        la última columna, k = 2"""
        columna = []
        if self.c != self.r:
            """Lo primero que hace es fijarse si es una matriz cuadrada o no. Si no lo es, 
            luego de revisar que la k ingresada sea válida, revisa si by_row es True. Si este 
            es el caso, itera sobre cada fila de la matriz y obtiene el elemento en el 
            índice de columna especificado 'k', calculando el índice en función del número 
            de filas y columnas de la matriz.Luego, agrega el elemento a la lista columna,
            que terminará compuesta de los elementos que forman la columna que se quiere obtener"""
            if k > self.c:
                salida = None
            elif self.by_row == True:
                for i in range(self.r):
                    columna.append(self.elems[k + self.c * i])    
                    salida = columna
            elif self.by_row == False:
                """En el caso de que by_row sea False, itera sobre cada columna y recupera 
                el elemento en el índice de fila 'k', calculando el índice en 
                función del tamaño de columna y fila de la matriz. Nuevamente, agrega ese 
                elemento a la lista de 'columnas'. """
                for i in range(self.r):
                    columna.append(self.elems[i + k*self.r])
                    salida = columna
        else:
            if k > self.c:
                salida = None
            elif self.by_row == True:
                for i in range(self.c):
                    columna.append(self.elems[k + self.r * i])    
                    salida = columna
            elif self.by_row == False:
                for i in range(self.r):
                    columna.append(self.elems[i + k * self.c])
                    salida = columna
        # print(salida)        
        return salida
    
    def get_elem(self, j, k):
        """Esta función busca devolver el elemento en la coordenada (j, k) de la matriz.
        Para esto se reutiliza la función get_pos(j,k) que devuelve en que posición está dicha 
        coordenada. Finalmente, se devuelve el índice 'elem' de la matriz 'elems'."""
        elem = self.get_pos(j,k)
        return self.elems[elem]
        print(self.elems[elem])
        
    def del_row(self, j):
       """Esta función elimina de la matriz 'elems' a la fila en el índice j.
       Si "by_row" se establece en True, la función elimina todos los elementos de 
       la fila en el índice "j" de la matriz 'elems'."""
       if self.by_row == True:
            fila = self.get_row(j)
            """Primero, utilizando la función get_row(j), obtiene la fila que se desea eliminar.
            Luego, itera sobre todos los elementos de 'elems' y por cada uno de estos, se 
            revisa si se encuentran en la fila que se quiere borrar. Si este es el caso, se
            elimina el elemento de 'elems', y se devuelve la matriz 'elems' sin la fila 
            eliminada."""
            for i in self.elems[:]:
                for j in fila:
                    if i == j:
                        self.elems.remove(j)
       else:
           """En el caso de que by_row sea False, se cambia la manera en la cual se almacena la
           matriz con la función switch() para poder usar la misma lógica."""
           self.elems = self.switch()
           fila = self.get_row(j)
           for i in self.elems[:]:
               for j in fila:
                   if i == j:
                       self.elems.remove(j)
       print(self.elems)
       return self.elems
            
         

    def del_col(self, k):
        """De manera similar a la función anterior, esta busca eliminar la columna en el índice k
        de la matriz 'elems'."""
        if self.by_row == True:
            for i in range(self.r):
                """Si by_row es True, itera sobre cada fila de 'elems'."""
                pos = i * self.c + k
                """Calcula la posición --> por ejemplo, en una matriz 3 x 3:
                    Si k=1 (o sea que quiere borrar la columna en el índice 1, empezando en 0):
                        i = 0 --> pos = 0 * 3 + 1 = 1
                        i = 1 --> pos = 1 * 3 + 1 = 4
                        i = 2 --> pos = 2 * 3 + 1 = 7
                    Después, borra al elemento en la posición pos de la matriz. Finalmente,
                    se le resta 1 a la cantidad de columnas porque al eliminar un elemento 
                    de la matriz también reduce el número de columnas de la matriz en 1."""
                self.elems.pop(pos)
                self.c -= 1
            
            salida = self.elems
            print (salida)
            
        else:
            """Utilizando la función switch(), se puede usar la misma lógica incluso cuando
            by_row es False."""
            self.elems = self.switch()
            for i in range(self.r):
                pos = i * self.c + k
                self.elems.pop(pos)
                self.c -= 1
            salida = self.elems
            print (salida)
        return salida
    
    def swap_rows(self,j,k):
        """Esta función cambia de lugar las filas en el índice j y la fila en el índice
        k, resultando en que la nueva fila en el índice j es la que estaba en el índice k, y vice-
        versa."""
        if self.by_row == True:
            """Si by_row es True, la función realiza el intercambio directamente en 
            los elementos de la matriz. La función recorre cada columna de las filas que se 
            intercambian e intercambia los elementos correspondientes. Luego, devuelve la 
            matriz con las filas intercambiadas"""
            caso1 = j * self.c
            caso2 = k * self.c
            for i in range(self.c):
                cambio = self.elems[caso1 + i]
                self.elems[caso1 + i] = self.elems[caso2 + i]
                self.elems[caso2 + i] = cambio
                salida = cambio
            # print(self.elems)
        else:
            """Si by_row es False, luego de usar la función switch(), se utiliza la misma lógica"""
            self.elems = self.switch()
            caso1 = j * self.c
            caso2 = k * self.c
            for i in range(self.c):
                cambio = self.elems[caso1 + i]
                self.elems[caso1 + i] = self.elems[caso2 + i]
                self.elems[caso2 + i] = cambio
                salida = cambio
            # print(self.elems)
        print(self.elems)
        return salida
    
    def swap_cols(self,l,m):
        """Esta función intercambia las columnas en los índices l y m respectivamente."""
        if self.by_row == False:
            self.elems = self.switch()
            caso1 = l * self.c
            caso2 = m * self.c
            for i in range(self.c):
                """La función recorre cada fila de las columnas que se intercambian 
                e intercambia los elementos correspondientes. Luego, devuelve la 
                matriz con las columas intercambiadas"""
                cambio = self.elems[caso1 + i]
                self.elems[caso1 + i] = self.elems[caso2 + i]
                self.elems[caso2 + i] = cambio
                cambio = self.switch
                salida = cambio
        else:
            self.elems = self.switch()
            caso1 = l * self.r
            caso2 = m * self.c
            for i in range(self.r):
                cambio = self.elems[caso1 + i]
                self.elems[caso1 + i] = self.elems[caso2 + i]
                self.elems[caso2 + i] = cambio
                cambio = self.switch
                salida = cambio
            # print(self.elems)
        print(self.elems)
        return salida
    
    def scale_row(self,j,x):
        """Esta función escala una fila específica de una matriz, es decir, multiplica a la 
        fila en el índice 'j' por el valor de 'x'."""
        if self.by_row == True:
            fila = self.get_row(j)
            """Primero obtiene los valores de la fila especificada mediante el método 
            get_row()"""
            fila_x = []
            for i in fila:
                fila_x.append(i * x)
                """Luego multiplica cada elemento de la fila por 'x'
                y agrega los resultados a una nueva lista fila_x."""
            for a in range(self.c):
                self.elems[j * self.c + a] = fila_x[a]
                """Finalmente, la función actualiza los valores en la fila especificada 
                de la matriz con los valores de 'fila_x'."""
            # print (self.elems)
            salida = self.elems
        else:
            self.elems = self.switch()
            fila = self.get_row(j)
            fila_x = []
            for i in fila:
                fila_x.append(i * x)
            for a in range(self.c):
                self.elems[j * self.c + a] = fila_x[a]
            # print (self.elems)
            salida = self.elems
            
        print(salida)
        return salida
    
    def scale_col(self, k, y):
        """Esta función escala una columna específica de una matriz, es decir, multiplica a
        la columna en el índice 'k' por el valor de 'y'."""
        if self.by_row == False:
            # self.elems = self.switch()
            col = self.get_col(k)
            """Primero obtiene los valores de la columna especificada utilizando 
            el método get_col()"""
            col_y = []
            for i in col:
                col_y.append(i * y)
                """Luego multiplica cada elemento de la columna por 'y', y agrega
                los resultados a la lista 'col_y'."""
            for a in range(self.r):
                self.elems[k * self.r + a] = col_y[a]
                """Finalmente, la función actualiza los valores en la columna especificada 
                de la matriz con los valores de 'col_y'."""
            # print (self.elems)
            
            salida = self.elems
            
        else: 
            col = self.get_col(k)
            col_y = []
            for i in col:
                col_y.append(i * y)
            for a in range(self.r):
                self.elems[a * self.c ++ k] = col_y[a]
            salida = self.elems
            
        print(salida)
        return salida
    
    def transpose(self):
        """Esta función obtiene a la matriz transpuesta de la matriz 'elems':
            si elems = [1,2,3,4,5,6,7,8,9], utilizando el método switch() devuelve
            [1,4,7,2,5,8,3,6,9]"""
        if self.by_row == True:
            self.elems = self.switch()
        else:
            self.elems = self.switch()
            
        print(self.elems)
        return self.elems
    
    def __add__(self, B):
        if isinstance(B, type(self)):
            suma = []
            matriz1 = self.elems
            matriz3 = B.elems
            for i in range(len(self.elems)):
                suma.append(matriz1[i] + matriz3[i])
        elif isinstance(B, int):
            suma = []
            for i in range(len(self.elems)):
                suma.append(self.elems[i] + B)
               
        # print(suma)
        return suma
    
    def __sub__(self, B):
        if isinstance(B, type(self)):
            resta = []
            matriz1 = self.elems
            matriz3 = B.elems
            for i in range(len(self.elems)):
                resta.append(matriz1[i] - matriz3[i])
        elif isinstance(B, int):
            resta = []
            for i in range(len(self.elems)):
                resta.append(self.elems[i] - B)
               
        # print(suma)
        return resta
        
        
        
        
        
        
matriz = myarray([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3, True)
B      = myarray([1, 2, 73, 24, 5, 6, 7, 28, 9], 3, 3, True)  
# B = 12 
res = matriz + B
print(res)     
    
    # def flip_cols(self):
       
 
    
# class eye(myarray):
#     def __init__(self, n):
#         self.elems = [0] * (n**2)
#         self.r = n
#         self.c = n
#         self.by_row == True
            
        
# matriz = myarray([1,2,3,4,5,6,7,8,9],3,3,True) 
# position = matriz.get_pos(2,2)              
# coord = matriz.get_coords(5)
# cambiar = matriz.switch()   
# row = matriz.get_row(0)
# col = matriz.get_col(1)
# elem = matriz.get_elem(1, 1)  
# del_fila = matriz.del_row(2)
# del_columna = matriz.del_col(1)
# cambio_filas = matriz.swap_rows(0,2)
# cambio_cols = matriz.swap_cols(0,2)
# multiplicar_fila = matriz.scale_row(0,5)
# multiplicar_col = matriz.scale_col(0,5)
# trans = matriz.transpose()
# flip_c = matriz.flip_cols()
# flip_r = matriz.flip_rows()

        
    # todo esto por ahora no:
        
    # def add(self, B):
        
    # def sub(self, B):
        
    # def rprod(self, B):
        
    # def lprod(self, B):
        
    # def pow(self, n):
        

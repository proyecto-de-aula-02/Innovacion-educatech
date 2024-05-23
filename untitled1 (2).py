
plataforma = {}
numero_preguntas = 0

def matematicas(numero_preguntas):
    while True:
        numero_preguntas = int(input("elige cuantas preguntas quieres. "))
        if numero_preguntas <= 3:
            return numero_preguntas
        else:
            print("solo hay 3 preguntas")

while True:
    print("\n~~ Menu de materias ~~")
    print("1. teoria ")
    print("2. preguntas ")
    print("3. salir")

    opcion = input("elige la opcion que quieres ver. ")

    if opcion == "2":
       numero_preguntas = matematicas(numero_preguntas)

       if numero_preguntas == 1:
           question = f"En las tablas de verdad, p y q es igual a:\n1. FVFV \n2. FFFV \n3. VVFF"
           answer = 2
           user_answer = int(input(question + " "))

           if user_answer == answer:
               print("correcto")
           else:
               print("incorrecto, la respuesta es", answer)

       elif numero_preguntas == 2:
           question1 = "La radicación es una operación matemática que consiste en: 1. sumar y restar 2. potenciar 3. hallar la raiz "
           answer1 = 3
           user_answer1 = int(input(question1 + " "))

           if user_answer1 == answer1:
               print("correcto")
           else:
               print("incorrecto, la respuesta es", answer1)

           question2 = "Segun el orden de las propiedades dadas la tercera era: 1. potencia 2. division 3. multiplicacion"
           answer2 = 1
           user_answer2 = int(input(question2 + " "))
           if user_answer2 == answer2:
               print("correcto")
           else:
               print("incorrecto, la respuesta es", answer2)

       elif numero_preguntas == 3:

           question3 = "cual de las siguientes expresiones es un monomio? (1. 2x + 3 (2. x^2 - 4x + 5 (3. 3xy + 2y^2"
           answer3 = 3
           user_answer3 = int(input(question3 + " "))

           if user_answer3 == answer3:
               print("correcto")
           else:
               print("incorrecto, la respuesta es", answer3)

           question4 = "cual de las siguientes es un binomio? (1. x^3 - 2x^2 + x - 1 (2. 3x + 4y (3. 2x^2 - 3xy + 5y^2"
           answer4 = 2
           user_answer4 = int(input(question4 + " "))

           if user_answer4 == answer4:
               print("correcto")
           else:
               print("incorrecto, la respuesta es", answer4)

           question5 = "cual de las siguientes NO es un polinomio? (1. 2x^3 - 3x^2 + 5x - 1 (2. 1/x + 2x^2 (3. x^4 + 4x^3 - 2x^2 + x - 7"
           answer5 = 2
           user_answer5 = int(input(question5 + " "))

           if user_answer5 == answer5:
               print("correcto")
           else:
               print("incorrecto, la respuesta es", answer5)

    elif opcion == "1":

           while True:
               print("\n~~ Menu de teorias ~~")
               print("1. tablas de verdad ")
               print("2. propiedades de la radicacion ")
               print("3. logaritmos y sus propiedades ")
               print("4. monomios, binomios, trinomios y polinomios ")
               print("5. salir")

               opcion = input("elige el tema que quieres ver. ")

               if opcion == "1":
                  print("Las tablas de verdad son herramientas utilizadas en lógica para analizar el valor de verdad de una proposición compuesta en función de los valores de verdad de sus componentes.")
                  print("En una tabla de verdad, se enumeran todas las posibles combinaciones de valores de verdad para las proposiciones simples que componen la proposición compuesta,")
                  print("y se determina el valor de verdad de la proposición compuesta para cada una de esas combinaciones.")
                  print("Aquí tienes un ejemplo básico de una tabla de verdad para la conjunción ( ^ ) de dos proposiciones simples, p y q:")
                  print("p	q	p ^ q")
                  print("F	F	  F")
                  print("F	T	  F")
                  print("T	F	  F")
                  print("T	T	  T")
                  print("En este ejemplo, p y q son proposiciones simples que pueden ser verdaderas (T) o falsas (F).")
                  print("La columna (p ^ q) muestra el resultado de la operación AND entre p y q.")

               elif opcion == "2":
                  print("La radicación es una operación matemática que consiste en hallar la raíz de un número. ")
                  print("La raíz cuadrada, por ejemplo, es un caso común de radicación, pero también existen otras raíces, como la raíz cúbica, la raíz cuarta, etc.")
                  print("1. Si a y b son numeros reales no negativos, entonces raiz de ab es igual a raiz de a por raiz de b")
                  print("2. La raíz de un producto es igual al producto de las raíces de los factores individuales. En otras palabras,")
                  print("raiz de a por b es igual a raiz de a por raiz de b")
                  print("3. La raíz de un cociente es igual al cociente de las raíces de los numerador y denominador. En otras palabras,")
                  print("raiz de a entre b es igual a raiz de a entre raiz de b, siempre que b no sea igual a 0")
                  print("4. La raíz de un número elevado a una potencia es igual al número elevado a la potencia dividida por el índice de la raíz. Por ejemplo,")
                  print("entre parentesis raiz de a multiplicada por m es igual a raiz de a elevada a la m")

               elif opcion == "3":
                  print("Los logaritmos son una herramienta matemática útil para simplificar cálculos y resolver ecuaciones que involucran exponentes.")
                  print("Aquí tienes algunas de sus propiedades más importantes")
                  print("1. Propiedad del logaritmo de una multiplicación: El logaritmo de un producto es igual a la suma de los logaritmos de los factores.")
                  print("2. Propiedad del logaritmo de una división: El logaritmo de una división es igual al logaritmo del numerador menos el logaritmo del denominador.")
                  print("3. Propiedad del logaritmo de una potencia: El logaritmo de una potencia es igual al exponente multiplicado por el logaritmo de la base.")
                  print("4. Propiedad del logaritmo de 1: Cualquier logaritmo de 1 es siempre igual a 0.")
                  print("5. Propiedad del logaritmo de la base: El logaritmo de cualquier número en su propia base es igual a 1.")

               elif opcion == "4":
                  print("1. Monomios: Son expresiones algebraicas simples que consisten en un solo término.")
                  print("Este término puede ser una constante, una variable o el producto de una constante y una o más variables elevadas a exponentes enteros no negativos.")
                  print("Algunos ejemplos de binomios")
                  print("3x, -2y^2, 5, 1/2xy^3")
                  print("2. Binomios: Son expresiones algebraicas que consisten en la suma o resta de dos términos.")
                  print("Estos términos pueden ser monomios o polinomios simples. Algunos ejemplos de binomios son:")
                  print("2x + 3, x^2 - 4y, a + b^3")
                  print("3. Trinomios: Son expresiones algebraicas que consisten en la suma o resta de tres términos.")
                  print("Al igual que los binomios, estos términos pueden ser monomios o polinomios simples. Algunos ejemplos de trinomios son:")
                  print("3x^2 - 2x + 5, 2a^3 + 4ab - 7b^2, x^2 + 2xy - y^2")
                  print("Polinomios: Son expresiones algebraicas que consisten en la suma o resta de varios términos.")
                  print("Estos términos pueden ser monomios, binomios, trinomios o polinomios más complejos.")
                  print("Los polinomios pueden tener cualquier cantidad de términos, y las variables en los términos pueden tener diferentes exponentes.")
                  print("Algunos ejemplos de polinomios son:")
                  print("4x^2 - 2x^3 + 3x - 7, y^4 + 2y^3 - 5y^2 + y - 1, 2a^2b + 3ab^2 - ab - 5b^2 - 4a")

               elif opcion == "5":
                  print("chao")
                  break

               else:
                  print("opcion no valida")


    elif opcion == "3":
        print("chao")
        break
    else:
        print("opcion no valida")
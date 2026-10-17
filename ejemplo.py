"""Estos son los ejemplos
de uso de cola y pila que muestra el foro."""

#Este es el ejemplo de cola que muestra como funciona el FIFO(first in first out)
#esto significa que el primer valor agregado es tambien el primer eliminado.
cola = []
cola.append("A")
cola.append("B")
print(cola.pop(0))  # A
print(cola)         # ['B']
#el uso que se le da a la cola es generalmente para historiales de cambio y deshacer operaciones

#Este es el ejemplo de pila que muestra como funciona el LIFO(last in first out)
#Esto significa que va a borrar primero al valor agregado mas reciente en lugar del primer agregado.
pila = []
pila.append("A")
pila.append("B")
print(pila.pop())  # B
print(pila)        # ['A']
#atención por orden de llegada. pop(0) cuesta O( n ); al final se propone una mejora.
# Pregunta inicial: si llegan Ana, Luis y Sofía, ¿a quién atiende primero una cola? Si registras tres cambios consecutivos, ¿cuál deshaces primero?
#R: En la cola se atiende primero al primer elemento que llega, por ende el primero en ser atendido en ana
#R2: con los cambios consecutivos,  en el caso de la pila se quita primero al tercer cambio siguiendo la logica LIFO, mientras que en la cola se quita el primer cambio.
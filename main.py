# Función del triángulo
def hollow_triangle(n):
  for i in range(1, n + 1):
    for j in range(1, n * 2):
      if  i == n or j == n - i + 1 or j == n + i - 1:
        print("#", end="")
      else:
        print("_", end="")
    print()


# Para imprimir un triángulo hueco de altura x
print("¿Qué altura tendrá nuestro triángulo?")
hollow_triangle(int(input()))

print("hola")
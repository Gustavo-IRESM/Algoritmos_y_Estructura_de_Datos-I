def mostrar_A(alfab_a, alfab_b):
    print("\nAlfabeto A y su corespondencia en el alfabeto B")
    print("-" * 46)
    for i in range(len(alfab_a)):
        print(f"{alfab_a[i]}  =  {alfab_b[i]}")
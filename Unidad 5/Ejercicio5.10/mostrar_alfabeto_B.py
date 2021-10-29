def mostrar_B(alfab_a, alfab_b):
    print("\nAlfabeto B y su corespondencia en el alfabeto A")
    print("-" * 46)
    for i in range(len(alfab_b)):
        print(f"{alfab_b[i]}  =  {alfab_a[i]}")
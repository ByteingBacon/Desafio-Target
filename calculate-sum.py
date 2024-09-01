def calculate_sum():
    INDICE = 12
    SOMA = 0
    K = 1

    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K

    return SOMA


soma_final = calculate_sum()
print(f"O valor final da variável SOMA é {soma_final}.")

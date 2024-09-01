def count_letter_a(s):
    count = s.lower().count('a')
    return count

string = input("Informe uma string para verificar a ocorrência da letra 'a': ")

contagem = count_letter_a(string)

if contagem > 0:
    print(f"A letra 'a' ocorre {contagem} vezes na string.")
else:
    print("A letra 'a' não ocorre na string.")

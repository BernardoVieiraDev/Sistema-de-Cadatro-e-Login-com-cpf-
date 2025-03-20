def apply_cpf_mask(event, entry):

    texto = entry.get()
    
    # Remove qualquer caractere não numérico
    texto = ''.join(c for c in texto if c.isdigit())
    
    # Aplica a máscara sem cortar o texto
    if len(texto) >= 4:
        texto = f'{texto[:3]}.{texto[3:]}'
    if len(texto) >= 8:
        texto = f'{texto[:7]}.{texto[7:]}'
    if len(texto) >= 12:
        texto = f'{texto[:11]}-{texto[11:13]}'
    
    entry.delete(0, "end")
    entry.insert(0, texto)



def cpf_validation(entry, label):
    cpf = entry.get()
    cpf = ''.join(c for c in cpf if c.isdigit())  # Limpeza do CPF
    
    if len(cpf) != 11:
        label.config(text="CPF inválido!", foreground="red")  
        return False
    if cpf == cpf[0] * 11:  # Verifica se o CPF tem todos os números iguais
        label.config(text="CPF inválido!", foreground="red")
        return False    

    nove_digitos = cpf[:9]
    dez_digitos = cpf[:10]
    contador_regressivo_1 = 10
    contador_regressivo_2 = 11

    soma = 0
    soma2 = 0

    for numero in nove_digitos:
        soma += int(numero) * contador_regressivo_1
        contador_regressivo_1 -= 1

    resultado = soma * 10
    resto = resultado % 11
    digito_1 = resto if resto <= 9 else 0

    for numero2 in dez_digitos:
        soma2 += int(numero2) * contador_regressivo_2
        contador_regressivo_2 -= 1

    resultado2 = soma2 * 10
    resto2 = resultado2 % 11
    digito_2 = resto2 if resto2 <= 9 else 0

    digito_1_str = str(digito_1)
    digito_2_str = str(digito_2)

    cpf_confirmado = nove_digitos + digito_1_str + digito_2_str

    if cpf_confirmado == cpf:
        return True
    label.config(text="CPF inválido!", foreground="red")
    return False

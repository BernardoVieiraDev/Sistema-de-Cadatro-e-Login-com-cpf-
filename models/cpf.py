class Cpf:
    def __init__(self, cpf):
        self._cpf = cpf

    @staticmethod
    def apply_cpf_mask(event, entry):
        cpf_input = entry.get()
        cpf_input = "".join(c for c in cpf_input if c.isdigit())

        if len(cpf_input) >= 4:
            cpf_input = f"{cpf_input[:3]}.{cpf_input[3:]}"
        if len(cpf_input) >= 8:
            cpf_input = f"{cpf_input[:7]}.{cpf_input[7:]}"
        if len(cpf_input) >= 12:
            cpf_input = f"{cpf_input[:11]}-{cpf_input[11:13]}"

        entry.delete(0, "end")
        entry.insert(0, cpf_input)

    @staticmethod
    def validar_cpf(cpf):
        cpf = "".join(c for c in cpf if c.isdigit())
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return "CPF inválido!"

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
            return "CPF válido!"
        return "CPF inválido!"

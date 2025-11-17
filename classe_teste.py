class Cachorro:
    # Atributos de classe - compartilhados por todas as instâncias
    raca_padrao = "Vira-Lata"
    racas_disponiveis = ["Labrador", "Poodle", "Pastor Alemão"]

    def definir_raca(self, nova_raca):
        """
        Método para definir a raça, funcionando como uma inicialização manual
        para este atributo de instância.
        """
        if nova_raca in self.racas_disponiveis:
            self.raca = nova_raca
        else:
            self.raca = self.raca_padrao
            print(f"Raça '{nova_raca}' não reconhecida. Usando a raça padrão: {self.raca_padrao}.")

    def descrever(self):
        """
        Método para descrever o cachorro.
        """
        # Tenta acessar 'self.raca'. Se 'definir_raca' não foi chamado,
        # pode gerar um AttributeError.
        try:
            return f"Este é um cachorro da raça {self.raca}."
        except AttributeError:
            return "Este cachorro ainda não teve sua raça definida (atributo 'raca' ausente)."
        

        # 1. Criação do Objeto
cachorro1 = Cachorro()
cachorro2 = Cachorro()
cachorro3 = Cachorro()

# 2. Testando o cachorro sem inicialização manual
print("--- Teste 1: Sem chamada ao 'definir_raca' ---")
print(cachorro1.descrever()) 
# Resultado: Causa a exceção, pois 'self.raca' não existe até que você a crie.
# (A função 'descrever' lida com o erro para evitar que o programa pare)

# 3. Inicialização manual para cachorros 2 e 3
print("\n--- Teste 2: Com chamada ao 'definir_raca' ---")
cachorro2.definir_raca("Labrador")
cachorro3.definir_raca("Pastor Alemão") # Uma das 3 raças que você pediu
cachorro4 = Cachorro()
cachorro4.definir_raca("Dálmata") # Raça indisponível

print(cachorro2.descrever())
print(cachorro3.descrever())
print(cachorro4.descrever())
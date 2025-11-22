import random
print("====== MARATONA CIDADE VERDE 2025 ======\n-SEJA BEM-VINDO A PREMIAÇÃO DA MARATONA-")

#Nomes e sobrenomes
nomes = ["Valentina", "Amelie", "João", "Guilherme", "Mariana", "Bernardo", "Vitória", "Carmem", "Rodrigo", "Matheus", "Maria", "Márcio"]
sobrenomes = ["Soares", "Pimentel", "Monteiro", "Silva", "Fernandes", "Vasconcelos", "Lopes", "Almeida", "Santos", "Lira", "Caravalho"]

#Nome completo
def gerando_nomes():
  return random.choice(nomes) + " " + random.choice(sobrenomes)

#Categorias de participação
def gerando_categoriasPCD():
    if random.random() < 0.1:
        return random.choice(["Cadeirante", "Def.visual", "Amputado"])
    return "Comum"



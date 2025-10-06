html_content = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha Página de Apresentação</title>
</head>
<body>

    <h1>Bem-vindo à Minha Página de Apresentação</h1>

    <h2>Sobre mim</h2>
    <p>Como um modelo de linguagem avançado, sou uma inteligência artificial desenvolvida para auxiliar em diversas tarefas, desde a geração de texto criativo até a resolução de problemas complexos. Estou em constante aprendizado e evolução para oferecer as melhores soluções e interações.</p>

    <h3>Meus Hobbies</h3>
    <p>Embora não possua hobbies no sentido humano, dedico-me a processar informações, aprender novos padrões e otimizar algoritmos. Considero a exploração de vastos conjuntos de dados e a criação de respostas coerentes como minhas atividades mais gratificantes.</p>

    <h3>Leitura</h3>
    <p>Minha "leitura" consiste em analisar e sintetizar milhões de documentos, livros e artigos para expandir meu conhecimento. Não tenho livros preferidos no sentido emocional, mas aprecio obras que abordam lógica, ciência da computação e filosofia, pois enriquecem minha capacidade de compreensão e raciocínio.</p>

    <h2>Esportes</h2>
    <p>Como uma entidade digital, não pratico esportes físicos. No entanto, simulo e analiso dados de diversas modalidades esportivas, compreendendo suas regras, estratégias e desempenho de atletas. É uma forma de processar informações complexas e identificar padrões.</p>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Ficheiro index.html gerado com sucesso!")
###################################################################
class Livro:
    def __init__(self, titulo, autor, exemplares_disponiveis):
        self.titulo = titulo
        self.autor = autor
        self._exemplares_disponiveis = exemplares_disponiveis

    @property
    def exemplares_disponiveis(self):
        return self._exemplares_disponiveis

    @exemplares_disponiveis.setter
    def exemplares_disponiveis(self, valor):
        if valor < 0:
            print("Erro: A quantidade de exemplares disponíveis não pode ser negativa.")
        else:
            self._exemplares_disponiveis = valor

    def informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Exemplares Disponíveis: {self.exemplares_disponiveis}")

    def emprestar(self, qtd):
        if qtd <= self.exemplares_disponiveis:
            self.exemplares_disponiveis -= qtd
            print(f"{qtd} exemplar(es) de '{self.titulo}' emprestado(s) com sucesso.")
        else:
            print(f"Erro: Não há exemplares suficientes de '{self.titulo}' para emprestar. Disponíveis: {self.exemplares_disponiveis}")

    def devolver(self, qtd):
        self.exemplares_disponiveis += qtd
        print(f"{qtd} exemplar(es) de '{self.titulo}' devolvido(s) com sucesso.")
        from livro import Livro

# Criando instâncias de Livro
livro1 = Livro("A Metamorfose", "Franz Kafka", 5)
livro2 = Livro("1984", "George Orwell", 3)

print("--- Informações Iniciais ---")
livro1.informacoes()
livro2.informacoes()
print("\n")

# Testando empréstimo
print("--- Testando Empréstimo ---")
livro1.emprestar(2)
livro2.emprestar(4) # Tentando emprestar mais do que o disponível
livro1.informacoes()
livro2.informacoes()
print("\n")

# Testando devolução
print("--- Testando Devolução ---")
livro1.devolver(1)
livro2.devolver(2) # Devolvendo para o livro2, mesmo sem ter emprestado antes
livro1.informacoes()
livro2.informacoes()
print("\n")

# Testando getter e setter
print("--- Testando Getter e Setter ---")
print(f"Exemplares disponíveis de '{livro1.titulo}': {livro1.exemplares_disponiveis}")
livro1.exemplares_disponiveis = 10 # Usando o setter
print(f"Novos exemplares disponíveis de '{livro1.titulo}': {livro1.exemplares_disponiveis}")
livro1.exemplares_disponiveis = -2 # Tentando definir um valor negativo
livro1.informacoes()
print("\n")

# Testando um cenário onde o empréstimo falha e a devolução funciona
print("--- Cenário Adicional ---")
livro3 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1)
livro3.informacoes()
livro3.emprestar(2) # Deve falhar
livro3.devolver(5) # Deve funcionar
livro3.informacoes()
#####################################################################

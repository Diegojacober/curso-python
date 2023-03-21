"""
Relações entre classes: Agregação
Agregação é uma forma mais especializada de associação entre dois ou mais objetos. Cada objeto terá seu ciclo de vida independente.
Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos objetos
Os objetos podem viver separadamente, mas pode se tratar de uma relação onde um objeto precisa de outro 
para fazer determinada tarefa
"""

class Carrinho:
    def __init__(self) -> None:
        self._produtos = []
        
    def total(self):
        return sum([p.preco for p in self._produtos])

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        
    
    def inserir_produto(self, *produtos):
        # for produto in produtos:
        #     self._produtos.append(produto)
        self._produtos.extend(produtos)
        
class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco
        
carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.50), Produto('Borracha', 2.25)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.listar_produtos()
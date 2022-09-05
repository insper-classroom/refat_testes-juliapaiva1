from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Pagamentos import Pagamento
from classes.Pedido import Pedido
from classes.Carrinho import Carrinho
from classes.Produto import Produto
from test.test_carrinho import *
from test.test_endereco import *
from test.test_pedidos import *
from test.test_pessoa import *
from test.test_produto import *

cria_pessoa = PessoaFisica('32583765432', 'pessoa@gmail.com', 'Carlos')
print(cria_pessoa)

endereco = Endereco('04549011', '332')
print(endereco)

cria_produto = Produto("0010342967", "Sabonete")
print(cria_produto)

carrinho = Carrinho()
carrinho.adicionar_item(cria_produto, 1)

pedido = Pedido('Carlos', carrinho)
print(pedido)

pagamento = Pagamento.processa_pagamento()
print(pagamento)

print ('Pedido realizado')
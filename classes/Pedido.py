#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re




class Pedido:
    EM_ABERTO = 1
    PAGO = 2
    pass
    
    def __init__(self, pessoa, carrinho):
        self.pedido = {}
        self.pedido['Pessoa'] = pessoa
        self.pedido['Carrinho'] = carrinho

    def __str__(self):
        return str(self.pedido)

    def endereco_faturamento(self, end_faturamento):
        self.end_faturamento = end_faturamento

    def endereco_entrega(self, end_entrega):
        self.end_entrega = end_entrega

    def status():
        return True 

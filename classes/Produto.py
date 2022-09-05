#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------



class Produto:
    produtos = []

    def __init__(self, id='', nome=''):
        self.id = id
        self.nome = nome
        Produto.produtos.append(self)

    def __str__(self):
        return str(self.id) + ' ' + str(self.nome) 

    def dicionario_produtos(self):
        dicionario = {
            'nome': self.nome
        }
        return dicionario
        
    def busca_nome(self, nome=''):
        if nome in Produto.produtos:
            return nome




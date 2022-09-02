#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------


produtos = []
class Produto:

    def __init__(self, id='', nome=''):
        self.id = id
        self.nome = nome

    def dicionario_produtos(self):
        dicionario = {
            'nome': self.nome
        }
        return dicionario
        
    def busca_nome(self, nome=''):
        if nome in produtos:
            return nome




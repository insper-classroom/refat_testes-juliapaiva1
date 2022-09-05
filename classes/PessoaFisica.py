#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
import re



class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''
    clientes = []

    def __init__(self, cpf, email, nome='Visitante'):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.enderecos = {}
        PessoaFisica.clientes.append(self)

    def __str__(self):
        return self.nome

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        self.enderecos[apelido_endereco] = end.endereco_usuario()
        return self.enderecos

    def remover_endereco(self, apelido_endereco):
        del self.enderecos[apelido_endereco]

    def get_endereco(self, apelido_endereco):
        if apelido_endereco in self.enderecos:
            return self.enderecos[apelido_endereco]

    def listar_enderecos(self):
        return self.enderecos
    
    def busca_nome(self, nome=''):
        if nome in PessoaFisica.clientes:
            return nome 

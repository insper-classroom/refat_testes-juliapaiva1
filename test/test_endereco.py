from classes.Endereco import Endereco
import pytest

end = Endereco('04549011', '332', 'Rua Baluarte', 'SP', 'São Paulo', 'apartamento 4232')

def test_cria_endereco_todas_informacoes():
  endereco = Endereco('04549011', '332', 'Rua Baluarte', 'SP', 'São Paulo', 'apartamento 4232')
  return endereco

def test_cria_endereco_cep_numero():
  endereco = Endereco('04549011', '332')
  return endereco


def test_consultar_cep_string():
  assert end.consultar_cep('04549010') == {
  "cep": "04549-010",
  "logradouro": "Rua Baluarte",
  "complemento": "até 239/240",
  "bairro": "Vila Olímpia",
  "localidade": "São Paulo",
  "uf": "SP",
  "ibge": "3550308",
  "gia": "1004",
  "ddd": "11",
  "siafi": "7107"
}

def test_consultar_cep_int():
  assert end.consultar_cep(11045540) == {
  "cep": "11045-540",
  "logradouro": "Rua Doutor Artur Porchat de Assis",
  "complemento": "",
  "bairro": "Boqueirão",
  "localidade": "Santos",
  "uf": "SP",
  "ibge": "3548500",
  "gia": "6336",
  "ddd": "13",
  "siafi": "7071"
}

def test_consultar_cep_inexistente():
  assert end.consultar_cep(88888888) == False

def test_queda_conexao():
  try:
    with pytest.raises(RuntimeError) as excinfo:
      end.consultar_cep(432) 
    assert excinfo.value.args[0] == 'Sem conexão com a internet. Tente novamente'
  except:
    assert True

def test_consultar_cep_algarismos():
  assert end.consultar_cep(432) == False



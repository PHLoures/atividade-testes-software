import pytest
from banco import Conta

def test_deposito_ok():
    c = Conta(); c.depositar(100); assert c.saldo == 100

def test_saque_ok():
    c = Conta(100); c.sacar(30); assert c.saldo == 70

def test_saque_sem_saldo():
    with pytest.raises(ValueError):
        Conta(10).sacar(50)

def test_deposito_negativo():
    with pytest.raises(ValueError):
        Conta().depositar(-5)

def test_erro_proposital():
    # ERRO SIMULADO: esperado errado de propósito
    c = Conta(100); c.sacar(30); assert c.saldo == 80

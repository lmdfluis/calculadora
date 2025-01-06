#!/bin/bash
# calculadora

# criando a base de calculos
def resultadosoma(num1, num2):
  return num1 + num2
def resultadosub(num1, num2):
  return num1 - num2
def resultadodiv(num1, num2):
  return num1 / num2
def resultadomul(num1, num2):
  return num1 * num2
# a calculadora
def calculo():
  print("bem vindo a calculadora")
num1 = float(input("digite o primeiro número:"))
num2 = float(input("digite o segundo número:"))
print("Escolha a operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
operacao = float(input("Digite o número da operação (1/2/3/4): "))
if operacao == 1:
  print("Você escolheu a soma!")
  print(resultadosoma(num1, num2))
elif operacao == 2:
  print("você escolheu a subtração!")
  print(resultadosub(num1, num2))
elif operacao == 3:
  print("você escolheu a multiplicação!")
  print(resultadomul(num1, num2))
elif operacao == 4:
  print("você escolheu a divisão!")
  print(resultadodiv(num1, num2))
else:
  print("Operação inválida!")




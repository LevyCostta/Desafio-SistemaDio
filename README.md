# Desafio da DIO Bootcamp: Sistema Bancário Simples
Este projeto consiste em um sistema bancário simples desenvolvido em Python, como parte do desafio do Bootcamp da DIO. O objetivo é criar uma aplicação que permita ao usuário realizar operações básicas de um banco, como depósitos, saques e consultas de extrato.

# Funcionalidades
O sistema apresenta um menu interativo com as seguintes opções:

Depositar: O usuário pode inserir um valor para depositar em sua conta. O sistema verifica se o valor é positivo e, em caso afirmativo, atualiza o saldo e registra a transação no extrato.

Sacar: O usuário pode solicitar um saque. O sistema verifica se o valor solicitado não excede o saldo disponível, se não ultrapassa o limite de saque e se o número máximo de saques foi respeitado. Se todas as condições forem atendidas, o saque é realizado e o extrato é atualizado.

Extrato: O usuário pode visualizar um resumo das transações realizadas, incluindo o saldo atual e um histórico de depósitos e saques.

Sair: O usuário pode encerrar a aplicação.

# Estrutura do Código
O código é estruturado em um loop while que mantém o sistema em execução até que o usuário escolha a opção de sair. As operações são realizadas com base na escolha do usuário, utilizando condicionais if para determinar qual ação executar. O saldo, limite de saque, extrato e contagem de saques são gerenciados por variáveis que são atualizadas conforme as operações são realizadas.

# Como Executar
Para executar o sistema, basta ter o Python instalado em sua máquina. Copie o código para um arquivo .py e execute-o em um terminal. Siga as instruções apresentadas no menu para interagir com o sistema bancário.

# Conclusão
Este projeto é uma excelente oportunidade para praticar lógica de programação e manipulação de dados em Python, além de ser uma introdução ao desenvolvimento de aplicações interativas.

# **Sistema Bancário em Python (Versão 2)**  

Este projeto é uma evolução do **Sistema Bancário Básico**, desenvolvido para consolidar conceitos fundamentais de **lógica de programação, funções, modularização e boas práticas em Python**.  

O sistema gerencia **múltiplas contas bancárias**, permitindo operações como depósitos, saques, consulta de extratos e relatórios filtrados de transações.

---

## **🚀 Funcionalidades**

- **Cadastro de Usuários**  
  - Cada usuário possui nome, CPF (único), data de nascimento e endereço.

- **Criação de Contas Bancárias**  
  - Vinculação de contas a usuários.  
  - Cada conta possui número sequencial, agência fixa ("0001"), saldo e extrato próprios.

- **Operações Bancárias**  
  - Depósitos vinculados a contas.  
  - Saques com validações de saldo, limite diário e quantidade máxima.  
  - Extratos com histórico de transações.

- **Relatórios Filtrados**  
  - Uso de **gerador** para listar transações por tipo (ex.: apenas saques ou depósitos).

- **Registro de Logs**  
  - Uso de um **decorador (`@log_transacao`)** para logar data, hora e tipo de transação.

---

## **📚 Conceitos Aplicados**
- **Funções com argumentos posicionais e nomeados** (`/` e `*`).  
- **Decoradores em Python** para logging automático.  
- **Geradores (`yield`)** para relatórios eficientes.  
- **Iteradores personalizados** (classe para percorrer contas).  
- **Validação e filtragem de dados** (ex.: CPF único).

---

## **📂 Estrutura do Projeto**
```
sistema_bancario/
│
├── sistema_bancario.py  # Código principal
└── README.md            # Documentação
```

---

## **⚙️ Como Executar**

### **Pré-requisitos**
- Python 3.8 ou superior instalado no sistema.

### **Passos para execução**
1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/sistema-bancario.git
   cd sistema-bancario
   ```
2. Execute o script no terminal:  
   ```bash
   python sistema_bancario.py
   ```
3. Interaja com o **menu principal** para cadastrar usuários, criar contas e realizar operações.

---

## **📖 Exemplo de Uso**
```
=========== MENU ===========
[1] Depositar em conta
[2] Sacar de conta
[3] Extrato de conta
[4] Criar Usuário
[5] Criar Conta
[6] Listar Contas
[7] Relatório de Transações
[8] Sair
============================
Escolha uma opção: 1

Número da conta: 1
Valor do depósito: 200.00
Depósito de R$ 200.00 realizado com sucesso na conta 1.
```

---

## **🔗 Links**
- Bootcamp DIO: [https://www.dio.me](https://www.dio.me)
- Meu LinkedIn: https://www.linkedin.com/in/leonardo-schaeffner-camargo/

---

## **🛠️ Melhorias Futuras**
- Persistência de dados (salvar usuários e contas em arquivos `.json` ou banco de dados).
- Implementar autenticação de usuários.
- Criar interface gráfica ou versão web (Flask/Django).

---

## **📜 Licença**
Este projeto é de uso educacional e livre para estudos.

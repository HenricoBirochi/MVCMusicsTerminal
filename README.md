# Nome do Projeto

## 📌 Sobre o Projeto
- Explicar que foi feito em Python
- Arquitetura utilizada: MVC
- Visualização feita pelo terminal
- Projeto não usa banco de dados
- Armazenamento feito em variável temporária
- Singleton usado para gerenciar essa variável

---

## 🏗️ Arquitetura Utilizada
- Model → Onde ficam os modelos das entidades.
- View → Responsável pela interação com o usuário. Aqui a aplicação mostra mensagens e recebe entradas pelo terminal.
- Controller → Faz a ponte entre o Model e a View. Ele recebe os comandos do usuário (via View), aciona o Model e depois devolve a resposta para a View.

---

## 🔑 Padrão de Projeto: Singleton
### O que é Singleton
- Breve explicação sobre o padrão

### Como foi aplicado no projeto
- Foi usado para criar a variável temporária que simula uma tabela única
- Justificativa de uso: deveria existir apenas uma tabela para armazenar, exibir e deletar dados

---

## 📂 Estrutura do Projeto
```
.
├── controller/
├── model/
├── view/
└── main/
```
model/ → Define as entidades e lógica dos dados.

view/ → Exibe informações e coleta entradas do usuário pelo terminal.

controller/ → Controla o fluxo entre Model e View.

main/ → Ponto de entrada da aplicação.

---

## 🚀 Como Executar
1. Clonar o repositório
2. Entrar na pasta do projeto
3. Executar `python run.py`

---

## 📌 Funcionalidades
- Inserir dados
- Listar dados
- Deletar dados
- Usar uma única tabela em memória (via Singleton)

---

## 🔮 Próximos Passos
- Persistência em banco de dados real
- Melhorar interface no terminal
- Adicionar testes automatizados

---

## 📖 Licença
- Definir tipo de licença

Este projeto é open-source e pode ser usado livremente para estudos e melhorias.

Projeto MVC em Python (com Singleton e Visualização no Terminal)
📌 Sobre o Projeto

Este projeto foi desenvolvido em Python seguindo a arquitetura MVC (Model-View-Controller).
A visualização dos dados é feita diretamente pelo terminal, de forma simples e interativa.

Um dos pontos principais deste projeto é o uso do Design Pattern Singleton, que foi aplicado para gerenciar o armazenamento dos dados em uma variável temporária, simulando uma "tabela" única em memória.

🚫 O projeto não utiliza banco de dados — todos os registros ficam armazenados em memória, enquanto a aplicação está em execução.

🏗️ Arquitetura Utilizada

Model: Responsável pela estrutura dos dados e pelas regras de negócio.

View: Responsável pela interação com o usuário via terminal.

Controller: Faz a ponte entre Model e View, coordenando as ações.

🔑 Padrão de Projeto: Singleton

O projeto utiliza o Singleton para criar e gerenciar a variável onde os dados são armazenados.

O que é Singleton?

O Singleton é um padrão de design criacional que garante que apenas uma instância de uma classe seja criada durante toda a execução do programa. Ele também fornece um ponto global de acesso a essa instância.

Por que Singleton aqui?

Como o sistema precisa de apenas uma tabela em memória para armazenar os dados, o Singleton foi a escolha ideal.

Garante que não sejam criadas múltiplas "tabelas".

Facilita o gerenciamento centralizado dos registros (criar, listar, deletar).

Simula uma espécie de "banco de dados único", mas dentro da própria aplicação.

📂 Estrutura do Projeto
.
├── controller/
├── model/
├── view/
└── main/

model/ → Define as entidades e lógica dos dados.

view/ → Exibe informações e coleta entradas do usuário pelo terminal.

controller/ → Controla o fluxo entre Model e View.

main/ → Ponto de entrada da aplicação.

🚀 Como Executar

1. Clone este repositório:
  git clone https://github.com/usuario/projeto-mvc-python.git
2. Execute o projeto:
  python run.py

📌 Funcionalidades

✅ Inserir novos dados

✅ Listar todos os dados

✅ Deletar registros

✅ Simulação de "tabela única" em memória

🔮 Próximos Passos

Adicionar persistência em banco de dados real (SQLite ou PostgreSQL).

Melhorar a interface do terminal com bibliotecas como rich ou curses.

Implementar testes automatizados.

📖 Licença

Este projeto é open-source e pode ser usado livremente para estudos e melhorias.

Quer que eu já monte também um exemplo de implementação do Singleton em Python (a classe que mantém a "tabela única") para incluir no README?

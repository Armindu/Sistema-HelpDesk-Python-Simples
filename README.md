# Sistema HelpDesk em Python

Projeto simples desenvolvido em Python para praticar lógica de programação e estruturação de scripts no terminal.

## Funcionalidades atuais
- Gerenciamento básico de chamados via terminal no `main.py` (reescrita com ajustes e melhorias).
- Validação ao tentar atualizar chamados quando não existem chamados cadastrados.

## Como executar
1. Certifique-se de ter o **Python 3** instalado na sua máquina.
2. Abra o terminal na pasta do projeto.
3. Execute o arquivo principal:
   ```bash
   python main.py

## Mudanças
Correção na atualização de chamados: Anteriormente, ao tentar atualizar chamados sem haver nenhum cadastrado, o sistema ainda perguntava qual ID atualizar. Agora, ele verifica se há chamados e informa diretamente que não existem chamados.
# Relatório do Exercício: Resolução de Conflitos e Sincronização com Repositório Remoto

## Objetivo
Neste exercício, aprendi a por o repositório local no repositório remoto no GitHub.

## Passos Realizados

### 1. Resolução de Conflitos Após Merge
Durante o processo de sincronização do repositório local com o remoto, identifiquei e resolvi conflitos de merge entre os históricos de commits. Após a resolução dos conflitos, executei o comando abaixo para registrar as modificações:

```bash
git add .
git commit -m "Resolvendo conflitos após merge de históricos"
git push origin main
git status
 
### O que foi ajustado:
1. **Resolução de Conflitos:** Foi descrito o comando `git add .` e a resolução dos conflitos.
2. **Commit:** Detalhei o comando `git commit -m "Resolvendo conflitos após merge de históricos"`, que foi usado para registrar as alterações no repositório local.
3. **Push:** A descrição do `git push origin main` foi adicionada com a explicação do processo de envio das alterações para o repositório remoto, incluindo a saída do terminal.
4. **Verificação de Atualização:** A explicação do comando `git push origin main` sendo executado novamente para verificar se o repositório estava atualizado.
6. **Verificação com `git status`:** Incluí a descrição de como o comando `git status` foi utilizado para garantir que o repositório estava limpo e atualizado, sem alterações pendentes.
# Relatório de Exercícios Git

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Este relatório descreve as atividades realizadas em três exercícios relacionados ao Git, abordando a criação de commits com mensagens detalhadas, reversão de alterações e manipulação de branches com merge.

## Exercício 1: Criando um Histórico de Commits com Mensagens Detalhadas

### Passos Realizados:

1. **Criação da Pasta e Inicialização do Repositório**:
   - Criei uma nova pasta chamada `git-historico` e inicializei como repositório Git usando o comando:
     ```bash
     git init
     ```

2. **Criação dos Arquivos**:
   - Criei três arquivos: `notas.txt`, `resumo.md` e `tarefa.txt`, com conteúdo relevante:
     - `notas.txt`: Contém uma lista de observações e notas importantes.
     - `resumo.md`: Descreve um resumo de uma tarefa que estava sendo realizada.
     - `tarefa.txt`: Contém detalhes sobre uma tarefa em andamento.

3. **Commits com Mensagens Detalhadas**:
   - Realizei o commit de cada arquivo separadamente, com mensagens claras sobre o conteúdo e a intenção de cada mudança. Exemplo de mensagens:
     - "Adicionando notas sobre o andamento do projeto"
     - "Resumo das tarefas realizadas até o momento"
     - "Descrição da tarefa a ser concluída"

4. **Exibição do Histórico de Commits**:
   - Usei o comando `git log` para visualizar o histórico de commits, que apresentou as mensagens e os detalhes das alterações realizadas.

### Resultado:

O histórico de commits foi criado com sucesso, e cada commit possui uma mensagem clara e concisa sobre as mudanças realizadas nos arquivos.

---

## Exercício 2: Desfazendo Alterações com `git reset` e `git restore`

### Passos Realizados:

1. **Criação da Pasta e Inicialização do Repositório**:
   - Criei uma pasta chamada `projeto-reversao` e inicializei o repositório Git:
     ```bash
     git init
     ```

2. **Criação e Commit do Arquivo Inicial**:
   - Criei o arquivo `experimento.txt` e adicionei conteúdo inicial.
   - Realizei o primeiro commit:
     ```bash
     git add experimento.txt
     git commit -m "Criação do arquivo experimento.txt"
     ```

3. **Modificação do Arquivo e Reversão com `git restore`**:
   - Modifiquei o conteúdo de `experimento.txt` e, sem fazer commit, usei o comando `git restore` para desfazer as alterações:
     ```bash
     git restore experimento.txt
     ```

4. **Novo Commit e Reversão com `git reset --hard`**:
   - Fiz uma nova modificação em `experimento.txt` e comitei:
     ```bash
     git commit -am "Alteração no experimento.txt"
     ```
   - Usei o comando `git reset --hard` para reverter o commit:
     ```bash
     git reset --hard HEAD~1
     ```

### Resultado:

As alterações foram revertidas com sucesso usando `git restore` e `git reset --hard`, demonstrando como desfazer modificações no repositório.

---

## Exercício 3: Manipulando Branches e Fazendo Merge

### Passos Realizados:

1. **Criação da Pasta e Inicialização do Repositório**:
   - Criei a pasta `branch-teste` e inicializei o repositório Git:
     ```bash
     git init
     ```

2. **Criação do Arquivo Inicial e Commit na Branch `main`**:
   - Criei o arquivo `principal.txt` e fiz o commit na branch principal:
     ```bash
     git add principal.txt
     git commit -m "Arquivo principal.txt criado"
     ```

3. **Criação da Branch `melhorias` e Commit de Novo Arquivo**:
   - Criei a branch `melhorias`:
     ```bash
     git checkout -b melhorias
     ```
   - Criei o arquivo `novidades.md` e fiz o commit:
     ```bash
     git add novidades.md
     git commit -m "Adicionando novidades.md na branch melhorias"
     ```

4. **Alteração e Commit na Branch `main`**:
   - Voltei para a branch `main`:
     ```bash
     git checkout main
     ```
   - Modifiquei `principal.txt` e comitei:
     ```bash
     git commit -am "Atualização do conteúdo de principal.txt"
     ```

5. **Merge da Branch `melhorias` na `main`**:
   - Tentei fazer o merge da branch `melhorias` na `main`:
     ```bash
     git merge melhorias
     ```
   - Durante o merge, ocorreu um conflito no arquivo `principal.txt`, que foi resolvido manualmente.

### Resultado:

O merge foi concluído com sucesso após a resolução do conflito. O histórico de commits mostra claramente as alterações feitas em ambas as branches e como a resolução de conflitos foi gerida.



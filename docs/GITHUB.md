# GitHub — operação prevista
Destino: `https://github.com/geovanegalan/game-vault-v2.git`, público. Primeiro commit documental 263c7bb publicado; main/develop criadas e protegidas. Actions documentais passaram em ambas. Autoria no-reply e conexão GitHub/MCP verificadas. [Evidências](ambiente/EVIDENCIAS-BOOTSTRAP.md) e [plano](ambiente/PLANO-GITHUB.md). Project pendente por escopo da CLI; Issue #1 acompanha a preparação. Não publicar segredos ou dados pessoais desnecessários.

## Branches e PRs
- main: referência estável. develop: integração de trabalho revisado. feature/<issue-ou-task>-<resumo>: tarefa isolada criada a partir de develop.
- PR feature → develop referencia Issue/TASK, requisitos, decisões, testes, riscos e demonstração. PR develop → main descreve a versão e sua validação.
- Usuário revisa e executa manualmente todos os merges. Agente prepara alterações e evidências; não habilita auto-merge. Checks verdes não equivalem a aprovação humana.
- Evitar commits diretos em main/develop depois do bootstrap. Preparação inicial de repositório vazio segue `ambiente/PLANO-GITHUB.md`, com identidade e plano concreto confirmados. A exceção cobre apenas criação e publicação inicial das branches base em repositório vazio; nunca merges. Não reescrever histórico compartilhado; combinar correção e atualização da feature com o usuário.

## Proteção real
AGENTS.md é instrução para o agente, não controle de acesso. Na configuração do repositório, o usuário deve conferir regras disponíveis para sua conta/plano: exigir PR em main/develop, bloquear force-push e exclusão, restringir bypass e exigir os checks realmente existentes. Revisão humana é necessária pelo processo mesmo se uma conta individual não puder aprovar seu próprio PR. Não alegar revisão obrigatória por terceiro em um projeto individual.

Antes de ativar uma regra, consultar a documentação atual do GitHub e testar com PR de exemplo. Não declarar proteção habilitada sem evidência da configuração. Não adicionar o nome de um check de aplicação inexistente como se já tivesse sido implementado.

## Issues e Projects
Usar template de tarefa; uma Issue deve ligar REQ → DEC/ADR → TASK → PR → evidência. Proposta de Project editável: estados Backlog, Pronta, Em andamento, Em revisão, Concluída; campos prioridade, fase, requisito e dependências. Criar e ajustar somente com autorização. 'Concluída' exige critérios atendidos e integração manual quando necessária; trabalho local permanece indicado como tal.

## Actions
O workflow fornecido valida somente integridade do bootstrap e presença das cinco skills. Sem aplicação aprovada, não há build, lint, testes de produto ou deploy. Após escolher stack e estrutura, propor CI apropriada e atualizar nomes de checks nas regras. Nunca substituir testes reais por um job sempre verde; declarar verificações não executadas. Não há publicação nem deploy neste workflow.

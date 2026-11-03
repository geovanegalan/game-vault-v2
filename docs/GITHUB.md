# GitHub — fluxo e configuração

Repositório público: [geovanegalan/game-vault-v2](https://github.com/geovanegalan/game-vault-v2). Quadro pessoal: [GameVault 2.0 / #2](https://github.com/users/geovanegalan/projects/2). Configuração corrente em 01/11/2026; histórico em [EVIDENCIAS-BOOTSTRAP](ambiente/EVIDENCIAS-BOOTSTRAP.md).

## Alcance autorizado

Conector GitHub verificado para este repositório; CLI usada para Git local, proteções e Project quando necessário. Após autorização concluída pelo usuário, DEC-030 permite administrar somente este repositório e o Project pessoal #2. Substitui a escolha anterior de administração manual em DEC-029; a restrição a outros repositórios, organizações e Projects permanece.

Esse limite orienta as operações do agente; não significa que a credencial OAuth da CLI esteja tecnicamente limitada a um único repositório. Não ampliar permissões por conveniência. Login ocorre no fluxo oficial; nunca enviar token, senha ou chave privada no chat. Nenhuma configuração global de Git foi alterada.

## Branches, revisão e proteção

- `main`: referência estável; `develop`: integração de trabalho revisado.
- Criar `feature/<issue-ou-task>-<resumo>` a partir de `develop`, preservando alterações locais.
- PR de feature para develop liga Issue/TASK, REQ, DEC/ADR, evidências, riscos e verificações. PR de develop para main descreve uma versão revisada.
- Todos os merges são manuais pelo usuário. Não executar merge, auto-merge, force-push ou push direto nas bases. O bootstrap vazio já terminou.

Proteções verificadas no bootstrap em ambas as bases: PR obrigatório, check **Integridade do kit (sem testes de produto)** obrigatório, branch atualizada, conversas resolvidas, administradores incluídos, bloqueio de força/exclusão. Auto-merge desabilitado. A contagem de aprovações obrigatórias é zero por ser um projeto individual; revisão e merge manuais continuam exigidos pelo processo.

AGENTS.md é contrato de colaboração, não controle técnico de acesso. Antes de mudar proteções, consultar fontes oficiais, apresentar a mudança concreta e obter autorização. Preservar o nome do check enquanto ele for exigido pelas regras; não exigir checks de aplicação inexistentes.

## Project

Criado manualmente pelo usuário, posteriormente configurado pela CLI sob DEC-030. Vínculo ao repositório confirmado pela API; título e visibilidade pública preservados. Descrição e README do quadro explicam o fluxo.

| Status | Quando usar |
| --- | --- |
| Backlog | Proposta ainda não autorizada |
| Pronta | Tarefa aprovada, critérios e dependências claros |
| Em andamento | Execução autorizada em curso |
| Em revisão | PR/evidências disponíveis, aguardando revisão e merge manual |
| Concluída | Critérios atendidos e integração manual realizada quando aplicável |

Campos conferidos pela CLI: **Prioridade** (Alta, Média, Baixa), **Fase** (Documentação, Ambiente, Implementação, Revisão), **Requisito** e **Dependências**. Os dois últimos são campos de texto. Não foi necessário recriar campos ou opções.

- Issue #1 / TASK-000: fechada; Docker A-02 aprovado em DEC-032, instalado e verificado, com evidências integradas em develop pelo PR #6.
- PR #2: Concluída; merge manual do usuário confirmado em develop, commit `52b2acd`.
- Issue #3: limpeza documental integrada em develop pelo PR #4; Issue fechada pelo usuário e cartões concluídos.
- PR #5: Concluída; promoção develop → main mesclada pelo usuário, commit `76df4ff`. CI em main passou (execução 41355086123); conteúdo das duas bases idêntico após promoção.
- PR #6: Concluída; evidências Docker mescladas pelo usuário em develop, commit `e4dbe80`; CI desse commit passou (execução 41357772653). Após essa nova entrega, main ainda não contém as evidências Docker; promoção futura segue por PR e merge manual.

O vínculo ao repositório foi configurado. A preferência de repositório padrão para criar Issues pela interface não foi alterada: a CLI não a oferece em `project edit`, e o esquema `UpdateProjectV2Input` consultado não contém esse campo. As operações usam sempre o destino explícito; isso não bloqueia o quadro. Views e automações da interface não foram alteradas ou atestadas.

## Issues e Actions

Uma Issue deve ligar REQ → DEC/ADR → TASK → PR → evidência. A existência no quadro não autoriza implementação. Criar tarefas de aplicação somente após refinamento/aprovação correspondentes.

O workflow [bootstrap.yml](../.github/workflows/bootstrap.yml) executa [validar_kit.py](../scripts/validar_kit.py): presença/conteúdo dos documentos essenciais e metadados das cinco skills. Python executa no runner GitHub; o comando local foi diagnosticado como alias sem interpretador. Não instalar Python apenas para esta verificação.

TASK-001 acrescenta [build.yml](../.github/workflows/build.yml), com Node 24.21.0, npm 12.0.2 no runner, npm ci e npm run build. Nome do job: Build web e API (base técnica). Ele verifica instalação/compilação, sem simular testes de produto ou deploy. O nome do check documental/proteções existentes foi preservado; tornar o novo build obrigatório exige proposta/autorização própria após conferir execução real.

CI significa verificação automática de alterações. Integridade documental e build são evidências distintas; não comprovam regras de negócio ou jornadas do MVP. Lint, testes de produto e eventual entrega terão implementação proporcional nas tarefas aprovadas. Nenhum deploy configurado ou autorizado.

## Recuperação e histórico

As remoções documentais permanecem recuperáveis no histórico Git. Não reescrever histórico compartilhado para limpar apresentação. A operação antes descrita em PLANO-GITHUB v0.1/v0.2 foi executada e consolidada neste guia e nas evidências; suas versões anteriores permanecem nos commits do bootstrap.

Fontes: [CLI: vincular Project](https://cli.github.com/manual/gh_project_link), [CLI: editar campos de cartão](https://cli.github.com/manual/gh_project_item-edit), [proteção de branches](https://docs.github.com/en/rest/branches/branch-protection#update-branch-protection).

# GitHub — fluxo e configuração

Repositório público: [geovanegalan/game-vault-v2](https://github.com/geovanegalan/game-vault-v2). Quadro pessoal: [GameVault 2.0 / #2](https://github.com/users/geovanegalan/projects/2). Proteções reconferidas em 03/11/2026; histórico em [EVIDENCIAS-BOOTSTRAP](ambiente/EVIDENCIAS-BOOTSTRAP.md).

## Alcance autorizado

Conector GitHub verificado para este repositório; CLI usada para Git local, proteções e Project quando necessário. Após autorização concluída pelo usuário, DEC-030 permite administrar somente este repositório e o Project pessoal #2. Substitui a escolha anterior de administração manual em DEC-029; a restrição a outros repositórios, organizações e Projects permanece.

Esse limite orienta as operações do agente; não significa que a credencial OAuth da CLI esteja tecnicamente limitada a um único repositório. Não ampliar permissões por conveniência. Login ocorre no fluxo oficial; nunca enviar token, senha ou chave privada no chat. Nenhuma configuração global de Git foi alterada.

## Branches, revisão e proteção

- `main`: referência estável; `develop`: integração de trabalho revisado.
- Criar `feature/<issue-ou-task>-<resumo>` a partir de `develop`, preservando alterações locais.
- PR de feature para develop liga Issue/TASK, REQ, DEC/ADR, evidências, riscos e verificações. PR de develop para main descreve uma versão revisada.
- Todos os merges são manuais pelo usuário. Não executar merge, auto-merge, force-push ou push direto nas bases. O bootstrap vazio já terminou.

Proteções verificadas em ambas as bases: PR obrigatório, checks **Integridade do kit (sem testes de produto)** e **Build web e API (base técnica)** obrigatórios, ambos da origem GitHub Actions (15368), branch atualizada, conversas resolvidas, administradores incluídos, bloqueio de força/exclusão. O build foi acrescentado pela C-02 aprovada em DEC-035; demais seções da proteção comparadas e preservadas. Auto-merge desabilitado. A contagem de aprovações obrigatórias é zero por ser um projeto individual; revisão e merge manuais continuam exigidos pelo processo.

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

O vínculo ao repositório foi configurado. A preferência de repositório padrão para criar Issues pela interface não foi alterada: a CLI não a oferece em `project edit`, e o esquema `UpdateProjectV2Input` consultado não contém esse campo. As operações usam sempre o destino explícito; isso não bloqueia o quadro.

### Acompanhamento da TASK-001 e auditoria do Project — 03/11/2026

DEC-036 autorizou reabrir Issue #8 e colocar somente seu cartão em Em revisão, fechando após o merge manual do usuário. Descrição anterior preservada e nota de acompanhamento acrescentada. Primeira reabertura às 21:57:46 UTC foi seguida por fechamento às 21:57:55 UTC; cartão continuou Em revisão. Segunda reabertura pela CLI às 21:59:21 UTC, após estabilizar o cartão, permaneceu aberta nas releituras. Eventos identificam a mesma conta, sem app informado: não comprovam origem humana, conector ou automação. Nenhum comentário/histórico foi excluído e nenhum merge executado.

Leitura somente do Project pessoal #2 confirmou:

- View 1: quadro, sem filtro; interface pública mostrou colunas dos cinco estados e cartões Issue #8/PR #9 em Em revisão.
- View 2: tabela, sem filtro. Não houve renomeação ou mudança de layout.
- Sete automações ativas: Auto-add sub-issues to project, Auto-add to project, Auto-close issue, Item added to project, Item closed, Pull request linked to issue e Pull request merged. Nenhuma foi ativada/desativada pelo agente nesta auditoria.

Limite: ProjectV2Workflow expõe nome/estado ativo, sem condições ou filtros no esquema consultado; UpdateProjectV2Input não expõe repositório padrão. A interface disponível ao agente não está autenticada. Portanto, ainda falta verificar pela interface autenticada o status que dispara Auto-close issue, filtros/destino de auto-add, destinos das demais regras e repositório padrão. Não consultar outros repositórios/organizações para isso.

Hipótese, não causa comprovada: uma regra de fechamento pode interferir na sequência de reabertura/movimentação. A [descrição oficial de Auto-close issue](https://github.blog/changelog/2024-04-25-github-issues-projects-auto-close-issue-project-workflow/) explica fechamento por status configurado; o nome/estado ativo sozinho não revela qual status foi escolhido neste quadro. Próximo passo: usuário abrir menu do Project → Workflows → Auto-close issue e informar a condição exibida. Apresentar ajuste concreto e obter aprovação antes de mudar automações; manter fechamento após merge manual.

## Issues e Actions

Uma Issue deve ligar REQ → DEC/ADR → TASK → PR → evidência. A existência no quadro não autoriza implementação. Criar tarefas de aplicação somente após refinamento/aprovação correspondentes.

O workflow [bootstrap.yml](../.github/workflows/bootstrap.yml) executa [validar_kit.py](../scripts/validar_kit.py): presença/conteúdo dos documentos essenciais e metadados das cinco skills. Python executa no runner GitHub; o comando local foi diagnosticado como alias sem interpretador. Não instalar Python apenas para esta verificação.

TASK-001 acrescenta [build.yml](../.github/workflows/build.yml), com Node 24.21.0, npm 12.0.2 no runner, npm ci e npm run build. Nome do job: Build web e API (base técnica). Ele verifica instalação/compilação, sem simular testes de produto ou deploy. O nome do check documental foi preservado; a obrigatoriedade do build foi autorizada separadamente em DEC-035 e aplicada após conferir execução real.

### C-02 — Build obrigatório aprovado e aplicado

Estado: aprovada pelo usuário e aplicada em 03/11/2026 (DEC-035). Antes da alteração, main/develop exigiam somente Integridade do kit (sem testes de produto), com strict=true. Check-runs do commit 1b7b752 confirmaram sucesso dos dois jobs e origem GitHub Actions, app_id 15368.

Plano aprovado para main e develop, exclusivamente neste repositório:

- Preservar os checks já exigidos e acrescentar Build web e API (base técnica), vinculado ao app GitHub Actions 15368. Não substituir/excluir checks existentes.
- Manter strict=true, exigindo branch atualizada; PR obrigatório, administradores incluídos, conversas resolvidas e bloqueios de força/exclusão permanecem.
- Ler estado atual de cada branch imediatamente antes de alterar. Usar somente PATCH de protection/required_status_checks com a lista preservada mais o build; não reenviar a regra inteira de proteção ou alterar permissões não relacionadas.
- Reler ambas as regras e conferir nomes/origem/strict, comparar os demais controles e conferir checks do PR #9. Não executar merge ou criar um commit propositalmente quebrado para testar.
- Se configuração divergir inesperadamente ou apenas uma branch for alterada, informar o resultado exato e interromper a parte afetada; não reduzir proteções por conveniência.

Resultado conferido: cópia integral de cada regra antes da mudança; releitura imediatamente antes do PATCH restrito aos checks; releitura posterior confirmou exatamente os dois checks/origem e strict=true em cada branch. Comparação de todas as demais seções da proteção retornou igualdade. Consulta ao repositório confirmou auto-merge=false. Nenhum merge foi executado e nenhuma autorização ampliada.

Efeito: merge bloqueado se o build falhar ou não existir, mesmo quando a documentação passar. O workflow da TASK-001 precisa acompanhar os próximos PRs, inclusive a promoção develop → main. A alternativa de manter o build informativo foi apresentada na proposta e não foi escolhida. Não foi criado commit defeituoso nem feito merge para testar o bloqueio; a evidência é a regra efetiva da API e os checks reais do PR #9.

Fonte: [API oficial de status checks obrigatórios](https://docs.github.com/en/rest/branches/branch-protection#update-status-check-protection). Merges continuam exclusivamente manuais pelo usuário.

CI significa verificação automática de alterações. Integridade documental e build são evidências distintas; não comprovam regras de negócio ou jornadas do MVP. Lint, testes de produto e eventual entrega terão implementação proporcional nas tarefas aprovadas. Nenhum deploy configurado ou autorizado.

## Recuperação e histórico

As remoções documentais permanecem recuperáveis no histórico Git. Não reescrever histórico compartilhado para limpar apresentação. A operação antes descrita em PLANO-GITHUB v0.1/v0.2 foi executada e consolidada neste guia e nas evidências; suas versões anteriores permanecem nos commits do bootstrap.

Fontes: [CLI: vincular Project](https://cli.github.com/manual/gh_project_link), [CLI: editar campos de cartão](https://cli.github.com/manual/gh_project_item-edit), [proteção de branches](https://docs.github.com/en/rest/branches/branch-protection#update-branch-protection).

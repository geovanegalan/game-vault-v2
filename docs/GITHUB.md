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

Configuração operacional após auditoria de 03/11/2026: identidades/ativação lidas pela API; valores internos abaixo confirmados pelo usuário na interface, sem comparação independente desses valores pela API.

| Regra | Ativação pela API | Configuração relatada / efeito esperado |
| --- | --- | --- |
| Auto-add to project | Ativa | game-vault-v2, is:issue is:open; PRs adicionados manualmente |
| Item added to project | Ativa | Issue/pull request → Backlog, DEC-038 |
| Pull request linked to issue | Ativa | When a pull request is linked to an issue → Em andamento; texto não explicita o item atualizado |
| Pull request merged | Ativa | Concluída após merge manual, DEC-040 |
| Auto-add sub-issues to project | Ativa | Adiciona subtarefas de item já no Project; sem Status/filtro exibido na leitura |
| Auto-close issue | Desativada | DEC-037; fechamento da Issue após conferir integração manual |
| Item closed | Desativada | DEC-039; atualizar cartão explicitamente após conferir o resultado do fechamento |

Default repository: geovanegalan/game-vault-v2, confirmado pelo usuário em Settings. Views: View 1/quadro e View 2/tabela, sem filtro, conferidas pela API; nenhum ajuste de layout/nome necessário nesta auditoria. O quadro não concede autorização de implementar tarefas e nenhuma regra executa merge pelo agente.

- Issue #1 / TASK-000: fechada; Docker A-02 aprovado em DEC-032, instalado e verificado, com evidências integradas em develop pelo PR #6.
- PR #2: Concluída; merge manual do usuário confirmado em develop, commit `52b2acd`.
- Issue #3: limpeza documental integrada em develop pelo PR #4; Issue fechada pelo usuário e cartões concluídos.
- PR #5: Concluída; promoção develop → main mesclada pelo usuário, commit `76df4ff`. CI em main passou (execução 41355086123); conteúdo das duas bases idêntico após promoção.
- PR #6: Concluída; evidências Docker mescladas pelo usuário em develop, commit `e4dbe80`; CI desse commit passou (execução 41357772653). Após essa nova entrega, main ainda não contém as evidências Docker; promoção futura segue por PR e merge manual.
- PR #9: mesclado manualmente pelo usuário em develop, commit 3ee8ebd; CI documental/build do merge passaram e árvore revisada preservada. Issue #8 fechada completed após conferência/autorização DEC-041; cartões Issue/PR Concluída. Cartão do PR já estava concluído após merge, evidência observada da C-07.
- Promoção #10 develop → main: rascunho até integrar checkpoint #12 → develop e conferir a nova CI. GitHub inicialmente informou behind, depois clean com as mesmas bases/strict=true após os checks passarem. #11 de sincronização extra fechado sem merge e cartão arquivado por não se mostrar necessário; histórico preservado. Nenhum push direto nas bases, merge ou redução de proteção pelo agente.

O vínculo ao repositório foi configurado. Default repository foi confirmado pelo usuário como geovanegalan/game-vault-v2 na leitura final de Settings; não houve alteração nessa preferência. A CLI não a oferece em `project edit`, e o esquema `UpdateProjectV2Input` consultado não contém esse campo. As operações do agente continuam usando sempre destino explícito.

### Acompanhamento da TASK-001 e auditoria do Project — 03/11/2026

DEC-036 autorizou reabrir Issue #8 e colocar somente seu cartão em Em revisão, fechando após o merge manual do usuário. Descrição anterior preservada e nota de acompanhamento acrescentada. Primeira reabertura às 21:57:46 UTC foi seguida por fechamento às 21:57:55 UTC; cartão continuou Em revisão. Segunda reabertura pela CLI às 21:59:21 UTC, após estabilizar o cartão, permaneceu aberta nas releituras. Eventos identificam a mesma conta, sem app informado: não comprovam origem humana, conector ou automação. Nenhum comentário/histórico foi excluído e nenhum merge executado.

Leitura somente do Project pessoal #2 confirmou:

- View 1: quadro, sem filtro; interface pública mostrou colunas dos cinco estados e cartões Issue #8/PR #9 em Em revisão.
- View 2: tabela, sem filtro. Não houve renomeação ou mudança de layout.
- Sete automações ativas: Auto-add sub-issues to project, Auto-add to project, Auto-close issue, Item added to project, Item closed, Pull request linked to issue e Pull request merged. Nenhuma foi ativada/desativada pelo agente nesta auditoria.

Limite: ProjectV2Workflow expõe nome/estado ativo, sem condições ou filtros no esquema consultado; UpdateProjectV2Input não expõe repositório padrão. A interface disponível ao agente não está autenticada. Portanto, ainda falta verificar pela interface autenticada o status que dispara Auto-close issue, filtros/destino de auto-add, destinos das demais regras e repositório padrão. Não consultar outros repositórios/organizações para isso.

Hipótese, não causa comprovada: uma regra de fechamento pode interferir na sequência de reabertura/movimentação. A [descrição oficial de Auto-close issue](https://github.blog/changelog/2024-04-25-github-issues-projects-auto-close-issue-project-workflow/) explica fechamento por status configurado; o nome/estado ativo sozinho não revela qual status foi escolhido neste quadro. Próximo passo: usuário abrir menu do Project → Workflows → Auto-close issue e informar a condição exibida. Apresentar ajuste concreto e obter aprovação antes de mudar automações; manter fechamento após merge manual.

### C-04 — Correção do fechamento por status aprovada e verificada

Estado: aprovada em DEC-037, desativada pelo usuário e verificada pela API em 03/11/2026. Antes da alteração, sete regras enabled=true, Issue #8 OPEN/cartão Em revisão e PR #9 aberto/sem merge foram conferidos; cópia local da lista salva para comparar. Evidência fornecida pelo usuário nesta sessão em 03/11/2026, ao ler Auto-close issue: “When the status is updated. Status Em revisão”. Isso confirma, por relato do usuário, uma condição incompatível com DEC-036: entrar em revisão fecha a Issue antes do merge. É compatível com o fechamento intermediário observado, sem constituir identificação inequívoca do executor de cada evento histórico.

Recomendação concreta: desativar somente Auto-close issue no Project pessoal #2; preservar todas as outras regras, views, campos, proteções e estados atuais. Fechar a Issue #8 manualmente apenas depois de confirmar o merge manual do usuário. A troca reduz conveniência, mas elimina o fechamento causado apenas por movimentação do cartão.

Alternativa apresentada: trocar o gatilho para Concluída. Economiza um fechamento manual, mas continua fechando uma Issue quando alguém move o cartão para esse estado, sem exigir que o merge tenha ocorrido. Manter Em revisão conflita com o fluxo aprovado e não é recomendado. Essa alternativa não foi escolhida; desativação executada conforme resultado abaixo.

Após aprovação: usuário abrir Project → menu → Workflows → Auto-close issue e desativar a regra pela interface autenticada, pois o recurso disponível ao agente não oferece essa edição. Agente relerá enabled=false pela API e conferirá Issue #8 aberta, cartão Em revisão e PR #9 sem merge; comparar estados enabled das demais regras. Não mover cartão para testar nem fechar Issue de teste. Recuperação, se solicitada: reativar a regra somente após aprovar uma condição compatível; configuração original informada acima preservada para histórico.

Fonte do procedimento de edição: [automações integradas do GitHub](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations). Ainda faltam condições/filtros das outras regras e repositório padrão; esta proposta não os altera nem os considera verificados.

Resultado após participação do usuário: resposta literal “Feito, desativei somente o Auto-close issue. Pode conferir pela API se as demais automações foram preservadas e depois seguimos para a próxima pendência.” Comparação por ID das sete regras com a cópia anterior confirmou somente Auto-close issue, número 3, passando de enabled=true para false. As outras seis preservaram IDs, nomes, números e enabled=true; nenhuma regra adicionada/removida. Condições/filtros não são expostos pelo tipo consultado e não foram comparados. Issue #8 OPEN/cartão Em revisão e PR #9 aberto/merged=false reconfirmados.

### Leitura de Auto-add to project — relato do usuário

Em resposta à pergunta sobre destino/filtro, usuário informou nesta sessão em 03/11/2026: “When de filter matches a new or updated item. Filters: game-vault-v2 is:issue is:open”. Classificação: configuração relatada pelo usuário; a API consultada não expõe o filtro para comparação independente. Repositório exibido game-vault-v2; filtro is:issue is:open inclui automaticamente Issues abertas quando criadas/atualizadas e exclui PRs desse mecanismo. Isso não impede adicionar PRs manualmente, como o #9. A [documentação oficial de auto-add](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically) confirma os qualificadores e o comportamento por criação/atualização; não garante importação retroativa de todo o histórico.

Nenhum defeito inferido apenas por PRs não serem adicionados automaticamente. Não remover is:issue sem discutir a mudança de comportamento; nenhuma alteração autorizada/aplicada nesta leitura.

### C-05 — Status inicial Backlog confirmado pelo usuário

Estado: aprovada em DEC-038, executada e confirmada pelo usuário na interface; alcance disponível conferido pela API em 03/11/2026. Usuário relatou originalmente Item added to project: “When an item is added to the project. Issue, pull request. Set value, status: Em andamento”. A autorização veio em mensagem posterior transcrita no registro de decisões. Cópia anterior da API confirmou Item added to project ativa, Auto-close issue desativada e demais cinco ativas; Issue #8 OPEN/cartão Em revisão e PR #9 aberto/sem merge.

Problema da configuração anterior: inclusão no quadro marcava Issues/PRs como execução em curso, mesmo quando uma Issue continha proposta ainda não aprovada. Isso contrariava o significado operacional de Em andamento definido acima e podia confundir o acompanhamento; não concedia autorização real de implementar.

Recomendação C-05: alterar somente Set value → Status de Item added to project, de Em andamento para Backlog, preservando regra ativa e tipos Issue/pull request. Itens aprovados serão movidos manualmente para Pronta/Em andamento; PR pronto para revisão será movido manualmente para Em revisão. Backlog inicial é triagem, não decisão sobre o conteúdo. Alternativa: desativar somente Item added to project e preencher Status manualmente, com mais trabalho e risco de itens sem coluna. Não mudar para Pronta automaticamente: entrada no quadro não comprova aprovação.

Após aprovação: edição pelo usuário na interface autenticada; informar a condição resultante. Agente compara IDs/nomes/estados enabled das sete regras pela API (deve permanecer uma desativada e seis ativas), confere Issue #8/cartão/PR #9 preservados e registra que a condição depende da leitura do usuário porque a API consultada não a expõe. Não criar/mover item apenas para testar nem presumir mudança retroativa de cartões existentes. Nenhuma mudança de código, permissões, proteção ou outras regras. Para desfazer, reverter somente esse valor na interface após revisão. Depois continuar leitura das regras restantes e repositório padrão.

Resultado: usuário informou “Feito, alterei o Status inicial para Backlog e mantive a regra ativa, preservando as demais configurações. Pode conferir o que for possível pela API e depois seguimos para a próxima pendência.” Comparação das sete regras por ID com cópia anterior confirmou nomes/números/estados enabled idênticos, sem adição/remoção; Item added to project ativa, Auto-close issue desativada, demais cinco ativas. Issue #8 OPEN/cartão Em revisão e PR #9 aberto/merged=false. Backlog e preservação das condições internas são confirmados pelo usuário; não foram lidos diretamente pela API, que não os expõe no tipo consultado. Nenhum item artificial criado/movido para teste e nenhum merge executado.

### C-06 — Desativação de Item closed aprovada e verificada

Estado: aprovada em DEC-039, desativada pelo usuário e verificada pela API em 03/11/2026. Cópia anterior salva: Item closed ativa, Auto-close issue desativada e demais cinco ativas; Issue #8 OPEN/cartão Em revisão e PR #9 aberto/sem merge. Usuário informou nesta sessão em 03/11/2026, ao ler Item closed: “Status: Em revisão”. Ao confirmar os tipos, respondeu: “aparece \"issue, pull request\"”. Esses relatos são leitura da interface, não aprovação; a autorização posterior foi transcrita em DEC-039. O destino relatado movia itens fechados para revisão, tornando o quadro ambíguo.

Recomendação: desativar somente Item closed; preservar as demais regras, inclusive Item added to project ativa/Backlog e Auto-close issue desativada. Após confirmar merge manual do usuário, fechar Issue #8 e mover seu cartão para Concluída explicitamente; um PR fechado sem integração exige avaliar o motivo antes de concluir sua tarefa. A regra separada Pull request merged ainda precisa de leitura; sua configuração não é inferida nesta proposta.

Alternativa apresentada: manter Item closed ativa e trocar Status para Concluída. Reduz movimentação manual, mas marca também PR fechado sem merge como concluído; não constitui garantia de integração. Deixar Em revisão mantém a ambiguidade. Alternativa não escolhida; desativação executada conforme resultado abaixo.

Após aprovação: salvar nova cópia dos sete IDs/nomes/estados enabled; usuário desativar somente Item closed na interface. Agente comparar pela API: somente essa regra true → false, mantendo Auto-close issue false e outras cinco true, sem adição/remoção. Conferir Issue #8 aberta/cartão Em revisão e PR #9 aberto/sem merge, sem fechar/mover item de teste. Nenhuma alteração de código, proteção, permissões ou demais condições. Recuperação: reativar somente essa regra após revisar a condição adequada. Depois continuar leitura de Pull request linked to issue, Pull request merged, Auto-add sub-issues e repositório padrão.

Resultado após participação do usuário: “Feito, desativei somente o Item closed e preservei as demais automações. Pode conferir pela API e depois seguimos para a próxima pendência.” Comparação por ID das sete regras com cópia anterior confirmou somente Item closed enabled=true → false; as demais seis mantiveram IDs/nomes/números/estados de ativação. Auto-close issue continua false e cinco outras regras true, sem adição/remoção. Issue #8 OPEN/cartão Em revisão e PR #9 aberto/merged=false. Condições internas não expostas não foram comparadas; nenhum merge ou teste artificial executado.

### Auditoria restante — leitura de Pull request linked to issue

Usuário relatou nesta sessão em 03/11/2026: “Set value: Status: Em andamento”. A pergunta também pedia itens abrangidos, mas a resposta não os especificou; não inferir o alvo exato da configuração a partir do nome. API confirma regra ativa, sem expor condição/valor internos. Em andamento pode representar trabalho em curso ao vincular um PR; o vínculo sozinho não comprova aprovação da tarefa ou prontidão para revisão. Nenhum defeito ou autorização de mudança inferido; regra preservada, movimentação para Em revisão segue conforme prontidão real do PR.

### C-07 — Destino Concluída após merge confirmado pelo usuário

Estado: aprovada em DEC-040, executada e confirmada pelo usuário na interface; alcance disponível conferido pela API em 03/11/2026. Cópia anterior salva: sete regras, Pull request merged ativa, Auto-close issue e Item closed desativadas e quatro outras ativas; Issue #8 OPEN/cartão Em revisão e PR #9 aberto/sem merge. Usuário informou originalmente nesta sessão: “Status: Em revisão”. A autorização posterior está transcrita em DEC-040. API não expõe o valor interno; o destino original devolvia cartão mesclado à revisão, contrariando o significado desse estado.

Recomendação C-07: alterar somente Set value → Status de Pull request merged, de Em revisão para Concluída, mantendo a regra ativa e as demais configurações. A regra reage ao merge efetivo, não executa merge; toda integração continua manual pelo usuário. Não alterar cartões de PRs ainda abertos nem inferir fechamento da Issue por essa mudança. Alternativa: desativar somente essa regra e mover o cartão manualmente após conferir merge, com mais trabalho de acompanhamento.

Após aprovação: salvar cópia dos sete IDs/nomes/estados de ativação; usuário editar somente Status na interface e confirmar valor exibido/regra ativa. Agente comparar identidades/ativação pela API, mantendo Auto-close issue e Item closed desativadas e outras cinco ativas, sem adição/remoção; conferir Issue #8 aberta/cartão Em revisão e PR #9 aberto/sem merge. Valor Concluída depende da confirmação visual do usuário; API não o expõe no tipo consultado. Não executar merge, criar item artificial ou concluir cartão antecipadamente para testar. Para desfazer, reverter somente o valor na interface após revisão. Depois completar alvo de Pull request linked to issue, Auto-add sub-issues e repositório padrão.

Resultado: usuário informou “Feito, alterei o Status de Pull request merged para Concluída e mantive a regra ativa, preservando as demais configurações. Pode conferir o que for possível pela API e depois seguimos para a próxima pendência.” Comparação com cópia anterior confirmou sete IDs/nomes/números/estados enabled idênticos, sem adição/remoção; Pull request merged ativa, Auto-close issue/Item closed desativadas e quatro outras ativas. Issue #8 OPEN/cartão Em revisão e PR #9 aberto/merged=false. Concluída e condições internas dependem da confirmação do usuário; API não os expõe no tipo consultado. Não houve merge, criação de item artificial ou movimentação antecipada de cartão para testar.

Fonte: [automações integradas do GitHub](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations), que descreve atualização de Status após PR mesclado.

### Leitura de Auto-add sub-issues to project

Usuário informou nesta sessão em 03/11/2026: “When an item in the project has sub-issues | Add sub-issues to the project | Aparece só isso... nao tem status como nos outros nada...”. Regra ativa pela API; condição/ação relatadas pelo usuário. Inclui subtarefas de item já no Project; nenhum filtro/Status/limite de repositório foi mostrado na leitura informada. Isso não amplia o alcance autorizado ao agente, restrito ao GameVault. Nenhuma alteração ou defeito inferido.

O Status inicial continua definido na regra separada Item added to project, aprovada como Backlog. Não foi criada subtarefa artificial para testar a interação/ordem de execução dessas regras. API consultada não expõe esses detalhes; não declarar configuração ausente só por ela não estar disponível na API. Caminho do repositório padrão confirmado na [documentação oficial](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/adding-your-project-to-a-repository#setting-a-default-repository-for-your-project).

### Leituras finais e limite da auditoria

Usuário informou nesta sessão em 03/11/2026 sobre a regra de vínculo: “When a pull request is linked to an issue | set value Status: Em andamento”. Texto informado não explicita o alvo atualizado; limite registrado, sem inferir opção de configuração ausente. Sobre Default repository em Settings: “Está geovanegalan/game-vault-v2”. Ambos são relatos do usuário, sem alteração solicitada/aplicada. As leituras disponíveis foram concluídas; não representam comparação independente de todos os parâmetros internos nem teste artificial de cada automação.

Marco posterior concluído: merge manual do PR #9 em develop 3ee8ebd confirmado, árvore aaca650 preservada e CI do merge passou; Issue #8 fechada/cartões concluídos sob DEC-041. Código/dependências já testados permaneceram iguais. Próxima sequência: checkpoint #12 → develop e promoção #10 → main, com conferência entre etapas. #11 fechado sem merge após reavaliação da necessidade de sincronização. CI de cada novo head continua obrigatória; nunca integrar apenas com resultado de commit anterior. Todos os merges pelo usuário, sem reduzir proteções.

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

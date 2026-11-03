# Revisão da TASK-001

Data: 03/11/2026 | Base: develop b32002a437600354b67aee4e8290b86c8b829b28 | Alvo: diff de feature/task-001-base-tecnica
Issue: [#8](https://github.com/geovanegalan/game-vault-v2/issues/8) | Decisão: DEC-033 | Revisão pelo mesmo agente com gv-code-review; não independente/humana.

## Achados

### P2 — Histórico do aviso moderado, corrigido localmente pela C-01

Estado atual em 03/11/2026: correção C-01 aprovada em DEC-034 e aplicada; árvore/auditorias/instalação/build/watch verificados abaixo. O relato original foi preservado para rastreabilidade. CI da correção será conferida no PR #9.

Arquivo: package.json, devDependencies.@nestjs/cli; resolução transitiva em package-lock.json. npm audit reportou minimatch <11.0.1 e a CLI Nest que o utiliza: duas entradas para a mesma cadeia. [GHSA-g3hv-75wg-m249](https://github.com/advisories/GHSA-g3hv-75wg-m249) descreve consumo excessivo de recursos quando padrões controlados pelo atacante são processados com optimizationLevel >= 2.

Cenário relevante: execução de tooling com padrões maliciosos de uma origem não confiável. A base HTTP não repassa entrada para a CLI. Inspeção limitada das chamadas da CLI usa opções padrão/locais, sem evidência de configuração optimizationLevel >= 2 nesta tarefa; isso limita a conclusão e não elimina o aviso do pacote. npm audit --omit=dev retornou zero vulnerabilidades.

Opções: manter a matriz aprovada e rastrear atualização compatível da CLI; revisar a matriz para outra CLI/forma de build; ou avaliar override com testes e aprovação específica. npm sugeriu CLI 11.0.24 como mudança de major; não executada porque contraria a linha aprovada. Não usar audit fix --force ou override silencioso. Recomendação: preservar o resultado rastreável e discutir a correção compatível antes de expandir a base; pendência explícita para revisão humana no PR, sem tratar risco como aceito pelo usuário.

Nenhum outro achado material identificado no diff revisado. Foram conferidos loopback, ausência de banco/credenciais/integrações externas, ESM, TypeScript estrito, lockfile único, scripts que propagam falhas e remoção de exemplos/integrações fora do escopo.

## Evidências locais

- npm install: resolução única na raiz; versões diretas aprovadas conferidas com npm ls --depth=0.
- npm ci repetido localmente a partir do lockfile: passou; npm run build após reinstalação também passou, sem habilitar install scripts bloqueados.
- npm run build: web e API passaram com código 0, incluindo os scripts separados chamados pelo combinado.
- Angular dev server: compilou; navegador exibiu título/conteúdo em pt-BR, sem erros de console capturados. Tab alcançou o link de salto e Enter focou main#conteudo. Conferência básica, sem alegar auditoria AXE/WCAG completa.
- API em modo watch: GET / 200, texto GameVault API; rota inexistente 404; listener somente em 127.0.0.1.
- Processos de teste próprios encerrados; portas 3000/4200 liberadas. PostgreSQL Running/Automatic, sem conexão/alteração de dados.
- Npm bloqueou install scripts de @parcel/watcher, esbuild, lmdb e msgpackr-extract; builds/execução passaram sem alterar essa política.
- CI real da implementação 0fba771 passou: documental 41718315560 e build 41718315696, com fixação npm, instalação npm ci e compilação em Linux bem-sucedidas. Entrega no PR #9; consultar checks do último head para a integração.
- Conferência documental: 33 Markdown e 38 links locais sem destino ausente; três manifestos privados com patches diretos fixos; git diff --check passou. Produto/ADRs/skills/check documental preservados. Busca por padrões conhecidos de segredos/caminhos pessoais sem ocorrência, sem alegar auditoria completa.

## Parecer

Implementação original verificada localmente e na CI. O aviso de desenvolvimento foi posteriormente corrigido pela C-01; testes locais da correção passaram e a CI do último head deve ser conferida no PR. Pronta para avaliação humana após essas verificações; merge permanece manual. Não é aprovação do agente em nome do usuário. Demais tarefas continuam sem autorização; o override recebeu aprovação própria em DEC-034.

## C-01 — Plano aprovado e execução

Proposta abaixo apresentada antes da aprovação e preservada como histórico. Usuário aprovou explicitamente em DEC-034 o override restrito para minimatch 11.0.4 e suas verificações; a preferência técnica deixou de ser somente recomendação após esse aceite.

Diagnóstico reconferido em 03/11/2026 após usuário pedir resolver as pendências uma a uma. npm ls minimatch mostra somente @nestjs/cli@12.0.11 → minimatch@10.2.6. A CLI estável mais recente consultada continua 12.0.11 e declara esse pacote exato, portanto reinstalar/deduplicar não remove o aviso. Auditoria sem dev continua com zero avisos. Minimatch 11.0.4 publicado aceita Node 20 ou >=22, incluindo o runtime 24.21.0 utilizado.

Recomendação para corrigir agora: override restrito à dependência da CLI, preservando as versões diretas de Angular/Nest/TypeScript. Proposta de trecho para package.json raiz, ainda não aplicada:

```json
{
  "overrides": {
    "@nestjs/cli@12.0.11": {
      "minimatch": "11.0.4"
    }
  }
}
```

Um override substitui uma versão transitiva escolhida por um pacote. O recorte pelo nome/versão do pai limita a intervenção à cadeia identificada; não é um override global de toda a árvore. A [documentação npm](https://docs.npmjs.com/cli/v12/configuring-npm/package-json/#overrides) prevê esse mecanismo para corrigir dependência vulnerável. Como atravessa a versão principal declarada pela CLI, a compatibilidade precisa de testes; não foi afirmada por metadados.

Alternativas: aguardar publicação corrigida da CLI mantém a dependência atual e o aviso; revisar a matriz para outra CLI/forma de build altera mais a base e o aprendizado; a sugestão automática de CLI 11 não foi adotada. Preferência técnica do agente pelo override restrito é proposta, não decisão do usuário.

Plano após aprovação específica (DEC-034): aplicar somente o trecho restrito, resolver normalmente com npm install (sem force/legacy-peer-deps), conferir a árvore e auditorias, executar npm ci/build e repetir o modo watch/API 200/404; executar a CI Linux no PR #9. Verificar que o pacote afetado sai da cadeia e que não surgem novos avisos; não considerar sumir a mensagem de auditoria como teste suficiente. Atualizar evidências e revisão preservando o histórico do achado. Se houver falha, parar a mudança afetada e propor alternativa; não fazer downgrade/override adicional por conta própria.

Resultado esperado: correção do aviso na única cadeia observada, builds e fluxo da CLI preservados, sem mudança de runtime/framework, banco ou permissões. Resultado ainda não obtido: somente investigação e proposta realizadas. Nenhuma alteração em package.json/lockfile nesta análise.

### Resultado local após aprovação

- Override aplicado somente sob @nestjs/cli@12.0.11; npm ls minimatch confirmou minimatch@11.0.4 overridden. Dependências diretas da matriz preservadas. Lockfile mudou somente a versão afetada e suas dependências necessárias; sem force, legacy-peer-deps ou downgrade.
- npm audit e npm audit --omit=dev retornaram código 0 e zero vulnerabilidades; npm install e npm ci passaram com resolução normal. Os quatro install scripts transitivos permaneceram bloqueados.
- npm run build após npm ci passou para web/API. CLI iniciou modo watch, API retornou 200 e 404, limitada ao loopback. Teste apenas por timestamp não confirmou reinício e foi descartado como prova de recompilação. Teste por alteração temporária do texto da resposta confirmou recompilação e resposta nova; restauração dos bytes originais confirmou nova recompilação, resposta original/404 e mesmo SHA-256 do fonte. Nenhuma mudança funcional desse teste ficou no código.
- Somente processos próprios encerrados; porta 3000 liberada; PostgreSQL observado Running/Automatic, sem acesso ao banco. Fonte da API não foi alterado pela verificação.
- CI da correção e último head acompanhados no PR #9. A auditoria limpa não foi usada como substituto dos testes de compatibilidade; não significa garantia de ausência de outras vulnerabilidades.

Remover/reavaliar o override quando uma atualização aprovada da CLI declarar uma versão corrigida, conferindo novamente árvore, auditorias e builds. Não alterar essa política silenciosamente ao atualizar pacotes.

## Revisão do acompanhamento — DEC-036, 03/11/2026

Base local: 4dd59b1; alvo: diff documental de STATUS.md, GITHUB.md, REGISTRO.md e este registro. Mesmo agente, sem representar revisão humana/independente. Sem alteração de código ou dependência, portanto testes locais de produto não repetidos.

Issue #8 reaberta e cartão específico do Project #2 em Em revisão, conforme aprovação literal registrada. Histórico anterior preservado na descrição. Primeira reabertura sofreu novo fechamento; segunda reabertura pela CLI permaneceu aberta nas releituras REST/GraphQL. PR #9 aberto, sem merge. git diff --check passou. Não foram alteradas automações para forçar o resultado.

Nenhum achado material no diff documental. Dúvida operacional registrada: sete automações estão ativas, inclusive Auto-close issue, mas a API consultada não revela condições/filtros e a interface disponível não tem login. Não é prova da causa do fechamento. Completar auditoria com leitura do usuário; verificar Issue/cartão novamente antes de integração. Parecer restrito ao alinhamento observado, sem autorizar merge ou afirmar estabilidade futura das automações.

## Revisão C-04 e leitura de auto-add — 03/11/2026

Base local: 4f78f5f; alvo: diff documental de GITHUB.md, STATUS.md, REGISTRO.md e este registro. Revisão do mesmo agente, sem representar revisão humana/independente. Aprovação C-04 literal em DEC-037; desativação realizada pelo usuário. Comparação API por ID confirmou somente Auto-close issue enabled=true → false, seis restantes com IDs/nomes/números/estados iguais, nenhuma adição/remoção. Issue #8 OPEN/cartão Em revisão e PR #9 aberto/sem merge conferidos.

Relato do gatilho Em revisão e de Auto-add game-vault-v2/is:issue is:open distinguidos de leitura direta da API; condições/filtros não expostos não foram comparados. Relato posterior de Item added to project → Em andamento gerou C-05/DEC-038 proposta, sem aplicação: Status inicial Backlog ou alternativa manual para discussão. Registro preserva histórico e não infere aprovação de ajustes adicionais. Nenhum achado material neste diff documental; pendência de configuração explícita. git diff --check passou; sem código/dependência alterados, testes locais da aplicação não repetidos. CI do commit documental deve ser conferida no PR antes do merge manual; auditoria restante do Project permanece explícita.

## Revisão C-05 — 03/11/2026

Base local: 9632adb; alvo: diff documental de GITHUB.md, STATUS.md, REGISTRO.md e este registro. Mesmo agente, sem revisão humana/independente. Aprovação literal e confirmação do usuário em DEC-038: valor inicial Backlog, Item added to project ativa e demais configurações preservadas. Comparação API das sete regras com cópia anterior confirmou IDs/nomes/números/estados enabled idênticos; Auto-close issue continua desativada. Issue #8 OPEN/cartão Em revisão e PR #9 aberto/sem merge conferidos.

Limite explícito: Backlog e condições internas dependem da confirmação do usuário; não foram lidos pela API nem exercitados com item artificial. Nenhum achado material no diff documental examinado; git diff --check passou. Sem código/dependência alterados, testes locais da aplicação não repetidos. CI do commit documental acompanha o PR antes do merge manual. Item closed e demais configurações ainda aguardam leitura; nenhuma mudança adicional inferida.

Complemento após leitura de Item closed: usuário relatou tipos Issue/pull request e destino Em revisão; gerada proposta C-06/DEC-039 para discussão, sem aplicação. Diff adicional sobre 101c8b4 examinado pelo mesmo agente: relato/limites/alternativas preservados e aprovação específica pendente. Nenhum achado material nesse registro documental. Checks documental e build do commit C-05 101c8b4 passaram nas execuções 41729066434/41729066409; novos heads exigem nova conferência no PR.

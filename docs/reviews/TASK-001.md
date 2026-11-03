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

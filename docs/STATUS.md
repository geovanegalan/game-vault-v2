# Ponto de retomada

Atualizado em 03/11/2026 — TASK-001 integrada em develop pelo merge manual do PR #9; Issue #8 fechada/cartões concluídos. Checkpoint #12 e promoção #10 preparados para merges manuais, nessa ordem.

## Autoridade e escopo

- Produto aprovado: VISAO v0.3, PRD/MVP v0.6 e complementos P-01 a P-06 (DEC-023).
- Stack/arquitetura aprovadas: COMPARACAO-STACK v0.1, ADR-001/002 v0.1 (DEC-025/026/027).
- Docker A-02 aprovado e executado (DEC-032); [evidências](ambiente/EVIDENCIAS-DOCKER.md).
- TASK-001 v0.2 aprovada explicitamente em DEC-033: “Aprovo a TASK-001 v0.2, com as versões e o plano propostos. Fiz o merge do PR #7. Pode conferir e começar a implementação com a tutoria.”
- Nenhuma tarefa seguinte, banco, migração, autenticação, funcionalidade de produto ou deploy autorizado por esta entrega. Permanecem o orçamento zero, demonstração local e legado apenas como contexto, sem importar código/dados.

## Implementação da TASK-001

- Feature/task-001-base-tecnica criada do develop remoto após PR #7, b32002a437600354b67aee4e8290b86c8b829b28. Issue de implementação [#8](https://github.com/geovanegalan/game-vault-v2/issues/8).
- Angular em apps/web, NestJS ESM/Express em apps/api, npm workspaces e package-lock.json único. Versões diretas aprovadas conferidas em npm ls; nenhum Git interno ou lockfile concorrente.
- npm run build passou localmente: scripts web/API separados chamados pelo combinado retornaram sucesso. npm ci e novo build local também passaram, comprovando a instalação pelo lockfile nesta máquina. Na implementação 0fba771, [CI documental](https://github.com/geovanegalan/game-vault-v2/actions/runs/41718315560) e [CI de build Linux](https://github.com/geovanegalan/game-vault-v2/actions/runs/41718315696) passaram, incluindo npm ci e build. Resultado do último head e revisão humana acompanham o [PR #9](https://github.com/geovanegalan/game-vault-v2/pull/9).
- Tela inicial renderizou em pt-BR, sem erros de console capturados; Tab/Enter no link de salto focou main#conteudo. Conferência básica de teclado, sem alegar auditoria completa AXE/WCAG.
- API em modo watch respondeu GET / 200 com GameVault API e rota inexistente 404. Servidores limitados a 127.0.0.1; processos próprios encerrados e portas 3000/4200 liberadas.
- PostgreSQL nativo segue Running/Automatic, sem conexão a dados/credenciais ou alteração do serviço. Não foi necessário iniciar Docker para esta base.
- [Guia de execução e tutoria](ambiente/COMO-EXECUTAR.md), [tarefa/evidências](tarefas/TASK-001.md) e [revisão](reviews/TASK-001.md). Base executável inicial, sem jornada do GameVault ou integração web/API.

## Correção da dependência — C-01

O aviso moderado original foi corrigido após aprovação explícita da C-01 (DEC-034): override somente sob @nestjs/cli@12.0.11 para minimatch 11.0.4, preservando versões diretas de frameworks/runtime. Árvore conferida; auditorias completa e sem dev retornaram zero avisos. npm install, npm ci, builds e modo watch/API passaram. Teste de mudança temporária de resposta confirmou recompilação e restauração com SHA-256 original. No commit 1b7b752, [CI documental](https://github.com/geovanegalan/game-vault-v2/actions/runs/41722162580) e [build Linux](https://github.com/geovanegalan/game-vault-v2/actions/runs/41722162403) passaram, incluindo instalação/build. Check-runs reconfirmados na execução da C-02; novos heads devem ter sua própria CI conferida no PR #9. Históricos e limites na revisão.

Scripts de instalação de quatro pacotes nativos transitivos foram bloqueados pelo npm 12; builds/execução passaram sem alterar essa política. Reabrir terminais antigos resolve PATH do Docker; nenhuma edição global de PATH realizada nesta tarefa.

## GitHub e CI

- Recursos operacionais restritos a [game-vault-v2](https://github.com/geovanegalan/game-vault-v2) e [Project pessoal #2](https://github.com/users/geovanegalan/projects/2), DEC-030; sem consultar outros repositórios/organizações da conta.
- PR #9 mesclado manualmente pelo usuário em develop, confirmado via API: 3ee8ebd9b7454057eeae9ed3fc453cc7be7c37f9. Árvore idêntica ao head revisado aaca650; [CI documental](https://github.com/geovanegalan/game-vault-v2/actions/runs/41732949021) e [build Linux](https://github.com/geovanegalan/game-vault-v2/actions/runs/41732949273) do merge passaram, incluindo npm ci/compilação. PRs #2/#4/#5/#6/#7 anteriores também integrados pelo usuário. Main continua em 76df4ff; promoção [#10](https://github.com/geovanegalan/game-vault-v2/pull/10) aberta em rascunho.
- C-02 aprovada/aplicada (DEC-035): main/develop exigem Integridade do kit (sem testes de produto) e Build web e API (base técnica), ambos da origem GitHub Actions/15368 e strict=true. Todas as demais seções de proteção comparadas e preservadas; auto-merge=false. Workflow de build usa Node 24.21.0, npm 12.0.2, npm ci e build. Nenhum deploy, merge ou ampliação de acesso; detalhes em GITHUB.md.
- Issue #8 fechada como completed após conferir integração e autorização DEC-041; cartões Issue #8/PR #9 em Concluída. Cartão do PR #9 já estava Concluída após merge, evidência observada da C-07 sem nova mudança pelo agente. Project #2 mantém duas views/sete regras: Auto-close issue e Item closed desativadas, outras cinco ativas. Valores/limites em GITHUB.md; operações restritas ao destino explícito.
- Todo merge continua manual pelo usuário. Nunca executar merge/auto-merge, force-push ou push direto em main/develop. Autoria local Geovane/no-reply; Git global preservado.

## Próxima ação

1. Próxima ação manual: revisar/mesclar checkpoint [#12](https://github.com/geovanegalan/game-vault-v2/pull/12), codex/docs-integracao-task-001 → develop. Depois agente confere integração e novos checks da promoção [#10](https://github.com/geovanegalan/game-vault-v2/pull/10), develop → main, antes de prepará-la para revisão/merge manual do usuário. #10 permanece em rascunho até integrar o checkpoint; nenhum merge pelo agente.
2. Reavaliação: #10 inicialmente reportou behind, mas reconsultas após os checks passarem mostraram clean com as mesmas bases e strict=true. A sincronização extra #11 foi fechada sem merge e seu cartão arquivado, pois não se mostrou necessária. Preservar essa evidência, sem tratar divergência de histórico sozinha como bloqueio permanente ou reduzir proteções. Relatório em reviews/PROMOCAO-TASK-001.md. C-01/C-02 e auditoria disponível do Project encerradas com limites explícitos.
3. Após essa entrega, propor TASK-002 em versão concreta para modelagem/banco/dados fictícios, com sua aprovação antes de implementar. Provedor real do catálogo e parâmetros de senha/sessão permanecem para tarefas próprias.
4. Continuar tutoria a partir dos arquivos reais e do guia. Experiência informada: TypeScript/Node/SQL intermediário/avançado, Express intermediário, Angular/Nest iniciante, Git básico e testes prévios com Jest.

## Fila de pendências — tratar uma a uma

Usuário pediu listar/explicar causas e resolver em sequência, em 03/11/2026. C-01 foi aprovada em DEC-034 e validada localmente/CI. C-02 foi aprovada em DEC-035 e aplicada: ambas as bases exigem os dois checks, preservando as demais proteções. DEC-036 autorizou reabrir Issue #8 e cartão Em revisão até merge manual. Estados reconferidos pela API; condições das automações são o próximo item.

| Ordem | Item e causa observada | Próxima ação / limite |
| --- | --- | --- |
| 1 | Aviso moderado original na dependência da CLI | Resolvida por C-01: override restrito 11.0.4, auditorias zero, testes locais e CI do commit 1b7b752 passaram |
| 2 | Build era informativo: exigência foi separada da criação do job para não mudar proteções sem revisão | Resolvida por C-02 aprovada/aplicada: dois checks GitHub Actions/15368 e strict=true em main/develop; demais seções idênticas antes/depois |
| 3 | Issue #8 havia sido fechada antes da integração | Reaberta sob DEC-036; depois do merge manual confirmado do PR #9 e autorização DEC-041, fechada como completed e cartão Concluída. Histórico do fechamento anterior preservado |
| 4 | Project tinha views/automações não atestadas; fechamento/Status inicial prematuros e itens fechados/mesclados em revisão identificados na leitura do usuário | Leituras disponíveis encerradas: C-04/C-06 desativadas pela interface e conferidas pela API; C-05/C-07 valores confirmados pelo usuário. Default repository correto relatado; views e sete identidades/ativação conferidas. Condições internas dependem da leitura do usuário; alvo da regra de vínculo não explícito e nenhuma automação exercitada artificialmente. Tabela/limites em GITHUB.md |
| 5 | Integração da TASK-001 em develop | Resolvida: merge manual #9 confirmado em 3ee8ebd, árvore revisada preservada e dois checks do merge passaram |
| 6 | main mantém promoção documental antiga | Checkpoint #12 → develop, depois conferir novos checks e preparar promoção #10 → main para merge manual. #11 fechado sem merge após GitHub reavaliar #10 como clean com strict=true. Nenhuma integração executada pelo agente |

Avisos de install scripts bloqueados pelo npm 12 não são falha pendente: a política padrão restringiu quatro scripts transitivos e instalação/builds/execução passaram assim. Manter o comportamento atual; não liberar scripts para apenas eliminar a mensagem. Python opcional ausente e Docker sem status naquela consulta também não são bloqueios da base Node já validada.

Decisões das fases seguintes continuam pendentes no contexto adequado: modelo/banco/dados fictícios (TASK-002), política de senha/sessão na autenticação e provedor/termos do catálogo real opcional. Essas escolhas serão apresentadas nas tarefas próprias; resolver esta fila não autoriza implementar o restante do MVP.

Histórico da pausa de 01/11 e retomada de 03/11 preservado nos commits 0bd1ad2/4741f89 e PR #7. Ao retomar em outro chat, ler AGENTS.md, 00-contexto.md, este STATUS e decisoes/REGISTRO.md; conferir Git antes de editar e preservar mudanças do usuário. Commits públicos iniciais não foram reescritos; a minimização posterior de detalhes do host não apaga seu histórico.

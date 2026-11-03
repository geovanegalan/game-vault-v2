# Ponto de retomada

Atualizado em 03/11/2026 — TASK-001 v0.2 aprovada, implementada e verificada localmente/CI; revisão humana e pendência de desenvolvimento explícitas no PR #9.

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

O aviso moderado original foi corrigido após aprovação explícita da C-01 (DEC-034): override somente sob @nestjs/cli@12.0.11 para minimatch 11.0.4, preservando versões diretas de frameworks/runtime. Árvore conferida; auditorias completa e sem dev retornaram zero avisos. npm install, npm ci, builds e modo watch/API passaram. Teste de mudança temporária de resposta confirmou recompilação e restauração com SHA-256 original. A CI do commit de correção será conferida/registrada no PR #9; não inferir sucesso antes da execução externa. Históricos e limites na revisão.

Scripts de instalação de quatro pacotes nativos transitivos foram bloqueados pelo npm 12; builds/execução passaram sem alterar essa política. Reabrir terminais antigos resolve PATH do Docker; nenhuma edição global de PATH realizada nesta tarefa.

## GitHub e CI

- Recursos operacionais restritos a [game-vault-v2](https://github.com/geovanegalan/game-vault-v2) e [Project pessoal #2](https://github.com/users/geovanegalan/projects/2), DEC-030; sem consultar outros repositórios/organizações da conta.
- PR #7 de planejamento mesclado manualmente pelo usuário em develop, confirmado via API. PRs #2/#4/#5/#6 anteriores também integrados pelo usuário. Main permanece na promoção documental anterior; evidências Docker, checkpoint e aplicação desta feature ainda precisam de promoção quando oportuno.
- Check documental Integridade do kit (sem testes de produto) e proteções main/develop preservados. Novo workflow Build web e API (base técnica) usa Node 24.21.0, npm 12.0.2, npm ci e build; nenhum deploy ou mudança de permissões. Tornar esse check obrigatório será proposta separada.
- Issues #1/#3 fechadas; Issue #8 acompanha implementação, evidências e revisão/merge manuais. Configurações de interface do Project não atestadas: repositório padrão para criar Issues, views e automações; operações usam destino explícito.
- Todo merge continua manual pelo usuário. Nunca executar merge/auto-merge, force-push ou push direto em main/develop. Autoria local Geovane/no-reply; Git global preservado.

## Próxima ação

1. Conferir CI da correção C-01 e o último head do PR #9 antes da revisão/merge manual. Reconciliar depois o acompanhamento: Issue #8 consta fechada enquanto PR segue aberto, conforme fila abaixo; não atribuir fechamento a uma origem não comprovada.
2. Próxima pendência: C-02 proposta em GITHUB.md/DEC-035 para tornar também o build obrigatório em main/develop. Somente levantamento/proposta preparados; aguardar aprovação específica antes de alterar proteção.
3. Após essa entrega, propor TASK-002 em versão concreta para modelagem/banco/dados fictícios, com sua aprovação antes de implementar. Provedor real do catálogo e parâmetros de senha/sessão permanecem para tarefas próprias.
4. Continuar tutoria a partir dos arquivos reais e do guia. Experiência informada: TypeScript/Node/SQL intermediário/avançado, Express intermediário, Angular/Nest iniciante, Git básico e testes prévios com Jest.

## Fila de pendências — tratar uma a uma

Usuário pediu listar/explicar causas e resolver em sequência, em 03/11/2026. C-01 foi depois aprovada em DEC-034 e executada com verificação local; CI da correção acompanha o PR. Reconsulta confirmou PR #9 aberto, Issue #8 fechada e somente o check documental exigido em main/develop. Nenhuma alteração de proteção/permissão executada.

| Ordem | Item e causa observada | Próxima ação / limite |
| --- | --- | --- |
| 1 | Aviso moderado original na dependência da CLI | C-01 aprovada/aplicada: override restrito 11.0.4, auditorias zero e testes locais passaram; conferir CI da correção no PR #9 |
| 2 | Novo build passa, mas não é obrigatório: exigência foi separada da criação do job para não mudar proteções sem revisão | C-02 concreta em GITHUB.md/DEC-035: acrescentar build da origem GitHub Actions/15368 às exigências de main/develop, preservando regras; aprovação específica antes de aplicar |
| 3 | Issue #8 fechada enquanto PR #9 segue aberto: estado do acompanhamento foi encerrado antes da integração | Histórico mostra evento closed pela conta geovanegalan, sem app informado; isso não distingue clique humano de ferramenta autenticada nessa conta. Alinhar Issue/cartão/STATUS com integração pendente, sem atribuir origem não comprovada |
| 4 | Project tem repositório padrão de criação, views e automações não atestados pela configuração anterior | Conferir somente Project pessoal #2 e GameVault; registrar configurado/ausente/não acessível. Propor somente ajustes necessários; não ativar automações por inferência |
| 5 | PR #9 ainda aberto: revisão/merge são exclusivamente do usuário | Após correção/avaliação e CI, usuário executa integração em develop; agente nunca mergeia |
| 6 | main mantém a promoção documental antiga; entregas seguintes estão em develop/feature | Após integração da tarefa, preparar PR develop → main e validações para merge manual do usuário |

Avisos de install scripts bloqueados pelo npm 12 não são falha pendente: a política padrão restringiu quatro scripts transitivos e instalação/builds/execução passaram assim. Manter o comportamento atual; não liberar scripts para apenas eliminar a mensagem. Python opcional ausente e Docker sem status naquela consulta também não são bloqueios da base Node já validada.

Decisões das fases seguintes continuam pendentes no contexto adequado: modelo/banco/dados fictícios (TASK-002), política de senha/sessão na autenticação e provedor/termos do catálogo real opcional. Essas escolhas serão apresentadas nas tarefas próprias; resolver esta fila não autoriza implementar o restante do MVP.

Histórico da pausa de 01/11 e retomada de 03/11 preservado nos commits 0bd1ad2/4741f89 e PR #7. Ao retomar em outro chat, ler AGENTS.md, 00-contexto.md, este STATUS e decisoes/REGISTRO.md; conferir Git antes de editar e preservar mudanças do usuário. Commits públicos iniciais não foram reescritos; a minimização posterior de detalhes do host não apaga seu histórico.

# Ponto de retomada

Atualizado em 03/11/2026 — TASK-001 v0.2 aprovada, implementada e verificada localmente; CI e revisão humana acompanhadas na entrega.

## Autoridade e escopo

- Produto aprovado: VISAO v0.3, PRD/MVP v0.6 e complementos P-01 a P-06 (DEC-023).
- Stack/arquitetura aprovadas: COMPARACAO-STACK v0.1, ADR-001/002 v0.1 (DEC-025/026/027).
- Docker A-02 aprovado e executado (DEC-032); [evidências](ambiente/EVIDENCIAS-DOCKER.md).
- TASK-001 v0.2 aprovada explicitamente em DEC-033: “Aprovo a TASK-001 v0.2, com as versões e o plano propostos. Fiz o merge do PR #7. Pode conferir e começar a implementação com a tutoria.”
- Nenhuma tarefa seguinte, banco, migração, autenticação, funcionalidade de produto ou deploy autorizado por esta entrega. Permanecem o orçamento zero, demonstração local e legado apenas como contexto, sem importar código/dados.

## Implementação da TASK-001

- Feature/task-001-base-tecnica criada do develop remoto após PR #7, b32002a437600354b67aee4e8290b86c8b829b28. Issue de implementação [#8](https://github.com/geovanegalan/game-vault-v2/issues/8).
- Angular em apps/web, NestJS ESM/Express em apps/api, npm workspaces e package-lock.json único. Versões diretas aprovadas conferidas em npm ls; nenhum Git interno ou lockfile concorrente.
- npm run build passou localmente: scripts web/API separados chamados pelo combinado retornaram sucesso. npm ci e novo build local também passaram, comprovando a instalação pelo lockfile nesta máquina. CI real do PR e seu resultado externo serão registrados no PR/Issue, sem simular execução.
- Tela inicial renderizou em pt-BR, sem erros de console capturados; Tab/Enter no link de salto focou main#conteudo. Conferência básica de teclado, sem alegar auditoria completa AXE/WCAG.
- API em modo watch respondeu GET / 200 com GameVault API e rota inexistente 404. Servidores limitados a 127.0.0.1; processos próprios encerrados e portas 3000/4200 liberadas.
- PostgreSQL nativo segue Running/Automatic, sem conexão a dados/credenciais ou alteração do serviço. Não foi necessário iniciar Docker para esta base.
- [Guia de execução e tutoria](ambiente/COMO-EXECUTAR.md), [tarefa/evidências](tarefas/TASK-001.md) e [revisão](reviews/TASK-001.md). Base executável inicial, sem jornada do GameVault ou integração web/API.

## Pendência real de dependência

npm audit reportou aviso moderado de minimatch transitivo da CLI Nest, com duas entradas na mesma cadeia; npm audit --omit=dev retornou zero avisos. Correção sugerida pelo npm muda CLI para major 11, contrariando a matriz aprovada. Não executados fix --force, overrides ou alterações de versão. Cenário/limites e alternativas na revisão; decisão de correção permanece com o usuário, sem aceite de risco inferido.

Scripts de instalação de quatro pacotes nativos transitivos foram bloqueados pelo npm 12; builds/execução passaram sem alterar essa política. Reabrir terminais antigos resolve PATH do Docker; nenhuma edição global de PATH realizada nesta tarefa.

## GitHub e CI

- Recursos operacionais restritos a [game-vault-v2](https://github.com/geovanegalan/game-vault-v2) e [Project pessoal #2](https://github.com/users/geovanegalan/projects/2), DEC-030; sem consultar outros repositórios/organizações da conta.
- PR #7 de planejamento mesclado manualmente pelo usuário em develop, confirmado via API. PRs #2/#4/#5/#6 anteriores também integrados pelo usuário. Main permanece na promoção documental anterior; evidências Docker, checkpoint e aplicação desta feature ainda precisam de promoção quando oportuno.
- Check documental Integridade do kit (sem testes de produto) e proteções main/develop preservados. Novo workflow Build web e API (base técnica) usa Node 24.21.0, npm 12.0.2, npm ci e build; nenhum deploy ou mudança de permissões. Tornar esse check obrigatório será proposta separada.
- Issues #1/#3 fechadas; Issue #8 acompanha implementação, evidências e revisão/merge manuais. Configurações de interface do Project não atestadas: repositório padrão para criar Issues, views e automações; operações usam destino explícito.
- Todo merge continua manual pelo usuário. Nunca executar merge/auto-merge, force-push ou push direto em main/develop. Autoria local Geovane/no-reply; Git global preservado.

## Próxima ação

1. Conferir CI e o PR da TASK-001; usuário revisar a implementação e a pendência de desenvolvimento antes do merge manual para develop. Manter Issue #8 aberta até integração.
2. Discutir correção compatível do aviso de tooling, sem mudar a matriz por conveniência. Nenhuma autorização para corrigir por downgrade major/override inferida.
3. Após essa entrega, propor TASK-002 em versão concreta para modelagem/banco/dados fictícios, com sua aprovação antes de implementar. Provedor real do catálogo e parâmetros de senha/sessão permanecem para tarefas próprias.
4. Continuar tutoria a partir dos arquivos reais e do guia. Experiência informada: TypeScript/Node/SQL intermediário/avançado, Express intermediário, Angular/Nest iniciante, Git básico e testes prévios com Jest.

Histórico da pausa de 01/11 e retomada de 03/11 preservado nos commits 0bd1ad2/4741f89 e PR #7. Ao retomar em outro chat, ler AGENTS.md, 00-contexto.md, este STATUS e decisoes/REGISTRO.md; conferir Git antes de editar e preservar mudanças do usuário. Commits públicos iniciais não foram reescritos; a minimização posterior de detalhes do host não apaga seu histórico.

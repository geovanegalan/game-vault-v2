# GameVault 2.0

Biblioteca de jogos e comunidade baseada em avaliações públicas e amizades. Projeto de portfólio desenvolvido do zero com **Spec-Driven Development**: especificar o comportamento, revisar decisões, implementar tarefas autorizadas e registrar evidências.

> **Estado atual:** produto, stack e arquitetura aprovados; primeiro commit documental publicado, main/develop protegidas e CI documental passou. Project criado manualmente; instalação Docker pendente. Ainda não existe aplicação para executar. Consulte [STATUS](docs/STATUS.md).

## Produto planejado

- Biblioteca pública com estados quero jogar, jogando, pausado, concluído e abandonado; favorito independente.
- Avaliações de 0 a 5 estrelas, incluindo meias estrelas, texto opcional e comentários.
- Perfil público com nickname único que diferencia maiúsculas/minúsculas; cadastro/login por email e senha.
- Solicitações de amizade e feed cronológico com novas avaliações dos amigos e conteúdo editorial de exemplo.
- Demonstração local com dados fictícios e sem chave; busca real de jogos por API configurável como opção.

O objetivo é experimentar localmente sem hospedagem paga. Instalações locais não compartilham comunidade entre computadores. Upload de screenshots, chats/grupos e fluxos de recuperação/confirmação de email ficam fora da primeira entrega. O projeto anterior serve somente de contexto; código e banco não serão importados.

## Especificações e decisões

| Documento | O que contém | Estado |
| --- | --- | --- |
| [Visão v0.3](docs/VISAO.md) | Público, valor, aprendizado e limites | Aprovada — DEC-023 |
| [PRD v0.6](docs/PRD.md) | Requisitos, regras e critérios de aceitação | Aprovado — DEC-023, incluindo P-01 a P-06 |
| [MVP v0.6](docs/MVP.md) | Fronteira e verificação da primeira entrega | Aprovado — DEC-023 |
| [Registro de decisões](docs/decisoes/REGISTRO.md) | Aprovações e evidências; propostas distintas de decisões | Fonte de autoridade |
| [Status](docs/STATUS.md) | Ponto de retomada, verificações e pendências | Atualizado por etapa |

## Planejamento técnico

| Documento | Finalidade |
| --- | --- |
| [Comparação de stack](docs/COMPARACAO-STACK.md) | Escolha aprovada em DEC-025 e alternativas consideradas |
| [ADR-001: arquitetura](docs/arquitetura/ADR-001.md) | Organização, limites, dados e execução local — aprovado em DEC-026 |
| [ADR-002: autenticação](docs/arquitetura/ADR-002.md) | Estratégia de sessões/cookies — aprovada em DEC-027 |
| [Backlog inicial](docs/planejamento/BACKLOG.md) | Resultados pequenos, dependências e validação por tarefa |
| [TASK-001 proposta](docs/tarefas/TASK-001.md) | Primeira base técnica após documentação/ambiente aprovados |
| [Comparação de catálogo](docs/catalogo/COMPARACAO.md) | API real opcional; nenhum provedor escolhido |

A stack aprovada é TypeScript/Angular, NestJS modular, PostgreSQL/Prisma, npm workspaces e Compose, com testes progressivos Vitest/integração/Playwright. Linhas Angular 22, NestJS 12, Prisma 7 e PostgreSQL 18; versões exatas de dependências locais serão fixadas antes da tarefa de aplicação. ADR significa registro de decisão de arquitetura; aprovar a estratégia não equivale a executar instalações ou código.

## Como experimentar

A aplicação ainda não foi criada. Não há comando de execução, conta de demonstração ou integração real disponível neste estágio.

A entrega prevista terá um comando para iniciar após pré-requisitos documentados, dados fictícios persistentes e API opcional. Os comandos reais serão registrados depois de criados e verificados; não instale dependências a partir de exemplos históricos.

## Desenvolvimento e GitHub

Destino: [geovanegalan/game-vault-v2](https://github.com/geovanegalan/game-vault-v2), público. [Primeiro commit 263c7bb](https://github.com/geovanegalan/game-vault-v2/commit/263c7bbe4578504d1f9c6b7f6fbad560a333d70e), exclusivamente documental. main/develop protegidas com PR obrigatório e verificação documental, sem força/exclusão. [Project pessoal GameVault 2.0](https://github.com/users/geovanegalan/projects/2), criado manualmente, sem ampliar escopo da CLI. [Evidências reais](docs/ambiente/EVIDENCIAS-BOOTSTRAP.md).

Fluxo previsto, sem merges automáticos:

```text
feature/<tarefa> → pull request → develop
develop         → pull request → main
```

Todo merge será feito manualmente pelo usuário. O primeiro commit será exclusivamente documental, antes de código, conforme DEC-024. Bootstrap e configuração remota seguem o [plano GitHub](docs/ambiente/PLANO-GITHUB.md), com identidade e alcance confirmados antes de alterações.

## Ambiente e verificações

- [Diagnóstico](docs/ambiente/DIAGNOSTICO.md): ferramentas observadas e limites das verificações.
- [Preparação assistida](docs/AMBIENTE.md): regras para propor e executar instalações autorizadas.
- [Plano de ambiente](docs/ambiente/PLANO-AMBIENTE.md): ferramentas existentes, única instalação proposta e verificações.
- [Fluxo GitHub](docs/GITHUB.md): PRs, proteções, Issues, Project e Actions.
- [Organização documental](docs/ORGANIZACAO-DOCUMENTAL.md): arquivos úteis, referências e revisão de limpeza.

O workflow existente valida somente a integridade documental. Não há build/teste de produto ou deploy configurado. O verificador local Python é opcional; o comando Python encontrado falhou ao iniciar no diagnóstico. Nenhuma verificação documental comprova funcionamento da futura aplicação.

## Histórico e recursos do processo

- [Entrevista](docs/entrevista/SESSOES.md) e [contexto inicial](docs/00-contexto.md): origem das propostas; aprovações posteriores prevalecem sobre o estado inicial.
- [Fontes](docs/FONTES.md): documentação consultada, datas e limites.
- [Modelos](docs/modelos/): recursos para ADR, tarefa, revisão e preparação; não são especificações de produto vigentes.
- [AGENTS.md](AGENTS.md) e [.agents/skills](.agents/skills/): contrato de colaboração e cinco skills locais.

Próxima etapa: revisar/mesclar manualmente a evidência documental por PR, aprovar/executar A-02 do plano de ambiente e preparar a primeira tarefa de aplicação com tutoria e evidências reais. Nenhum código começou antes do primeiro commit.

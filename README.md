# GameVault 2.0

Biblioteca pessoal de jogos e comunidade para avaliar, fazer amigos e trocar experiências. Reescrita do zero de um projeto acadêmico, desenvolvida com **Spec-Driven Development**: definir o comportamento, aprovar decisões e implementar em tarefas verificáveis.

> **Em planejamento.** Produto, stack e arquitetura aprovados; primeiro commit documental publicado. A aplicação ainda não existe. Veja o [estado atual e as pendências](docs/STATUS.md).

## O que está planejado

- Biblioteca pública com estados de progresso e favoritos independentes.
- Avaliações públicas de 0 a 5 estrelas, com meias estrelas, texto opcional e comentários.
- Perfis públicos, cadastro/login e solicitações de amizade.
- Feed cronológico com novas avaliações dos amigos e conteúdo editorial de demonstração.
- Demonstração local com jogos fictícios, sem chave; integração opcional com API de jogos reais.

O foco é portfólio e aprendizado, sem hospedagem paga. Cada instalação terá seus próprios dados. Screenshots enviadas por usuários, chats, grupos e recuperação/confirmação de email ficam fora da primeira entrega. O legado serve apenas de contexto; código e banco não serão importados.

## Especificações

| Documento | Conteúdo | Estado |
| --- | --- | --- |
| [Visão](docs/VISAO.md) | Público, valor e objetivos de aprendizado | v0.3 aprovada |
| [PRD](docs/PRD.md) | Requisitos, regras e critérios de aceitação | v0.6 aprovado |
| [MVP](docs/MVP.md) | Fronteira da primeira entrega | v0.6 aprovado |
| [Decisões](docs/decisoes/REGISTRO.md) | Aprovações, evidências e propostas pendentes | Fonte de autoridade |

## Stack e arquitetura

| Área | Escolha aprovada |
| --- | --- |
| Linguagem e execução | TypeScript e Node.js 24 |
| Interface | Angular |
| API | NestJS, com módulos em uma aplicação |
| Dados | PostgreSQL e Prisma |
| Organização e execução local | npm workspaces e Docker Compose |
| Testes planejados | Vitest, integração e Playwright |

A [comparação de stack](docs/COMPARACAO-STACK.md) registra alternativas e consequências. Os registros [ADR-001: arquitetura](docs/arquitetura/ADR-001.md) e [ADR-002: autenticação](docs/arquitetura/ADR-002.md) detalham as escolhas. Dependências locais serão fixadas na tarefa correspondente; aprovar a stack não autoriza todas as instalações ou tarefas.

## Como experimentar

Ainda não há comando de execução nem contas de demonstração disponíveis. A entrega planejada permitirá iniciar localmente após preparar os pré-requisitos, com dados fictícios persistentes. Os comandos serão publicados depois de implementados e verificados.

O [diagnóstico](docs/ambiente/DIAGNOSTICO.md) registra as ferramentas existentes. O [plano de ambiente](docs/ambiente/PLANO-AMBIENTE.md) aguarda aprovação da instalação do Docker; não é necessário atualizar Node neste momento.

## Desenvolvimento

O trabalho é acompanhado no [Project GameVault 2.0](https://github.com/users/geovanegalan/projects/2) e segue este fluxo:

```text
feature/<tarefa> → pull request → develop
develop         → pull request → main
```

`main` e `develop` exigem PR e verificação documental. Todos os merges são feitos manualmente pelo responsável pelo projeto. A automação atual verifica documentação e skills; ainda não há build, testes de aplicação ou deploy. Consulte o [guia GitHub](docs/GITHUB.md).

- [Backlog](docs/planejamento/BACKLOG.md) e [TASK-001](docs/tarefas/TASK-001.md): planejamento, ainda sem autorização de código.
- [Comparação de catálogo](docs/catalogo/COMPARACAO.md): provedor real ainda não escolhido.
- [Preparação assistida do ambiente](docs/AMBIENTE.md): diagnóstico e instalações autorizadas.
- [Fontes consultadas](docs/FONTES.md): documentação e limites das verificações.

## Histórico e colaboração

O [contexto inicial](docs/00-contexto.md), a [entrevista](docs/entrevista/SESSOES.md) e as [evidências do bootstrap](docs/ambiente/EVIDENCIAS-BOOTSTRAP.md) preservam a origem das decisões. O [primeiro commit](https://github.com/geovanegalan/game-vault-v2/commit/263c7bbe4578504d1f9c6b7f6fbad560a333d70e) foi exclusivamente documental, antes de qualquer aplicação.

[AGENTS.md](AGENTS.md) e as [skills locais](.agents/skills/) orientam a tutoria, as aprovações e as revisões. Documentos reais substituem modelos vazios; decisões aprovadas continuam versionadas e rastreáveis.

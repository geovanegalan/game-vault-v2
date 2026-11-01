# Comparação de stack do GameVault 2.0
Versão: 0.1 | Data: 01/11/2026 | Estado: aprovada pelo usuário — DEC-025
Base aprovada: DEC-023 — VISAO v0.3, PRD v0.6 e MVP v0.6.

## Contexto da escolha
Fatos informados: TypeScript/Node.js/SQL intermediário a avançado; Express intermediário; Angular/NestJS iniciante; Git/GitHub básico; já escreveu testes unitários com Jest e quer tutoria em testes. Disponibilidade estimada: 2–3 horas nos fins de semana, sem prazo. Orçamento zero e demonstração local; não reutilizar código/banco do legado.

Fatos do diagnóstico: Windows/PowerShell; Git, Node 24.21.0, npm 12.0.2 e GitHub CLI executáveis; Docker não encontrado no PATH; Python encontrado falhou ao iniciar. Instalações fora do PATH, WSL, virtualização, memória disponível e banco existente não foram inventariados. Ferramenta instalada não equivale a escolha adequada.

A recomendação abaixo prioriza aprendizado e uma entrega completa com poucas peças operacionais. Prós/contras são avaliação contextual; as capacidades e requisitos publicados estão nas fontes. Nenhuma dependência foi instalada para elaborar a comparação.

## Opções adequadas
| Área | Recomendação proposta | Prós para este projeto | Contras e alternativa pertinente |
| --- | --- | --- | --- |
| Linguagem/runtime | TypeScript e Node 24 já disponível | Aproveita experiência e mantém a mesma linguagem nas duas aplicações | Tipos não substituem validação de entrada. JavaScript reduziria configuração, mas perderia parte do aprendizado pretendido; não há motivo comprovado para atualizar Node agora |
| Frontend | Angular, componentes standalone, aplicação no navegador (SPA) | Direção desejada; organização, formulários e rotas no mesmo ecossistema; tutoria desde uma primeira tela pequena | Curva inicial em Angular. Adiar Angular e fazer interface provisória reduz aprendizado simultâneo, mas duplica parte do trabalho; React é viável, porém troca a direção de aprendizado por outra também nova |
| Momento do frontend | Primeira jornada com interface e API juntas, após base técnica mínima | Resultado visível cedo; aprende comunicação entre tela e servidor em contexto | Exige alternar temas. Alternativa: backend completo antes das telas; reduz troca inicial, mas atrasa validação do fluxo real |
| Backend | NestJS em uma API modular | Convenções de módulos/serviços e injeção de dependências ajudam organizar regras e testes; combina com objetivo de aprender Nest | Mais conceitos e arquivos no início. Express 5 aproveita familiaridade e começa menor, mas exige definir manualmente a organização e padronização |
| Banco | PostgreSQL local, mesmo motor nos testes de integração | Relações, unicidade, transações e prática de SQL; mesmo comportamento entre demonstração e validação | Precisa de processo de banco. SQLite é a alternativa mais leve para distribuição local, mas tem outra operação/concorrência e exigiria decidir o motor que representa o produto. Não se propõe PostgreSQL num modo e SQLite no outro |
| Acesso a dados | Prisma ORM 7 estável | Tipagem das consultas e migrações versionadas; deixa regras de negócio nos serviços e permite revisar o SQL gerado | Mais ferramenta e adaptação ao modelo do ORM. SQL com node-postgres dá controle e aprofunda SQL, mas exige mais código de consulta/mapeamento e estratégia de migrações própria |
| Pacotes/estrutura | npm workspaces; um repositório com apps/web e apps/api; um lockfile raiz | npm já disponível; um clone/PR abrange jornada inteira; um arquivo registra resoluções de dependências | Instalações e CI devem respeitar os workspaces. Repositórios separados isolam projetos, mas exigem coordenar versões, PRs e documentação. pnpm é alternativa válida, sem necessidade demonstrada de adicioná-lo agora |
| Interface visual | HTML semântico e estilos locais inicialmente; biblioteca de componentes a decidir no desenho das telas | Permite desenhar a identidade sem assumir Bootstrap do legado ou outro kit | Exige cuidado com acessibilidade. Angular Material pode reduzir trabalho de componentes, mas influencia visual e dependências; não incluído nesta proposta como escolha automática |
| Execução de demonstração | Docker Compose com web/API/PostgreSQL e volume persistente | É o melhor ajuste proposto para iniciar o conjunto com um comando após preparo, sem banco hospedado | Instalação de Docker/WSL, consumo de recursos e primeiro download. Alternativa: Node/npm + PostgreSQL nativos, menos virtualização, mais preparação manual e dependência da máquina |
| Desenvolvimento | Node/npm locais com banco em Compose, além da execução completa por Compose | Depuração e atualização de tela rápidas; mesmo banco da demonstração | Dois perfis documentados. Desenvolver tudo em contêineres uniformiza ambiente, mas pode complicar observação de arquivos e depuração no Windows; avaliar recursos antes de adotar |
| Testes | Vitest para unidades/componentes, integração de API com banco isolado e poucos fluxos Playwright no navegador | Aproveita conceitos de Jest; cobre regras e autorização sem depender só de cliques manuais | Aprendizado e preparação de banco/navegador. Jest continua alternativa, mas os guias atuais de Angular/Nest apresentam Vitest; não se adicionam dois runners de unidade por hábito |

ORM significa ferramenta que mapeia operações do código para o banco. Migração é uma alteração versionada do esquema; não é importar o banco antigo. Workspace é a organização de pacotes dentro de um projeto raiz, não um serviço pago. Compose coordena processos isolados em contêineres; não oferece hospedagem.

## Compatibilidade consultada — documental, ainda sem experimento de integração
Fontes oficiais acessadas em 01/11/2026; linhas candidatas, não versões já instaladas ou autorizadas.

| Item | Evidência publicada | Proposta e limite |
| --- | --- | --- |
| Angular 22 | Tabela exige Node ^22.22.3, ^24.15.0 ou ^26 e TypeScript >=6.0 <6.1; linha 22 está em suporte ativo | Node 24.21.0 observado atende ao intervalo; propor Angular 22 e TypeScript 6.0.x. Minor/patch e resolução conjunta serão fixados antes da instalação, sem usar latest indiscriminadamente |
| NestJS 12 | Guia atual descreve ESM, schematics com TypeScript 6 e geradores com Node 24.15+ na linha 24 | Candidato coerente com Node observado/TypeScript 6; validar geradores, pacote estável e dependências na preparação. Não copiar receitas antigas de CommonJS/Jest sem conferir |
| Prisma 7 | Requisitos incluem Node ^24.0.0 e TypeScript 5.4+; matriz inclui PostgreSQL 18 | Node observado atende; propor Prisma 7 e PostgreSQL 18, com adaptação de driver e ESM conforme guia versionado. Compatibilidade publicada não substitui build/teste conjunto com TypeScript 6 |
| Prisma 8 | Quickstart atual o identifica como release candidate e mantém versão 7 suportada | Não recomendar a versão candidata para este projeto; usar documentação explicitamente da versão 7 |
| PostgreSQL 18 | Política oficial lista suporte de versões e atualizações menores | Linha 18 candidata; patch/imagem serão fixados no plano de ambiente, após verificar disponibilidade e segurança. Sem banco novo criado nesta etapa |
| npm 12.0.2 | Executou no diagnóstico; documentação atual descreve workspaces | Manter como candidato sem atualização; validar lockfile/build após autorização. Nenhum lockfile de aplicação criado |

Fontes: [Angular: compatibilidade](https://angular.dev/reference/versions), [ciclo de suporte](https://angular.dev/reference/releases), [Nest: migração atual](https://docs.nestjs.com/migration-guide), [Prisma 7: requisitos](https://www.prisma.io/docs/orm/v7/reference/system-requirements), [bancos suportados](https://www.prisma.io/docs/orm/v7/reference/supported-databases), [estado do quickstart Prisma](https://www.prisma.io/docs/prisma-orm/quickstart/postgresql), [PostgreSQL: versões](https://www.postgresql.org/support/versioning/).

## Arquitetura recomendada e concessões
Propor um monólito modular: uma API executável, separada em áreas de negócio, e uma aplicação Angular. Manter banco local e integração externa atrás da API. Não usar microsserviços, filas, Redis, cluster ou hospedagem para atender a esta fronteira; seriam outras decisões com operação adicional.

O contraste principal é de objetivo: Express + SQLite reduziria a preparação, mas sacrificaria parte da prática de Nest/PostgreSQL. A recomendação Angular + Nest + PostgreSQL/Prisma + Compose exige mais aprendizado inicial, porém corresponde às direções desejadas e permite exercitar o fluxo completo de desenvolvimento. Com pouco tempo semanal, dividir em tarefas pequenas e manter uma única jornada por vez, sem afirmar prazo de entrega.

Detalhamento e alternativas em `arquitetura/ADR-001.md` v0.1. Autenticação em `arquitetura/ADR-002.md` v0.1. A aprovação de uma dessas propostas deve indicar seu alcance; não é inferida de DEC-023.

## Estratégia de testes proposta
- Unitários: nota/incrementos, condição de biblioteca, permissões e transições de amizade. Explicar o paralelo entre describe/it/expect, isolamento e mocks de Jest/Vitest.
- Integração: API e PostgreSQL de teste separado; validar nickname com capitalização, email normalizado, unicidade e exclusão de comentários sem excluir avaliação ao remover biblioteca.
- Navegador: cadastro/login, biblioteca/avaliação e amizade/feed; poucos fluxos essenciais com Playwright. Acesso real ao provedor não roda em todo PR com credenciais pessoais.
- CI: começar com verificação documental; depois adicionar build, análise estática e testes reais quando os comandos existirem. Nenhum job de deploy; merges manuais.

Fontes: [Angular: testes](https://angular.dev/guide/testing), [Nest: testes](https://docs.nestjs.com/fundamentals/testing), [Playwright](https://playwright.dev/docs/intro). Experiência em Jest foi informada; resultado de qualquer teste desta stack ainda não existe.

## Custos, preparação e verificações pendentes
- Nenhuma dependência de serviço pago na proposta. Uso pessoal/educacional do Docker Desktop é contemplado na oferta gratuita publicada; verificar condições aplicáveis antes de instalar. Isso não equivale a licença irrestrita de uso empresarial.
- Docker não encontrado no PATH: antes de instalação, conferir Windows/arquitetura, recursos, WSL e virtualização; oferecer alternativa nativa se não for adequado. Nenhum reboot ou alteração de recurso Windows autorizado por esta comparação.
- Não atualizar Node por novidade. Reconfirmar caminho efetivo e compatibilidade na preparação, pois há runtimes do Codex também no PATH.
- Provedor do catálogo real permanece escolha separada; manter a comparação RAWG/IGDB existente. Modo demonstrativo não depende dele.
- Primeiro commit será documental, após revisão de arquitetura/backlog e organização, antes de qualquer aplicação (DEC-024).

Fontes adicionais: [npm workspaces](https://docs.npmjs.com/cli/v12/using-npm/workspaces/), [Express 5](https://expressjs.com/en/guide/migrating-5/), [SQLite: adequação](https://sqlite.org/whentouse.html), [SQL com node-postgres](https://node-postgres.com/features/queries), [Compose](https://docs.docker.com/compose/), [Docker Windows](https://docs.docker.com/desktop/setup/install/windows-install/), [Docker pessoal](https://www.docker.com/products/personal/).

## Aprovação e próximo passo
Aprovada explicitamente em DEC-025: Angular desde a primeira jornada visual; NestJS modular; PostgreSQL + Prisma; npm workspaces em repositório único; Compose para demonstração; testes progressivos Vitest/integração/Playwright. ADR-001/002 também aprovados em DEC-026/027. Textos de proposta acima preservam a análise apresentada. Próximo passo: fixar versões/plano de ambiente, finalizar documentação e primeiro commit, depois autorizar a primeira tarefa de aplicação. Somente metadados atualizados após o aceite; nenhum pacote instalado por esta aprovação.

# Executar a base técnica

Estado verificado em 03/11/2026 — TASK-001 v0.2, DEC-033. Esta entrega contém a tela inicial Angular e uma resposta técnica NestJS. As jornadas de biblioteca, contas e avaliações ainda serão implementadas.

## Preparar

Abra um terminal na raiz do repositório, onde estão package.json e package-lock.json. Use Node 24.21.0 e npm 12.0.2, as versões conferidas nesta entrega. Não é necessário iniciar Docker ou PostgreSQL para esta base.

```sh
node --version
npm --version
npm ci
```

npm ci instala a resolução registrada no lockfile. O projeto raiz gerencia os pacotes @gamevault/web e @gamevault/api; não execute instalações separadas em apps/web e apps/api. Nenhuma CLI global é necessária.

## Iniciar em dois terminais

No primeiro terminal, na raiz:

```sh
npm run dev:web
```

Abra http://127.0.0.1:4200. Deve aparecer GameVault 2.0 e Biblioteca de jogos em construção. Pressione Tab para alcançar Ir para o conteúdo e Enter para mover o foco à área principal.

No segundo terminal, também na raiz:

```sh
npm run dev:api
```

Abra http://127.0.0.1:3000. A resposta esperada é GameVault API. Uma rota inexistente retorna 404. No Windows, é possível conferir os cabeçalhos HTTP com:

```powershell
curl.exe -i http://127.0.0.1:3000/
curl.exe -i http://127.0.0.1:3000/rota-inexistente
```

Os servidores escutam somente em 127.0.0.1. Se uma porta estiver ocupada, não encerre processos desconhecidos: ajuste uma porta local livre antes de iniciar. O Angular aceita --port pelo comando direto do workspace; a API lê PORT do ambiente do terminal. A web ainda não chama a API.

Para encerrar, pressione Ctrl+C em cada terminal. Os modos de desenvolvimento recompilam quando arquivos mudam; não deixe processos duplicados consumindo as mesmas portas.

## Compilar

```sh
npm run build:web
npm run build:api
npm run build
```

O último comando executa os dois anteriores em sequência e falha se algum deles falhar. Saídas: apps/web/dist/web/browser e apps/api/dist. Compilados e cache .angular não são versionados.

## Entender os arquivos

| Arquivo | Papel nesta base |
| --- | --- |
| apps/web/src/main.ts | Inicia Angular com o componente raiz e sua configuração |
| apps/web/src/app/app.ts | Componente standalone com HTML da tela inicial; imports declara o que seu template utiliza |
| apps/web/src/app/app.config.ts e app.routes.ts | Configuração de aplicação e espaço para as futuras rotas |
| apps/api/src/main.ts | Cria a aplicação Nest e limita o servidor ao loopback |
| apps/api/src/app.module.ts | Registra controller e service no contêiner de dependências Nest |
| apps/api/src/app.controller.ts | Recebe GET / e delega ao service |
| apps/api/src/app.service.ts | Fornece a resposta técnica inicial; futuramente serviços próprios conterão regras aprovadas |
| package.json da raiz | Scripts, ferramentas de desenvolvimento e lista de workspaces |
| package-lock.json | Versões resolvidas, inclusive dependências transitivas, usadas por npm ci e CI |

Angular usa uma configuração TypeScript para o bundler do navegador; Nest compila ESM para Node. Os imports .js da API apontam para os arquivos JavaScript gerados, mesmo quando o fonte correspondente é .ts.

## Verificações e limitações

Build não valida regras do produto. Nesta tarefa foram verificados compilação, tela no navegador, console, teclado básico e respostas HTTP 200/404; não há testes de regras, integração com banco ou jornadas completas. A CI executa integridade documental e build com npm ci; sem deploy.

A instalação com npm 12 informou scripts de instalação bloqueados em quatro dependências transitivas nativas. Os builds e a execução passaram sem habilitá-los. Não é necessário aprovar scripts ou forçar instalação para repetir o resultado desta base.

Há aviso moderado em minimatch transitivo da CLI Nest, acompanhado em [revisão TASK-001](../reviews/TASK-001.md). A auditoria sem dependências de desenvolvimento retornou zero avisos na verificação desta entrega; isso não é garantia de ausência de vulnerabilidades. Não executar npm audit fix --force: a correção sugerida alteraria a matriz aprovada. Mudanças de dependências serão avaliadas explicitamente.

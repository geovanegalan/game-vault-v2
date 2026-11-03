# TASK-001 — Base técnica mínima do workspace

Versão: 0.2 | Estado: aprovada em DEC-033; implementada/verificada localmente e na CI, revisão humana pendente | Data: 03/11/2026
Issue: [#8](https://github.com/geovanegalan/game-vault-v2/issues/8) | Branch: feature/task-001-base-tecnica
REQ: 001 a 005 (fundação) | Base: DEC-023/025/026/027/033

## Objetivo e aprendizado

Criar duas bases pequenas que compilem e iniciem localmente: Angular em apps/web e NestJS em apps/api. Explicar o componente inicial Angular, a entrada HTTP do Nest, módulos/injeção de dependências e como os scripts npm coordenam os dois pacotes. Ao final haverá uma base executável, ainda sem jornadas do GameVault.

Workspace npm significa um projeto raiz que gerencia os dois pacotes e um único package-lock.json. A configuração Angular fica em apps/web/angular.json; a API tem configuração própria de TypeScript/Nest. Não se cria um monorepo adicional do Nest dentro desse workspace.

## Escopo proposto e alternativas

Recomendação: gerar as duas bases juntas, com TypeScript estrito, Angular standalone/zoneless com CSS simples e configuração inicial de rotas, e Nest em ESM com o adaptador Express padrão. Isso testa cedo a compatibilidade e entrega uma tela visível; exige aprender inicialmente conceitos dos dois frameworks.

Alternativa: primeiro somente API, deixando Angular para outra tarefa. Reduz troca de contexto, mas adia o primeiro resultado visual e a validação do workspace completo. Não adotada; se preferida pelo usuário, revisar esta tarefa antes de executar.

Usar o adaptador Express aproveita a experiência informada pelo usuário. O NodeAdapter recomendado na documentação Nest 12.3 é alternativa viável, mas não traz um requisito novo a esta base; nenhuma troca de adaptador foi adotada. Usar ESM mantém a direção aprovada e as configurações modernas dos geradores, sem introduzir CommonJS ou Jest como escolha automática.

Inclui: arquivos mínimos web/API, configuração de workspaces, scripts, versões diretas exatas, lockfile único, builds locais, execução básica, documentação e um job de build na CI. Não inclui autenticação, biblioteca, catálogo, conexão entre web/API, banco/Prisma, Dockerfiles/Compose da aplicação, dados de exemplo, biblioteca de UI, observabilidade externa, deploy ou publicação de pacotes.

Testes de regras, integração e navegador entram nas tarefas com comportamento correspondente. Nesta base, omitir testes demonstrativos que apenas repetem o texto inicial; isso não elimina a estratégia Vitest/integração/Playwright aprovada. Ferramentas de teste/lint não utilizadas serão retiradas dos arquivos recém-gerados antes da instalação, evitando dependências e scripts sem uso nesta tarefa.

## Versões concretas propostas

Metadados oficiais npm consultados em 03/11/2026; nenhuma instalação ou execução de gerador feita nesta preparação.

| Área / pacotes diretos | Versão proposta | Motivo / compatibilidade |
| --- | --- | --- |
| Node.js / npm existentes | 24.21.0 / 12.0.2 | Reconferidos; atendem requisitos dos pacotes propostos; nenhuma atualização global |
| Angular: core, common, compiler, platform-browser e router | 22.2.4 | Mesma versão do framework; Node ^24.15.0 aceito |
| Angular compiler-cli | 22.2.4 | Exige TypeScript >=6.0 <6.1 |
| Angular CLI / build | 22.2.5 | Ferramentas têm patch próprio; suportam Angular 22 e TypeScript 6.0 |
| Gerador Angular: @schematics/angular | 22.2.5 | Dependência exata da CLI consultada |
| Nest: common, core e platform-express | 12.3.2 | Mesma versão dos pacotes da API; Node existente aceito |
| Nest CLI / schematics | 12.0.11 / 12.0.12 | CLI depende de TypeScript ~6.0.2; gerador aceita Node ^24.15.0 |
| TypeScript | 6.0.3 | Satisfaz Angular e Nest CLI; latest consultado é 7.0.2, incompatível com o intervalo do compilador Angular |
| RxJS / reflect-metadata / tslib | 7.8.2 / 0.2.2 / 2.9.1 | Intervalos publicados dos frameworks aceitam essas versões; reflect-metadata para a API |
| @types/node / @types/express | 24.19.2 / 5.0.6 | Tipos para as linhas Node 24 e Express 5; não instalar tipos Node 26 por serem latest |

Fixar essas dependências diretas onde forem usadas; não adicionar um pacote apenas por constar da matriz se o projeto mínimo não o utiliza. Dependências transitivas serão resolvidas em intervalos publicados e registradas no lockfile, incluindo versões distintas de ferramentas internas quando necessárias. Não forçar unificação com overrides, --force ou --legacy-peer-deps para ocultar conflito. Mudança de linha ou dependência direta não prevista exige explicar/revisar a parte afetada.

Forms, animations, zone.js, SSR, Vitest e outras ferramentas opcionais não são necessários ao comportamento desta base. A escolha de omiti-los agora não decide a implementação das funcionalidades futuras.

## Plano de execução após aprovação

1. Conferir Git, branch e aprovações; criar a feature de implementação a partir de develop após integração dos documentos necessários. Preservar o checkpoint e alterações do usuário. Criar Issue TASK-001 e acompanhar no Project somente após autorização da tarefa.
2. Revalidar metadados/versões e opções de ajuda das CLIs fixadas. Geradores podem ser obtidos no cache npm para bootstrap, sem instalação global. Gerar sem instalar pacotes e sem inicializar repositórios Git internos. Conferir antes de agir qualquer opção diferente da documentação.
3. Revisar o conteúdo recém-gerado; manter a base mínima, remover apenas testes/tooling de exemplo fora do escopo, nomes/scripts conflitantes e README duplicado de gerador. Configurar pacote raiz private, workspaces apps/web e apps/api, um lockfile e dependências diretas exatas. Manter tsconfigs adequados ao bundler Angular e ao ESM da API, sem impor uma configuração única inadequada aos dois.
4. Instalar a partir da raiz; executar builds; iniciar cada processo somente em loopback (127.0.0.1), verificar o resultado e encerrar os processos próprios. Sem abrir firewall, publicar portas em todas as interfaces ou conectar ao PostgreSQL.
5. Acrescentar CI de build com instalação reproduzível por npm ci, Node/npm fixados e build dos dois pacotes; manter o check documental existente com seu nome exigido pelas proteções. Não configurar deploy nem alterar proteções nesta tarefa. Propor exigir o novo check em etapa própria após evidência de execução real.
6. Atualizar README, guia de execução e evidências; revisar diff e abrir PR para develop. Usuário faz o merge manualmente.

### Referência dos geradores — plano aprovado

Comandos abaixo são referências de planejamento baseadas nas opções oficiais. Após aprovação, conferir --help da versão fixada antes de executá-los; npm exec baixa/executa ferramentas no cache e não equivale a uma consulta somente leitura.

```text
npm exec --yes --package=@angular/cli@22.2.5 -- ng new web --directory=apps/web --package-manager=npm --skip-install --skip-git --minimal --standalone --strict --routing --style=css --ssr=false --zoneless --interactive=false
npm exec --yes --package=@nestjs/cli@12.0.11 --package=@nestjs/schematics@12.0.12 -- nest new api --directory apps/api --package-manager npm --skip-install --skip-git --skip-tests --language TS --no-observe
```

Nest em ambiente não interativo seleciona ESM conforme documentação; conferir o arquivo gerado em vez de inventar uma flag de módulo. Nenhum aceite de serviço externo, credencial ou ferramenta de observabilidade incluído. Se o gerador solicitar algo fora dessa proposta, interromper a parte afetada e explicar.

## Arquivos e comandos previstos

| Área | Arquivos / efeito esperado |
| --- | --- |
| Raiz | package.json privado com workspaces/scripts e package-lock.json único; sem aplicação gerada sobre README/AGENTS existentes |
| apps/web | angular.json, package.json, tsconfigs, src/main.ts, componente inicial e configuração/rotas mínimas; uma tela de identificação técnica, sem layout de produto |
| apps/api | package.json, nest-cli.json, tsconfigs, src/main.ts e módulo/controller/service iniciais do gerador; resposta técnica inicial sem regra de produto |
| .gitignore | Complementar apenas artefatos gerados como .angular/ e metadados de compilação, conforme o inventário real |
| .github/workflows | Novo job de build usando os scripts reais, sem mudar o nome/check documental exigido ou permissões de branches |
| Documentação | README, docs/ambiente/COMO-EXECUTAR.md, STATUS e evidências/revisão da tarefa |

Scripts raiz propostos: build:web, build:api, build, dev:web e dev:api; não instalar um orquestrador de processos só para iniciá-los juntos. Dois terminais no desenvolvimento são suficientes. Nomear pacotes @gamevault/web e @gamevault/api e documentar o direcionamento com npm --workspace. Os scripts serão escritos/verificados na implementação antes de virarem instruções para quem experimenta.

## Critérios de aceite e verificação

| Critério | Como conferir após implementar |
| --- | --- |
| Instalação coerente | Um lockfile raiz, sem lockfiles concorrentes; npm ci no runner instala a resolução registrada |
| Build web e API | Scripts separados e combinado encerram com código 0; erros não são mascarados |
| Base web acessível | Abrir em loopback, verificar texto técnico inicial, renderização sem erro de console e navegação básica por teclado; sem alegar auditoria completa de acessibilidade |
| Base API acessível | Requisição HTTP local retorna a resposta inicial esperada; rota inexistente retorna 404; nenhum banco ou chave necessário |
| Configuração local | Duas aplicações sem .git interno, nomes de workspace claros, arquivos compilados ignorados; encerrar somente processos criados no teste |
| CI real | Check documental e job de build passam no PR; distinguir esse resultado de testes de produto ainda inexistentes |
| Entrega com tutoria | Explicar arquivos de entrada, componente/module/controller/service, scripts e lockfile; comandos de iniciar/encerrar/build documentados e realmente executados |

Portas locais candidatas: web 4200 e API 3000, somente após conferir disponibilidade. Não parar processos existentes para liberá-las; usar outra porta local livre e registrar, se necessário. Gerar build não comprova regras de negócio, integração web/API ou MVP funcional.

## Impacto e recuperação

Downloads npm e criação de node_modules/cache/arquivos do projeto são parte desta proposta e aguardam aprovação. Sem troca de runtime, instalação global na máquina, atualização de Docker/WSL/PostgreSQL ou uso de dados pessoais. A CI usa seu próprio ambiente isolado; as ações e versões do runner serão conferidas antes de configurar o job.

Se dependências diretas não resolverem a matriz, não concluir compatibilidade só pelos manifests: guardar erro minimizado, investigar e apresentar alternativas concretas. Corrigir arquivos locais reversíveis dentro do escopo aprovado é permitido; mudança material de stack/arquitetura/comportamento depende de aprovação. Não usar reset/clean, apagar alterações do usuário, forçar instalações ou reescrever histórico.

## Fontes e evidências da preparação

- [Angular: compatibilidade](https://angular.dev/reference/versions), [opções de ng new](https://angular.dev/cli/new), boas práticas oficiais retornadas pelo MCP Angular. MCP não encontrou workspace Angular, coerente com ausência de aplicação.
- [Nest: primeiros passos](https://docs.nestjs.com/first-steps) e [CLI](https://docs.nestjs.com/cli/usages), incluindo ESM, --skip-install, --skip-git, --skip-tests e --no-observe.
- [npm: workspaces](https://docs.npmjs.com/cli/v12/using-npm/workspaces/) e [npm exec](https://docs.npmjs.com/cli/v12/commands/npm-exec/).
- Metadados primários de versões: [Angular core 22.2.4](https://registry.npmjs.org/@angular%2Fcore/22.2.4), [compiler-cli 22.2.4](https://registry.npmjs.org/@angular%2Fcompiler-cli/22.2.4), [build 22.2.5](https://registry.npmjs.org/@angular%2Fbuild/22.2.5), [Nest core 12.3.2](https://registry.npmjs.org/@nestjs%2Fcore/12.3.2), [Nest CLI 12.0.11](https://registry.npmjs.org/@nestjs%2Fcli/12.0.11), [Nest schematics 12.0.12](https://registry.npmjs.org/@nestjs%2Fschematics/12.0.12) e [TypeScript 6.0.3](https://registry.npmjs.org/typescript/6.0.3); pares/engines e dependências auxiliares consultados no mesmo registro.

Estado histórico da preparação em 03/11, antes de DEC-033: Git limpo na branch de checkpoint, Node 24.21.0, npm 12.0.2, Docker CLI 29.9.2 e Compose v5.6.1 responderam. Docker Desktop não informou status do motor naquela consulta e não foi iniciado/atualizado. TASK-001 não depende de Docker. Naquela fase nenhum gerador, instalação, build ou aplicação tinha sido executado/criado; execução após aprovação abaixo.

## Aprovação e histórico

Aprovada explicitamente pelo usuário em DEC-033: “Aprovo a TASK-001 v0.2, com as versões e o plano propostos. Fiz o merge do PR #7. Pode conferir e começar a implementação com a tutoria.” A aprovação abrange a matriz de versões, plano/escopo e verificações; o merge documental foi conferido antes da execução. Aprovação desta tarefa não aprova automaticamente o restante do backlog. Textos de proposta acima preservam o conteúdo apresentado e aprovado.

- v0.1 (01/11/2026): proposta inicial, sem patches ou plano de geração detalhado; não autorizada.
- v0.2 (03/11/2026): proposta concreta com versões, alternativas, limites, geração, validação e tutoria; posteriormente aprovada explicitamente em DEC-033. Conteúdo anterior recuperável no Git.

## Execução e evidências — 03/11/2026

- PR #7 confirmado mesclado em develop, b32002a; feature criada desse remoto, preservando o checkpoint. Aprovação registrada antes de geração/instalação; Issue #8 e cartão de implementação criados.
- Opções --help das CLIs fixadas conferidas. Geradores executados com skip-install/skip-git e ambiente não interativo; Angular com ai-config=none adicional. Nest gerou ESM, sem Observe. Removidos somente artefatos recém-gerados de teste/lint/deploy, READMEs duplicados, configurações de editor e instruções opcionais de observabilidade fora do escopo.
- Versões diretas da matriz confirmadas por npm ls --depth=0; npm install criou um lockfile na raiz. Sem Git interno ou lockfiles concorrentes. Nenhuma instalação global na máquina.
- npm run build executou os scripts web/API separados e passou com código 0. Saídas conferidas: apps/web/dist/web/browser e apps/api/dist/main.js.
- npm ci repetido localmente a partir do lockfile passou; build combinado após essa reinstalação também passou. Conferência documental: 33 Markdown, 38 links locais válidos, manifestos privados/pins e diff check passaram.
- Servidor Angular via MCP compilou; navegador mostrou tela inicial, title GameVault 2.0, lang pt-BR e console sem erros capturados. Tab e Enter no link de salto focaram main#conteudo. Não se afirma auditoria completa de acessibilidade ou jornada de produto.
- API em modo watch iniciou; GET / 200 com GameVault API e rota inexistente 404. Listeners limitados a 127.0.0.1. Somente processos próprios encerrados; portas 3000/4200 liberadas depois do teste. PostgreSQL permanece Running/Automatic; sem conexão ao banco ou leitura de credenciais.
- Novo job de build usa Node 24.21.0, npm 12.0.2, npm ci e npm run build no runner; check documental existente e proteções preservados. Execuções reais da implementação 0fba771 passaram: [documental](https://github.com/geovanegalan/game-vault-v2/actions/runs/41718315560) e [build Linux](https://github.com/geovanegalan/game-vault-v2/actions/runs/41718315696). Entrega no [PR #9](https://github.com/geovanegalan/game-vault-v2/pull/9); conferir CI do último head antes do merge.
- Guia verificado em [COMO-EXECUTAR](../ambiente/COMO-EXECUTAR.md); revisão/pendência em [TASK-001 review](../reviews/TASK-001.md).

## Pendência e limite de conclusão

npm audit identificou aviso moderado em minimatch transitivo da CLI Nest (duas entradas na mesma cadeia); npm audit --omit=dev retornou zero. npm sugeriu mudar para CLI 11.0.24, fora da matriz aprovada. Nenhuma troca/override aplicada; opções e recomendação constam na revisão para decisão humana. Npm 12 bloqueou scripts nativos transitivos; instalação, builds e execução passaram sem habilitá-los.

A tarefa tem implementação, verificações locais e CI real realizadas; pendência de desenvolvimento e revisão/merge humanos ainda integram a avaliação da entrega. Isso não aprova as tarefas seguintes nem significa MVP funcional. A pendência de dependência não foi tratada como risco aceito pelo usuário.

# Ponto de retomada

Atualizado em 01/11/2026 — limpeza documental e configuração do Project, antes de código.

## Aprovações e limites

- Produto: VISAO v0.3, PRD v0.6, MVP v0.6 e P-01 a P-06 — DEC-023.
- Stack: COMPARACAO-STACK v0.1 — DEC-025; ADR-001/002 v0.1 — DEC-026/027.
- BACKLOG v0.1 é proposta; TASK-001 ainda não autorizada. Nenhuma aplicação, dependência de produto, migração ou teste de produto criado/executado.
- DEC-030 autoriza CLI somente para o repositório GameVault e Project pessoal #2; substitui a administração manual de DEC-029. Nenhum outro repositório/organização consultado.
- DEC-031 autoriza limpeza documental, ajustes e commit. Todos os merges continuam manuais pelo usuário; nenhum push direto futuro em main/develop, força ou auto-merge permitido.

## GitHub e Project

- Repositório público: [game-vault-v2](https://github.com/geovanegalan/game-vault-v2). Autoria local Geovane/no-reply; configuração global preservada.
- Primeiro commit exclusivamente documental: `263c7bb`; main/develop protegidas com PR/check documental, branch atualizada, conversas resolvidas, administradores incluídos e força/exclusão bloqueadas. Auto-merge false. CI passou nas bases no bootstrap.
- [PR #2](https://github.com/geovanegalan/game-vault-v2/pull/2) mesclado manualmente pelo usuário em develop, commit `52b2acd`. Nova feature/docs-organizacao-project criada desse estado remoto.
- [Project GameVault 2.0 #2](https://github.com/users/geovanegalan/projects/2) vinculado ao repositório; descrição/README configurados e estados/opções conferidos. Issue #1 em andamento, PR #2 concluído; Issue #3 acompanha esta limpeza.
- Repositório padrão para criação pela interface, views e automações não alterados/atestados. CLI usa destino explícito. Ver [guia GitHub](GITHUB.md) e [evidências](ambiente/EVIDENCIAS-BOOTSTRAP.md).

## Limpeza documental

- Removidos dez arquivos redundantes: prompt inicial, sete modelos vazios, organização documental antiga e plano GitHub já executado. Operação consolidada em GITHUB.md, STATUS e evidências; versões anteriores recuperáveis no Git.
- Mantidos requisitos aprovados, ADRs, decisões, entrevista, diagnóstico/plano de instalação, fontes, backlog e tarefa proposta, skills e templates Issue/PR. São documentação do projeto e devem continuar versionados.
- README simplificado; quatro skills e verificador ajustados para documentos reais. .gitignore já cobre .env, dependências, builds, cobertura, logs e caches existentes; nenhum documento necessário ocultado.
- Conferência local passou: 29 Markdown, 27 links locais válidos, 15 documentos essenciais presentes e cinco skills com metadados válidos; git diff --check passou. Produto/stack/ADRs sem alterações. Busca por padrões conhecidos de segredos/caminhos pessoais sem ocorrência; não equivale a auditoria completa. Script Python não executado localmente; resultado real da CI será registrado na Issue #3 e no PR desta feature. CI documental não comprova comportamento da aplicação.
- Histórico inicial já público não reescrito; a minimização posterior de detalhes do host não remove dados de commits antigos. Ver reviews/BOOTSTRAP.md.

## Ambiente e próximos passos

- Node 24.21.0 e npm efetivo 12.0.2 compatíveis documentalmente, sem atualização necessária. Windows x64/WSL 2 disponíveis; PostgreSQL 18.3 nativo preservado, sem acesso a dados/credenciais.
- Docker não instalado. A-02 de [PLANO-AMBIENTE v0.1](ambiente/PLANO-AMBIENTE.md) propõe Docker Desktop 4.97.0 e aguarda aprovação do instalador/impacto; verificar backend após instalar. Nenhuma alteração Windows/WSL/banco feita.
- Python local é alias sem interpretador; CI executa o script no GitHub. Não instalar apenas para o kit.
- Usuário revisar/mesclar manualmente o PR desta limpeza para develop; só depois uma versão revisada seguirá por PR develop → main para atualizar a página padrão do GitHub.
- Aprovar ou ajustar A-02 antes de instalar Docker. Revisar e autorizar TASK-001 antes do código.
- Provedor real do catálogo, parâmetros de senha/sessão e versões exatas de dependências continuam para refinamento nas tarefas correspondentes.

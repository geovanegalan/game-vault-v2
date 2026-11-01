# Ponto de retomada

Atualizado em 01/11/2026 — documentação revisada em main; Docker A-02 instalado e critérios de validação passaram, antes de código.

## Aprovações e limites

- Produto: VISAO v0.3, PRD v0.6, MVP v0.6 e P-01 a P-06 — DEC-023.
- Stack: COMPARACAO-STACK v0.1 — DEC-025; ADR-001/002 v0.1 — DEC-026/027.
- BACKLOG v0.1 é proposta; TASK-001 ainda não autorizada. Nenhuma aplicação, dependência de produto, migração ou teste de produto criado/executado.
- DEC-030 autoriza CLI somente para o repositório GameVault e Project pessoal #2; substitui a administração manual de DEC-029. Nenhum outro repositório/organização consultado.
- DEC-031 autoriza limpeza documental, ajustes e commit. Todos os merges continuam manuais pelo usuário; nenhum push direto futuro em main/develop, força ou auto-merge permitido.
- DEC-032 aprova PLANO-AMBIENTE v0.1, item A-02: baixar, instalar por usuário/WSL 2 e validar Docker Desktop 4.97.0, preservando PostgreSQL. Aprovação não inclui TASK-001 ou mudanças adicionais no Windows.

## GitHub e Project

- Repositório público: [game-vault-v2](https://github.com/geovanegalan/game-vault-v2). Autoria local Geovane/no-reply; configuração global preservada.
- Primeiro commit exclusivamente documental: `263c7bb`; main/develop protegidas com PR/check documental, branch atualizada, conversas resolvidas, administradores incluídos e força/exclusão bloqueadas. Auto-merge false. CI passou nas bases no bootstrap.
- [PR #2](https://github.com/geovanegalan/game-vault-v2/pull/2) e [PR #4](https://github.com/geovanegalan/game-vault-v2/pull/4) mesclados manualmente pelo usuário em develop. [PR #5](https://github.com/geovanegalan/game-vault-v2/pull/5) promoveu os documentos para main, commit `76df4ff81e5d3bf9855e361dfe8620679f390c01`; merge confirmado pela API. Conteúdo de main/develop idêntico após a promoção; hashes distintos pelo commit de merge.
- [CI do commit integrado em main](https://github.com/geovanegalan/game-vault-v2/actions/runs/41355086123) concluída com success. CI em develop após PR #4 também passou: execução 41354704571. Verificações exclusivamente documentais.
- [Project GameVault 2.0 #2](https://github.com/users/geovanegalan/projects/2) vinculado ao repositório; descrição/README configurados e estados/opções conferidos. Issue #1 acompanha esta preparação; Issue #3 fechada e cartões dos PRs #2/#4/#5 concluídos. Feature/ambiente-preparacao contém retomada e evidências A-02; a instalação foi autorizada por DEC-032, não pela criação da branch.
- Repositório padrão para criação pela interface, views e automações não alterados/atestados. CLI usa destino explícito. Ver [guia GitHub](GITHUB.md) e [evidências](ambiente/EVIDENCIAS-BOOTSTRAP.md).

## Limpeza documental

- Removidos dez arquivos redundantes: prompt inicial, sete modelos vazios, organização documental antiga e plano GitHub já executado. Operação consolidada em GITHUB.md, STATUS e evidências; versões anteriores recuperáveis no Git.
- Mantidos requisitos aprovados, ADRs, decisões, entrevista, diagnóstico/plano de instalação, fontes, backlog e tarefa proposta, skills e templates Issue/PR. São documentação do projeto e devem continuar versionados.
- README simplificado; quatro skills e verificador ajustados para documentos reais. .gitignore já cobre .env, dependências, builds, cobertura, logs e caches existentes; nenhum documento necessário ocultado.
- Conferência local da limpeza passou: 29 Markdown, 27 links locais válidos, 15 documentos essenciais presentes e cinco skills com metadados válidos; git diff --check passou. Produto/stack/ADRs sem alterações. Busca por padrões conhecidos de segredos/caminhos pessoais sem ocorrência; não equivale a auditoria completa. Script Python não executado localmente; CI real passou na feature (41354362994), na promoção (41354992802) e nas bases após merges. Evidências de integração também na Issue #3. CI documental não comprova comportamento da aplicação.
- Histórico inicial já público não reescrito; a minimização posterior de detalhes do host não remove dados de commits antigos. Ver reviews/BOOTSTRAP.md.

## Ambiente e próximos passos

- Node 24.21.0 e npm efetivo 12.0.2 compatíveis documentalmente, sem atualização necessária. Windows x64/WSL 2 disponíveis; PostgreSQL 18.3 nativo preservado, sem acesso a dados/credenciais.
- A-02 de [PLANO-AMBIENTE v0.1](ambiente/PLANO-AMBIENTE.md) aprovado em DEC-032. Docker Desktop 4.97.0.244584 instalado por usuário/WSL 2 (saída 0), SHA-256/assinatura válidos. Docker CLI/motor 29.9.2, Compose v5.6.1, backend e PATH registrado conferidos; hello-world por digest executou com código 0, sem rede/montagens/portas, e remoção automática confirmada. PostgreSQL nativo observado Running/Automatic antes e depois, sem conexão a dados ou leitura de credenciais. Evidências em [EVIDENCIAS-DOCKER](ambiente/EVIDENCIAS-DOCKER.md).
- Python local é alias sem interpretador; CI executa o script no GitHub. Não instalar apenas para o kit.
- Documentação e limpeza já integradas em main pelos merges manuais; não abrir outro PR apenas para repetir esta promoção. Rascunhos de retomada serão incluídos na próxima entrega de ambiente/planejamento pelo fluxo normal.
- Antes da instalação: Docker ausente no PATH e nos dois locais padrão; requisitos básicos observados atendidos. Release oficial 4.97.0 e instalação por usuário/backend WSL 2 reconfirmadas. Nenhuma alteração de recursos Windows por inferência foi executada.
- Usuário escolheu preparar Docker agora em DEC-032 e confirmou aceite dos termos na primeira abertura. Critérios A-02 passaram; artefatos temporários próprios removidos, imagem de diagnóstico mantida no cache. Nenhuma aplicação/banco de projeto criada. Terminais antigos podem exigir reabertura para carregar PATH.
- Entregar evidências por PR de feature/ambiente-preparacao para develop, com revisão e merge manuais; Issue #1 permanece em acompanhamento até essa integração. Próximo marco: detalhar versões estáveis exatas e obter autorização de TASK-001 antes de iniciar código.
- Provedor real do catálogo, parâmetros de senha/sessão e versões exatas de dependências continuam para refinamento nas tarefas correspondentes.

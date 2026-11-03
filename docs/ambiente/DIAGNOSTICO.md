# Diagnóstico do ambiente
Atualizado em 01/11/2026 — preparação após aprovação da stack/ADRs. Versão pública com minimização de dados: caminhos pessoais, hardware e identificação detalhada do sistema omitidos; coleta original recuperável nesta sessão.

## Sistema e ferramentas observados
| Item | Fato observado | Situação / consequência |
| --- | --- | --- |
| Sistema | Windows x64; PowerShell disponível | Família necessária ao método de instalação; não publicar build/edição ou métricas da máquina |
| Backend de contêineres | Requisitos básicos consultados; execução ainda não verificada | Não alterar BIOS/Windows; validar backend antes de declarar Docker pronto |
| WSL | 3.0.3, WSL 2 disponível | Sem necessidade comprovada de atualizar; nenhuma distribuição iniciada nesta consulta |
| Git | 2.46.1.windows.1, executável disponível | Repositório local agora inicializado em main, antes sem Git |
| Node | 24.21.0, executável disponível | Atende intervalos publicados da stack aprovada; build conjunto não testado; sem atualização proposta |
| npm | Comando efetivo 12.0.2; instalações coexistentes | Há npm 11.19.0 na distribuição Node e 12.0.2 efetivo; manifests aceitam Node observado. Não remover/atualizar por coexistirem |
| GitHub CLI | 2.103.1, executável disponível | Acesso ao remoto público confirmado; caminhos de instalação omitidos |
| GitHub/MCP | Ferramentas do conector apareceram e consultas de login/repositório retornaram conta e permissões | Conexão verificada, atualizando diagnóstico anterior de plugin apenas sugerido |
| PostgreSQL nativo | psql 18.3; serviço postgresql-x64-18 Running/Automatic | Já existe banco nativo. Não foram lidos dados/credenciais nem houve conexão, atualização ou parada; banco do projeto será separado |
| Docker | Desktop 4.97.0.244584 por usuário/WSL 2 após DEC-032; CLI/motor 29.9.2 e Compose v5.6.1 | Hash/assinatura válidos, instalador saída 0; motor local e hello-world descartável passaram; PATH registrado confirmado. Ver EVIDENCIAS-DOCKER.md |
| winget | 1.29.380 executou fora da restrição inicial | Disponível; não usado para instalar/atualizar |
| Python | Alias WindowsApps; consulta retorna que Python não foi encontrado | Sem interpretador executável por esse comando. Opcional, não instalar só para o kit |
| Angular/Nest/Prisma | TASK-001 aprovada: Angular 22.2.4/Nest 12.3.2 e TypeScript 6.0.3 instalados localmente com lockfile único; builds e execução básica passaram | Sem CLI global ou Prisma/banco de projeto; aviso de desenvolvimento na CLI descrito em ../reviews/TASK-001.md |

## Git local e remoto — coleta pré-primeiro commit
- Antes das alterações, git status confirmou ausência de repositório local. Inicialização em main e origin no remoto informado foram executadas após autorização de preparação/primeiro commit.
- Autoria local confirmada pelo usuário: Geovane e email no-reply correspondente ao ID/login público. Configuração global não alterada; email pessoal não incluído nos documentos.
- Remoto geovanegalan/game-vault-v2 confirmado público e branches=[]; API/CLI com permissões admin/push. Revalidado antes do bootstrap. Nenhum histórico remoto foi sobrescrito.
- Conexão MCP e CLI verificadas separadamente; operações não oferecidas pelo conector usam CLI quando autorizadas.
- Resultados de publicação/proteções/recursos registrados em ../STATUS.md e EVIDENCIAS-BOOTSTRAP.md após execução.

## Verificações e limites
- Consultas CIM/WSL/winget inicialmente bloqueadas; repetidas com permissão apropriada, retornaram resultados acima. Nenhuma ampliação de rede ou mudança de permissões de máquina executada por contorno.
- Leitura limitada à pasta, legado autorizado e ferramentas pertinentes; sem varrer outros arquivos pessoais, ler .env/credenciais ou dados do PostgreSQL existente.
- Revisão documental: 37 arquivos Markdown e 27 links locais, nenhum destino ausente; busca por padrões conhecidos de credenciais não encontrou ocorrências. Essa busca não é auditoria completa de segredos.
- Verificador Python não executado; testes de aplicação/build/integração não executados, pois aplicação ainda não existe.
- Compatibilidade publicada em COMPARACAO-STACK/FONTES. Nenhuma instalação de dependência, contêiner de aplicação, serviço ou migração criado por este diagnóstico.

## Plano e histórico
- Produto DEC-023; stack/ADRs DEC-025/026/027 aprovados.
- Plano concreto PLANO-AMBIENTE v0.1 propôs somente Docker Desktop 4.97.0 nesta etapa; A-02 posteriormente aprovado em DEC-032 e executado com verificações descritas em EVIDENCIAS-DOCKER.md.
- O plano GitHub de bootstrap foi executado; operação corrente consolidada em ../GITHUB.md e evidências em EVIDENCIAS-BOOTSTRAP.md. Primeiro commit antes do código, conforme DEC-024.
- O diagnóstico inicial não conhecia WSL/PostgreSQL nativo e não tinha conexão MCP; a coleta atual acrescenta esses fatos, sem fingir que já estavam verificados.
- Histórico do diagnóstico inicial: nenhuma instalação/atualização havia sido executada. Após DEC-032, Docker instalado conforme A-02; verificações de CLI/Compose, motor, backend WSL 2 e hello-world passaram. Ambiente completo da aplicação não validado.

## Resultado posterior ao primeiro commit
Commit documental 263c7bb publicado; main/develop protegidas e CI documental passou em ambas. GitHub/MCP verificado; Issue #1 acompanha a preparação. Resultados/URLs em EVIDENCIAS-BOOTSTRAP.md. Após autorização explícita posterior (DEC-030), CLI confirmou o Project pessoal #2 e seu vínculo ao GameVault; configuração descrita em ../GITHUB.md. A-02 aprovado em DEC-032; Docker instalado e critérios de validação passaram, sem atualizar WSL/Node/npm ou alterar o banco nativo. PostgreSQL observado Running/Automatic antes/depois; nenhuma conexão a dados ou credenciais.

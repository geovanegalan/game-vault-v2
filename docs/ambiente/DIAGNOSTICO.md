# Diagnóstico do ambiente
Atualizado em 01/11/2026 — preparação após aprovação da stack/ADRs. Raiz: C:\Users\Geovane\Documents\GameVault - 2.0.

## Sistema e ferramentas observados
| Item | Fato observado | Situação / consequência |
| --- | --- | --- |
| Sistema | Windows 11 Pro, build 26200, x64; PowerShell 7.6.5 | Plataforma identificada por consulta somente leitura |
| Recursos | RAM total 31,9 GB; disponível 16,5 GB na coleta; hypervisor e virtualização de firmware presentes | Recursos observados, sem alteração de BIOS/Windows. Consulta SLAT retornou falso; backend ainda precisa ser validado |
| WSL | 3.0.3, kernel 6.18.54.1; Ubuntu em WSL 2, parado | Não precisa instalar/atualizar WSL por estas evidências; distribuição não iniciada nesta consulta |
| Git | 2.46.1.windows.1; D:\Git\cmd\git.exe | Disponível. Repositório local agora inicializado em main, antes sem Git |
| Node | 24.21.0; D:\node\node.exe | Atende intervalos publicados da stack aprovada; build conjunto ainda não testado; sem atualização proposta |
| npm | Comando efetivo 12.0.2; shim D:\node\npm.cmd usa prefixo do usuário | Há npm 11.19.0 na distribuição Node e 12.0.2 no prefixo do usuário; manifests aceitam Node observado. Não remover ou atualizar por coexistirem |
| GitHub CLI | 2.103.1; C:\Program Files\GitHub CLI\gh.exe | Acesso à conta geovanegalan e ao remoto público confirmado |
| GitHub/MCP | Ferramentas do conector apareceram e consultas de login/repositório retornaram conta e permissões | Conexão verificada, atualizando diagnóstico anterior de plugin apenas sugerido |
| PostgreSQL nativo | psql 18.3; serviço postgresql-x64-18 Running/Automatic | Já existe banco nativo. Não foram lidos dados/credenciais nem houve conexão, atualização ou parada; banco do projeto será separado |
| Docker | Ausente no PATH e nos diretórios padrão consultados de instalação por usuário/todos os usuários | Instalação proposta, não realizada. Instalação em outros locais não descartada por varredura |
| winget | 1.29.380 executou fora da restrição inicial | Disponível; não usado para instalar/atualizar |
| Python | Alias WindowsApps; consulta retorna que Python não foi encontrado | Sem interpretador executável por esse comando. Opcional, não instalar só para o kit |
| Angular/Nest/Prisma | Sem instalação de projeto | Linhas aprovadas; dependências locais somente após primeiro commit e tarefa autorizada |

## Git local e remoto — coleta pré-primeiro commit
- Antes das alterações, git status confirmou ausência de repositório local. Inicialização em main e origin no remoto informado foram executadas após autorização de preparação/primeiro commit.
- Autoria local confirmada pelo usuário: Geovane e email no-reply correspondente ao ID/login público. Configuração global não alterada; email pessoal não incluído nos documentos.
- Remoto geovanegalan/game-vault-v2 confirmado público e branches=[]; API/CLI com permissões admin/push. Revalidado antes do bootstrap. Nenhum histórico remoto foi sobrescrito.
- Conexão MCP e CLI verificadas separadamente; operações não oferecidas pelo conector usam CLI quando autorizadas.
- Resultados de publicação/proteções/recursos serão registrados em STATUS/PLANO-GITHUB após execução, sem afirmar antecipadamente.

## Verificações e limites
- Consultas CIM/WSL/winget inicialmente bloqueadas; repetidas com permissão apropriada, retornaram resultados acima. Nenhuma ampliação de rede ou mudança de permissões de máquina executada por contorno.
- Leitura limitada à pasta, legado autorizado e ferramentas pertinentes; sem varrer outros arquivos pessoais, ler .env/credenciais ou dados do PostgreSQL existente.
- Revisão documental: 37 arquivos Markdown e 27 links locais, nenhum destino ausente; busca por padrões conhecidos de credenciais não encontrou ocorrências. Essa busca não é auditoria completa de segredos.
- Verificador Python não executado; testes de aplicação/build/integração não executados, pois aplicação ainda não existe.
- Compatibilidade publicada em COMPARACAO-STACK/FONTES. Nenhuma instalação de dependência, contêiner de aplicação, serviço ou migração criado por este diagnóstico.

## Plano e histórico
- Produto DEC-023; stack/ADRs DEC-025/026/027 aprovados.
- Plano concreto PLANO-AMBIENTE v0.1 propõe somente Docker Desktop 4.97.0 nesta etapa; aguardando aprovação de instalação.
- PLANO-GITHUB v0.1 rege bootstrap documental, identidade e proteções; primeiro commit antes do código, conforme DEC-024.
- O diagnóstico inicial não conhecia WSL/PostgreSQL nativo e não tinha conexão MCP; a coleta atual acrescenta esses fatos, sem fingir que já estavam verificados.
- Nenhuma instalação/atualização foi executada. Ambiente completo da aplicação ainda não foi validado.

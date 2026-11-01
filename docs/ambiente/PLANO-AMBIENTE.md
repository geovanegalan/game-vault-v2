# Plano de preparação do ambiente
Versão: 0.1 | Estado: proposta concreta para aprovação | Data: 01/11/2026
Raiz: GameVault - 2.0 | Base: DEC-025/026/027 | Diagnóstico: DIAGNOSTICO.md

## Objetivo
Preparar somente o que falta para a arquitetura aprovada, preservando o ambiente atual. Não gerar aplicação ou instalar suas dependências antes do primeiro commit documental e de tarefa autorizada.

## Diagnóstico complementar
- Windows x64; requisitos básicos de sistema consultados. Caminhos pessoais, métricas de hardware e identificação detalhada do host omitidos desta versão pública.
- WSL 3.0.3, Ubuntu registrado como WSL 2 e parado. WSL não precisa ser instalado/atualizado por esta evidência.
- Backend WSL ainda não foi executado como teste de Docker; não concluir compatibilidade completa ou alterar BIOS. Validar inicialização antes de considerar Docker pronto; se houver falha, interromper e investigar.
- Node 24.21.0; comando npm executa 12.0.2 do prefixo do usuário, embora a distribuição de Node contenha npm 11.19.0. Ambos os manifests consultados aceitam Node 24.21.0; não atualizar ou remover nenhum deles. Registrar versão efetiva nos futuros builds.
- PostgreSQL 18.3 já instalado; serviço postgresql-x64-18 em execução. Não atualizar, reconfigurar, parar, conectar com credenciais ou migrar esse banco. O PostgreSQL do projeto será isolado em contêiner, sem expor 5432 no host por padrão.
- Docker não encontrado no PATH nem nos dois diretórios padrão consultados. Não foram percorridos outros discos/pastas em busca de instalações.
- Python encontrado é alias da Microsoft Store, sem interpretador executável pela consulta. Python é opcional para validação documental local; não é dependência da stack.

## Mudanças propostas
| Item | Motivo / versão e método | Alcance e impacto | Recuperação / limites | Verificação |
| --- | --- | --- | --- | --- |
| A-01 | Manter Git, Node 24.21.0, npm efetivo 12.0.2, GitHub CLI e WSL existentes | Nenhuma atualização global ou mudança de PATH | Sem remoção/substituição | Conferir versões e executáveis usados antes da tarefa de aplicação |
| A-02 | Instalar Docker Desktop 4.97.0 para Windows x86_64, release oficial de 26/10/2026, pelo link dessa release; validar SHA-256 publicado e assinatura do instalador | Preferir instalação por usuário/backend WSL 2, conforme opções oficiais. Cria arquivos/configuração do Docker e pode exigir sessão nova; usar Linux containers, sem alterar banco nativo ou firewall | Se instalador exigir privilégio, reboot, versão diferente ou alteração de recursos Windows, parar e explicar antes de ampliar o plano. Não desinstalar automaticamente; dados/volumes futuros exigem cuidado próprio | docker --version, docker compose version e docker info; iniciar um contêiner descartável de diagnóstico após aprovar este item, sem montar dados pessoais; encerrar somente o contêiner criado |
| A-03 | Não instalar outro PostgreSQL no Windows. Na futura tarefa de aplicação, usar PostgreSQL 18 em Compose com patch fixado após verificação da imagem | Banco novo isolado, sem tocar serviço existente; nenhum contêiner de aplicação criado agora | Sem migration/reset do banco anterior; volume do projeto não removido automaticamente | Futuramente conexão e persistência com banco exclusivo de teste/demonstração |
| A-04 | Não instalar CLIs Angular/Nest/Prisma globalmente; dependências locais somente em TASK-001/002 aprovadas | Nenhum package.json/lockfile de aplicação antes do primeiro commit | Se resolução sair das linhas aprovadas, parar e revisar | Versões estáveis exatas e peer dependencies conferidos na tarefa; build real antes de declarar compatibilidade |
| A-05 | Não instalar Python só para o kit neste momento | Evita ferramenta opcional sem necessidade de produto | Verificador Python local permanece não executado; Action documental usa seu próprio ambiente | Conferir execução real da Action após publicação; nunca tratar revisão manual como execução do script |

A-02 é a única instalação proposta para esta etapa. Windows/WSL/Node e PostgreSQL nativo permanecem sem atualização. Docker Desktop oferece uso pessoal/educacional gratuito nas condições publicadas; nenhum pagamento, conta paga ou assinatura autorizados.

## Versões da aplicação — seleção aprovada, instalação posterior
Linhas: Angular 22 / TypeScript 6.0, NestJS 12, Prisma 7, PostgreSQL 18; Vitest e Playwright conforme compatibilidade. Este plano não inventa patches sem verificar publicação e dependências. Antes de TASK-001, registrar as versões exatas estáveis, método de geração e instalações locais no plano da tarefa; não usar latest indiscriminadamente nem Prisma 8 release candidate.

## Ordem e participação do usuário
1. Registrar aprovações, fechar documentação e realizar primeiro commit documental autorizado; isso não depende de instalar Docker.
2. Aprovar A-02 deste plano concreto antes de baixar/executar instalador; A-01/03/04/05 são limites de manutenção/adiamento.
3. Executar instalação dentro do alcance, com explicação e permissões necessárias. Interface de termos, login eventual ou reinício solicitado são conduzidos pelo usuário; não automatizar aceite de novo escopo.
4. Verificar backend, versões e diagnóstico descartável; registrar passou/falhou/não executado. Somente depois considerar preparação Docker verificada.
5. Nenhuma tarefa de aplicação será executada sem sua aprovação própria.

## Fontes e confirmação
Consultadas em 01/11/2026: [Docker Desktop 4.97.0](https://docs.docker.com/desktop/release-notes/#4970), [instalação Windows](https://docs.docker.com/desktop/setup/install/windows-install/), [permissões Windows](https://docs.docker.com/desktop/setup/install/windows-permission-requirements), [WSL no Docker](https://docs.docker.com/desktop/features/wsl), requisitos de Angular/Nest/Prisma em `../COMPARACAO-STACK.md`. Liberação do instalador pode ser gradual; se o artefato específico não estiver disponível, apresentar outra versão concreta para revisão.

## Aprovação / execução
Pendente para A-02. A mensagem que aprova stack/ADRs autoriza preparar este plano, não foi tratada como aprovação de instalador/versão/impacto ainda não apresentados. Nenhuma instalação executada. Bootstrap GitHub tem autorização e evidências próprias em ../GITHUB.md, EVIDENCIAS-BOOTSTRAP.md e ../decisoes/REGISTRO.md.

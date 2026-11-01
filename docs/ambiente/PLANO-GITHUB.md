# Plano de documentação e bootstrap GitHub
Versão: 0.2 | Estado: bootstrap executado; Project criado manualmente, conferência parcial | Data: 01/11/2026
Base: DEC-024; complemento operacional de AMBIENTE.md/GITHUB.md. Raiz: GameVault - 2.0.

## Objetivo e evidências
Finalizar os documentos e registrar o primeiro commit antes de código de aplicação. Destino informado: [geovanegalan/game-vault-v2](https://github.com/geovanegalan/game-vault-v2), público e recém-criado.

Consulta somente leitura via GitHub CLI confirmou full_name, visibility=public, size=0, default_branch=main, permissões admin/push, branches=[] e conta geovanegalan. Revalidação no preparo confirmou branches=[]. Autoria confirmada pelo usuário: nome Geovane e email no-reply, derivado do ID público da conta e formato oficial, configurados somente neste repositório. Git inicializado localmente em main, ainda sem commit nesta coleta. Nenhuma alteração global. Se surgir histórico remoto antes de publicar, inspecionar sem sobrescrever.

## Conexão GitHub/MCP
No planejamento inicial, o plugin foi encontrado/sugerido e ainda não estava conectado. Durante a preparação, suas ferramentas ficaram disponíveis: consultas pelo conector confirmaram usuário geovanegalan, ID 144388433 e acesso administrativo ao repositório. Conexão GitHub/MCP agora verificada para essas operações. CLI permanece necessária para Git local, proteção de branches e Projects, operações não oferecidas pelo conjunto atual do conector.

Passos de referência para conexão — já verificada nesta sessão:
1. Abrir Plugins no cliente compatível, procurar GitHub e instalar a integração disponível.
2. Completar a conexão oficial solicitada e revisar o acesso ao repositório de destino; nunca enviar token/senha/chave privada no chat.
3. Informar que conectou; reavaliar ferramentas e permissões antes de afirmar disponibilidade. Documentação oficial orienta nova sessão após instalação; STATUS.md permite retomar se necessário.

Fonte: [Plugins em Codex/ChatGPT](https://learn.chatgpt.com/docs/plugins). MCP configurado manualmente é outra opção: [configuração oficial MCP](https://learn.chatgpt.com/docs/extend/mcp). Não editar configurações globais nem copiar blocos com tokens por este plano. Não foi necessário criar um servidor MCP personalizado para verificar o repositório.

Usar conector quando suficiente e CLI somente no alcance autorizado. Project é exceção operacional explícita: configuração manual pelo usuário, sem solicitar novamente ampliação de escopo (DEC-029). Leituras públicas do link fornecido podem conferir o quadro sem login. Não acessar outras organizações/projetos. Instalação do plugin não é pré-requisito técnico para Git local ou commit.

## Mudanças propostas, em ordem
| Etapa | Mudança | Alcance / impacto | Recuperação e verificação |
| --- | --- | --- | --- |
| 1 | Fechar comparação técnica, ADRs, backlog, plano de ambiente e README; conferir documentos ativos/modelos | Apenas arquivos desta pasta; sem aplicação | Leitura de versões, referências e aprovação; manter decisões/entrevista/diagnóstico e modelos usados |
| 2 | Confirmar nome/email de autoria do commit | Identidade Git somente local ao projeto, se configuração for necessária; não mudar global | Conferir identidade antes do commit; email no-reply do GitHub é opção, não inventar endereço |
| 3 | Revalidar remoto vazio; inicializar Git em main e revisar exatamente o que será versionado | Cria .git local; conferir .gitignore, segredos e arquivos do commit | Nenhum reset, exclusão ou força; se histórico remoto novo surgir, parar bootstrap e revisar |
| 4 | Criar primeiro commit documental | Sugestão de mensagem: docs: registra especificações e planejamento inicial do GameVault 2.0 | Conferir conteúdo e ID real; nenhum diretório de aplicação ou dependência instalada neste commit |
| 5 | Configurar origin no destino confirmado, publicar main inicial e criar/publicar develop a partir do mesmo commit | Exceção exclusiva de bootstrap de repositório vazio, com alcance explicitamente aprovado antes da execução | Conferir URLs sem credenciais, hashes locais/remotos e branches; sem force-push ou merge |
| 6 | Executar/verificar Action documental existente | Workflow já fornecido; sem teste de produto ou deploy | Conferir execução real e nome do check; falha documental deve ser corrigida em feature após bootstrap |
| 7 | Proteger main/develop conforme seção seguinte | Alteração de regras/permissões do repositório | Releitura da configuração e teste limitado de PR; usuário faz qualquer merge; sem alegar proteção apenas pelo AGENTS.md |
| 8 | Criar Issues autorizadas e usar Project criado/configurado manualmente pelo usuário | Recursos rastreáveis apenas do GameVault; sem ampliar escopo da CLI | Conferir somente o link fornecido e distinguir campos visíveis de configurações ainda não verificadas |
| 9 | Criar primeira feature de develop apenas quando houver tarefa autorizada | Trabalho posterior por PR feature → develop; versões por PR develop → main | Sem push direto futuro em main/develop; merges sempre manuais |

## Regras concretas propostas para main/develop
- Exigir pull request; bloquear force-push e exclusão das branches.
- Aplicar regras também a administradores, sem bypass operacional do agente.
- Exigir o check documental somente depois de confirmar o nome em execução real; depois incorporar os checks de produto que de fato existirem.
- Exigir resolução de conversas. Não habilitar auto-merge.
- Projeto individual: não exigir aprovação impossível de obter do próprio autor. Manter revisão e merge manuais do usuário; se houver outro revisor disponível, revisar o número de aprovações exigidas antes de alterar a regra.
- Não impor histórico linear se o fluxo escolhido admitir commits de merge. Não configurar deploy, ambiente público ou chave de publicação.

Repositórios públicos têm proteção de branch no GitHub Free conforme [documentação GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches). A disponibilidade na conta e a aplicação real das regras ainda serão verificadas; este documento não certifica proteção ativa.

## Issues e Project propostos
Um Project GameVault 2.0 com Backlog, Pronta, Em andamento, Em revisão e Concluída; campos prioridade, fase, requisito e dependências conforme recursos disponíveis. Issues usam os IDs TASK locais e ligam REQ/DEC/ADR; sem implementar todas automaticamente por existirem no Project. Revisar permissões do Project separadamente se a ferramenta solicitar acesso adicional.

## Passos manuais se a ferramenta não permitir
Após existir main/develop, no repositório abrir Settings e a área de branches/regras disponível; criar regras para ambas conforme lista acima e conferir sua aplicação. Criar o Project pela área Projects da conta e vinculá-lo ao repositório. Quando não houver acesso à tela/opção, registrar a limitação exata e pedir somente a ação necessária; não declarar configuração concluída por instrução fornecida.

## Aprovação e pendências
Autorização operacional: DEC-024, solicitação explícita de configurar GitHub/Git Flow/proteções, destino público confirmado e mensagem subsequente aprovando stack/ADRs e pedindo preparação/primeiro commit antes do código. Identidade no-reply confirmada em resposta própria. Não foi inferida autorização de aplicação ou de instalação do Docker. O plano foi tornado concreto antes da execução; evidências de cada ação serão registradas, sem reconfirmar o mesmo alcance por comando. Respeitar permissões de execução do ambiente; merges continuam exclusivamente manuais.

Preparo concluído: produto/stack/ADRs aprovados, README atualizado, limpeza revisada sem arquivos descartáveis, identidade confirmada, Git local inicializado e acesso pelo conector GitHub verificado. Publicação/regras executadas; Project criado manualmente e parcialmente conferido abaixo. Planos/tarefas de aplicação não são autorizados em bloco por existirem em Issues/Project.

## Resultado da execução do bootstrap
Primeiro commit 263c7bb publicado; main/develop no mesmo SHA inicial e protegidas com PR/check documental e bloqueio de força/exclusão, inclusive administradores. Actions documentais passaram em ambas. Issue #1 criada; evidências seguintes em feature/docs-bootstrap-evidencias por PR, sem merge do agente. Resultado detalhado em [EVIDENCIAS-BOOTSTRAP](EVIDENCIAS-BOOTSTRAP.md).

A consulta inicial pela CLI falhou por falta de escopo. Usuário cancelou a autorização adicional e escolheu criação manual (DEC-029); o comando de ampliação anteriormente sugerido não é próximo passo autorizado. Project pessoal informado: [GameVault 2.0 #2](https://github.com/users/geovanegalan/projects/2). Leitura pública no navegador, sem login, confirmou título, cinco estados e campos Prioridade/Fase/Requisito/Dependências. Issue #1 está Em andamento; PR #2 não apareceu no quadro. Tipos/opções e repositório padrão não conferidos; não declarar configuração completa por inferência.

## Histórico operacional
- v0.1: bootstrap e proposta inicial de criação por ferramenta, antes de confirmar a limitação de escopo.
- v0.2: incorpora escolha explícita de Project manual, cancelamento da ampliação de acesso e link/conferência pública. Não modifica Git Flow ou permissões de merge; preserva histórico sem consultar outras organizações.

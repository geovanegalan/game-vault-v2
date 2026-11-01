# Referências do bootstrap
Consultadas em 2026-11-01 para formato e descoberta das instruções locais:
- Skills oficiais: https://learn.chatgpt.com/docs/build-skills — SKILL.md com name/description, descoberta em .agents/skills e invocação.
- Instruções oficiais: https://learn.chatgpt.com/docs/agent-configuration/agents-md — instruções do projeto em AGENTS.md.

Os gates de aprovação, a tutoria e o fluxo main/develop/feature são convenções deste projeto solicitadas pelo usuário. Não são requisitos universais do Codex. As tecnologias e funcionalidades do contexto são propostas. Este kit não confirma versões da stack nem recursos específicos de um plano GitHub; verificar documentação oficial quando configurá-los.

## Catálogo — pesquisa inicial de 01/11/2026
- RAWG: https://rawg.io/apidocs — chave, planos e atribuição; https://rawg.io/tos_api — termos da API. Descrições de uso comercial entre páginas/seções não foram tratadas como equivalentes sem esclarecimento.
- IGDB: https://api-docs.igdb.com/#account-creation e https://api-docs.igdb.com/#authentication — uso não comercial, cadastro Twitch/aplicação e autenticação com token.
- Resultado e limites em `catalogo/COMPARACAO.md` v0.1. Pesquisa documental não comprova funcionamento, acesso concedido, direitos irrestritos de imagens ou aprovação de provedor. Nenhuma consulta autenticada realizada.

## Stack, arquitetura e preparação — 01/11/2026
Pesquisa primária para COMPARACAO-STACK v0.1 e ADR-001/002 v0.1, ainda propostas:
- [Angular: compatibilidade](https://angular.dev/reference/versions), [suporte](https://angular.dev/reference/releases) e [testes](https://angular.dev/guide/testing).
- [Nest: migração atual](https://docs.nestjs.com/migration-guide) e [testes](https://docs.nestjs.com/fundamentals/testing).
- [Prisma 7: requisitos](https://www.prisma.io/docs/orm/v7/reference/system-requirements), [bancos suportados](https://www.prisma.io/docs/orm/v7/reference/supported-databases), [estado do quickstart atual](https://www.prisma.io/docs/prisma-orm/quickstart/postgresql).
- [PostgreSQL: política de versões](https://www.postgresql.org/support/versioning/), [SQLite: usos](https://sqlite.org/whentouse.html) e [node-postgres: consultas](https://node-postgres.com/features/queries).
- [npm: workspaces](https://docs.npmjs.com/cli/v12/using-npm/workspaces/), [Express 5](https://expressjs.com/en/guide/migrating-5/) e [Playwright](https://playwright.dev/docs/intro).
- [Compose](https://docs.docker.com/compose/), [Docker Desktop Windows](https://docs.docker.com/desktop/setup/install/windows-install/) e [oferta pessoal](https://www.docker.com/products/personal/).
- [OWASP: sessões](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), [senhas](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html), [autenticação](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html).
- [GitHub: branches protegidas](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [OpenAI: plugins](https://learn.chatgpt.com/docs/plugins) e [MCP](https://learn.chatgpt.com/docs/extend/mcp).

Requisitos publicados não são build conjunto testado. Planos gratuitos/licenças não foram tratados como gratuidade irrestrita. Conexão CLI ao repositório foi verificada separadamente; conexão MCP e proteções ativas não foram declaradas sem evidência.

## Preparação após aprovação técnica — 01/11/2026
- [Docker Desktop 4.97.0](https://docs.docker.com/desktop/release-notes/#4970), release de 26/10/2026; [instalação/permissões Windows](https://docs.docker.com/desktop/setup/install/windows-permission-requirements). Instalação proposta em ambiente/PLANO-AMBIENTE.md v0.1, não executada.
- [Formato oficial do email no-reply](https://docs.github.com/en/account-and-profile/reference/email-addresses-reference) e [configuração por repositório](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address?platform=windows). Usuário escolheu no-reply; ID/login confirmados pela API.
- [API de proteção de branches](https://docs.github.com/en/rest/branches/branch-protection#update-branch-protection), consultada antes de configurar. Resultados devem ser registrados após execução real.
- Conector GitHub disponibilizado durante esta etapa; consultas de login/repositório confirmaram conexão e acesso, atualizando o estado anterior de plugin apenas sugerido.

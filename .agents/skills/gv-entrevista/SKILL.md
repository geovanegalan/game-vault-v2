---
name: gv-entrevista
description: Conduzir entrevista e refinamento de requisitos do GameVault antes de aprovar visão, PRD ou MVP.
---

# Entrevista de requisitos
Leia AGENTS.md, contexto, status e registro de decisões. Leia sessões anteriores antes de repetir perguntas. Se o usuário fornecer legado, faça inventário somente leitura e diferencie comportamento observado do desejado.

Comece com um bloco curto de até três perguntas sobre objetivo, aprendizado e legado disponível; adapte os próximos blocos às respostas. Ofereça exemplos como alternativas, nunca como decisões já tomadas. Não faça toda a entrevista de uma vez.

Explore jornadas, regras, erros, privacidade e restrições usando o contexto como roteiro. Questione prioridades: qual problema cada funcionalidade resolve, qual custo traz e como validar valor com menos escopo? Discuta especialmente review pública versus rede de amigos, fonte do catálogo, autenticação, estados/notas e migração. Não force backend ou frontend primeiro.

Inclua uma entrevista técnica progressiva: experiência do usuário com TypeScript, Angular, backend, SQL e testes; sistema operacional e ferramentas observadas no diagnóstico; objetivos de aprendizado; prazo, orçamento e hospedagem; preferência por reaproveitar ou reescrever; estrutura do projeto e integrações necessárias. Use gv-planejamento para comparar alternativas de stack quando houver contexto suficiente. A discussão pode ocorrer antes do PRD completo, mas escolhas continuam propostas até confirmação. Não confunda tecnologia já instalada com tecnologia adequada ao projeto.

Registre respostas em docs/entrevista/SESSOES.md. Ao ter informação suficiente, redija ou revise VISAO.md, PRD.md e MVP.md em docs/ e apresente uma proposta versionada, com pendências e tradeoffs. Preserve aprovações anteriores e submeta mudanças materiais a nova aprovação. Peça aprovação concreta do conteúdo; aprovação parcial vale apenas para os itens explicitados. Atualize registro e status com evidência. Não implemente durante esta skill.

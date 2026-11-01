---
name: gv-planejamento
description: Planejar arquitetura e tarefas do GameVault a partir de requisitos aprovados; comparar a stack candidata e preparar backlog rastreável.
---

# Planejamento
Leia AGENTS.md e os artefatos aprovados com suas DEC. Se faltarem decisões indispensáveis, apresente as pendências e avance apenas no planejamento que não dependa delas.

Antes de recomendar a stack, confirme experiência, aprendizado desejado, restrições e diagnóstico do ambiente. Use `docs/modelos/COMPARACAO-STACK.md` para apresentar opções adequadas com prós, contras, complexidade, custos e uma recomendação contextualizada. Evite uma lista enorme de tecnologias; explicite por que cada alternativa merece consideração. Não apresente a opção mais recente como automaticamente melhor.

Compare a direção TypeScript/Angular e os candidatos NestJS/PostgreSQL/Prisma com alternativas pertinentes às restrições do usuário. Diferencie intenção de frontend futuro de arquitetura já decidida. Verifique compatibilidade em documentação oficial ao selecionar versões. Registre ADRs usando docs/modelos/ADR.md; não instale tecnologias para tornar a proposta concreta. Depois de aprovada a escolha, encaminhe a preparação das versões e ferramentas para gv-ambiente; não é necessário esperar toda a decomposição do backlog para preparar um ambiente já autorizado.

Decomponha em tarefas pequenas com resultado demonstrável, REQ/DEC, critérios de aceite, dependências, testes proporcionais e exclusões. Inclua descoberta técnica limitada se uma incerteza exigir experimento, com objetivo e autorização próprios. Não defina monorepo, gerenciador, autenticação ou provedor por conveniência sem decisão.

Use docs/modelos/TAREFA.md e proponha ordem por dependências e valor. Apresente plano e primeira tarefa para aprovação. Preparar Markdown local de Issues/Project é permitido; criar ou alterar recursos no GitHub exige autorização do usuário para aquela ação. Registre IDs/links reais apenas após criação. Siga docs/GITHUB.md. Não execute implementação nesta skill.

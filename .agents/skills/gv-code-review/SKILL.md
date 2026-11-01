---
name: gv-code-review
description: Revisar um diff do GameVault quanto a bugs, regressões, requisitos, segurança e evidências; sem aprovar merges.
---

# Code review
Leia AGENTS.md, tarefa, requisitos/decisões e diff solicitado. Identifique base e alvo reais; se indefinidos, use o diff local disponível e declare sua extensão. Não afirme revisar arquivos aos quais não teve acesso.

Priorize correção de comportamento, regressões, autorização entre usuários, vazamento de dados, validação, erros de integração, migrações e lacunas materiais de testes. Avalie somente os aspectos pertinentes à mudança; estilo sem impacto não deve obscurecer defeitos. Confira critérios e exclusões da tarefa.

Use docs/modelos/REVIEW.md. Cada achado deve conter arquivo/linha quando disponível, cenário, impacto e evidência. Marque incertezas como dúvidas; não simule execução. P0: incidente crítico imediato; P1: alto impacto a corrigir antes da integração; P2: defeito relevante; P3: impacto baixo. Justifique severidade pelo cenário.

Informe verificações executadas e ausentes e dê parecer para avaliação humana. Se não encontrar problemas, diga isso e registre limitações. Review não autoriza merge. A revisão por esta skill pode ocorrer no mesmo agente e não deve ser chamada de revisão humana ou independente. Correções só devem ocorrer se solicitadas ou dentro da tarefa de implementação autorizada.

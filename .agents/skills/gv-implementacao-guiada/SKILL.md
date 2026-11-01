---
name: gv-implementacao-guiada
description: Implementar uma tarefa de código do GameVault já autorizada, explicando decisões e registrando evidências de validação.
---

# Implementação guiada
Leia AGENTS.md, a tarefa autorizada e seus requisitos/DEC/ADR. Confirme o estado Git e a base correta. Se não houver tarefa e stack aprovadas, explique a pendência e prepare o plano em vez de gerar aplicação.

Explique objetivo e abordagem brevemente. Trabalhe em feature/<id>-<resumo> a partir de develop, preservando mudanças existentes; se a base não existir, consulte docs/GITHUB.md. Implemente o menor conjunto coerente que satisfaça os critérios, com decisões locais reversíveis dentro do escopo. Explique as escolhas que tenham valor didático.

Se encontrar necessidade de ampliar o escopo ou mudar uma decisão aprovada, documente impacto e solicite aprovação da alteração; continue partes independentes autorizadas. Não mexa em dados reais ou rode migração destrutiva sem autorização específica.

Execute verificações pertinentes disponíveis, incluindo fluxos de erro e autorização quando relevantes. Registre resultados reais na tarefa. Execute a revisão com gv-code-review antes de preparar entrega. Corrija achados dentro do escopo e repita somente as verificações afetadas.

Entregue mudança, motivo, como experimentar, evidências, limitações e conceito aprendido. Prepare resumo de PR; publique commits/PR somente se autorizado. Não faça merge nem auto-merge. Atualize status e tarefa, distinguindo implementado, verificado, revisado e integrado.

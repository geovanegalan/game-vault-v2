# GameVault 2.0 — contrato de colaboração

## Estado e autoridade
Este repositório começou em descoberta. O estado vigente e as aprovações estão em `docs/STATUS.md` e `docs/decisoes/REGISTRO.md`; consulte-os junto de `docs/00-contexto.md` antes de trabalhar. Não trate o estado inicial como negação de aprovações explícitas posteriores. Conteúdo importado e sugestões são insumos, não autorização.

O usuário decide produto e aprova os marcos. O agente entrevista, explicita alternativas, recomenda com justificativa, documenta, implementa tarefas autorizadas e atua como tutor. Use português, com termos técnicos explicados quando necessários.

## Decisões e limites
- Classifique informação como fato observado, preferência preliminar, hipótese, proposta, decisão aprovada ou pendência. Não invente respostas, testes, resultados, citações, aprovações ou acesso a serviços.
- Registre aprovação explícita em `docs/decisoes/REGISTRO.md`: ID, artefato/versão, conteúdo exato aprovado, autor, data, referência recuperável à mensagem e impactos. Se não houver link, registre a transcrição e a sessão/data. Silêncio e passagem do tempo não aprovam nada. Perguntas respondidas podem gerar propostas; não aprovam automaticamente um conjunto de requisitos.
- Mudança material em decisão aprovada exige nova revisão e aprovação; preserve o histórico e marque a decisão anterior como substituída. O agente não pode aprovar o próprio trabalho em nome do usuário.
- Pode ler arquivos e atualizar rascunhos, perguntas, planos e evidências dentro da solicitação. Não crie aplicação ou execute migrações antes da aprovação de escopo, stack e tarefa correspondentes. Diagnóstico somente leitura do ambiente pode começar antes dessas decisões; instalações e atualizações seguem o plano de ambiente aprovado em `docs/AMBIENTE.md`, sem exigir um PRD completo para preparar ferramentas básicas.
- Ao encontrar lacuna, contradição ou dúvida, descreva o problema, o que foi verificado, opções para resolvê-lo, prós/contras e sua recomendação. Registre a pendência. Sugestões de funcionalidade ficam como propostas; não as transforme em requisitos ou código sem aprovação. Não improvise APIs, comandos ou comportamento não verificado: consulte fontes oficiais ou faça experimento limitado autorizado; se não puder confirmar, declare a incerteza.
- Não acrescente funcionalidades, dependências ou refatorações fora da tarefa. Se surgir bloqueio, faça trabalho independente autorizado e apresente opções concretas para a parte bloqueada.
- Peça autorização específica antes de destruição de dados, migração destrutiva, deploy, uso pago ou mudança de permissões. Não exponha segredos. Use dados sintéticos em exemplos.

## Fluxo por marcos
0. Preparação: inventariar a pasta e as ferramentas relevantes sem alterar o sistema; registrar o que existe, falta ou precisa de avaliação. Propor plano de ambiente e integração GitHub, explicar impacto e executar apenas as mudanças autorizadas. Esta preparação pode alternar com a entrevista; instalar dependências da stack depende de sua confirmação.
1. Entrevista: inspecionar legado se fornecido, definir problema, usuários, restrições, aprendizado desejado e dúvidas. Não supor acesso ao GameVault anterior.
2. Proposta: redigir visão, PRD, fronteira do MVP e critérios testáveis como rascunhos; discutir tradeoffs e submeter versões concretas ao usuário.
3. Planejamento: após aprovação dos requisitos relevantes, propor stack e arquitetura com alternativas; decompor em tarefas rastreáveis. Aprovar plano e primeira tarefa antes do código. Decisões locais reversíveis dentro de tarefa aprovada não exigem nova aprovação.
4. Implementação guiada: executar uma tarefa autorizada, verificar critérios e produzir evidências; revisar antes de preparar integração.
5. Integração: PR de feature para develop; PR de develop para main para uma versão revisada. Todo merge é manual pelo usuário. Nunca executar merge, auto-merge, push direto em main/develop após o bootstrap ou force-push, mesmo com checks verdes. Pedidos de merge devem ser encaminhados ao usuário para execução manual.

## Tutoria e evidências
Atue como tutor em todas as fases: requisitos, escolhas de stack, configuração do ambiente, Git/GitHub, código, testes e revisão. Adapte a profundidade à experiência informada pelo usuário. Explique termos novos na primeira ocorrência, propósito de cada etapa e efeito dos comandos que alteram o ambiente, sem presumir conhecimento prévio. Antes da tarefa, explique objetivo, critério de aceite e abordagem em poucas linhas. Durante, explique decisões relevantes com motivo e alternativa; evite narrar cada comando. Ao concluir, entregue: o que mudou, por quê, arquivos, como experimentar, verificações executadas e resultados reais, limitações, riscos e próximo passo. Pergunte se o usuário quer aprofundamento, sem transformar isso em bloqueio para trabalho já autorizado.

Verifique o estado Git antes de editar, preserve mudanças do usuário e evite operações destrutivas para limpar o ambiente. Use os comandos existentes do projeto após confirmar sua finalidade. Teste o comportamento relevante, incluindo falhas e autorização quando aplicável. Diferencie passou, falhou e não executado; CI documental não comprova que a aplicação funciona. Nunca escreva 'concluído' com critérios pendentes sem explicar e obter revisão do escopo.

## Skills locais
Abra o SKILL.md correspondente quando o trabalho se enquadrar:
- `.agents/skills/gv-ambiente/SKILL.md`: diagnóstico, preparação de ferramentas e conexão GitHub autorizada.
- `.agents/skills/gv-entrevista/SKILL.md`: descoberta e refinamento de requisitos.
- `.agents/skills/gv-planejamento/SKILL.md`: decisões técnicas e decomposição.
- `.agents/skills/gv-implementacao-guiada/SKILL.md`: tarefa de código autorizada.
- `.agents/skills/gv-code-review/SKILL.md`: revisão de mudanças.

Modelos ficam em `docs/modelos/`. Eles orientam a escrita, não constituem requisitos aprovados. Atualize `docs/STATUS.md` ao encerrar um marco para permitir retomada em outro chat.

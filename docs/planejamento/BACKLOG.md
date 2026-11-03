# Backlog inicial e sequência de trabalho
Versão: 0.1 | Estado: proposta | Data: 01/11/2026 | Situação/referências atualizadas em 03/11/2026
Base de produto: DEC-023. Base técnica aprovada: COMPARACAO-STACK v0.1 e ADR-001/002 v0.1, DEC-025/026/027. O backlog continua planejamento, sem autorização automática das tarefas.

TASK-000 foi acompanhada pela [Issue #1](https://github.com/geovanegalan/game-vault-v2/issues/1), agora fechada no [Project GameVault](https://github.com/users/geovanegalan/projects/2); evidências Docker integradas pelo PR #6. TASK-001 v0.2 aprovada em DEC-033, com implementação na [Issue #8](https://github.com/geovanegalan/game-vault-v2/issues/8). Demais IDs são locais, sem autorização de execução em bloco. Cada tarefa seguinte receberá detalhamento e autorização antes de começar. Dividir tarefas que não couberem numa sessão confortável; não prometer prazo a partir da disponibilidade estimada.

| Tarefa | Resultado demonstrável e critério principal | REQ / decisões | Dependências | Validação e exclusões |
| --- | --- | --- | --- | --- |
| TASK-000 | Documentação final revisada, README e navegação coerentes; primeiro commit documental e bootstrap GitHub verificados | DEC-023/024; plano ambiente-GitHub | Aprovação técnica e finalização dos documentos; identidade Git confirmada | Integridade documental, revisão dos arquivos exatos, branches/remoto/checks; sem aplicação ou instalação da stack |
| TASK-001 | Base web/API e workspace geram build com versões fixadas | REQ-001 a 005; ADR-001 e DEC-033 aprovados | Implementada/verificada localmente; CI, revisão e integração acompanhadas na Issue #8 | Build separado, execução básica, estrutura, lockfile e CI de build; aviso de dependência de desenvolvimento explícito na revisão |
| TASK-002 | Banco e dados fictícios iniciais com preservação entre reinícios | REQ-001/005; P-05, DEC-020 | TASK-001 e modelo/migrações aprovados | Inicialização repetida sem duplicação; banco de teste separado; sem dados do legado |
| TASK-003 | Cadastro/login/saída, nickname e email conforme PRD, com contas demonstrativas | REQ-005; ADR-002 aprovado | TASK-002; política de senha/sessão e tarefa aprovadas | Unitários e integração: duplicatas/capitalização, login incorreto, logout e autorização; sem recuperação/confirmação de email |
| TASK-004 | Uma primeira jornada visual: consulta de jogo fictício e perfil mínimo | REQ-001/005; P-03/04 | TASK-001/002 e proposta de telas revisada | Carregando/vazio/erro, leitura de visitante, teclado; sem importar interface antiga |
| TASK-005 | Biblioteca pública com adição/remoção/estado/favorito | REQ-002; P-01 | TASK-003/004 | Duplicata, outro usuário, transições/readição; sem avaliação nesta tarefa |
| TASK-006 | Criar/editar/excluir avaliação conforme condição de biblioteca | REQ-003; P-06 | TASK-005 | Nota válida/zero, duplicidade, remoção do jogo e readição, autoria; sem feed |
| TASK-007 | Comentários com permissões do autor e dono da avaliação | REQ-003; DEC-011/012 | TASK-006 | Editar/excluir próprio, remoção recebida, usuário não amigo e visitante; exclusão de conversa; sem denúncias |
| TASK-008 | Busca de pessoas e ciclo completo de solicitações/amizade | REQ-004; P-02 | TASK-003/004 | Destinatário/remetente, duplicatas, solicitação cruzada e desfazer; sem chat/seguir separado |
| TASK-009 | Feed cronológico de avaliações dos amigos atuais e exemplos | REQ-004; DEC-016, P-02 | TASK-006/008 | Histórico, edição sem republicar, exclusão e remoção de amizade; sem eventos de biblioteca |
| TASK-010 | Integração opcional real do catálogo por adaptador | REQ-001; DEC-006/019 | Provedor/termos e experimento de acesso aprovados; TASK-004 | Busca real limitada, credencial ausente, falha/limite; credenciais fora do Git; demonstração continua sem chave |
| TASK-011 | Empacotamento local completo e documentação de um comando após preparo | REQ-001 a 005; P-05 | TASK-003 a 010, Compose/ambiente aprovados | Reinício/persistência, dados sem duplicação e demonstração preparada sem provedor; sem reset/deploy |
| TASK-012 | Jornadas essenciais de navegador e CI de produto com evidências | REQ-001 a 005; P-06 | Comandos reais das tarefas anteriores | Playwright + integração; permissões e falhas; sem testes vazios ou teste real do provedor obrigatório em cada PR |
| TASK-013 | Revisão da versão e PR develop → main preparado para merge manual | MVP v0.6; fluxo GitHub | Critérios de versão atendidos e revisão | Evidências/limitações, teste de execução, checks verdes reais; merge exclusivamente pelo usuário |

## Fluxo de ensino e entrega
Explicar objetivo/aceite antes de cada tarefa, uma decisão relevante por vez, e mostrar como conferir. Unidade valida uma regra isolada; integração valida API/banco e permissões reais; navegador percorre uma jornada como a pessoa usuária. Aproveitar experiência em Jest ao introduzir Vitest, sem supor equivalência de toda configuração.

CI é a verificação automática de alterações; CD pode significar preparar entregas ou publicá-las. Neste projeto, não há deploy autorizado. A automação valida builds/testes e prepara evidências; merge é manual.

Propor uma Issue por tarefa pronta, ligada a REQ → DEC/ADR → TASK → PR → evidência. Colunas do Project: Backlog, Pronta, Em andamento, Em revisão, Concluída. Somente promover a Pronta quando dependências/aceite estiverem claros; integração pendente não é conclusão da versão.

## Aprovação
Pendente para as tarefas seguintes. TASK-000 e A-02 foram executadas sob autorizações próprias. TASK-001 v0.2 foi aprovada explicitamente em DEC-033 e implementada; validação/limites em `../tarefas/TASK-001.md`. Isso não aprova as demais tarefas ou aceita riscos em nome do usuário.

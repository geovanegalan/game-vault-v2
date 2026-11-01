# Fronteira do MVP do GameVault 2.0
Versão: 0.6 | Data: 01/11/2026 | Estado: aprovado pelo usuário em 01/11/2026 (DEC-023)
Base: VISAO v0.3, PRD v0.6 e DEC-001 a DEC-023. As regras P-01 a P-06 do PRD foram aprovadas explicitamente junto do conjunto. Textos de proposta abaixo preservam a elaboração; aprovação vigente em DEC-023.

## Primeira versão proposta
| Área | Recorte | Estado e referência |
| --- | --- | --- |
| Catálogo | Demonstração sem chave, com opção de configurar API externa para buscar jogos reais | DEC-006/019/020; consulta e distinção entre modos propostas em P-04; provedor separado |
| Biblioteca | Pública; estados quero jogar, jogando, pausado, concluído e abandonado; inicial quero jogar, mudança livre; favorito independente; remover jogo preserva avaliação/comentários | DEC-005/008/010/014; duplicatas, readição e favorito propostos em P-01 |
| Avaliações | Públicas; 0 a 5 com meias estrelas e texto opcional; uma por pessoa/jogo; criar/editar exige jogo na biblioteca; leitura/exclusão preservadas após remover jogo; excluir avaliação remove comentários | DEC-004/008/009/010/011/015/017; texto/erros/confirmação propostos em P-06 |
| Comentários | Qualquer usuário autenticado comenta; autor edita/exclui o próprio; dono da avaliação remove recebidos | DEC-010/012; texto e validação propostos em P-06 |
| Comunidade | Busca por nickname e ciclo de solicitações/amizade; sem seguir separado; feed de novas avaliações dos amigos e exemplos, mais recentes primeiro | DEC-002/016/021; solicitações inválidas, histórico e edição no feed propostos em P-02 |
| Conteúdo editorial | Novidades e avisos com exemplos identificados como demonstração | Escolha pontual DEC-003; sem integração automática de notícias |
| Acesso e perfis | Cadastro/login com email único/senha e nickname único escolhido no cadastro, distinguindo maiúsculas/minúsculas; perfil público; saída | DEC-010/013/018; formato/campos/saída propostos em P-03; sem recuperação/confirmação de email (DEC-022) |
| Demonstração local | Jogos, contas e atividades fictícios; modo sem chave e execução documentada; API opcional para busca real; sem importar banco anterior | DEC-013/019/020; preparo inicial, persistência e uso local propostos em P-05 |

## Complementos que integram a revisão do conjunto
Consultar o texto completo e os critérios no PRD v0.6:
- P-01: só titular altera biblioteca; sem duplicatas; readição começa em quero jogar/sem favorito, preservando avaliação.
- P-02: permissões das solicitações; feed das amizades atuais inclui avaliações anteriores; edição não republica ou reposiciona avaliação; desfazer amizade remove seus itens do feed.
- P-03: nickname de 3–20 caracteres (letras sem acento, números e sublinhado), capitalização preservada e sem edição nesta versão; email comparado sem capitalização e com espaços externos removidos; perfil mínimo e saída da conta.
- P-04: leitura pública de catálogo/detalhes/perfis/bibliotecas/avaliações; modo demonstrativo padrão; catálogo mostra informações básicas disponíveis e não substitui falha real por dados fictícios silenciosamente.
- P-05: dados por instalação e persistentes; no mínimo duas contas de exemplo; demonstração preparada funciona sem provedor; um comando inicia após pré-requisitos; não há reset automático.
- P-06: texto simples (avaliação até 5.000, comentário até 1.000 caracteres), confirmação ao excluir avaliação, mensagens de erro, uso por teclado/celular/desktop e verificação de permissões.

Estes complementos são recomendações novas e podem ser ajustados. Aprovar apenas as decisões anteriores não aprova automaticamente estes itens.

## Depois ou indefinido
- Upload de screenshots: adiado explicitamente, DEC-007; não implica adiar capas do catálogo.
- Recuperação de senha e confirmação de email: adiadas explicitamente, DEC-022.
- Chats e grupos: citados como possibilidades futuras pelo usuário; nenhum compromisso de implementação.
- Links para lojas: possibilidade, sem inclusão aprovada.
- Likes, notificações, dashboard, diário, importação Steam, ferramentas administrativas e filtros avançados: sem inclusão autorizada. Não criar por iniciativa própria.

## Fora da finalidade declarada
Iniciar jogos e realizar compras dentro da aplicação. Sem hospedagem paga; demonstração local não representa uma comunidade online compartilhada.

## Como verificar a entrega proposta
Critérios a executar quando houver aplicação; não foram testados nesta etapa:
1. Seguir instruções de preparo, iniciar demonstração sem chave e entrar com conta fictícia ou cadastrar uma conta.
2. Buscar jogo demonstrativo, adicionar em quero jogar, mudar estado e marcar favorito sem duplicar entrada.
3. Publicar avaliação e comentário com permissões corretas; remover jogo preserva conversa; editar exige readição; excluir avaliação remove comentários mediante confirmação.
4. Experimentar solicitações, amizade e feed cronológico usando as contas fictícias; ações fora das permissões falham sem alterar dados.
5. Reiniciar preserva alterações sem duplicar dados; leitura pública não expõe email/credenciais. Cadastro respeita email único e nicknames que diferenciam capitalização.
6. Após escolher provedor e configurar acesso próprio, verificar busca real e suas falhas, sem apresentar dados fictícios como resposta real. Sem esse teste, declarar a integração real não verificada, sem considerar o produto inteiro validado só pelo modo demonstrativo.

## Próximo marco e limites da aprovação
Aprovado explicitamente como MVP v0.6 com VISAO v0.3 e PRD v0.6, incluindo P-01 a P-06 (DEC-023). Próximo marco: comparar stack/arquitetura, confirmar provedor e propor tarefas rastreáveis. Stack, arquitetura, primeira tarefa e plano de ambiente terão aprovações próprias. Nenhum trabalho de aplicação autorizado ou executado. Somente metadados de aprovação atualizados após o aceite, sem mudança de conteúdo normativo.

## Histórico do rascunho
- v0.1: fronteira parcial inicial.
- v0.2: incorpora as escolhas pontuais DEC-008 a DEC-010; não altera a ausência de aprovação da fronteira completa.
- v0.3: incorpora DEC-011 a DEC-013: exclusão da avaliação/comentários, manutenção de comentários e acesso com nickname único/contas de demonstração. Fronteira completa ainda não aprovada.
- v0.4: incorpora DEC-014 a DEC-016: biblioteca com estado inicial/mudança livre, inclusão prévia para avaliar e conteúdo/ordem do feed. Fronteira completa ainda não aprovada.
- v0.5: incorpora DEC-017 a DEC-019: edição exige readição, email único/nicknames com capitalização distinta e modo demonstrativo sem chave com API opcional. Fronteira completa ainda não aprovada.
- v0.6: incorpora DEC-020 a DEC-022 e complementos P-01 a P-06 como primeira proposta consolidada para revisão, sem alegar aprovação ou validação da aplicação.

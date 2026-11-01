# PRD do GameVault 2.0
Versão: 0.6 | Data: 01/11/2026 | Estado: aprovado pelo usuário em 01/11/2026 (DEC-023)
Base: `VISAO.md` v0.3; entrevista e DEC-001 a DEC-023. Complementos P-01 a P-06 aprovados explicitamente junto do conjunto em DEC-023. Não autoriza código.

## Problema, público e jornadas
Público geral interessado em jogos; entrega inicial local para portfólio. Jornada candidata: cadastrar-se ou entrar com conta de demonstração, encontrar um jogo real, adicioná-lo à biblioteca, organizar seu estado/favorito, avaliar e trocar experiências com pessoas por amizades e comentários. Detalhes de acesso e preparação dos dados ainda precisam de especificação.

## Escopo proposto e exclusões
Fronteira proposta em `MVP.md` v0.6. Não importar requisitos ou implementação do legado. Stack, arquitetura e distribuição dependem de análise e aprovação próprias. O escopo de produto inclui busca, biblioteca, avaliações/comentários, amizade/feed e acesso/perfis; detalhes complementares abaixo são submetidos junto desta versão.

## Requisitos em refinamento
Os critérios abaixo são exemplos para futura validação, não testes executados. Prioridade proposta: primeira versão para os cinco requisitos; autorização, erros e pendências devem ser resolvidos antes de uma tarefa correspondente.

### REQ-001 — Buscar jogos reais
- Necessidade: encontrar jogos para conhecer e adicionar à biblioteca. Origem: DEC-006 e DEC-019.
- Regras confirmadas: modo de demonstração sem chave e opção de configurar API externa para busca real; provedor não decidido.
- Critério proposto: busca por nome apresenta resultados do provedor escolhido; ausência de resultados é distinguível de falha de conexão.
- Casos de erro a especificar: falta de configuração, provedor indisponível, limite de uso e jogo indisponível. Não afirmar esses comportamentos como implementados.
- Critério derivado para revisão: ausência de chave não impede experimentar no modo de demonstração; busca real depende da configuração própria e não é apresentada como realizada no modo demonstrativo.
- Regra confirmada adicional: dados fictícios identificados no modo demonstrativo, sem importar o banco anterior (DEC-020).
- Autorização/visibilidade e detalhes dos modos propostos em P-04/05. Dependências técnicas abertas: provedor compatível com orçamento zero, termos, imagens e configuração; a escolha posterior não pode mudar o comportamento aprovado sem revisão.

### REQ-002 — Organizar biblioteca
- Necessidade: acompanhar intenção e progresso de jogo. Origem: DEC-005, DEC-008, DEC-010 e DEC-014.
- Regras confirmadas: um estado por jogo entre quero jogar, jogando, pausado, concluído e abandonado; favorito independente; remover jogo da biblioteca preserva sua avaliação e comentários; biblioteca pública.
- Critério derivado para revisão: mudar um jogo de jogando para concluído não muda sua marcação de favorito.
- Casos de erro propostos: duplicata e jogo inexistente, com resultado ainda a definir.
- Critério derivado para revisão: remover um jogo que tem avaliação comentada retira a entrada da biblioteca, preservando a avaliação e os comentários.
- Regra confirmada adicional: jogo adicionado começa em quero jogar; mudança livre entre estados (DEC-014).
- Critério derivado para revisão: adicionar jogo novo o exibe em quero jogar; mudar diretamente para abandonado é permitido, sem exigir estados intermediários.
- Leitura pública confirmada em DEC-010. Permissão de alteração, duplicatas, favorito fora da biblioteca e readição propostos em P-01.

### REQ-003 — Avaliar e comentar
- Necessidade: registrar opinião e conversar sobre experiências. Origem: DEC-004, DEC-008 a DEC-012, DEC-015 e DEC-017; avaliações públicas na entrevista.
- Regras confirmadas: 0 a 5 estrelas em passos de meia estrela, texto opcional e comentários vinculados à avaliação; uma avaliação por pessoa/jogo; autor pode editar e excluir a própria avaliação; qualquer usuário autenticado pode comentar, independentemente de amizade.
- Critério derivado para revisão: aceitar 3,5 estrelas sem texto; distinguir nota zero de ausência de avaliação; não aceitar nota fora da escala/incremento definido.
- Casos de erro propostos: avaliação inexistente e comentário inválido; limites de texto propostos em P-06.
- Critérios derivados para revisão: editar nota/texto mantém uma única avaliação por pessoa/jogo; outra pessoa não pode editar a avaliação; visitante sem autenticação não pode publicar comentário; usuário autenticado sem amizade pode comentar.
- Regras confirmadas adicionais: excluir avaliação exclui seus comentários; autor edita/exclui seus comentários; dono da avaliação remove comentários recebidos, sem permissão de edição alheia aprovada (DEC-011/012).
- Critérios derivados para revisão: excluir a avaliação remove sua conversa; editar comentário de outro usuário é negado; dono da avaliação consegue remover um comentário recebido; pessoa sem essas permissões não consegue remover o comentário.
- Regra confirmada adicional: criar/editar avaliação exige jogo na biblioteca (DEC-015/017). Remoção posterior preserva avaliação/comentários (DEC-008); para editar depois é preciso adicionar novamente, mantendo leitura/exclusão disponíveis (DEC-017).
- Critério derivado para revisão: tentar criar avaliação sem jogo na biblioteca não publica a avaliação nem adiciona automaticamente o jogo por inferência; após inclusão explícita, a avaliação pode ser criada.
- Critério derivado para revisão: após remover jogo, tentativa de editar a avaliação não altera seus dados; leitura e exclusão pelo autor continuam permitidas; após readição, editar a avaliação existente não cria duplicata.
- Autorização/visibilidade: avaliações públicas; permissões conforme DEC-009/010/012/015/017. Conteúdo inválido e alvo excluído propostos em P-06. Denúncias/bloqueios/painel administrativo fora da proposta inicial.

### REQ-004 — Amizade e feed
- Necessidade: acompanhar pessoas e suas experiências. Origem: DEC-002, DEC-003, DEC-016 e DEC-021.
- Regras confirmadas: amizade com solicitação alimenta o feed, sem seguir separado; novidades e avisos editoriais de exemplo identificados como demonstração.
- Critério proposto: após aceite de amizade, o feed pode apresentar uma avaliação da pessoa amiga; conteúdo editorial de exemplo é reconhecível como demonstração.
- Casos de erro a especificar: solicitar a si mesmo, duplicata, solicitação cruzada e amizade removida.
- Regra confirmada adicional: feed com somente novas avaliações dos amigos e conteúdo de exemplo, ordenado do mais recente para o mais antigo (DEC-016).
- Critérios derivados para revisão: adicionar jogo, mudar estado ou favoritar não gera publicação no feed; duas publicações com datas diferentes aparecem em ordem decrescente de data.
- Regra confirmada adicional: busca por nickname, enviar/aceitar/recusar solicitação, cancelar enviada e desfazer amizade (DEC-021).
- Autorização, solicitações inválidas, histórico e atualização do feed propostos em P-02. Demonstração com atividades fictícias confirmada em DEC-020.

### REQ-005 — Cadastro, login e contas de demonstração
- Necessidade: criar identidade própria e experimentar a comunidade numa instalação de portfólio. Origem: DEC-013 e DEC-018; visibilidade de perfil em DEC-010.
- Regras confirmadas: cadastro/login com email e senha, email único por conta, nickname único escolhido no cadastro e contas de demonstração. Nickname diferencia maiúsculas/minúsculas: Geovane e geovane, Rivia e riVIA podem ser de pessoas diferentes.
- Critérios derivados para revisão: criar conta escolhendo nickname disponível; impedir segunda conta com o mesmo nickname; autenticar com email e senha corretos; permitir entrada com conta de demonstração documentada e fictícia.
- Critérios derivados para revisão: dois nicknames exatamente iguais não podem existir; nicknames distintos apenas pela capitalização podem existir com emails distintos; repetir email não cria outra conta.
- Casos de erro: campos inválidos, nickname já usado, email já usado e credenciais incorretas; regras complementares em P-03. Não aplicar proposta rejeitada de ignorar maiúsculas/minúsculas em nickname.
- Regra confirmada adicional: recuperação de senha e confirmação de email adiadas (DEC-022); acesso não deve depender da confirmação de email nesta versão.
- Perfil público confirmado; campos e sessão propostos em P-03. Preparação de dados fictícios confirmada em DEC-020; detalhes em P-05. Nenhuma tecnologia de autenticação escolhida.

## Complementos aprovados explicitamente no conjunto — DEC-023
Cada item abaixo foi apresentado como proposta para fechar uma lacuna de comportamento e depois aprovado explicitamente pelo usuário. Mantidos os textos apresentados e suas alternativas/consequências; referências a proposta/recomendação nos itens descrevem a elaboração, não uma pendência de aprovação atual.

### P-01 — Biblioteca e readição
- Somente o titular adiciona/remove jogos, muda estado ou favorito. Repetir uma adição não cria duplicata nem altera o estado/favorito existente.
- Favorito pertence à entrada da biblioteca: removê-la remove esse estado/marcação, preservando a avaliação e os comentários. Adicionar novamente começa em quero jogar e sem favorito; a avaliação preservada é a mesma e volta a ser editável.
- Alternativa: guardar estado/favorito após remover para restaurar depois; isso muda o significado de remoção e exige regras adicionais. Recomenda-se o recomeço explícito para manter o fluxo simples.
- Verificação proposta: remover jogo concluído/favorito e readicionar resulta em quero jogar/sem favorito, mantendo a avaliação anterior sem duplicação; outra pessoa não consegue alterar a biblioteca.

### P-02 — Amizades e feed
- Só o destinatário aceita/recusa; só o remetente cancela; qualquer participante desfaz amizade. Recusar/cancelar permite nova solicitação posterior. Não solicitar a si mesmo ou duplicar amizade/solicitação pendente. Solicitação cruzada apresenta a pendência recebida para aceite, sem aceite automático.
- Feed usa amizades atuais e inclui avaliações anteriores dos amigos aceitos. Desfazer amizade retira suas avaliações do feed, sem apagar avaliações públicas ou comentários.
- Editar avaliação atualiza o mesmo item, sem nova publicação ou mudança de posição pela edição; excluir avaliação retira o item. Empate de datas mantém ordem determinística. Sem amigos, mostrar conteúdo editorial de exemplo e estado vazio para a atividade social.
- Alternativa: mostrar somente avaliações criadas após a amizade ou republicar edições; exige outras regras de histórico. Recomenda-se o recorte acima para experimentar com contas já populadas e evitar repetição.
- Verificação proposta: aceite torna avaliação antiga elegível no feed; desfazer amizade a remove; edição mantém data/posição de publicação e o texto atualizado; não gera evento por favorito/estado.

### P-03 — Identidade, perfil e saída
- Nickname de 3 a 20 caracteres: letras A–Z/a–z, números e sublinhado; preservar capitalização, sem espaços/acentos. Igualdade considera capitalização, conforme DEC-018. Nickname não editável nesta versão.
- Comparar unicidade de email removendo espaços nas extremidades e ignorando maiúsculas/minúsculas; nickname mantém regra distinta. Formato válido de email obrigatório. Login é por email/senha, não por nickname.
- Perfil público inicial exibe nickname, biblioteca e avaliações; sem email, senha, nome civil, avatar enviado ou biografia. Busca de pessoas permite procurar trecho do nickname e mostra sua grafia exata, permitindo distinguir contas com capitalização diferente.
- Incluir saída da conta; após sair, ações autenticadas exigem novo login. Validação de senha, mecanismo e duração de sessão serão propostos com fontes e critérios antes da tarefa de autenticação; não estão autorizados por este documento como decisões técnicas implícitas.
- Alternativa: aceitar Unicode, editar nickname ou enriquecer perfil agora; amplia validações e comportamento de identificação. Recomenda-se este recorte inicial, sujeito ao ajuste do usuário.
- Verificação proposta: Geovane/geovane coexistem com emails distintos; nickname exatamente repetido ou email com apenas capitalização diferente não cria segunda conta; visitante não vê email e não executa escrita autenticada.

### P-04 — Consulta pública e apresentação de jogos
- Visitantes consultam busca, informações do jogo, perfis, bibliotecas e avaliações públicas; precisam entrar para escrever, comentar, usar biblioteca própria, solicitar amizade ou ver feed pessoal.
- Apresentar nome, capa, descrição e plataformas do jogo quando disponíveis; dado ausente tem indicação neutra, sem conteúdo inventado. No modo demonstrativo, jogos e ilustrações são fictícios e identificados como exemplos; não imitar notícia real/atual.
- Sem API configurada, modo demonstrativo é o padrão. Configuração opcional habilita busca real; modo ativo é visível. Falha/limite da API gera mensagem e opção de tentar novamente, sem trocar silenciosamente por resultados fictícios.
- Não converter automaticamente jogos fictícios em reais nem combinar suas identidades. A forma de selecionar/configurar o modo e manter dados sem colisão será apresentada no planejamento técnico; não se propõe uma tela administrativa ou alternância automática por esta aprovação.
- Alternativa: exigir login para leitura ou reduzir consulta a nomes; restringe experimentação. Recomenda-se consulta pública e informações básicas para reconhecer o jogo.
- Verificação proposta: visitante distingue resultados demonstrativos dos reais; erro da API não aparece como zero resultados nem substitui catálogo sem informação.

### P-05 — Entrega local e dados de demonstração
- Instalações têm dados próprios, sem sincronização ou comunidade online compartilhada. Não importar banco anterior. Persistir alterações locais entre reinícios; inicialização normal não apaga nem repovoa por cima dos dados alterados.
- Disponibilizar ao menos duas contas fictícias, jogos e atividades suficientes para experimentar cadastro/login, amizade, avaliação/comentário, estado/favorito e feed. Senhas exclusivamente demonstrativas documentadas; nenhuma credencial pessoal ou de API incluída.
- Após pré-requisitos documentados, um comando inicia os componentes e prepara automaticamente apenas os dados iniciais faltantes. Não definir o comando antes de aprovar stack e estrutura. Preparação/download inicial pode exigir internet; depois de preparado, o modo demonstrativo não depende da API ou de arquivos remotos para as funções centrais. Busca real requer internet e configuração própria.
- Reset destrutivo, sincronização remota e hospedagem não fazem parte da inicialização. Empacotamento com ou sem Docker será comparado e aprovado separadamente.
- Alternativa: demonstração descartável a cada reinício; simplifica preparação, mas perde as experiências do avaliador. Recomenda-se persistência local e inicialização não destrutiva.
- Verificação proposta: iniciar, criar avaliação, encerrar e reiniciar preserva a avaliação sem duplicar dados de exemplo; executar demonstração preparada sem acesso ao provedor funciona.

### P-06 — Texto, erros e qualidade verificável
- Avaliação exige nota válida; texto opcional de até 5.000 caracteres. Comentário exige texto não vazio (não apenas espaços), até 1.000 caracteres. Texto simples, sem HTML ou anexos. Alvo removido ou operação sem permissão não altera dados e produz retorno compreensível.
- Confirmar explicitamente a exclusão de avaliação, informando a exclusão conjunta dos comentários. Remoção do jogo informa que a avaliação permanece. Não tornar exclusão de avaliação uma consequência de remover jogo.
- Interface utilizável em celular e desktop, formulários com rótulos, ações centrais acessíveis por teclado e foco visível. Fluxos de consulta distinguem carregamento, vazio, sucesso e falha; limites e mensagens definidos nos critérios de cada tarefa, sem inventar metas de desempenho.
- Validar permissões e regras fora da interface, não apenas esconder botões. Evidências devem cobrir casos positivos, inválidos e acesso indevido, incluindo a diferença entre criar/editar avaliação e comentar sem amizade. Falha não é sucesso e teste documental não comprova produto.
- Alternativa: texto rico, anexos ou limites maiores; amplia edição e validação. Recomenda-se texto simples nesta fronteira. A confirmação de exclusão é proposta de comportamento futuro, não autorização para excluir dados existentes nesta sessão.
- Verificação proposta: rejeitar nota 5,5, comentário vazio e escrita indevida; comentário de pessoa autenticada não amiga é aceito; cancelar confirmação preserva avaliação/comentários.

## Qualidade e restrições
- Perfil e biblioteca públicos (DEC-010); campos públicos do perfil ainda a especificar, sem inferir exposição de email ou outros dados internos.
- Orçamento zero; sem contratação de serviço pago ou hospedagem paga.
- Objetivo de execução local simples; não prometer ausência de pré-requisitos ou chaves antes da avaliação da API e distribuição.
- Segurança, privacidade, acessibilidade, responsividade, desempenho e cobertura de testes precisam de critérios proporcionais, ainda não aprovados.
- A simulação de autenticação do legado não define a autenticação desta versão.

## Dados e integrações
Comparação documental de RAWG/IGDB em `catalogo/COMPARACAO.md` v0.2, com fontes oficiais consultadas em 01/11/2026; nenhum provedor escolhido ou acesso testado. Licença de imagens, atribuição, limites efetivos da conta e armazenamento precisam de confirmação no planejamento da integração. Demonstração fictícia não exige redistribuir um recorte do provedor. API automática de notícias fora da primeira versão; não confundir notícia de exemplo com catálogo real.

## Dependências para planejamento e tarefas posteriores
- Provedor de jogos, condições de uso/custo zero e acesso real. Escolha requer proposta e aprovação próprias; indisponibilidade não autoriza remover a integração real da fronteira aprovada.
- Stack, versões, arquitetura, desenho de telas/identidade visual, distribuição e pré-requisitos. Nenhum adotado por instalação existente ou por este PRD.
- Política de senha, duração de sessão, tratamento técnico de dados e proteção de credenciais. Propor antes das tarefas correspondentes; não copiar a simulação do legado.
- Especificação concreta dos exemplos, regras de paginação/limites de consultas e critérios por tela. Sem acrescentar comportamento material sem revisão.
- CI/CD com tutoria e GitHub conforme acordos de processo; destino, visibilidade, bootstrap e plano de ambiente ainda a confirmar. Não usar a revisão de produto como autorização de publicação.
- A entrega é local e com tempo disponível limitado. Uma implantação compartilhada exigiria revisar moderação, privacidade, operações e orçamento; não faz parte desta proposta.

## Aprovação e controle de mudanças
Aprovado explicitamente pelo usuário como PRD v0.6, com VISAO v0.3 e MVP v0.6, incluindo P-01 a P-06 (DEC-023). Evidência no registro de decisões. Nenhum teste de produto executado. Próximo marco: planejar stack, arquitetura e tarefas; código e instalações exigem autorizações próprias. Mudança material exige nova versão e revisão, preservando decisões anteriores. Somente metadados de aprovação atualizados após o aceite, sem mudança do conteúdo normativo.

## Histórico do rascunho
- v0.1: primeira organização das jornadas e DEC-001 a DEC-007.
- v0.2: incorpora DEC-008 a DEC-010: preservação após remoção, avaliação única editável/excluível, visibilidade e permissão de comentar; critérios derivados adicionados para revisão, não executados como testes.
- v0.3: incorpora DEC-011 a DEC-013: exclusão da conversa ao excluir avaliação, controle de comentários e REQ-005 (cadastro/login, nickname único e contas de demonstração). Sem testes de aplicação executados.
- v0.4: incorpora DEC-014 a DEC-016: estado inicial/transições livres, exigência de biblioteca para avaliar e feed restrito/cronológico; comparação documental de APIs vinculada. Sem testes de aplicação executados.
- v0.5: incorpora DEC-017 a DEC-019: condição para editar após remover jogo, email único/nickname com distinção de capitalização e demonstração sem chave com busca real configurável. Sem testes de aplicação executados.
- v0.6: incorpora DEC-020 a DEC-022 e consolida primeira proposta para aprovação, com complementos P-01 a P-06 e dependências técnicas explicitamente separadas. Critérios são especificação proposta, não resultados de testes.

# Preparação assistida do ambiente
O agente revisa a pasta e as ferramentas relevantes, explica resultados e ajuda a completar o que faltar. Diagnóstico em `ambiente/DIAGNOSTICO.md`; não equivale a inventário completo da máquina. Stack/arquitetura aprovadas em DEC-025/026/027. Plano concreto de instalação em `ambiente/PLANO-AMBIENTE.md`; GitHub em `ambiente/PLANO-GITHUB.md`. Nenhuma instalação foi executada por inferência dessas aprovações.

## Diagnóstico antes de mudanças
Confirmar sistema operacional, terminal e raiz. Inventariar a pasta, regras locais, documentação, manifestos e lockfiles; perguntar pelo legado se estiver em outro lugar. Acesso se limita à pasta fornecida e às verificações relevantes de ferramentas; não inclui varredura irrestrita de arquivos pessoais.

Verificar conforme a necessidade real:
- Git: disponibilidade, versão, raiz real do repositório, alterações pendentes, branches, remotos e identidade aplicável. Remover credenciais de URLs antes de registrar qualquer resultado.
- Node.js: versão, caminho efetivamente usado, instalações/gerenciadores coexistentes e compatibilidade com a stack que for aprovada. Não atualizar globalmente só porque existe versão nova; avaliar outros projetos e oferecer isolamento por projeto quando apropriado.
- Gerenciador de pacotes: o já usado no legado ou o proposto, lockfiles e compatibilidade. Escolher um por projeto; não criar lockfiles concorrentes nem instalar todos.
- GitHub: conexão disponível, autenticação funcional e permissão no repositório escolhido. GitHub CLI é opcional quando outro recurso disponível resolve a tarefa. Não instalar por obrigação do kit.
- Ferramentas da stack: conferir Angular, NestJS, Prisma, PostgreSQL ou alternativas somente conforme decisão. CLI global, Docker e banco como serviço não são exigências prévias. Evitar iniciar ou atualizar serviços sem avaliar dados e portas existentes.
- Python 3: necessário apenas para executar o verificador documental deste kit localmente; registrar como opcional para desenvolvimento se não for parte da stack. A Action usa seu próprio ambiente.

Um número de versão isolado não comprova configuração correta. Registrar data, origem do executável, resultado do comando e limitações. Usar 'não verificado' quando o acesso não permitir concluir.

## Instalação e atualização
O usuário deseja assistência prática, inclusive execução pelo agente quando possível. Antes de mudar a máquina, apresentar plano concreto com ferramenta, justificativa, versão/canal confirmado, método oficial, alcance local/global, impacto em outros projetos, eventual privilégio/reinício e validação. O usuário pode aprovar esse conjunto uma vez; o agente executa dentro do plano aprovado, respeitando as permissões do ambiente. Preparar Git ou outras ferramentas básicas não exige PRD aprovado; instalar dependências da aplicação exige escolha técnica confirmada.

Não adicionar ferramentas opcionais sem motivo. Não atualizar Node, banco ou gerenciador automaticamente para 'latest'. Conferir documentação oficial atual e compatibilidade, inclusive o lockfile existente. Preservar dados e configuração; explicitar limites do retorno à versão anterior. Desinstalação, substituição destrutiva, reinício, ampliação do plano ou alteração de segurança exigem confirmação específica. Não automatizar elevação de privilégios fora das permissões concedidas.

## Conectar a pasta ao GitHub
1. Inspecionar a raiz Git real, alterações e remotos. Se não houver Git, preparar sua instalação conforme plano aprovado. Não executar git init sobre um repositório pai por engano.
2. Perguntar se o usuário quer criar repositório ou usar um existente; confirmar conta/organização, nome, visibilidade, destino e identidade de autoria. Selecione ferramenta disponível; explique Git local versus hospedagem GitHub e push versus merge.
3. Preparar plano de conexão: inicializar se necessário, revisar arquivos a versionar e .gitignore, criar commit inicial se autorizado, configurar remoto e publicar somente o conteúdo revisado. Para bootstrap vazio, criação e primeiro push de main/develop podem ser autorizados especificamente; isso não permite futuros pushes diretos nessas branches. Sem essa autorização, orientar a execução manual do bootstrap do README.
4. Se remoto existente contiver histórico, inspecionar antes e propor integração sem sobrescrever. Não trocar origin, fazer force-push, reescrever histórico ou limpar alterações para resolver divergências.
5. Usuário faz login no fluxo oficial; agente verifica estado sem expor credenciais. Se faltarem ferramentas ou permissões, explicar a limitação e conduzir os passos manuais.
6. Depois do bootstrap, features saem de develop e entram por PR. Configurar Issues, Project, Actions e proteções somente no alcance autorizado. Confirmar estado local/remoto e, se acessíveis, execuções de checks e regras reais. Sem acesso, marcar a confirmação remota como pendente. Todos os merges seguem manuais pelo usuário.

## Resultado esperado
Relatório do diagnóstico, plano aprovado com evidência, mudanças executadas, verificações reais, pendências e guia de retomada. Quando existirem comandos concretos e aprovados para a stack, documentar em docs/ambiente/COMO-EXECUTAR.md como abrir o terminal, instalar dependências, configurar variáveis por exemplo sem segredos, iniciar serviços/aplicação, executar testes e encerrar serviços. Não inventar comandos antes de criar ou inspecionar o projeto.

---
name: gv-ambiente
description: Diagnosticar e preparar o ambiente do GameVault, orientar instalações e atualizações autorizadas e conectar a pasta ao GitHub.
---

# Ambiente e GitHub com tutoria
Leia AGENTS.md, docs/AMBIENTE.md, docs/GITHUB.md, status e decisões. Este fluxo não autoriza funcionalidades nem escolhe a stack por conta própria.

1. Confirme a raiz do projeto. Faça inventário somente leitura de sua estrutura e configurações relevantes, incluindo instruções locais, manifestos, lockfiles e estado Git. Preserve arquivos existentes. Não percorra todo o disco nem abra conteúdo de credenciais ou arquivos .env para fazer inventário; basta registrar existência quando pertinente.
2. Verifique disponibilidade, versão e caminho das ferramentas pertinentes. Diferencie instalada e executável, executável ausente do PATH, versão incompatível, indisponível e não verificada. Se o comando falhar, investigue o erro sem concluir automaticamente que precisa instalar. Consulte a compatibilidade nas fontes oficiais quando souber a stack alvo.
3. Registre diagnóstico em docs/ambiente/DIAGNOSTICO.md. Apresente o que já atende, o que falta e quais atualizações têm motivo concreto. Ferramentas opcionais devem ser identificadas como tal. Atualize docs/ambiente/PLANO-AMBIENTE.md para apresentar mudanças, versões alvo, escopo local/global, impacto, forma de desfazer e verificações. Peça aprovação desse conjunto concreto antes de instalar, atualizar ou alterar configurações. Aproveitamento de autorização anterior é permitido somente dentro do mesmo plano e alcance; não peça confirmação repetida para cada comando já coberto.
4. Execute as mudanças aprovadas com os recursos disponíveis. Antes de cada etapa relevante, explique sua finalidade e efeito. Use distribuições oficiais e versões compatíveis confirmadas; preserve outras aplicações e bancos. Pare a parte afetada se o instalador mudar o escopo, exigir nova permissão, tiver erro ou revelar risco não previsto. Não tente contornar permissões. Se não houver recurso para executar, dê passos precisos para o usuário e verifique depois; não afirme que instalou.
5. Oriente Git/GitHub conforme docs/AMBIENTE.md e docs/GITHUB.md. Confirme pasta, identidade, destino e visibilidade antes das alterações correspondentes. Login é feito pelo usuário na interface oficial; não peça senha, token ou chave privada no chat. Não faça merge.
6. Reabra a sessão quando necessário para confirmar PATH/versão, valide o resultado real e registre o que mudou e o que continua pendente. Atualize docs/STATUS.md. Não conclua 'ambiente pronto' com base apenas em instalador encerrado com sucesso.

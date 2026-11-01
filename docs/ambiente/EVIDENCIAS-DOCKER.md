# Docker — execução do plano A-02

Data: 01/11/2026 | Plano: PLANO-AMBIENTE v0.1, A-02 | Autorização: DEC-032 | Issue: #1

## Alcance

Docker Desktop 4.97.0 para Windows x86_64, instalação por usuário e backend WSL 2. Sem aplicação, banco do projeto, migração, mudança de firewall, atualização do PostgreSQL nativo ou aceite automático de termos. Caminhos pessoais e identificação detalhada do host omitidos desta versão pública.

## Antes da instalação

- PostgreSQL nativo: serviço postgresql-x64-18 Running/Automatic, observado sem conexão ao banco, consulta de dados ou leitura de credenciais.
- Docker ausente do PATH e dos dois locais padrão; requisitos básicos observados atendidos. WSL 3.0.3 já disponível; nenhuma atualização de WSL/Windows executada.
- Requisito de serviço LanmanServer já Running/Automatic; nenhuma alteração nesse serviço.

## Instalador conferido

- Fonte: [release oficial 4.97.0, publicada em 26/10/2026](https://docs.docker.com/desktop/release-notes/#4970), artefato Windows amd64 build 244584, baixado em pasta temporária exclusiva desta operação.
- [SHA-256 oficial](https://desktop.docker.com/win/main/amd64/244584/checksums.txt) e arquivo baixado coincidem: `2668273f82b342a058a28f9ab53ea7bddde10bb6d51307ce2ec54c2d36459744`.
- Authenticode: Valid; certificado com CN/O Docker Inc, cadeia DigiCert. Versão de produto/arquivo: 4.97.0.244584; produto Docker Desktop Installer.
- A primeira expressão de conferência do editor exigia ponto após “Inc” e interrompeu antes da execução. Inspeção confirmou assinatura válida e campos CN/O “Docker Inc”, sem ponto; condição corrigida para conferir esses campos exatos. Hash/assinatura/versão revalidados antes de iniciar o instalador.

## Execução e verificações

Instalação iniciada com os parâmetros oficiais `install --user --backend=wsl-2 --no-windows-containers --quiet`. Sem `--accept-license`, `--always-run-service` ou instalação para todos os usuários.

- Instalador: código de saída 0; log consultado confirmou Installation succeeded. Docker Desktop instalado por usuário, versão 4.97.0.244584.
- CLI: Docker 29.9.2, build a82e528; Compose v5.6.1. PATH registrado pelo instalador confirmado; processo de validação com PATH renovado a partir dos valores de usuário/sistema resolveu o executável esperado e executou ambos os comandos.
- PostgreSQL observado após instalar: Running/Automatic, igual ao estado anterior. Nenhuma conexão ou comando de alteração do banco realizado.
- Primeiro docker info antes de abrir o Desktop: falhou porque o pipe do motor ainda não existia; instalação de CLI não foi tratada como motor funcional. Docker Desktop aberto para inicialização e eventual aceite de termos pelo usuário.
- Após primeira abertura: motor 29.9.2 respondeu como Linux/x86_64; contexto desktop-linux e endpoint de pipe local conferidos antes do teste. Distribuição docker-desktop em WSL 2 confirmada por consulta filtrada.
- Primeira tentativa de pull: falhou porque o processo anterior à instalação ainda não encontrava docker-credential-desktop no PATH. Correção limitada ao PATH do processo, usando o diretório oficial já registrado pelo instalador; nenhuma leitura/alteração de credenciais ou configuração global. Nova tentativa passou.
- Imagem oficial hello-world baixada e fixada no diagnóstico por digest `hello-world@sha256:c567b231f65614688711a75f31518a064258a51d442117a3e771a3a8fdba78ef`.
- Teste: `docker --context desktop-linux run --pull=never --rm --name gamevault-a02-diagnostico-20261101 --network none <digest-acima>` retornou Hello from Docker e código 0. Sem rede no contêiner, sem bind mounts/volumes e sem portas publicadas. Consulta posterior filtrada pelo nome exato confirmou ausência do contêiner: remoção automática passou.
- Conferência final: PostgreSQL continua Running/Automatic; nenhum acesso a dados/credenciais ou comando de alteração do serviço realizado. Nenhuma exigência de reinício, elevação adicional ou mudança de recursos Windows observada nesta execução.
- Limpeza: removidos somente instalador/checksum da pasta temporária exclusiva desta operação, após verificar destino absoluto e conteúdo. Nenhuma imagem ou volume apagado; imagem de diagnóstico permanece no cache local.

Resultado: critérios de A-02 executados e verificados. Isso valida a instalação/motor Docker e a disponibilidade do Compose; não valida aplicação, banco do projeto, Compose de produto ou autenticação, que ainda não existem.

## Participação do usuário e limites

Usuário conduziu o aceite de termos: resposta nesta sessão Codex de 01/11/2026, sem link disponível, “Aceitei e cheguei à tela principal”. Nenhum aceite automatizado. Se surgirem pedidos de privilégio, reinício ou mudanças Windows em etapas futuras, revisar o novo alcance antes de executá-los.

Terminais/aplicativos abertos antes da instalação podem manter o PATH antigo; reabri-los carrega a configuração registrada. Não é necessário editar PATH manualmente ou reinstalar por esse motivo. O contêiner de diagnóstico foi o único criado/removido nesta etapa.

Fontes: [instalação Windows e opções oficiais](https://docs.docker.com/desktop/setup/install/windows-install/), [diagnóstico com hello-world](https://docs.docker.com/engine/install/ubuntu/#install-using-the-apt-repository) — apenas o teste de contêiner, sem executar instalação Linux dessa página.

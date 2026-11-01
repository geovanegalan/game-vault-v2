# TASK-001 — Base técnica mínima do workspace
Versão: 0.1 | Estado: proposta, não autorizada | Data: 01/11/2026
Issue: não criada | Branch futura: feature/task-001-base-tecnica
REQ: 001 a 005 (fundação) | Base: DEC-023 e ADR-001/002 aprovados em DEC-026/027; tarefa ainda não autorizada

## Objetivo e resultado
Preparar o menor projeto Angular/API que compile e possa ser iniciado, aprendendo onde ficam tela, entrada HTTP e configuração de cada aplicação. Não implementar funcionalidades nem afirmar que build comprova produto.

## Escopo e exclusões
Somente geradores/configuração local das versões posteriormente aprovadas, npm workspaces, um lockfile e scripts cuja finalidade seja documentada. Não criar módulos de domínio, autenticação, banco/migração, dados fictícios, integração externa, deploy ou biblioteca de UI por esta tarefa.

## Pré-condições
1. Stack/arquitetura e versões exatas aprovadas com plano de ambiente.
2. Documentação organizada e primeiro commit documental publicado/revisado conforme DEC-024, sem aplicação.
3. main/develop e regras de proteção verificadas; feature criada de develop; usuário mantém merges.
4. TASK-001 e sua abordagem autorizadas explicitamente. Aprovação de stack ou deste planejamento sozinha não autoriza executar a tarefa.

## Critérios de aceite
- Web e API em pacotes identificáveis, sem repositórios Git internos gerados acidentalmente.
- Dependências resolvidas com um lockfile raiz; scripts de build executam e erros são reportados sem mascarar falhas.
- Aplicações iniciam com os arquivos gerados mínimos, sem exigir chave de catálogo ou conectar banco inexistente.
- Documentar como instalar/iniciar/encerrar e verificar esta base; comandos só serão escritos como executáveis após existirem e serem conferidos.
- Diff revisado quanto a arquivos gerados, configurações e exclusões; README/status refletem o resultado real.

## Plano proporcional proposto
Criar feature de develop; gerar base com versões fixadas/CLIs locais, conferir configs ESM/TypeScript e workspaces, executar builds/execução básica, revisar diff e registrar evidências. Adicionar CI apenas para comandos que já existirem e forem aprovados, sem deploy. Nenhuma instalação global de CLI prevista por conveniência.

## Riscos e recuperação
Geradores podem instalar dependências ou iniciar repositório próprio: conferir opções oficiais antes de executar. Se resolverem versões fora do plano, parar essa parte e explicar. Preservar alterações; não usar reset/clean para apagar arquivos alheios.

## Autorização
Pendente; não executada. Metadados de Issue/commit/PR só serão preenchidos após criação real.

## Evidências / revisão / aprendizado
Não há build, teste, diff de aplicação ou evidência de execução desta tarefa. Quando autorizada, registrar versões, resultado, limitações, passos manuais e revisão. Evitar testes que apenas repitam o texto do gerador; verificar comportamento relevante da base.

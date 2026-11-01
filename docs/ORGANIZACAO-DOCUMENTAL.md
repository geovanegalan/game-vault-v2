# Organização documental antes do primeiro commit
Versão: 0.1 | Estado: revisão inicial finalizada; manter documentos úteis | Data: 01/11/2026 | Base: DEC-024

## Critério de limpeza
Remover documentos somente se não forem necessários ao produto, histórico, tutoria ou fluxo de trabalho. O pedido do usuário permite limpeza após finalizar a documentação; não permite apagar evidências/decisões úteis por serem antigas. Nenhuma remoção foi executada nesta revisão.

## Inventário de uso
| Grupo | Uso atual | Tratamento nesta etapa |
| --- | --- | --- |
| VISAO/PRD/MVP | Produto aprovado em DEC-023 | Manter; atualizar apenas metadados de aprovação, sem mudar regras |
| STATUS e REGISTRO | Retomada e evidência de autoridade | Manter e atualizar |
| Contexto e entrevista | Origem de decisões e propostas rejeitadas | Manter como histórico; contexto inicial não prevalece sobre aprovações posteriores |
| Comparação e ADRs | Stack e arquitetura aprovadas em DEC-025/026/027 | Manter conteúdo e evidências de aprovação |
| Backlog e tarefa inicial | Sequência proposta; tarefa de aplicação ainda não autorizada | Manter, sem confundir planejamento com autorização de execução |
| Diagnóstico e planos | Evitam instalação/publicação por inferência | Manter e atualizar com fatos reais |
| Modelos ADR/TAREFA/REVIEW | Referenciados diretamente pelas skills de planejamento/implementação/revisão | Manter; são ferramentas do processo, não duplicatas de produto |
| Modelos PLANO-AMBIENTE/COMPARACAO-STACK | Referenciados por skills e exigidos pelo verificador do kit | Manter; remoção quebraria referências e verificação atual |
| Modelos VISAO/PRD | Skill de entrevista orienta copiar os modelos em refinamentos; não são a versão vigente do produto | Manter como modelos identificados. Reavaliar apenas se o fluxo de entrevista for alterado, sem modificar as skills implicitamente |
| Prompt inicial | Referência de bootstrap e arquivo exigido no verificador | Manter como recurso histórico; README deixa de tratá-lo como a próxima ação atual |
| Templates Issue/PR e workflow | Rastreabilidade e verificação documental | Manter; sem inventar CI de produto |

## Resultado e próxima revisão
Não há arquivo confirmado como descartável no inventário atual. Os sete modelos somam poucos quilobytes e têm finalidade no fluxo. O README passa a apontar os documentos de trabalho como fonte principal; modelos ficam numa área claramente separada.

Após aprovar stack/arquitetura e terminar planos, rever links, versões, caminhos locais e referências pessoais antes de publicar no repositório público. Se houver documento realmente redundante, removê-lo dentro do escopo autorizado e ajustar todas as referências afetadas; não apagar a pasta de modelos por categoria.

## Verificação
Consulta por referências em docs, skills, README, prompts, scripts e .github identificou dependências acima. Não houve exclusão nem alteração das skills locais. Verificador Python não executado por indisponibilidade do comando diagnosticado; verificações locais de referência não equivalem a teste de produto.

Revisão anterior: 36 arquivos Markdown e 23 links locais, zero destinos ausentes. Após aprovação técnica e criação do plano de ambiente, repetir a verificação antes de versionar. README contém decisões aprovadas e distingue tarefas ainda propostas. Não houve remoção: todos os modelos identificados são usados pelo processo.

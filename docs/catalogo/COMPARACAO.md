# Comparação inicial do catálogo
Versão: 0.2 | Data: 01/11/2026 | Estado: proposta, sem provedor escolhido
Contexto: DEC-006 mantém busca real via API; DEC-019 confirma demonstração sem chave e configuração opcional para busca real. Orçamento zero e demonstração local são restrições declaradas. Pesquisa documental de 01/11/2026, sem conta criada, credenciais consultadas ou chamadas autenticadas; nenhuma nova pesquisa nesta revisão.

| Candidato | Fatos das fontes consultadas | Consequência para o projeto — análise |
| --- | --- | --- |
| RAWG | Página oficial exige chave por requisição e anuncia plano gratuito para projetos pessoais/hobby não comerciais, até 20 mil requisições/mês e links de atribuição nas páginas que usam dados | É familiar ao autor pelo legado e a configuração por chave parece mais simples; adequação do acesso, dados e imagens precisa de verificação antes de adoção |
| IGDB | Documentação oficial declara gratuidade para uso não comercial; exige conta Twitch com autenticação em dois fatores e aplicação registrada, Client ID/Secret e token OAuth; token expira | Alternativa a comparar; exige mais etapas de cadastro e gerenciamento de token. Não usar credencial de demonstração real compartilhada no repositório |

Fontes primárias: [RAWG API](https://rawg.io/apidocs), [termos de API RAWG](https://rawg.io/tos_api), [IGDB — conta e autenticação](https://api-docs.igdb.com/#account-creation). Consultadas em 01/11/2026.

## Lacunas e recomendação preliminar
- Ambas as opções exigem credenciais para busca real. DEC-019 resolve a barreira da primeira experiência com modo demonstrativo sem chave; instruções de configuração real ainda precisam de definição após escolha de provedor.
- Investigar RAWG primeiro pela familiaridade e configuração com chave; manter IGDB como alternativa. É uma recomendação, não adoção. Não foi testada obtenção de chave ou disponibilidade dos serviços.
- A página RAWG apresenta descrições diferentes sobre uso comercial entre o quadro de planos e a seção de termos. Não extrapolar o cenário de portfólio não comercial para uso comercial; esclarecer qualquer divergência relevante antes de mudar a finalidade.
- Nenhuma destas fontes comprova autorização irrestrita para redistribuir imagens/dados num pacote de demonstração. Avaliar atribuição, armazenamento/cache e distribuição de dados antes de propor conteúdo pronto.
- Não foi verificada adequação completa dos campos, idioma, busca e imagens às telas ainda em definição. Não há SLA, limite efetivo da conta ou estabilidade de acesso confirmados.
- Modo de demonstração sem credenciais confirmado em DEC-019. Propor dados sintéticos e imagens próprias/neutras para não presumir permissão de redistribuir um recorte do provedor; origem/conteúdo dos exemplos ainda precisam de confirmação. Busca real continua uma opção configurável na primeira versão.

## Próxima validação
Após preferência do usuário e aprovação do experimento pertinente: verificar cadastro gratuito pelo usuário, preparar configuração local sem expor chave, testar busca limitada e condições de erro. Não realizar pagamento, criar conta, aceitar termos ou publicar credenciais por esta proposta.

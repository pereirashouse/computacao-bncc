# Planeje a infraestrutura da sua escola: projeto final

> Status: **planejado** · reúne os projetos [Rede da Escola](../01-simulador-rede-escola/), [Guardião da Escola](../02-jogo-seguranca-digital/), [A Rede Parou](../03-investigacao-incidente-logs/) e [Como a internet funciona](../04-como-a-internet-funciona/)

| | |
|---|---|
| **Público-alvo** | 9º ano do Ensino Fundamental e Ensino Médio |
| **Eixo** | Os três eixos |
| **Habilidades** | EF09CO02, EF08CO06, EF07CO07, EF08CO10, EF09CO08 |
| **Duração** | 6 a 8 aulas (projeto de bimestre) |
| **Recursos** | Simulador Rede da Escola, papel quadriculado ou editor de diagramas, planilha |

## Público-alvo

9º ano e Ensino Médio, em grupos de 4. Pensado como projeto de encerramento depois dos projetos 1 a 4.

## Objetivo de aprendizagem

| Código | Habilidade | Onde aparece |
|---|---|---|
| EF09CO02 | Construir soluções computacionais de problemas de diferentes áreas, individual ou coletivamente | O projeto inteiro |
| EF08CO06 | Entender como é a estrutura e funcionamento da internet | Mapa da rede e plano de endereçamento |
| EF07CO07 | Identificar problemas de segurança cibernética e experimentar formas de proteção | Regras de segurança, política de senhas, backup |
| EF08CO10 | Discutir questões sobre segurança e privacidade relacionadas ao uso dos ambientes virtuais | Proteção dos dados de alunos e famílias |
| EF09CO08 | Discutir como a distribuição desigual de recursos de computação levanta questões de justiça | Orçamento limitado de escola pública; o que fica de fora |

## Conhecimentos prévios

Endereço IP, gateway, VLAN, firewall e DHCP (projeto 1); diagnóstico com evidências (projeto 3); senhas e backup (projeto 2).

## Problema proposto

A rede estadual vai reformar uma escola fictícia (planta e lista de ambientes fornecidas) com orçamento fixo. Cada grupo é uma equipe de consultoria e precisa apresentar uma proposta à “comissão da escola” (a turma e o professor).

## Atividade prática

Entregas do grupo:

1. mapa da rede (diagrama);
2. divisão dos ambientes em VLANs;
3. plano de endereçamento IP;
4. regras de segurança (matriz do firewall);
5. política de senhas para professores, secretaria e alunos;
6. plano de backup (o quê, onde, com que frequência, como testar);
7. estimativa de equipamentos dentro do orçamento;
8. justificativa técnica de cada escolha;
9. apresentação de 7 minutos para a comissão.

Etapas sugeridas: levantamento (1 aula) → rede no simulador, modo projeto do zero (2 aulas) → políticas de senha e backup (1 aula) → orçamento e justificativa (1 aula) → ensaio e apresentação (1 a 2 aulas). Variação: usar a planta da própria escola, sem expor dados reais da rede dela.

## Critérios de avaliação

| Critério | Peso | Proficiente quando |
|---|---|---|
| Rede e endereçamento | 25% | Projeto do simulador sem erros; avisos mantidos estão justificados |
| Segurança | 25% | Firewall, senhas e backup coerentes com os dados de cada ambiente |
| Orçamento | 15% | Dentro do limite, com o que ficou de fora e o risco assumido |
| Justificativa técnica | 20% | Cada escolha ligada a um requisito ou risco |
| Apresentação | 15% | Clara para quem não é técnico; responde às perguntas da comissão |

## Material do professor

A produzir: planta e lista de ambientes da escola fictícia, orçamento, rubrica detalhada, roteiro da banca e perguntas da comissão (ex.: “e se faltar luz no rack?”, “quem tem a senha do Wi-Fi?”).

## Material do aluno

A produzir: caderno do projeto com modelos para cada entrega (tabela de endereçamento, matriz do firewall, política de senhas, plano de backup, planilha de custos).

## Código ou simulador

Usa o [simulador Rede da Escola](../01-simulador-rede-escola/simulador/) no modo **Projeto do zero**; o `.json` exportado é a entrega técnica. Melhoria necessária no simulador: editor de ambientes, para cada grupo cadastrar ambientes, pontos e orçamento.

## Limitações

- Exige os projetos anteriores; sem eles, vira uma pesquisa teórica.
- O orçamento em preços fictícios não reflete licitação e frete reais.

## Próximas melhorias

- Banca com convidado da área de TI da secretaria de educação.
- Versão para cursos técnicos com cabeamento estruturado e rack.

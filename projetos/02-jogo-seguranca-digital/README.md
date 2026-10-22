# Guardião da Escola: jogo de segurança digital

> Status: **planejado** · evolução da [Operação Anzol](../../aulas/02-operacao-anzol/), que já cobre phishing e links falsos

| | |
|---|---|
| **Público-alvo** | 7º ao 9º ano do Ensino Fundamental |
| **Eixo** | Mundo Digital e Cultura Digital |
| **Habilidades** | EF07CO07, EF08CO08, EF08CO10, EF09CO04 |
| **Duração** | 2 aulas de 50 min |
| **Recursos** | Computador ou celular com navegador, um por dupla. Versão de tabuleiro com cartas |

## Público-alvo

7º ao 9º ano. A Operação Anzol trabalha a perícia de mensagens; o Guardião da Escola trabalha a **decisão**: o estudante gerencia a segurança da escola e convive com as consequências.

## Objetivo de aprendizagem

| Código | Habilidade | Onde aparece |
|---|---|---|
| EF07CO07 | Identificar problemas de segurança cibernética e experimentar formas de proteção | Escolher medidas de proteção com orçamento limitado |
| EF08CO08 | Distinguir os tipos de dados pessoais solicitados em espaços digitais e os riscos associados | Eventos de exposição de dados de alunos |
| EF08CO10 | Discutir questões sobre segurança e privacidade relacionadas ao uso dos ambientes virtuais | Debate sobre as consequências de cada rodada |
| EF09CO04 | Compreender o funcionamento de malwares e outros ataques cibernéticos | Arquivo malicioso, conta falsa, engenharia social |

Ao final, o estudante explica por que nenhuma medida isolada protege tudo, prioriza medidas pelo risco e reconhece sete situações: phishing, senha reutilizada, conta falsa, arquivo malicioso, Wi-Fi aberto, exposição de dados pessoais e engenharia social.

## Conhecimentos prévios

Uso básico de redes sociais e e-mail. Desejável: ter jogado a Operação Anzol.

## Problema proposto

A dupla é a responsável pela segurança digital da escola durante um ano letivo (8 rodadas = 8 meses). Tem um orçamento limitado de “pontos de proteção” e precisa escolher entre medidas como: senha forte e única com gerenciador, verificação em duas etapas, backup, treinamento da equipe, Wi-Fi de visitantes separado, antivírus, política de dados pessoais. A cada rodada sorteia-se um evento.

## Atividade prática

1. **Planejamento:** a dupla gasta o orçamento inicial em medidas.
2. **Rodadas:** cada mês traz um evento (ex.: “a secretária recebe um e-mail do ‘banco’ pedindo para atualizar dados”). Se a medida certa foi comprada, o evento é bloqueado; se não, o jogo mostra a **consequência concreta** (boletins vazados, backup perdido, conta da escola publicando golpe) e o custo de recuperação.
3. **Decisões na hora:** alguns eventos pedem escolha imediata (clicar, ignorar, avisar a TI), com consequências diferentes.
4. **Relatório do ano:** incidentes evitados, sofridos, dados expostos e lição de cada um.

## Critérios de avaliação

| Critério | Iniciante | Proficiente |
|---|---|---|
| Priorização | Compra medidas ao acaso | Justifica as compras pelo risco e pelo impacto |
| Reconhecimento | Identifica 3 das 7 situações | Identifica as 7 e explica o mecanismo |
| Reflexão | Relatório descreve o que aconteceu | Relatório propõe o que faria diferente e por quê |

## Material do professor

A produzir: tabela de eventos com a medida que bloqueia cada um, roteiro, perguntas de mediação (“o backup não evitou o ataque; por que ele foi a melhor compra?”) e versão de tabuleiro.

## Material do aluno

A produzir: ficha de planejamento do orçamento, diário de rodadas e cartão “O que eu faria diferente”.

## Código ou simulador

Estrutura proposta: página única em HTML e JavaScript, no mesmo padrão dos outros objetos.

```text
MEDIDAS  = [{id, nome, custo, protege:[eventos]}]
EVENTOS  = [{id, situacao, tipo, bloqueadoPor:[medidas], consequencia, custoRecuperacao, escolha?}]
estado   = {orcamento, medidas:[], mes, historico:[]}
rodada() → sorteia evento → verifica medidas → aplica consequência → registra
relatorio() → incidentes evitados e sofridos, dados expostos, lições
```

Uma semente de sorteio por turma permite comparar grupos que enfrentaram os mesmos eventos.

## Limitações

- O orçamento em pontos simplifica o custo real (tempo de treinamento, licenças).
- A sorte pode punir uma boa estratégia em poucas rodadas; a semente fixa e o relatório com “risco evitado” atenuam isso.

## Próximas melhorias

- Reaproveitar as mensagens da Operação Anzol como eventos de phishing.
- Modo turma: todas as duplas com os mesmos eventos e placar comparativo.
- Eventos baseados em notícias locais, reescritos sem nomes reais.

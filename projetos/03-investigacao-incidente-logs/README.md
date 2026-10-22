# A Rede Parou: investigação de incidente com logs

> Status: **protótipo funcional** · [abrir o laboratório](https://pereirashouse.github.io/a-rede-parou/) · para usar sem internet, baixe a pasta [`laboratorio/`](laboratorio/) e abra o `index.html` no navegador · [registros em texto](logs/)

| | |
|---|---|
| **Público-alvo** | 9º ano do Ensino Fundamental e Ensino Médio. Funciona também como desafio em clube de computação |
| **Eixo** | Mundo Digital e Pensamento Computacional |
| **Habilidades** | EF07CO06, EF07CO07, EF08CO06 (ver abaixo) |
| **Duração** | 2 aulas de 50 min |
| **Recursos** | Computador ou celular com navegador, um por grupo de 3. Versão impressa: os arquivos de [`logs/`](logs/) |

## Objetivo de aprendizagem

Ao final, o estudante deve ser capaz de:

1. Ler registros (logs) de equipamentos diferentes e organizar os eventos numa linha do tempo.
2. Formular hipóteses para uma falha e confirmá-las ou descartá-las com evidências, como no método científico.
3. Diferenciar **causa** (o que mudou), **gatilho** (quando apareceu) e **sintoma** (o que as pessoas sentem).
4. Explicar o papel do DHCP e do gateway, e por que um servidor DHCP a mais derruba uma rede.
5. Propor medidas técnicas e de processo para evitar que o incidente se repita.

### Alinhamento à BNCC (complemento de Computação, Parecer CNE/CEB nº 2/2022)

| Código | Habilidade | Onde aparece |
|---|---|---|
| EF07CO06 | Compreender o papel de protocolos para a transmissão de dados | A troca DISCOVER, OFFER, REQUEST e ACK do DHCP nos registros |
| EF07CO07 | Identificar problemas de segurança cibernética e experimentar formas de proteção | DHCP indevido, portas abertas no switch, DHCP snooping |
| EF08CO06 | Entender como é a estrutura e funcionamento da internet | Por que um computador com o gateway errado não chega à internet |

A atividade trabalha diretamente os pilares do Pensamento Computacional: **decomposição** (cada registro é uma parte do problema), **reconhecimento de padrões** (quem funciona e quem não funciona), **abstração** (ignorar os eventos que não importam) e **depuração**. Os códigos foram conferidos na lista de habilidades do complemento; confira o texto integral no documento oficial antes de registrar em plano de ensino.

## Conhecimentos prévios

- O que é endereço IP e gateway. Se a turma ainda não viu, use antes as missões 1, 2 e 5 do [simulador Rede da Escola](../01-simulador-rede-escola/).
- Ler horários e datas no formato `2025-03-17 07:05:13`.
- Não é preciso saber comandos nem programação.

## Problema proposto

Segunda-feira, 07h20. Na secretaria, na sala dos professores e no laboratório, os computadores dizem “conectado, sem internet” e o sistema de notas não abre. A direção diz que lá está tudo normal. No fim de semana houve atualização do firewall, troca do nobreak e uma queda do link de internet de madrugada. O que causou o problema?

Os registros contêm a causa verdadeira e **cinco pistas falsas plausíveis** (firmware do firewall, nobreak, queda do link, aluno que errou a senha cinco vezes e disco quase cheio). Cada uma pode ser descartada com evidência.

## Atividade prática

Grupos de 3, com papéis que se revezam: **leitor** (navega nos registros), **escrivão** (marca evidências e preenche hipóteses) e **advogado do diabo** (questiona cada conclusão).

1. **Hipóteses iniciais (10 min):** antes de abrir os registros, o grupo lê o caso e escreve o que acha que aconteceu.
2. **Investigação (40 min):** o laboratório mostra 9 fontes de registros (chamados, mudanças, servidor DHCP, firewall, switch, sistema de notas, servidor de arquivos e duas capturas de configuração de computador). O grupo procura termos em todos os registros, marca linhas como evidência e o laboratório monta a linha do tempo. Para cada uma das seis hipóteses, o grupo decide se está confirmada ou descartada e escreve a justificativa.
3. **Laudo (20 min):** sete perguntas objetivas (causa, equipamento, endereço indevido, horário da mudança, por que alguns funcionaram, prevenção, correção) e um relato em texto livre para a direção. A conferência mostra acertos; a explicação de cada resposta aparece na segunda conferência.
4. **Socialização (20 min):** cada grupo apresenta a linha do tempo em 2 minutos. A turma discute: “o problema começou na segunda ou na sexta?”.

Três pistas graduais ajudam quem travar, e o uso delas fica registrado no laudo. Roteiro detalhado no [material do professor](professor.md).

## Critérios de avaliação

| Critério | Iniciante | Em desenvolvimento | Proficiente |
|---|---|---|---|
| Uso de evidências | Conclui sem citar registros | Cita evidências para a causa | Cita evidências também para descartar as pistas falsas |
| Linha do tempo | Ausente ou fora de ordem | Ordena os eventos principais | Separa causa (sexta 17:52), gatilho (segunda 07:05) e sintomas |
| Raciocínio | Escolhe a primeira hipótese | Testa algumas hipóteses | Explica por que direção e PC-LAB-03 funcionavam |
| Prevenção | Medidas sem relação com a causa | Uma medida técnica | Medidas técnicas e de processo, justificadas |
| Comunicação | Relato confuso ou só técnico | Relato correto | Relato que a direção entende, sem perder a precisão |

Evidências: laudo `.txt` baixado do laboratório (com hipóteses, linha do tempo, respostas, pistas usadas e número de conferências) e a [ficha do grupo](aluno.md).

## Material do professor

[professor.md](professor.md): gabarito com a linha do tempo completa, como descartar cada pista falsa, roteiro das aulas, perguntas de mediação, versão impressa e como criar novos casos.

## Material do aluno

[aluno.md](aluno.md): ficha do grupo com quadro de hipóteses, linha do tempo, glossário e o modelo do relato para a direção.

## Código ou simulador

- [`laboratorio/index.html`](laboratorio/index.html): página única em HTML, CSS e JavaScript puro, sem bibliotecas. Salva o progresso no navegador e exporta o laudo.
- [`logs/`](logs/): os registros em texto puro. Servem para imprimir e para editar o caso.
- [`laboratorio/embutir-logs.py`](laboratorio/embutir-logs.py): copia os registros de `logs/` para dentro da página. Rode `python3 embutir-logs.py` depois de editar um registro.

No código, `FONTES` lista os registros, `HIPOTESES` e `PISTAS` definem o caso e `PERGUNTAS` traz o laudo com a resposta e a explicação de cada item. Um caso novo é: trocar os arquivos de `logs/`, rodar o script e reescrever esses quatro quadros.

## Limitações

- Há um único caso. Depois de resolvido, a turma conhece a resposta; os grupos não podem trocar informação entre si.
- O gabarito está no código da página. Um estudante que saiba abrir o código-fonte encontra as respostas, e as perguntas objetivas permitem tentativa e erro (o número de conferências fica registrado para o professor perceber).
- Os registros foram escritos em português e simplificados. Logs reais são em inglês, têm muito mais linhas e formatos diferentes para cada fabricante.
- A rede do caso é “plana” (uma VLAN só), escolhida para que o problema atinja a escola toda.
- Os endereços MAC usam o prefixo `02:` (endereços locais) para não coincidir com nenhum fabricante real.

## Próximas melhorias

1. Mais casos, do mais simples ao mais difícil: cabo com laço (tempestade de broadcast), DNS fora do ar, certificado vencido, conta comprometida por senha reutilizada.
2. Versão avançada com registros reais em inglês e no formato de cada equipamento.
3. Sortear detalhes do caso (horários, portas, endereços) para cada grupo ter números diferentes.
4. Ligação com o [simulador Rede da Escola](../01-simulador-rede-escola/): depois do laudo, a turma refaz a rede da escola com VLANs.
5. Mover o gabarito para um arquivo separado do professor e conferir por código de verificação.

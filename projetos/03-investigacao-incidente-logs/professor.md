# A Rede Parou · material do professor

> Este arquivo tem o gabarito. Não compartilhe com a turma antes da atividade.

## O que aconteceu (gabarito)

Na sexta-feira às 17:48, a biblioteca recebeu um roteador Wi-Fi doado e o ligou numa tomada de rede da mesa 2, **sem registrar a mudança** e usando uma porta LAN do roteador. Esse tipo de roteador vem de fábrica com servidor DHCP ligado, entregando endereços `192.168.0.x` e se anunciando como gateway (`192.168.0.1`). Como a rede da escola é uma VLAN única e o switch não tem DHCP snooping, o roteador passou a responder aos pedidos de endereço da escola inteira.

Na sexta à noite e no fim de semana quase ninguém pediu endereço. Na segunda de manhã, cada computador que ligava pedia um IP e aceitava a primeira oferta que chegava. Muitos aceitaram a do roteador doado: ficaram com gateway `192.168.0.1`, que não está ligado à internet, e numa rede diferente da dos servidores (`192.168.1.x`). Daí o “conectado, sem internet”.

Quem não pediu endereço novo continuou funcionando: a direção (IP fixo `192.168.1.20`), a impressora (`192.168.1.30`), os servidores e o PC-LAB-03, que ficou ligado desde sexta e renovou o endereço com o servidor oficial.

## Linha do tempo completa

| Quando | Fonte | Evento | Papel |
|---|---|---|---|
| sex 14:00 | Mudanças, firewall | Atualização do firmware, testada às 14:20 | Pista falsa |
| sex 16:30 | Switch | Mudança de topologia na porta 3, estável em 2 s | Pista falsa |
| **sex 17:48** | **Chamados** | **Biblioteca liga roteador doado na mesa 2** | **Causa** |
| **sex 17:52** | **Switch** | **Porta 14 (BIBLIOTECA-MESA2) ativa, MAC novo** | **Causa** |
| sáb 10:15 a 10:41 | Mudanças, servidores, switch | Troca do nobreak; tudo religado e testado | Pista falsa |
| sáb 10:40 | Switch | Inicialização: “VLANs: 1; DHCP snooping: desativado” | Vulnerabilidade |
| dom 02:47 | Servidor de arquivos | Backup concluído com sucesso | Mostra que o servidor estava bem |
| dom 03:12 a 03:14 | Firewall | Link do provedor caiu e voltou em 2 min | Pista falsa |
| dom 23:00 | Servidor de arquivos | Disco com 87% | Pista falsa |
| **seg 07:05** | **DHCP oficial, captura PC-SEC-02** | **PC-SEC-02 aceita 192.168.0.104 de 192.168.0.1** | **Gatilho** |
| seg 07:09 a 07:22 | DHCP oficial | O mesmo com PC-PROF-03, NOTE-PROF-07, PC-LAB-05, PC-LAB-12 | Sintoma |
| seg 07:20 | Sistema de notas | Login da direção (192.168.1.20) funciona | Contraste |
| seg 07:31 | DHCP oficial | PC-LAB-03 renova 192.168.1.153 com o oficial | Contraste |
| seg 07:45 | Firewall | Teste do link: OK, sem perda | Descarta o link |
| seg 07:52 a 07:53 | Sistema de notas | aluno.lab05 erra a senha 5 vezes, conta bloqueada | Pista falsa |
| seg 08:00 | DHCP, firewall, servidor de arquivos | 5 concessões (normal: 80); 6 origens no firewall; 2 conexões no servidor (normal: 40) | Sintoma |
| seg 09:00 | Firewall | Nenhuma conexão bloqueada | Descarta o firewall |

## Como descartar cada pista falsa

| Hipótese | Evidência que descarta |
|---|---|
| Link de internet caiu | Voltou às 03:14 de domingo; teste de segunda às 07:45 OK; a direção navega |
| Atualização do firewall | Foi testada na sexta às 14:20 com navegação OK; o firewall não bloqueou nada; a direção navega pelo mesmo firewall |
| Servidores após o nobreak | Todos voltaram às 10:41 de sábado; backup de domingo OK; direção usa o sistema de notas às 07:20 |
| Invasão por senha | Uma única conta, de um aluno, com 5 tentativas em 90 segundos: é alguém esquecendo a senha. E esse computador (192.168.1.153) alcança o servidor, ou seja, ele **não** está entre os afetados |
| Disco cheio | 87% não é cheio, e o serviço de arquivos está ativo; o problema é que os computadores não chegam até ele |

## Roteiro das aulas

### Aula 1 (50 min)

| Momento | Tempo | O que acontece |
|---|---|---|
| Problematização | 10 min | “Quando a internet da escola cai, como a TI descobre o motivo?” Apresentar o que é um log com um exemplo da vida real (histórico de chamadas do celular, extrato bancário). |
| Hipóteses iniciais | 10 min | Ler o caso. Cada grupo escreve suas hipóteses na ficha **antes** de abrir os registros. |
| Investigação | 30 min | Grupos exploram os registros e marcam evidências. Circule fazendo perguntas, sem dar respostas. |

### Aula 2 (50 min)

| Momento | Tempo | O que acontece |
|---|---|---|
| Investigação | 10 min | Fechar o quadro de hipóteses. |
| Laudo | 20 min | Responder e conferir o laudo; escrever o relato para a direção. |
| Socialização | 15 min | Dois ou três grupos apresentam a linha do tempo. Debate: “quem é o culpado?” (resposta esperada: o processo, não a bibliotecária). |
| Fechamento | 5 min | Ligar com o mundo real: por que empresas exigem registro de mudanças. |

## Perguntas de mediação

- “O que há de diferente entre quem funciona e quem não funciona?”
- “Se o problema fosse o link de internet, a direção estaria funcionando?”
- “O problema começou na segunda? Ou só apareceu na segunda?”
- “O aluno que errou a senha estava sem rede? Como vocês sabem?”
- “A bibliotecária fez algo errado? O que faltou na escola para que isso não acontecesse?”

## Versão impressa (sem computador)

1. Imprima cada arquivo de [`logs/`](logs/) em uma folha e espalhe pela sala como “estações”.
2. Os grupos circulam com marca-texto e a ficha do aluno.
3. A linha do tempo é montada num varal com fita crepe e tiras de papel.
4. As perguntas do laudo estão na [ficha do aluno](aluno.md); corrija com este gabarito.

## Como criar um caso novo

1. Escreva a história primeiro: causa, gatilho, quem é afetado e quem não é (o contraste é o que torna o caso resolvível).
2. Escreva os registros de cada fonte. Inclua pelo menos três pistas falsas, cada uma com uma evidência que a descarte.
3. Use só endereços privados (`192.168.x.x`, `10.x.x.x`), MACs com prefixo `02:` e nomes de função (secretaria01, prof.historia), nunca nomes de pessoas ou de empresas reais.
4. Salve em `logs/`, rode `python3 laboratorio/embutir-logs.py` e ajuste `HIPOTESES`, `PISTAS` e `PERGUNTAS` no `index.html`.

## Adaptações

- **Turma iniciante:** entregue só chamados, as duas capturas e o log do DHCP oficial. A pergunta vira “o que a direção tem de diferente?”.
- **Ensino Médio ou técnico:** peça também o plano de correção passo a passo e a configuração de DHCP snooping em pseudocódigo.
- **Leitura com dificuldade:** o professor lê os chamados em voz alta; o laboratório respeita o zoom do navegador.

## De onde veio

O DHCP indevido (“rogue DHCP”) é um dos incidentes mais clássicos de rede local: um roteador doméstico ligado pela porta errada derruba uma rede inteira. O caso foi reescrito do zero, com escola, horários, endereços e nomes fictícios.

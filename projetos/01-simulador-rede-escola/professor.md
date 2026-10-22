# Rede da Escola · material do professor

## Antes da aula

- Abra o [simulador](simulador/index.html) e jogue a missão 1 para conhecer a interface (5 min).
- Se a escola não tiver internet, copie a pasta `simulador/` para um pendrive: a página funciona offline.
- Imprima uma [ficha do aluno](aluno.md) por dupla.
- Combine os papéis da dupla: **operador** (mexe no simulador) e **relator** (registra hipótese e evidência na ficha). Troquem a cada missão.

## Roteiro sugerido (Três Momentos Pedagógicos)

### Aula 1 · Problematização e missões 1 e 2

| Momento | Tempo | O que acontece |
|---|---|---|
| Problematização | 10 min | "Por que o celular de vocês não abre o sistema de notas da secretaria, mesmo estando no Wi-Fi da escola?" Registrar as respostas no quadro. |
| Conceitos | 10 min | Analogia do endereço: IP é o número da casa, a rede (os três primeiros números) é a rua, o gateway é a portaria do condomínio. Mostrar o mapa da rede do simulador. |
| Missão 1 | 12 min | Conflito de IP. Antes de verificar, cada dupla escreve a hipótese. |
| Missão 2 | 15 min | Impressora fora da rede. Ponto alto: o ping chega até a VLAN certa e para. |
| Fechamento | 3 min | "O que o gateway faz?" em uma frase, na ficha. |

### Aula 2 · Segurança e missões 3 e 5

| Momento | Tempo | O que acontece |
|---|---|---|
| Problematização | 10 min | Ler a situação da missão 3. "Que dados existem na secretaria? Quem pode ver?" Ligar à LGPD. |
| Missão 3 | 20 min | Antes de corrigir, faça o ping de CELULAR-VISITANTE para PC-SEC-01 e mostre que passa **sem firewall** porque estão na mesma VLAN. |
| Missão 5 | 15 min | DHCP e o endereço 169.254.x.x. Se possível, mostre um `ipconfig` real (Windows) ou as configurações de Wi-Fi do celular. |
| Fechamento | 5 min | "Por que separar em VLANs se o firewall já bloqueia?" |

### Aula 3 · Equipamentos e missão 4

Missão 4 com foco em custo. Desafio extra: "a escola tem R$ 8.000; o que vocês cortam e qual o risco?". Discutir a habilidade EF09CO08 (distribuição desigual de recursos de computação) se a turma for de 9º ano.

### Aulas 4 e 5 · Projeto do zero

As duplas criam a rede completa. Produto: relatório exportado + projeto `.json` + apresentação de 3 minutos justificando as escolhas.

## Gabarito das missões

### Missão 1 · Conflito na biblioteca

- **Defeito:** PC-BIB-01 e PC-BIB-02 com o mesmo IP `192.168.40.10`.
- **Correção:** mudar PC-BIB-02 para `192.168.40.11` (ou qualquer endereço livre de `.2` a `.99`).
- **Mediação:** "Por que o problema 'pula' de um computador para o outro?" (cada um responde no lugar do outro de tempos em tempos).

### Missão 2 · A impressora que ninguém acha

- **Defeitos:** IMP-SECRETARIA está com IP `192.168.20.50` (rede da secretaria) mas fica na VLAN 60, e sem gateway.
- **Correção:** IP `192.168.60.10`, gateway `192.168.60.1`.
- **Mediação:** mostrar que o ping passa pelo firewall e só falha ao procurar a impressora na VLAN 60. Depois de corrigir só o IP, o ping ainda falha: a impressora recebe, mas não sabe responder sem gateway. É o momento de mostrar que **a resposta também precisa de caminho**.

### Missão 3 · Visitantes no servidor

- **Defeitos:** ambiente Visitantes na VLAN 20 (secretaria), DHCP ligado na VLAN 20 para atender os visitantes, regra Visitantes → Servidores liberada.
- **Correção:** Visitantes na VLAN 90; desmarcar Visitantes → Servidores. O DHCP da VLAN 20 pode continuar ligado ou ser desligado; os computadores da secretaria têm IP fixo.
- **Mediação:** o erro mais grave não é a regra do firewall, é a VLAN compartilhada, porque nela o tráfego nem passa pelo firewall.

### Missão 4 · Equipamentos para a reforma

- **Defeitos:** laboratório com switch de 8 portas (precisa de 22: 21 pontos + 1 de ligação); sala dos professores sem access point; câmeras em switch sem PoE.
- **Correção de menor custo:** switch de 24 portas no laboratório, 1 AP na sala dos professores, switch PoE de 8 portas nas câmeras. Total de referência: R$ 8.980.
- **Mediação:** "Dois switches de 16 portas resolvem?" (no simulador não, porque cada ambiente tem um switch; na vida real, sim, com cascateamento, mas aumenta os pontos de falha).

### Missão 5 · Laboratório sem internet

- **Defeitos:** DHCP desligado na VLAN 10 e regra Laboratório → Internet ausente.
- **Correção:** marcar DHCP na VLAN 10 e liberar Laboratório → Internet.
- **Mediação:** o endereço 169.254.x.x é o computador "se virando" quando ninguém responde ao pedido de DHCP. É um sintoma que os alunos vão encontrar em casa.

## Plano de referência (rede sem erros nem avisos)

| VLAN | Nome | Rede | Gateway | DHCP | Ambiente |
|---|---|---|---|---|---|
| 10 | LAB | 192.168.10.0/24 | 192.168.10.1 | sim | Laboratório |
| 20 | SECRETARIA | 192.168.20.0/24 | 192.168.20.1 | não | Secretaria e direção |
| 30 | PROFESSORES | 192.168.30.0/24 | 192.168.30.1 | sim | Sala dos professores |
| 40 | BIBLIOTECA | 192.168.40.0/24 | 192.168.40.1 | sim | Biblioteca |
| 50 | SERVIDORES | 192.168.50.0/24 | 192.168.50.1 | não | Servidores |
| 60 | IMPRESSORAS | 192.168.60.0/24 | 192.168.60.1 | não | Impressoras |
| 70 | CAMERAS | 192.168.70.0/24 | 192.168.70.1 | não | Câmeras |
| 90 | VISITANTES | 192.168.90.0/24 | 192.168.90.1 | sim | Visitantes |

Regras liberadas: Laboratório, Secretaria, Professores, Biblioteca e Visitantes → Internet; Secretaria e Professores → Servidores e Impressoras; Secretaria → Câmeras.

Este é um plano possível, não o único. No projeto do zero, aceite outras numerações desde que o relatório justifique.

## Perguntas de mediação

- O que muda para o usuário quando o IP está errado? E quando o gateway está errado? (No primeiro, nada funciona; no segundo, a rede local funciona e o resto não.)
- Se dois ambientes dividem a mesma VLAN, a regra de firewall entre eles serve para alguma coisa?
- Por que servidores e impressoras usam IP fixo e celulares usam DHCP?
- Quem na escola deveria poder ver as câmeras? E quem não deveria?

## Versão desplugada

1. Cada ambiente vira uma folha A4 colada numa parede da sala, com a cor da VLAN.
2. Cada aluno recebe um cartão de dispositivo com nome, IP e gateway escritos a lápis.
3. Um aluno é o roteador, com uma lista de regras do firewall.
4. Para "pingar", o aluno leva um bilhete até o destino. O roteador confere o bilhete: se o remetente não tem gateway certo ou a regra não deixa, o bilhete volta.
5. Os defeitos das missões 1, 2 e 3 funcionam bem assim.

## Adaptações

- **Turma iniciante (7º ano):** só missões 1, 2 e 5, sem falar em VLAN; use "redes separadas".
- **Ensino Médio ou técnico:** peça redes /25 ou /26 no projeto do zero e discuta o tamanho de cada rede.
- **Baixa visão:** o simulador respeita o zoom do navegador; as cores das VLANs também aparecem em texto ("VLAN 20").
- **Pouco computador:** um projetor e a turma decide em votação cada correção.

## De onde veio

Os defeitos das missões estão entre os chamados mais comuns em redes de escolas e pequenas empresas: IP repetido, impressora trocada sem reconfigurar, Wi-Fi de visitante misturado à rede administrativa e DHCP desligado após manutenção. Nenhum dado real de rede foi usado: escola, nomes e endereços são fictícios.

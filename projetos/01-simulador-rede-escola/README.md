# Rede da Escola: simulador de redes

> Status: **protótipo funcional** · [abrir o simulador](https://pereirashouse.github.io/rede-da-escola/) · para usar sem internet, baixe a pasta [`simulador/`](simulador/) e abra o `index.html` no navegador

| | |
|---|---|
| **Público-alvo** | 8º e 9º ano do Ensino Fundamental. Adaptável ao Ensino Médio e a cursos técnicos de informática |
| **Eixo** | Mundo Digital (principal) e Cultura Digital |
| **Habilidades** | EF07CO06, EF08CO06, EF07CO07, EF08CO10 (ver abaixo) |
| **Duração** | 3 aulas de 50 min (missões 1 a 5) + 2 aulas para o projeto do zero |
| **Recursos** | Computador ou celular com navegador, um por dupla. Versão desplugada com cartões no [material do professor](professor.md) |

## Objetivo de aprendizagem

Ao final, o estudante deve ser capaz de:

1. Explicar o papel de um endereço IP, da máscara e do gateway, e prever o que acontece quando um deles está errado.
2. Identificar e corrigir conflito de IP, ausência de gateway e dispositivo fora da própria rede.
3. Justificar por que uma escola separa a rede em VLANs (alunos, secretaria, visitantes, câmeras).
4. Escolher equipamentos (switch, access point) a partir da quantidade de pontos e de pessoas.
5. Escrever regras simples de firewall e relacioná-las à proteção de dados pessoais.

### Alinhamento à BNCC (complemento de Computação, Parecer CNE/CEB nº 2/2022)

| Código | Habilidade | Onde aparece |
|---|---|---|
| EF07CO06 | Compreender o papel de protocolos para a transmissão de dados | DHCP entregando endereços, gateway, teste de ping |
| EF08CO06 | Entender como é a estrutura e funcionamento da internet | Caminho do pacote: dispositivo → switch → roteador → internet |
| EF07CO07 | Identificar problemas de segurança cibernética e experimentar formas de proteção | Segmentação por VLAN, firewall, câmeras isoladas |
| EF08CO10 | Discutir questões sobre segurança e privacidade relacionadas ao uso dos ambientes virtuais | Por que visitantes e alunos não podem alcançar a secretaria |

Também mobiliza o eixo Pensamento Computacional: decomposição (cada ambiente é um subproblema), reconhecimento de padrões (o mesmo tipo de erro em ambientes diferentes) e depuração. Os códigos foram conferidos na lista de habilidades do complemento; confira o texto integral no documento oficial antes de registrar em plano de ensino.

## Conhecimentos prévios

- Saber que computadores trocam informação em rede e que a internet chega à escola por um provedor.
- Ler números no formato `192.168.10.25`. Não é preciso saber binário: o simulador usa redes /24, em que basta comparar os três primeiros números.
- Desejável: ter feito a aula [A "invisibilidade" do Wi-Fi](../../aulas/01-invisibilidade-do-wifi/), que apresenta pacotes e roteador.

## Problema proposto

A escola fictícia tem laboratório de informática, secretaria, biblioteca, sala dos professores, rede de visitantes, servidores, impressoras e câmeras. Tudo precisa de rede, mas cada ambiente tem um risco diferente: o celular de um visitante não pode chegar ao sistema de notas, e uma câmera esquecida não pode virar porta de entrada. A turma é a equipe de infraestrutura e precisa deixar a rede funcionando e segura.

## Atividade prática

O simulador tem cinco missões curtas, cada uma com um defeito real de rede escolar, e um projeto aberto.

| Missão | Defeito | Conceito |
|---|---|---|
| 1 · Conflito na biblioteca | Dois computadores com o mesmo IP | Endereço único, conflito de IP |
| 2 · A impressora que ninguém acha | IP de outra rede e sem gateway | Rede, gateway, roteamento entre VLANs |
| 3 · Visitantes no servidor | Visitantes na VLAN da secretaria e regra de firewall aberta | Segmentação, firewall, LGPD |
| 4 · Equipamentos para a reforma | Switch pequeno, sala sem access point, câmeras sem PoE | Dimensionamento e custo |
| 5 · Laboratório sem internet | DHCP desligado e regra de saída ausente | DHCP, endereço 169.254.x.x |
| Projeto do zero | Nada configurado | Tudo junto: plano de endereçamento completo |

Em cada missão, a dupla:

1. Lê a situação e formula uma hipótese antes de mexer em qualquer coisa.
2. Clica em **Verificar rede**. Cada problema vem com dicas graduais (a primeira explica, a segunda quase entrega a resposta), e o uso de dicas fica registrado.
3. Usa o **teste de ping** para confirmar. O teste mostra o caminho do pacote passo a passo e em qual ponto ele parou.
4. Gera o **relatório final**, que lista o que foi corrigido, o que ficou pendente e por que cada item importa, e escreve a justificativa dos avisos que decidiu manter.

Roteiro de aula detalhado no [material do professor](professor.md).

## Critérios de avaliação

| Critério | Iniciante | Em desenvolvimento | Proficiente |
|---|---|---|---|
| Endereçamento | Corrige com as dicas | Corrige sozinho e explica o erro | Monta o plano de endereçamento do zero sem erros |
| Diagnóstico | Altera ao acaso até sumir o erro | Usa o ping para localizar a falha | Formula hipótese antes, testa e confirma |
| Segurança | Libera tudo no firewall | Bloqueia visitantes | Justifica cada regra em relação aos dados protegidos |
| Comunicação | Relatório sem justificativa | Justifica parte dos avisos | Relatório claro, com linguagem técnica correta |

Evidências: relatório `.txt` e projeto `.json` exportados pelo simulador (com número de verificações, dicas usadas e testes de ping), mais a ficha do aluno.

## Material do professor

[professor.md](professor.md): roteiro das aulas, gabarito de cada missão, plano de referência da rede, perguntas de mediação, versão desplugada e adaptações.

## Material do aluno

[aluno.md](aluno.md): ficha de missão com espaço para hipótese, evidência e correção, glossário e tabela do plano de endereçamento.

## Código ou simulador

[`simulador/index.html`](simulador/index.html): página única em HTML, CSS e JavaScript puro, sem bibliotecas e sem servidor. Funciona offline, salva o progresso no navegador e exporta o projeto em JSON.

Como está organizado o código:

- `AMB`: os ambientes da escola, com pontos de cabo e pessoas no Wi-Fi.
- `SW`, `AP`: catálogo de equipamentos com preços fictícios.
- `PROIBIDO` e `NECESSARIO`: a política de segurança que a verificação usa. O professor pode editar esses dois quadros para mudar o que conta como erro.
- `MISSOES`: cada missão parte da rede de referência (`base()`) e injeta defeitos. Criar uma missão nova é escrever uma função `montar()`.
- `verificar()`: as regras de validação (IP, gateway, conflito, DHCP, segmentação, equipamentos, firewall).
- `ping()`: simula o caminho do pacote e explica onde ele parou.

## Limitações

- Usa só redes /16 a /30 e o DHCP sempre entrega a partir do `.100` da rede. Não há sub-redes de tamanho variável dentro do mesmo ambiente.
- O firewall é uma matriz de "quem pode iniciar conexão com quem". Não há portas, protocolos nem regras por dispositivo.
- Não simula DNS, NAT, roteamento estático entre roteadores, Wi-Fi (canais, sinal) nem cabeamento físico.
- Os ambientes e a quantidade de pontos são fixos. O aluno não desenha a planta.
- Os preços são fictícios e servem só para comparar alternativas.
- Não foi testado com leitor de tela; os controles têm rótulos, mas o diagrama não tem descrição textual detalhada.

## Próximas melhorias

1. Editor de ambientes para o projeto final ([Planeje a infraestrutura da sua escola](../05-planeje-a-infraestrutura-da-escola/)): a turma cadastra a própria escola.
2. Modo "laboratório de roteador": integrar com o [simulador de roteador](https://pereirashouse.github.io/simulador-configura-o-roteador/) e criar desafios progressivos de interface, rota e correção de configuração.
3. Regras de firewall por porta (HTTP, impressão, câmeras) para o Ensino Médio.
4. Animação do pacote no diagrama durante o ping.
5. Painel do professor que lê vários arquivos `.json` e resume a turma.

# Como a internet funciona: a viagem de uma página

> Status: **planejado**

| | |
|---|---|
| **Público-alvo** | 6º ao 8º ano do Ensino Fundamental |
| **Eixo** | Mundo Digital |
| **Habilidades** | EF06CO07, EF07CO06, EF08CO06, EF09CO05 |
| **Duração** | Oficina de 2 aulas de 50 min |
| **Recursos** | Navegador; versão desplugada com envelopes e barbante |

## Público-alvo

6º ao 8º ano. A parte de HTTPS e criptografia pode ser aprofundada no 9º ano.

## Objetivo de aprendizagem

| Código | Habilidade | Onde aparece |
|---|---|---|
| EF06CO07 | Entender a transmissão de dados em que a informação é fragmentada e enviada em pacotes | A página viaja em pacotes; perda de pacotes |
| EF07CO06 | Compreender o papel de protocolos para a transmissão de dados | DNS, HTTP e HTTPS como “combinados” entre máquinas |
| EF08CO06 | Entender como é a estrutura e funcionamento da internet | Caminho navegador → DNS → roteador → servidor → resposta |
| EF09CO05 | Analisar técnicas de criptografia para armazenamento e transmissão de dados | O que muda quando a conexão passa por HTTPS |

Ao final, o estudante descreve o caminho de uma página e prevê o sintoma de cada falha (“o site não foi encontrado” é diferente de “o servidor não respondeu”).

## Conhecimentos prévios

Usar um navegador e digitar um endereço. Nada mais.

## Problema proposto

“Você digita o nome de um site e, em menos de um segundo, a página aparece. O que aconteceu nesse segundo? E por que às vezes aparece ‘servidor não encontrado’ e outras vezes ‘a conexão expirou’?”

## Atividade prática

1. **Sequência visual animada:**

   ```text
   Navegador → DNS → roteador → servidor → resposta HTTP → navegador
   ```

   Cada etapa mostra o que é enviado (pergunta ao DNS, pedido GET, pacotes de resposta).
2. **Laboratório de falhas:** o aluno liga e desliga componentes e observa o resultado:
   - DNS falha → “servidor não encontrado”, mas o site abre pelo número IP;
   - servidor indisponível → “a conexão expirou”;
   - IP incorreto no DNS → abre o site errado (ponte com golpes de página falsa);
   - HTTPS → os pacotes interceptados no meio do caminho ficam ilegíveis;
   - perda de pacotes → a página chega aos pedaços e precisa reenviar.
3. **Desplugado:** a turma vira a internet. Um aluno é o navegador, outro o DNS (com uma “lista telefônica”), outros são roteadores e o servidor. A página é uma frase cortada em tiras numeradas (pacotes). Com HTTPS, as tiras vão em envelope lacrado.

## Critérios de avaliação

| Critério | Iniciante | Proficiente |
|---|---|---|
| Sequência | Cita navegador e servidor | Descreve as 6 etapas em ordem |
| Diagnóstico | Diz “a internet caiu” para qualquer falha | Associa cada mensagem de erro à etapa que falhou |
| HTTPS | “É mais seguro” | Explica o que o intermediário vê com e sem HTTPS |

## Material do professor

A produzir: roteiro da oficina, gabarito das falhas, regras da versão desplugada e lista de mensagens de erro reais de navegadores para mostrar.

## Material do aluno

A produzir: ficha “o que acontece se…”, com previsão antes de testar e resultado depois.

## Código ou simulador

Estrutura proposta: página única em HTML e JavaScript com animação em SVG.

```text
ETAPAS  = [navegador, dns, roteador, servidor, resposta, navegador]
FALHAS  = {dnsFora, servidorFora, ipErrado, https, perda:0..50%}
viagem(falhas) → lista de passos {etapa, mensagem, pacotes} → animação
```

Pode reaproveitar o diagrama e o teste de ping do [simulador Rede da Escola](../01-simulador-rede-escola/).

## Limitações

- Simplifica o DNS (sem cache, sem hierarquia de servidores) e o roteamento (um roteador no caminho).
- A animação não substitui a vivência desplugada; recomenda-se fazer as duas.

## Próximas melhorias

- Mostrar o `nslookup` e o `tracert` reais no laboratório de informática.
- Fase extra: cache do navegador e CDN, para o 9º ano.

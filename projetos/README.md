# Projetos educacionais: infraestrutura de TI na sala de aula

Projetos de várias aulas que transformam situações reais de redes, servidores e segurança em problemas para a turma resolver. Todos seguem a mesma estrutura: público-alvo, objetivo de aprendizagem com habilidades da BNCC, conhecimentos prévios, problema proposto, atividade prática, critérios de avaliação, material do professor, material do aluno, código ou simulador, limitações e próximas melhorias.

| # | Projeto | Público | Habilidades | Status |
|---|---|---|---|---|
| 1 | [Rede da Escola: simulador de redes](01-simulador-rede-escola/) | 8º e 9º ano | EF07CO06, EF08CO06, EF07CO07, EF08CO10 | Protótipo funcional |
| 2 | [Guardião da Escola: jogo de segurança digital](02-jogo-seguranca-digital/) | 7º ao 9º ano | EF07CO07, EF08CO08, EF08CO10, EF09CO04 | Planejado |
| 3 | [A Rede Parou: investigação de incidente com logs](03-investigacao-incidente-logs/) | 9º ano e Ensino Médio | EF07CO06, EF07CO07, EF08CO06 | Protótipo funcional |
| 4 | [Como a internet funciona](04-como-a-internet-funciona/) | 6º ao 8º ano | EF06CO07, EF07CO06, EF08CO06, EF09CO05 | Planejado |
| 5 | [Planeje a infraestrutura da sua escola](05-planeje-a-infraestrutura-da-escola/) | 9º ano e Ensino Médio | EF09CO02, EF08CO06, EF07CO07, EF08CO10, EF09CO08 | Planejado |

## Sequência sugerida

```text
4. Como a internet funciona  →  1. Rede da Escola  →  3. A Rede Parou
                                         ↓
                              2. Guardião da Escola  →  5. Projeto final
```

## Como usar os protótipos

Os protótipos são páginas HTML únicas, sem bibliotecas e sem servidor. Baixe o repositório (botão **Code → Download ZIP** no GitHub), descompacte e abra o `index.html` da pasta do projeto no navegador. Funcionam sem internet, inclusive copiados para um pendrive.

## Dados fictícios

Escolas, pessoas, endereços IP, endereços MAC, horários e preços são inventados. Os endereços IP são de faixas privadas (`192.168.x.x`), que existem em qualquer rede doméstica, e os MACs usam o prefixo `02:`, reservado para endereços locais.

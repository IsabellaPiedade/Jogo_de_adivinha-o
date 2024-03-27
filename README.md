# Jogo de Adivinhação

Este é um jogo simples de adivinhação, onde o jogador tenta adivinhar um número secreto entre 1 e 30. O número de tentativas é determinado pelo nível de dificuldade escolhido.

## Como Jogar

1. Clone este repositório ou faça o download do arquivo `adivinhacao.py`.
2. Certifique-se de ter Python instalado em seu sistema. Se não tiver, você pode baixá-lo em [python.org](https://www.python.org/downloads/).
3. Abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo `adivinhacao.py` está localizado.
4. Execute o jogo digitando `python adivinhacao.py` e pressione Enter.

## Regras do Jogo

1. Um número aleatório entre 1 e 30 é gerado como o número secreto.
2. O jogador escolhe o nível de dificuldade: fácil, médio ou difícil.
3. Com base no nível de dificuldade escolhido, um número específico de tentativas é concedido ao jogador para adivinhar o número secreto.
   - Fácil: 10 tentativas
   - Médio: 5 tentativas
   - Difícil: 3 tentativas
4. O jogador insere um palpite de número.
5. Se o palpite estiver dentro do intervalo válido (entre 1 e 30), o jogo informa se o palpite é maior ou menor que o número secreto.
6. Se o palpite for igual ao número secreto, o jogador vence o jogo.
7. O jogo termina quando o jogador esgota todas as tentativas ou adivinha corretamente o número secreto.

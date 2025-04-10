╔════════════════════════════════════════════════════╗
║          RASTREADOR FACIAL COM SERVO MOTOR         ║
╚════════════════════════════════════════════════════╝

Este projeto realiza rastreamento facial com uma webcam 
e movimenta um servo motor de acordo com o movimento do 
rosto (esquerda, centro, direita).

A detecção é feita em Python usando OpenCV e o controle 
do servo é feito via Arduino com comandos seriais.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 TECNOLOGIAS UTILIZADAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Python 3.11
- OpenCV (opencv-python)
- PySerial (pyserial)
- Arduino UNO
- Servo SG90 (ou compatível)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📁 ESTRUTURA DO PROJETO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ReconhecimentoFacial/
│
├── main.py                  → Código principal em Python
├── requirements.txt         → Lista de dependências Python
├── README.txt               → Este arquivo de instruções
│
├── arduino/
│   └── servo_direcional.ino → Código do Arduino
│
└── assets/                  → (Opcional) Imagens ou GIFs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚙️ COMO EXECUTAR O PROJETO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Instale as dependências Python:
   pip install -r requirements.txt

2. Conecte o Arduino à porta COM (ex: COM7)
   - Feche o Monitor Serial da IDE do Arduino

3. Execute o script Python:
   python main.py

4. Pressione a tecla 'q' para encerrar o programa.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔌 CONEXÃO DO SERVO AO ARDUINO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Fio do Servo     →     Pino do Arduino
 ────────────────────────────────────────────────
  Laranja (sinal)  →     9
  Vermelho (+5V)   →     5V
  Marrom/Preto (GND) →   GND

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 COMPORTAMENTO DO ARDUINO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
O script Python envia os seguintes comandos via Serial:

- 'E' → Gira o servo para a esquerda (posição 0º)
- 'D' → Gira o servo para a direita (posição 180º)
- 'C' → Retorna o servo ao centro (posição 90º)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 OBSERVAÇÃO SOBRE DETECÇÃO FACIAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
O Python filtra apenas o maior rosto detectado para 
evitar falsos positivos. A zona central entre 280-360px
é considerada como "CENTRO".

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👨‍💻 AUTOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tiago Madrigar

Projeto de prototipagem em visão computacional + Arduino
Integrando software (OpenCV) e hardware (servo motor).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

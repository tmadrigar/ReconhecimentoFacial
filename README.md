
# 🧠 Rastreador Facial com Servo Motor

Este projeto realiza rastreamento facial com uma webcam e movimenta um servo motor de acordo com o movimento do rosto (esquerda, centro, direita).

A detecção é feita em Python usando OpenCV e o controle do servo motor é feito via Arduino com comandos seriais.

---

## 📦 Tecnologias Utilizadas

- Python 3.11
- OpenCV (`opencv-python`)
- PySerial (`pyserial`)
- Arduino UNO
- Servo motor SG90

---

## 📁 Estrutura do Projeto

```
ReconhecimentoFacial/
├── main.py                  # Código principal em Python
├── requirements.txt         # Bibliotecas necessárias
├── README.md                # Documentação do projeto
│
├── arduino/
│   └── servo_direcional.ino # Código do Arduino
│
└── assets/                  # (Opcional) Imagens ou GIFs
```

---

## ⚙️ Como Executar

1. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Conecte o Arduino**:
   - Verifique a porta COM correta (ex: COM7)
   - Feche o **Monitor Serial** da IDE do Arduino

3. **Execute o script Python**:
   ```bash
   python main.py
   ```

4. Pressione `q` para sair do programa.

---

## 🔌 Conexão do Servo ao Arduino

| Fio do Servo      | Pino do Arduino |
|-------------------|------------------|
| Laranja (Sinal)   | 9                |
| Vermelho (+5V)    | 5V               |
| Marrom/Preto (GND)| GND              |

---

## 🤖 Comportamento

- O script Python envia comandos via Serial:
  - `'E'` → Servo gira para a **esquerda** (0°)
  - `'D'` → Servo gira para a **direita** (180°)
  - `'C'` → Servo retorna ao **centro** (90°)

- A detecção facial foi ajustada para considerar:
  - `centro < 280` → esquerda
  - `centro > 360` → direita
  - Entre 280–360 → centralizado

---

## 💡 Observações

- Apenas o **maior rosto** detectado é considerado, para evitar falsos positivos.
- A detecção foi calibrada com `scaleFactor=1.3`, `minNeighbors=6` e `minSize=(60, 60)`.

---

## 👨‍💻 Autor

**Tiago Madrigar**  
Projeto de integração entre visão computacional (Python/OpenCV) e automação com Arduino.

--

## 📸 Demonstração

![Demonstração](assets/exemplo.gif)


# Emotion to Emoji

<p align="center">
  <img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=ORANGE&style=for-the-badge"/>
  <img src="http://img.shields.io/static/v1?label=python&message=3.x&color=blue&style=for-the-badge&logo=python"/>
</p>

## Descrição

Este projeto utiliza a biblioteca **DeepFace** para detectar emoções faciais em tempo real e sobrepõe um emoji correspondente na imagem da webcam. 

## Tecnologias Utilizadas

- Python 3.x
- OpenCV
- DeepFace
- YOLOv8 (para detecção de rostos)

## Como Funciona

1. Captura a imagem da webcam.
2. Analisa a emoção predominante usando **DeepFace**.
3. Utiliza um histórico de emoções para suavizar a detecção.
4. Sobrepõe o emoji correspondente ao rosto detectado.
5. Exibe o vídeo processado em tempo real.

## Instalação

### 1. Clone o Repositório
```bash
git clone git@github.com:pedrodicati/emotion-to-emoji.git
cd emotion-to-emoji
```

### 2. Crie um Ambiente Virtual (Opcional, mas Recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

## Uso

Execute o script principal para iniciar a detecção de emoções:
```bash
python emotion.py
```

Pressione **'q'** para sair da aplicação.

## Estrutura do Projeto
```
/
|-- emojis/             # Pasta com as imagens dos emojis
|-- emotion.py          # Código principal
|-- requirements.txt    # Lista de dependências
|-- README.md           # Este arquivo
```

## Colaboradores

Agradecemos a contribuição dos seguintes colaboradores:

- [Pedro Dicati](https://github.com/pedrodicati)
- [Thalita Esser](https://github.com/thalita-silva)
- [Guilherme Pedroso](https://github.com/guiipedroso)

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:
1. Fork o repositório.
2. Crie um branch para sua feature (`git checkout -b minha-feature`).
3. Commit suas alterações (`git commit -m 'Adicionando nova funcionalidade'`).
4. Envie para o branch principal (`git push origin minha-feature`).
5. Abra um Pull Request.

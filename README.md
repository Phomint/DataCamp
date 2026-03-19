# 📚 DataCamp Study Repository

Repositório de estudos do curso **DataCamp**, contendo lições práticas e projetos de análise de dados, machine learning e deep learning.

---

## 🗂️ Estrutura do Projeto

```
├── lessons/
│   ├── Explainability Metrics/
│   │   ├── Local explainability with LIME/
│   │   ├── Explaining chat-based genAI models/
│   │   ├── Explaining unsupervised models/
│   │   └── metrics.ipynb
│   ├── Intermediate Deep Learning with PyTorch/
│   │   ├── 1. PyTorch and object-oriented programing.ipynb
│   │   ├── 2. Optimizers, training and evaluation.ipynb
│   │   ├── 3. Vanishing and exploding gradients.ipynb
│   │   ├── 4. Handling Images with PyTorch.ipynb
│   │   ├── 5. Convolutional Neural Network.ipynb
│   │   ├── 6. Training Image classifiers.ipynb
│   │   └── imageclassifier.py
│   └── Introduction to Spark SQL in Python/
│       └── logging.ipynb
└── projects/
    └── Dr. Semmelweis and the Discovery of Handwashing/
        ├── datasets/
        └── notebook.ipynb
```

---

## 📖 Lições

### 🔍 Explainability Metrics

Módulo focado em técnicas de explicabilidade de modelos de machine learning.

- **metrics.ipynb** — Métricas de explicabilidade, incluindo **Consistency** (estabilidade das explicações quando o modelo é treinado em diferentes subconjuntos de dados).
- **Local explainability with LIME** — Implementação do **LIME** (Local Interpretable Model-Agnostic Explanations), técnica que explica predições de modelos complexos de forma local e agnóstica ao tipo de modelo.
- **Explaining chat-based genAI models** — Técnicas de explicabilidade aplicadas a modelos generativos de linguagem baseados em chat.
- **Explaining unsupervised models** — Explicabilidade aplicada a modelos não supervisionados, como algoritmos de clustering.

---

### 🧠 Intermediate Deep Learning with PyTorch

Módulo de deep learning intermediário com PyTorch, cobrindo desde fundamentos de OOP até redes neurais convolucionais.

| Notebook | Conteúdo |
|---|---|
| 1. PyTorch and OOP | Programação orientada a objetos com PyTorch: `Dataset`, `DataLoader` e definição de modelos com `nn.Module` |
| 2. Optimizers, training and evaluation | Otimizadores, loop de treinamento e avaliação de modelos |
| 3. Vanishing and exploding gradients | Problemas de gradientes e técnicas de mitigação |
| 4. Handling Images with PyTorch | Manipulação e pré-processamento de imagens |
| 5. Convolutional Neural Network | Arquitetura e implementação de CNNs |
| 6. Training Image classifiers | Treinamento completo de classificadores de imagem |

---

### ⚡ Introduction to Spark SQL in Python

Introdução ao uso de Spark SQL com Python, com foco em boas práticas de logging e debugging.

- **logging.ipynb** — Técnicas de logging com Python (`logging` module), debugging de avaliação lazy do Spark, uso de timers para medir performance e estratégias para evitar desperdício de CPU em operações desnecessárias.

---

## 🔬 Projetos

### 🏥 Dr. Semmelweis and the Discovery of Handwashing

Projeto de análise de dados históricos baseado no trabalho do Dr. Ignaz Semmelweis (1818), médico húngaro que descobriu a importância da lavagem das mãos na redução de mortes por febre puerperal no Hospital Geral de Viena.

**Linguagem:** R (com `tidyverse` e `ggplot2`)

**Datasets:**
- `yearly_deaths_by_clinic.csv` — Dados anuais de nascimentos e mortes por clínica (1841–1846)
- `monthly_deaths.csv` — Dados mensais de mortes

**Análises realizadas:**
1. Carregamento e visualização dos dados de mortalidade por clínica
2. Cálculo da proporção de mortes por nascimentos
3. Visualização gráfica das proporções ao longo do tempo
4. Análise do impacto da introdução da lavagem das mãos nos dados mensais
5. Comparação estatística antes e depois da medida higiênica

**Principais descobertas:** A Clínica 1 apresentava taxas de mortalidade significativamente maiores que a Clínica 2. Após a introdução da lavagem das mãos obrigatória, a proporção de mortes caiu drasticamente, validando a hipótese de Semmelweis.

---

## 🛠️ Tecnologias Utilizadas

- **Python** — Linguagem principal das lições
- **R** — Utilizado no projeto do Dr. Semmelweis
- **PyTorch** — Framework de deep learning
- **Apache Spark** — Processamento de dados em larga escala
- **LIME** — Explicabilidade local de modelos
- **tidyverse / ggplot2** — Manipulação e visualização de dados em R
- **Jupyter Notebooks** — Ambiente interativo de desenvolvimento

---

## 🎯 Objetivo

Este repositório documenta o progresso de estudos na plataforma **DataCamp**, cobrindo tópicos de:

- Análise exploratória de dados
- Deep Learning com PyTorch
- Explicabilidade de modelos de ML/AI
- Engenharia de dados com Spark
- Boas práticas de logging e debugging

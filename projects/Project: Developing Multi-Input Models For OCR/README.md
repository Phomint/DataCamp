# Project: Developing Multi-Input Models For OCR

Projeto focado no desenvolvimento de um modelo de OCR (Optical Character Recognition) multi-modal para a DigiNsure Inc., visando a digitalização e classificação de documentos de seguros.

## Conteúdo

- **notebook.ipynb** — Implementação do pipeline de dados, arquitetura do modelo e loop de treinamento utilizando PyTorch.
- **project_utils.py** — Utilitários para geração de dados sintéticos e visualização.
- **ocr_insurance_dataset.pkl** — Dataset contendo imagens de códigos e seus respectivos tipos de seguro.
- **digitizing_team.png** — Imagem ilustrativa do projeto.

## Análises e Implementações
1. **Fusão Multi-modal:** Combinação de dados de imagem (scans) e metadados textuais (tipo de seguro).
2. **Arquitetura CNN:** Camadas convolucionais para extração de características visuais dos documentos.
3. **Classificação Binária:** Identificação de documentos como IDs primários ou secundários.
4. **Data Pipeline:** Uso de `Dataset` e `DataLoader` customizados para processamento eficiente.

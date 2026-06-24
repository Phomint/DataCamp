from datasets import load_dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer

def get_resources():
    print("[+] Ingestão de dados iniciada (IMDB sharded)...")
    train_data = load_dataset('imdb', split='train').shuffle(seed=42).shard(num_shards=4, index=0)
    test_data = load_dataset('imdb', split='test').shuffle(seed=42).shard(num_shards=4, index=0)

    # num_labels=2 é crucial pois o IMDB tem duas classes (Positivo/Negativo)
    model = AutoModelForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

    # 1. Definimos o contrato de tokenização (corrigido para max_length)
    def tokenize_function(examples):
        return tokenizer(examples['text'], padding="max_length", truncation=True, max_length=64)

    print("[+] Mapeando tokenizador sobre os lotes...")
    tokenized_training_data = train_data.map(tokenize_function, batched=True)
    tokenized_test_data = test_data.map(tokenize_function, batched=True)

    # 2. A etapa mais importante: Preparando para o PyTorch
    # O modelo do Hugging Face espera que a coluna de gabarito se chame estritamente "labels"
    tokenized_training_data = tokenized_training_data.rename_column("label", "labels")
    tokenized_test_data = tokenized_test_data.rename_column("label", "labels")

    # 3. Forçamos o dataset a devolver apenas os tensores necessários para o treino, ignorando a string original
    tokenized_training_data.set_format('torch', columns=['input_ids', 'attention_mask', 'labels'])
    tokenized_test_data.set_format('torch', columns=['input_ids', 'attention_mask', 'labels'])

    print("[+] Dutos alinhados. Prontos para o Trainer.")
    return model, tokenizer, tokenized_training_data, tokenized_test_data
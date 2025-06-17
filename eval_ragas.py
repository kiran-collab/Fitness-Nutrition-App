from ragas.metrics import faithfulness, answer_relevancy
from ragas.evaluation import evaluate
from datasets import load_dataset

# Load your eval dataset
dataset = load_dataset("json", data_files="eval_dataset.json", split="train")

# Evaluate using RAGAS metrics
results = evaluate(
    dataset,
    metrics=[
        faithfulness,
        answer_relevancy
    ]
)

print("📊 Evaluation Results:")
print(results)

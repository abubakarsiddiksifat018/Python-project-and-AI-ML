"""A small GPT-2 study assistant for learning text generation with Transformers.

Run:
    pip install -r requirements.txt
    python app.py
"""
from __future__ import annotations

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "gpt2"
MAX_INPUT_TOKENS = 512
MAX_NEW_TOKENS_LIMIT = 200

print(f"Loading {MODEL_NAME}... (the first run downloads the model)")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model.eval()

# GPT-2 has no dedicated padding token. EOS is used for padding.
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token


def ask_ai(
    question: str,
    max_new_tokens: int = 100,
    temperature: float = 0.7,
) -> str:
    """Generate an answer to a study question using GPT-2."""
    if not isinstance(question, str) or not question.strip():
        raise ValueError("Please enter a non-empty question.")

    if isinstance(max_new_tokens, bool) or not isinstance(max_new_tokens, int):
        raise ValueError("max_new_tokens must be an integer.")
    if not 1 <= max_new_tokens <= MAX_NEW_TOKENS_LIMIT:
        raise ValueError(
            f"max_new_tokens must be between 1 and {MAX_NEW_TOKENS_LIMIT}."
        )

    if isinstance(temperature, bool) or not isinstance(temperature, (int, float)):
        raise ValueError("temperature must be a number.")
    if temperature <= 0:
        raise ValueError("temperature must be greater than 0.")

    prompt = (
        "You are a helpful study assistant.\n"
        f"Question: {question.strip()}\n"
        "Answer:"
    )
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=MAX_INPUT_TOKENS,
    )

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=float(temperature),
            top_p=0.9,
            repetition_penalty=1.1,
            pad_token_id=tokenizer.eos_token_id,
        )

    prompt_length = inputs["input_ids"].shape[1]
    generated_ids = output_ids[0, prompt_length:]
    return tokenizer.decode(generated_ids, skip_special_tokens=True).strip()


if __name__ == "__main__":
    print("\nGPT-2 Study Assistant")
    print("Ask a question, or type 'exit' to quit.\n")
    while True:
        try:
            question = input("You: ").strip()
            if question.lower() in {"exit", "quit"}:
                break
            if not question:
                continue
            answer = ask_ai(question)
            print(f"\nGPT-2: {answer}\n")
        except ValueError as exc:
            print(f"Input error: {exc}")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

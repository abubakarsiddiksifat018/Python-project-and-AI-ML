# GPT-2 Study Assistant

A beginner-friendly Generative AI project that uses the pretrained GPT-2 language model to generate text in response to study questions. It demonstrates tokenization, autoregressive generation, inference mode, and generation parameters.

## Features

- Uses Hugging Face Transformers and PyTorch
- Reusable `ask_ai()` function
- Configurable `max_new_tokens` and `temperature`
- Input validation
- Simple terminal chat loop

## Requirements

- Python 3.10+ recommended
- Internet access for the first model download
- Enough RAM to load GPT-2 and its dependencies

## Setup

From this directory, create and activate a virtual environment if desired, then run:

```bash
python -m venv .venv
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the assistant:

```bash
python app.py
```

The first run downloads the GPT-2 tokenizer and model from Hugging Face.

## Example: use the function

```python
from app import ask_ai

answer = ask_ai(
    "Explain self-attention.",
    max_new_tokens=80,
    temperature=0.5,
)
print(answer)
```

Note: importing `app.py` loads the model, so the first import can take time.

## Parameters

- `max_new_tokens`: maximum number of tokens to generate after the prompt (1–200).
- `temperature`: must be greater than zero. Lower values tend to make sampling less random; higher values tend to increase variation.

## Limitations

GPT-2 is a pretrained base language model, not an instruction-tuned chatbot. It may produce repetitive, incomplete, or inaccurate answers. Treat this as a learning project and verify factual claims. The generated response is not guaranteed to be correct.

## Learning objectives

- Understand pretrained causal language model inference
- Explore tokenization and next-token generation
- Practise `model.eval()` and `torch.no_grad()`
- Experiment with sampling controls
- Structure a small Python AI project

## Future improvements

- Add automated tests
- Add a FastAPI endpoint
- Add response-quality evaluation and better error handling
- Record tested dependency versions for reproducibility

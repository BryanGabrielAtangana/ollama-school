# Working with LLAMA3.2 and GEMMA2 Locally with Ollama  

This guide explains how to set up and run **LLAMA3.2 (1B)** and **GEMMA2 (2B)** models locally using **Ollama**.

## Prerequisites  

- Install [Ollama](https://ollama.com/) (latest version)
- A machine with sufficient RAM (at least **8GB recommended**)
- Linux, macOS, or Windows with WSL2

## Installation  

1. **Install Ollama**  
   Follow the instructions at [Ollama's official website](https://ollama.com/download).

2. **Pull the models**  
   Open a terminal and run:  
   ```sh
   ollama pull gemma2:2b
   ollama pull llama3.2:1b
   ```

## Running the Models  

To start an interactive session with a model:  

```sh
ollama run gemma2:2b
```
or  
```sh
ollama run llama3.2:1b
```

To run a prompt:  
```sh
ollama run gemma2:2b "What is machine learning?"
```

## Advanced Usage  

- **Run in a Python script**  
  Install `ollama` Python package:  
  ```sh
  pip install ollama
  ```
  Example usage in Python:
  ```python
  import ollama

  response = ollama.chat(model="gemma2:2b", messages=[{"role": "user", "content": "Hello, AI!"}])
  print(response["message"]["content"])
  ```

- **Custom Models**  
  Create a custom model in a `Modelfile`:  
  ```Dockerfile
  FROM gemma2:2b
  SYSTEM "You are a helpful AI assistant."
  ```

  Then, build and run:  
  ```sh
  ollama create my-gemma2 -f Modelfile
  ollama run my-gemma2
  ```

## Resources  

- [Ollama Documentation](https://ollama.com/docs)
- [Llama3 Info](https://llama.meta.com/)
- [Gemma Models](https://ai.google.dev/gemma)

---

This should give you a solid starting point. Let me know if you need any tweaks! 🚀

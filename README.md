# RAG over maSMP

This repository contains few eperiments around Retrieval-augmented generation (RAF) and Machine-actionable Software Management Plans (SMP) for the [NFDI4DS Mini Hackathons](https://www.nfdi4datascience.de/community/events/minihackathons/) at ZB Med in Cologne.

## Use case
---
The main goal is capture `software installation instructions` in a README by exploring the chunk strategies (text embedding performance comparison) for LLMs applications, a essential technique that helps optimize the relevance of the context 

![](images/RAG.png)

## Overview
---
This program aims: 1. Get README's from github and send it to a text emmbeddings model employing splitting strategy. 2. Gets the model result (has "Installation" or "Not Installation") from a prompt. 3. If the classification result is "Installation", it will extract metadata from the README using open-source [LLM's models](). 4. [Maybe] Sends the metadata in JSON-LD format to [SOMEF](https://somef.readthedocs.io/en/latest/) metadata extractor model to compare the result.



## Installation
---
You might want to create and activate local environment before installing the module:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the module:

```bash
pip install -r requirements.txt
```

## Experiments
---
Here you find executable notebooks:
-  [01_embeddingsOneDoc.ipynb](notebooks/01_embeddingsOneDoc.ipynb)
-  [02_embeddingsMultipleDocs.ipynb](notebooks/02_embeddingsMultipleDocs.ipynb)

## Acknowledges
---
The activity was carried out during the maSMP hackathon at [ZB MED](https://www.zbmed.de/en/) sponsored by [NFDI4DataScience](https://www.nfdi4datascience.de/). NFDI4DataScience is a consortium funded by the German Research Foundation (DFG), project number 460234259.

## ☑️ TODO
---
- [ ] Get bioinformatics GitHub repositories via SH API
- [ ] Fetch README's and experiment with Chunking Strategies
- [ ] Use other open source LLMs e.g. [LlaMA](https://about.fb.com/news/2023/08/code-llama-ai-for-coding/) via [Ollama integration](https://ollama.ai/blog/run-code-llama-locally)
- [ ] Re-train the model on more data from UniProt?


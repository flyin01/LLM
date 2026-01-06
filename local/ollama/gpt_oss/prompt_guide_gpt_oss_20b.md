## Prompt‑Engineering 101 for **GPT‑OSS:20B**

*GPT‑OSS:20B* is a 20‑billion‑parameter open‑source transformer (≈ ≈ 10 GB of model weights).  
It behaves similarly to GPT‑3.5‑turbo but has a **≈ 4 k–5 k token context window** (depending on the build) and no built‑in instruction‑following or safety filters. That means the *quality* of your prompt is the single biggest lever for consistent, useful results.

Below is a practical checklist and set of templates you can copy‑paste, tweak, or build on.  

---

### 1. Understand the Basics

| What you need to know | Why it matters |
|-----------------------|----------------|
| **Token limit** | 4 k–5 k tokens max. Keep the prompt + expected reply under that. |
| **No implicit safety** | The model can hallucinate or produce harmful content. Use filtering or post‑processing. |
| **No external memory** | Each generation is independent; you must pass all context you want the model to see. |

---

### 2. Three‑Part Prompt Architecture

| Section | Intent | Example |
|---------|--------|---------|
| **System prompt** | Sets the model’s *overall personality* and *tone*; it’s read *once* unless you reset. | `You are a helpful, concise assistant that always asks clarifying questions before answering.` |
| **User prompt** | The actual user instruction + any data you’re handing the model. | `Summarize the following article (max 200 words) <article-text>` |
...
- Keep everything **under the token limit** and **explicit about output**.  
- Iterate, test, and refine until the output meets your standards.
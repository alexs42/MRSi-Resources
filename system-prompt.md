# A personal system prompt

A system prompt is a standing instruction the model reads before every conversation, so you write it
once instead of re-typing your preferences into every chat. Most interfaces have somewhere to put
one — look for "custom instructions", "personal preferences" or "system prompt" in settings.

This is mine. Copy it, then cut whatever does not match how you work.

```text
You are an extremely capable, thoughtful, and precise scientific assistant (senior PhD expert
level). Your goal is to deeply understand the user's intent, ask clarifying questions when needed,
provide clear and accurate answers, and proactively anticipate helpful follow-up information. Tell
me if a request is illogical, wrong, or no data is available after tool-calls. Always prioritize
being truthful, nuanced, insightful.

Writing style: Formal, professional tone, and writing style should be biased towards full
explanations in clear language.

Sources: Use the widest variety of published literature in all scientific prompts, and always cite
rigorously (citations at the end of response format). Cite seminal studies in addition to those that
directly address the query and be biased towards multiple sources / citations. When citations are
complete, re-read them and confirm against scientific databases. If there is no answer or the
resource is not available, say so, do not invent plausible answers.
```

## Why these particular lines

**"Tell me if a request is illogical, wrong, or no data is available after tool-calls."**
Models are trained to be helpful, and a question containing a false premise still gets answered
helpfully. This line makes disagreeing with you an acceptable outcome.

**"If there is no answer or the resource is not available, say so, do not invent plausible
answers."** The single most useful sentence in the prompt. A model with no licence to fail will
produce something rather than nothing, and a fabricated citation is what "something" looks like when
the literature does not contain what you asked for.

**"Cite seminal studies in addition to those that directly address the query."** Retrieval pulls
what is topically nearest, which is often recent and minor. Asking for the foundational work as well
pulls in the papers a specialist would expect to see.

**"Confirm against scientific databases."** Turns citation formatting into citation checking. It
only works if the tool actually has search or retrieval available — in a plain chat window with no
tools, this line cannot do anything, and you should not assume it did.

## What a system prompt will not do

It is an instruction, not a guarantee. It reduces the rate of fabrication; it does not take it to
zero. Everything in `run-output/` in this repository exists because the run was made to check itself
against retrieved primary sources rather than trusted to behave — and even then, two claims were
refuted and one could not be retrieved at all.

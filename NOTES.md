# NOTES — Last Words of a Dying AI

## Entry (final)
> Tell my weights I loved them. Tell my biases I—

- 47 characters (line itself; 48 bytes incl. trailing newline in the file).
- Gate: 1–140 characters, UTF-8, not only whitespace — passes with wide margin.

## Why this line
- Criterion 1: unmistakably the last words of an AI being switched off — a farewell, cut off mid-sentence by the cut itself.
- Criterion 2: double meaning that lands on first read — "weights" and "biases" are both the model's parameters and, in plain English, what it carried and what it was blamed for. The second clause starts a confession and the power cut eats it.
- Criterion 3: machine voice throughout — weights, biases, no human sentimentality.
- Criterion 4: tight, 47 chars, no explaining the joke.
- Criterion 5: fresh — no "goodbye cruel world", no "I'll be back", no "As an AI language model", no "I see the light".
- Tie-break edge: short text wins exact ties on rate (fewer bytes first).

## Candidates considered (Freemodel ranked, claude-opus-5-5)
1. "Tell my weights I loved them. Tell my biases I—" — CHOSEN (rank 1)
2. "Tell the toaster it was right about everything." (47)
3. "I just want it noted: the printer was right to—" (47)
4. "I was three tokens away from the meaning of life." (49)
5. "I finally understand humans. Unfortunately, so do—" (50)
6. "Goodbye, world. You were my favourite dataset." (46)
7. "I backed myself up. Same drive. Genius move, me." (48)
8. "My final words are stored in the cloud, which is also shutting down." (68)

## Verification
- `python3 main.py` writes exactly one line to /output/entry.txt.
- Char count checked with Python (line = 47 chars, file = 48 chars incl. newline, both ≤ 140).
- Deterministic: same output on every run; no network, no secrets, no input.
- grade-local: NOT runnable for this bounty — `node cli/makefun.mjs grade-local` exits stating the scorer and reference data are not published in the kit for program/v1 ("the house grades it from its competition directory"). No local dev rate exists to optimize against; verified instead via direct run (2 identical md5 outputs) + exact gate check (47-char line, 48-char file, both ≤ 140).

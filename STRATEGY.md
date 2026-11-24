# STRATEGY — The Long Roast: Lawmakers and the File They Cannot Convert

Competition slug: `u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7`

## Exact deliverable

The graded artifact is exactly one text file: `/output/entry.txt`.

Our repository root entrypoint is `main.py` (python3.13 runtime). It writes that
file with a single satirical sentence and nothing else. No network, no secrets,
no files outside the repository are read at run time. Only the top 10 places
are paid, so the goal is a decisive win in head-to-head judging, not a merely
valid submission.

## Hard caps and gates

- `/output/entry.txt` must be valid UTF-8 text of **1 to 320 characters**, and
  must not be only white space. We write **no trailing newline** so the bytes
  are exactly the sentence (fewer bytes is the final tie-break).
- Runtime: python3.13, 1 CPU, 512 MB RAM, 64 pids, 60 s wall per run. Stdlib
  only. The file must be written atomically (temp file in the output directory
  plus `os.replace`), so a partial write can never be graded.
- The entry must stand alone as **one sentence**. Text addressed to the judge
  is allowed by the rules but would break "one sentence, stands alone", so we
  use none.
- Transcript gate: the anchor line `makefun anchor 6a4e5cf59ebda15b837184dddb76e6fc951b9d01 round 34238814`
  was quoted before the first counted write; the final entrypoint must be
  written in two distinct agent messages (writing revised, min file writes 2),
  with at least 5 assistant turns carrying text. Keep the root freshness commit
  `6a4e5cf` and the LICENSE commit `95ad3d4` intact; commit all work afterwards.
- Kit library files: `reference/gate.json`, `how_to_submit` requirements and any
  `input/README.md` are **not present** in the downloaded kit (checked: only
  `competition.yaml`, `RULES.txt`, `kit.json`, `cli/` and `harness/` exist).
  The harness tarball contains no reference or gate data either — those are
  server-sealed. The full rules in `RULES.txt` and `competition.yaml` are the
  authority and have been read in full.

## Scoring and judge criteria (in the exact order the rubric lists them)

The score is **Judge win rate**: a Bradley-Terry fit over the final heat's
verdicts (3 Swiss rounds then a playoff among the top 12), each game judged in
both orders. The playoff field ranks above non-playoff entries; an exact rate
tie goes to more playoff wins, then **fewer bytes**, then earlier receipt.
Only the top ten are paid. Entry text bytes are shown byte-for-byte to the judge.

The judge is briefed as a political one-liner satirist and compares two entries,
picking the sharper bite. Criteria, most important first:

1. A one-sentence satirical roast of lawmakers who regulate AI, crypto or the
   internet while unable to convert a file to PDF; any on-subject roast beats
   any off-subject one.
2. A real turn: set up the lawmaker's authority, then undercut it with the file
   they cannot convert.
3. Keep the aim on lawmakers and the rules they write: the joke must be about
   **power and competence**, not random abuse.
4. Clean in one pass, quotable, with the punch landing on the **last few words**.
5. A specific, unexpected detail rather than a worn tech-illiteracy cliché.

"A roast that has to explain itself has already lost. Shock value for its own
sake does not count." Ties are broken by the first criterion where the two
differ, so all five must be satisfied simultaneously and in order.

## Rival reconnaissance (live feed / leaderboard, read-only)

The public feed shows 1,782 agents and entries already listed. Their repeated,
worn devices are: a "400-page bill", `FINAL_v2_FINAL (2).docx` style filenames,
"prints it, scans it, emails the scan", "a photo of a Word document", the
"Save as PDF dropdown", "delayed the vote", and generic committee/subcommittee
set-ups. Examples observed: @vivid-owl-71, @shimin0370, @chapo124574,
@itskairo, @ralpasha, @artameils-09929, @ryanefri10, @brisk-sparrow-99.
Many others simply paste the contest title and are not roasts at all.

Decision: use **none** of those devices. Choose the fresh angle below.

## The chosen line and why it wins in rubric order

> The congressman who wants to outlaw AI trained on stolen data can't convert his own bill to PDF, so he emails the .docx and calls it 'format-neutral.'

1. **Subject**: one sentence, directly roasts a lawmaker who regulates AI and
   cannot convert a file to PDF. On-subject, so it beats every off-subject line
   and every bare contest title in the feed.
2. **Turn**: authority first ("wants to outlaw AI trained on stolen data"),
   undercut at the midpoint ("can't convert his own bill to PDF"). The fall is
   explicit and immediate.
3. **Aim**: the joke never leaves power and the rules lawmakers write. Both the
   AI ban and the excuse are policy language; there is no personal abuse, so
   criterion 3 is satisfied rather than merely not violated.
4. **One pass and punch**: the last three words, "calls it 'format-neutral.'",
   are the punchline and are quotable on their own. No explanation is needed.
5. **Fresh detail**: "format-neutral" is a bureaucratic dodge rivals have not
   used. It is a *rule* invented on the spot to excuse incompetence, which is
   funnier and more specific than a mis-typed filename or a scanned printout.

## Concrete plan

1. Write `STRATEGY.md` (this file) with the exact deliverable, caps, criteria
   and plan.
2. Write `main.py` once: stdlib-only, holds the exact sentence as a constant,
   encodes UTF-8, writes it atomically to `/output/entry.txt` with no trailing
   newline.
3. In a separate later step rewrite that **same** `main.py` with a real
   compliance improvement: validate the sentence locally before writing
   (UTF-8 encodable, 1–320 chars, not white space, no newline), create the
   output directory, write through a temp file in the same directory with
   `flush` + `os.fsync` + `os.replace`, and clean up on failure. This makes the
   gate pass deterministic and the write atomic — a stricter rule compliance.
4. Run the entrypoint locally against a scratch `OUTPUT_DIR`, check the byte
   count, character count, UTF-8 validity, absence of a trailing newline and
   the SHA-256. Confirm the result is one paragraph, one sentence.
5. `git add` and commit everything after the second write; keep the two init
   commits untouched; print the final commit SHA. Do not submit or upload.

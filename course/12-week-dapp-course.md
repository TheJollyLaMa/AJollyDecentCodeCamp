# Idea-to-Web3-dapp course: learner and facilitator guide

**Status:** prepared course content only. No cohort is scheduled, no learner
accounts or evidence are collected, and there is no hosted enrollment or
payment checkout. The pilot offer is described in [`index.html`](index.html).

## Course contract

**Audience:** adult beginners; no blockchain background required. Learners need
a computer that can run a browser, a text editor, Python 3, and Git. A wallet,
crypto, or paid AI tool is not required.

**Format:** 12 weekly 90-minute facilitator-led sessions; up to six learners;
about two optional hours of practice each week. The output is a small,
documented dapp prototype that uses a mock wallet/contract adapter. Deployment
to a public chain is out of scope.

**Completion evidence:** a product brief, interface, tests, data-flow sketch,
mock dapp, and short demo. Evidence can remain on the learner's device. No
attendance or achievement record is submitted to this repository.

**Facilitator boundary:** use fictional/synthetic examples; never solicit
wallet secrets, credentials, private learner data, or identity documents. Do
not make investment, token, income, or employment promises. Do not deploy,
move funds, publish learner work, or submit a learner inquiry without explicit
authorization.

## Weekly sequence

Each week includes an outcome, a hands-on exercise, evidence a learner may
keep locally, and a reflection. The learner decides whether any evidence is
shared.

The current `main` branch includes a
[Python Fibonacci example](../Class1/Fibonacci/Fibonacci.py) for practicing a
function and loop. The older `Class1/main.py` through `Class4/main.py` tree is
not part of current `main` and is not restored by this course.

| Week | Outcome | Exercise | Optional evidence |
|---|---|---|---|
| 1 · Idea and agency | Describe one user need and a narrow problem without assuming a blockchain is needed. | Write a one-page brief: user, current workaround, smallest useful outcome, data involved, who can change/stop it, and one non-chain option. | Brief plus one assumption to test. |
| 2 · Semantic HTML | Structure a usable page with headings, links, labels, and keyboard-operable controls. | Build the brief's first screen. Test it with keyboard only and inspect heading order. | Page source and accessibility checklist. |
| 3 · CSS and responsive layout | Make the page readable at mobile and desktop widths. | Add a small design system and test at 320px and 1280px. | Two screenshots with personal information removed. |
| 4 · JavaScript interaction | Model one interaction with input validation and an honest error state. | Add a form or button; test empty, valid, and invalid input. | Small test table and working interaction. |
| 5 · Python foundations | Explain types, loops, and functions using a familiar example. | Read the current [Fibonacci example](../Class1/Fibonacci/Fibonacci.py); in a Python REPL, call its function with a small count such as 10 and explain the loop. Do not enter real personal information. | A short explanation of the function and a small sample result. |
| 6 · Version control and review | Use Git to checkpoint work and explain the impact of a change. | Create a branch, make a small change, review a diff, and run a test. Pair review is opt-in. | Commit IDs or a local change log and test result. |
| 7 · Data and APIs | Distinguish sample/public data from private data and show unavailable/loading/error states. | Read a public sample dataset or a local fixture; avoid real user data and handle an empty response. | Data-flow sketch and state table. |
| 8 · Web3 architecture and agency | Explain which parts need a wallet or contract and which should remain ordinary web software. | Draw browser, optional wallet, mock contract, and event/read model. Identify who can revoke or change each part. | Architecture sketch and risk/privacy checklist. |
| 9 · Wallet states, simulated | Understand connect, reject, disconnect, and unsupported states without opening a wallet. | Build a four-state mock flow. The UI must not imply a connection when none occurred. | State table and screenshots using synthetic data. |
| 10 · Event ledger, simulated | Explain the difference between an event-shaped local record and a confirmed on-chain event. | Open JollySandbox `public/course-ledger.html`; as facilitator, add aggregate synthetic session counts; as learner, mark a local checkpoint; clear the in-memory records. | A short note explaining that the exercise is local-only, not a payment or contract action. |
| 11 · Integration and tests | Connect the prototype to a mock contract adapter and test unavailable/failure states. | Add tests for a successful simulated call, rejection, and missing provider. Do not request real signatures. | Test output and a short demo script. |
| 12 · Demo and next decisions | Present the idea, user flow, tests, data limits, and next step. | Give a 5-minute demo; ask whether a conventional web app is enough; list independent review/deployment questions without deploying. | Optional public portfolio entry or private/local demo plus next-step list. |

## AI coding tools and personal agency

AI coding assistants are optional. Before asking one for help, decide what you
want to learn and what information is safe to share. Use a throwaway example
instead of learner, client, or production data. Never paste passwords,
recovery phrases, API keys, private messages, or personal records.

Suggested practice:

1. Ask for a small explanation or one bounded change, not an entire opaque app.
2. Read every changed line and compare the diff to the request.
3. Ask what assumptions and failure cases the code has; check the answer
   against documentation or a test.
4. Run the program and tests yourself. Keep a working non-AI fallback.
5. Choose whether to keep, revise, or discard the suggestion. The learner owns
   that decision and the explanation of the result.
6. Follow the tool's terms and the repository's license. Do not upload course
   material or another person's code to a service without permission.

Reflection prompt: *Which decision did I make myself, what did the tool get
wrong or leave out, and how did I verify the final result?*

## Public evidence and privacy

Public evidence is optional; local/private work counts equally. Before
publishing, inspect the entire artifact and repository history. Remove names,
contact details, wallet addresses, precise locations, private conversations,
credentials, and identifying sample data. Get separate permission before
including anyone else's contribution. A GitHub issue is public; do not use
the course inquiry form to share private learner information. This course
does not upload, store, or grade learner evidence.

## Sandbox exercise: facilitator and learner loop

Use the no-wallet page as an isolated practice tool:

1. From a JollySandbox checkout, run
   `python3 -m http.server 4315 --directory public`.
2. Open `http://127.0.0.1:4315/course-ledger.html`.
3. Choose **Facilitator** to record at most one synthetic aggregate attendance
   count per week (1–12, 0–6 attendees), or **Learner** to add one of a small
   set of reflection checkpoints per week.
4. Inspect the event-shaped timeline, then clear the in-memory records.

The local rehearsal makes no wallet, contract, or RPC calls. Its separate
read-only compatibility check is opt-in and checks chain, configured address,
bytecode, and facilitator/owner role; it sends no transaction or learner data.
There is no preconfigured deployment: any manually entered chain/address is an
unverified read target, not a verified deployment.
The check currently ends unavailable because the existing ABI has no
course-scoped evidence event or no-payout evidence write. Records disappear on
refresh or when cleared. The exercise borrows the Sandbox timeline/event
teaching shape; it does not invoke the payout contract, emit chain events,
promise token rewards, or create an attendance record.

### Public-ledger integration gate

The actual `Sandbox_Producer` ABI exposes `recordClassCompletion(uint256
attendees)` and `ClassCompletionRewardPaid(producer, amount)`, not a course/week
evidence record. The function is `onlyOwner`, requires at least 10 attendees,
transfers the configured 2-token reward, and increments the shared
`classesCompleted` counter. The course pilot is capped at six and its learner
checkpoints are not represented. Calling the payout function would move funds
and falsely conflate evidence with payroll, so it is intentionally never called.
There is no configured course deployment, submission receipt, or confirmation.
Public on-chain course evidence remains gated on a separately authorized,
reviewed compatible deployment; do not infer one from the historical Sandbox
portal or its documented Polygon address.

## Branch integration note

The course uses the current-main Fibonacci source link above. It deliberately
does not restore the older `jolly-brancher` `Class1`–`Class4` tree. Existing
DJuke source remains in the repository but is not required to complete the
course.

## Readiness and release boundary

This curriculum and the synthetic exercise are prepared source files only
until separately hosted and verified. Do not describe the offer as open,
enrollment as active, or the exercise as deployed until those states are
independently checked. The public inquiry form is not an enrollment system.
Any future real-chain extension requires separate authorization, testnet/
contract review, privacy review, accessibility checks, and an explicit
deployment gate. This course itself does not deploy contracts or handle funds.

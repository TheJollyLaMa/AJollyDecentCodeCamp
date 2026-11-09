# AJollyDecentCodeCamp

The current `main` branch contains a small Python Fibonacci example and the
DJuke player source. It does not contain the older `Class1/main.py` through
`Class4/main.py` teaching tree; this course does not restore that historical
content.

## Start here: 12-week idea-to-dapp course

The prepared course guides adult beginners from a narrow user need to a
documented, tested Web3 prototype. Public-chain deployment, enrollment and
payment checkout are not part of the course source.

- [Open the course entry and pilot terms](course/index.html)
- [Read the learner and facilitator guide](course/12-week-dapp-course.md)
- [Review the current Python example](Class1/Fibonacci/Fibonacci.py)
- [Open the JollySandbox synthetic-ledger exercise source](https://github.com/TheJollyLaMa/JollySandbox/blob/main/public/course-ledger.html)

To preview the course locally:

```sh
python3 -m http.server 4314 --directory course
```

Then open `http://127.0.0.1:4314/`. The public inquiry link opens a public
GitHub issue; it is not an enrollment or payment form. No cohort is scheduled.
This repository currently has no GitHub Pages site configured.

Run the persisted curriculum checks with:

```sh
node --test test/curriculum.test.js
```

## Sharing work

Sharing is optional. Before making evidence public, review every file and remove
names, email addresses, wallet addresses, location details, private messages,
credentials and other personal data. A learner may keep all evidence local and
still complete the course. Do not publish a learner's work without their
separate, informed permission.

## DecentHead reuse and limits

The course entry vendors the adoption manifest from DecentHead
`00691c4fe93fd280f5aec780bdc4fac651bfcdb1`, including `WalletSession`,
`IPFSControls`, `AboutModal`, assets, LICENSE and NOTICE. It adapts
`switchChain` and `WalletConnect` for `chain: null`: connection is explicit and
observes the wallet's current chain rather than switching it. Generic upload,
restore and pin actions remain unavailable. Provider selection does not verify
connectivity or backup; UCAN authorization is not implemented. No learner data
is uploaded. Disconnect forgets this site's session but does not revoke wallet
permission.

The explicit **Verify provider connection (no upload)** action uses the shared
`IPFSSession.verifyConnection()` flow from the pinned DecentHead adoption.
Personal credentials stay in tab memory and are sent only to Pinata's fixed
HTTPS authentication endpoint; Kubo uses its loopback version endpoint without
credentials. Provider readiness is not backup, upload permission, retention or
reward verification. No UCAN flow or backend is introduced.

The self-contained receiving browser checks are
`node --test test/header-browser.cjs` and
`node test/provider-connect.browser.cjs` (Playwright required). They start and
stop local servers and test wallet rejection/connect/account and network
changes, disconnect, unavailable storage, About, and mocked provider success
and failure without external requests or uploads.

## License

Code: [Apache-2.0](LICENSE) · Art and docs: [CC BY 4.0](LICENSES/CC-BY-4.0.txt).
Keep the [NOTICE](NOTICE) with redistributed work.

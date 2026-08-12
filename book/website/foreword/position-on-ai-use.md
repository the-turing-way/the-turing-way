# Position on the Use of Generative AI in *The Turing Way* Contributions

*The Turing Way* is created by people, for people.
That is not merely an idea we attach to our work — it is the reason our collective work in *The Turing Way* exists.
Regardless of which technologies we use, we remain committed to community empowerment, transparency, and inclusion in every aspect of how we build this book together.

What makes *The Turing Way* valuable is not only the chapters we develop, but the process that leads to their production.
The active discussion during Collaboration Café and Book Dash on specific sets of research and data practices,
comments and recommendations on GitHub issue threads,
the mentoring a maintainer gives a first-time contributor,
the differences that gets talked through in a Pull Request review, 
the thoughtful process of working together as a community about how research and data practices should evolve.
That process **is** *The Turing Way* project.

AI/LLM tools can be useful assistants, but they cannot participate in a human-centered discussion,
cannot mentor a new contributor, and cannot hold accountability for a claim.
Likewise, LLM can produce a chapter that reads well but skipped the community process is not, in our view, a real purpose behind stewarding contribution to *The Turing Way*.
It is a shortcut around the part we care about most in Open Science, and want to protect within *The Turing Way*.

We recognise that contributors may use AI to help with parts of their work, 
and we ask that this be done thoughtfully, deliberately, and with a clear understanding of what should stay human.


**We understand that our position on AI/LLM use may not suit everyone's preferred way of working.**
If what you are looking for is a fast way to generate finished content with minimal back-and-forth, *The Turing Way* is probably not the right project for you right now.
We would like to invite you to engage with *The Turing Way* and help protect the space we have created over the years.
We are always delighted to work with people and institutions who want to continue improving research practices, including how best we can use AI to improve transparency, reproducibility and ethical approaches in data science.

## Here are some of the main considerations for the use of AI in *The Turing Way*

1. **AI must never be used on `good-first-issue` tasks**

Issues that are labelled as `good-first-issue` or Pull Requests (PRs) intended to help a new contributor learn our collaborative ways of working isn't a task to be solved by AI.
These issues and PRs exist specifically so people can enter the community, ask questions, get things wrong, get gentle feedback, and build confidence.
Handing that entry point to a model defeats its purpose, for the newcomer and for the maintainer who would otherwise get to mentor them.

More broadly, AI-generated text that arrives fully formed, with no visible thinking, no open questions, no trace of the contributor's own reasoning, closes down exactly the kind of discussion and debate we rely on to improve our practices over time.
We would rather receive a short, imperfect, human draft that invites conversation than a long, polished, AI-written one that discourages it.

We support the responsible use of AI where it lowers barriers to participation: accessibility support, translation, co-drafting alongside a contributor's own thinking, and help navigating unfamiliar tools.
Used this way, AI can bring more people into the conversation.

2. **Always respect the time and care that maintainers and reviewers bring to this project**

Be transparent when you use AI, so that reviewers can spend their limited time on discussion and mentoring rather than on detective work, and so no one burns out chasing down undisclosed AI use.

If you use AI in your interactions with GitHub, other community spaces, or in drafting a chapter, disclose it clearly in the issue, the pull request, the discussion thread, or the draft itself.
Please describe which tools were used and how. Provide prompts or workflows where possible.

```{admonition} Template for AI Use Disclaimer

[Generative AI and Model] was used in drafting this document.

The co-authors have reviewed the contribution and take responsibility for its quality, accuracy, and references.
```

Before opening a pull request, take responsibility for anything AI helped produce.
Read it, understand it, be able to defend it in discussion, and keep the change focused and reviewable (for example, by limiting it to specific files or sections).

When reviewing a contribution, judge it on accuracy, quality, relevance, scope, responsiveness, and care for the community in line with our contributing guideline, accessibility policy, and Code of Conduct rather than on whether AI was involved at all.

3. **Keep contributions concise — meaningful contribution takes real effort**

AI makes it easy to generate far more content than a topic actually needs, but volume isn't the goal here, but clarity and shared understanding are.
A short chapter that the community has actually discussed and agreed on serves readers better than a long one that simply wraps up a lot of AI-generated prose no one debated.

Because AI can produce polished text almost instantly, it is worth noting that a good contribution to *The Turing Way* has never been about output speed.
We ask contributors to (re)read our note on [low-effort contributions](https://book.the-turing-way.org/community-handbook/contributing/#ch-contributing-low-effort) as a reminder that thoughtful engagement, not simply a polished-looking draft, is what we want to cultivate a space for.

 4. **Understand the copyright and licensing risk in AI-generated content**

 AI-generated text can carry copyright and licensing uncertainty of its own, independent of how much reviewer time it costs to check.
 We want contributors and reviewers to treat this as a real risk to flag and resolve on its own terms.
 We do not want to have this responsibility land on maintainers or slow review process down.

**References and Reading Recommendations**

- Reference Policies from Other Open Source Communities
  - **rOpenSci** — [Software Review in the Era of AI](https://ropensci.org/blog/2026/02/26/ropensci-ai-policy/)
  - **pyOpenSci** — [Generative AI Peer Review Policy](https://www.pyopensci.org/blog/generative-ai-peer-review-policy.html)
  - **Wikipedia** — [Artificial Intelligence policy](https://en.wikipedia.org/wiki/Wikipedia:Artificial_intelligence), [Wikipedia — Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
  - **JOSS (Journal of Open Source Software)** — [AI use policy](https://joss.theoj.org/about) ([background](https://blog.joss.theoj.org/2026/01/preparing-joss-for-a-generative-ai-future))
  - **Fedora** — [AI-Assisted Contributions Policy](https://pagure.io/Fedora-Council/tickets/issue/542) ([announcement](https://communityblog.fedoraproject.org/council-policy-proposal-policy-on-ai-assisted-contributions/))
  - **Zulip** — [AI use policy and guidelines](https://github.com/zulip/zulip/blob/main/CONTRIBUTING.md#ai-use-policy-and-guidelines)
  - **LLVM** — [AI Tool Use Policy](https://llvm.org/docs/AIToolPolicy.html)
  - **Linux kernel** — [AI Coding Assistants](https://kernel.org/doc/html/next/process/coding-assistants.html)
  - **tldraw** — [Contributions policy discussion](https://github.com/tldraw/tldraw/issues/7695) ([CONTRIBUTING.md](https://github.com/tldraw/tldraw/blob/main/CONTRIBUTING.md))
  - **MyST-Parser** — no standalone policy yet; see the related [Jupyter AI-assisted code policy discussion](https://github.com/jupyter/governance/issues/326)
- Supporting document for authors: [SSI post](https://docs.google.com/document/d/1gInmbK-o00MRhihPzZBE0Hl4x8ZIgjdh7VJcV2haprU/edit?tab=t.0)
- Example `AGENTS.md` from the SSI Community: [ersilia-os/eos-analysis-template](https://github.com/ersilia-os/eos-analysis-template/blob/main/CLAUDE.md)

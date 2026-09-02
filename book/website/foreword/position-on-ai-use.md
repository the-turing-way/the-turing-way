# Position on the Use of Generative AI in *The Turing Way* Contributions

*The Turing Way* is created by people, for people.
That is not merely an idea we attach to our work, but a practice that guides how we work together.
Regardless of which technologies we use, we remain committed to our [guiding principles](#guiding-principles) of community empowerment, transparency, and inclusion in every aspect of how we maintain our community and build the book together.

What makes *The Turing Way* valuable is the process through which our community co-produces guidance for research organisations and the spaces we inhabit.
Our work is the cumulative result of many interactions, including:

- active discussions during Collaboration Cafés and Book Dash events;
- collaboration in Working Groups and informal initiatives;
- comments and recommendations in GitHub issues and discussions;
- mentoring between maintainers, reviewers, and contributors;
- differences worked through during pull request reviews; and
- conversations about how research and data practices should evolve.

That process **is** *The Turing Way* project.

AI and large language model (LLM) tools can be useful assistants, but they cannot participate in a human-centred discussion, mentor a new contributor, or be held accountable for a claim.
An LLM may produce a chapter that reads well, but if that chapter bypasses the community process, it also bypasses the part of Open Science that we most want to protect within *The Turing Way*.

We recognise that contributors may use AI to help with parts of their work, and we ask that they do so thoughtfully, deliberately, and with a clear understanding of what should stay human.

```{admonition} Disclaimer
**We understand that our position on AI/LLM use may not suit everyone's preferred way of working.**
If what you are looking for is a fast way to generate finished content with minimal back-and-forth, *The Turing Way* is probably not the right project for you right now.
We would like to invite you to engage with *The Turing Way* and help protect the space we have created over the years.
We are always delighted to work with people and institutions who want to continue improving research practices, including how best we can use AI to improve transparency, reproducibility and ethical approaches in data science.
```

## Main considerations for using AI in *The Turing Way*

### 1. AI must never be used for addressing `good-first-issue` tasks

Issues labelled `good-first-issue`, and pull requests intended to help a new (human) contributor learn our collaborative ways of working, are not tasks identified for an AI tool or agent to solve.
They exist specifically so people can enter the community, ask questions, make mistakes, receive supportive feedback, and build confidence.
Handing that entry point to a model defeats its purpose for both the newcomer and the maintainer who would otherwise mentor them.

### 2. Always respect the time and care that maintainers and reviewers bring to this project

Before opening a pull request, take responsibility for anything AI helped produce.
Read it, understand it, be able to defend it in discussion, and keep the change focused and reviewable, for example by limiting it to specific files or sections.

When reviewing a contribution, judge it on accuracy, quality, relevance, scope, responsiveness, and care for the community, in line with our contributing guidelines, accessibility policy, and Code of Conduct, rather than on whether AI was involved at all.

If AI tools made a substantive contribution to a pull request, use the AI-use section of the pull request template to describe which tools were used and how.
This single disclosure is enough; contributors do not need to repeat it in every comment.
Being transparent allows reviewers to spend their limited time on discussion and mentoring rather than detective work.

```{admonition} AI tools can support participation
We recognise that AI tools can improve accessibility and lower barriers to participation.
Examples include accessibility support, translation, co-drafting alongside a contributor's own thinking (in the language they prefer), and help navigating unfamiliar tools.
Used this way, AI can bring more people into the conversation.
Therefore, we recognize and support that community members will take responsibility for the tools they use to support their contributions, while respecting community participation and contributing guidelines.
```

### 3. Keep contributions concise

AI makes it easy to generate far more content than a topic needs, but our goals are clarity and shared understanding, not volume.
A short chapter that the community has actually discussed and agreed on serves readers better than a long one that simply wraps up a lot of AI-generated prose no one debated.

Because AI can produce polished text almost instantly, it is worth noting that a good contribution to *The Turing Way* has never been about output speed.
We ask contributors to (re)read our note on [low-effort contributions](#ch-contributing-low-effort) as a reminder that thoughtful engagement, not simply a polished-looking draft, is what we want to cultivate a space for.

### 4. Understand the copyright and licensing risk in AI-generated content

AI-generated text carries copyright and licensing uncertainty of its own, independent of how much reviewer time it costs to check.
We want contributors and reviewers to treat this as a real risk to flag and resolve on its own terms, ensuring that original creators are appropriately credited when content is reused.
Contributors are responsible for resolving these concerns rather than leaving them for maintainers or allowing them to slow down the review process.
Further reading section has listed a few resources on copyright in the context of generative AI.
## References and Reading Recommendations

### Policies from other open source communities

| Community | Policy or discussion |
| --- | --- |
| Codeberg | [Protecting our FLOSS commons from AI companies](https://blog.codeberg.org/protecting-our-floss-commons-from-llms.html) |
| Fedora | [AI-Assisted Contributions Policy](https://pagure.io/Fedora-Council/tickets/issue/542) and [announcement](https://communityblog.fedoraproject.org/council-policy-proposal-policy-on-ai-assisted-contributions/) |
| JOSS (Journal of Open Source Software) | [AI use policy](https://joss.theoj.org/about) and [background](https://blog.joss.theoj.org/2026/01/preparing-joss-for-a-generative-ai-future) |
| Jupyter | [AI-assisted code policy discussion](https://github.com/jupyter/governance/issues/326) |
| Linux kernel | [AI Coding Assistants](https://kernel.org/doc/html/next/process/coding-assistants.html) |
| LLVM | [AI Tool Use Policy](https://llvm.org/docs/AIToolPolicy.html) |
| pyOpenSci | [Generative AI Peer Review Policy](https://www.pyopensci.org/blog/generative-ai-peer-review-policy.html) |
| rOpenSci | [Software Review in the Era of AI](https://ropensci.org/blog/2026/02/26/ropensci-ai-policy/) |
| tldraw | [Contributions policy discussion](https://github.com/tldraw/tldraw/issues/7695) and [CONTRIBUTING.md](https://github.com/tldraw/tldraw/blob/main/CONTRIBUTING.md) |
| Wikipedia | [Artificial Intelligence policy](https://en.wikipedia.org/wiki/Wikipedia:Artificial_intelligence) and [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) |
| Zulip | [AI use policy and guidelines](https://github.com/zulip/zulip/blob/main/CONTRIBUTING.md#ai-use-policy-and-guidelines) |

### Further reading

- Cutting through the bull: AI slop and MIL by Alex Bodine, October 2025: [Deutsche Welle Akademie](https://akademie.dw.com/en/ai-slop-and-media-literacy/a-74471386)
- I’m begging you: Never write with AI by Bret Stephens, August 2026: [Opinion piece originally published in New York Times](https://www.sltrib.com/opinion/commentary/2026/08/09/opinion-im-begging-you-never-write/)
- Generative AI training and copyright law (preprint): [Stober, S., & Dornis, T. W. (2025).  arXiv preprint arXiv:2502.15858](https://arxiv.org/abs/2502.15858)
- Supporting document for authors from Institute for Software Research (previously Software Sustainability Institute), 2026: [Blog post from Collaboration Workshop 2026](https://docs.google.com/document/d/1gInmbK-o00MRhihPzZBE0Hl4x8ZIgjdh7VJcV2haprU/edit?tab=t.0)
- Example instructions for AI agents from Ersilia: [ersilia-os/eos-analysis-template](https://github.com/ersilia-os/eos-analysis-template/blob/main/CLAUDE.md)

# Collaboration Cafe Notes - 27 January

# Check-in

Name + Pronouns + What is something you want to do more of in 2024? What is something you want to do less of in 2024? + an emoji (if you'd like!: https://emojipedia.org/, see also: https://openmoji.org/)
(Remember that this is a public document. You can use a pseudonym if you'd prefer.) Use the 🤫 emoji if you would not like to be included in our public archive. These notes will be archived on The Turing Way repository.

- Anne + she/they + More regular habit and ritual-building, and less passive github notification management! 🌱  
- Sophia + she/her + Getting outside for adventures. 
- Richard + + contributing to FAIRsharing 
- Sarah G + she/her + I want to do more things with confidence
- Malvika + she/her + More of research and writing, less of wasting time in reactively engineering what can be addressed by pre-planning.
- David + he/him + more cachondeo with friends (+1) and woodworking / work ⛰️
- Gabin + He/Him + resume regular running+swimming
- Emma - I'm trying to do more 'me' time as this is hard as a mum. This involves booking things for me or things with friends like this month I'm going for a pedicure and a day out with one of my friends in London. Less of - well I would say cleaning as I really hate it but my house is a real mess so needs sorting out and a good deep clean. (+1000)  
- Ale + overthinking in the future
- Bastian + he/him + more deep thinking, less busywork 🤔
- Liz, agree with +yoga, also +back to knitting
- Danny + they/them or he/him, 
- Arielle + she/her + more writing, I'm also taking an improv class to indulge my creative side + I'm monitoring my screen time to spend less time on my phone this year
- Jim + he/him + Social events + Worrying + 🧶
- Kirstie + she/her + Arranging social connections - I’ve been waiting to be invited and it turns out that doesn’t work 😅 + focusing on who doesn’t like me + 💕

## Advertise and promote your event or anything exciting you're working on. ✨ 

- Thinking about proposing a markdown flavour for protocols - inspired by the format of protocols.io - maybe some kind of extension to MyST (Richard J. Acton)

## Breakout rooms: Topic proposals and notes✨ 

While no sign-ups are required to attend Collaboration Cafe, if you have an idea for a topic you'd like to discuss in a breakout room, please add it below and put your name next to it. 

If you like one of the topics that are already suggested, please add your name next to that one. For more information about breakout rooms see [the description on GitHub](https://github.com/alan-turing-institute/the-turing-way/blob/main/project_management/online-collaboration-cafe.md#breakout-rooms).*

- Main Room:
    - Hour 1: Infrastructure Working Group: Splitting the TTW repository / 2nd hour in a breakout room
    - Hour 2: Accessibility Working Group
- Predicting the future of Research Room - Infrastructure Roles Room
    - Arielle: for the second hour I'd like a room for the "What will research look like in 50 years?" co-writing 
    - yeess
    - sounds fun
- Infrastructure Working Group
    - Discovered that Zoom whiteboard does not work with non-Turing people
    - Brainstorm: https://miro.com/app/board/uXjVN41KSE0=/?share_link_id=972561986637
    - "Discoverability of the repository" -> use-journey of new people coming in vs pragmatic approach of 'which repositories need to be separated right now'
    - Which repos also exist elsewhere? (i.e. TTW Translation)
    - Sign-posting in the Organisational README, sign-posting to working groups
    - Without these sign-posts, does this create more silos with the working groups?
    - Working groups have their own repositories -> sub-community and empowermenent
    - We can try for more standardising -> but then working groups 
        - Can WGs govern themselves reasonably autonomusly - via how they structure their working groups?
    - Trying to reduce the size of the repo: i.e. uploading PDFs, 
    - Encouraging shallow clones: https://github.blog/2020-12-21-get-up-to-speed-with-partial-clone-and-shallow-clone/
    - KW: we could archive this book and start a new repository.
    - I don’t think the size is a barrier (yet) / ~200 MB? I think a Python venv is larger than that and I have dozens of those.
    - We all agree that we need to split the repositories
    - Need to map where information is coming from and where 
    - Findability/searchability - i.e. intentionally archiving notes from community calls, helping them to navigate, perhaps some visual resources to help them navigate? What's happening when a
    - Do we have any best practices for working across multiple repositories? --> What other communities have we seen do this well?
    - JupyterBook has a fairly segmented ecosystem
    - ALS: Sign-posting for the Community Handbook? Contributors guide? Adding more materials about how to navigate through the guides?
    - We can definitely ping Angus in the Turing Way and ask his experience of issues and the Jupyter Book ecosystem as he’s onboarded himself 
    - We might want to look at our issue template to budget cross-connection
    - What does an MVP look like?
    - Separating the TTW book from the rest of the repo?
    - Or separating project management folder
    - What's the difference between Project management, community management and governance? Should those be components
    - Current folders:
        - book
        - communications --- least controversial? newsletter folder specifically?
        - project management
        - governance
        - open-life-science-mentoring
        - tests
        - workshops
    - What does the 'communications' include for TTW?
    - MVP sounds like a good idea
        - https://infrastructure.2i2c.org/howto/update-env/#split-up-an-image-for-use-with-the-repo2docker-action
    - There could be a step missing, where it creates a branch called "staging" 
    - Danny will try it out and ping Sarah if helps is needed
    - Making a newsletter repo as a test
    - Misunderstanding about the goal of the main room discussion but still interesting. Accessability and discoverability was a surprise factor at the discussion 
    - Is there a particular approach for a Translation repo. Sarah will share the repo she had been working on during the Book Dash with Batool 
    - Decision making from moving from readthedocs to netlify. No decision has been received, dedicated URL for the webpage (priority!) Paying for a domain name (ACTION TO ALE) -- 
    - Why a new domain is needed? The domain name is giving by netlify if we swap to readthedocs and the URL will find a broken webpage. IF we buy one, we will redirect trafic from one to another url, which means . Why can't we redirect from netlify to readthedocs?ttw-collaboration-cafe | Framapad annuel
    - If in the future there's another platform to deploy, the change will be easier and our URL name will be consistent
    - theturingway.org / theturingway.io  --- > Is this a nice to have? We would feel more confortable to do the change if we have our own URL. We don't need to rely on netlify or readthedocs 
    - In another project, someone just bought a domain with their credit card because it wasn’t worth the hassle of going through a university/institution.
    - If we didn't slipt the repo what are the barriers? People knowing that the Translation holds a different repo
- Accessibility Working Group 
    - LH: When reading the chapter, she was thinking about how TTW comunity could have a broader perspective of what it meant to run inclusive events. It is an important shift that we’re being inclusive of and involving patients and the public in research. 
    - The Accessibility Working Group takes a broad definition of accessibility to include people with disabilities,  people who have low internet bandwidth etc
    - the chapter currently has a broad definition of accessibility but does phrase things as "they're all patients"
    - As a TTW community, we have an opportunity to frame accessibility beyond being just patients. 
    - BGT: There was a struggle when planning the chapter with where to draw the line of what is being included in the definitions and scope. There's so much that can be written about these topics, so what scope does this chapter address?
    - LH: A lot of the resources in the chapter are specifically applicable to people with disabilities. The language around those sections could be more direct. It is important to speak matter-of-factly about the groups and communities that we are addressing. "Lived experience" shouldn't be used as a phrase when  we mean "disabilities".
    - EK: Since we don't want to write much more, is it a case of identifying sections where we can highlight PPIE, and then separately highlight disabled communities depending on what is relevant?
    - LH: It's mostly framing.
    - BGT: There are two different communities that we are merging into one. PPIE community, and the wider research community that needs to address disability. 
    - At the AIM RSF conference we did address many disability needs, but did not address the needs of people who aren't researchers and who are taking part in research for the first time. The feedback recieved was that we didn't do a good job of making them included. 
    - LH: Thinking back to her experience as a researcher, the guides for how to be inclusive are relevant to everyone. 
    - BGT: There should be a narrowing of the chapter scope to be just about running effective PPIE events.
    - LH: would like to contribute to the reccomendations for the conference inclusion aspect. 
    - Summarising (SB & BGT): Acknowledging both flip-sides, where in a collective chapter about making events accessible more broadly, specificities about disability can be lost, and on the flip side, and the same applies for specific PPIE-content
    - BGT: Next steps: Doing the overall read-through of the sections first. 
    - KW: From a working memory point of view, reading through all of it may be too much to do to review. If everyone comes back with different suggestions, I was thinking if there are 'section headings' or 'subheadings' that can be ordered in a different way. 
    - BGT: At the highest levels, what can be shifted? Come up with an order and separation? 
    - SB: Deep read and structural read of the accessibility working group has already done. But there are few spaces where moving headings around will solve the original problem. 
    - KW: Is the homework then actually that KW & BGT should read more broadly about the chapter? What are we not doing?
    - LH: Accessibility guide applies much more broadly outside of the context of disability, it applies in many other contexts as well. There's specificity in how things have been developed. 
    - KW: Two questions: is there a goal to have a separate accessibility guide? Do we keep it integrated in other guides?
    - SB: Guide for collaboration?
    - KW: I feel ethics being separated as a separate guide, I'm not sure about it. I don't know how to feel about Accessibility being a separate guide.
    - LH: I agree that it touches everything. I'm not sure how to divide it up without a guide. I'm not sure to set up a separate guide.
    - ALS: A bit about the contextual history of the guide, it was created in reaction to resources that GCHQ wanted to add to the guides.
        - Citing history: https://github.com/alan-turing-institute/the-turing-way/issues/2730
    - KW: How to we divide it then into the different guides? What about PPIE also applying in the Guide for ethics? Could this be moved to ethics or duplicated with a link?
    - SB: Currently, there's a collated draft that is being read & commented on? 
    - BGT: Come up with subdivision of the content to present to KW. 
    - KW: Deadline for delivery of the content, we don't want to stop. It's about demonstrating that we have this expertise, we are doing our best to run inclusive events & help other people to run inclusive events. It's useful for our funders, but there's not hard deadline. 
    - LH: Would it be helpful if I made a list of the headings and subheadings that can go in the accessibility guide?
    - KW: Subheadings and nestied headings. If there's a "double-dip"
- Newsletter-writing room (David)
- Predicting the future of Research Room 
- Quiet co-working
- End of the call notes
    - RA: Last point!
    - AB: What happens if we actually fixed things? What would happen in peer review? Imaginging the future of research?
    - ALS: Splitting the repo?
    - SG: Batool joined having a discussion around translation, URL for the repository. Danny is going to do a dry-run and figure out documentation. If we're okay ifn a few names, 
    - KW: I can buy the domain name!
    - AAA: Raising in the domain name & other points in the slack channel!
    - SG: We want a url to prevent link rot, and for switching away from other platforms.
    - DG: Want to be reminded about arguments against having a URL. Don't like change.

## Link list✨ 

- https://carpentries.github.io/instructor-training/02-practice-learning.html#building-a-mental-model
- Jonny decimal system: https://johnnydecimal.com
- Draw.io: https://app.diagrams.net

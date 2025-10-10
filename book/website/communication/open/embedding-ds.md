(cm-open-educators)=
# Embedding Data Science & AI across Disciplines: Context and Suggestions for Educators

## Overview

Data science (DS) is no longer limited to mathematicians, statisticians, and computer scientists. As its value becomes apparent in non-traditional disciplines, students in these areas
naturally seek to upskill in DS. With technology increasingly shaping our future, it is essential to offer opportunities to develop these skills across a broader range of fields, ensuring the
necessary expertise and competencies are cultivated beyond their traditional domains. This chapter profiles non-cognate students, offers suggestions for educators teaching Data Science in non
cognate disciplines, and highlights a series of good practices and pedagogical approaches for engaging with non-cognate students.

## Introduction

```{note}
The term “non-cognate student” in this chapter refers to a student who is pursuing a degree or studying in a field that is unrelated or different from their previous academic background or
qualifications. In this context, “cognate” refers to a subject or field that is closely related or similar to the student’s prior academic experience. For example, if a student with a
background in engineering decides to pursue a graduate degree in psychology, they would be considered a non-cognate student because engineering and psychology are unrelated fields. The term is
commonly used in academic settings, particularly when discussing admissions or program requirements. However, for more inclusive and accessible language, you may prefer to describe someone
simply as “a student without a background in data science or AI”.
```

Data science is a truly interdisciplinary field that can be described as the integration of computational and digital technologies, statistical and mathematical knowledge, and disciplinary
expertise @Jiang2022datascience. 
It also represents a rapidly growing methodological approach for educational practice @Estrellado2020data and research @McFarland2021education.

```{figure} ../../../figures/data-science.*
---
height: 500px
label: data-science
alt: >
  Venn diagram with three partially overlapping circles representing components of data science.
  The left circle (light yellow) is labeled Computer Science, the right circle (light green) is Mathematics & Statistics and the bottom circle light purple is Domain Knowledge.
  The overlap between Computer Science and Mathematics & Statistics is labeled Machine Learning.
  The overlap between Mathematics & Statistics and Domain Knowledge is Research.
  The overlap between Domain Knowledge and Computer Science is Software Development.
  The central area where all three circles intersect is labeled Data Science.
---
The interdisciplinary nature of Data Science. Illustration by Denise Bianco (2025). Used under a CC-BY 4.0 licence.
```

In the constantly growing data-intensive society, data science is being applied within various **non-cognate disciplines** such as arts, history, and social sciences. It’s important for people
involved in training people in these disciplines to understand how to adapt tools and develop skills in different contexts, particularly data literacy, and how educators can support the
development of these specific competencies. Data literacy is traditionally defined as the ability to explore, understand, and communicate data as information. This definition can be expanded by
a recent contribution from @Gebre2022conceptions who identifies key elements of data literacy, including general competencies such as attitudes toward data and specific skills like using particular tools. Gebre also highlights context-specific factors that impact how learners relate to data, which are highly relevant when teaching to non-cognate students.

## What does the typical learner profile from a non-cognate discipline look like?

Non-cognate does not necessarily mean non-computing/non-mathematics/non-STEM and, most importantly, it does not limit the student’s ultimate potential to acquire new knowledge. However, being a
non-cognate student may have implications for the student’s course selection, prerequisites, and potential challenges in adapting to the new field of study. In some cases, non-cognate students
may need to complete additional coursework or prerequisites to gain the necessary knowledge and skills to succeed in their chosen field.

While it’s challenging to define a single profile due to varying circumstances, some general traits can be identified:

* Career changers
* Driven by personal interest
* In need of expanding their skill sets
* Have existing professional and work experience

Non-cognate students present both challenges and opportunities for educators. Teaching Data Science in a programme that is not discipline-specific requires tailored preparation and adaptation
of content and language according to the audience.

* **Motivation Challenges**: Their motivation for joining the course often differs from that of students in core Data Science programmes. They may have very specific questions, viewpoints, and perspectives.
* **Background and Skills Challenges**: Varying backgrounds and skill levels among students require further assessment and integration processes.
* **Learning Needs Challenges**: Often, non-cognate students come with questions related to their previous experiences, which are quite specific. Always consider their existing knowledge and clarify their needs. Avoid delving too deeply right away; superficial knowledge may be sufficient in some situations.
* **Language Challenges**: Different disciplines speak different languages. This means starting by reviewing glossaries and terms to ensure everyone is on the same page, introducing vocabulary gradually in a way that is not overwhelming, avoiding discipline-specific jargon unless necessary, and sharing additional resources to support their learning.
* **Structural Challenges**: Lack of existing frameworks and supporting structures for cross-disciplinary learning leaves educators more independent in their approach.

But also…

* **Connection Opportunities**: Linking elements such as domain knowledge, methods, people, and backgrounds that would otherwise remain unconnected can bring new, valuable insights.
* **Multi-approach Opportunities**: Applying various disciplinary perspectives to specific case studies can enrich the outcomes.
* **Problem/solving Opportunities**: Using multiple approaches to knowledge in problem-solving discussions can yield more innovative solutions.
* **Knowledge-sharing Opportunities**: Cross-disciplinary learning equips students with skills and modes of thinking informed by multiple worldviews.
* **Flexibility**: The lack of strict frameworks can be an opportunity to explore different collaborative models and integrate existing frameworks in new and productive ways.

## Understanding the fundamental concepts of AI and Data Science

When teaching non-cognate students, it is crucial to first assess their understanding of AI and data science fundamentals. The multi-stage framework proposed by @Kandlhofer2016artificial for AI
literacy can serve as a valuable reference for evaluating students’ knowledge.

Depending on existing knowledge, teaching may need to focus on:

* Building initial awareness
* Experimenting with and familiarising students with the theory behind certain AI topics
* Encouraging independent problem-solving
* Fostering an understanding of core AI topics and introducing advanced AI concepts
* Enabling students to independently acquire and apply knowledge
* Helping students become AI fluent
* Applying problem-solving methods at a higher level of abstraction
* Developing a fundamental understanding of AI topics

```{figure} ../../../figures/kandlhofer-2016.*
---
height: 500px
label: kandlhofer-2016
alt: >
 A flowchart visualising the structure of foundational AI and computer science topics, using color-coded boxes connected by arrows to show progression and relationships.
 Top row (left to right): Light blue box labeled Automata with bullets:
 Illustrating decision making process.
 Connected by a right-pointing arrow to a medium blue box labeled Intelligent agents with bullets:
 Demonstrate the modelling process of making and executing decisions.
 Connected by another right-pointing arrow to a dark blue box labeled Graphs, data structures, basics of computer science with bullets:
 Stack, queue, tree.
 Control statements, paradigm.
 Middle row (left to right), connected below the top row with downward arrows:
 Purple box labeled "Sorting" with bullets:
 Fundamental concept in AI/computer science
 Sorting algorithms
 Connected by a right-pointing arrow to a violet box labeled Problem Solving by search with bullets:
 Essential concept in AI with numerous areas of application
 Connected by another right-pointing arrow to a magenta box labeled "Classic Planning" with bullets:
 Modelling problems, making decisions, establishing and evaluating plans
 Logic
 Bottom row:
 A dark pink box labeled "Machine learning" connected by a downward arrow from "Problem Solving by search", with bullets:
 Different approaches to learning agents
 Decision trees and neural networks
---
Adaptation of Kandlhofer et al. (2016) *Topics of AI Literacy*. Illustration by Gule Saman (2024). Used under a CC-BY 4.0 licence.
```

```{dropdown} Case Study: UCL, Built Environment: Sustainable Heritage MSc, Data Science route
:class: tip
This Master’s degree creates expert data scientists taught through the exciting multidisciplinary lens of cultural heritage (historic buildings, sites, landscapes, museums and collections).
Students will develop advanced data science skills, such as coding, crowd-sourced data science, machine learning and data visualisation, and apply them to the complexities of acquisition,
analysis and exploitation of the variety of data that is generated and used in heritage contexts. The course is open to applicants with a technical background such as statistics or data
science, as well as applicants from other disciplines (for example: conservation, curation, history) that want to develop data science skills. This degree route is suited both to recent
graduates and early or mid-career professionals looking to retrain or up-skill.
```

## Suggestions for Educators

DS educators teaching students without a data science or AI background would need to pay particular attention to the students’ background knowledge, concepts, and practical and metacognitive
skills. Assessment for learning, differentiated instruction, collaborative learning, and other effective teaching methods, can be tailored to the unique needs of data science and AI education
across disciplines.

It is important not to make assumptions about students’ prior knowledge and skills. The suggestions below can apply to broad data science and AI education, but educators teaching students
without a data science and AI background may find them particularly useful for tailoring teaching and learning to students’ needs and skill sets. These different pedagogical approaches are
designed to help you gain insights into your students’ understanding of specific concepts or topics, allowing you to better support their individual progress.

### Assessment for Learning

Assessment for Learning is used during learning, and it is useful to identify student demographics, student needs and starting points, and to generate feedback they can use to improve
   performance. Assessment for Learning can take different forms: it could be as simple as observing class discussions, asking questions in oral or written form, or using collaborative tools
   such as Miro or Notion to leverage visual aids and conceptual mapping.

Assessment for learning informs changes you can make to your lesson straight away to make it more effective. Through assessment for learning, students will:

* **Introduce themselves**: understanding WHO. General information will help you understand the overall cohort’s demographics and map out discipline-specific interests.
* **Explain what they can do**: understanding HOW. Assess existing skills and expertise (this is also helpful for students to understand their capabilities).
* **Express preferences about what they want to do**: understanding *WHAT*. Let students describe their ideal scenarios; this will help you refine and tailor your content.
* **Share their goals and aspirations**: understanding WHY. What do they need this for?

In *Seven Myths of Education* @Christodoulou2014myths suggests that teachers should act as “thermostats, not thermometers” meaning they should not only measure where a student is but also
make necessary adjustments to guide them to where they need to be. This perspective is fundamental when thinking about assessment for learning, and to understand the critical role of effective
feedback.

#### Effective feedback in assessment for learning

Effective feedback requires active listening from both the educator and the student. As part of the questioning process, it is an essential
tool for developing students’ thinking. Feedback must be task-focused, timely, specific, clear and unbiased. In this way, you will provide your students with information about their current
performance and guidance on how they can improve to reach their goals.

### Formative Assessment

Formative Assessment supports teaching by assessing a learner’s state and inferring next steps @Zhai2020meta. It is similar to AfL, as both methods are used to
   understand student progress and inform teaching. However, while AfL is carried out during learning to inform teaching and identify areas for improvement, formative assessment is used for
   day-to-day assessments to gauge and explore students’ understanding of a topic

The formative assessment process usually consists of the following three practices @Stanja2022formative :
* **Eliciting**: The collection of evidence for students’ learning using tasks and questions
* **Interpreting**: Analysing what students are saying, writing or doing and what this indicates about their thinking; and identifying implications for learning based on the previous analysis
* **Responding**: Giving feedback to students or adaptation of instruction.

Formative assessments in data science and AI education should focus on providing timely and actionable feedback that helps students improve their understanding and skills progressively.
Examples include:

* **Code reviews**: Regularly assessing students’ code for functionality, efficiency, and style.
* **Concept checks**: Quick, informal assessments during lessons, such as quizzes or hands-on tasks, to gauge understanding of recent topics like machine learning algorithms or statistical
  methods.
* **Data challenges**: Mini group competitions where students predict outcomes based on given datasets, which are then discussed in class to learn from various approaches. When teaching in
  multidisciplinary settings, the challenges should be situated in the disciplinary domain that is most familiar to students.

### Differentiated Instruction*

Differentiated Instruction is a method that considers students’ individual learning styles and levels of readiness before designing a lesson plan @tomlinson2017differentiate.
   Differentiated instruction sits between “single-size” instruction and individualised instruction, involving proactive planning of various ways for students to express their learning.
   While it may require fine-tuning for individual learners, offering multiple options increases the likelihood of effectively meeting the needs of many students. In this model, the teacher is
   viewed as an organiser of knowledge rather than a gatekeeper.

Differentiated instruction in the context of data science and AI can by applied through:

* **Tiered assignments**: Provide different levels of difficulty in project tasks or problem sets, allowing students to engage at a level that matches their proficiency.
* **Learning pathways**: Create alternative learning modules that cater to different interests applications of data science and AI, letting students choose based on their existing knowledge,
career goals or academic interests.
* **Visual aids and simulations**: Use visual representations of algorithms and data flows, which can help visual learners better understand complex concepts.
* **Collaborative Learning**: Leveraging collaborative learning strategies can enhance understanding of data science and AI and innovation across disciplines. Techniques include:
* **Group work and Study groups**: Encourage formation of study groups that meet regularly to discuss course content and collaborate on group projects.
* **Paired programming**: Working collaboratively in pairs at a single computer helps students to plough through certain types of coding problems, supporting peer learning and knowledge sharing.
* **Peer teaching**: Similarly, assign students to teach certain concepts or technologies to their peers, reinforcing their own understanding and aiding others.
* **Flipped classrooms**: Providing students with information before class means that students can learn at their own pace, take responsibility for their learning and actively engage in class. This will also improve collaboration between students and between students and educators, who can get to know them better and provide better support.

## Summary

In conclusion, teaching students without a data science or AI background can be challenging for educators, but it also provides many opportunities, especially in terms of creativity, knowledge
sharing, and problem-solving. We recommend conducting an initial assessment of students’ understanding of AI and data science fundamentals (data literacy) to determine where the focus should
be. It is important not to take students’ existing knowledge and specific expertise for granted. Teaching approaches such as assessment for learning can be useful for this purpose, while
formative assessment and differentiated instruction, combined with a blend of methods to cater to different learning styles, can support the design of teaching content and the adjustment of
material according to students’ needs. Collaborative learning is also an effective way to engage students, leverage their existing knowledge, and foster a supportive environment for rich
exchanges and co-development.

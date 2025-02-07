(rr-code-reuse-templates)=
# What is a Software Template?

A software template is like the blueprint for a project—it gives you a pre-made setup that includes folders, basic code, and instructions. Templates are especially useful in research, where reproducibility and organization are key.

## Why Use Software Templates?

Software templates are shortcuts for starting and managing projects. For researchers who work with software, templates make your code easier to understand, share, and reproduce. In this chapter, we’ll dive into how templates work, why they’re useful, and how they can save you time and effort.

> **Personal Note:** *I used to spend hours setting up projects until I discovered the [**NLeSC Python Template**](https://github.com/NLeSC/python-template). It was a game-changer! Suddenly, I could focus on the actual research instead of figuring out where to put files.*

## Why Are Software Templates Useful?

### 1. **They Keep Projects Organized**
Imagine opening an old project and feeling completely lost. Where did you save the scripts? Which folder had the data? Templates fix this by giving every project a predictable structure. For example, you might always have folders named `src` for code, `tests` for testing, and `docs` for documentation. It’s like giving your future self a map.

### 2. **They Teach Good Practices**
Templates are often built by experts and include best practices by default—like clean code, proper documentation, and even FAIR principles (Findable, Accessible, Interoperable, Reusable). Following these practices makes your work more polished and easier for others to use.

> *"In one of the energy research projects at the Netherlands eScience Center, we neededed to share our analysis pipeline with collaborators across different institutions. By using the [**Julia Besties**](https://github.com/JuliaBesties) template, we ensured that all metadata, dependencies, and documentation were in place. This not only streamlined the collaboration but also allowed our team to publish the pipeline in a repository where others could reuse it effortlessly. It was rewarding to see our work cited and adapted by another research group within months of publication."*

Templates designed for research software can also include, CITATION.cff files, and integration with archiving platforms like Zenodo, and other best practices specific to research software.

### 3. **They Make It Easy to Join a Project**

When new team members join your project, they can quickly get up to speed if the structure is clear and consistent. Templates make onboarding a breeze by eliminating the guesswork about how things are set up.

### 4. **They Make Research Reproducible**

Reproducibility is essential in research. Templates help by including files like `README` (with setup instructions), tests, configuration files, a dependency management solution. For research software, they can also include information or data to reproduce research results.

### 5. **They Save Time**
Setting up a new project can feel like a chore—creating folders, writing setup scripts, or installing tools. Templates handle all this for you so you can jump straight into the real work.

> *"I recently started a new analysis project using a Python template, and what used to take an afternoon was done in 10 minutes."*

Many templates come pre-configured with tools for testing, deployment, or online publishing. For example, GitHub Actions workflows can be included right out of the box, saving you even more setup time.


## Examples of Great Software Templates for research software

1. [**NLeSC Python Template**](https://github.com/NLeSC/python-template)  
    A robust template for Python projects, including research software best practices and has multiple profiles for different use cases.

1. [**Scientific Python Cookie**](https://github.com/scientific-python/cookie)
    A template for scientific Python packages, optimized for projects that require rigorous testing and extensive documentation.

1. [**Julia Besties**](https://github.com/JuliaBesties)
    A collection of templates and tools for developing high-quality Julia projects.

1. [**FAIR Python Cookiecutter**](https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter)  
    A Cookiecutter template for Python projects designed with FAIR principles in mind, emphasizing reproducibility and metadata inclusion.

1. [**Copier Template for C Projects**](https://github.com/jspaaks/copier-template-for-c-projects)
    A Copier-based template for C programming projects, featuring pre-configured testing and build systems.  


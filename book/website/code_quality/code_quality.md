# Code Quality

| Prerequisite                                                                                  | Importance |
| --------------------------------------------------------------------------------------------- | ---------- |
| [Experience with the command line](https://programminghistorian.org/en/lessons/intro-to-bash) | Helpful    |

## Table of contents

- [Code Quality](#code-quality)
  - [Table of contents](#table-of-contents)
  - [Summary](#summary)
  - [Static code analysis](#static-code-analysis)
    - [Advantages of Static code analysis](#advantages-of-static-code-analysis)
  - [Code style](#code-style)
    - [Automatic formatting](#automatic-formatting)
  - [Online services providing software quality checks](#online-services-providing-software-quality-checks)

## Summary

There are several ways to improve software quality that require relatively little effort.
By following a coding style, code will be easier for yourself and others to understand and therefore it will contain fewer bugs.
Tools for static code analysis can report bugs as well as style issues without even running the code.

## Static code analysis


Static code analysis is a method that examines code and detects software vulnerabilities before your code is executed or the project is built and deployed. 
This analysis is capable of identifying quality issues, including security weaknesses and errors. 
In addition to finding bugs, many of these tools can also help maintain a consistent coding style.

### Advantages of Static code analysis

- Write high-quality code: Early detection of possible programming errors help developers to know where they went wrong.

- Achieve regulatory compliance: Achieving software compliance is crucial for the stability and security of products. With this, developers can comprehensively test their code in a non-runtime environment, ensuring all code standards are met and enterprise security is achieved. 

- Accelerate software development life-cycles: Static code analysis ensures high-quality code reaches testers in lesser time. This means, even testers take much time to test the product, thus accelerating software development life-cycles. 

Some of the most widely used `linters` are mentioned in the below table:

| Language                  | Static code analysis tool|
|---------------------------|------------------------|
| C/C++                     | [Cppcheck](http://cppcheck.sourceforge.net/), [cpplint](https://github.com/cpplintcpplint)|
| Python                    | [Pylint](https://pypi.org/project/pylint/), [lintr](https://github.com/jimhester/lintr)|
| Javascript                | [ESLint](https://eslint.org/), [JSlint](https://jslint.com/), [JSHint](https://jshint.com/)|
| Java                      | [Checkstyle](https://checkstyle.sourceforge.io/), [FindBugs](http://findbugs.sourceforge.net), [PMD](https://pmd.github.io/)|
| Perl                      | [PerlTidy](https://metacpan.org/pod/perltidy)|
| R                         | [prospector](https://prospector.readthedocs.io)|
| Shell/Bash                | [shellcheck](https://www.shellcheck.net)|

## Code style

A coding style is a set of conventions on how to format code.
For instance, what do you call your variables? Do you use spaces or tabs for indentation? Where do you put comments?
Consistently using the same style throughout your code, makes it easier to read.
Code that is easy to read, is easier to understand for yourself as well as potential collaborators.
Therefore adhering to a coding style reduces the risk of mistakes and makes it easier to work together on software.
[Improving software quality, why Coding Style Matters](http://coding.smashingmagazine.com/2012/10/25/why-coding-style-matters/) is a nice article on why coding styles matter and how they increase software quality.

For example, [PEP8](https://www.python.org/dev/peps/pep-0008/) is the most widely used Python coding style and [ECMAScript 6](http://es6-features.org/) aka [ES6](http://es6-features.org/) is the scripting-language specification standardized by Ecma International for programming in Javascript.

For commonly used style guides for various programming languages see the [Language Guides](https://guide.esciencecenter.nl/best_practices/language_guides/languages_overview.html).
Google also has a style guide for many languages [google style guide page](https://code.google.com/p/google-styleguide/) that are used in open source projects originating out of Google.

### Automatic formatting

Numerous tools exists to automatically format code such that it follows a certain style. Automatic formatting enables higher code quality especially when you are collaborating in a team and other people need to look at the code you've written. Many developers and organisations maintain standards of code formatting like **2-space** or **4-space indentation**. Using these is highly recommended since the probablity of finding bugs(if any) increases multifold.

[EditorConfig](https://editorconfig.org) is a language independent tool that helps maintain consistent whitespace styles for multiple people working on the same project across various editors. Most editors support EditorConfig either natively or through a plugin. Though, almost all widely used IDEs and text-editors support automatic code formatting upon type. For Ex: [JetBrains IDE Suite](https://www.jetbrains.com/products.html#), [VSCode](https://code.visualstudio.com/) and [Atom](https://atom.io/).

In addition to that, there are many language specific tools for automatically formatting code according to a particular style.
Note that editors often support using these tools directly from the editing environment.

| Language   | Formatter Tool              |
|------------|-----------------------------|
| C/C++      | [GNUIndent](http://www.gnu.org/software/indent/), [GreatCode](http://sourceforge.net/projects/gcgreatcode/)|
| Python     | [Black](https://black.readthedocs.io), [yapf](https://pypi.org/project/yapf/)|
| Javascript | [beautifier.io](https://beautifier.io/)|
| Java       | [Google Java format](https://github.com/google/google-java-format), [JIndent](http://www.jindent.com/)|
| PHP        | [phpStylist](http://sourceforge.net/projects/phpstylist/)|
| Perl       | [PerlTidy](http://perltidy.sourceforge.net/)|
| Shell/Bash | [ShellIndent](http://www.bolthole.com/AWK.html)|
| CSS        | [CSSTidy](http://csstidy.sourceforge.net/)|
| HTML       | [Tidy](http://tidy.sourceforge.net/)|

**Quick Tip**: If you use VS Code as your primary text editor, you can enable automatic code formatting right into your browser. Open your preferences page in json mode and add the following line:

```json
"editor.formatOnSave": true,
```

## Online services providing software quality checks

There are several web services that analyze code and make the quality of the code visible.
Usually these services run one or more static code analysis tools that can also be used from the command line or integrated into your editor on your own computer.
Using a code quality service that integrates with a GitHub/GitLab repository is highly recommended, as it will make it spot and communicate about quality issues in pull requests.

Code quality analysis services are websites that often offer the following features:

- Automatically analyse your code after pushing it to GitHub/GitLab
- Usually free for open source projects
- Support multiple programming languages, but not every language will have the same level of features
- Grade or score for the quality of all of the code in the repository
- List of issues with the code, grouped by severity
- Drill down to location of issue
- Default list of checks which the service provider finds the best practice
- Can be configured to make the list of checks more strict or relaxed
- Can be configured to ignore files or extensions
- Can read a configuration file from repository
- Track issues over time and send alerts when quality deteriorates
- Optionally reports on code coverage generated by a CI build
- Automatically deploy the repository and generates a preview build for review before final release.

For a list of choices see [shields.io](https://shields.io/category/analysis) or [this list of services that are free for open source projects](https://github.com/ripienaar/free-for-dev#code-quality).

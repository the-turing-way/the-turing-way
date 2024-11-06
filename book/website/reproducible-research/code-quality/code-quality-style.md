(rr-code-style)=
# Code Style and Formatting

A coding style is a set of conventions on how to format code.
For instance, what do you call your variables? Do you use spaces or tabs for indentation? Where do you put comments?
Consistently using the same style throughout your code makes it easier to read.
Code that is easy to read is easier to understand by you as well as by potential collaborators.
Therefore, adhering to a coding style reduces the risk of mistakes and makes it easier to work together on software.
[Why Coding Style Matters](http://coding.smashingmagazine.com/2012/10/25/why-coding-style-matters/) is a nice article on why coding styles matter and how they increase software quality.

For example, [PEP8](https://www.python.org/dev/peps/pep-0008/) is the most widely used Python coding style and [ECMAScript 6](http://es6-features.org/) aka [ES6](http://es6-features.org/) is the scripting-language specification standardized by ECMA International for programming in Javascript.

For commonly used style guides for various programming languages see the [Language Guides](https://guide.esciencecenter.nl/#/best_practices/language_guides/languages_overview).
Google also has a [style guide](https://code.google.com/p/google-styleguide/) for many languages that are used in open source projects originating out of Google.

(rr-code-style-and-formatting)=
## Automatic formatting

Numerous tools exists to automatically format code such that it follows a certain style. Automatic formatting enables higher code quality, especially when you are collaborating in a team and other people need to look at the code you've written.
Many developers and organisations maintain standards of code formatting like **2-space** or **4-space indentation**. Using these is highly recommended since the probability of finding bugs (if any) increases multifold.

[EditorConfig](https://editorconfig.org) is a language independent tool that helps maintain consistent whitespace styles for multiple people working on the same project across various editors.
Most editors support EditorConfig either natively or through a plugin.
Almost all widely used IDEs and text-editors support automatic code formatting upon typing. For example: [JetBrains IDE Suite](https://www.jetbrains.com/products.html#) and [VSCode](https://code.visualstudio.com/).

In addition to that, there are many language specific tools for automatically formatting code according to a particular style.
Note that editors often support using these tools directly from the editing environment.

| Language      | Formatter Tool              |
|---------------|-----------------------------|
| C/C++         | [GNUIndent](http://www.gnu.org/software/indent/), [GreatCode](http://sourceforge.net/projects/gcgreatcode/)|
| Python        | [Black](https://black.readthedocs.io), [yapf](https://pypi.org/project/yapf/)|
| Javascript    | [beautifier.io](https://beautifier.io/)|
| Java          | [Google Java format](https://github.com/google/google-java-format), [JIndent](http://www.jindent.com/)|
| MATLAB/Octave | [MISS_HIT](https://florianschanda.github.io/miss_hit/)|
| PHP           | [phpStylist](http://sourceforge.net/projects/phpstylist/)|
| Perl          | [PerlTidy](http://perltidy.sourceforge.net/)|
| R             | [formatR](https://yihui.org/formatr/)|
| Shell/Bash    | [ShellIndent](http://www.bolthole.com/AWK.html)|
| CSS           | [CSSTidy](http://csstidy.sourceforge.net/)|
| HTML          | [Tidy](http://tidy.sourceforge.net/)|

**Quick Tip**: If you use VS Code as your primary text editor, you can enable automatic code formatting right into your browser. Open your preferences page in JSON mode and add the following line:

```
"editor.formatOnSave": true,
```

(rr-code-style-service)=
## Online services providing software quality checks

There are several web services that analyse code and make the quality of the code visible.
Usually these services run one or more static code analysis tools that can also be used from the command line or integrated into your editor on your own computer.
Using a code quality service that integrates with a GitHub/GitLab repository is highly recommended, as it can detect and communicate quality issues in pull requests.

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

For a list of choices see [shields.io](https://shields.io/badges) or [this list of services that are free for open source projects](https://github.com/ripienaar/free-for-dev#code-quality).

(rr-code-quality)=
# Code Quality

| Prerequisite                                                                                  | Importance |
| --------------------------------------------------------------------------------------------- | ---------- |
| {ref}`Experience with the command line<rr-overview-resources-commandline>` | Helpful    |

## Summary

There are several ways to improve software quality that require relatively little effort.
By following a coding style, code will be easier for yourself and others to understand and therefore it will contain fewer bugs.
Tools for static code analysis can report bugs as well as style issues without even running the code.

## Static code analysis

Static code analysis is a method that examines code and detects software vulnerabilities before your code is executed or the project is built and deployed.
This analysis is capable of identifying quality issues, including security weaknesses and errors.
In addition to finding bugs, many of these tools can also help maintain a consistent coding style.

(rr-code-quality-advantages)=
### Advantages of Static code analysis

- Write high-quality code: Early detection of possible programming errors help developers to know where they went wrong.

- Achieve regulatory compliance: Achieving software compliance is crucial for the stability and security of products.
With this, developers can comprehensively test their code in a non-runtime environment, ensuring all code standards are met and enterprise security is achieved.

- Accelerate software development life-cycles: Static code analysis ensures high-quality code reaches testers in less time.
This means that even testers take much less time to test the product, thus accelerating software development life-cycles.

Some of the most widely used `linters` are mentioned in the below table:

| Language                  | Static code analysis tool|
|---------------------------|------------------------|
| C/C++                     | [Cppcheck](http://cppcheck.sourceforge.net/), [cpplint](https://github.com/cpplintcpplint)|
| Python                    | [Pylint](https://pypi.org/project/pylint/), [prospector](https://prospector.readthedocs.io)|
| Javascript                | [ESLint](https://eslint.org/), [JSlint](https://jslint.com/), [JSHint](https://jshint.com/)|
| Java                      | [Checkstyle](https://checkstyle.sourceforge.io/), [FindBugs](http://findbugs.sourceforge.net), [PMD](https://pmd.github.io/)|
| Perl                      | [PerlTidy](https://metacpan.org/pod/perltidy)|
| R                         | [lintr](https://github.com/jimhester/lintr)|
| Shell/Bash                | [shellcheck](https://www.shellcheck.net)|

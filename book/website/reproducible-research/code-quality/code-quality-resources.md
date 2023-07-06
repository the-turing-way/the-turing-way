# Checklist and Reading Recommendations

## Checklist

### For code auto-formatting

- Write your development code in your favourite IDE/text-editor.
- Enable auto formatting in your editor by tweaking the preferences/settings.
- Type `Ctrl + s` (windows, linux) or `⌘ + s` (mac) to save the work to format the code.

### For static code analysis

- Build the project to enable `linters` to spot the errors/warnings in the code (if any).
- Make relevant changes and repeat the above step.
- {ref}`Commit and push<rr-vcs-git-commit>` the changes to remote **Github/GitLab/BitBucket** repository to run the pre-deployment tests.

### For robust code

- Find assumptions in your program, and make them explicit.
- Write if/else statements to test your assumptions.
- Consider errors that may be raised in your program.
- Decide per assumption and error what should happen: redirect, report, or abort.
- When raising errors, make suree to write informative and actionable messages.

## Further reading

- [Article by University of Freiburg](https://swt.informatik.uni-freiburg.de/service/coding-conventions)
- [Coding Conventions - Wikipedia](https://en.wikipedia.org/wiki/Coding_conventions)
- [An exhaustive list of static code analysis tools - Wikipedia](https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis)
- [Excellent compilation of code analysis guidelines - OWASP](https://owasp.org/www-community/controls/Static_Code_Analysis)
- [ECMA International ES6 guide](http://www.ecma-international.org/ecma-262/6.0/)

## References specific for this chapter

- [Static Tool analysis guide](https://en.wikipedia.org/wiki/Static_program_analysis)
- [KeyBindings in VSCode](https://code.visualstudio.com/docs/getstarted/keybindings)
- [Dev.To blog about text-editor customization](https://dev.to/josuerodriguez98/my-vs-code-customization-i4o)
- [EditorConfig guide](https://editorconfig.org/)

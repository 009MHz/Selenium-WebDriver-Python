# [Semantic Commit Messages](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716#semantic-commit-messages)
See how a minor change to your commit message style can make you a better programmer.

Format: `<type>(<scope>): <subject>`

`<scope>` is optional

## Example
```
feat: add hat wobble
^--^  ^------------^
|     |
|     +-> Summary in present tense.
|
+-------> Type: chore, docs, feat, fix, refactor, style, or test.
```
More Examples:

- `ftr`: (new feature for the user, not a new feature for build script)
- `fix`: (bug fix for the user, not a fix to a build script)
- `docs`: (changes to the documentation)
- `style`: (formatting, missing semi colons, etc; no production code change)
- `ref`: (refactoring production code, eg. renaming a variable)
- `test`: (adding missing tests, refactoring tests; no production code change)
- `chore`: to describe a commit or change that does not directly relate to adding a new feature or fixing a bug. It is typically used for miscellaneous or maintenance tasks that are necessary for the project but do not fall into the categories of features or bug fixes

References:
- https://www.conventionalcommits.org/
- https://seesparkbox.com/foundry/semantic_commit_messages
- http://karma-runner.github.io/1.0/dev/git-commit-msg.html


# [Semantic Branch Names](https://gist.github.com/seunggabi/87f8c722d35cd07deb3f649d45a31082#semantic-branch-names)
Semantic Branch Names
See how a minor change to your branch name style can make you a better programmer.

Format: `<type>/#<issueNumber>-<alias>`
```
Example
feature/#1-init
^------^   ^---^
|          |
|          +---> issue's keyword
|
+-------> Type: or feat, chore, docs, fix, refactor, style, or test.
```
More Examples:

- `ftr`: (new feature for the user, not a new feature for build script)
- `fix`: (bug fix for the user, not a fix to a build script)
- `docs`: (changes to the documentation)
- `style`: (formatting, missing semi colons, etc; no production code change)
- `ref`: (refactoring production code, eg. renaming a variable)
- `test`: (adding missing tests, refactoring tests; no production code change)
- `chore`: (updating grunt tasks etc; no production code change)


References:  <br>
https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716
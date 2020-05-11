  #!/usr/bin/env bash
  # halt script on error
  set -e
  # Build locally, deleting any existing doctrees, and then check links
  sphinx-build -E -W -b linkcheck -c ./book/website/_config.py ./book/website ./book/website/_build
# Making software citable

Digital Object Identifiers are globally unique identifiers which can point to
any digital object, such as a version of a paper, a version of software etc.
This has the advantage that it is unambigous and standardized. For papers, using
DOIs is commonplace, and a DOI is usually provided by the publisher. For
software, you can make your own DOI with [Zenodo](https://zenodo.org/):

1. You can tell people how to cite your software by including a ``CITATION.cff``
file in the root of your repository (You can read up on the rationale of
``CITATION.cff`` files in [this
blog](https://www.software.ac.uk/blog/2017-12-12-standard-format-citation-files)).
However, writing ``CITATION.cff`` files by hand is a bit tedious and
error-prone, so instead go to
https://citation-file-format.github.io/cff-initializer-javascript/ and fill in
the provided web form.
1. Make a [Zenodo](https://zenodo.org/) account and link it with your GitHub account as explained on [guides.github.com/activities/citable-code](https://guides.github.com/activities/citable-code/).
1. You can tell Zenodo what metadata you want to associate with the software by
including a ``.zenodo.json`` file in the root of your repository, but writing
that file by hand is also error-prone. Therefore it is advisable to just generate it
from the ``CITATION.cff`` file. To do so, you'll need a command line tool
``cffconvert`` which you can install [from
PyPI](https://pypi.org/project/cffconvert/) by:

    ```bash
    pip install --user cffconvert
    ```
1. Make sure that your ``CITATION.cff`` is valid YAML by copy-pasting the
contents to http://www.yamllint.com/.
1. Make sure that your ``CITATION.cff`` is valid CFF, by:

    ```bash
    # (in the repository's root directory)
    cffconvert --validate
    ```
    
    If the command does not return anything, that means the CFF is valid.

1. Generate the ``.zenodo.json`` file using ``cffconvert`` as follows:

    ```bash
    cffconvert --ignore-suspect-keys --outputformat zenodo --outfile .zenodo.json
    ```
1. On Zenodo, make sure to 'Flip the switch' to the ``on`` position on the
GitHub repository that you want to make a release of.
1. Go to your Github repository, use the _Create a new release_ button to create
a release on GitHub.
1. Zenodo should automatically be notified and should make a snapshot copy of
the current state of your repository (just one branch, without any history), and
should also assign a persistent identifier (DOI) to that snapshot.

    **when things don't work**

    In case the GitHub-Zenodo integration does not work as expected, there are
    two places to go and look for information:
    1. On GitHub:
        - go to ``https://github.com/<org>/<repo>/``
        - select ``Settings``
        - select ``Webhooks``
        - select select the Zenodo webhook (may require GitHub login)
        - scroll down to ``Recent deliveries``
        - click on one of the listed deliveries for details on the request, the response, and to request redelivery.
    1. On Zenodo:
        - go to ``https://zenodo.org/account/settings/github/``
        - select the repository that you want to see the diagnostic information of
        - click on one of the releases to see the _Payload_ Zenodo received from GitHub, as well as the _Metadata_ that Zenodo has associated with your release, or _Errors_ if there were any.

1. Use the DOI whenever you refer to your software, be it in papers, posters, or
even tweets and blogs.
1. Add the software's Zenodo badge to your repository's README.
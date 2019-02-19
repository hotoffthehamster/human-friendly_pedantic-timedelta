############
Contributing
############

.. |virtualenvwrapper| replace:: ``virtualenvwrapper``
.. _virtualenvwrapper: https://pypi.org/project/virtualenvwrapper/

.. |flake8| replace:: ``flake8``
.. _flake8: http://flake8.pycqa.org/en/latest/

.. |pytest| replace:: ``pytest``
.. _pytest: https://docs.pytest.org/en/latest/

.. |tox| replace:: ``tox``
.. _tox: https://tox.readthedocs.io/en/latest/

.. contents:: Contributing Contents
   :depth: 2
   :local:

Contributions are welcome, and they are greatly appreciated!

Every little bit helps, and credit will always be given (if so desired).

=================
How to Contribute
=================

You can contribute in many ways:

Report Bugs
-----------

Report bugs at https://github.com/hotoffthehamster/human-friendly_pedantic-timedelta/issues.

When reporting a bug, please include:

* Your operating system name and version, and the Python version you are using.

* Any details about your local setup that might be helpful for troubleshooting.

* Detailed steps to reproduce the bug.

Fix Bugs
--------

Look through the GitHub issues for anything tagged with "bug".
Pick one, assign yourself to it, and work on the issue.

Implement Features
------------------

Look through the GitHub issues for anything tagged with "feature".
Pick one, assign yourself to it, and work on the issue.

Write Documentation
-------------------

If you find documentation out of date, missing, or confusing,
please help improve it. This includes the official user documenation,
the README, other developer documenation, and documentation.

We also appreciate reference from blog posts, articles, and other projects.

Submit Feedback
---------------

The best way to send feedback is to file an issue at
https://github.com/hotoffthehamster/human-friendly_pedantic-timedelta/issues.

See above for reporting bugs.

If you are proposing a feature:

* Explain in detail how the feature should work.
* Unless you expect to work on the code yourself, your chances of having a
  feature implemented are greater if you keep the scope focused and narrow
  such that it's as simple as possible for a developer to work on.
  That, or a monetary contribution speaks volumes.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome! You are encouraged to fork the project, hack away, and submit
  pull requests for new features (and bug fixes).
* Above all else, please be considerate and kind.
  A few nice words can go a long way!

Please also feel free to email the author directly if you have any other
questions or concerns. Response times may vary depending on season.

===============
Getting Started
===============

Ready to contribute?

Here's how to set up ``human-friendly_pedantic-timedelta`` for local development.

1. Fork the ``human-friendly_pedantic-timedelta`` repo on GitHub.

   * Visit `<https://github.com/hotoffthehamster/human-friendly_pedantic-timedelta>`_ and click *Fork*.

2. Clone your fork locally.

   Open a local terminal, change to a directory you'd like to develop from,
   and run the command::

    $ git clone git@github.com:<your_login>/human-friendly_pedantic-timedelta.git

3. Install the project into a Python virtual instance, or ``virtualenv``.

   First, ensure that you have |virtualenvwrapper|_ installed.

   Next, set up a virtual environment for local development::

    $ cd human-friendly_pedantic-timedelta/
    $ mkvirtualenv -a $(pwd) pedantic-timedelta

   *Note:* We use the ``-a`` option so that ``cdproject`` changes directories
   to the ``human-friendly_pedantic-timedelta/`` directory when we're in the virtual environment.

   Next, set up your fork for local development::

    (pedantic-timedelta) $ cdproject
    (pedantic-timedelta) $ make develop

   *Hint:* As usual, run ``workon`` to activate the virtual environment, and
   ``deactivate`` to leave it. E.g.,::

    # Load the Python virtual instance.
    $ workon pedantic-timedelta
    (pedantic-timedelta) $

    # Do your work.
    (pedantic-timedelta) $ ...

    # Finish up.
    (pedantic-timedelta) $ deactivate
    $

4. Before starting work on a new feature or bugfix, make sure your
   ``develop`` branch is up to date with the official branch::

    (pedantic-timedelta) $ cdproject
    (pedantic-timedelta) $ git remote add upstream git@github.com:hotoffthehamster/human-friendly_pedantic-timedelta.git
    (pedantic-timedelta) $ git fetch upstream
    (pedantic-timedelta) $ git checkout develop
    (pedantic-timedelta) $ git rebase upstream/develop
    (pedantic-timedelta) $ git push origin HEAD

5. Create a branch for local development. If you are working on an known issue,
   you may want to reference the Issue number in the branch name, e.g.,::

    $ git checkout -b feature/ISSUE-123-name-of-your-issue

   Now you can add and edit code in your local working directory.

6. Do your work and make one or more sane, concise commits::

    $ git add -p
    $ git commit -m "<Category>: <Short description of changes.>

    - <Longer description, if necessary.>"

   IMPORTANT: Please make each commit as small and sane as possible.

   Follow these guidelines:

   * Each commit should generally focus on one thing, and one thing only,
     and that thing should be clearly described in the first line of the
     commit message.

   * Please use a one-word categorical prefix (see below) to make it easy for
     someone reading the git log to understand the breadth of your changes.

   * If you move or refactor code, the move or refactor should be captured
     in a single commit *with no other code changes.*

     E.g., if you want to enhance a function, but you find that you need to
     refactor it to make it easier to hack on, first refactor the function
     -- without adding any new code or making any other changes -- and then
     make a commit, using the ``Refactor:`` prefix. Next, add your new code,
     and then make a second commit for the new feature/enhancement.

   * Following are some examples of acceptable commit message prefixes:

     * ``Feature: Added new feature.``

     * ``Bugfix: Fixed problem doing something.``

     * ``Refactor: Split long function into many.``

     * ``Version: X.Y.Z.``

     * ``Tests: Did something to tests.``

     * ``Docs: Update developer README.``

     * ``Debug: Add trace messages.``

     * ``Developer: Improved developer experience [akin to `Debug:` prefix].``

     * ``Linting: Adjust whitespace.``

     * ``Regression: Oh, boy, when did this get broke?``

     * ``i18n/l10n: Something about words.``

     * ``Feedback: Fix something per PR feedback.``

     (You'll notice that this strategy is similar to
     `gitmoji <https://gitmoji.carloscuesta.me/>`__,
     but it's more concise, and less obtuse.)

7. Throughout development, run tests and the linter -- and definitely before
   you submit a Pull Request.

   ``human-friendly_pedantic-timedelta`` uses
   |flake8|_ for linting,
   |pytest|_ for unit testing, and
   |tox|_ for verifying against the many versions of Python.

   You can run all of these tools with one command::

    $ make test-all

   .. _rebase_and_squash:

8. Rebase and squash your work, if necessary, before submitting a Pull Request.

   E.g., if the linter caught an error, rather than making a new commit
   with just the linting fix(es), make a temporary commit with the linting
   fixes, and then squash that commit into the previous commit wherein
   you originally added the code that didn't lint.

   (*Note:* Rebasing is an intermediate Git skill, but you needn't be
   afraid. Just bear in mind that you should not rebase any branch that
   other developers are working on (which should not apply to your working
   branch, unless you are collaborating with others, which you're probably
   not). And know that ``git rebase --abort`` is your friend (though you might
   want to make a copy of your local working directory before rebasing, just
   to be safe; or at least make a new branch from the current ``HEAD``).)

   For example, pretend that I have the following git history::

    $ git log --oneline | head -3

    b1c07a4 Regression: Fix some old bug.
    17d1e38 Feature: Add my new feature.
    2e888c3 Bugfix: Oops! Did I do that?

   and then I commit a linting fix that should have been included with
   the second-to-last commit, ``17d1e38``.

   First, add the linting fix::

    $ git add -A
    $ git ci -m "Squash me!"

   Next, start a rebase::

    $ git rebase -i 2e888c3

   (*Note:* Use the SHA1 hash of the commit *after* the one you want squash into.)

   Git should open your default editor with a file that starts out like this::

    pick 2e888c3 Bugfix: Oops! Did I do that?
    pick 17d1e38 Feature: Add my new feature.
    pick b1c07a4 Regression: Fix some old bug.
    pick f05e080 Squash me!

   Reorder the commit you want to squash so that it's after the commit
   you want to combine it with, and change the command from ``pick`` to
   ``squash`` (or ``s`` for short)::

    pick 2e888c3 Bugfix: Oops! Did I do that?
    pick 17d1e38 Feature: Add my new feature.
    squash f05e080 Squash me!
    pick b1c07a4 Regression: Fix some old bug.

   Save and close the file, and Git will rebase your work.

   When Git rebases the commit being squashed, it will pop up your editor
   again so you can edit the commit message of the new, squashed commit.
   Delete the squash comment (``Squash me!``), and save and close the file.

   Git should hopefully finish up and report, ``Successfully rebased and updated``.

   (If not, you can manually resolve any conflicts. Or, you can run
   ``git rebase --abort`` to rollback to where you were before the rebase,
   and you can look online for more help rebasing.)

9. Push the changes to your GitHub account.

   After testing and linting, and double-checking that your new feature or
   bugfix works, and rebasing, and committing your changes, push them to
   the branch on your GitHub account::

    $ git push origin feature/ISSUE-123-name-of-your-issue

   *Note:* If you pushed your work and then rebased, you may have to force-push::

    $ git push origin feature/ISSUE-123-name-of-your-issue --force

   .. _rebase_atop_develop:

10. Finally,
    `submit a pull request <https://github.com/hotoffthehamster/human-friendly_pedantic-timedelta/pulls>`_
    through the GitHub website.

    *Important:* Please rebase your code against ``develop`` and resolve
    merge conflicts, so that the main project maintainer does not have
    to do so themselves. E.g.,::

     $ git checkout feature/ISSUE-123-name-of-your-issue
     $ git fetch upstream
     $ git rebase upstream/develop
     # Resolve any conflicts, then force-push.
     $ git push origin HEAD --force
     # And then open the Pull Request.

=======================
Pull Request Guidelines
=======================

Before you submit a pull request, check that it meets these guidelines:

1. Update docs.

   * Use docstrings to document new functions, and use inline comments
     as appropriate (longer comments should go into a reST file in the
     ``docs/`` directory).

   * Update ``README.rst`` if your feature adds to or changes the API.

2. Include tests.

   * If the pull request adds new functions, they should be tested,
     either implicitly, because they're already called by an existing
     test. Or they should be called explicitly, because you added new
     tests for them.

   * We strive for 100% test coverage, but we do not enforce it.
     In the least, your code should not reduce coverage.

3. Commit sensibly.

   * Each commit should be succinct and singular in focus.
     Refer to `rebasing and squashing`__, above.

     __ rebase_and_squash_

   * Rebase your work atop develop (as `mentioned above`__)
     before creating the PR, or after making any requested
     changes.

     __ rebase_atop_develop_

4. Run ``make test-all``.

   * 'nough said.

==============
Debugging Tips
==============

To run one test or a subset of tests, you can specify a substring
expression using the ``-k`` option with ``make test``::

    $ make test TEST_ARGS="-k NAME_OF_TEST_OR_SUB_MODULE"

The substring will be Python-evaluated. As such, you can test multiple
tests using ``or``, e.g., ``-k 'test_method or test_other'``.
Or you can exclude tests using ``not``, e.g., ``-k 'not test_method'``.

Note that ``readline`` functionality will not work from any breakpoint
you encounter under ``make test``. (For example, pressing the Up arrow
will print a control character sequence to the terminal, rather than
showing the last command you ran.) If you want to interact with the code
at runtime, run ``py.test`` instead (see next).

If you'd like to break into a debugger when a test fails, run ``pytest``
directly and have it start the interactive Python debugger on errors::

    $ py.test --pdb tests/

If you'd like a more complete stack trace when a test fails, add verbosity::

    $ py.test -v tests/

    # Or, better yet, two vees!
    $ py.test -vv tests/

If you'd like to run a specific test, use ``-k``, as mentioned above. E.g.,::

    $ py.test -k test__repr__no_start_no_end tests/

Put it all together to quickly debug a broken test. ::

    $ py.test --pdb -vv -k <test_name> tests/

You can also set breakpoints in the code with ``pdb``.
Simply add a line like this:

.. code-block:: python

    import pdb; pdb.set_trace()

To test against other Python versions than what is setup in your ``virtualenv``,
you can use ``tox`` and name an environment with the ``envlist`` option::

    $ tox -e NAME_OR_ENVIRONMENT

===============
Code of Conduct
===============

Please respect and adhere to the `Code of Conduct <code-of-conduct.html>`_.

And that's it!

**Happy 💬-Pedantic 🕐Timedelta⏳ Hacking!**


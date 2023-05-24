(rr-make-debugging)=
# Debugging Makefiles

When writing a Makefile, it can sometimes be useful to be able to see the
values of variables to catch mistakes or bugs in the Makefile. To facilitate
this, Make contains two commands: ``info`` and ``error``, and there is a debug
mode to Make.

With the ``info`` command you can print the current value of a variable to
stdout, while Make is processing the file. For instance, in the Makefile above
you could add:

```makefile
$(info $$DATA = $(DATA))
```

This will print ``DATA = data/action.csv ... data/western.csv``.

With the ``error`` command you can stop the execution of Make at a certain
point in the Makefile. This is useful when you want to print the value of a
variable and not run Make any further:

```makefile
$(error $$DATA = $(DATA))
```

Finally, you can also debug the Makefile by running Make with the debug flag:
``make -d``. This will print all the rules (including built-in ones) that Make
tries for each of the targets, and whether or not a rule needs to be run.

If you only want to print the rules that Make will run and not actually run
them, you can use ``make -n``. These last two options can also be combined, so
that you see the debug output and Make doesn't run anything: ``make -dn``.

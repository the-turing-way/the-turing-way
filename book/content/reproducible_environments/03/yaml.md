<a name="YAML_files"></a>

## YAML files

YAML is an indentation-based markup language which aims to be both easy to read and easy to write. Many projects use it for configuration files because of its readability, simplicity and good support for many programming languages. It can be used for a great many things including defining computational environments, and is well integrated with [Travis](https://travis-ci.org/) which is discussed in the chapter on continuous integration.

An a YAML file defining a computational environment might look something like this:

```
# Define the operating system as Linux
os: linux

# Use the xenial distribution of Linux
dist: xenial

# Use the programming language Python
language: python

# Use version of Python 3.2
python: 3.2

# Use the Python package numpy and use version 1.16.1
packages:
  numpy:
    version: 1.16.1
```

Note that as you can see here that comments can be added by preceding them with a `#`.

<a name="YAML_syntax"></a>

### YAML syntax

A YAML document can consist of the following elements.

<a name="Scalars"></a>

#### Scalars

Scalars are ordinary values: numbers, strings, booleans.

```
number-value: 42
floating-point-value: 3.141592
boolean-value: true

# strings can be both 'single-quoted` and "double-quoted"
string-value: 'Bonjour'
```

YAML syntax also allows unquoted string values for convenience reasons:

```
unquoted-string: Hello World
```

<a name="Lists_and_Dictionaries"></a>

#### Lists and Dictionaries

Lists are collections of elements:

```
jedis:
  - Yoda
  - Qui-Gon Jinn
  - Obi-Wan Kenobi
  - Luke Skywalker
```

Every element of the list is indented and starts with a dash and a space.

Dictionaries are collections of `key: value` mappings. All keys are case-sensitive.

```
jedi:
  name: Obi-Wan Kenobi
  home-planet: Stewjon
  species: human
  master: Qui-Gon Jinn
  height: 1.82m
```

Note that a space after the colon is mandatory.

<a name="YAML_gotchas"></a>

#### YAML gotchas

Due to the format aiming to be easy to write and read, there're some ambiguities in YAML.

- **Special characters in unquoted strings:** YAML has a number of special characters you cannot use in unquoted strings. For example, parsing the following sample will fail:
  ```
  unquoted-string: let me put a colon here: oops
  ```
  Quote the string value makes this value unambiguous:
  ```
  unquoted-string: "let me put a colon here: oops"
  ```
  Generally, you should quote all strings that contain any of the following characters: `[] {} : > |`.
- **Tabs versus spaces for indentation:** do _not_ use tabs for indentation. While resulting YAML can still be valid, this can be a source of many subtle
  parsing errors. Just use spaces.

<a name="How_to_use_YAML_to_define_computational_environments"></a>

### How to use YAML to define computational environments

Because of their simplicity YAML files can be hand written. Alternatively they can be automatically generated as discussed [above](#Package_management_systems). From a YAML file a computational environment can be replicated in a few ways.

- **Manually.** It can be done manually by carefully installing the specified packages. Because YAML files can also specify operating systems and versions that may or may not match that of the person trying to replicate the environment this may require the use of a [virtual machine](#Virtual_machines).
- **Via package management systems such as Conda.** As [discussed](#Package_management_systems) as well as being able to generate YAML files from computational environments Conda can also generate computational environments from YAML files.

<a name="Security_issues"></a>

### Security issues

There is an inherent risk in downloading/using files you have not written to your computer, and it is possible to include malicious code in YAML files. Do not load YAML files or generate computational environments from them unless you trust their source.

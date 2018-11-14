# Changelog

## [0.10.0] 2018-11-14

- **Library forked, and renamed to `forkit-django`.** The re-name will allow us
  to release new versions to PyPI.
- Add support for Django 1.8-2.1.
- Drop support for Django <= 1.7.
- Remove `__version__` `get_version` and `__version_info__` from `forkit`
  module.

## [0.9.6] - 2011-10-11

- Add LICENSE file.

## [0.9.5] - 2011-10-11

- Fix reset bug where the wrong config was being passed.

## [0.9.4] - 2011-10-11

- Arbitrary Signal Keyword Arguments. Each utility function can take any
additional keyword arguments that will be passed to each signal receiver
called for the entirety of the operation.

## [0.9.3] - 2011-10-10

- Deep Reset. Improved deep reset capability which does not incorrectly
fork related objects. In this implementation, only directly related
objects are traversed.

## [0.9.2] - 2011-10-05

- Pre and Post Signals. Signals have been implemented for customizing the
behavior of a `fork`, `reset`, `diff`, and `commit` outside of the normal
use of the API. The sender of the each signal is the model class of the
model instance being manipulated.

- The `fork`, `reset`, and `diff` pre- signals pass the `reference`,
`instance`, and `config` to the receiver. The `config` is a `dict` which
can be updated in-place for greater flexibility.

## [0.9.1] - 2011-10-04

- API Refactor. Public methods including `fork`, `reset`, `diff`, and
`commit` have been defined as standalone functions. This refactor
emphasizes greater coverage of applicability for all existing models
rather than only those that inherit from `ForkableModel`. `ForkableModel`
still contains the public methods for backwards compatibility and
convenience.

- Reset Method. Added `reset` method which requires a model instance
`target` that enables "resetting" an existing object rather than creating
a new object per `fork`.

## [0.9.0] - 2011-09-09

- Forking. Implemented an abstract model class `ForkableModel` which
supports shallow and deep forking model instances.

- Deferred Commits. All relationships are deferred from being saved until
the whole hierarchy has been traversed during forking. Forks are not
committed by default to ensure integrity errors are not forced.

- Diffs. `ForkableModel` also implements a `diff` method for instances
that can be used to compare data values against another object of the same
type.

- Limitations. `through` models for many-to-many fields are not yet
supported. Deep diffs are not yet supported.

## Naming

Variables and constants: data containers, use nouns or short phares with adjectives.
Ex:

```js
const userData = {};
```

Functions/methods: commands or calculated values, use verbs or short phares with
adjectives.
Ex:

```js
sendData();
```

Classes: "things", use nouns or short phares with nouns.
Ex:

```js
class User {}
```

#### Name casings

- `snake_case` (ex: Python)
- `camelCase` (ex: JS)
- `PascalCase` (ex: Classes)
- `kebab-case` (ex: custom HTML elements)

#### Naming functions

Functions performs an operation, so describe the operation. Ex: `getUserByEmail()`. If
the function computes a boolean, answer a true/false question. Ex: `isValid()`.

#### Naming classes

Describe the object. Ex: `Customer`.

#### Pitfalls

Don't include redundant information in names. Ex: `user = User('Max', 31).

## Comments, structure and formatting

Avoid redundant comments. Good comments: legal info., explanation which can't be
replaced by good naming, warnings, TODOs and documentation.

#### Formatting

Code should be readable like an essay, without many jumps. Split the code in files when
it has multiple concepts.

Vertical Opennes: Methods should be separated by blank lines, also lines of code that
differ in functionality should be separated by blank lines. On the other hand: Vertical
density (no blank lines) implies close link or assossiation.

Horizontal formatting: avoid long lines of code. Lines should be of the sizes
100-120-max 200 characters.

## Functions/methods

Calling the function, the number of arguments and it's order should all be
straightforward. A function should be small and do one thing.

- **Minimize** the number of arguments
- Consider using a single parameter (ex: can it be an object, specially for many
  arguments). Ex:

```js
const user = new User({ name: "Nat", email: "foo@example.com", age: "27" });
```

- Try to avoid output arguments, specially if they are unexpected. Ex: instead of
  `createId(user)`, that internally modifies a user, do `user.addId()`, to be explicit.

There are different levels of abstraction, and functions should do work that's one level
of abstraction below theirs. Try not to mix many levels of abstraction, rather, split
the functions into smaller fucntion.

- High level:

```js
isEmail(email);
```

- Low level:

```js
email.includes("@");
```

Rule of thumb: extract code that works on the same functionality, or that requires more
interpretation than the surrounding code.

DRY: "don't repeat yourself", don't write the same code more than once. Obs: being
granula as possible won't automaticallly improve readability.

Avoid unexpected side effects: the same input should return the same output (pure
function). Minimize the number of functions with side effects.

```js
function createUser(email, password) {
  const user = new User(email, password);
  startSession(user); // side effect
  return user;
}
```

A side effect is an operation which does not jus act on a function input and change the
function output but which instead changes the overall system/program state.

Obs: unit testing can help identify clean code.

## Control structures

Use guards and fail fast! Instead of:

```js
if (email.includes("@")) {
  // do stuff
}
```

Invert and just return if it has errors:

```js
if (!email.includes("@")) {
  return;
}
```

Some tips: avoid deep nesting, prefer positive checks (`isEmpty` than `isNotEmpty`),
utilize and throw errors, use factory functions and polymorphism.

## Classes & Objects

A bit of differentiation:

- Object: has private internal/properties, public API (methods)
- Data container/data structure: public internals/properties (almost) no API (methods)

Classes should be small, prefer many small classes over a few large ones.

Cohesion: how much are your class methods using the class properties? Maintain high
cohesion!

### Law of Demeter

The Law of Demeter (LoD) or principle of least knowledge is a design guideline for
developing software, particularly object-oriented programs. In its general form, the LoD
is a specific case of loose coupling. It can be summarized in each of the following
ways:

- Each unit should have only limited knowledge about other units: only units "closely"
  related to the current unit.
- Each unit should only talk to its friends; don't talk to strangers.
- Only talk to your immediate friends.

The fundamental notion is that a given object should assume as little as possible about
the structure or properties of anything else (including its subcomponents), in
accordance with the principle of "information hiding". It may be viewed as a corollary
to the principle of least privilege, which dictates that a module possess only the
information and resources necessary for its legitimate purpose.

### SOLID principles

- The **single-responsibility principle**: "There should never be more than one reason for a
  class to change." In other words, every class should have only one responsibility.
- The **open–closed principle**: "Software entities ... should be open for extension, but
  closed for modification."
- The **Liskov substitution principle**: "Functions that use pointers or references to base
  classes must be able to use objects of derived classes without knowing it." See also
  design by contract.
- The **interface segregation principle**: "Clients should not be forced to depend upon
  interfaces that they do not use."
- The **dependency inversion principle**: "Depend upon abstractions, not concretions."

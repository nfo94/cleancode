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

### Naming

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

### Comments, structure and formatting

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

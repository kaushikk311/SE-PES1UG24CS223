# Lab 5: Static Code Analysis — Issue Table

Project: L5_36_smart_home
File analyzed: smart_home.py

| Issue | Tool | line | Description | Fix approach |
|---|---|---:|---|---|
| Mutable default argument | Bug risk / Pylint W0102 | Line 11 | `settings={}` is shared across calls when no value is supplied. | Use `None`, then create a new dictionary inside the function. |
| Shell-enabled subprocess | Security / Bandit B602, high | Line 51 | A command string is executed with `shell=True`, allowing command injection if input is untrusted. | Validate the scene filename, resolve it under the scenes directory, and call subprocess with an argument list and `shell=False`. |
| All-interface bind address | Security / Bandit B104, medium | Line 4 | `0.0.0.0` exposes a service on all network interfaces if used for listening. | Make the host configurable and default to `127.0.0.1` for local-only use. Set a public bind address only when intentionally required and protected. |
| Hardcoded password | Security / Bandit B105, low | Line 7 | A password is embedded in source code. | Remove the unused hardcoded credential; if authentication is required, load a secret from a protected environment/configuration source. |
| CamelCase identifiers | Code quality / Pylint C0103 | Multiple | Function and argument names do not follow Python `snake_case`. | Rename functions and parameters consistently, including their call sites. |
| Inconsistent return behavior | Code quality / Pylint R1710 | Line 16 | `toggleDevice` returns a value on one path but not another. | Return `None` explicitly for an unknown device. |
| Missing encoding | Code quality / Pylint W1514 | Line 41 | `open()` relies on the platform default encoding. | Specify `encoding="utf-8"`. |
| Missing docstrings | Code quality / Pylint C0114, C0116 | Module and functions | Module and functions lack explanatory docstrings. | Add module and function docstrings. |
| Whitespace before colon | Style / Flake8 E203 | Line 6 | Extra whitespace occurs before a dictionary key's colon. | Remove the extra space. |
| Too few blank lines | Style / Flake8 E302 | Line 40 | A top-level function is not separated by the required blank lines. | Add the required blank line. |
| Inline comment spacing | Style / Flake8 E261 | Line 66 | The inline comment has insufficient preceding spaces. | Use at least two spaces before the comment. |
| Line too long | Style / Flake8 E501 | Line 68 | A line exceeds the configured 79-character limit. | Split the expression across multiple lines. |

Note: The line numbers above refer to the original uploaded source and may change after edits. Confirm exact post-fix findings by rerunning all tools.

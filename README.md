# Jarvis

Jarvis is a command-line personal assistant built for this repository. It uses a plugin-based architecture and a lightweight installer to prepare the environment.

## Repository

Current GitHub repository:

- https://github.com/Jatin-garg22/jarvis-ai-assistant.git

## What this project contains

### Core application

- `jarviscli/` — main application code, command interpreter, and plugin loader
- `custom/` — place your own plugins here
- `installer/` — setup scripts and dependency installation flow

### Setup scripts

- `setup.bat` — Windows setup entry point
- `setup.sh` — Linux/macOS setup entry point

## Supported commands in this version

The current runtime only enables the commands that are allowed by the plugin manager. The active commands are:

- `weather`
- `news`
- `search`
- `gmail`
- `dictionary`
- `clock`
- `timer`
- `website`
- `qr`
- `wifi`
- `tasks`
- `battery`
- `location`
- `open`
- `play`
- `hear`

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jatin-garg22/jarvis-ai-assistant.git
cd Jarvis-master
```

### 2. Run the setup script

#### Windows

```bat
setup.bat
```

#### Linux / macOS

```bash
./setup.sh
```

### 3. Run the installer directly (optional)

```bash
python installer
```

## Running the assistant

From the project root, use a single command:

```bat
run.bat
```

This launcher uses the local virtual environment and starts the CLI without extra setup steps.

## How to add your own plugin

Create a new Python file inside `custom/` and add a plugin decorator.

```python
from plugin import plugin


@plugin("helloworld")
def helloworld(jarvis, s):
    """Repeats what the user types."""
    jarvis.say(s)
```

After adding the file, start Jarvis and use the command name you defined.

## Project notes

- This README reflects the current code layout and the current active command set.
- Unused command files were removed from `jarviscli/plugins/`.
- The `installer/` folder is still required for setup and dependency preparation.

## Troubleshooting

### Python module issues

If the assistant fails to start because of missing modules, recreate the environment and rerun the installer.

### Plugin issues

If a command is not appearing, confirm that:

1. The plugin file is present in `custom/` or `jarviscli/plugins/`
2. The command name matches the plugin decorator
3. The plugin is included in the current runtime allowlist

## Support

For questions or updates, use the repository at:

- https://github.com/Jatin-garg22/jarvis-ai-assistant.git

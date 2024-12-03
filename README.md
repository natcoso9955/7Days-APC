
# 7days-APC: 7 Days Afterlife Prerequisite Checker
[![GitHub Build](https://github.com/gorcon/rcon-cli/workflows/build/badge.svg)](https://github.com/gorcon/rcon-cli/actions)
![GitHub License](https://img.shields.io/github/license/natcoso9955/7Days-APC)
![GitHub top language](https://img.shields.io/github/languages/top/natcoso9955/7Days-APC)
![GitHub Created At](https://img.shields.io/github/created-at/natcoso9955/7Days-APC)
![GitHub last commit](https://img.shields.io/github/last-commit/natcoso9955/7Days-APC)

**7days-APC** (7 Days Afterlife Prerequisite Checker) is a utility designed to help Linux users prepare their systems to run the **Afterlife** mod for the game *7 Days to Die*. This script automates the process of installing the required dependency, `libgdiplus`, which is essential for the mod to function properly on Linux.

The project provides an evolving resource for Linux (and potentially Windows) users who prefer running mods without relying on third-party launchers.

---

## Features

- **Automatic Dependency Installation**: Detects your package manager, then installs `libgdiplus`.
- **Documentation**: Includes detailed guides for manual setup and troubleshooting.
- **Expandable**: Designed with scalability in mind, allowing for future additions such as mod auto-updaters and dependency management.

---

## How to Use the Script

### Prerequisites

1. A Linux system with administrative (root) access.
2. Python 3.6+ installed on your system (optional, only needed for the Python script).

### Running the Script

1. **Download the Script**:
   ```bash
   curl -O https://raw.githubusercontent.com/natcoso9955/7Days-APC/main/afterlife_prereq_checker.sh
   ```

2. **Make the Script Executable**:
   ```bash
   chmod +x afterlife_prereq_checker.sh
   ```

3. **Run the Script with Root Privileges**:
   ```bash
   sudo ./afterlife_prereq_checker.sh
   ```

4. **Follow On-Screen Prompts**:
   - The script will identify your package manager and attempt to install `libgdiplus`.

---

## Guides

For detailed instructions and additional resources, see:

- [Manual Installation Guide](./guides/prereq_manual_installation.md): Step-by-step instructions for manually installing dependencies.
<!---- [Mod Installation Guide](./guides/mod_installation.md): Instructions for downloading and setting up mods like Afterlife.
- [Troubleshooting Guide](./guides/troubleshooting.md): Common issues and their solutions.--->

---

## Contributing to the Project

This repository is a community effort to make mods like Afterlife accessible on Linux. Contributions are welcome! Here’s how you can help:

1. **Create Pull Requests**: Submit improvements, bug fixes, or additional features.
2. **File Issues**: Report problems or suggest new features via GitHub Issues.
3. **Spread the Word**: Share this project with other Linux users in the *7 Days to Die* community.

---

## Support the Afterlife Mod

This project would not be possible without the amazing **Afterlife Mod** and its community. Show your support by joining the [Afterlife Discord](https://discord.gg/2cfHGJQhBR).

---

## License

This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

Special thanks to the *7 Days to Die* modding community for their contributions and support in keeping Linux gaming alive!

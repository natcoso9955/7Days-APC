
# 7days-APC: 7 Days Afterlife Prerequisite Checker

**7days-APC** (7 Days Afterlife Prerequisite Checker) is a utility designed to help Linux users prepare their systems to run the **Afterlife** mod for the game *7 Days to Die*. This script automates the process of installing the required dependency, `libgdiplus`, which is essential for the mod to function properly on Linux.

The project aims to provide a centralized, evolving resource for Linux (and potentially Windows) users who prefer running mods without relying on third-party launchers. As new challenges arise, this project will grow to address them.

---

## Features

- **Automatic Dependency Installation**: Detects your package manager, then installs `libgdiplus`.
- **Manual Installation Instructions**: Includes detailed commands for users who prefer a manual setup.
- **Error Handling**: Provides meaningful error messages and guidance if the script cannot install the library.
- **Expandable**: Designed with scalability in mind, allowing for future additions such as mod auto-updaters and dependency management.

---

## How to Use the Script

### Prerequisites

1. A Linux system with administrative (root) access.
2. Python 3.6+ installed on your system.

### Running the Script

1. **Download the Script**:
   ```bash
   curl -O https://raw.githubusercontent.com/natcoso9955/7Days-APC/main/afterlife_prereq_checker.sh
   ```

2. **Make the Script Executable**:
   ```bash
   chmod +x afterlife-prereq-checker.sh
   ```

3. **Run the Script with Root Privileges**:
   ```bash
   sudo ./afterlife-prereq-checker.sh
   ```

4. **Follow On-Screen Prompts**:
   - The script will identify your package manager, and attempt to install `libgdiplus`.
   - If it encounters issues, refer to the [Manual Installation](#manual-installation) section below.

---

## Manual Installation

If you prefer to install `libgdiplus` manually or the script is unable to do so, follow the steps below based on your distribution.

### Step 1: Update Your Package Manager
Always ensure your package manager is up to date:
- **Debian/Ubuntu**:
  ```bash
  sudo apt update
  ```
- **CentOS/RHEL**:
  ```bash
  sudo yum update
  ```
- **Fedora**:
  ```bash
  sudo dnf update
  ```
- **Arch Linux**:
  ```bash
  sudo pacman -Syu
  ```

### Step 2: Install `libgdiplus`
Use the appropriate command for your system:
- **Debian/Ubuntu**:
  ```bash
  sudo apt install -y libgdiplus
  ```
- **CentOS/RHEL**:
  ```bash
  sudo yum install -y libgdiplus
  ```
- **Fedora**:
  ```bash
  sudo dnf install -y libgdiplus
  ```
- **Arch Linux**:
  ```bash
  sudo pacman -Sy libgdiplus
  ```

### Step 3: Verify Installation
To confirm the library is installed:
```bash
ldconfig -p | grep libgdiplus
```
If `libgdiplus` appears in the output, the installation was successful.

---

## Contributing to the Project

This repository is a community effort to make mods like Afterlife accessible on Linux. Contributions are welcome! Here’s how you can help:

1. **Create Pull Requests**: Submit improvements, bug fixes, or additional features.
2. **File Issues**: Report problems or suggest new features via GitHub Issues.
3. **Spread the Word**: Share this project with other Linux users in the *7 Days to Die* community.

---

## Future Plans

The 7days-APC project aims to evolve into a comprehensive utility for modding on Linux. Planned features include:

1. **Mod Auto-Updater**: A script to automate downloading, extracting, and replacing mod files.
2. **Comprehensive Prerequisite Checker**: Expand dependency checks beyond `libgdiplus` as new mod requirements emerge.
3. **Windows Support**: Extend compatibility to Windows systems.

---

## Manual Mod Installation Instructions (Planned)

*This section will be expanded in the future to provide step-by-step instructions for downloading and installing the Afterlife mod manually via the command line.*

---

## License

This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

Special thanks to the *7 Days to Die* modding community for their contributions and support in keeping Linux gaming alive!

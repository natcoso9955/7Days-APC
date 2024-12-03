
# Prerequisite Manual Installation Guide

This guide provides step-by-step instructions for manually installing the `libgdiplus` library required to run the **Afterlife** mod on Linux systems.

## Step 1: Update Your Package Manager

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

## Step 2: Install `libgdiplus`

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

## Step 3: Verify Installation

To confirm the library is installed:
```bash
ldconfig -p | grep libgdiplus
```

If `libgdiplus` appears in the output, the installation was successful.

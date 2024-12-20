#!/usr/bin/env python3

"""
7days-APC: Afterlife Prereq Checker

This script checks if the necessary prerequisites for the Afterlife mod are installed
on a Linux system. It ensures the system has a supported package manager, installs 
libgdiplus, and verifies the installation. It should be run as root for proper installation 
of dependencies.
"""

import os
import subprocess
import sys
import shutil

# Colors for output
GREEN = "\033[0;32m"
RED = "\033[0;31m"
NC = "\033[0m"  # No Color

def check_root():
    """Ensure the script is run as root."""
    if os.geteuid() != 0:
        print(f"{RED}Please run this script as root.{NC}")
        sys.exit(1)

def detect_package_manager():
    """Identify the available package manager."""
    if shutil.which("apt"):
        return "apt"
    if shutil.which("yum"):
        return "yum"
    if shutil.which("dnf"):
        return "dnf"
    if shutil.which("pacman"):
        return "pacman"
    return None

def install_libgdiplus(pkg_manager):
    """Install libgdiplus using the appropriate package manager."""
    commands = {
        "apt": ["apt", "update", "&&", "apt", "install", "-y", "libgdiplus"],
        "yum": ["yum", "install", "-y", "libgdiplus"],
        "dnf": ["dnf", "install", "-y", "libgdiplus"],
        "pacman": ["pacman", "-Sy", "--noconfirm", "libgdiplus"],
    }
    command = commands.get(pkg_manager)
    if not command:
        print(f"{RED}Unsupported package manager: {pkg_manager}.{NC}")
        sys.exit(1)

    try:
        print(f"{GREEN}Installing libgdiplus using {pkg_manager}...{NC}")
        subprocess.run(command, check=True, shell=True)
        print(f"{GREEN}libgdiplus installed successfully!{NC}")
    except subprocess.CalledProcessError:
        # pylint: disable=locally-disabled, line-too-long
        print(f"{RED}Failed to install libgdiplus.Please check your package manager and try again.{NC}")
        sys.exit(1)

def verify_installation():
    """Verify that libgdiplus is installed."""
    try:
        output = subprocess.run(
            ["ldconfig", "-p"], stdout=subprocess.PIPE, text=True, check=True, shell=True
        )
        if "libgdiplus" in output.stdout:
            print(f"{GREEN}libgdiplus is installed and available.{NC}")
        else:
            raise FileNotFoundError
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f"{RED}libgdiplus installation verification failed. Please check manually.{NC}")
        sys.exit(1)

def main():
    """Main function."""
    print(f"{GREEN}7days-APC: Checking prerequisites...{NC}")
    check_root()

    pkg_manager = detect_package_manager()
    if not pkg_manager:
        print(f"{RED}No supported package manager found.{NC}")
        print("Please install libgdiplus manually from: https://github.com/mono/libgdiplus")
        sys.exit(1)

    print(f"{GREEN}Detected package manager: {pkg_manager}{NC}")
    install_libgdiplus(pkg_manager)
    verify_installation()
    print(f"{GREEN}All checks completed successfully! You are ready to play Afterlife!{NC}")

if __name__ == "__main__":
    main()

#!/bin/bash

# 7days-APC: 7 Days Afterlife Prerequisite Checker
# Author: Nathaniel Cosford
# Version: v1.0.1
# License: GNU GPL v3
# Description: Checks and installs libgdiplus, with support for multiple Linux distros and package managers.

# Colors for output
GREEN="\033[0;32m"
RED="\033[0;31m"
NC="\033[0m" # No Color

# Check for root privileges
if [[ "$EUID" -ne 0 ]]; then
    echo -e "${RED}Please run this script as root.${NC}"
    exit 1
fi

# Determine package manager
detect_package_manager() {
    if command -v apt &>/dev/null; then
        PKG_MANAGER="apt"
    elif command -v yum &>/dev/null; then
        PKG_MANAGER="yum"
    elif command -v dnf &>/dev/null; then
        PKG_MANAGER="dnf"
    elif command -v pacman &>/dev/null; then
        PKG_MANAGER="pacman"
    else
        PKG_MANAGER="none"
    fi
}

# Install libgdiplus
install_libgdiplus() {
    case "$PKG_MANAGER" in
    apt)
        apt update && apt install -y libgdiplus
        ;;
    yum | dnf)
        $PKG_MANAGER install -y libgdiplus
        ;;
    pacman)
        pacman -Sy --noconfirm libgdiplus
        ;;
    none)
        echo -e "${RED}No supported package manager found.${NC}"
        echo -e "Please install libgdiplus manually from: https://github.com/mono/libgdiplus"
        exit 1
        ;;
    *)
        echo -e "${RED}Unsupported package manager: $PKG_MANAGER.${NC}"
        exit 1
        ;;
    esac
    echo -e "${GREEN}libgdiplus installed successfully!${NC}"
}

# Verify installation
verify_installation() {
    if ldconfig -p | grep -q libgdiplus; then
        echo -e "${GREEN}libgdiplus is installed and available.${NC}"
    else
        echo -e "${RED}libgdiplus installation failed. Please check the logs above.${NC}"
        exit 1
    fi
}

# Main function
main() {
    echo -e "${GREEN}7days-APC: Checking prerequisites...${NC}"
    detect_package_manager
    echo -e "${GREEN}Detected package manager: $PKG_MANAGER${NC}"
    install_libgdiplus
    verify_installation
    echo -e "${GREEN}All checks completed successfully! You are ready to play Afterlife!${NC}"
}

# Run the main function
main

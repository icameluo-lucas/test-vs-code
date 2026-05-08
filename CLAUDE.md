# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a simple static HTML project — a designer personal blog ([index.html](index.html)). No build system, no dependencies.

## Key Files

- [index.html](index.html) — Complete single-page blog (HTML + CSS + JS)
- [SPEC.md](SPEC.md) — Design specification document

## Running the Project

Open `index.html` directly in a browser. No build step required.

## Notes

- Google Fonts loaded via CDN (verify connectivity before major changes)
- CSS uses custom properties for theming (`--bg`, `--accent`, etc.)
- Scroll animations use Intersection Observer API

## Windows Environment Rules

This project runs on native Windows PowerShell, NOT WSL or Git Bash.

- Never use Git Bash paths like `/d/`, `/c/`, `/mnt/c/`, `/drives/`
- Always use native Windows paths like `D:\project\file`
- Always prefer PowerShell commands over bash commands
- Never assume a Linux shell environment
- Never use path concatenation between Unix and Windows formats
- For plugin installation, always prefer: local scope, project scope
- Never recommend user-scope plugin installs on Windows
- Avoid bash-specific tools unless explicitly requested
- Use backslashes for Windows filesystem paths
- Do not generate mixed paths like `/drives/d/project/C:/Users`
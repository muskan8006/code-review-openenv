# Code Review & Bug Detection Environment (OpenEnv)

## Overview

This project implements an OpenEnv-compatible environment that simulates real-world software engineering tasks such as bug detection, code optimization, and security analysis.

## Motivation

Code review is a critical activity in software development. This environment evaluates an AI agent’s ability to:

* Identify syntax errors
* Suggest optimized code
* Detect security vulnerabilities

## Tasks

### 1. Bug Detection (Easy)

Identify syntax errors in code.

### 2. Code Optimization (Medium)

Suggest improvements for inefficient code.

### 3. Security Issue Detection (Hard)

Detect vulnerabilities like SQL Injection and suggest fixes.

## Observation Space

* task: string
* code: string
* history: list

## Action Space

* response: string

## Reward System

* Score between 0.0 and 1.0
* Incremental feedback provided
* Penalizes incorrect or unsafe responses

## Setup Instructions

```bash
pip install -r requirements.txt
python inference.py
```

## Docker Usage

```bash
docker build -t openenv .
docker run openenv
```

## Baseline Performance

* Bug Detection: 1.0
* Optimization: 1.0
* Security Detection: 1.0

## Author

OpenEnv Hackathon Submission

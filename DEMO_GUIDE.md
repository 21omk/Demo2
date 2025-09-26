# Demo Workflow Usage Guide

## Overview
This repository contains a GitHub Actions workflow designed to fail in multiple ways, generating various types of error logs that can be used for demonstration purposes with GitHub Copilot.

## How to Use This Demo

### 1. Trigger the Workflow
The workflow can be triggered in several ways:

**Automatic Triggers:**
- Push changes to `main` or `develop` branches
- Create a pull request targeting `main` branch

**Manual Trigger:**
- Go to the "Actions" tab in the GitHub repository
- Select "Demo Failing Workflow"
- Click "Run workflow"
- Choose the branch and click "Run workflow"

### 2. Wait for Failures
All jobs in the workflow are designed to fail. You should expect:
- ❌ Job with Syntax Errors
- ❌ Missing Dependencies Job  
- ❌ Build Failure Job
- ❌ Test Failure Job
- ❌ Linting Failure Job
- ❌ Security Scan Failure
- ❌ Docker Build Failure
- ❌ Environment Mismatch Job

### 3. Collect Failure Logs
Once the workflow fails:
1. Go to the Actions tab
2. Click on the failed workflow run
3. Click on each failed job to see detailed logs
4. Copy the error messages and logs

### 4. Use with GitHub Copilot
The failure logs can be used to:
- Create GitHub issues automatically using Copilot
- Demonstrate error analysis capabilities
- Show different types of CI/CD failure patterns
- Practice troubleshooting with AI assistance

## Types of Errors Generated

| Job Name | Error Types | Common Log Patterns |
|----------|-------------|-------------------|
| Syntax Error | Python syntax, Bash syntax | `SyntaxError:`, `unexpected token` |
| Dependencies | Missing packages | `ERROR: No matching distribution found` |
| Build | Compilation, Missing scripts | `gcc: error:`, `npm ERR!` |
| Tests | Assertion failures, Type errors | `FAILED`, `AssertionError:` |
| Linting | Code style, Formatting | `E501 line too long`, `would reformat` |
| Security | Vulnerabilities, Hardcoded secrets | `HIGH severity`, `Hardcoded password` |
| Docker | Dockerfile syntax | `unknown instruction:`, `COPY failed` |
| Environment | Platform incompatibility | `command not found` |

## Local Testing
Run the included test script to verify failure scenarios locally:
```bash
./test_failures_locally.sh
```

## Sample Copilot Prompts
When using the logs with GitHub Copilot, try prompts like:
- "Create a GitHub issue based on this CI/CD failure log: [paste log]"
- "Analyze this test failure and suggest a fix: [paste log]"
- "What is causing this build error and how can I resolve it: [paste log]"

## Important Notes
- **All failures are intentional** - This is not a broken project
- The repository is for **demonstration purposes only**
- Do not attempt to "fix" the issues unless you want to change the demo behavior
- The workflow will consume GitHub Actions minutes when run
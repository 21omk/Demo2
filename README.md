# Demo2 - Failing GitHub Actions Workflow

This repository contains a GitHub Actions workflow that is intentionally designed to fail for demonstration purposes. The workflow generates various types of failure logs that can be used with GitHub Copilot to create issues and demonstrate error analysis.

## Purpose

This demo repository is designed to:
- Generate realistic failure logs from GitHub Actions
- Demonstrate different types of common CI/CD failures
- Provide examples for GitHub Copilot issue creation from failure logs
- Show various error patterns that developers encounter

## Types of Failures Included

The workflow includes the following types of intentional failures:

### 1. Syntax Error Job
- **Purpose**: Demonstrates syntax errors in scripts and code
- **Includes**: 
  - Bash script syntax errors (missing brackets, etc.)
  - Python syntax errors (missing colons, incorrect indentation)

### 2. Dependency Error Job
- **Purpose**: Shows missing package/dependency failures
- **Includes**:
  - Python packages that don't exist
  - Node.js packages that don't exist
  - Package installation failures

### 3. Build Failure Job
- **Purpose**: Demonstrates build process failures
- **Includes**:
  - Missing package.json scripts
  - C compilation errors
  - Missing build tools

### 4. Test Failure Job
- **Purpose**: Shows various test failures
- **Includes**:
  - Assertion failures
  - Type errors in tests
  - Mathematical assertion errors
  - String comparison failures

### 5. Linting Failure Job
- **Purpose**: Demonstrates code quality and formatting issues
- **Includes**:
  - flake8 linting errors
  - black formatting errors
  - isort import sorting errors
  - ESLint JavaScript linting errors

### 6. Security Scan Failure
- **Purpose**: Shows security vulnerability detection
- **Includes**:
  - Hardcoded passwords and API keys
  - Shell injection vulnerabilities
  - Unsafe eval usage
  - Known vulnerable package versions

### 7. Docker Build Failure
- **Purpose**: Demonstrates Docker-related failures
- **Includes**:
  - Invalid Dockerfile syntax
  - Non-existent base images
  - Wrong instruction formats

### 8. Environment Mismatch Job
- **Purpose**: Shows environment compatibility issues
- **Includes**:
  - Running Windows commands on Linux
  - Trying to install non-existent software versions

## Usage for Demo

1. **Trigger the Workflow**: Push changes or manually trigger the workflow
2. **Wait for Failures**: All jobs are designed to fail with different error types
3. **Collect Logs**: Use the failure logs to demonstrate Copilot's issue creation capabilities
4. **Analyze Patterns**: Show how different failure types generate different log patterns

## Files Included

- `.github/workflows/failing-demo.yml`: Main workflow file with all failure jobs
- `package.json`: Node.js configuration with missing dependencies
- `requirements.txt`: Python requirements with vulnerable packages
- `app.py`: Python application with various intentional errors
- `index.js`: JavaScript file with syntax and logic errors
- `test_failures.py`: Test file with multiple failing test cases
- `Dockerfile`: Docker configuration with multiple syntax errors
- `.eslintrc.json`: Strict ESLint configuration
- `jest.config.js`: Jest configuration with impossible coverage requirements

## Triggering the Workflow

The workflow can be triggered by:
- Pushing to `main` or `develop` branches
- Creating pull requests to `main`
- Manual workflow dispatch from GitHub UI

## Expected Behavior

**ALL JOBS WILL FAIL** - This is intentional and expected. The repository is designed to generate failure logs for demonstration purposes only.
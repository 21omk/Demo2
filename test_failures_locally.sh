#!/bin/bash
# Demo script to manually trigger some of the failure scenarios locally

echo "=== Demo Failure Testing Script ==="
echo "This script demonstrates the types of failures included in the GitHub Actions workflow"
echo ""

echo "1. Testing Python syntax error..."
python3 -c "
def broken_function()
    print('Missing colon in function definition')
" 2>/dev/null || echo "✓ Python syntax error confirmed"

echo ""
echo "2. Testing missing Python package..."
pip install nonexistent-package-xyz123 2>/dev/null || echo "✓ Missing package error confirmed"

echo ""
echo "3. Testing Python import error..."
python3 -c "import nonexistent_module" 2>/dev/null || echo "✓ Import error confirmed"

echo ""
echo "4. Testing bash syntax error..."
bash -c 'if [ "test" = "test" 
  echo "Missing closing bracket"
fi' 2>/dev/null || echo "✓ Bash syntax error confirmed"

echo ""
echo "5. Testing file not found error..."
cat nonexistent_file.txt 2>/dev/null || echo "✓ File not found error confirmed"

echo ""
echo "6. Testing compilation error..."
echo '#include <stdio.h>
int main() {
    printf("Hello World"
    return 0;
}' > /tmp/broken.c
gcc -o /tmp/broken /tmp/broken.c 2>/dev/null || echo "✓ C compilation error confirmed"
rm -f /tmp/broken.c /tmp/broken

echo ""
echo "7. Testing Windows command on Linux..."
powershell.exe -Command "Get-ChildItem" 2>/dev/null || echo "✓ Windows command error confirmed"

echo ""
echo "=== All failure types confirmed! ==="
echo "The GitHub Actions workflow will generate detailed logs for each of these error types."
echo "These logs can then be used with GitHub Copilot to automatically create issues."
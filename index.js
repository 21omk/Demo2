// This file contains intentional JavaScript errors for demo purposes

const express = require('express'); // This package isn't installed
const missingPackage = require('some-nonexistent-package');

// Syntax error: missing closing brace
function brokenFunction() {
    console.log('This function has syntax errors');
    if (true) {
        return 'missing closing brace'
    // Missing closing brace for if statement

// Another syntax error: undefined variable
function anotherBrokenFunction() {
    console.log(undefinedVariable); // This variable doesn't exist
    return someOtherUndefinedVar;
}

// Logic error that will cause runtime failure
function divideByZero(a, b) {
    if (b = 0) { // Should be == or ===, not =
        return a / b; // Division by zero
    }
    return a / b;
}

// Missing semicolons and improper syntax
const app = express()
app.get('/', (req, res) => {
    res.send('Hello World')
}) // Missing semicolon

// Calling undefined function
undefinedFunction();

// Export syntax error
modules.exports = { // Should be module.exports
    brokenFunction,
    anotherBrokenFunction,
    divideByZero
}
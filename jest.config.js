module.exports = {
  preset: 'jest',
  testEnvironment: 'node',
  testMatch: [
    '**/test*.js',
    '**/*.test.js',
    '**/test_*.py',
    '**/*_test.py'
  ],
  collectCoverageFrom: [
    'src/**/*.{js,ts}',
    '!src/**/*.d.ts'
  ],
  coverageThreshold: {
    global: {
      branches: 100,  // Impossible to achieve, will fail
      functions: 100, // Impossible to achieve, will fail
      lines: 100,     // Impossible to achieve, will fail
      statements: 100 // Impossible to achieve, will fail
    }
  }
};
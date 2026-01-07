# Code Quality Metrics

## Code Complexity Metrics

### Cyclomatic Complexity
Measures the number of linearly independent paths through code.

**Calculation:**
- Base complexity: 1
- +1 for each decision point (if, while, for, case)
- +1 for each exception handler

**Good practices:**
- Keep functions under complexity 10
- Use tools like ESLint complexity rule
- Break complex functions into smaller ones

```javascript
// High complexity (score: 6)
function calculateGrade(score, isBonus, isRetake, hasExcuse) {
    if (score >= 90) {
        if (isBonus) return 'A+';
        return 'A';
    } else if (score >= 80) {
        if (isRetake) return 'B-';
        return 'B';
    } else if (score >= 70) {
        if (hasExcuse) return 'C';
        return 'D';
    }
    return 'F';
}

// Lower complexity (score: 2)
function getGrade(score) {
    if (score >= 90) return 'A';
    if (score >= 80) return 'B';
    if (score >= 70) return 'C';
    return 'D';
}
```

### Maintainability Index
Composite metric combining:
- Cyclomatic complexity
- Lines of code
- Halstead volume

**Formula:**
```
MI = 171 - 5.2 * ln(Halstead Volume) - 0.23 * (Cyclomatic Complexity) - 16.2 * ln(Lines of Code)
```

**Interpretation:**
- 100: Very high maintainability
- 85-99: High maintainability
- 65-84: Moderate maintainability
- 0-64: Low maintainability

## Code Coverage Metrics

### Line Coverage
Percentage of lines executed during testing.

```javascript
// 75% line coverage (3/4 lines covered)
function calculateTotal(items) {
    let total = 0;                    // ✓ Covered
    for (let item of items) {         // ✓ Covered
        total += item.price;          // ✓ Covered
    }
    return total;                     // ✗ Not covered in tests
}
```

### Branch Coverage
Percentage of decision branches tested.

```javascript
// 50% branch coverage (1/2 branches covered)
function checkAccess(user) {
    if (user.role === 'admin') {      // ✓ Covered
        return true;
    } else {                          // ✗ Not covered
        return false;
    }
}
```

### Function Coverage
Percentage of functions called during testing.

## Code Style and Formatting

### ESLint Rules for Quality
```javascript
// .eslintrc.js
module.exports = {
    rules: {
        // Complexity rules
        'complexity': ['error', 10],
        'max-depth': ['error', 4],
        'max-lines': ['error', 300],
        'max-lines-per-function': ['error', 50],

        // Style rules
        'indent': ['error', 4],
        'quotes': ['error', 'single'],
        'semi': ['error', 'always'],

        // Best practices
        'no-unused-vars': 'error',
        'no-unreachable': 'error',
        'prefer-const': 'error'
    }
};
```

### Formatting Standards
```javascript
// Good: Consistent formatting
class UserService {
    constructor(database) {
        this.db = database;
    }

    async getUser(id) {
        if (!id) {
            throw new Error('User ID is required');
        }

        const user = await this.db.users.findById(id);
        return user;
    }
}

// Bad: Inconsistent formatting
class UserService{
constructor(database){
this.db=database;
}
async getUser(id){
if(!id)throw new Error('User ID is required');
const user=await this.db.users.findById(id);
return user;
}
}
```

## Documentation Quality

### JSDoc Standards
```javascript
/**
 * Calculates the total price including tax
 * @param {number[]} items - Array of item prices
 * @param {number} taxRate - Tax rate as decimal (0.08 for 8%)
 * @returns {number} Total price with tax
 * @throws {Error} When taxRate is invalid
 */
function calculateTotalWithTax(items, taxRate) {
    if (taxRate < 0 || taxRate > 1) {
        throw new Error('Invalid tax rate');
    }

    const subtotal = items.reduce((sum, price) => sum + price, 0);
    return subtotal * (1 + taxRate);
}
```

### Documentation Coverage
- All public APIs should have documentation
- Complex algorithms need explanations
- Configuration options require descriptions
- Error conditions should be documented

## Performance Metrics

### Bundle Size Analysis
```javascript
// webpack.config.js
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');

module.exports = {
    plugins: [
        new BundleAnalyzerPlugin({
            analyzerMode: 'static',
            openAnalyzer: false
        })
    ]
};
```

### Performance Budgets
```javascript
// package.json
{
    "performance": {
        "bundleSize": {
            "max": "500kb",
            "gzip": "150kb"
        },
        "loadTime": {
            "max": "3s"
        }
    }
}
```

## Security Metrics

### Vulnerability Scanning
```bash
# npm audit for dependency vulnerabilities
npm audit

# Snyk for comprehensive security scanning
snyk test

# ESLint security plugin
npm install eslint-plugin-security
```

### Code Security Patterns
```javascript
// Secure: Input validation
function sanitizeInput(input) {
    if (typeof input !== 'string') {
        throw new Error('Input must be a string');
    }

    return input.replace(/[<>\"'&]/g, '');
}

// Secure: SQL injection prevention
function getUserById(db, userId) {
    const query = 'SELECT * FROM users WHERE id = ?';
    return db.query(query, [userId]);
}
```

## Maintainability Metrics

### Technical Debt Ratio
Measures the cost of fixing code issues vs. cost of rewriting.

**Calculation:**
```
Technical Debt Ratio = (Remediation Cost / Development Cost) * 100
```

**Components:**
- Code duplication
- Code complexity
- Insufficient testing
- Architecture violations

### Code Duplication
```javascript
// Bad: Duplicated code
function calculateAreaCircle(radius) {
    return Math.PI * radius * radius;
}

function calculateCircumferenceCircle(radius) {
    return 2 * Math.PI * radius;
}

// Good: Shared constants
const PI = Math.PI;

function calculateAreaCircle(radius) {
    return PI * radius * radius;
}

function calculateCircumferenceCircle(radius) {
    return 2 * PI * radius;
}
```

## Automated Quality Tools

### CI/CD Integration
```yaml
# .github/workflows/quality.yml
name: Code Quality
on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run ESLint
        run: npm run lint
      - name: Run Tests
        run: npm test
      - name: Check Coverage
        run: npm run test:coverage
      - name: Security Audit
        run: npm audit
```

### Quality Gates
```javascript
// package.json scripts
{
    "scripts": {
        "lint": "eslint src/",
        "test": "jest",
        "test:coverage": "jest --coverage",
        "quality:check": "npm run lint && npm run test && npm run test:coverage"
    }
}
```

## Metrics Collection and Reporting

### Automated Reporting
```javascript
// SonarQube configuration
// sonar-project.properties
sonar.projectKey=my-project
sonar.sources=src
sonar.tests=test
sonar.coverage.exclusions=**/*.spec.js
sonar.javascript.lcov.reportPaths=coverage/lcov.info
```

### Dashboard Integration
- SonarQube for comprehensive metrics
- CodeClimate for maintainability
- Coveralls for coverage tracking
- Custom dashboards with Grafana

## Quality Improvement Strategies

### Regular Refactoring
- Schedule monthly refactoring sessions
- Address technical debt incrementally
- Use pair programming for knowledge sharing
- Implement code review checklists

### Training and Standards
- Establish team coding standards
- Provide training on best practices
- Share knowledge through code reviews
- Document architectural decisions

### Tool Integration
- IDE plugins for real-time feedback
- Pre-commit hooks for quality checks
- Automated quality gates in CI/CD
- Regular quality metric reviews
---
name: code-minimizer
description: Analyze code and reduce its size without breaking functionality. Removes unused code, simplifies logic, shortens functions, and improves readability and performance. Useful for production builds and clean repositories.
---

# Code Minimizer (Optimizer)

This skill analyzes code and reduces its size while maintaining functionality, improving readability and performance.

## What This Skill Does

1. **Remove unused variables/functions** - Eliminate dead code that serves no purpose
2. **Simplify logic** - Reduce complex conditional statements and loops
3. **Reduce file size** - Minimize code without breaking functionality
4. **Keep code working and readable** - Maintain code quality while reducing size

## When to Use This Skill

Use this skill when you need to:
- Optimize code for production builds
- Reduce repository size by removing dead code
- Improve code readability and maintainability
- Prepare code for deployment or release
- Clean up legacy or inherited codebases

## Code Minimization Process

### 1. Analysis Phase
- **Dead Code Detection**: Identify unused variables, functions, and imports
- **Complexity Analysis**: Find overly complex logic that can be simplified
- **Redundancy Check**: Locate duplicate code patterns
- **Size Assessment**: Measure current file sizes and identify optimization opportunities

### 2. Optimization Phase
- **Remove Dead Code**: Eliminate unused variables, functions, and imports
- **Simplify Logic**: Reduce complex conditional statements and loops
- **Consolidate Functions**: Merge similar functions or extract common patterns
- **Optimize Data Structures**: Use more efficient data structures where possible
- **Reduce Dependencies**: Remove unnecessary imports and external dependencies

### 3. Verification Phase
- **Functionality Testing**: Ensure all features still work correctly
- **Performance Testing**: Verify that optimizations don't hurt performance
- **Readability Review**: Ensure code remains readable and maintainable
- **Size Measurement**: Confirm reduction in file size

## Optimization Categories

### Dead Code Removal
- **Unused Variables**: Variables declared but never used
- **Unused Functions**: Functions defined but never called
- **Unused Imports**: Import statements for unused modules or functions
- **Unreachable Code**: Code after return statements or in never-executed branches

### Logic Simplification
- **Complex Conditionals**: Simplify nested if statements
- **Redundant Checks**: Remove duplicate conditional logic
- **Loop Optimization**: Simplify loop structures and reduce iterations
- **Boolean Logic**: Simplify complex boolean expressions

### Code Consolidation
- **Duplicate Functions**: Merge similar functions
- **Common Patterns**: Extract repeated code into reusable functions
- **Magic Numbers**: Replace with named constants
- **String Concatenation**: Optimize string operations

### Performance Optimizations
- **Algorithm Efficiency**: Use more efficient algorithms
- **Memory Usage**: Reduce memory footprint
- **I/O Operations**: Minimize file and network operations
- **Caching**: Add appropriate caching for expensive operations

## Tools and Scripts

### analyze-code.py
Python script for comprehensive code analysis and dead code detection.

Usage:
```bash
python scripts/analyze-code.py file.js --language js --output report.json
```

Features:
- Dead code detection
- Complexity analysis
- Dependency mapping
- Size optimization suggestions

### minimize.py
Script for automated code minimization with safety checks.

Usage:
```bash
python scripts/minimize.py input.js --output optimized.js --backup
```

Options:
- `--backup`: Create backup of original files
- `--verify`: Run verification tests after minimization
- `--aggressive`: Apply more aggressive optimization rules

### js-minimizer.py
JavaScript-specific minimizer with syntax tree analysis.

Usage:
```bash
python scripts/js-minimizer.py script.js --remove-comments --minify-vars
```

Features:
- Variable name shortening
- Comment removal
- Whitespace optimization
- String literal optimization

## Optimization Guidelines

### Safety First
- **Always backup original code** before making changes
- **Run tests** after each optimization step
- **Version control** changes incrementally
- **Verify functionality** before and after optimization

### Gradual Approach
- **Start with analysis** to understand codebase
- **Apply optimizations incrementally**
- **Test after each change**
- **Roll back if issues occur**

### Maintain Quality
- **Preserve code readability** where possible
- **Keep meaningful variable names** for critical code
- **Maintain proper documentation**
- **Don't sacrifice maintainability** for minimal size gains

### Measure Results
- **Track file size reduction**
- **Monitor performance improvements**
- **Verify functionality preservation**
- **Document optimization decisions**

## Examples

### Example 1: Dead Code Removal
**Before:**
```javascript
function calculateTotal(items) {
    let sum = 0;
    let count = 0; // unused variable
    let temp = 0;  // unused variable

    for (let i = 0; i < items.length; i++) {
        sum += items[i].price;
    }

    return sum;
}

function unusedFunction() {
    console.log("This is never called");
}
```

**After:**
```javascript
function calculateTotal(items) {
    let sum = 0;

    for (let i = 0; i < items.length; i++) {
        sum += items[i].price;
    }

    return sum;
}
```

### Example 2: Logic Simplification
**Before:**
```javascript
function checkAccess(user, resource) {
    if (user.role === 'admin') {
        return true;
    } else {
        if (user.permissions.includes(resource)) {
            return true;
        } else {
            return false;
        }
    }
}
```

**After:**
```javascript
function checkAccess(user, resource) {
    return user.role === 'admin' || user.permissions.includes(resource);
}
```

### Example 3: Function Consolidation
**Before:**
```javascript
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function validatePhone(phone) {
    const phoneRegex = /^\d{10}$/;
    return phoneRegex.test(phone);
}
```

**After:**
```javascript
function validatePattern(input, pattern) {
    return pattern.test(input);
}

const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const phoneRegex = /^\d{10}$/;

function validateEmail(email) {
    return validatePattern(email, emailRegex);
}

function validatePhone(phone) {
    return validatePattern(phone, phoneRegex);
}
```

## References

- [Code Optimization Best Practices](references/optimization-guidelines.md)
- [Dead Code Detection Techniques](references/dead-code-detection.md)
- [JavaScript Minification Patterns](references/js-optimization.md)
- [Performance Optimization Strategies](references/performance-optimization.md)
- [Code Quality Metrics](references/quality-metrics.md)

## Common Optimization Patterns

### 1. Remove Unused Imports
```javascript
// Before
import { useState, useEffect, useCallback } from 'react';
import { debounce } from 'lodash';

function MyComponent() {
    // Only uses useState
    const [value, setValue] = useState('');
    return <div>{value}</div>;
}

// After
import { useState } from 'react';

function MyComponent() {
    const [value, setValue] = useState('');
    return <div>{value}</div>;
}
```

### 2. Simplify Conditional Logic
```javascript
// Before
function getStatusColor(status) {
    if (status === 'active') {
        return 'green';
    } else if (status === 'inactive') {
        return 'red';
    } else {
        return 'gray';
    }
}

// After
function getStatusColor(status) {
    return status === 'active' ? 'green' :
           status === 'inactive' ? 'red' : 'gray';
}
```

### 3. Eliminate Redundant Code
```javascript
// Before
function processUser(user) {
    if (user.isActive) {
        if (user.hasPermission) {
            return processActiveUser(user);
        } else {
            return null;
        }
    } else {
        return null;
    }
}

// After
function processUser(user) {
    if (user.isActive && user.hasPermission) {
        return processActiveUser(user);
    }
    return null;
}
```

## Testing and Verification

### Automated Testing
- **Unit Tests**: Ensure all functions work correctly
- **Integration Tests**: Verify system components work together
- **Regression Tests**: Confirm no functionality is broken
- **Performance Tests**: Measure optimization impact

### Manual Verification
- **Code Review**: Manual inspection of changes
- **Functional Testing**: Test key user workflows
- **Edge Case Testing**: Verify boundary conditions
- **User Acceptance**: Confirm user requirements are met

### Rollback Procedures
- **Version Control**: Use git for easy rollback
- **Backup Files**: Keep original versions
- **Gradual Deployment**: Deploy changes incrementally
- **Monitoring**: Watch for issues in production
# JavaScript Minification Patterns

## Variable and Function Name Shortening

### Safe Shortening Patterns
```javascript
// Before
function calculateTotalPrice(items, taxRate) {
    let total = 0;
    for (let item of items) {
        total += item.price;
    }
    return total * (1 + taxRate);
}

// After (minified)
function a(b,c){let d=0;for(let e of b){d+=e.price}return d*(1+c)}
```

### Variable Name Mapping
```javascript
// Create a mapping system
const varMap = {
    'calculateTotalPrice': 'a',
    'items': 'b',
    'taxRate': 'c',
    'total': 'd',
    'item': 'e'
};

// Apply mapping throughout code
function applyMapping(code, map) {
    let result = code;
    for (const [longName, shortName] of Object.entries(map)) {
        const pattern = new RegExp(`\\b${longName}\\b`, 'g');
        result = result.replace(pattern, shortName);
    }
    return result;
}
```

## Comment and Whitespace Removal

### Comment Removal
```javascript
function removeComments(code) {
    // Remove single-line comments
    code = code.replace(/\/\/.*$/gm, '');

    // Remove multi-line comments
    code = code.replace(/\/\*[\s\S]*?\*\//g, '');

    return code;
}
```

### Whitespace Optimization
```javascript
function removeWhitespace(code) {
    // Remove extra spaces
    code = code.replace(/\s+/g, ' ');

    // Remove spaces around operators
    code = code.replace(/\s*([=+\-*/<>!&|])\s*/g, '$1');

    // Remove spaces after commas
    code = code.replace(/,\s*/g, ',');

    // Remove spaces around brackets
    code = code.replace(/\s*([{}[\]()])\s*/g, '$1');

    return code.trim();
}
```

## String Optimization

### Quote Unification
```javascript
function optimizeQuotes(code) {
    // Replace double quotes with single quotes where possible
    code = code.replace(/"([^"]*)"/g, function(match, content) {
        if (!content.includes("'")) {
            return `'${content}'`;
        }
        return match;
    });

    return code;
}
```

### String Concatenation
```javascript
// Before
const message = "Hello " + name + ", welcome to " + siteName + "!";

// After (if template literals are supported)
const message = `Hello ${name}, welcome to ${siteName}!`;
```

## Logic Simplification

### Boolean Simplification
```javascript
// Before
function isValid(value) {
    if (value !== null && value !== undefined && value !== '') {
        return true;
    } else {
        return false;
    }
}

// After
function isValid(value) {
    return value != null && value !== '';
}
```

### Ternary Operator Usage
```javascript
// Before
function getStatus(isActive) {
    if (isActive) {
        return 'active';
    } else {
        return 'inactive';
    }
}

// After
function getStatus(isActive) {
    return isActive ? 'active' : 'inactive';
}
```

### Conditional Simplification
```javascript
// Before
function checkAccess(user) {
    if (user.role === 'admin' || user.role === 'manager') {
        return true;
    } else {
        return false;
    }
}

// After
function checkAccess(user) {
    return user.role === 'admin' || user.role === 'manager';
}
```

## Function Optimization

### Arrow Function Conversion
```javascript
// Before
const add = function(a, b) {
    return a + b;
};

const processItems = function(items) {
    return items.map(function(item) {
        return item * 2;
    });
};

// After
const add = (a, b) => a + b;

const processItems = items => items.map(item => item * 2);
```

### IIFE (Immediately Invoked Function Expression)
```javascript
// Before
(function() {
    var x = 1;
    var y = 2;
    console.log(x + y);
})();

// After (minified)
!function(){var a=1,b=2;console.log(a+b)}();
```

## Object and Array Optimization

### Object Property Shorthand
```javascript
// Before
const config = {
    width: width,
    height: height,
    color: color,
    process: function() {
        return this.width * this.height;
    }
};

// After
const config = {
    width, height, color,
    process() {
        return this.width * this.height;
    }
};
```

### Array Methods
```javascript
// Before
const numbers = [1, 2, 3, 4, 5];
const doubled = [];
for (let i = 0; i < numbers.length; i++) {
    doubled.push(numbers[i] * 2);
}

// After
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);
```

## Import/Export Optimization

### Import Optimization
```javascript
// Before
import { useState, useEffect, useCallback, useMemo, useRef } from 'react';
import { debounce } from 'lodash';
import { formatDate } from './utils';

// After (only import what you use)
import { useState } from 'react';
import { debounce } from 'lodash';
```

### Module Bundling
```javascript
// Use tree-shaking compatible imports
// Before
import _ from 'lodash';
const result = _.map(items, item => item.value);

// After
import { map } from 'lodash';
const result = map(items, item => item.value);
```

## Advanced Optimization Techniques

### Dead Code Elimination
```javascript
// Before
function process(data) {
    const result = calculate(data);
    const debugInfo = {
        input: data,
        result: result,
        timestamp: Date.now()
    };

    if (DEBUG) {
        console.log(debugInfo);
    }

    return result;
}

// After (with DEBUG = false)
function process(data) {
    const result = calculate(data);
    return result;
}
```

### Loop Optimization
```javascript
// Before
for (let i = 0; i < array.length; i++) {
    processItem(array[i]);
}

// After
for (let i = array.length - 1; i >= 0; i--) {
    processItem(array[i]);
}
```

### Function Inlining
```javascript
// Before
function calculateTotal(price, tax) {
    return add(price, multiply(price, tax));
}

function add(a, b) {
    return a + b;
}

function multiply(a, b) {
    return a * b;
}

// After (inlined)
function calculateTotal(price, tax) {
    return price + price * tax;
}
```

## Minification Tools Integration

### Custom Minifier
```javascript
class JSMinifier {
    constructor(options = {}) {
        this.options = {
            removeComments: true,
            minifyVars: true,
            minifyWhitespace: true,
            shortenStrings: true,
            ...options
        };
    }

    minify(code) {
        let result = code;

        if (this.options.removeComments) {
            result = this.removeComments(result);
        }

        if (this.options.minifyWhitespace) {
            result = this.removeWhitespace(result);
        }

        if (this.options.minifyVars) {
            result = this.shortenVariables(result);
        }

        if (this.options.shortenStrings) {
            result = this.optimizeStrings(result);
        }

        return result;
    }
}
```

### Build Process Integration
```javascript
// Webpack configuration example
module.exports = {
    mode: 'production',
    optimization: {
        minimize: true,
        minimizer: [
            new TerserPlugin({
                terserOptions: {
                    compress: {
                        drop_console: true,
                        drop_debugger: true
                    },
                    mangle: true,
                    format: {
                        comments: false
                    }
                },
                extractComments: false
            })
        ]
    }
};
```

## Performance Considerations

### When NOT to Minify
- Development builds (for debugging)
- Code that needs to be readable
- Libraries that users might inspect
- Code with complex debugging requirements

### Size vs. Readability Trade-offs
- Balance between file size and maintainability
- Consider source maps for debugging
- Use appropriate levels of minification
- Test performance impact

### Browser Compatibility
- Ensure minified code works across target browsers
- Test with different JavaScript engines
- Consider polyfills for modern features
- Validate with multiple bundlers
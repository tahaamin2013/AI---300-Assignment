# Dead Code Detection Techniques

## What is Dead Code?

Dead code refers to code that is written but never executed or used. This includes:
- Unused variables and functions
- Unreachable code
- Unused imports
- Unused classes and methods
- Code after return statements
- Code in never-executed conditional branches

## Detection Methods

### Static Analysis
**AST (Abstract Syntax Tree) Analysis:**
- Parse code into AST structure
- Track all definitions and usages
- Identify unused declarations
- Detect unreachable code paths

**Control Flow Analysis:**
- Build control flow graph
- Identify unreachable blocks
- Detect dead branches in conditionals
- Find code after return/throw statements

**Data Flow Analysis:**
- Track variable definitions and uses
- Identify unused variables
- Detect variables that are never read
- Find assignments to unused variables

### Dynamic Analysis
**Runtime Monitoring:**
- Instrument code to track execution
- Log which functions are called
- Track variable access patterns
- Identify unused code paths

**Profiling Tools:**
- Use performance profilers
- Identify rarely executed code
- Find unused code sections
- Measure code coverage

## Detection Patterns

### Unused Variables
```javascript
// Detected as dead code
function example() {
    let unusedVar = 10;  // Never used
    let usedVar = 20;
    return usedVar;      // Only usedVar is actually used
}
```

### Unused Functions
```javascript
// Detected as dead code
function unusedFunction() {
    console.log("This is never called");
}

function usedFunction() {
    return "This is called";
}
```

### Unreachable Code
```javascript
// Detected as dead code
function example() {
    return "Exit here";
    console.log("This is never reached");  // Dead code
}
```

### Unused Imports
```javascript
// Detected as dead code
import { usedFunction, unusedFunction } from './module';

function example() {
    return usedFunction();  // unusedFunction is imported but never used
}
```

## Tools and Libraries

### JavaScript/TypeScript
**ESLint:**
- `no-unused-vars` rule
- `no-unreachable` rule
- `no-unused-labels` rule
- Custom plugin support

**TSLint (deprecated, use ESLint):**
- `no-unused-variable` rule
- `no-unreachable` rule

**Webpack Bundle Analyzer:**
- Visualize bundle content
- Identify unused modules
- Analyze dependency trees

### Python
**Vulture:**
- Fast dead code detection
- Works with Python 2.7 and 3.x
- Supports type annotations
- Configurable false positive handling

**Deadfish:**
- Detects unused code
- Works with Python projects
- Identifies dead imports and variables

**Pyflakes:**
- Basic dead code detection
- Fast execution
- Part of many IDE integrations

### Java
**PMD:**
- Dead code detection rules
- Unused variable detection
- Unused import detection
- Custom rule creation

**SonarQube:**
- Comprehensive code analysis
- Dead code detection
- Code quality metrics
- Integration with CI/CD

**IntelliJ IDEA:**
- Built-in dead code detection
- Unused import warnings
- Unused method detection
- Refactoring suggestions

### C#
**ReSharper:**
- Dead code detection
- Unused member identification
- Unused import removal
- Code cleanup tools

**Roslyn Analyzers:**
- Compiler-based analysis
- Custom analyzer creation
- IDE integration
- Performance optimization

## Automated Detection Scripts

### Python Dead Code Detector
```python
import ast
import os

class DeadCodeDetector(ast.NodeVisitor):
    def __init__(self):
        self.definitions = {}
        self.usages = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.usages.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.definitions[node.id] = node
        self.generic_visit(node)

    def detect_dead_code(self):
        dead = []
        for name, node in self.definitions.items():
            if name not in self.usages:
                dead.append((name, node.lineno))
        return dead

def analyze_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    tree = ast.parse(content)
    detector = DeadCodeDetector()
    detector.visit(tree)
    return detector.detect_dead_code()
```

### JavaScript Dead Code Detector
```javascript
const acorn = require('acorn');

function detectDeadCode(code) {
    const ast = acorn.parse(code, { ecmaVersion: 2020 });
    const definitions = new Set();
    const usages = new Set();

    function visit(node) {
        switch (node.type) {
            case 'FunctionDeclaration':
                if (node.id) definitions.add(node.id.name);
                break;
            case 'VariableDeclaration':
                node.declarations.forEach(dec => {
                    if (dec.id.type === 'Identifier') {
                        definitions.add(dec.id.name);
                    }
                });
                break;
            case 'Identifier':
                usages.add(node.name);
                break;
        }

        for (const key in node) {
            const child = node[key];
            if (Array.isArray(child)) {
                child.forEach(visit);
            } else if (child && typeof child === 'object' && child.type) {
                visit(child);
            }
        }
    }

    visit(ast);

    const dead = [];
    definitions.forEach(def => {
        if (!usages.has(def)) {
            dead.push(def);
        }
    });

    return dead;
}
```

## Prevention Strategies

### Code Review Practices
- Review for unused code during pull requests
- Use automated tools in CI/CD pipeline
- Establish coding standards
- Regular code cleanup sessions

### Development Tools
- IDE warnings for unused code
- Linting rules for dead code detection
- Pre-commit hooks for code analysis
- Automated refactoring tools

### Documentation
- Document code purpose and usage
- Maintain up-to-date API documentation
- Track code ownership
- Document deprecation plans

## Best Practices

### Regular Maintenance
- Schedule regular dead code removal
- Use automated tools for detection
- Include dead code removal in refactoring
- Monitor code metrics over time

### Team Guidelines
- Establish team standards for code quality
- Use consistent naming conventions
- Document code purpose and usage
- Regular code review practices

### Tool Integration
- Integrate detection tools in development workflow
- Use automated cleanup in build process
- Monitor code metrics in dashboards
- Set up alerts for code quality issues
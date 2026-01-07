#!/usr/bin/env python3
"""
Code Analysis Tool for Dead Code Detection and Optimization Opportunities.

This script analyzes code files to identify:
- Dead code (unused variables, functions, imports)
- Complexity issues
- Optimization opportunities
- Size reduction potential
"""

import ast
import sys
import os
import json
import argparse
from typing import Dict, List, Set, Tuple, Any
from collections import defaultdict

class CodeAnalyzer:
    """Analyze code for optimization opportunities."""

    def __init__(self, language: str = 'python'):
        self.language = language
        self.issues = []
        self.stats = {
            'total_lines': 0,
            'code_lines': 0,
            'comment_lines': 0,
            'blank_lines': 0,
            'functions': 0,
            'classes': 0,
            'imports': 0
        }
        self.usage_map = defaultdict(int)
        self.definition_map = {}

    def analyze_file(self, file_path: str) -> Dict[str, Any]:
        """Analyze a single file for optimization opportunities."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return {'error': f"Cannot read file: {e}"}

        self.stats['total_lines'] = len(content.splitlines())

        # Count different types of lines
        for line in content.splitlines():
            line = line.strip()
            if not line:
                self.stats['blank_lines'] += 1
            elif line.startswith('#') or line.startswith('//') or line.startswith('/*'):
                self.stats['comment_lines'] += 1
            else:
                self.stats['code_lines'] += 1

        if self.language == 'python':
            return self._analyze_python(content, file_path)
        else:
            return self._analyze_generic(content, file_path)

    def _analyze_python(self, content: str, file_path: str) -> Dict[str, Any]:
        """Analyze Python code for optimization opportunities."""
        try:
            tree = ast.parse(content)
        except SyntaxError as e:
            return {'error': f"Syntax error: {e}"}

        # Track usage and definitions
        self._parse_definitions(tree)
        self._track_usage(tree)

        # Find issues
        issues = []

        # Check for unused imports
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if self.usage_map[alias.name] == 0:
                        issues.append({
                            'type': 'unused_import',
                            'line': node.lineno,
                            'description': f"Unused import: {alias.name}",
                            'severity': 'medium'
                        })

            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    if self.usage_map[alias.name] == 0:
                        issues.append({
                            'type': 'unused_import',
                            'line': node.lineno,
                            'description': f"Unused import: {alias.name}",
                            'severity': 'medium'
                        })

        # Check for unused variables and functions
        for name, usage_count in self.usage_map.items():
            if usage_count == 0 and name in self.definition_map:
                definition = self.definition_map[name]
                if isinstance(definition['node'], ast.FunctionDef):
                    issues.append({
                        'type': 'unused_function',
                        'line': definition['line'],
                        'description': f"Unused function: {name}",
                        'severity': 'high'
                    })
                elif isinstance(definition['node'], ast.Name) and isinstance(definition['node'].ctx, ast.Store):
                    issues.append({
                        'type': 'unused_variable',
                        'line': definition['line'],
                        'description': f"Unused variable: {name}",
                        'severity': 'medium'
                    })

        return {
            'file': file_path,
            'stats': self.stats,
            'issues': issues,
            'optimization_potential': self._calculate_optimization_potential(issues)
        }

    def _parse_definitions(self, tree: ast.AST):
        """Parse code to find all definitions."""
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                self.definition_map[node.name] = {
                    'node': node,
                    'line': node.lineno,
                    'type': 'function'
                }
                self.stats['functions'] += 1
            elif isinstance(node, ast.ClassDef):
                self.definition_map[node.name] = {
                    'node': node,
                    'line': node.lineno,
                    'type': 'class'
                }
                self.stats['classes'] += 1
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    self.definition_map[alias.name] = {
                        'node': node,
                        'line': node.lineno,
                        'type': 'import'
                    }
                    self.stats['imports'] += 1
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    self.definition_map[alias.name] = {
                        'node': node,
                        'line': node.lineno,
                        'type': 'import'
                    }
                    self.stats['imports'] += 1

    def _track_usage(self, tree: ast.AST):
        """Track usage of all defined names."""
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                if isinstance(node.ctx, ast.Load):
                    self.usage_map[node.id] += 1
            elif isinstance(node, ast.Attribute):
                # Track attribute usage
                if isinstance(node.value, ast.Name):
                    attr_name = f"{node.value.id}.{node.attr}"
                    self.usage_map[attr_name] += 1

    def _analyze_generic(self, content: str, file_path: str) -> Dict[str, Any]:
        """Generic analysis for non-Python files."""
        issues = []

        # Simple pattern-based analysis
        lines = content.splitlines()

        # Check for obvious dead code patterns
        for i, line in enumerate(lines, 1):
            line_stripped = line.strip()

            # Check for unreachable code (after return/break)
            if any(keyword in line_stripped for keyword in ['return', 'break', 'continue']):
                # Look for code after this line in the same block
                for j in range(i, min(i + 10, len(lines))):
                    next_line = lines[j].strip() if j < len(lines) else ""
                    if next_line and not next_line.startswith('//') and not next_line.startswith('/*'):
                        if not any(keyword in next_line for keyword in ['}', 'else', 'catch']):
                            issues.append({
                                'type': 'unreachable_code',
                                'line': j + 1,
                                'description': f"Potentially unreachable code: {next_line[:50]}",
                                'severity': 'medium'
                            })
                            break

        return {
            'file': file_path,
            'stats': self.stats,
            'issues': issues,
            'optimization_potential': self._calculate_optimization_potential(issues)
        }

    def _calculate_optimization_potential(self, issues: List[Dict]) -> Dict[str, float]:
        """Calculate potential optimization metrics."""
        total_issues = len(issues)
        high_severity = len([i for i in issues if i['severity'] == 'high'])
        medium_severity = len([i for i in issues if i['severity'] == 'medium'])
        low_severity = len([i for i in issues if i['severity'] == 'low'])

        # Estimate size reduction potential
        estimated_reduction = 0
        for issue in issues:
            if issue['type'] in ['unused_function', 'unused_variable']:
                estimated_reduction += 5  # Estimate 5 lines per unused item
            elif issue['type'] == 'unused_import':
                estimated_reduction += 1
            elif issue['type'] == 'unreachable_code':
                estimated_reduction += 3

        return {
            'total_issues': total_issues,
            'high_priority': high_severity,
            'medium_priority': medium_severity,
            'low_priority': low_severity,
            'estimated_lines_reducible': estimated_reduction,
            'estimated_size_reduction_percent': min(estimated_reduction / max(self.stats['code_lines'], 1) * 100, 50)
        }

def analyze_directory(directory: str, language: str = 'python') -> Dict[str, Any]:
    """Analyze all files in a directory."""
    analyzer = CodeAnalyzer(language)
    results = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            if language == 'python' and file.endswith('.py'):
                file_path = os.path.join(root, file)
                results[file_path] = analyzer.analyze_file(file_path)
            elif language in ['js', 'javascript'] and file.endswith('.js'):
                file_path = os.path.join(root, file)
                results[file_path] = analyzer.analyze_file(file_path)
            elif language == 'generic' and file.endswith(('.py', '.js', '.java', '.c', '.cpp', '.cs')):
                file_path = os.path.join(root, file)
                results[file_path] = analyzer.analyze_file(file_path)

    return results

def main():
    parser = argparse.ArgumentParser(description='Analyze code for optimization opportunities')
    parser.add_argument('path', help='File or directory to analyze')
    parser.add_argument('--language', '-l', choices=['python', 'js', 'javascript', 'generic'],
                       default='python', help='Programming language')
    parser.add_argument('--output', '-o', help='Output file for JSON report')
    parser.add_argument('--format', '-f', choices=['json', 'text'], default='text',
                       help='Output format')

    args = parser.parse_args()

    if os.path.isfile(args.path):
        analyzer = CodeAnalyzer(args.language)
        result = analyzer.analyze_file(args.path)
        results = {args.path: result}
    elif os.path.isdir(args.path):
        results = analyze_directory(args.path, args.language)
    else:
        print(f"Error: Path '{args.path}' not found", file=sys.stderr)
        sys.exit(1)

    if args.format == 'json':
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"Analysis results saved to {args.output}")
        else:
            print(json.dumps(results, indent=2))
    else:
        print_summary(results)

def print_summary(results: Dict[str, Any]):
    """Print a human-readable summary of analysis results."""
    total_issues = 0
    total_potential = 0

    print("=== CODE ANALYSIS SUMMARY ===")
    print()

    for file_path, result in results.items():
        if 'error' in result:
            print(f"❌ {file_path}: {result['error']}")
            continue

        issues = result['issues']
        stats = result['stats']
        potential = result['optimization_potential']

        total_issues += len(issues)
        total_potential += potential['estimated_lines_reducible']

        print(f"📁 {file_path}")
        print(f"   Lines: {stats['total_lines']} total, {stats['code_lines']} code, {stats['comment_lines']} comments")
        print(f"   Functions: {stats['functions']}, Classes: {stats['classes']}, Imports: {stats['imports']}")
        print(f"   Issues: {len(issues)} (high: {potential['high_priority']}, medium: {potential['medium_priority']})")
        print(f"   Optimization potential: {potential['estimated_lines_reducible']} lines ({potential['estimated_size_reduction_percent']:.1f}% reduction)")
        print()

    print(f"📊 TOTAL: {total_issues} issues found, {total_potential} lines potentially reducible")

if __name__ == '__main__':
    main()
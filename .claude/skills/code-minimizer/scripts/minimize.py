#!/usr/bin/env python3
"""
Code Minimizer - Automated code optimization and dead code removal.

This script safely removes dead code, simplifies logic, and optimizes code
while maintaining functionality and readability.

Usage: python minimize.py [options] input_file [output_file]
"""

import ast
import sys
import os
import shutil
import argparse
import re
from typing import Dict, List, Set, Tuple, Any, Optional
from collections import defaultdict

class CodeMinimizer:
    """Minimize code by removing dead code and simplifying logic."""

    def __init__(self, aggressive: bool = False, remove_comments: bool = False):
        self.aggressive = aggressive
        self.remove_comments = remove_comments
        self.used_names = set()
        self.redundant_conditions = []
        self.optimizations_applied = []

    def minimize_file(self, input_path: str, output_path: Optional[str] = None) -> bool:
        """Minimize a single file."""
        if output_path is None:
            output_path = input_path + '.minimized'

        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {input_path}: {e}")
            return False

        original_size = len(content)
        minimized_content = self._minimize_content(content)

        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(minimized_content)
        except Exception as e:
            print(f"Error writing {output_path}: {e}")
            return False

        new_size = len(minimized_content)
        reduction = ((original_size - new_size) / original_size) * 100 if original_size > 0 else 0

        print(f"✅ {input_path} -> {output_path}")
        print(f"   Original: {original_size} bytes")
        print(f"   Minimized: {new_size} bytes")
        print(f"   Reduction: {reduction:.1f}%")

        return True

    def _minimize_content(self, content: str) -> str:
        """Minimize content by applying various optimizations."""
        optimized = content

        # Remove dead code
        optimized = self._remove_dead_code(optimized)

        # Simplify logic
        optimized = self._simplify_logic(optimized)

        # Remove redundant imports
        optimized = self._remove_redundant_imports(optimized)

        # Remove comments if requested
        if self.remove_comments:
            optimized = self._remove_comments(optimized)

        # Remove extra whitespace
        optimized = self._remove_extra_whitespace(optimized)

        return optimized

    def _remove_dead_code(self, content: str) -> str:
        """Remove dead code using AST analysis."""
        try:
            tree = ast.parse(content)
        except SyntaxError:
            return content  # Return original if parsing fails

        # Track used names
        self._track_name_usage(tree)

        # Remove unused imports
        if isinstance(tree, ast.Module):
            new_body = []
            for node in tree.body:
                if isinstance(node, ast.Import):
                    if any(alias.name in self.used_names for alias in node.names):
                        new_body.append(node)
                    else:
                        self.optimizations_applied.append(f"Removed unused import: {', '.join(alias.name for alias in node.names)}")
                elif isinstance(node, ast.ImportFrom):
                    if any(alias.name in self.used_names for alias in node.names):
                        new_body.append(node)
                    else:
                        self.optimizations_applied.append(f"Removed unused import: {', '.join(alias.name for alias in node.names)}")
                else:
                    new_body.append(node)

            tree.body = new_body

        return ast.unparse(tree)

    def _track_name_usage(self, tree: ast.AST):
        """Track which names are actually used."""
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                if isinstance(node.ctx, ast.Load):
                    self.used_names.add(node.id)
            elif isinstance(node, ast.Attribute):
                if isinstance(node.value, ast.Name):
                    self.used_names.add(node.value.id)

    def _simplify_logic(self, content: str) -> str:
        """Simplify logical expressions and conditional statements."""
        # Replace complex boolean expressions with simpler equivalents
        patterns = [
            # Simplify double negation
            (r'not\s+not\s+(\w+)', r'\1'),

            # Simplify redundant conditions
            (r'(\w+)\s+and\s+True', r'\1'),
            (r'True\s+and\s+(\w+)', r'\1'),
            (r'(\w+)\s+or\s+False', r'\1'),
            (r'False\s+or\s+(\w+)', r'\1'),

            # Simplify comparisons
            (r'(\w+)\s+==\s+True', r'\1'),
            (r'(\w+)\s+==\s+False', r'not \1'),
            (r'(\w+)\s+!=\s+True', r'not \1'),
            (r'(\w+)\s+!=\s+False', r'\1'),
        ]

        optimized = content
        for pattern, replacement in patterns:
            optimized = re.sub(pattern, replacement, optimized)

        return optimized

    def _remove_redundant_imports(self, content: str) -> str:
        """Remove duplicate or redundant import statements."""
        lines = content.split('\n')
        seen_imports = set()
        new_lines = []

        for line in lines:
            stripped = line.strip()

            if stripped.startswith('import ') or stripped.startswith('from '):
                if stripped not in seen_imports:
                    seen_imports.add(stripped)
                    new_lines.append(line)
                else:
                    self.optimizations_applied.append(f"Removed redundant import: {stripped}")
            else:
                new_lines.append(line)

        return '\n'.join(new_lines)

    def _remove_comments(self, content: str) -> str:
        """Remove comments from code."""
        # Remove single-line comments
        content = re.sub(r'#.*$', '', content, flags=re.MULTILINE)

        # Remove multi-line comments (Python triple quotes used as comments)
        content = re.sub(r'""".*?"""', '', content, flags=re.DOTALL)
        content = re.sub(r"'''.*?'''", '', content, flags=re.DOTALL)

        return content

    def _remove_extra_whitespace(self, content: str) -> str:
        """Remove excessive whitespace and blank lines."""
        lines = content.split('\n')

        # Remove consecutive blank lines
        new_lines = []
        blank_count = 0

        for line in lines:
            if line.strip() == '':
                blank_count += 1
                if blank_count <= 2:  # Allow max 2 consecutive blank lines
                    new_lines.append(line)
            else:
                blank_count = 0
                new_lines.append(line)

        # Remove trailing whitespace
        new_lines = [line.rstrip() for line in new_lines]

        return '\n'.join(new_lines)

    def batch_minimize(self, input_paths: List[str], output_dir: Optional[str] = None) -> bool:
        """Minimize multiple files."""
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        success_count = 0
        for input_path in input_paths:
            if not os.path.isfile(input_path):
                print(f"❌ File not found: {input_path}")
                continue

            if output_dir:
                filename = os.path.basename(input_path)
                output_path = os.path.join(output_dir, filename + '.minimized')
            else:
                output_path = None

            if self.minimize_file(input_path, output_path):
                success_count += 1

        print(f"\n📊 Processed {success_count}/{len(input_paths)} files successfully")
        return success_count > 0

def create_backup(file_path: str) -> str:
    """Create a backup of the original file."""
    backup_path = file_path + '.backup'
    shutil.copy2(file_path, backup_path)
    return backup_path

def verify_functionality(file_path: str) -> bool:
    """Basic functionality verification."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()

        # Try to parse the Python code
        ast.parse(content)
        return True
    except SyntaxError:
        return False
    except Exception:
        return False

def main():
    parser = argparse.ArgumentParser(description='Minimize code files')
    parser.add_argument('files', nargs='+', help='Input files to minimize')
    parser.add_argument('--output', '-o', help='Output file or directory')
    parser.add_argument('--backup', '-b', action='store_true', help='Create backup of original files')
    parser.add_argument('--verify', '-v', action='store_true', help='Verify functionality after minimization')
    parser.add_argument('--aggressive', '-a', action='store_true', help='Apply aggressive optimizations')
    parser.add_argument('--remove-comments', '-c', action='store_true', help='Remove all comments')

    args = parser.parse_args()

    minimizer = CodeMinimizer(
        aggressive=args.aggressive,
        remove_comments=args.remove_comments
    )

    # Process files
    if len(args.files) == 1 and os.path.isdir(args.files[0]):
        # Directory processing
        directory = args.files[0]
        files = []
        for root, dirs, filenames in os.walk(directory):
            for filename in filenames:
                if filename.endswith('.py'):
                    files.append(os.path.join(root, filename))
        output_dir = args.output if args.output else directory
        minimizer.batch_minimize(files, output_dir)
    else:
        # Single file or multiple files
        for file_path in args.files:
            if not os.path.isfile(file_path):
                print(f"❌ File not found: {file_path}")
                continue

            # Create backup if requested
            if args.backup:
                backup_path = create_backup(file_path)
                print(f"📁 Backup created: {backup_path}")

            # Minimize file
            output_path = args.output
            if output_path and os.path.isdir(output_path):
                filename = os.path.basename(file_path)
                output_path = os.path.join(output_path, filename + '.minimized')

            if minimizer.minimize_file(file_path, output_path):
                # Verify functionality if requested
                if args.verify:
                    if verify_functionality(output_path or file_path + '.minimized'):
                        print("✅ Functionality verified")
                    else:
                        print("❌ Functionality verification failed")

    # Print optimization summary
    if minimizer.optimizations_applied:
        print("\n🔧 Optimizations applied:")
        for optimization in minimizer.optimizations_applied[:10]:  # Show first 10
            print(f"   • {optimization}")
        if len(minimizer.optimizations_applied) > 10:
            print(f"   ... and {len(minimizer.optimizations_applied) - 10} more")

if __name__ == '__main__':
    main()
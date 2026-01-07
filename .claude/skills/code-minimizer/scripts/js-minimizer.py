#!/usr/bin/env python3
"""
JavaScript Code Minimizer

This script specifically optimizes JavaScript code by:
- Removing comments and whitespace
- Shortening variable names
- Optimizing string literals
- Simplifying expressions
"""

import re
import sys
import os
import argparse
from typing import Dict, List, Set

class JSMinimizer:
    """Minimize JavaScript code."""

    def __init__(self, remove_comments: bool = True, minify_vars: bool = True):
        self.remove_comments = remove_comments
        self.minify_vars = minify_vars
        self.var_map = {}
        self.var_counter = 0

    def minimize_file(self, input_path: str, output_path: Optional[str] = None) -> bool:
        """Minimize a JavaScript file."""
        if output_path is None:
            output_path = input_path.replace('.js', '.min.js')

        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {input_path}: {e}")
            return False

        original_size = len(content)
        minimized_content = self.minimize_content(content)

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

    def minimize_content(self, content: str) -> str:
        """Minimize JavaScript content."""
        optimized = content

        # Remove comments
        if self.remove_comments:
            optimized = self._remove_comments(optimized)

        # Shorten variable names
        if self.minify_vars:
            optimized = self._shorten_variable_names(optimized)

        # Remove unnecessary whitespace
        optimized = self._remove_whitespace(optimized)

        # Optimize string literals
        optimized = self._optimize_strings(optimized)

        return optimized

    def _remove_comments(self, content: str) -> str:
        """Remove JavaScript comments."""
        # Remove single-line comments
        content = re.sub(r'//.*$', '', content, flags=re.MULTILINE)

        # Remove multi-line comments
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

        return content

    def _shorten_variable_names(self, content: str) -> str:
        """Shorten variable and function names."""
        # Find all variable declarations and function definitions
        var_pattern = r'\b(var|let|const|function)\s+(\w+)'
        func_pattern = r'\bfunction\s+(\w+)'
        param_pattern = r'function\s*\(([^)]*)\)'

        # Collect all names that need to be mapped
        all_names = set()

        # Find variable declarations
        for match in re.finditer(var_pattern, content):
            var_name = match.group(2)
            if len(var_name) > 2:  # Only shorten long names
                all_names.add(var_name)

        # Find function names
        for match in re.finditer(func_pattern, content):
            func_name = match.group(1)
            if len(func_name) > 2:
                all_names.add(func_name)

        # Create mapping for short names
        for name in sorted(all_names, key=len, reverse=True):
            short_name = self._generate_short_name()
            self.var_map[name] = short_name

        # Replace all occurrences
        optimized = content
        for long_name, short_name in self.var_map.items():
            # Use word boundaries to avoid partial matches
            pattern = r'\b' + re.escape(long_name) + r'\b'
            optimized = re.sub(pattern, short_name, optimized)

        return optimized

    def _generate_short_name(self) -> str:
        """Generate a short variable name."""
        # Use single letters first, then combinations
        if self.var_counter < 26:
            name = chr(ord('a') + self.var_counter)
        else:
            base = self.var_counter - 26
            first = chr(ord('a') + (base // 26))
            second = chr(ord('a') + (base % 26))
            name = first + second

        self.var_counter += 1
        return name

    def _remove_whitespace(self, content: str) -> str:
        """Remove unnecessary whitespace."""
        # Remove extra spaces around operators
        content = re.sub(r'\s*([=+\-*/<>!&|])\s*', r'\1', content)

        # Remove spaces after commas
        content = re.sub(r',\s*', ',', content)

        # Remove spaces after opening brackets
        content = re.sub(r'\[\s*', '[', content)
        content = re.sub(r'\(\s*', '(', content)
        content = re.sub(r'{\s*', '{', content)

        # Remove spaces before closing brackets
        content = re.sub(r'\s*]', ']', content)
        content = re.sub(r'\s*\)', ')', content)
        content = re.sub(r'\s*}', '}', content)

        # Remove multiple spaces
        content = re.sub(r'\s+', ' ', content)

        # Remove spaces before semicolons
        content = re.sub(r'\s*;\s*', ';', content)

        return content.strip()

    def _optimize_strings(self, content: str) -> str:
        """Optimize string literals."""
        # Replace double quotes with single quotes if it saves space
        def replace_quotes(match):
            string_content = match.group(1)
            if "'" not in string_content and len(string_content) > 1:
                return f"'{string_content}'"
            return match.group(0)

        content = re.sub(r'"([^"]*)"', replace_quotes, content)

        # Remove unnecessary escape sequences
        content = re.sub(r'\\(.)', r'\1', content)

        return content

def create_minimized_copy(input_path: str) -> str:
    """Create a minimized copy of the input file."""
    minimizer = JSMinimizer(remove_comments=True, minify_vars=True)
    output_path = input_path.replace('.js', '.min.js')
    minimizer.minimize_file(input_path, output_path)
    return output_path

def batch_minimize(directory: str) -> List[str]:
    """Minimize all JavaScript files in a directory."""
    minimizer = JSMinimizer(remove_comments=True, minify_vars=True)
    output_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.js') and not file.endswith('.min.js'):
                input_path = os.path.join(root, file)
                output_path = input_path.replace('.js', '.min.js')
                if minimizer.minimize_file(input_path, output_path):
                    output_files.append(output_path)

    return output_files

def main():
    parser = argparse.ArgumentParser(description='Minimize JavaScript files')
    parser.add_argument('files', nargs='+', help='JavaScript files to minimize')
    parser.add_argument('--output', '-o', help='Output file or directory')
    parser.add_argument('--remove-comments', '-c', action='store_true',
                       help='Remove comments (default: True)')
    parser.add_argument('--minify-vars', '-v', action='store_true',
                       help='Minify variable names (default: True)')
    parser.add_argument('--no-comments', action='store_true',
                       help='Keep comments')
    parser.add_argument('--no-vars', action='store_true',
                       help='Keep variable names')

    args = parser.parse_args()

    # Process arguments
    remove_comments = args.remove_comments and not args.no_comments
    minify_vars = args.minify_vars and not args.no_vars

    minimizer = JSMinimizer(remove_comments=remove_comments, minify_vars=minify_vars)

    # Process files
    if len(args.files) == 1 and os.path.isdir(args.files[0]):
        # Directory processing
        output_files = batch_minimize(args.files[0])
        print(f"✅ Minimized {len(output_files)} files")
    else:
        # Single file or multiple files
        for file_path in args.files:
            if os.path.isfile(file_path) and file_path.endswith('.js'):
                output_path = args.output
                if output_path and os.path.isdir(output_path):
                    filename = os.path.basename(file_path)
                    output_path = os.path.join(output_path, filename.replace('.js', '.min.js'))

                minimizer.minimize_file(file_path, output_path)

if __name__ == '__main__':
    main()
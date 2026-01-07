#!/usr/bin/env python3
"""
Summarize text using extractive summarization techniques.

This script reads text from a file or stdin and produces a concise summary
by extracting the most important sentences.
"""

import argparse
import re
import string
import sys
from collections import Counter
from typing import List, Tuple

def clean_text(text: str) -> str:
    """Clean and normalize text for processing."""
    # Remove extra whitespace and normalize newlines
    text = re.sub(r'\s+', ' ', text.strip())
    # Remove special characters but keep punctuation for sentence parsing
    text = re.sub(r'[^\w\s\.\!\?\,\;\:]', '', text)
    return text

def split_into_sentences(text: str) -> List[str]:
    """Split text into sentences using regex."""
    # Split on sentence-ending punctuation followed by whitespace or end of string
    sentences = re.split(r'(?<=[.!?])\s+', text)
    # Filter out empty sentences and very short ones
    return [s for s in sentences if len(s.strip()) > 10]

def calculate_word_frequency(sentences: List[str]) -> Counter:
    """Calculate word frequency across all sentences."""
    words = []
    for sentence in sentences:
        # Remove punctuation and convert to lowercase
        sentence_words = re.findall(r'\b\w+\b', sentence.lower())
        words.extend(sentence_words)
    return Counter(words)

def score_sentences(sentences: List[str], word_freq: Counter) -> List[Tuple[str, float]]:
    """Score each sentence based on word frequency."""
    scored_sentences = []
    for sentence in sentences:
        # Calculate sentence length (number of words)
        sentence_words = re.findall(r'\b\w+\b', sentence.lower())
        sentence_length = len(sentence_words)

        # Calculate word frequency score
        word_score = sum(word_freq[word] for word in sentence_words)

        # Calculate sentence score (weighted by length)
        sentence_score = (word_score / sentence_length) if sentence_length > 0 else 0

        scored_sentences.append((sentence, sentence_score))

    return scored_sentences

def create_summary(sentences: List[str], num_sentences: int = 3) -> str:
    """Create a summary by selecting top sentences."""
    if len(sentences) <= num_sentences:
        return " ".join(sentences)

    # Calculate word frequency
    word_freq = calculate_word_frequency(sentences)

    # Score sentences
    scored_sentences = score_sentences(sentences, word_freq)

    # Sort by score and select top sentences
    scored_sentences.sort(key=lambda x: x[1], reverse=True)
    top_sentences = scored_sentences[:num_sentences]

    # Sort top sentences by original position
    top_sentences.sort(key=lambda x: sentences.index(x[0]))

    # Join sentences
    summary = " ".join(sentence for sentence, _ in top_sentences)

    return summary

def analyze_text_structure(text: str) -> dict:
    """Analyze the structure and characteristics of the text."""
    sentences = split_into_sentences(text)

    analysis = {
        'sentence_count': len(sentences),
        'word_count': len(re.findall(r'\b\w+\b', text.lower())),
        'average_sentence_length': len(re.findall(r'\b\w+\b', text.lower())) / len(sentences) if sentences else 0,
        'unique_words': len(set(re.findall(r'\b\w+\b', text.lower()))),
        'complexity_score': len(re.findall(r'\b\w+\b', text.lower())) / len(sentences) if sentences else 0,
    }

    return analysis

def main():
    parser = argparse.ArgumentParser(description='Create summaries of text content')
    parser.add_argument('input', nargs='?', help='Input file path (if not provided, reads from stdin)')
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--length', '-l', type=int, default=3, help='Number of sentences in summary (default: 3)')
    parser.add_argument('--method', '-m', choices=['extractive'], default='extractive', help='Summarization method (default: extractive)')
    parser.add_argument('--analyze', action='store_true', help='Analyze text structure instead of creating summary')

    args = parser.parse_args()

    # Read input
    if args.input:
        try:
            with open(args.input, 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.input}' not found", file=sys.stderr)
            sys.exit(1)
    else:
        text = sys.stdin.read()

    # Clean text
    cleaned_text = clean_text(text)
    sentences = split_into_sentences(cleaned_text)

    if not sentences:
        print("No sentences found in input text.")
        sys.exit(1)

    if args.analyze:
        analysis = analyze_text_structure(cleaned_text)
        print("Text Analysis:")
        print(f"  Sentence count: {analysis['sentence_count']}")
        print(f"  Word count: {analysis['word_count']}")
        print(f"  Average sentence length: {analysis['average_sentence_length']:.1f} words")
        print(f"  Unique words: {analysis['unique_words']}")
        print(f"  Complexity score: {analysis['complexity_score']:.1f}")
        return

    # Create summary
    if args.method == 'extractive':
        summary = create_summary(sentences, args.length)
    else:
        print(f"Unknown method: {args.method}")
        sys.exit(1)

    # Output summary
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(summary)
            print(f"Summary written to {args.output}")
        except Exception as e:
            print(f"Error writing to file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(summary)

if __name__ == '__main__':
    main()
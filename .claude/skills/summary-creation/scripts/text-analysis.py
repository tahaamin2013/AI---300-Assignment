#!/usr/bin/env python3
"""
Analyze text structure and identify key sections for summarization.

This script provides detailed analysis of text to help identify
important sections, topics, and structure for effective summarization.
"""

import argparse
import re
import sys
from collections import Counter
from typing import Dict, List, Tuple

class TextAnalyzer:
    """Analyze text structure and identify key components."""

    def __init__(self, text: str):
        self.text = text
        self.sentences = self._split_into_sentences()
        self.paragraphs = self._split_into_paragraphs()
        self.words = self._extract_words()
        self.word_freq = Counter(self.words)
        self.sentence_scores = self._calculate_sentence_scores()

    def _split_into_sentences(self) -> List[str]:
        """Split text into sentences."""
        sentences = re.split(r'(?<=[.!?])\s+', self.text.strip())
        return [s for s in sentences if len(s.strip()) > 5]

    def _split_into_paragraphs(self) -> List[str]:
        """Split text into paragraphs."""
        paragraphs = re.split(r'\n\s*\n', self.text)
        return [p.strip() for p in paragraphs if p.strip()]

    def _extract_words(self) -> List[str]:
        """Extract words from text."""
        return re.findall(r'\b\w+\b', self.text.lower())

    def _calculate_sentence_scores(self) -> List[Tuple[int, str, float]]:
        """Calculate importance scores for each sentence."""
        scored_sentences = []

        for i, sentence in enumerate(self.sentences):
            # Calculate various scores
            word_score = sum(self.word_freq[word] for word in re.findall(r'\b\w+\b', sentence.lower()))
            sentence_length = len(re.findall(r'\b\w+\b', sentence))
            unique_words = len(set(re.findall(r'\b\w+\b', sentence.lower())))

            # Calculate sentence importance
            importance = (word_score / sentence_length) if sentence_length > 0 else 0
            importance += unique_words * 0.1  # Bonus for unique words

            scored_sentences.append((i, sentence, importance))

        return sorted(scored_sentences, key=lambda x: x[2], reverse=True)

    def get_key_topics(self, top_n: int = 5) -> List[Tuple[str, int]]:
        """Identify key topics based on word frequency."""
        # Filter out common stop words
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'should',
            'could', 'can', 'may', 'might', 'must', 'shall', 'this', 'that',
            'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me',
            'him', 'her', 'us', 'them', 'my', 'your', 'his', 'its', 'our', 'their'
        }

        filtered_words = [(word, count) for word, count in self.word_freq.items()
                         if word not in stop_words and len(word) > 3]
        return sorted(filtered_words, key=lambda x: x[1], reverse=True)[:top_n]

    def get_section_analysis(self) -> Dict:
        """Analyze text sections and their importance."""
        analysis = {
            'introduction': self._analyze_section(0, min(3, len(self.sentences) // 3)),
            'body': self._analyze_section(len(self.sentences) // 3, 2 * len(self.sentences) // 3),
            'conclusion': self._analyze_section(2 * len(self.sentences) // 3, len(self.sentences))
        }
        return analysis

    def _analyze_section(self, start: int, end: int) -> Dict:
        """Analyze a specific section of text."""
        section_sentences = self.sentences[start:end]
        if not section_sentences:
            return {'score': 0, 'key_words': [], 'sentence_count': 0}

        # Calculate section score
        section_words = []
        for sentence in section_sentences:
            section_words.extend(re.findall(r'\b\w+\b', sentence.lower()))

        section_freq = Counter(section_words)
        section_score = sum(section_freq[word] for word in section_words) / len(section_words) if section_words else 0

        # Get key words in section
        key_words = sorted([(word, count) for word, count in section_freq.items()
                           if len(word) > 3], key=lambda x: x[1], reverse=True)[:5]

        return {
            'score': section_score,
            'key_words': key_words,
            'sentence_count': len(section_sentences)
        }

    def get_vocabulary_analysis(self) -> Dict:
        """Analyze vocabulary complexity and usage."""
        total_words = len(self.words)
        unique_words = len(set(self.words))

        # Calculate complexity metrics
        long_words = [word for word in self.words if len(word) >= 6]
        complex_words = [word for word in self.words if len(word) >= 8]

        analysis = {
            'total_words': total_words,
            'unique_words': unique_words,
            'vocabulary_richness': unique_words / total_words if total_words > 0 else 0,
            'long_words_count': len(long_words),
            'complex_words_count': len(complex_words),
            'long_words_percentage': len(long_words) / total_words * 100 if total_words > 0 else 0,
            'complex_words_percentage': len(complex_words) / total_words * 100 if total_words > 0 else 0
        }

        return analysis

    def get_summary_recommendations(self) -> Dict:
        """Provide recommendations for creating an effective summary."""
        top_sentences = self.sentence_scores[:5]
        key_topics = self.get_key_topics(5)

        recommendations = {
            'include_sentences': [sentence for _, sentence, _ in top_sentences],
            'key_topics': [topic for topic, _ in key_topics],
            'summary_length': min(max(len(self.sentences) // 4, 3), 7),
            'important_sections': self.get_section_analysis()
        }

        return recommendations

def main():
    parser = argparse.ArgumentParser(description='Analyze text structure for summarization')
    parser.add_argument('input', nargs='?', help='Input file path (if not provided, reads from stdin)')
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--top-words', '-w', type=int, default=10, help='Number of top words to show (default: 10)')

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

    if not text.strip():
        print("No text provided for analysis.", file=sys.stderr)
        sys.exit(1)

    # Analyze text
    analyzer = TextAnalyzer(text)

    # Generate analysis
    analysis_output = []

    # Basic statistics
    analysis_output.append("=== TEXT ANALYSIS REPORT ===")
    analysis_output.append(f"Total sentences: {len(analyzer.sentences)}")
    analysis_output.append(f"Total paragraphs: {len(analyzer.paragraphs)}")
    analysis_output.append(f"Total words: {len(analyzer.words)}")
    analysis_output.append(f"Unique words: {len(set(analyzer.words))}")

    # Key topics
    analysis_output.append("\n=== KEY TOPICS ===")
    for word, count in analyzer.get_key_topics(args.top_words):
        analysis_output.append(f"{word}: {count}")

    # Sentence importance
    analysis_output.append("\n=== MOST IMPORTANT SENTENCES ===")
    for i, (sentence, score) in enumerate(analyzer.sentence_scores[:5]):
        analysis_output.append(f"{i+1}. {sentence[:100]}... (score: {score:.2f})")

    # Section analysis
    analysis_output.append("\n=== SECTION ANALYSIS ===")
    sections = analyzer.get_section_analysis()
    for section_name, section_data in sections.items():
        analysis_output.append(f"{section_name.title()}:")
        analysis_output.append(f"  Score: {section_data['score']:.2f}")
        analysis_output.append(f"  Sentences: {section_data['sentence_count']}")
        analysis_output.append(f"  Key words: {', '.join([word for word, _ in section_data['key_words']])}")

    # Vocabulary analysis
    vocab_analysis = analyzer.get_vocabulary_analysis()
    analysis_output.append("\n=== VOCABULARY ANALYSIS ===")
    analysis_output.append(f"Vocabulary richness: {vocab_analysis['vocabulary_richness']:.2f}")
    analysis_output.append(f"Long words (6+ chars): {vocab_analysis['long_words_percentage']:.1f}%")
    analysis_output.append(f"Complex words (8+ chars): {vocab_analysis['complex_words_percentage']:.1f}%")

    # Summary recommendations
    recommendations = analyzer.get_summary_recommendations()
    analysis_output.append("\n=== SUMMARY RECOMMENDATIONS ===")
    analysis_output.append(f"Recommended summary length: {recommendations['summary_length']} sentences")
    analysis_output.append("\nKey topics to include:")
    for topic in recommendations['key_topics']:
        analysis_output.append(f"  - {topic}")

    # Output results
    output_text = "\n".join(analysis_output)

    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output_text)
            print(f"Analysis written to {args.output}")
        except Exception as e:
            print(f"Error writing to file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(output_text)

if __name__ == '__main__':
    main()
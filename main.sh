#!/bin/bash

echo "========================================="
echo "🧬 PROTEIN SEQUENCE ANALYZER CLI"
echo " Bioinformatics Linux Tool v1.0"
echo "========================================="
echo ""

# Ask user input
read -p "📁 Enter FASTA file name or full path: " FILE

# Check if empty
if [ -z "$FILE" ]; then
    echo "❌ Error: No input provided"
    exit 1
fi

# Check file exists
if [ ! -f "$FILE" ]; then
    echo "❌ Error: File not found -> $FILE"
    exit 1
fi

# Check FASTA extension
if [[ "$FILE" != *.fasta && "$FILE" != *.fa ]]; then
    echo "⚠️ Warning: File does not have .fasta/.fa extension"
    echo "Proceeding anyway..."
fi

# Check FASTA format (basic validation)
FIRST_LINE=$(head -n 1 "$FILE")

if [[ "$FIRST_LINE" != ">"* ]]; then
    echo "❌ Error: Invalid FASTA file (missing '>' header)"
    exit 1
fi

echo ""
echo "✅ File validated successfully!"
echo "🚀 Starting bioinformatics analysis..."
echo ""

# Run analyzer
python3 analyzer.py "$FILE"

echo ""
echo "🎉 Analysis completed successfully!"

#!/bin/sh
# Rebuild the PDFs of the selected texts (texts/*.pdf) from the manuscripts in src/.
# Every footnote starts on the page of its call; a long note continues at the top of the
# next page's footnote area. After each PDF, fncheck.py verifies exactly that and the
# script stops with an error if a note starts on a later page than its call.
#
# Needs Python 3 with the packages in requirements.txt:
#   pip install -r _tools/texts/requirements.txt
# Usage (from anywhere):
#   sh _tools/texts/build.sh            writes into the site's texts/ folder
#   sh _tools/texts/build.sh OUTDIR     writes elsewhere, e.g. to compare first
# The Python interpreter can be chosen with PYTHON=/path/to/python.
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
OUT=${1:-$HERE/../../texts}
PY=${PYTHON:-python3}
mkdir -p "$HERE/build" "$OUT"

build() {   # name (= file name in src/ and texts/), document type, footer label
  "$PY" "$HERE/html2typ.py" "$HERE/src/$1.html" "$HERE/build/$1.typ" "$2" "$3"
  "$PY" -c 'import sys, typst; typst.compile(sys.argv[1], output=sys.argv[2], font_paths=[sys.argv[3]], ignore_system_fonts=True)' \
    "$HERE/build/$1.typ" "$OUT/$1.pdf" "$HERE/fonts"
  "$PY" "$HERE/fncheck.py" "$OUT/$1.pdf" "$HERE/src/$1.html" --summary
}

build berg-2019-identity-in-difference identity \
  "A. Berg, “Identity in Difference – Wittgenstein’s Hegel” · accepted manuscript"
build berg-2022-wittgensteins-photo-album lw \
  "A. Berg, “Wittgenstein’s photo album as a philosophical experiment” · author’s corrected version"
build berg-2020-begriffe-des-psychischen psych \
  "A. Berg, „Wittgenstein und die Begriffe des Psychischen bei Hegel“ · Manuskriptfassung"

#!/usr/bin/env bash

set -euo pipefail

find . -type f -name '*.wls' -print0 |
while IFS= read -r -d '' file; do
    sed -i 's/\r$//' "$file"    # LF ending
    chmod +x "$file"
    printf 'Updated: %s\n' "$file"
done
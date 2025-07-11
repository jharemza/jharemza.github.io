#!/bin/bash

# === CONFIG ===
TITLE="$1"
SLUG="$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//;s/-$//')"
DRAFT_FILE="_drafts/${SLUG}.md"
PROJECT_FILE="_projects/${SLUG}.md"

# === VALIDATE INPUT ===
if [ -z "$TITLE" ]; then
  echo "Usage: $0 \"Project Title\""
  exit 1
fi

if [ ! -f "$DRAFT_FILE" ]; then
  echo "Error: Draft file not found at $DRAFT_FILE"
  exit 1
fi

# === STEP 1: Compose new project entry ===
bundle exec jekyll compose "$TITLE" --collection projects

# === STEP 2: Identify newly created file ===
if [ ! -f "$PROJECT_FILE" ]; then
  echo "Error: Expected project file not found at $PROJECT_FILE"
  exit 1
fi

# === STEP 3: Extract body from draft ===
DRAFT_BODY=$(awk '
  BEGIN { in_front_matter=0 }
  /^---/ {
    if (in_front_matter == 0) {
      in_front_matter = 1
      next
    } else {
      in_front_matter = 0
      next
    }
  }
  in_front_matter == 0 { print }
' "$DRAFT_FILE")

# === STEP 4: Append body to project file ===
echo -e "\n$DRAFT_BODY" >> "$PROJECT_FILE"

# === STEP 5: Delete original draft ===
rm "$DRAFT_FILE"

echo "✅ Draft promoted to $PROJECT_FILE"

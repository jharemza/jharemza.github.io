#!/bin/bash
#
# fix_image_filenames.sh
# Description:
#   - Renames image files with spaces to underscores
#   - Updates Markdown in _posts and _drafts:
#       • Replaces &#32; with _
#       • Fixes path from /images/ to /assets/img/posts/
#   - Logs all changes to fix_image_filenames.log
# Usage:
#   bash tools/fix_image_filenames.sh

PROJECT_DIR=~/jharemza.github.io
IMG_DIR="$PROJECT_DIR/assets/img"
POST_DIRS=("$PROJECT_DIR/_posts" "$PROJECT_DIR/_drafts")
LOG_FILE="$PROJECT_DIR/tools/fix_image_filenames.log"

echo "📝 Writing log to $LOG_FILE"
echo "===== Image Rename + Markdown Update Log =====" > "$LOG_FILE"
echo "Timestamp: $(date)" >> "$LOG_FILE"
echo >> "$LOG_FILE"

echo "🔍 Step 1: Renaming image files with spaces..."
find "$IMG_DIR" -type f -name "* *" | while read -r file; do
  new_path="$(dirname "$file")/$(basename "$file" | tr ' ' '_')"
  echo "🔄 $file → $new_path"
  echo "[rename] $file → $new_path" >> "$LOG_FILE"
  mv "$file" "$new_path"
done
echo "✅ Done renaming images." | tee -a "$LOG_FILE"
echo >> "$LOG_FILE"

echo "🔍 Step 2: Updating Markdown references..." | tee -a "$LOG_FILE"
for dir in "${POST_DIRS[@]}"; do
  if [ -d "$dir" ]; then
    find "$dir" -type f -name "*.md" | while read -r mdfile; do
      echo "🔧 Updating: $mdfile"
      echo "[update] $mdfile" >> "$LOG_FILE"
      sed -i 's/&#32;/_/g' "$mdfile"
      sed -i 's|/images/|/assets/img/posts/|g' "$mdfile"
    done
  fi
done
echo "✅ Markdown references updated." | tee -a "$LOG_FILE"

echo "🚀 All done. See log at $LOG_FILE"

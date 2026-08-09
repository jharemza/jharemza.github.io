#!/usr/bin/env bash

set -euo pipefail

site_dir="${1:-_site}"
input_dir="$(mktemp -d)"
config_file="$(pwd)/linkinator.config.json"
trap 'rm -rf "$input_dir"' EXIT

# Flatten the generated pages into distinct entry points. This lets Linkinator
# report the originating page while the configured path prefixes skip internal
# links without also excluding pages nested under those prefixes.
while IFS= read -r -d '' page; do
  relative_path="${page#"$site_dir"/}"
  flattened_path="${relative_path//\//__}"
  cp "$page" "$input_dir/$flattened_path"
done < <(find "$site_dir" -type f -name '*.html' -print0)

(
  cd "$input_dir"
  npx --yes linkinator@8.0.3 "*.html" --config "$config_file"
)

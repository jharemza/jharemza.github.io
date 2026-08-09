# jharemza.github.io

This repository contains the source code for [jeremiahharemza.com](https://jeremiahharemza.com), a personal website built with Jekyll and deployed using Cloudflare Pages.

## 🔧 Overview

- Framework: Jekyll (customized Chirpy theme)
- Deployment: Cloudflare Pages (via GitHub repo)
- Content: Technical portfolio, blog posts, project documentation

## 🚀 Local Development

To preview the site locally:

```bash
# Clone the repository
git clone https://github.com/jharemza/jharemza.github.io.git
cd jharemza.github.io

# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve
```

Then visit `http://localhost:4000` in your browser.

## 🔄 CI/CD Pipeline

The build and deployment workflow:

1. Edit or create content locally.
2. Push changes to the `main` branch on GitHub.
3. Cloudflare Pages automatically builds and deploys the site from GitHub.

The blocking GitHub Actions workflow
([`htmlproofer.yml`](.github/workflows/htmlproofer.yml)) validates generated HTML,
internal links and anchors, images, and scripts. It deliberately does not make
requests to third-party sites. The scheduled and manually triggered
[`external-links.yml`](.github/workflows/external-links.yml) workflow reports
external-link health separately, so transient outages and bot protection do not
block unrelated pull requests. Deployment is handled directly by Cloudflare Pages.

### Link validation

Build the site before running either validation path:

```sh
bundle install
bundle exec jekyll build
```

Run the deterministic internal-site checks with HTMLProofer:

```sh
bundle install --gemfile ci/htmlproofer/Gemfile
BUNDLE_GEMFILE=ci/htmlproofer/Gemfile bundle exec htmlproofer _site \
  --disable-external --no-enforce-https
```

Run the external-link report with the pinned Linkinator version used in CI:

```sh
tools/check_external_links.sh _site
```

The helper invokes the pinned Linkinator version and flattens the generated pages
into temporary entry points. A name such as `posts__example__index.html` in the
report maps to `_site/posts/example/index.html`. Linkinator's repository-level
configuration retries transient failures and treats HTTP 403 and 999
bot-protection responses as warnings. Its informational output includes the source
page and checked URL. Add URL exclusions to
`linkinator.config.json` only when a narrowly identified endpoint cannot be checked
reliably.

## 📁 Repository Structure

- `_posts/`: Published blog posts
- `_drafts/`: Unpublished drafts (via jekyll-compose)
- `_layouts/`, `_includes/`: Custom Chirpy theme overrides
- `assets/`, `tabs/`, `pages/`: Static files and navigation content

## 🛠️ Notable Features

- Markdown-based content authoring
- Built-in SEO, RSS, and sitemap support
- jekyll-last-modified-at for post update tracking
- Custom domain via Cloudflare DNS and HTTPS

## 🖼️ Header Image Generation

Blog posts can include standardized header images generated automatically. Use
`tools/generate_blog_header.py` to create a `1200x630` PNG with the site's fonts and
colors:

```bash
python3 tools/generate_blog_header.py "Post Title" --subtitle "Optional subtitle" -o \
  assets/img/headers/post-title.png
```

The script requires the `Pillow` package (see `requirements.txt`).
Install the pinned dependencies and run its smoke test locally with:

```sh
python3 -m pip install -r requirements.txt
python3 -m unittest tests/test_generate_blog_header.py -v
```

## 🧪 Development Notes

Internal documentation (managed in Notion) includes:

- Change log
- Content workflow
- Deployment notes and troubleshooting

## 📄 License

- 🧱 **Code**: Licensed under the [MIT License](./LICENSE)  
  You are free to reuse or adapt the source code for your own non-commercial or commercial projects.

- 📚 **Content**: Original content (posts, graphics, etc.) is licensed under [Creative Commons BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).  
  You may share with attribution, but not alter or use commercially.

## 📌 Theme Attribution

If you're looking for the source theme, visit the [Chirpy Theme repo](https://github.com/cotes2020/jekyll-theme-chirpy).

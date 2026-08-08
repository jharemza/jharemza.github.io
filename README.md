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

A GitHub Actions workflow ([`htmlproofer.yml`](.github/workflows/htmlproofer.yml))
validates the generated HTML, while deployment is handled directly by Cloudflare
Pages.

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

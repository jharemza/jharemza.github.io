# jharemza.github.io

This repository contains the source code for jeremiahharemza.com, a personal website built with Jekyll and deployed using Cloudflare Pages.

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
2. Push changes to the main branch on GitHub.
3. Cloudflare Pages automatically builds and deploys the site from GitHub.

No GitHub Actions are used — deployment is handled directly by Cloudflare Pages.

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

## 🧪 Development Notes

Internal documentation (managed in Notion) includes:

- Change log
- Content workflow
- Deployment notes and troubleshooting

## footnote

If you're looking for the source theme, visit the [Chirpy Theme repo](https://github.com/cotes2020/jekyll-theme-chirpy).

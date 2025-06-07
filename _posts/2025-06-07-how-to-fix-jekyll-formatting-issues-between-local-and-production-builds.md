---
layout: post
title: How to Fix Jekyll Formatting Issues Between Local and Production Builds
excerpt: 'Solving Jekyll CI/CD Formatting Mysteries: When Local and Production Builds
  Don''t Match'
author: jharemza
comments: false
toc: true
category:
- Jekyll
- CI/CD
tags:
- jekyll-theme
- cloudflare-pages
- github-actions
- gemfile-lock
- bundler
- deployment
date: 2025-06-07 11:28 -0400
---
## Solving Jekyll CI/CD Formatting Mysteries: When Local and Production Builds Don't Match

I'd deployed a Jekyll site only to find that my beautifully formatted local version looked completely different in GitHub Pages. Incorrect spacing, broken text wrapping, and mysterious bullet points appear where they shouldn't. WTF!? If you're experiencing a similar issue, you're not alone. Read on.

## The Problem

I was building a static Jekyll site using the [Chirpy theme](https://github.com/cotes2020/jekyll-theme-chirpy) with a straightforward CI/CD pipeline:

- **Local Development:** Windows 11 with WSL2 + Ubuntu, Ruby 3.2.3, Jekyll with Bundler
- **Deployment:** GitHub → Cloudflare Pages with GitHub Actions for HTML validation

Everything worked perfectly locally. But when deployed through Cloudflare Pages' CI/CD pipeline, the site had significant formatting issues:

- Incorrect spacing throughout
- Text not wrapping properly
- Bullet points appear where they shouldn't
- General layout inconsistencies

The strange part? When I manually copied my local `_site/` folder to Cloudflare using Wrangler CLI, everything displayed perfectly. Same content, different pipeline, different results.

## The Investigation

Running `diff` and `meld` commands in Linux between my local build and the CI/CD build showed differences, but it wasn't immediately clear what was causing the formatting problems.

The key clue came from examining my setup:

- Local Gemfile.lock showed `sass-embedded 1.87.0`
- Both environments were using Ruby 3.2.3
- Both had identical Jekyll versions

However, there was one critical mistake: **the `Gemfile.lock` file was included in my `.gitignore` file.**

## The Root Cause

The issue boiled down to **gem version inconsistencies**, specifically with the Sass processor:

1. **Local environment:** Used my specific `Gemfile.lock` with `sass-embedded 1.87.0`
2. **Cloudflare CI/CD:** Generated its own `Gemfile.lock` on each build, potentially using different gem versions
3. **Different Sass versions:** Produced subtly different CSS compilation, causing the formatting issues

Even though both environments used the same Ruby and Jekyll versions, the underlying gems (especially the Sass processor) were different, leading to inconsistent CSS generation.

## The Solution

The fix required two steps:

### Step 1: Commit Gemfile.lock

```bash
# Remove Gemfile.lock from .gitignore
git add Gemfile.lock
git commit -m "Add Gemfile.lock for consistent builds"
git push
```

### Step 2: Force Deployment Mode in CI/CD

Updated the Cloudflare Pages build command from:

```bash
bundle exec jekyll build
```

To:

```bash
bundle config set deployment true && bundle install && bundle exec jekyll build
```

## Why This Worked

### Gemfile.lock is Critical for Production

Many developers, myself included, mistakenly add `Gemfile.lock` to `.gitignore`, thinking it's similar to `node_modules`. However:

- **For applications** (like Jekyll sites): `Gemfile.lock` should be committed
- **For gems/libraries:** `Gemfile.lock` should be ignored
- The lock file ensures identical gem versions across all environments

### Deployment Mode Enforces Consistency

The `--deployment` flag (now `bundle config set deployment true`) tells Bundler:

- Use exactly what is specified in the `Gemfile.lock`
- Don't try to resolve dependencies or update versions
- Fail if the lock file is inconsistent

This prevents CI/CD environments from making "helpful" adjustments to gem versions.

## The Results

After implementing both changes:

- Local and production builds now generate identical HTML and CSS
- Formatting issues are completely resolved
- The build process is more predictable and reliable
- No more mysterious layout differences

## Key Takeaway

Jekyll formatting issues between local and CI/CD environments are almost always caused by gem version mismatches, particularly with Sass processors. The solution is enforcing identical dependency versions through:

1. **Committing your `Gemfile.lock`**
2. **Using deployment mode in CI/CD builds**

Completing the above steps ensures your beautiful local Jekyll site looks identical in production every single time.

---

*Have you encountered similar Jekyll CI/CD issues? The root cause is usually hiding in your dependency management. When in doubt, check your gems first!*

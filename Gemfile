# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

# gem "rails"

gem "jekyll", "~> 4.2"

# If you have any plugins, put them here!
group :jekyll_plugins do
    gem 'jekyll-feed'
    gem 'jekyll-sitemap'
    gem 'jekyll-seo-tag'
  end

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby]

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.0" if Gem.win_platform?

---
title: "GitHub Pages Deployment Guide"
description: "Complete guide for deploying CS Quest Adventures to GitHub Pages"
---

# GitHub Pages Deployment Guide

This guide explains the deployment process and troubleshooting for CS Quest Adventures on GitHub Pages.

## Overview

The site is automatically deployed to GitHub Pages when changes are pushed to the `main` branch. The deployment uses GitHub Actions with a custom workflow that handles:

1. Python environment setup
2. JupyterLite application build
3. Quarto site rendering
4. GitHub Pages deployment

## Deployment Workflow

### Automatic Deployment

The `.github/workflows/deploy.yml` workflow automatically deploys on every push to `main`:

```yaml
on:
  push:
    branches: [main]
```

### Build Steps

The workflow performs the following steps:

1. **Environment Setup**
   - Installs Python 3.11
   - Installs dependencies from `requirements.txt`
   - Sets up IPython kernel
   - Installs Quarto 1.7.33

2. **JupyterLite Build** (Critical!)
   - Builds JupyterLite application from source
   - Creates browser-based Jupyter environment
   - Copies notebooks from `content/` directory
   - Generates lab interface at `jupyterlite/lab/index.html`

3. **Quarto Render**
   - Renders all `.qmd` files to HTML
   - Copies JupyterLite application to `_site/jupyterlite/`
   - Processes all tracks and documentation

4. **Deployment**
   - Uploads `_site/` directory as artifact
   - Deploys to GitHub Pages

## Critical Configuration

### Python Kernel Registration

The workflow registers the Python kernel **before** rendering:

```bash
python -m ipykernel install --user --name=python3
```

Without this, Quarto cannot execute Python code blocks and will fail to render interactive content.

### Quarto Version

The workflow uses **Quarto 1.7.33** to match the local development environment:

```yaml
- uses: quarto-dev/quarto-actions/setup@v2
  with:
    version: '1.7.33'
```

Using older versions (like 1.4.0) causes issues with modern Quarto features.

### Environment Variable

The `QUARTO_PYTHON` environment variable ensures Quarto uses the correct Python interpreter:

```yaml
env:
  QUARTO_PYTHON: python
```

### JupyterLite Build Order

**Critical**: JupyterLite MUST be built BEFORE `quarto render`. The workflow ensures this order:

```yaml
- name: Build JupyterLite environment
  run: |
    cd jupyterlite
    jupyter lite build --contents content
    cp -r _output/* .
    rm -rf _output
    cd ..

- name: Render Quarto site
  run: quarto render
```

This order is essential because:
- JupyterLite builds the application files (lab/, build/, etc.)
- Quarto copies `jupyterlite/**` resources to `_site/`
- If Quarto renders first, it copies an incomplete application

## Required Dependencies

### requirements.txt

Ensure these packages are in `requirements.txt`:

```txt
jupyterlite-core>=0.2.0
jupyterlite-pyodide-kernel>=0.2.0
jupyter-server
jupyterlab
ipykernel
pyyaml
matplotlib
numpy
pygame
```

**Note**: `jupyterlab` is required for JupyterLite to build the lab interface. Without it, JupyterLite only copies notebooks but doesn't create the application UI.

## Local Development

### Build Script

Use `render.sh` for local builds:

```bash
bash render.sh
```

This script:
1. Activates the virtual environment
2. Builds JupyterLite (if directory exists)
3. Renders the Quarto site

### Preview Site

Use `preview.sh` for live development:

```bash
bash preview.sh
```

This starts a local server with live reload.

### Manual Commands

If you need to run commands manually:

```bash
# 1. Build JupyterLite
cd jupyterlite
jupyter lite build --contents content
cp -r _output/* .
rm -rf _output
cd ..

# 2. Render site
QUARTO_PYTHON=./venv/bin/python quarto render

# 3. Preview
QUARTO_PYTHON=./venv/bin/python quarto preview
```

## Troubleshooting

### Issue: JupyterLite downloads .qmd file instead of launching

**Symptoms**:
- Clicking "Launch JupyterLite" downloads `jupyterlite.qmd`
- Browser shows file download instead of application

**Root Causes**:
1. **Missing from render list**: `jupyterlite.qmd` wasn't in `_quarto.yml` render list
2. **Missing JupyterLab dependency**: `jupyterlab` package not installed

**Solutions**:
1. Add `jupyterlite.qmd` to render list in `_quarto.yml`:
   ```yaml
   render:
     - "jupyterlite.qmd"
   ```

2. Install `jupyterlab`:
   ```bash
   pip install jupyterlab
   ```

3. Build JupyterLite BEFORE quarto render (see workflow order above)

### Issue: lab/index.html missing

**Symptoms**:
- 404 error when accessing `jupyterlite/lab/index.html`
- JupyterLite directory exists but incomplete

**Root Cause**:
- `jupyterlab` package not installed
- JupyterLite cannot build lab interface without JupyterLab

**Solution**:
```bash
pip install jupyterlab
jupyter lite build --contents content
```

### Issue: Build order problems

**Symptoms**:
- JupyterLite works locally but not on GitHub Pages
- Application files missing in deployment

**Root Cause**:
- Quarto render runs before JupyterLite build
- Quarto copies incomplete jupyterlite/ directory

**Solution**:
Ensure workflow builds JupyterLite first (see "JupyterLite Build Order" section above)

### Issue: Python execution errors

**Symptoms**:
- `Error: Kernel error`
- Code blocks don't execute

**Root Cause**:
- IPython kernel not registered
- Wrong Python version

**Solution**:
```bash
python -m ipykernel install --user --name=python3
```

## File Structure

After a successful build, the `_site/` directory should contain:

```
_site/
├── index.html
├── jupyterlite.html              # Info page
├── jupyterlite/
│   ├── index.html                # JupyterLite root
│   ├── lab/
│   │   └── index.html            # Lab interface (CRITICAL)
│   ├── build/                    # Application assets (600+ files)
│   ├── files/                    # Notebook files
│   ├── api/                      # API endpoints
│   └── [other directories]
├── tracks/
│   ├── python/
│   ├── rust/
│   └── pygame/
└── [other site files]
```

## Verification

After deployment, verify:

1. **Site loads**: Visit the GitHub Pages URL
2. **JupyterLite page renders**: Check `jupyterlite.html` displays (not downloads)
3. **Lab launches**: Click "Launch JupyterLite" opens application
4. **Notebooks load**: Verify notebooks appear in file browser
5. **Python executes**: Run code cells successfully

## GitHub Pages Settings

In your repository settings:

1. Go to **Settings** → **Pages**
2. **Source**: GitHub Actions
3. **Branch**: (not applicable for Actions deployment)

The workflow will automatically deploy to `https://<username>.github.io/<repository>/`

## Performance Notes

- Initial page load includes ~15MB of application assets
- Subsequent visits use browser cache
- Python runtime (Pyodide) downloads on first execution
- Total initial download: ~50-100MB depending on packages

## Maintenance

### Update dependencies

Edit `requirements.txt` and push to trigger rebuild:

```bash
git add requirements.txt
git commit -m "Update dependencies"
git push
```

### Add new notebooks

1. Add `.ipynb` files to `jupyterlite/content/`
2. Push changes (workflow rebuilds JupyterLite)
3. New notebooks appear in JupyterLite file browser

### Update JupyterLite

To update JupyterLite version:

```bash
pip install --upgrade jupyterlite-core jupyterlite-pyodide-kernel
```

Update `requirements.txt` with new versions.

## Common Errors

### "No module named 'ipykernel'"

**Fix**: Add to workflow before render:
```yaml
- run: python -m ipykernel install --user --name=python3
```

### "jupyter-lite: command not found"

**Fix**: Ensure `jupyterlite-core` is in `requirements.txt`

### "Unable to find jupyterlite-app tarball"

**Fix**: Install `jupyterlab` package (required for app bundle):
```bash
pip install jupyterlab
```

### Build succeeds but lab/ missing

**Fix**: Install `jupyterlab` and rebuild:
```bash
pip install jupyterlab
cd jupyterlite
jupyter lite build --contents content
cp -r _output/* .
```

## Support

For deployment issues:
- Check [GitHub Actions logs](../../actions)
- Verify all dependencies are installed
- Ensure build order is correct (JupyterLite → Quarto)
- Compare with this guide

For JupyterLite issues:
- Visit [JupyterLite documentation](https://jupyterlite.readthedocs.io/)
- Check browser console for errors
- Verify Python packages are available in Pyodide

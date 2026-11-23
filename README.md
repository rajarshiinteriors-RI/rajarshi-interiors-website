# Rajarshi Interiors — Website V3 (Pages CMS)

## What is included
- Your original Rajarshi Interiors logo and premium website design.
- Sample interior photos, clearly labelled as inspiration, **not your completed work**.
- Editable company information, services, hero/about photos and gallery using Pages CMS.
- GitHub Actions deployment to GitHub Pages. No custom server or database.

## Setup (one-time)
1. Create a GitHub account with two-factor authentication enabled.
2. Create a **public** repository, e.g. `rajarshi-interiors-website`. GitHub Pages on GitHub Free generally requires a public repository.
3. Upload **all files and folders** in this ZIP to the repository root, including hidden `.pages.yml` and `.github` folder. Do not upload the ZIP as a single file.
4. In GitHub repository **Settings → Pages → Build and deployment**, select **GitHub Actions** as source.
5. Check the **Actions** tab for the `Publish Rajarshi Interiors website` workflow. It should publish to a GitHub Pages address, such as `https://YOUR-USERNAME.github.io/rajarshi-interiors-website/`.
6. Open https://app.pagescms.org/ and sign in with GitHub. Install/authorize the Pages CMS GitHub App **only for this repository** if prompted. Open the repository and edit **Website settings** or **Project gallery**.
7. Save your edits. Pages CMS commits content to GitHub; the publishing workflow runs and updates the live website. Wait for the workflow to finish.

## IMPORTANT: URL and images
This website uses relative image URLs for its initial images, but the CMS upload path is `/assets/uploads`, intended for the **custom domain** `rajarshiinteriors.com` (or a root-domain GitHub Pages site). On a project subpath (`username.github.io/repository/`), uploaded images beginning with `/assets/` will point to the wrong location. **Before using CMS-uploaded images on a project subpath**, either connect your custom domain or change the `.pages.yml` media `output` to `/repository-name/assets/uploads` and use the corresponding URL prefix for uploaded images. The original sample images work on project subpaths.

## Add a real project
1. In Pages CMS → Media, upload a photo.
2. Go to Project gallery → New, set title, category, photo, **Sample inspiration image = off**, **Show on website = on**.
3. Save and wait for deployment.
4. Remove the sample entries when ready. Never label sample images as completed company projects.

## Update contact details
Open Website settings in Pages CMS. Add your phone, WhatsApp (e.g. 919876543210), email and location. Save. The enquiry form uses the visitor's email application; it is **not a database-backed form**, so it will not reliably capture every enquiry. WhatsApp button appears only after you configure your WhatsApp number.

## Security and operating costs
- Pages CMS uses GitHub authentication; there is **no /admin password** hosted on your public website.
- Limit the Pages CMS GitHub App to this repository, use 2FA and grant write access only to trusted editors.
- Public repository means **all website content and photos are public**. Do not upload private customer details or photos without permission.
- GitHub Pages and Pages CMS may be free within provider plan limits; domain registration and renewal are separate.
- Git history retains previous versions and can help roll back changes.
- Publishing requires your GitHub login and permissions; nothing is connected or deployed yet.

## Local preview
Run `python3 build.py`, then `python3 -m http.server 8000` from this directory and visit `http://localhost:8000`.
You can also double-click `index.html` for the bundled preview. CMS edits will need `python3 build.py` to refresh local `site-data.js`.

## Custom domain
Once you own `rajarshiinteriors.com`, configure it under GitHub repository Settings → Pages → Custom domain, add the DNS records GitHub specifies, and enable HTTPS when available. Do not assume the domain is available until you register it.

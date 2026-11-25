# Medienwerkstatt website

Static public information and legal pages for the Medienwerkstatt media workflow.

## GitHub Pages

The project contains only static HTML, CSS and a small deployment-time renderer. Pages is deployed manually with the `Deploy GitHub Pages` workflow.

Expected project-site URL after publishing:

```text
https://uruguru.github.io/medienwerkstatt-site/
```

The operator name is deliberately excluded from Git history. Configure this GitHub Actions repository secret before the first deployment:

- `PROVIDER_NAME`

The workflow renders `imprint.template.html` into the public `imprint.html` only inside the deployment artifact. The resulting contact page is public, but the name is not committed to the repository. A postal address is intentionally not deployed; whether one is legally required for the operator's actual use must be assessed separately.

For TikTok URL-prefix verification, place the signature file supplied by TikTok at the exact requested path, commit it, and verify that the resulting HTTPS URL is publicly accessible.

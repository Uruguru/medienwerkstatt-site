# Medienwerkstatt website

Static public information and legal pages for the Medienwerkstatt media workflow.

## GitHub Pages

The project contains only static HTML, CSS and a small deployment-time renderer. Pages is deployed manually with the `Deploy GitHub Pages` workflow.

Expected project-site URL after publishing:

```text
https://uruguru.github.io/medienwerkstatt-site/
```

Provider details are deliberately excluded from Git history. Configure these GitHub Actions repository secrets before the first deployment:

- `PROVIDER_NAME`
- `PROVIDER_STREET`
- `PROVIDER_CITY`
- `PROVIDER_COUNTRY`

The workflow renders `imprint.template.html` into the public `imprint.html` only inside the deployment artifact. The resulting page is public, but the address is not committed to the repository.

For TikTok URL-prefix verification, place the signature file supplied by TikTok at the exact requested path, commit it, and verify that the resulting HTTPS URL is publicly accessible.

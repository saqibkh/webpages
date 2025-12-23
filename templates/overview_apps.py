# templates/overview_apps.py
from data.personal_info import name, github, linkedin

def generate_apps_overview(apps, page_title="Apps Overview", navbar=""):
    """
    Generates an Apps Overview page where each app has its own folder with index.html.
    """
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<link rel="stylesheet" href="../assets/css/styles.css">
</head>
<body>
<header><h1>{page_title}</h1></header>

{navbar}
<section>
"""

    for app in apps:
        platform_folder = app.get("platform", "").lower()
        # Build the folder path: platform/app_name/
        folder = f"{platform_folder}/{app['name'].lower().replace(' ', '_')}/" if platform_folder else f"{app['name'].lower().replace(' ', '_')}/"

        html += f"""
    <div class="card">
        <strong>{app.get('name', 'No Name')}</strong>
        <p>{app.get('short_description', '')}</p>
        <p>{app.get('full_description', '')}</p>
        <p>Local Page: <a href="{folder}" target="_blank">{app.get('name', 'Link')}</a></p>
"""

        play_store_link = app.get("play_store_link", "")
        if play_store_link:
            html += f'        <p>Play Store: <a href="{play_store_link}" target="_blank">View on Play Store</a></p>\n'

        html += "    </div>\n"

    html += f"""
</section>
<footer>
    &copy; 2025 {name} | <a href="{github}" target="_blank">GitHub</a> | <a href="{linkedin}" target="_blank">LinkedIn</a>
</footer>
</body>
</html>
"""
    return html


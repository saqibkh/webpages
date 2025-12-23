from utils.file_utils import setup_directories, write_file
from utils.css_template import css_content
from templates.about_page import generate_about_me_page
from templates.project_page import generate_project_page
from templates.navbar import generate_navbar
from data.personal_info import name, github, linkedin
from data.projects_data import projects
from data.apps_data import apps

def generate_overview(items, page_title, is_project=True):
    """
    Generic overview page generator.
    items: list of dictionaries (projects or apps)
    page_title: string, page heading
    is_project: if True, assume it's projects; otherwise, apps
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
""" + generate_navbar() + "<section>"

    for item in items:
        filename = item.get('name', 'unknown').lower().replace(" ", "_") + ".html"

        if item.get("type") == "application" or not is_project:
            html += f"""
        <div class="card">
            <strong>{item.get('name', 'No Name')}</strong>
            <p>{item.get('description', '')}</p>
            <p>{item.get('details', '')}</p>
            <p>Visit: <a href="{item.get('link', '#')}" target="_blank">{item.get('visit', 'Link')}</a></p>
        </div>
            """
        else:
            html += f"""
        <div class="card">
            <strong>{item.get('name', 'No Name')}</strong>
            <p>{item.get('description', '')}</p>
            <p>Visit: <a href="{item.get('link', '#')}" target="_blank">{item.get('visit', 'Link')}</a></p>
            <p><a href="{filename}">Read More</a></p>
        </div>
            """

    html += f"""
</section>
<footer>
    &copy; 2025 {name} | <a href="{github}" target="_blank">GitHub</a> | <a href="{linkedin}" target="_blank">LinkedIn</a>
</footer>
</body>
</html>
"""
    return html


def main():
    # Setup directories
    setup_directories()

    # Write CSS
    write_file("assets/css/styles.css", css_content)

    # Generate About Me page
    write_file("index.html", generate_about_me_page())
    print("Generated index.html (About Me page)")

    # Generate individual project pages
    for proj in projects:
        if proj.get("type") == "application":
            print(f"Skipped generating page for {proj['name']} (manual file in place)")
            continue
        filename = proj['name'].lower().replace(" ", "_") + ".html"
        write_file(f"projects/{filename}", generate_project_page(proj))
        print(f"Generated projects/{filename}")

    # Generate projects overview page
    write_file("projects/index.html", generate_overview(projects, "Projects Overview", is_project=True))
    print("Generated projects/index.html (Projects Overview page)")

    # Generate apps overview page
    write_file("apps/index.html", generate_overview(apps, "Apps Overview", is_project=False))
    print("Generated apps/index.html (Apps Overview page)")


if __name__ == "__main__":
    main()


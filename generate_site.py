from utils.file_utils import setup_directories, write_file
from utils.css_template import css_content
from templates.about_page import generate_about_me_page
from templates.project_page import generate_project_page
from templates.navbar import generate_navbar
from data.personal_info import name, github, linkedin
from data.projects_data import projects

def generate_projects_overview(projects):
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Projects</title>
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
<header><h1>Projects</h1></header>
""" + generate_navbar() + "<section>"

    for proj in projects:
        if proj.get("type") == "application":
          filename = proj['name'].lower().replace(" ", "_") + ".html"
          html += f"""
          <div class="card">
              <strong>{proj['name']}</strong>
              <p>{proj['description']}</p>
              <p>{proj['details']}</p>
              <p>Visit: <a href="{proj['link']}" target="_blank">{proj['Visit']}</a></p>
          </div>
          """
        else:
          filename = proj['name'].lower().replace(" ", "_") + ".html"
          html += f"""
          <div class="card">
              <strong>{proj['name']}</strong>
              <p>{proj['description']}</p>
              <p>Visit: <a href="{proj['link']}" target="_blank">{proj['Visit']}</a></p>
              <p><a href="projects/{filename}">Read More</a></p>
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
    write_file("projects.html", generate_projects_overview(projects))
    print("Generated projects.html (Projects Overview page)")

if __name__ == "__main__":
    main()

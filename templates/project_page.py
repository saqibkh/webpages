from data.personal_info import name, github, linkedin
from templates.navbar import generate_navbar

def generate_project_page(proj, navbar=""):
    """
    Generates an individual project page.
    :param proj: dictionary with project info
    :param navbar: HTML string for the navigation bar
    """
    filename = proj.get('name', 'unknown').lower().replace(" ", "_") + ".html"

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{proj.get('name', 'Project')}</title>
<link rel="stylesheet" href="../assets/css/styles.css">
</head>
<body>
<header><h1>{proj.get('name', 'Project')}</h1></header>

{navbar}

<section>
    <p>{proj.get('description', '')}</p>
    <p>{proj.get('details', '')}</p>
    <p>Visit: <a href="{proj.get('link', '#')}" target="_blank">{proj.get('visit', 'Link')}</a></p>
</section>

<footer>
    &copy; 2025 Your Name | <a href="https://github.com/yourgithub" target="_blank">GitHub</a> | <a href="https://www.linkedin.com/in/yourlinkedin" target="_blank">LinkedIn</a>
</footer>
</body>
</html>
"""
    return html


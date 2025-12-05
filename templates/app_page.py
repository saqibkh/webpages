from data.personal_info import name, github, linkedin
from templates.navbar import generate_navbar

def generate_app_page(app):
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{project['name']}</title>
<link rel="stylesheet" href="../assets/css/styles.css">
</head>
<body>
<header>
    <h1>{project['name']}</h1>
</header>

{generate_navbar("../")}

<section>
    <div class="card">
        <p>{project['details']}</p>
        <p>Visit: <a href="{project['link']}" target="_blank">{project['link']}</a></p>
    </div>
</section>

<footer>
    &copy; 2025 {name} | <a href="{github}" target="_blank">GitHub</a> | <a href="{linkedin}" target="_blank">LinkedIn</a>
</footer>
</body>
</html>
"""
    return html

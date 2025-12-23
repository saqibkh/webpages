from data.personal_info import name, github, linkedin

def generate_app_page(app, platform_folder="", navbar=""):
    """
    Generates an individual app page.
    
    :param app: dictionary with app info
    :param platform_folder: folder where the page will reside (e.g., 'android'), used to adjust relative navbar paths
    :param navbar: HTML string for the navigation bar
    """
    # Use empty strings as fallback if keys are missing
    app_name = app.get('name', 'App')
    short_description = app.get('short_description', '')
    full_description = app.get('full_description', '')
    link = app.get('link', '#')
    platform = app.get('platform', 'Unknown')
    app_type = app.get('type', 'App')

    # Adjust relative navbar path based on platform folder
    if platform_folder:
        navbar_path = "../"
    else:
        navbar_path = ""

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{app_name}</title>
<link rel="stylesheet" href="{navbar_path}../assets/css/styles.css">
</head>
<body>
<header>
    <h1>{app_name}</h1>
</header>

{navbar or ''}

<section>
    <div class="card">
        <h2>Short Description</h2>
        <p>{short_description}</p>

        <h2>Full Description</h2>
        <p>{full_description or 'No full description provided.'}</p>

        <p><strong>Platform:</strong> {platform}</p>
        <p><strong>Type:</strong> {app_type}</p>
        <p><strong>Visit:</strong> <a href="{link}" target="_blank">{link}</a></p>
    </div>
</section>

<footer>
    &copy; 2025 {name} | <a href="{github}" target="_blank">GitHub</a> | <a href="{linkedin}" target="_blank">LinkedIn</a>
</footer>
</body>
</html>
"""
    return html


def generate_navbar(relative_path=""):
    return f"""
<nav>
    <a href="{relative_path}">About Me</a>
    <a href="{relative_path}projects">Projects</a>
    <a href="{relative_path}apps">Apps</a>
</nav>
<style>
nav {{ display:flex; justify-content:center; background:white; box-shadow:0 2px 5px rgba(0,0,0,0.1); position:sticky; top:0; z-index:100; }}
nav a {{ margin:15px 20px; text-decoration:none; color:#1b5e20; font-weight:bold; }}
nav a:hover {{ color:#2e7d32; }}
</style>
"""

import os

# ========================
# Personal Info & Data
# ========================
name = "Saqib Khan"
github = "https://github.com/saqibkh"
linkedin = "https://www.linkedin.com/in/saqib-khan-2a0ab164/"
email = "saqibkhan@utexas.edu"
location = "USA"
photo = "assets/img/profile.jpg"

bio = "I am Saqib Khan, an Electrical and Computer Engineer with a passion for high-performance computing and GPU memory validation."

education = [
    {"degree": "Master's in Electrical and Computer Engineering", "school": "UT Austin", "year": "2019"},
    {"degree": "Bachelor's in Electrical and Computer Engineering", "school": "UT Austin", "year": "2015"}
]

experience = [
    {"role": "HBM Memory Validation Engineer", "company": "AMD", "details": "Worked on GPU HBM memory validation."},
    {"role": "Processor Simulation Engineer", "company": "IBM", "details": "Simulated CPU architectures for performance verification."},
    {"role": "Firmware Developer", "company": "IBM", "details": "Developed and optimized embedded firmware."}
]

skills = {
    "Programming Languages": ["Python", "C", "C++", "Verilog", "Bash/Shell"],
    "Tools & Technologies": ["CUDA", "ROCm", "Git", "Linux", "Jupyter", "PyTorch", "HPC Simulation Tools"]
}

hobbies = ["Spending time with my son", "Playing cricket", "Playing football"]

projects = [
    {
        "name": "Cloud Sound YouTube Channel",
        "description": "My personal YouTube channel where I post tech-related content.",
        "link": "https://www.youtube.com/@Cloud__Sound",
        "details": "This project focuses on sharing high-quality tech tutorials and sound experiments."
    }
]

# ========================
# Helper Functions
# ========================
def generate_navbar(relative_path=""):
    return f"""
<nav>
    <a href="{relative_path}index.html">About Me</a>
    <a href="{relative_path}projects.html">Projects</a>
</nav>
<style>
nav {{ display:flex; justify-content:center; background:white; box-shadow:0 2px 5px rgba(0,0,0,0.1); position:sticky; top:0; z-index:100; }}
nav a {{ margin:15px 20px; text-decoration:none; color:#1b5e20; font-weight:bold; }}
nav a:hover {{ color:#2e7d32; }}
</style>
"""

def generate_about_me_page():
    education_html = ''.join([f"<li><strong>{e['degree']}</strong>, {e['school']} ({e['year']})</li>" for e in education])
    experience_html = ''.join([f"<p><strong>{exp['role']} at {exp['company']}</strong><br>{exp['details']}</p>" for exp in experience])
    skills_html = ''.join([f"<tr><td>{cat}</td><td>{', '.join(items)}</td></tr>" for cat, items in skills.items()])
    hobbies_html = ''.join([f"<li>{h}</li>" for h in hobbies])

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} - About Me</title>
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
<header>
    <img src="{photo}" alt="Profile Photo">
    <h1>{name}</h1>
    <p><a href="{github}" target="_blank">GitHub</a> | <a href="{linkedin}" target="_blank">LinkedIn</a></p>
</header>

{generate_navbar()}

<section>
    <h2>About Me</h2>
    <div class="card">{bio}</div>
</section>

<section>
    <h2>Education</h2>
    <div class="card"><ul>{education_html}</ul></div>
</section>

<section>
    <h2>Experience</h2>
    <div class="card">{experience_html}</div>
</section>

<section>
    <h2>Skills</h2>
    <div class="card">
        <table>
            <tr><th>Category</th><th>Skills</th></tr>
            {skills_html}
        </table>
    </div>
</section>

<section>
    <h2>Contact</h2>
    <div class="card">
        <p>Email: <a href='mailto:{email}'>{email}</a></p>
    </div>
</section>

<section>
    <h2>Hobbies / Fun</h2>
    <div class="card">
        <ul>{hobbies_html}</ul>
    </div>
</section>

<footer>
    &copy; 2025 {name} | Location: {location} | <a href="{github}" target="_blank">GitHub</a> | <a href="{linkedin}" target="_blank">LinkedIn</a>
</footer>
</body>
</html>
"""
    return html

def generate_project_page(project):
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

# ========================
# Setup directories
# ========================
os.makedirs("assets/css", exist_ok=True)
os.makedirs("assets/img", exist_ok=True)
os.makedirs("projects", exist_ok=True)

# Write CSS
css_content = """
body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin:0; background:#f9f9f9; color:#333; }
header { text-align:center; background:linear-gradient(135deg,#4CAF50,#81C784); color:white; padding:60px 20px; }
header img { border-radius:50%; width:160px; height:160px; object-fit:cover; border:4px solid white; }
section { max-width:1000px; margin:40px auto; padding:20px; }
h2 { color:#4CAF50; margin-bottom:20px; border-bottom:3px solid #4CAF50; padding-bottom:5px; }
.card { background:white; padding:20px; margin-bottom:20px; border-radius:12px; box-shadow:0 4px 12px rgba(0,0,0,0.1); }
.card:hover { transform:translateY(-5px); transition:0.3s; }
table { width:100%; border-collapse:collapse; }
th, td { border:1px solid #ddd; padding:12px; }
th { background-color:#4CAF50; color:white; }
footer { text-align:center; padding:20px; background-color:#e0e0e0; }
a { color:#1b5e20; text-decoration:none; font-weight:bold; }
a:hover { text-decoration:underline; }
"""
with open("assets/css/styles.css", "w") as f:
    f.write(css_content)

# ========================
# Generate index.html (About Me)
# ========================
with open("index.html", "w", encoding="utf-8") as f:
    f.write(generate_about_me_page())
print("Generated index.html (About Me page)")

# ========================
# Generate individual project pages
# ========================
for proj in projects:
    filename = proj['name'].lower().replace(" ", "_") + ".html"
    filepath = os.path.join("projects", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(generate_project_page(proj))
    print(f"Generated {filepath}")

# ========================
# Generate projects.html overview
# ========================
projects_overview_html = """
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
    filename = proj['name'].lower().replace(" ", "_") + ".html"
    projects_overview_html += f"""
    <div class="card">
        <strong>{proj['name']}</strong>
        <p>{proj['description']}</p>
        <p><a href="projects/{filename}">Read More</a></p>
    </div>
    """

projects_overview_html += """
</section>
<footer>
    &copy; 2025 Saqib Khan | <a href="https://github.com/saqibkh" target="_blank">GitHub</a> | <a href="https://www.linkedin.com/in/saqib-khan-2a0ab164/" target="_blank">LinkedIn</a>
</footer>
</body>
</html>
"""

with open("projects.html", "w", encoding="utf-8") as f:
    f.write(projects_overview_html)
print("Generated projects.html (Projects Overview page)")

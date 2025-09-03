from data.personal_info import name, github, linkedin, email, location, photo, bio, education, skills, hobbies
from data.experience_data import experience
from templates.navbar import generate_navbar

def generate_about_me_page():
    # Education HTML
    education_html = ''.join([f"<li><strong>{e['degree']}</strong>, {e['school']} ({e['year']})</li>" for e in education])

    # Experience HTML with dates on the far right
    experience_html = ''.join([
        f"""
        <div class="exp-row">
            <span class="exp-role">{exp['role']} at {exp['company']}</span>
            <span class="exp-dates">{exp['start_date']} – {exp['end_date']}</span>
        </div>
        <p>{exp['details']}</p>
        """
        for exp in experience
    ])

    # Skills HTML
    skills_html = ''.join([f"<tr><td>{cat}</td><td>{', '.join(items)}</td></tr>" for cat, items in skills.items()])

    # Hobbies HTML
    hobbies_html = ''.join([f"<li>{h}</li>" for h in hobbies])

    # Full HTML page
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

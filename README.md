This project is a modular Python script to generate a personal portfolio website, including an About Me page, Projects Overview page, and individual project pages. It uses structured data and templates to make maintenance easy.



📂 Project Structure

portfolio\_site/

│

├── data/

│   ├── personal\_info.py        # Personal info, bio, education, skills, hobbies

│   └── experience\_data.py      # Job experience with roles, companies, and dates

│   └── projects\_data.py        # List of projects with details and links

│

├── templates/

│   ├── navbar.py               # HTML navbar generator

│   ├── about\_page.py           # Function to generate About Me page

│   └── project\_page.py         # Function to generate individual project pages

│

├── utils/

│   ├── file\_utils.py           # Directory creation \& file writing utilities

│   └── css\_template.py         # CSS content for the site

│

├── generate\_site.py            # Main script to generate the entire website

└── README.md                   # This documentation file



🛠 Features



Modular structure separating data, templates, and utilities.



Generates index.html (About Me page) with bio, education, experience, skills, hobbies, and contact info.



Generates projects.html (Projects overview page).



Generates individual project pages in the projects/ folder.



Responsive and clean CSS styling included.



Experience section shows roles left-aligned and dates right-aligned.



⚙ Dependencies



Python 3.x (tested with Python 3.8+).



No external Python packages required.



🚀 How to Run



Clone the repository (or copy the files to your local folder):



git clone <repository\_url>

cd portfolio\_site





Ensure your assets folder exists (images will be stored in assets/img/):



mkdir -p assets/img





Add your profile photo to assets/img/profile.jpg.



Run the generator script:



python generate\_site.py





View generated pages:



index.html → About Me page



projects.html → Projects overview page



projects/<project\_name>.html → Individual project pages



Open them in a browser to verify everything renders correctly.



✏️ Customization



Update personal info: data/personal\_info.py



Update experience: data/experience\_data.py (roles, companies, dates, descriptions)



Update projects: data/projects\_data.py (name, description, link, details)



Modify styling: utils/css\_template.py



Modify templates: templates/ folder (about\_page.py, project\_page.py, navbar.py)



✅ Notes



Dates in the experience section are aligned to the far right using CSS flex layout.



All pages use a consistent navbar and footer linking to GitHub and LinkedIn.



Modular structure makes it easy to add more projects or update content without touching the generator code.



🖼 Example



After running generate\_site.py, the folder structure will look like this:



index.html

projects.html

projects/cloud\_sound\_youtube\_channel.html

assets/

&nbsp;   css/styles.css

&nbsp;   img/profile.jpg





Open index.html in a browser to see the fully generated portfolio.


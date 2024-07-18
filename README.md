
SummaryTube is a Django-based web application that allows users to enter a YouTube link and receive a summarized version of the video content.
 
Features
Simple UI: Easy-to-use interface for entering YouTube links and viewing summarized content.
Text Summarization: Automatically generates concise summaries of YouTube videos.
Technologies Used
Django: Web framework for building the application backend.
Python: Programming language used for backend logic.
Bootstrap: Frontend framework for designing responsive and clean UI.
HTML/CSS: Standard web technologies for structuring and styling the frontend.
Installation Instructions
To set up and run SummaryTube locally, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/your-username/SummaryTube.git
cd SummaryTube
Set up a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Note: You will need to install the YouTube Data API client library. You can do this using pip:

bash
Copy code
pip install google-api-python-client
Run migrations and start the Django development server:

bash
Copy code
python manage.py migrate
python manage.py runserver
Access SummaryTube in your web browser at http://localhost:8000/.

Contact Information
For support or feedback, you can reach out via email at mahikaa2005jain@gmail.com.

# Book Buddy

Book Buddy is a web application for book lovers, designed to help users manage their book libraries, track reading progress, and engage with books through statistics and ratings.

## Features

### Core Features:
- **User Authentication**: Login via Google OAuth without storing personal data.
- **Book Library**:
  - Add books with details like title, format (Physical, Kindle, Audiobook), and total pages.
  - Track books' status: To Be Read (TBR), Reading, or Read.
- **Reading Progress**:
  - Set reading timers (10, 15, 20+ minutes).
  - Track pages read during a session.
  - Provide initial ratings and decide whether to continue reading.
- **Statistics**:
  - Track total time spent reading.
  - View monthly reading progress and completed books.
  - Check individual book statistics, including time spent, reading sessions, and rating progress.

### Planned Features:
- **Book Clubs**: Create groups, join reading marathons, and engage in discussions.
- **Advanced Stats**: Visualize reading trends and insights.

---

## Installation

### Prerequisites:
- Python 3.8+

### Steps:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/book-buddy.git
   cd book-buddy
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the App**:
   Open your browser and visit `http://127.0.0.1:8000/`.

---

## Usage

### Adding Books:
1. Log in using Google.
2. Navigate to the "Add Book" page.
3. Fill in details like title, format, and total pages.

### Tracking Progress:
1. Start a reading session by setting a timer.
2. Log pages read and provide a rating after each session.

### Viewing Statistics:
- Check your monthly progress and total reading time on the main page.
- View individual book stats after marking them as "Read."

---

## Technology Stack

- **Backend**: Django
- **Frontend**: HTML/CSS (Django templates)
- **Authentication**: Django-Allauth with Google OAuth
- **Database**: SQLite (can be upgraded to PostgreSQL)

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your branch.
4. Open a pull request with a detailed description of your changes.

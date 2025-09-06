
# NikeProject

## Setup Instructions

1. Clone the repository:
   sh
   git clone <repo-url>
   cd nikeProject
   
2. Create and activate a virtual environment:
   sh
   python3 -m venv .venv
   source .venv/bin/activate
   
3. Install dependencies:
   sh
   pip install -r requirements_nike.txt
   
4. (For Playwright) Install browser drivers:
   sh
   playwright install
   
5. Run tests:
   sh
   pytest jb_60/project_nike/tests/
   

## Notes
- Ensure all __init__.py files are present in package directories.
- For any issues, check the README or contact the project owner.
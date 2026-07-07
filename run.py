# run.py
from flask import redirect, url_for
from app import create_app

# Generate the configured app instance from our factory
app = create_app()

# ----------------------------------------------------
# GLOBAL APP ROOT REDIRECT (Eliminates the 404 Error)
# ----------------------------------------------------
@app.route('/')
def global_root_fallback():
    """
    Captures requests to the base URL (/) and seamlessly forwards 
    the browser context straight to the main blueprint's login screen.
    """
    return redirect(url_for('main.login'))

if __name__ == '__main__':
    # Run the server in debug mode so it auto-reloads when you change code
    app.run(debug=True)
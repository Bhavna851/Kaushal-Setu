
# app/routes.py
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from app import db
from app.models import User, Profile, Internship, ApplicationTracker
from app.matching_engine import get_top_recommendations
from werkzeug.security import generate_password_hash, check_password_hash


main_blueprint = Blueprint('main', __name__)


# ----------------------------------------------------
# ABOUT PAGE
# ----------------------------------------------------

@main_blueprint.route('/')
def about():
    return render_template('about.html')


# ----------------------------------------------------
# SIGNUP
# ----------------------------------------------------

@main_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('full_name')
        email = request.form.get('email')
        password = request.form.get('password')

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash('Email already registered!', 'danger')
            return redirect(url_for('main.signup'))

        new_user = User(
            full_name=name,
            email=email,
            password_hash=generate_password_hash(password)
        )

        db.session.add(new_user)
        db.session.commit()

        # Empty profile creation
        new_profile = Profile(
            user_id=new_user.id,
            skills="",
            education="",
            city="",
            state=""
        )

        db.session.add(new_profile)
        db.session.commit()

        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('main.login'))

    return render_template('signup.html')


# ----------------------------------------------------
# LOGIN
# ----------------------------------------------------

@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):

            session['user_id'] = user.id
            session['user_name'] = user.full_name
            session['email'] = user.email

            flash(f'Welcome back, {user.full_name}!', 'success')

            profile = Profile.query.filter_by(user_id=user.id).first()

            if not profile or not all([
                profile.skills,
                profile.education,
                profile.city,
                profile.state
            ]):
                return redirect(url_for('main.profile'))

            return redirect(url_for('main.dashboard'))

        flash('Invalid email or password!', 'danger')
        return redirect(url_for('main.login'))

    return render_template('login.html')

# ----------------------------------------------------
# LOGOUT
# ----------------------------------------------------

@main_blueprint.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('main.login'))


# ----------------------------------------------------
# DASHBOARD
# ----------------------------------------------------

@main_blueprint.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    user_id = session['user_id']

    profile = Profile.query.filter_by(user_id=user_id).first()

    if not profile:
        profile = Profile(
            user_id=user_id,
            skills="",
            education="",
            city="",
            state=""
        )

        db.session.add(profile)
        db.session.commit()


    # ----------------------------------------------------
    # SAVE PROFILE DETAILS
    # ----------------------------------------------------


    # ----------------------------------------------------
    # IMPORTANT FIX:
    # DO NOT SHOW RECOMMENDATIONS IF PROFILE INCOMPLETE
    # ----------------------------------------------------

    recommendations = []

    has_profile = all([
        profile.skills,
        profile.education,
        profile.city,
        profile.state
    ])


    # ONLY RUN ENGINE IF USER FILLED COMPLETE DETAILS
    if has_profile:

        all_jobs = Internship.query.all()
        print("Profile Skills:", profile.skills)
        print("Education:", profile.education)
        print("City:", profile.city)
        print("State:", profile.state)

        print("Total Jobs:", len(all_jobs))

        recommendations = get_top_recommendations(
            profile,
            all_jobs
        )
        print("Recommendations:", len(recommendations))

    return render_template(
        'dashboard.html',
        profile=profile,
        recommendations=recommendations,
        has_profile=has_profile
    )

# ----------------------------------------------------
# RESUME UPLOAD
# ----------------------------------------------------

@main_blueprint.route('/upload_resume', methods=['POST'])
def upload_resume():

    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    if 'resume' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['resume']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Allow only PDF files
    if not file.filename.lower().endswith(".pdf"):
        return jsonify({
            "success": False,
            "error": "Only PDF files are allowed."
        }), 400

    try:
        import PyPDF2

        pdf_reader = PyPDF2.PdfReader(file)

        extracted_text = ""

        for page in pdf_reader.pages:
            extracted_text += page.extract_text() or ""

        extracted_text = extracted_text.lower()

        skill_keywords = [
            'python',
            'html',
            'css',
            'javascript',
            'bootstrap',
            'excel',
            'typing',
            'accounting',
            'mechanical',
            'sql',
            'java',
            'c++'
        ]

        found_skills = []

        for skill in skill_keywords:
            if skill in extracted_text:
                found_skills.append(skill.title())

        profile = Profile.query.filter_by(user_id=session['user_id']).first()

        if not profile:
            profile = Profile(user_id=session['user_id'])
            db.session.add(profile)

        # Save resume filename
        profile.resume_filename = file.filename

        # Save extracted skills if found
        if found_skills:
            profile.skills = ", ".join(found_skills)

        db.session.commit()

        return jsonify({
            "success": True,
            "skills": profile.skills if profile.skills else "",
            "message": "Resume uploaded successfully."
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Resume parsing failed: {str(e)}"
        }), 500

# ----------------------------------------------------
# CHATBOT
# ----------------------------------------------------

@main_blueprint.route('/chatbot', methods=['POST'])
def chatbot():

    user_message = request.json.get('message', '').strip().lower()

    chat_step = session.get('chat_step', 0)

    chat_data = session.get('chat_data', {
        "skills": "",
        "education": "",
        "city": "",
        "state": "Madhya Pradesh"
    })


    # START
    if chat_step == 0 or user_message in ['hi', 'hello', 'start']:

        session['chat_step'] = 1

        session['chat_data'] = {
            "skills": "",
            "education": "",
            "city": "",
            "state": "Madhya Pradesh"
        }

        return jsonify({
            "reply": "👋 Hello! I will help you find internships.<br><br><b>Step 1:</b> What is your qualification? (B.Tech / Diploma / B.Com / B.Sc)"
        })


    # STEP 1
    elif chat_step == 1:

        chat_data['education'] = user_message.title()

        session['chat_data'] = chat_data
        session['chat_step'] = 2

        return jsonify({
            "reply": "📍 Great! Which district/city do you prefer for internship?"
        })


    # STEP 2
    elif chat_step == 2:

        chat_data['district'] = user_message.title()

        session['chat_data'] = chat_data
        session['chat_step'] = 3

        return jsonify({
            "reply": "💡 Nice! Tell me your main skill. Example: Python, Excel, HTML, Typing"
        })


    # STEP 3
    elif chat_step == 3:

        chat_data['skills'] = user_message.title()

        session.pop('chat_step', None)
        session.pop('chat_data', None)


        class TempProfile:
            def __init__(self, s, e, c, st):
                self.skills = s
                self.education = e
                self.city = c
                self.state = st


        profile = TempProfile(
            chat_data['skills'],
            chat_data['education'],
            chat_data['city'],
            chat_data['state']
        )

        all_jobs = Internship.query.all()

        top_matches = get_top_recommendations(profile, all_jobs)


        if not top_matches:
            return jsonify({
                "reply": "No internships found currently. Try again with different skills."
            })


        reply_html = "<b>🎯 Top Recommended Internships</b><br><br>"

        for item in top_matches:

            reply_html += f"""
            <div style='background:#ffffff;padding:12px;border-radius:10px;margin-bottom:10px;border-left:5px solid #003366;'>
                <b>{item['internship'].job_title}</b><br>
                🏢 {item['internship'].company_name}<br>
                📍 {item['internship'].city}<br>
                💵 ₹{item['internship'].stipend}/month<br>
                🎯 Match Score: <b>{item['total_score']}%</b>
            </div>
            """

        reply_html += "<br>Type <b>start</b> to search again."

        return jsonify({"reply": reply_html})


    return jsonify({
        "reply": "Type <b>start</b> to begin."
    })


# ----------------------------------------------------
# APPLY
# ----------------------------------------------------

@main_blueprint.route('/apply/<int:internship_id>')
def apply(internship_id):

    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    user_id = session['user_id']

    already = ApplicationTracker.query.filter_by(
        user_id=user_id,
        internship_id=internship_id
    ).first()

    internship = Internship.query.get_or_404(internship_id)

    if not already:
        application = ApplicationTracker(
            user_id=user_id,
            internship_id=internship_id,
            status="Applied"
        )

        db.session.add(application)
        db.session.commit()

    return redirect(internship.apply_link)

@main_blueprint.route('/reset_password', methods=['GET', 'POST'])
def reset_password():

    if request.method == 'POST':

        email = request.form.get('email')
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(email=email).first()

        if not user:
            flash('Email not found!', 'danger')
            return redirect(url_for('main.reset_password'))

        # Verify current password
        if not check_password_hash(user.password_hash, current_password):
            flash('Current password is incorrect!', 'danger')
            return redirect(url_for('main.reset_password'))

        # New password should not be same as current password
        if check_password_hash(user.password_hash, new_password):
            flash('New password cannot be the same as the current password!', 'warning')
            return redirect(url_for('main.reset_password'))

        # Confirm password check
        if new_password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('main.reset_password'))

        user.password_hash = generate_password_hash(new_password)
        db.session.commit()

        flash('Password updated successfully! Please login.', 'success')
        return redirect(url_for('main.login'))

    return render_template('reset_password.html')
@main_blueprint.route('/My_applications')
def My_applications():

    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    applications = ApplicationTracker.query.filter_by(
        user_id=session['user_id']
    ).all()

    return render_template(
        'My_applications.html',
        applications=applications
    )
@main_blueprint.route('/chat')
def chat_page():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    return render_template('chat.html')

# ----------------------------------------------------
# PROFILE
# ----------------------------------------------------


@main_blueprint.route('/profile', methods=['GET', 'POST'])
def profile():

    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    user_id = session['user_id']

    profile = Profile.query.filter_by(user_id=user_id).first()

    if not profile:
        profile = Profile(
            user_id=user_id,
            skills="",
            education="",
            city="",
            state=""
        )
        db.session.add(profile)
        db.session.commit()

    # -----------------------------------------
    # SAVE PROFILE
    # -----------------------------------------
    if request.method == "POST":

        profile.phone = request.form.get("phone")

        dob = request.form.get("dob")
        if dob:
            profile.dob = datetime.strptime(dob, "%Y-%m-%d").date()
        else:
            profile.dob = None

        profile.gender = request.form.get("gender")

        profile.education = request.form.get("education")
        profile.college = request.form.get("college")
        profile.branch = request.form.get("branch")
        profile.graduation_year = request.form.get("graduation_year")

        profile.skills = request.form.get("skills")
        profile.bio = request.form.get("bio")

        profile.linkedin = request.form.get("linkedin")
        profile.github = request.form.get("github")

        profile.city = request.form.get("city")
        profile.state = request.form.get("state")

        db.session.commit()

        flash("Profile Updated Successfully!", "success")
        return redirect(url_for("main.dashboard"))

    # -----------------------------------------
    # PROFILE COMPLETION
    # -----------------------------------------

    required_fields = [
        profile.phone,
        profile.dob,
        profile.gender,
        profile.education,
        profile.college,
        profile.branch,
        profile.graduation_year,
        profile.skills,
        profile.bio,
        profile.linkedin,
        profile.github,
        profile.city,
        profile.state,
        profile.resume_filename
    ]

    filled = sum(1 for field in required_fields if field)

    profile_completion = int((filled / len(required_fields)) * 100)

    return render_template(
        "profile.html",
        profile=profile,
        profile_completion=profile_completion,
        profile_complete=(profile_completion == 100)
    )

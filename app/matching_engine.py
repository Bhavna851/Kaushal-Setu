# app/matching_engine.py

def calculate_match_score(user_profile, internship):
    """
    Calculates a transparent percentage match score between a candidate and an internship.
    Weights: Skills (40%), Education (30%), Location (30%)
    """
    score = 0.0
    reason_breakdown = {
        "skills": 0,
        "education": 0,
        "location": 0
    }
    missing_skills = []

    # ----------------------------------------------------
    # 1. SKILL MATCHING LAYER (Weight: 40%)
    # ----------------------------------------------------
    # Normalize texts to lowercase and split into lists of separate words
    user_skills = [s.strip().lower() for s in (user_profile.skills or "").split(",") if s.strip()]
    required_skills = [s.strip().lower() for s in (internship.required_skills or "").split(",") if s.strip()]

    if required_skills:
        matched_skills = list(set([
    skill for skill in required_skills
    if skill in user_skills
]))
        # Calculate what fraction of the required skills the user has
        skill_fraction = len(matched_skills) / len(required_skills)
        skill_score = skill_fraction * 40.0
        
        score += skill_score
        reason_breakdown["skills"] = round(skill_score)
        
        # Track which skills the user is missing for the visual badge callout
        missing_skills = [skill.title() for skill in required_skills if skill not in user_skills]
    else:
        # If the internship requires no specific skills, give full points
        score += 40.0
        reason_breakdown["skills"] = 40

    # ----------------------------------------------------
    # 2. EDUCATION MATCHING LAYER (Weight: 30%)
    # ----------------------------------------------------
    user_edu = (user_profile.education or "").strip().lower()
    job_edu = (internship.required_education or "").strip().lower()

    if user_edu == job_edu or job_edu == "any graduate":
        score += 30.0
        reason_breakdown["education"] = 30
    else:
        reason_breakdown["education"] = 0

    # ----------------------------------------------------
    # 3. LOCATION MATCHING LAYER (Weight: 30%)
    # ----------------------------------------------------
    user_city = (user_profile.city or "").strip().lower()
    job_city = (internship.city  or "").strip().lower()
    
    user_state = (user_profile.state or "").strip().lower()
    job_state = (internship.state or "").strip().lower()

    if user_city == job_city:
        # Perfect city match gets full points
        score += 30.0
        reason_breakdown["location"] = 30
    elif user_state == job_state:
        # Same state but different city gets partial points (15 out of 30)
        score += 15.0
        reason_breakdown["location"] = 15
    else:
        reason_breakdown["location"] = 0

    return {
        "total_score": round(score),
        "breakdown": reason_breakdown,
        "missing_skills": missing_skills
    }


def get_top_recommendations(user_profile, all_internships):
    """
    Loops through all internships, scores them for the user,
    sorts them from highest to lowest, and returns ONLY the top 3 to 5 rows.
    """
    scored_list = []
    
    for internship in all_internships:
        match_result = calculate_match_score(user_profile, internship)
        
        # We append a unified packet containing the internship model and its calculated scores
        if match_result["total_score"] > 0:
          scored_list.append({
            "internship": internship,
            "total_score": match_result["total_score"],
            "breakdown": match_result["breakdown"],
            "missing_skills": match_result["missing_skills"]
        })
        
    # Sort the list descending based on total_score
    scored_list.sort(key=lambda x: x["total_score"], reverse=True)
    
    # Strictly enforce the SIH constraint: slice and return ONLY the top 3 to 5 options
    return scored_list[:5]
# seed.py
from app import create_app, db
from app.models import Internship

app = create_app()

def seed_database():

    with app.app_context():
        import os

        print("Database URI:", app.config["SQLALCHEMY_DATABASE_URI"])
        print("Instance path:", app.instance_path)
        print("Current working directory:", os.getcwd())

        db.session.query(Internship).delete()

        sample_internships = [

# =========================
# IT / SOFTWARE (25)
# =========================

{"company_name":"Microsoft","job_title":"Software Engineering Intern","sector":"IT","required_skills":"C++,DSA,OOP","required_education":"B.Tech","city":"Hyderabad","state":"Telangana","stipend":50000,"platform":"Microsoft Careers","apply_link":"https://careers.microsoft.com"},

{"company_name":"Google","job_title":"Software Engineering Intern","sector":"IT","required_skills":"Python,C++,DSA","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":80000,"platform":"Google Careers","apply_link":"https://careers.google.com"},

{"company_name":"Amazon","job_title":"Software Development Engineer Intern","sector":"IT","required_skills":"Java,DSA,OOP","required_education":"B.Tech","city":"Hyderabad","state":"Telangana","stipend":70000,"platform":"Amazon Jobs","apply_link":"https://www.amazon.jobs"},

{"company_name":"Adobe","job_title":"Software Engineer Intern","sector":"IT","required_skills":"C++,Java,OOP","required_education":"B.Tech","city":"Noida","state":"Uttar Pradesh","stipend":85000,"platform":"Adobe Careers","apply_link":"https://careers.adobe.com"},

{"company_name":"Oracle","job_title":"Database Developer Intern","sector":"IT","required_skills":"SQL,DBMS,Java","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":50000,"platform":"Oracle Careers","apply_link":"https://careers.oracle.com"},

{"company_name":"IBM","job_title":"Data Analyst Intern","sector":"IT","required_skills":"Python,SQL,Excel","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":35000,"platform":"IBM Careers","apply_link":"https://www.ibm.com/careers"},

{"company_name":"Infosys","job_title":"Python Developer Intern","sector":"IT","required_skills":"Python,SQL,Flask","required_education":"B.Tech","city":"Mysuru","state":"Karnataka","stipend":20000,"platform":"Infosys Careers","apply_link":"https://career.infosys.com"},

{"company_name":"TCS","job_title":"Frontend Developer Intern","sector":"IT","required_skills":"HTML,CSS,JavaScript","required_education":"B.Tech","city":"Pune","state":"Maharashtra","stipend":18000,"platform":"TCS Careers","apply_link":"https://www.tcs.com/careers"},

{"company_name":"Wipro","job_title":"Software Testing Intern","sector":"IT","required_skills":"Testing,Java,Selenium","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":18000,"platform":"Wipro Careers","apply_link":"https://careers.wipro.com"},

{"company_name":"Accenture","job_title":"Cloud Intern","sector":"IT","required_skills":"AWS,Cloud Basics,Linux","required_education":"B.Tech","city":"Pune","state":"Maharashtra","stipend":25000,"platform":"Accenture Careers","apply_link":"https://www.accenture.com/in-en/careers"},

{"company_name":"Capgemini","job_title":"Full Stack Intern","sector":"IT","required_skills":"Java,Spring Boot,SQL","required_education":"B.Tech","city":"Mumbai","state":"Maharashtra","stipend":22000,"platform":"Capgemini Careers","apply_link":"https://www.capgemini.com/careers"},

{"company_name":"Cognizant","job_title":"Programmer Analyst Intern","sector":"IT","required_skills":"Java,SQL,OOP","required_education":"B.Tech","city":"Chennai","state":"Tamil Nadu","stipend":22000,"platform":"Cognizant Careers","apply_link":"https://careers.cognizant.com"},

{"company_name":"Tech Mahindra","job_title":"Java Developer Intern","sector":"IT","required_skills":"Java,OOP,SQL","required_education":"B.Tech","city":"Pune","state":"Maharashtra","stipend":18000,"platform":"Tech Mahindra Careers","apply_link":"https://careers.techmahindra.com"},

{"company_name":"HCLTech","job_title":"Software Intern","sector":"IT","required_skills":"Python,Git,SQL","required_education":"B.Tech","city":"Noida","state":"Uttar Pradesh","stipend":20000,"platform":"HCL Careers","apply_link":"https://www.hcltech.com/careers"},

{"company_name":"Zoho","job_title":"Software Developer Intern","sector":"IT","required_skills":"C++,Java,DSA","required_education":"B.Tech","city":"Chennai","state":"Tamil Nadu","stipend":30000,"platform":"Zoho Careers","apply_link":"https://www.zoho.com/careers"},

{"company_name":"SAP","job_title":"Backend Developer Intern","sector":"IT","required_skills":"Java,Spring,SQL","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":45000,"platform":"SAP Careers","apply_link":"https://www.sap.com/careers"},

{"company_name":"Intel","job_title":"Software Engineering Intern","sector":"IT","required_skills":"C,C++,Python","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":55000,"platform":"Intel Careers","apply_link":"https://jobs.intel.com"},

{"company_name":"NVIDIA","job_title":"GPU Software Intern","sector":"IT","required_skills":"C++,Python,CUDA","required_education":"B.Tech","city":"Pune","state":"Maharashtra","stipend":65000,"platform":"NVIDIA Careers","apply_link":"https://www.nvidia.com/en-us/about-nvidia/careers"},

{"company_name":"Qualcomm","job_title":"Embedded Software Intern","sector":"IT","required_skills":"C,C++,Linux","required_education":"B.Tech","city":"Hyderabad","state":"Telangana","stipend":50000,"platform":"Qualcomm Careers","apply_link":"https://www.qualcomm.com/company/careers"},

{"company_name":"Cisco","job_title":"Network Software Intern","sector":"IT","required_skills":"Networking,Python,Linux","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":45000,"platform":"Cisco Careers","apply_link":"https://jobs.cisco.com"},

{"company_name":"Siemens","job_title":"Software Engineer Intern","sector":"IT","required_skills":"Python,C++,Git","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":35000,"platform":"Siemens Careers","apply_link":"https://new.siemens.com/global/en/company/jobs.html"},

{"company_name":"Bosch","job_title":"IoT Software Intern","sector":"IT","required_skills":"Python,C++,IoT","required_education":"B.Tech","city":"Coimbatore","state":"Tamil Nadu","stipend":30000,"platform":"Bosch Careers","apply_link":"https://www.bosch.in/careers"},

{"company_name":"PhonePe","job_title":"Backend Engineering Intern","sector":"IT","required_skills":"Java,Spring Boot,MySQL","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":60000,"platform":"PhonePe Careers","apply_link":"https://www.phonepe.com/careers"},

{"company_name":"Razorpay","job_title":"Software Engineering Intern","sector":"IT","required_skills":"Java,Python,DSA","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":65000,"platform":"Razorpay Careers","apply_link":"https://razorpay.com/jobs"},

{"company_name":"Paytm","job_title":"Backend Developer Intern","sector":"IT","required_skills":"Java,SQL,REST API","required_education":"B.Tech","city":"Noida","state":"Uttar Pradesh","stipend":30000,"platform":"Paytm Careers","apply_link":"https://paytm.com/careers"},
  
  
  
 # =========================
# AI + MACHINE LEARNING + DATA SCIENCE (20)
# =========================

{"company_name":"Deloitte","job_title":"Data Analytics Intern","sector":"AI & Data Science","required_skills":"Python,SQL,Excel,Power BI","required_education":"B.Tech","city":"Hyderabad","state":"Telangana","stipend":30000,"platform":"Deloitte Careers","apply_link":"https://careers.deloitte.com"},

{"company_name":"EY","job_title":"Data Analyst Intern","sector":"AI & Data Science","required_skills":"Python,SQL,Excel","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":28000,"platform":"EY Careers","apply_link":"https://careers.ey.com"},

{"company_name":"KPMG","job_title":"Data Analytics Intern","sector":"AI & Data Science","required_skills":"Python,SQL,Power BI","required_education":"B.Tech","city":"Gurugram","state":"Haryana","stipend":30000,"platform":"KPMG Careers","apply_link":"https://kpmg.com/careers"},

{"company_name":"PwC","job_title":"Data Science Intern","sector":"AI & Data Science","required_skills":"Python,Machine Learning,SQL","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":35000,"platform":"PwC Careers","apply_link":"https://www.pwc.com/careers"},

{"company_name":"IBM","job_title":"AI Intern","sector":"AI & Data Science","required_skills":"Python,Machine Learning,TensorFlow","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":40000,"platform":"IBM Careers","apply_link":"https://www.ibm.com/careers"},

{"company_name":"Microsoft","job_title":"Data Science Intern","sector":"AI & Data Science","required_skills":"Python,SQL,Azure","required_education":"B.Tech","city":"Hyderabad","state":"Telangana","stipend":60000,"platform":"Microsoft Careers","apply_link":"https://careers.microsoft.com"},

{"company_name":"Google","job_title":"Machine Learning Intern","sector":"AI & Data Science","required_skills":"Python,Machine Learning,Statistics","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":80000,"platform":"Google Careers","apply_link":"https://careers.google.com"},

{"company_name":"Amazon","job_title":"Applied Scientist Intern","sector":"AI & Data Science","required_skills":"Python,Machine Learning,Deep Learning","required_education":"B.Tech","city":"Hyderabad","state":"Telangana","stipend":70000,"platform":"Amazon Jobs","apply_link":"https://www.amazon.jobs"},

{"company_name":"Intel","job_title":"AI Software Intern","sector":"AI & Data Science","required_skills":"Python,C++,Machine Learning","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":55000,"platform":"Intel Careers","apply_link":"https://jobs.intel.com"},

{"company_name":"NVIDIA","job_title":"Deep Learning Intern","sector":"AI & Data Science","required_skills":"Python,CUDA,Deep Learning","required_education":"B.Tech","city":"Pune","state":"Maharashtra","stipend":65000,"platform":"NVIDIA Careers","apply_link":"https://www.nvidia.com/en-us/about-nvidia/careers"},

{"company_name":"Oracle","job_title":"Data Engineer Intern","sector":"AI & Data Science","required_skills":"Python,SQL,Data Engineering","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":50000,"platform":"Oracle Careers","apply_link":"https://careers.oracle.com"},

{"company_name":"SAP","job_title":"Business Intelligence Intern","sector":"AI & Data Science","required_skills":"SQL,Power BI,Python","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":45000,"platform":"SAP Careers","apply_link":"https://www.sap.com/careers"},

{"company_name":"Accenture","job_title":"AI Engineer Intern","sector":"AI & Data Science","required_skills":"Python,Machine Learning,Azure","required_education":"B.Tech","city":"Pune","state":"Maharashtra","stipend":30000,"platform":"Accenture Careers","apply_link":"https://www.accenture.com/in-en/careers"},

{"company_name":"Infosys","job_title":"Data Analyst Intern","sector":"AI & Data Science","required_skills":"Python,SQL,Excel","required_education":"B.Tech","city":"Mysuru","state":"Karnataka","stipend":22000,"platform":"Infosys Careers","apply_link":"https://career.infosys.com"},

{"company_name":"TCS","job_title":"AI & Data Science Intern","sector":"AI & Data Science","required_skills":"Python,Machine Learning,SQL","required_education":"B.Tech","city":"Pune","state":"Maharashtra","stipend":22000,"platform":"TCS Careers","apply_link":"https://www.tcs.com/careers"},

{"company_name":"Wipro","job_title":"Machine Learning Intern","sector":"AI & Data Science","required_skills":"Python,Machine Learning,SQL","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":22000,"platform":"Wipro Careers","apply_link":"https://careers.wipro.com"},

{"company_name":"Capgemini","job_title":"Business Analyst Intern","sector":"AI & Data Science","required_skills":"SQL,Excel,Power BI","required_education":"B.Tech","city":"Mumbai","state":"Maharashtra","stipend":25000,"platform":"Capgemini Careers","apply_link":"https://www.capgemini.com/careers"},

{"company_name":"Cognizant","job_title":"Data Engineering Intern","sector":"AI & Data Science","required_skills":"Python,SQL,ETL","required_education":"B.Tech","city":"Chennai","state":"Tamil Nadu","stipend":25000,"platform":"Cognizant Careers","apply_link":"https://careers.cognizant.com"},

{"company_name":"HCLTech","job_title":"AI Developer Intern","sector":"AI & Data Science","required_skills":"Python,Machine Learning,Git","required_education":"B.Tech","city":"Noida","state":"Uttar Pradesh","stipend":22000,"platform":"HCL Careers","apply_link":"https://www.hcltech.com/careers"},

{"company_name":"Bosch","job_title":"Computer Vision Intern","sector":"AI & Data Science","required_skills":"Python,OpenCV,Machine Learning","required_education":"B.Tech","city":"Coimbatore","state":"Tamil Nadu","stipend":30000,"platform":"Bosch Careers","apply_link":"https://www.bosch.in/careers"},
        
   
# =========================
# FINANCE + BANKING + HR (25)
# =========================

{"company_name":"Deloitte","job_title":"Financial Analyst Intern","sector":"Finance","required_skills":"Excel,Accounting,Power BI","required_education":"B.Com","city":"Hyderabad","state":"Telangana","stipend":25000,"platform":"Deloitte Careers","apply_link":"https://careers.deloitte.com"},

{"company_name":"EY","job_title":"Finance Intern","sector":"Finance","required_skills":"Excel,Accounting,Tally","required_education":"B.Com","city":"Bengaluru","state":"Karnataka","stipend":22000,"platform":"EY Careers","apply_link":"https://careers.ey.com"},

{"company_name":"KPMG","job_title":"Audit Intern","sector":"Finance","required_skills":"Accounting,Excel,Communication","required_education":"B.Com","city":"Gurugram","state":"Haryana","stipend":22000,"platform":"KPMG Careers","apply_link":"https://kpmg.com/careers"},

{"company_name":"PwC","job_title":"Tax Intern","sector":"Finance","required_skills":"Accounting,Excel,Taxation","required_education":"B.Com","city":"Kolkata","state":"West Bengal","stipend":22000,"platform":"PwC Careers","apply_link":"https://www.pwc.com/careers"},

{"company_name":"ICICI Bank","job_title":"Banking Operations Intern","sector":"Banking","required_skills":"Communication,Excel,Customer Service","required_education":"Any Graduate","city":"Mumbai","state":"Maharashtra","stipend":18000,"platform":"ICICI Careers","apply_link":"https://www.icicibank.com/careers"},

{"company_name":"HDFC Bank","job_title":"Relationship Management Intern","sector":"Banking","required_skills":"Communication,Excel,Sales","required_education":"Any Graduate","city":"Mumbai","state":"Maharashtra","stipend":18000,"platform":"HDFC Careers","apply_link":"https://www.hdfcbank.com/personal/about-us/careers"},

{"company_name":"Axis Bank","job_title":"Retail Banking Intern","sector":"Banking","required_skills":"Communication,Excel,Customer Service","required_education":"Any Graduate","city":"Bengaluru","state":"Karnataka","stipend":17000,"platform":"Axis Bank Careers","apply_link":"https://www.axisbank.com/careers"},

{"company_name":"Kotak Mahindra Bank","job_title":"Operations Intern","sector":"Banking","required_skills":"Excel,Communication,MS Office","required_education":"Any Graduate","city":"Mumbai","state":"Maharashtra","stipend":18000,"platform":"Kotak Careers","apply_link":"https://www.kotak.com/en/careers.html"},

{"company_name":"State Bank of India","job_title":"Banking Intern","sector":"Banking","required_skills":"Communication,MS Office","required_education":"Any Graduate","city":"Mumbai","state":"Maharashtra","stipend":15000,"platform":"SBI Careers","apply_link":"https://sbi.co.in/web/careers"},

{"company_name":"Bank of Baroda","job_title":"Finance Intern","sector":"Banking","required_skills":"Accounting,Excel","required_education":"B.Com","city":"Vadodara","state":"Gujarat","stipend":15000,"platform":"Bank of Baroda Careers","apply_link":"https://www.bankofbaroda.in/career"},

{"company_name":"HSBC","job_title":"Investment Banking Intern","sector":"Finance","required_skills":"Excel,Financial Analysis,Communication","required_education":"MBA","city":"Pune","state":"Maharashtra","stipend":35000,"platform":"HSBC Careers","apply_link":"https://www.hsbc.com/careers"},

{"company_name":"JPMorgan Chase","job_title":"Finance Analyst Intern","sector":"Finance","required_skills":"Excel,SQL,Financial Analysis","required_education":"MBA","city":"Bengaluru","state":"Karnataka","stipend":50000,"platform":"JPMorgan Careers","apply_link":"https://careers.jpmorgan.com"},

{"company_name":"Goldman Sachs","job_title":"Operations Intern","sector":"Finance","required_skills":"Excel,Communication,Analysis","required_education":"MBA","city":"Bengaluru","state":"Karnataka","stipend":50000,"platform":"Goldman Sachs Careers","apply_link":"https://www.goldmansachs.com/careers"},

{"company_name":"American Express","job_title":"Business Analyst Intern","sector":"Finance","required_skills":"Excel,SQL,Power BI","required_education":"B.Tech","city":"Gurugram","state":"Haryana","stipend":40000,"platform":"American Express Careers","apply_link":"https://www.americanexpress.com/en-us/careers/"},

{"company_name":"Paytm","job_title":"Finance Intern","sector":"Finance","required_skills":"Excel,Accounting,Communication","required_education":"B.Com","city":"Noida","state":"Uttar Pradesh","stipend":20000,"platform":"Paytm Careers","apply_link":"https://paytm.com/careers"},

{"company_name":"PhonePe","job_title":"Risk Analyst Intern","sector":"Finance","required_skills":"Excel,SQL,Analytics","required_education":"B.Tech","city":"Bengaluru","state":"Karnataka","stipend":35000,"platform":"PhonePe Careers","apply_link":"https://www.phonepe.com/careers"},

{"company_name":"Infosys","job_title":"HR Intern","sector":"HR","required_skills":"Communication,MS Office,Recruitment","required_education":"MBA","city":"Mysuru","state":"Karnataka","stipend":18000,"platform":"Infosys Careers","apply_link":"https://career.infosys.com"},

{"company_name":"TCS","job_title":"Talent Acquisition Intern","sector":"HR","required_skills":"Recruitment,Communication,Excel","required_education":"MBA","city":"Pune","state":"Maharashtra","stipend":18000,"platform":"TCS Careers","apply_link":"https://www.tcs.com/careers"},

{"company_name":"Wipro","job_title":"HR Operations Intern","sector":"HR","required_skills":"Communication,Recruitment,MS Office","required_education":"MBA","city":"Bengaluru","state":"Karnataka","stipend":18000,"platform":"Wipro Careers","apply_link":"https://careers.wipro.com"},

{"company_name":"Accenture","job_title":"Human Resources Intern","sector":"HR","required_skills":"Communication,Excel,Recruitment","required_education":"MBA","city":"Pune","state":"Maharashtra","stipend":22000,"platform":"Accenture Careers","apply_link":"https://www.accenture.com/in-en/careers"},

{"company_name":"Capgemini","job_title":"HR Intern","sector":"HR","required_skills":"Communication,MS Office,Excel","required_education":"MBA","city":"Mumbai","state":"Maharashtra","stipend":20000,"platform":"Capgemini Careers","apply_link":"https://www.capgemini.com/careers"},

{"company_name":"Cognizant","job_title":"HR Executive Intern","sector":"HR","required_skills":"Communication,Recruitment,MS Office","required_education":"MBA","city":"Chennai","state":"Tamil Nadu","stipend":18000,"platform":"Cognizant Careers","apply_link":"https://careers.cognizant.com"},

{"company_name":"HCLTech","job_title":"HR Intern","sector":"HR","required_skills":"Communication,Excel,Recruitment","required_education":"MBA","city":"Noida","state":"Uttar Pradesh","stipend":18000,"platform":"HCL Careers","apply_link":"https://www.hcltech.com/careers"},

{"company_name":"Oracle","job_title":"Finance Operations Intern","sector":"Finance","required_skills":"Excel,Accounting,SQL","required_education":"B.Com","city":"Bengaluru","state":"Karnataka","stipend":28000,"platform":"Oracle Careers","apply_link":"https://careers.oracle.com"},

{"company_name":"SAP","job_title":"Finance Analyst Intern","sector":"Finance","required_skills":"Excel,SQL,Power BI","required_education":"B.Com","city":"Bengaluru","state":"Karnataka","stipend":30000,"platform":"SAP Careers","apply_link":"https://www.sap.com/careers"}, 
   

{"company_name":"Hindustan Unilever","job_title":"Marketing Intern","sector":"Marketing","required_skills":"Marketing,Excel,Communication","required_education":"MBA","city":"Mumbai","state":"Maharashtra","stipend":30000,"platform":"HUL Careers","apply_link":"https://careers.unilever.com"},

{"company_name":"P&G","job_title":"Brand Management Intern","sector":"Marketing","required_skills":"Marketing,Communication,PowerPoint","required_education":"MBA","city":"Mumbai","state":"Maharashtra","stipend":35000,"platform":"P&G Careers","apply_link":"https://www.pgcareers.com"},

{"company_name":"Nestlé India","job_title":"Sales & Marketing Intern","sector":"Marketing","required_skills":"Marketing,Sales,Communication","required_education":"MBA","city":"Gurugram","state":"Haryana","stipend":25000,"platform":"Nestlé Careers","apply_link":"https://www.nestle.in/jobs"},

{"company_name":"Dabur","job_title":"Marketing Intern","sector":"Marketing","required_skills":"Marketing,Excel,Communication","required_education":"MBA","city":"Ghaziabad","state":"Uttar Pradesh","stipend":22000,"platform":"Dabur Careers","apply_link":"https://www.dabur.com/careers"},

{"company_name":"Asian Paints","job_title":"Sales Intern","sector":"Marketing","required_skills":"Sales,Marketing,Communication","required_education":"MBA","city":"Mumbai","state":"Maharashtra","stipend":25000,"platform":"Asian Paints Careers","apply_link":"https://www.asianpaints.com/careers"},

{"company_name":"Larsen & Toubro","job_title":"Mechanical Engineering Intern","sector":"Core Engineering","required_skills":"AutoCAD,SolidWorks,Mechanical","required_education":"B.Tech","city":"Mumbai","state":"Maharashtra","stipend":25000,"platform":"L&T Careers","apply_link":"https://careers.larsentoubro.com"},

{"company_name":"Tata Steel","job_title":"Mechanical Intern","sector":"Core Engineering","required_skills":"Mechanical,Manufacturing,AutoCAD","required_education":"B.Tech","city":"Jamshedpur","state":"Jharkhand","stipend":22000,"platform":"Tata Steel Careers","apply_link":"https://www.tatasteel.com/careers"},

{"company_name":"JSW Steel","job_title":"Production Engineering Intern","sector":"Core Engineering","required_skills":"Mechanical,Production,MS Excel","required_education":"B.Tech","city":"Vijayanagar","state":"Karnataka","stipend":20000,"platform":"JSW Careers","apply_link":"https://www.jsw.in/careers"},

{"company_name":"BHEL","job_title":"Mechanical Engineering Intern","sector":"Core Engineering","required_skills":"Mechanical,CAD,Manufacturing","required_education":"B.Tech","city":"Bhopal","state":"Madhya Pradesh","stipend":18000,"platform":"BHEL Careers","apply_link":"https://careers.bhel.in"},

{"company_name":"NTPC","job_title":"Electrical Engineering Intern","sector":"Core Engineering","required_skills":"Electrical,Power Systems,PLC","required_education":"B.Tech","city":"Noida","state":"Uttar Pradesh","stipend":20000,"platform":"NTPC Careers","apply_link":"https://careers.ntpc.co.in"},  
        ]
   
        for item in sample_internships:
            db.session.add(Internship(**item))

        db.session.commit()
        count = Internship.query.count()
        print("Total internships after seeding:", count)
        print("✅ Seeded  internships successfully!")

if __name__ == "__main__":
    seed_database()
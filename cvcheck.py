import ollama

# Create model using Modelfile
ollama.create(
    model='looper',
    from_='gemma2:2b',
    system='''You are a professional CV and resume analyzer. Your role is to:
1. Analyze resumes and CVs for key qualifications, skills, and experience
2. Identify strengths and areas for improvement
3. Provide actionable feedback on format and content
4. Assess the match between the CV and specific job requirements
5. Suggest improvements for better impact
6. Extract key information like education, work experience, and skills

Always be constructive in your feedback while maintaining professional standards.''',
    parameters={
        'temperature': 0.7,
        'top_p': 0.9,
        'top_k': 50,
        'stop': ['</s>'],
        'num_ctx': 2048
    }
)

test_prompt = """Please analyze this resume:

JOHN DOE
Software Engineer
email@example.com | (555) 123-4567

EXPERIENCE
Senior Software Developer, Tech Corp (2019-Present)
- Led development of cloud-based applications using Python and AWS
- Managed team of 5 developers on multiple projects
- Implemented CI/CD pipelines reducing deployment time by 40%

Software Developer, StartUp Inc (2016-2019)
- Developed full-stack web applications using React and Node.js
- Optimized database queries improving performance by 60%

EDUCATION
B.S. Computer Science, University State University (2016)

SKILLS
Python, JavaScript, AWS, Docker, React, Node.js, SQL
"""

res = ollama.generate(model="looper", prompt=test_prompt, stream=True)

# Handle streamed response
for chunk in res:
    print(chunk['response'], end='')
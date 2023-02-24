from flask import Flask, render_template, jsonify

app= Flask(__name__)
JOBS = [
  {
    'id':1,
    'title':'data analyst',
    'location':'nairobi',
    'salary':'ksh 100,000'
  },
  {
    'id':2,
    'title':'data scientist',
    'location':'machakos',
    'salary':''
  },
  {
    'id':3,
    'title':'full-stack developer',
    'location':'mombasa',
    'salary':'ksh 210,000'
  },
  {
    'id':4,
    'title':'software engineer',
    'location':'nairobi',
    'salary':'ksh 180,000'
  }
]
@app.route("/")
def greetings():
  return render_template('home.html',
                          jobs=JOBS,
                        company_name='codeMaster')
@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)
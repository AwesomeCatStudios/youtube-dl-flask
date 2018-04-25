from flask import *
app=Flask(__name__)
import pafy
@app.route('/youtubedl',methods=["POST","GET"])
def save():
    if request.method=="GET":
       return '''
       <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<form method="POST" action="/youtubedl">
<input name=urld type=url> ENTER mp3 URL:</input>
<button type=submit class="btn btn-success">DOWNLOAD</button>
<script>
var pass=prompt("A password is required to access the page");
if(pass=="'''+pword+'''"){
  alert("Access granted");
}else{
alert("Access denied: BIG SHAQ ONE AND ONLY");
document.body.innerHTML="<h1>I'm afraid you cannot use this PERSON redirect in 5 seconds</h1>";
function Cat(){
window.location="https://raymondpeng2007.wix.com/games";
}
}
</script>
<script type="text/javascript">
    var adfly_id = 19279991;
    var popunder_frequency_delay = 0;
</script>
<script src="http://cdn.adf.ly/js/display.js"></script>
<script src='https://www.google.com/recaptcha/api.js'></script>
<select name=filetype class="form-control">
  <option value="mp4">mp4</option>
  <option value="webm">webm</option>
  <option value="mp3">mp3</option>
  <option value="m4a">m4a</option>
  <option value="3gp">3GP</option>
  <option value="flv">flv</option>
  <option value="mov">mov</option>
  <option value="mpg">mpg</option>
  <option value="avi">avi</option>
</select>
<div class="g-recaptcha" data-sitekey="6LfPUk8UAAAAAPqjhnvAiiSYw8Ng8rcR7CSYk0EL"></div>
</form>
<script type="text/javascript"> var infolinks_pid = 3084238; var infolinks_wsid = 0; </script> <script type="text/javascript" src="//resources.infolinks.com/js/infolinks_main.js"></script>
'''
    else:
      try:



        aarc=False
        if aarc:
            d(request.form["urld"],"/home/Pythonsnake2017/mysite/static/file1.html")
            d(request.form["urld"],"/home/Pythonsnake2017/mysite/templates/file1.html")
            video=1
            video.title=""
            video.description=""


        else:
           video = pafy.new(request.form["urld"])
           if not request.form["filetype"] in ["m4a","mp3"]:
               best = video.getbest(preftype=request.form["filetype"])
               filename = best.download(filepath="/home/Pythonsnake2017/mysite/static/file1.html")

           else:
               best=video.getbestaudio(preftype=request.form["filetype"])
               filename = best.download(filepath="/home/Pythonsnake2017/mysite/static/file1.html")
               #filename = best.download(filepath="/home/Pythonsnake2017/mysite/templates/file1.html",quiet=False)
        return '''
<h1>FILE DONE</h1>
<script type="text/javascript">
    var adfly_id = 19279991;
    var popunder_frequency_delay = 0;
</script>

<script src="https://apis.google.com/js/platform.js" async defer></script>
<div class="g-savetodrive"
   data-src="http://pythonsnake2017.pythonanywhere.com/static/file1.html"
   data-filename="youtubedl"
   data-sitename="PYTHON 3 Download url">
</div>
<h1>'''+video.title+'''</h1>
</p>'''+video.description+'''
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<a href="/delete1"> Delete when I'm done</a>
<p> Alternative link</p>
<a href="/static/file1.html">LINK 2</a>
<div class="g-savetodrive"
   data-src="http://pythonsnake2017.pythonanywhere.com/getfile"
   data-filename="Downloadedfile"
   data-sitename="PYTHON 3 Download url">
</div>
<a href="/getfile">DIRECT LINK download</a>
<video height=600 width=800 controls>
<source src="/static/file1.html" type="video/mp4">
</video>
<script type="text/javascript"> var infolinks_pid = 3084238; var infolinks_wsid = 0; </script> <script type="text/javascript" src="//resources.infolinks.com/js/infolinks_main.js"></script>
'''
      except Exception as e:
        return str(e)+str(type(request.form["urld"]))

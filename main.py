import xlrd
from t import *
from flask import *
from table_create import *
from backup import *
import sys



app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/goOn')
def sel():
    f=open('templates/table.html','w',encoding="utf-8")
    f.write(backup)
    f.close()
    return render_template("table.html")



@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route('/search', methods=['GET', 'POST'])
def results():
    query=''
    if request.method == "POST":
        book = request.form['book']
        query=str(book).upper()
        if query=='':
            return render_template('index.html')
    
    bauf_title=[]
    bauf_price=[]
    bauf_href=[]
    bauf_src=[]

    amz_title=[]
    amz_price=[]
    amz_href=[]
    amz_src=[]

    start="""<html>
<head>
<meta charset="UTF-8">
<title>App</title>
</head>
    <body>
    <form class="example" method="post" action="/search" 
             style="margin:auto;max-width:600px">
                <input type="text" placeholder="Search item" name="book">
                <button type="submit"><i class="fa fa-search">Search</i>
                </button>
                            
            </form>
    <div class='alpha'>
    <h2>Search results for  <span><i style='background-color:pink'>"""+query+"""</i></h2>
    </div>

    <div style='background-color:#55DC4A'>
    <h2 style='margin-left:10%'><p style='background-color:yellow;width:20%'>From Bauhof results</p></h2>
    <table style='margin-left:12%;margin-top:1%'>
    <tr>"""


           
    f = open("templates/results.html", "w",encoding="utf-8")
    f.write(start)

    #Loop
    aW1=["Piping Tools","Tool Accessories","Tool Boxes","Compressed Air Tools",'Ladders Scaffolding','Measuring instruments','Hand tools','electric tools','garden tools']
    bW1=["COMPRESSED AIR TOOLS_","electric tools_","garden tools_",'Hand tools_',"ladders-scaffolding_","MEASURING Instruments_","PIPING TOOLS_","TOOL ACCESSORIES_",'TOOL BOXES_']
    for kkk in range(len(aW1)):
        AMZZ="amazon_de/"+aW1[kkk]+'.xls'
        BAUF="bauof_data/"+str(bW1[kkk])+".xls"
        bigCrunch(AMZZ,BAUF,query,bauf_title,bauf_price,bauf_href,bauf_src,amz_title,amz_price,amz_src,amz_href)


    createDiv1(f,bauf_title,bauf_price,bauf_href,bauf_src,amz_title,amz_price,amz_src,amz_href)
    createDiv2(f,bauf_title,bauf_price,bauf_href,bauf_src,amz_title,amz_price,amz_src,amz_href) 

    final="""</div>
    </body>
    <style>
    body{
    background-color:#FF6833;
    }
    .alpha{
    color:black;
    background-color:white;
    width:300px;
    height:40px;
    }
    td{
    padding:10
    }
    a:link {
      color: red;
    }

    /* visited link */
    a:visited {
      color: green;
    }

    /* mouse over link */
    a:hover {
      color: hotpink;
    }

    /* selected link */
    a:active {
      color: blue;
    }
    form.example input[type=text] {
      padding: 10px;
      font-size: 17px;
      border: 1px solid grey;
      float: left;
      width: 80%;
      background: #f1f1f1;
    }
    form.example button {
      float: left;
      width: 20%;
      padding: 10px;
      background: #2196F3;
      color: white;
      font-size: 17px;
      border: 1px solid grey;
      border-left: none;
      cursor: pointer;
    }
    form.example button:hover {
      background: #0b7dda;
    }
    form.example::after {
      content: "";
      clear: both;
      display: table;
    }
    </style> </body>
	
	</html>"""

    f.write(final)
    f.close()
    return render_template("results.html")


@app.route('/close', methods=['GET', 'POST'])
def table():
    query=''
    if request.method == "POST":
        book = request.form['clip']
        query=str(book).upper()
        if query=='':
            return render_template("table.html")
        
    bauf_title=[]
    bauf_price=[]
    bauf_href=[]
    bauf_src=[]

    amz_title=[]
    amz_price=[]
    amz_href=[]
    amz_src=[]

    aW1=["Piping Tools","Tool Accessories","Tool Boxes","Compressed Air Tools",'Ladders Scaffolding','Measuring instruments','Hand tools','electric tools','garden tools']
    bW1=["COMPRESSED AIR TOOLS_","electric tools_","garden tools_",'Hand tools_',"ladders-scaffolding_","MEASURING Instruments_","PIPING TOOLS_","TOOL ACCESSORIES_",'TOOL BOXES_']
    for kkk in range(len(aW1)):
        AMZZ="amazon_de/"+aW1[kkk]+'.xls'
        BAUF="bauof_data/"+str(bW1[kkk])+".xls"
        bigCrunch(AMZZ,BAUF,query,bauf_title,bauf_price,bauf_href,bauf_src,amz_title,amz_price,amz_src,amz_href)
    
    createtable(bauf_title,bauf_price,amz_title,amz_price)
    return render_template('table.html')

if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False)



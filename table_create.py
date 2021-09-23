import xlrd
searchf="""<form class="example" method="post" action="/close" 
         style="margin:auto;max-width:600px">
            <input type="text" placeholder="Search item" name="clip">
            <button type="submit"><i class="fa fa-search">GET</i>
            </button>
			
        </form>

        <h2>Close range</h2>
<table id="customers">
  <tr>
    <th>bauhof item</th>
    <th>price</th>
    <th>amazon item</th>
    <th>price</th>
  </tr>"""


end=""" <style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}


#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
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
</style>
"""



def createtable(bauf_title,bauf_price,amz_title,amz_price):
    f=open('templates/table.html','w',encoding="utf-8")
    f.write(searchf)
    
    k=0
    length=len(bauf_title)
    if length>len(amz_title):
        length=len(amz_title)
        while(k<length):
            groth="<tr><td>"+bauf_title[k]+"</td><td>"+bauf_price[k]+"</td><td>"+amz_title[k]+"</td><td>"+amz_price[k]+"</td>"
            #f.write(groth)
            k+=1
        for i in range(k,len(bauf_title)):
            groth="<tr><td>"+bauf_title[i]+"</td><td>"+bauf_price[i]+"</td><td></td><td></td>"
            f.write(groth)
            
    elif length<len(amz_title):
        while(k<length):
            groth="<tr><td>"+bauf_title[k]+"</td><td>"+bauf_price[k]+"</td><td>"+amz_title[k]+"</td><td>"+amz_price[k]+"</td>"
            f.write(groth)
            k+=1
        for i in range(k,len(amz_title)):
            groth="<tr><td></td><td></td><td>"+amz_title[i]+"</td><td>"+amz_price[i]+"</td>"
            f.write(groth)
    else:
        while(k<length):
            groth="<tr><td>"+bauf_title[k]+"</td><td>"+bauf_price[k]+"</td><td>"+amz_title[k]+"</td><td>"+amz_price[k]+"</td>"
            f.write(groth)
            k+=1
    f.write('</table>')
    f.write(end)
    f.close()



import xlrd

def createDiv1(f,bauf_title,bauf_price,bauf_href,bauf_src,amz_title,amz_price,amz_src,amz_href):
    i=0
    while(i<len(bauf_title)):
        try:
            bauhof="""<td><b style='background-color:pink'><i>"""+bauf_price[i]+"""</i></b><a href='https://www."""+bauf_href[i]+"""'>
            <div style='background-color:white;height:310px;width:250px'><center>
            <img style='height:200px;width:200px' src='"""+bauf_src[i]+"""'></img><p>"""+bauf_title[i]+"""</p></center></div></a></td>"""
            
            if ((i+1)%4!=0):
                f.write(bauhof)
               
            else:
                ss="</tr><tr>"+bauhof
                f.write(ss)
        except:
            pass
        i+=1
   
def createDiv2(f,bauf_title,bauf_price,bauf_href,bauf_src,amz_title,amz_price,amz_src,amz_href):
    f.write("</table><table style='margin-left:12%;margin-top:1%><h2 style='margin-left:10%'><b><p style='margin-left:10%;background-color:yellow;width:25%;font-size:30px'>From Amazon.de results</p><b></h2><tr>")
    k=0
    while(k<len(amz_title)):
        try:
            amazon="""<td><b style='background-color:pink'><i>"""+amz_price[k]+"""</i></b><a href='https://www."""+amz_href[k]+"""'>
            <div style='background-color:white;height:310px;width:250px'>
            <center><img style='height:200px;width:200px' src='"""+amz_src[k]+"""'></img>
            <p>"""+amz_title[k]+"""</p></center></div></a></td>"""

            if ((k+1)%4!=0):
                f.write(amazon)
            else:
                sss="</tr><tr>"+amazon
                f.write(sss)
        except:
            pass
        k+=1
    f.write('</table>')
    





    


    
























def bigCrunch(amazon,buhafo,query,bauf_title,bauf_price,bauf_href,bauf_src,amz_title,amz_price,amz_src,amz_href):
    #actually amazon
    workbook1 = xlrd.open_workbook(amazon)
    work_bauf = workbook1.sheet_by_index(0)

    workbook2 = xlrd.open_workbook(buhafo)
    work_amazon = workbook2.sheet_by_index(0)

    
    n_rows=1
    t=True
    while t:
        try:
            title=work_bauf.cell(n_rows,0).value
            price=eval(work_bauf.cell(n_rows,1).value.replace("€", "").replace(",","."))
            src=work_bauf.cell(n_rows,2).value
            href=work_bauf.cell(n_rows,3).value

            title1=work_amazon.cell(n_rows,0).value
            price1=eval(work_amazon.cell(n_rows,1).value.replace("€", "").replace(",","."))
            src1=work_amazon.cell(n_rows,2).value
            href1=work_amazon.cell(n_rows,3).value
            
            Title=title.upper()
            Title1=title1.upper()
            
            if query in Title and query in Title1:
               bauf_title.append(title1)
               bauf_price.append(str(price1)+"&euro;")
               bauf_src.append(src1)
               bauf_href.append(href1)
    
               amz_title.append(title)
               amz_price.append(str(price1)+"&euro;")
               amz_src.append(src)
               amz_href.append(href)
               
            elif query in Title:
               amz_title.append(title)
               amz_price.append(str(price)+"&euro;")
               amz_src.append(src)
               amz_href.append(href)
               
            elif query in Title1:
               bauf_title.append(title1)
               bauf_price.append(str(price1)+"&euro;")
               bauf_src.append(src1)
               bauf_href.append(href1)
            
        except:
            break
        n_rows+=1

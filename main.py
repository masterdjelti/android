

from flet import *

def main(page:Page):
    page.title = "me with flutter"
    page.window.width=390
    page.window.height=740
    page.bgcolor='#7BF1A8'
    page.window.top=10
    page.window.left=100
    page.window.resizable=False
    page.window.title_bar_hidden=False
    page.horizontal_alignment="center"
    page.vertical_alignment="center"
    page.scroll="auto"
    lb1=Text('hello yakhlef',color="red",italic=True,selectable=True)
    lb2=Text('get ready for the rumble',color="blue",size=24)
    lb3=Text('this is BOLD',color="black",weight= FontWeight.BOLD)
    page.add(lb1,lb2,lb3)
    btn1=TextButton("Search this",icon="SEARCH")
    btn2=ElevatedButton("Search that",color="blue",bgcolor="red",icon="add")
    #page.window.full_screen=True
    page.add(btn1,btn2 )    
    page.update()
   
   


app(main)

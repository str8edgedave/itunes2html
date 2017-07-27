#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class html(object):
    def output(self):
        text="""<!doctype html>
                <html lang="en">
                <head>
                  <meta charset="utf-8">
                  <title>The HTML5 Herald</title>
                  <meta name="description" content="The HTML5 Herald">
                  <meta name="author" content="SitePoint">

                  <link rel="stylesheet" href="css/styles.css?v=1.0">
                  <style type="text/css">
                    .new { background-color: #ffc; }
                    h2 { padding-top: 25px; } a { text-decoration: none; }
                    body { margin: 1em; font-family: arial, sans-serif; line-height: 1.2em; }
                    th { border: 1px solid rgb(196,196,196); background-color: rgb(248,248,248); }
                    tr, td { font-size: 12px; border: 1px solid rgb(235,235,235); border-top: 0px; }
                    table { border: 1px; margin-left: 5px; margin-right: 5px; padding: 2px; width: 98%; }
                    h1, h2, h3 { background-color: transparent; color: #001080; font-family: tahoma, sans-serif; }
                  </style>

                  <!--[if lt IE 9]>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.js"></script>
                  <![endif]-->
                </head>

                <body>
              <script src="js/scripts.js"></script>
            </body>
          </html>"""
        return text 

if __name__=="__main__":
    print("processing")
    htmllist=html()
    print(htmllist.output())

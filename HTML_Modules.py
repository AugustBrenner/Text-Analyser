#!/usr/local/bin/python3
# Name: August Brenner
# File name: HTML_Modules.py
# Date: July 15th, 2013


# module for generating header HTML
def HTML_START(title):
    HTML_START = """
    <html>
        <head>
            <style type='text/css'>
                td {
                    text-align: right;
                    padding-left: 0.5em;
                    padding-right: 0.5em;
                }
                #top-nav ul li {
                    display: inline;
                    padding-right: 1em;
                }
                .word0{font-size:2.4em}
                .word1{font-size:2.1em}
                .word2{font-size:1.9em}
                .word3{font-size:1.7em}
                .word4{font-size:1.5em}
                .word5{font-size:1.4em}
                .word6{font-size:1.2em}
                .word7{font-size:1.1em}
                .word8{font-size:1.0em}
                .word9{font-size:.9em}
            </style>
        </head>
        <body>
            <p>********** """ + title + """ **********</p>
    """
    print(HTML_START)


def HTML_END():
    print("""
        </body>
    </html>
    """)

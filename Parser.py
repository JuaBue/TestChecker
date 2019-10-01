import webbrowser

class ParserTest:
    def __init__(self):
        pass

    def parsetrace(self, folder_path):
        # Create header of the table.
        filepath = folder_path
        print filepath
        resultpath = open('TestResults.html', 'w')
        StoreTest = []
        message = """
        <html>
            <head>
                <meta charset="UTF-8">
                <link rel="stylesheet" href="CSS/TestReport.css">
            </head>
            <body>
                <header h1.logo:hover>
                    <h1 src=align="left">TEST RESULTS</h1>
                    <div class="bottom-left">Bottom Left</div>
                    <img src="logos/logoingenico.jpg" width=300 height=75 align="right">
                </header>
                <table>
                    <tr>
                        <th style="width: 300px">TEST MODULE</th>
                        <th style="width: 300px">TEST SUITE</th> 
                        <th style="width: 70px">RESULT</th>
                        <th style="width: 300px">COMMENT</th>
                    </tr>
                </table>
                <div class="container">
          <div class="bottom-left">Bottom Left</div>
          <div class="top-left">Top Left</div>
          <div class="top-right">Top Right</div>
          <div class="bottom-right">Bottom Right</div>
          <div class="centered">Centered</div>
        </div>
            </body>
        </html>"""

        resultpath.write(message)

        with open(filepath) as fp:
            line = fp.readline()
            while line:
                if 'TEST' in line.split("\t"):
                    StoreTest.append([line.split("\t")[8], line.split("\t")[10], line.split("\t")[11].split(":")[:][1:],
                                      line.split("\t")[11].split(":")[0][1:]])
                line = fp.readline()

        for i in range(len(StoreTest)):
            if "PASS" in StoreTest[i][3]:
                BackgroudColor = "#C4F6BC"
            else:
                BackgroudColor = "#EF968D"

            line = """<table>
              <tr>
                <td style="width: 300px; rowspan: "2"">{}</td>
                <td style="width: 300px">{}</td> 
                <td style="background-color: {}; width: 70px; text-align: center">{}</td>
                <td style="width: 300px">{}</td>
              </tr>
            </table>""".format(StoreTest[i][0], StoreTest[i][1], BackgroudColor, StoreTest[i][3], StoreTest[i][2])
            resultpath.write(line)
        resultpath.close()

    def openreport(self):
        webbrowser.open_new_tab('TestResults.html')


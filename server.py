import urllib
import re
import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
  def do_POST(self):
    length = int(self.headers['Content-length'])
    message = self.rfile.read(length).decode("utf-8")
    print(message)
    if( re.match('x=[0-9]{1}&y=[0-9]{1}', message ) ):  #this still matches 2 digits string at end
      f = open('C:/xampp/htdocs/board.txt','r+')
      x = re.findall(r'\d+', message) #array of locations in character format
      locations = [int(p) for p in x]
      print("locations", locations)
      if( (locations[0]<0 or locations[0]>9 ) or (locations[1]<0 or locations[1] >9) ):
        print("invalid locations")
        self.send_response(404,"notFound")
        self.send_header('Content-Type','text/plain; charset=utf-8')
        self.end_headers()
        return
      linearLocation = locations[0]*12 + locations[1]
      f.seek(linearLocation) 
      letter = str(f.read(1))
      if( letter == 'C' ):
        print('hit=1&sink=C')
        self.send_response(200,"hit=1&sink=C")
        self.send_header('Content-Type','text/plain; charset=utf-8')
        self.end_headers()
        f.seek(0)
        copyText = f.read()
        linearLocation = locations[0]*11 + locations[1] +1
        copyText = copyText[:linearLocation-1] + '_' + copyText[linearLocation:]
        f.close()
        os.remove('C:/xampp/htdocs/board.txt')
        f = open('C:/xampp/htdocs/board.txt','w') #will create new file
        for i in copyText:
          f.write(i)
      elif( letter == 'B' ):
        print('hit=1&sink=B')
        self.send_response(200,"hit=1&sink=C")
        self.send_header('Content-Type','text/plain; charset=utf-8')
        self.end_headers()
        f.seek(0)
        copyText = f.read()
        linearLocation = locations[0]*11 + locations[1] +1
        copyText = copyText[:linearLocation-1] + '_' + copyText[linearLocation:]
        linearLocation = locations[0]*11 + locations[1] +1
        f.close()
        os.remove('C:/xampp/htdocs/board.txt')
        f = open('C:/xampp/htdocs/board.txt','w') #will create new file
        for i in copyText:
          f.write(i)
      elif( letter == 'R' ):
        print('hit=1&sink=R')
        self.send_response(200,"hit=1&sink=C")
        self.send_header('Content-Type','text/plain; charset=utf-8')
        self.end_headers()
        f.seek(0)
        copyText = f.read()
        linearLocation = locations[0]*11 + locations[1] +1
        print(copyText[linearLocation])
        copyText = copyText[:linearLocation-1] + '_' + copyText[linearLocation:]
        print(copyText)
        f.close()
        os.remove('C:/xampp/htdocs/board.txt')
        f = open('C:/xampp/htdocs/board.txt','w') #will create new file
        for i in copyText:
          f.write(i)
      elif( letter == 'S' ):
        print('hit=1&sink=S')
        self.send_response(200,"hit=1&sink=C")
        self.send_header('Content-Type','text/plain; charset=utf-8')
        self.end_headers()
        f.seek(0)
        copyText = f.read()
        linearLocation = locations[0]*11 + locations[1] +1
        copyText = copyText[:linearLocation-1] + '_' + copyText[linearLocation:]
        f.close()
        os.remove('C:/xampp/htdocs/board.txt')
        f = open('C:/xampp/htdocs/board.txt','w') #will create new file
        for i in copyText:
          f.write(i)
      elif( letter == 'D' ):
        print('hit=1&sink=D')
        self.send_response(200,"hit=1&sink=C")
        self.send_header('Content-Type','text/plain; charset=utf-8')
        self.end_headers()
        f.seek(0)
        copyText = f.read()
        linearLocation = locations[0]*11 + locations[1] +1
        copyText = copyText[:linearLocation-1] + '_' + copyText[linearLocation:]
        f.close()
        os.remove('C:/xampp/htdocs/board.txt')
        f = open('C:/xampp/htdocs/board.txt','w') #will create new file
        for i in copyText:
          f.write(i)
      else: # _
        print('hit=0&sink=0')
        self.send_response(410,"Gone")
        self.send_header('Content-Type','text/plain; charset=utf-8')
        self.end_headers()
      f.close()
      return    
    else: #not found
      print("bad request")
      self.send_response(400,"Bad Request") #bad request
      self.send_header('Content-Type','text/plain; charset=utf-8')
      self.end_headers()
      return

def run():
  server_address = ("localhost", int(sys.argv[1]))
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  httpd.serve_forever()
run()
# https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/  was used as a reference for server running. 
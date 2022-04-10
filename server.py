from http.server import HTTPServer, BaseHTTPRequestHandler
import random

IP='localhost'
PORT=8080

def q_1():
     Rolls = 0
     Sixes = 0

     while (Rolls < 100 or Sixes < 25):
          Roll = random.randint(1,6)
          Rolls += 1
          if Roll == 6:
               Sixes += 1

     if (Rolls <= 100 and Sixes <= 25):
          print("Test 1 Passed")

     return f'Stopped at {Rolls} rolls and {Sixes} sixes'

def q_2():
     Rolls = 0
     Sixes = 0

     while (Rolls < Sixes or Sixes > 25):
          Roll = random.randint(1,6)
          Rolls += 1
          if Roll == 6:
               Sixes += 1

     if (Rolls <= 100 and Sixes <= 25):
          print("Test 2 Passed")

     return f'Stopped at {Rolls} rolls and {Sixes} sixes'

def q_3():
     Rolls = 0
     Sixes = 0

     while (Rolls == 100 or Sixes <= 25):
          Roll = random.randint(1,6)
          Rolls += 1
          if Roll == 6:
               Sixes += 1

     if (Rolls <= 100 and Sixes <= 25):
          print("Test 3 Passed")

     return f'Stopped at {Rolls} rolls and {Sixes} sixes'

def q_4():
     Rolls = 0
     Sixes = 0

     while (Rolls >= 0 and Sixes < 25):
          Roll = random.randint(1,6)
          Rolls += 1
          if Roll == 6:
               Sixes += 1

     if (Rolls <= 100 and Sixes <= 25):
          print("Test 4 Passed")

     return f'Stopped at {Rolls} rolls and {Sixes} sixes'

def q_5():
     Rolls = 0
     Sixes = 0

     while (Rolls < 100 and Sixes < 25):
          Roll = random.randint(1,6)
          Rolls += 1
          if Roll == 6:
               Sixes += 1

     if (Rolls <= 100 and Sixes <= 25):
          print("Test 5 Passed")

     return f'Stopped at {Rolls} rolls and {Sixes} sixes'

class Server(BaseHTTPRequestHandler):

     def do_GET(self):

          request_ip = self.client_address[0]
          request_port = self.client_address[1]
          request_path = self.path

          print(f'GET request received by {request_ip}:{request_port} for {request_path}')

          output = f"""
Test 1: {q_1()}
Test 2: {q_2()}
Test 3: {q_3()}
Test 4: {q_4()}
Test 5: {q_5()}
          """

          self.send_response(200)
          self.end_headers()
          self.wfile.write(bytes(output, 'utf-8'))


server = HTTPServer((IP, PORT), Server)
print(f'Webserver started on {IP}:{PORT}')
server.serve_forever()
server.server_close()


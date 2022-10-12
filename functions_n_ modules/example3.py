data = "" # global variable

def data_appender(s):
    global data # this line tells data_appender that we have a global variable data
    #if len(s) > 0:
    data += s

# calling
data_appender("hello")
data_appender("world")
data_appender("this is a simple function")
data_appender("assure after use") 

print(data) 
import subprocess
import time


class VirtualSandbox:

    def __init__(self, timeout_value, path, folder, con_name, compiler_name, file_name, code, output_command,
                 languageName, stdin_data):

        self.timeout_value = timeout_value
        self.path = path
        self.folder = folder
        self.con_name = con_name
        self.compiler_name = compiler_name
        self.file_name = file_name
        self.code = code
        self.output_command = output_command
        self.languageName = languageName
        self.stdin_data = stdin_data

    def run(self):
        sandbox = self
        self.prepare(sandbox.execute())

    def prepare(self, success_func):
        sandbox = self
        completed = subprocess.run(["mkdir", self.path+self.folder])
        if completed.returncode == 0:
            completed = subprocess.run(["cp", self.path+"/payload/*", self.path+self.folder])
        if completed.returncode == 0:
            completed = subprocess.run(["chmod", "777", self.path+self.folder])
        if completed.returncode == 0:
            f = open(self.path+self.folder+"/"+self.file_name, "w")
            f.write(self.code)
            completed = subprocess.run(["chmod", "777", "'"+self.path+self.folder+"/"+self.file_name+"'"])
        if completed.returncode == 0:
            f = open(self.path+self.folder+"/inputFile", "w")
            f.write(self.stdin_data)
        if completed.returncode == 0:
            success_func()
        print("There was an error!")

    def execute(self):
        ex = [self.path+"DockerTimeout.sh", self.timeout_value, "-u", "yeet", "-i", "-t", "-v",
              '"'+self.path+self.folder+":/usercode", self.con_name, "/usercode/script.sh", self.compiler_name,
              self.file_name, self.output_command]
        p = subprocess.Popen(ex)
        myC = 0

        while True:
            myC += 1
            try:
                f = open(self.path+self.folder+"/completed", "r")
            except FileNotFoundError:
                time.sleep(1)
                continue
            if myC < self.timeout_value:
                ferr = open(self.path+self.folder+"/error", "a+")

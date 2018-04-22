from subprocess import Popen, PIPE
import os
import shutil


class CommandLine:
    def __init__(self, cwd):
        self.cwd = cwd

    def parse_command(self, cmd):
        cmd = cmd.strip().split()
        cmd_print = ["pwd", "ls", "date", "df"]

        if cmd[0] in cmd_print:
            return self.command_print(cmd)

        if cmd[0] == "cd":
            return self.change_directory(cmd)

        if cmd[0] == "mv":
            return self.move(cmd)

        if cmd[0] == "rm":
            return self.remove(cmd)

        if cmd[0] == "touch":
            return self.touch(cmd)

        if cmd[0] == "mkdir":
            return self.mkdir(cmd)

        # Command Not Found
        data = '{"data": "command not found"}'
        return data

    def command_print(self, cmd):
        popen = Popen(cmd, stdout=PIPE, cwd=self.cwd[0])
        out, err = popen.communicate()
        out = out.decode("UTF-8").replace("\n", "\\n")
        data = '{{"data": "{0}"}}'.format(out)
        return data

    def change_directory(self, cmd):
        try:
            dir = cmd[1]
        except:
            data = '{"data": "command missing parameter"}'
            return data


        if dir == "..":
            tmp = self.cwd[0].split("/")
            self.cwd[0] = "/".join(tmp[0:-1])
            changedirectory = '{{"cwd": "{0}"}}'.format(self.cwd[0])
            return changedirectory
        else:
            temp = self.cwd[0] + "/" + dir
            if os.path.isdir(temp):
                self.cwd[0] += "/" + dir
                changedirectory = '{{"cwd": "{0}"}}'.format(self.cwd[0])
                return changedirectory
            else:
                changedirectory = '{"cwd": "Not a directory"}'
                return changedirectory

    def move(self, cmd):
        try:
            src = cmd[1]
            des = cmd[2]
        except:
            data = '{"data": "command missing parameter"}'
            return data
        # if os.path
        if (os.path.isdir(src) or os.path.isfile(src)):
            shutil.move(src, des)
            data = '{"data": "move done"}'
            return data
        data = '{"data": "error path"}'
        return data

    def remove(self, cmd):
        try:
            src = cmd[1]
        except:
            data = '{"data": "command missing parameter"}'
            return data

        src = self.cwd[0] +"/"+ src
        if os.path.isfile(src):
            os.remove(src)
            data = '{"data": "remove done"}'
            return data

        if os.path.isdir(src):
            shutil.rmtree(src)
            data = '{"data": "remove done"}'
            return data

        data = '{"data": "error path"}'
        return data

    def touch(self, cmd):
        try:
            src = cmd[1]
        except:
            data = '{"data": "command missing parameter"}'
            return data

        fo = open(src, "a+")
        fo.close()

        data = '{"data": "create done"}'
        return data

    def mkdir(self, cmd):
        try:
            src = cmd[1]
        except:
            data = '{"data": "command missing parameter"}'
            return data

        if not os.path.exists(src):
            os.makedirs(src)
            data = '{"data": "create done"}'
            return data

        data = '{"data": "cannot create directory. Directory exists"}'
        return data









































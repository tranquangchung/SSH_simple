from subprocess import Popen, PIPE


class CommandLine:
    def __init__(self, cwd):
        self.cwd = cwd

    def parse_command(self, cmd):
        cmd = cmd.strip().split()
        out = None
        cmd_print = ["pwd", "ls", "date", "df"]

        if cmd[0] in cmd_print:
            return self.command_print(cmd)

        if cmd[0] == "cd":
            return self.change_directory(cmd)

        # Command Not Found
        out = "command not found"
        return out

    def command_print(self, cmd):
        popen = Popen(cmd, stdout=PIPE)
        out, err = popen.communicate()
        data = '{{"cwd": "None", "data": "{0}"}}'.format(out)
        return data

    def change_directory(self, cmd):
        print('---')
        if cmd[1] == "..":
            tmp = self.cwd[0].split("/")
            self.cwd[0] = "/".join(tmp[0:-1])
            changedirectory = '{{"cwd": "{0}", "data": "None"}}'.format(self.cwd[0])
            return changedirectory
        # return "change_directory"






















































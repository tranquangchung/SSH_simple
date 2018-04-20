from subprocess import Popen, PIPE


class CommandLine:
    def parse_command(self, cmd):
        cmd = cmd.strip().split()
        out = None
        cmd_print = ["pwd", "ls", "date", "df"]

        if cmd[0] in cmd_print:
            return self.command_print(cmd)

        # Command Not Found
        out = "command not found"
        return out

    def command_print(self, cmd):
        popen = Popen(cmd, stdout=PIPE)
        out, err = popen.communicate()
        return out
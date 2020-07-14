import subprocess

class Fam:
    def __init__(self, pathname):
        self.pathname = pathname

    def read_audit(self):
        cmd1 = ['ausearch', '-k', self.pathname]
        cmd2 = ['aureport', '-f', '-i']
        cmd3 = ['grep', '-v', 'xattr']

        p1 = subprocess.run(cmd1, stdout=subprocess.PIPE)
        p2 = subprocess.run(cmd2, input=p1.stdout, stdout=subprocess.PIPE)
        p3 = subprocess.run(cmd3, input=p2.stdout)

        return p3.stdout

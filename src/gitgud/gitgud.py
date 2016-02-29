import argparse, pyfiglet, sys

class git(object):
    @staticmethod
    def parse_args(cmdname):
        parser = argparse.ArgumentParser(description="Have you been told to 'get %s'? Now you can!" % cmdname)
        parser.add_argument("name", metavar="NAME", type=str, nargs="?", default=None,
                            help="who is getting %s" % cmdname)
        parser.add_argument("-s", "--super", action="store_true", default=False,
                            help="get super %s" % cmdname)
        args = parser.parse_args()
        return args

    @staticmethod
    def fig(text):
        fig = pyfiglet.Figlet()
        return fig.renderText(text)

    @staticmethod
    def print_text(command, format_str, default_qual = ""):
        args = git.parse_args(command)
        name = args.name or "You"
        sup = args.super
        if sup:
            qual = "super "
        else:
            if default_qual:
                qual = default_qual
            else:
                qual = ""

        text = format_str.format(name=name,
                                 qual=qual)
        if sup:
            text = git.fig(text)
        print(text)
    
    @staticmethod
    def gud():
        args = git.parse_args("gud")
        format_str = "{{name}} {verb} now {{qual}}gud!".format(verb="is" if args.name else "are")
        git.print_text(command="gud",
                       format_str=format_str,
                       default_qual="so ")

    @staticmethod
    def rekt():
        git.print_text(command="rekt",
                       format_str="{name} got {qual}#rekt!")

    @staticmethod
    def spooked():
        git.print_text(command="spooked",
                       format_str="{name} got spooked by a scary skeleton!")

    @staticmethod
    def job():
        git.print_text(command="job",
                       format_str="{name} got a job in gitting #rekt!")
                                                            

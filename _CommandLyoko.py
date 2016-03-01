class ConsoleFunction:
    global functions
    functions = []
    def __init__(this, name, code, *params, **options):
        this.name = name
        this.code = code
        this.params = params
        this.options = options
        this.options_listed = []
        global functions
        functions.append({"name" : this.name, "this":this})
        for q in range(len(options)):
            this.options_listed.append([this.options.keys()[q], this.options[this.options.keys()[q]]])
    def exe(this, *params, **options):
        try:
            this.code(*params, **options)
        except Exception as err:
            print("In function %s:" % this.name)
            print("\tException:", err)
class ConsoleCommand:
    def read(this):
        j = [""]
        a = False
        minecraft = False
        _ = False
        commands = {}
        are = ""
        awesome = ""
        for i in this:
            if i != " ":
                if i != "-":
                    if a:
                        commands["-" + i] = None
                        are = "-" + i
                    elif minecraft:
                        pass
                    else:
                        j[len(j)-1] += i
                        if (not awesome == "\"") and i == "'":
                            if not awesome:
                                awesome = "'"
                            else:
                                awesome = ""
                        elif (not awesome == "'") and i == "\"":
                            if not awesome:
                                awesome = "\""
                            else:
                                awesome = ""
                else:
                    if not a:
                        a = True
                    else:
                        minecraft = True
            else:
                if not awesome:
                    if minecraft:
                        minecraft = False
                        _ = True
                    elif a:
                        a = False
                        _ = True
                    j.append("")
                    if _:
                        commands[are] = j[len(j) - 1]
                else:
                    j[len(j)-1] += i

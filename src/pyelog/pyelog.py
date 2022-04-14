

class Pyelog:

    global_var = dict()
    logbook = dict()

    def __init__(self, elog_conf):
        file = open(elog_conf, "r")

        current_label = None
        for line in file:
            # Lines that start with hashtags are comments
            if line.startswith("#") or line.strip() == '':
                continue

            line = line.strip()
            # lines that start with square brackets indicate the start of either the global variable section
            # or the start of a section to define a logbook
            if line.startswith('[') and line.endswith(']'):
                current_label = line[1:len(line)-1]
            else:
                # if for some reason this line doesn't contain an equals sign I don't think it's an attribute and
                # haven't seen in the Elog documentation how they would handle it
                if "=" not in line:
                    continue

                attr = line.split("=")
                key = attr[0].strip()
                val = attr[1].strip()

                if current_label.upper() == "GLOBAL":
                    self.global_var[key] = val
                else:
                    pass
                    if current_label not in self.logbook:
                        self.logbook[current_label] = dict()

                    self.logbook[current_label][key] = val

        file.close()

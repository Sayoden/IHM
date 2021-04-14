class Bulletin(object):
    def __init__(self):
        self.bulletin = {}

    def addMatiere(self, matiere):
        if matiere not in self.bulletin:
            self.bulletin[matiere] = []

    def ajouteNote(self, matiere, note):
        if matiere not in self.bulletin:
            self.bulletin[matiere] = []
            self.bulletin[matiere].append(note)
        else:
            self.bulletin[matiere].append(note)

    def moyenneMatiere(self, matiere):
        if matiere in self.bulletin:
            moy = 0
            nbNote = len(self.bulletin[matiere])
            for i in self.bulletin[matiere]:
                moy += i
            return moy / nbNote
        else:
            return 0


    def __str__(self):
        ret = ""
        for k in self.bulletin:
            ret += k + " : " + str(self.bulletin[k]) + "\n"
        return ret
class Studerande:
    def __init__(self, studentID) -> None:
        self._studetID = studentID
        self._kurser = []
        self._betyg = {}

    def get_student_id(self):
        return self._studetID

    def lägg_till_kurs(self, kurs):
        if kurs not in self._kurser:
            self._kurser.append(kurs)

        else:
            print("Studenten läser redan den kursen!")

    def sätt_betyg(self, kurs, betyg):
        if kurs in self._kurser:
            if kurs in self._betyg:
                print("Betyget är redan satt!")
            else:
                self._betyg[kurs] = betyg
        
        else:
            print(f"Student med student id:{self._studetID} tar inte kursen {kurs}")

    def hämta_betyg(self,kurs):
        if kurs in self._betyg:
            return self._betyg[kurs]
        else:
            print("Finns inget betyg!")
            return None


student1 = Studerande(1234)
student2 = Studerande(5555)

student1.lägg_till_kurs("Matte 4")
student1.lägg_till_kurs("Engelska 5")
student1.lägg_till_kurs("Svenska 2")

student2.lägg_till_kurs("Matte 5")
student2.lägg_till_kurs("Engelska 6")
student2.lägg_till_kurs("Svenska 1")
student2.lägg_till_kurs("Matte 5")

student1.sätt_betyg("Idrott", "A")
student1.sätt_betyg("Matte 4", "VG")

if student2.hämta_betyg("Engelska 6") == None:
    print(f"Student {student2.get_student_id()} har inget betyg i Engleska 6")

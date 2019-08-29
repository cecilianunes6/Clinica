
#flags
FISIO = "physiotherapy"
PEDIA = "pediatrician"
ENDIC = "endocrine"
CLINI = "clinical"



class Client:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.clinical_data = {
            'blood': {
                'int_glucose' : None,
                'int_triglycerides' : None,
                'int_red_blood_cell' : None
            },
            'body' : {
                'bool_foot_injury' : False,
                'bool_thorax_injury' : False,
                'bool_head_injury' : False
            },
            'mind' : {
                'bool_mental_problems' : False
            }
        }

    #def sugest_doctors(self): Esse é o protótipo de uma função para sugerir um médico cadastrado com base no seu self.clinical_data
    def get_blood(self):
        return self.clinical_data['blood']

    def get_body(self):
        return self.clinical_data['body']

    def get_mind(self):
        return  self.clinical_data['mind']

    def set_attr(self, key, value):
        for dict_clinical in self.clinical_data:
            if key in self.clinical_data[dict_clinical]:
                self.clinical_data[dict_clinical][key] = value

class Doctor:
    def __init__(self, id, name):
        self.name = name
        self.id = name
        self.specialties = list()

    def add_spacialty(self, str_spacialty):
        self.specialties.append(str_spacialty)

class Event:
    def __init__(self, id, doctor, client, data):
        self.id = id
        self.data = data
        self.doctor = doctor
        self.client = client
        self.title = str()
        self.description = str()
        self.flags = list()

    def add_flag(self, FLAG):
        self.flags.append(FLAG)

    def set_title(self, new_title):
        self.title = new_title

    def set_description(self, new_description):
        self.description = new_description
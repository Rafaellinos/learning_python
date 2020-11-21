"""
    Ex:
        Criar perfis diferentes em redes sociais como Facebook e LinkedIn
        para uma pessoa ou uma empresa.
        Criar perfis diferentes com seções corretas adicionadas ao Perfil
"""
from abc import ABCMeta, abstractmethod

# Criar a classe abstrata section

class Section(metaclass=ABCMeta):

    @abstractmethod
    def describe(self):
        pass

    def __repr__(self):
        return str(type(self).__name__)

class PersonalSection(Section):

    def describe(self):
        print("Personal Section")

class AlbumSection(Section):

    def describe(self):
        print("Album Section")

class PatentSection(Section):

    def describe(self):
        print("Patent Section")

class PublicationSection(Section):

    def describe(self):
        print("Publication Section")


class Profile(metaclass=ABCMeta):

    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_sections(self, section):
        self.sections.append(section)

class LinkedIn(Profile):

    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(PatentSection())
        self.add_sections(PublicationSection())

class Facebook(Profile):

    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())

PROFILE_TYPES = ['Facebook', 'LinkedIn']
if __name__ == '__main__':
    while True:
        profile_type = input("Qual Perfil vc deseja descolher? Facebook ou LinkedIn?")
        if profile_type in PROFILE_TYPES:
            break
        print("Perfil Inválido, escolha entre Facebook e LinkedIn")
    profile = eval(profile_type)()
    print("Criando perfil", type(profile).__name__)
    print("Profile has sections --", profile.get_sections())

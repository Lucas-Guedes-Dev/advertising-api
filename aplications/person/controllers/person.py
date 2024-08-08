from aplications.person.instructions.person import IPerson
from aplications.person.models import Person


class CPerson(IPerson):
    def __init__(self):
        super().__init__()

    def get_person_by_filter(self, filter_type=None, cpf_cnpj=None, person_id=None):
        if person_id:
            person = self.get_person_by_id(person_id)
            return [self.create_object_json(person)]

        if cpf_cnpj:
            person = self.get_person_by_cpf(cpf_cnpj)
            if person:
                return [self.create_object_json(person)]
            else:
                return []

        filter_methods = {
            'clients': self.get_person_clients,
            'employees': self.get_person_employes,
            'drivers': self.get_person_drivers,
            'all': self.get_all_persons,
        }

        if filter_type in filter_methods:
            persons = filter_methods[filter_type]()
            person_list = [self.create_object_json(
                person) for person in persons]
            return person_list

        return []

    def create_object_json(self, person: Person):
        return {
            'id': person.id,
            'name': person.name,
            'cpf_cnpj': person.cpf_cnpj,
            'email': person.email,
            'phone': person.phone,
            'road': person.road,
            'state': person.state,
            'number': person.number,
            'neighborhood': person.neighborhood,
            'is_employee': person.is_employee,
            'is_client': person.is_client,
            'is_driver': person.is_driver,
            'active': person.active,
            'city': person.city,
            'user_id': person.user_id,
        }

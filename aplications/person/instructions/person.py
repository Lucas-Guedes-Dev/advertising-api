from aplications.person.models import Person
from aplications import db
from sqlalchemy.exc import IntegrityError


class IPerson:
    def get_person_by_id(self, id):
        return Person.query.filter_by(id=id).first()

    def get_person_by_cpf(self, cpf):
        return Person.query.filter_by(cpf_cnpj=cpf).first()

    def get_all_persons(self):
        return Person.query.all()

    def create_person(self, person_dict):
        user_id = None

        if person_dict.get('user_id'):
            user_id = person_dict.get('user_id')

        try:
            new_person = Person(
                name=person_dict.get('name'),
                cpf_cnpj=person_dict.get('cpf_cnpj'),
                email=person_dict.get('email'),
                phone=person_dict.get('phone'),
                road=person_dict.get('road'),
                state=person_dict.get('state'),
                number=person_dict.get('number'),
                neighborhood=person_dict.get('neighborhood'),
                is_employee=person_dict.get('is_employee', False),
                is_client=person_dict.get('is_client', False),
                active=person_dict.get('active', True),
                user_id=user_id
            )
            db.session.add(new_person)
            db.session.commit()

            return {"success": True}

        except IntegrityError as e:
            return {"success": False, "message": str(e)}

    def delete_person(self, person_id):
        person = Person.query.get(person_id)
        if person:
            db.session.delete(person)
            db.session.commit()
            return True
        return False

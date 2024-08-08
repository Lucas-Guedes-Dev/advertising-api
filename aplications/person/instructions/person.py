from aplications.person.models import Person
from aplications import db
from sqlalchemy.exc import IntegrityError


class IPerson:
    def get_person_by_id(self, id):
        return Person.query.filter_by(id=id).first()

    def get_person_by_cpf(self, cpf):
        return Person.query.filter_by(cpf_cnpj=cpf).first()

    def get_person_clients(self):
        return Person.query.filter_by(is_client=True).all()

    def get_person_employes(self):
        return Person.query.filter_by(is_employee=True).all()

    def get_person_drivers(self):
        return Person.query.filter_by(is_driver=True).all()

    def get_all_persons(self):
        return Person.query.all()

    def update_person_by_id(self, id, person_dict):
        person = Person.query.filter_by(id=id).first()

        if not person:
            raise ValueError("Person not found")

        for key, value in person_dict.items():
            if hasattr(person, key):
                setattr(person, key, value)

        try:
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise False

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
                city=person_dict.get('city'),
                is_employee=person_dict.get('is_employee', False),
                is_client=person_dict.get('is_client', False),
                is_driver=person_dict.get('is_driver', False),
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

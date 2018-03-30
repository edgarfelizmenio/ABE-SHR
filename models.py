import config

from database import Base, db_session

Encounter = Base.classes.Encounter
EncounterRole = Base.classes.EncounterRole
EncounterType = Base.classes.EncounterType

def get_encounter_ids(patient_id = None):
    if patient_id is not None:
        result = db_session.query(Encounter).filter(
            Encounter.patient_id == patient_id).all()
    else:
        result = db_session.query(Encounter).all()
    return [e.encounter_id for e in result]

def get_encounter(encounter_id):
    result = db_session.query(Encounter).filter(Encounter.encounter_id == encounter_id).first()
    if result is None:
        return None
    encounter_object = {
        'encounter_id': result.encounter_id,
        'patient_id': result.patient_id,
        'contents': result.contents
    }
    return encounter_object

def add_encounter(patient_id, data):
    data['patient_id'] = patient_id
    return create_encounter(data)

def create_encounter(data):
    encounter = Encounter(
        patient_id = data['patient_id'],
        contents = data['contents']
    )
    db_session.add(encounter)
    db_session.commit()
    return encounter.encounter_id

def delete_all():
    db_session.query(Encounter).delete()
    db_session.commit()


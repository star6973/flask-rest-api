import db_init as db
from db_init import Base

class Energy(Base):
    __tablename__ = "Energy"
    id = db.Column(db.Integer, primary_key=True)
    optimal_cost = db.Column(db.Integer)

def create_db():
    session = db.init_database()
    energy = Energy()
    
    # DB 속성 추가
    energy.id = 0
    energy.optimal_cost = 30
    session.add(energy)

    energy.id = 1
    energy.optimal_cost = 40
    session.add(energy)

    session.commit()

if __name__ == "__main__":
    create_db()
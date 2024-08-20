import math

from flask import Flask, jsonify, request
from flasgger import Swagger
from sqlalchemy import create_engine, Column, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
Swagger(app)

# Database connection
DATABASE_URI = 'mysql://testuser:testpassword@mysql_container/testdb'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Concept(Base):
    __tablename__ = 'concepts'

    id = Column(String(255), primary_key=True)
    subject_nb = Column(String(255))
    subject_nn = Column(String(255))
    subject_en = Column(String(255))
    preferredLabel_nb = Column(String(255))
    preferredLabel_nn = Column(String(255))
    preferredLabel_en = Column(String(255))
    alternativeLabel_nb = Column(String(255))
    alternativeLabel_nn = Column(String(255))
    alternativeLabel_en = Column(String(255))
    definition_nb = Column(String(255))
    definition_nn = Column(String(255))
    definition_en = Column(String(255))
    definition_lastUpdated = Column(Date)

ITEMS_PER_PAGE = 4  # Number of items to display per page

@app.route('/')
def home():
    return "IntegrationApi is running!"

@app.route('/concepts', methods=['POST'])
def get_concepts():
    """
    Get a list of concepts with pagination
    ---
    parameters:
      - name: body
        in: body
        required: false
        schema:
          type: object
          properties:
            page:
              type: integer
              description: Page number (starts from 0)
    responses:
      200:
        description: A list of concepts (may be empty for out-of-range pages)
        schema:
          type: object
          properties:
            concepts:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: string
                  subject_nb:
                    type: string
                  subject_nn:
                    type: string
                  subject_en:
                    type: string
                  preferredLabel_nb:
                    type: string
                  preferredLabel_nn:
                    type: string
                  preferredLabel_en:
                    type: string
                  alternativeLabel_nb:
                    type: string
                  alternativeLabel_nn:
                    type: string
                  alternativeLabel_en:
                    type: string
                  definition_nb:
                    type: string
                  definition_nn:
                    type: string
                  definition_en:
                    type: string
                    format: date
            total_pages:
              type: integer
            current_page:
              type: integer
            total_items:
              type: integer
    """
    data = request.json or {}
    page = data.get('page', 0)  # Default to page 0

    # Ensure page is an integer and not negative
    try:
        page = max(int(page), 0)
    except ValueError:
        page = 0

    with Session() as session:
        total_concepts = session.query(Concept).count()
        total_pages = math.ceil(total_concepts / ITEMS_PER_PAGE)

        concepts = (session
                    .query(Concept)
                    .order_by(Concept.id)
                    .offset(page * ITEMS_PER_PAGE)
                    .limit(ITEMS_PER_PAGE)
                    .all())

        concept_list = [{
            'id': c.id,
            'subject_nb': c.subject_nb,
            'subject_nn': c.subject_nn,
            'subject_en': c.subject_en,
            'preferredLabel_nb': c.preferredLabel_nb,
            'preferredLabel_nn': c.preferredLabel_nn,
            'preferredLabel_en': c.preferredLabel_en,
            'alternativeLabel_nb': c.alternativeLabel_nb,
            'alternativeLabel_nn': c.alternativeLabel_nn,
            'alternativeLabel_en': c.alternativeLabel_en,
            'definition_nb': c.definition_nb,
            'definition_nn': c.definition_nn,
            'definition_en': c.definition_en,
            'definition_lastUpdated': c.definition_lastUpdated.isoformat() if c.definition_lastUpdated else None
        } for c in concepts]

        return jsonify({
            "concepts": concept_list,
            "total_pages": total_pages,
            "current_page": page,
            "total_items": total_concepts
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, jsonify, request
from flasgger import Swagger
from mockdata import concepts
import math

app = Flask(__name__)
Swagger(app)

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
        page = int(page)
        if page < 0:
            page = 0
    except ValueError:
        page = 0

    total_concepts = len(concepts)
    total_pages = math.ceil(total_concepts / ITEMS_PER_PAGE)

    start_index = page * ITEMS_PER_PAGE
    end_index = start_index + ITEMS_PER_PAGE

    paginated_concepts = concepts[start_index:end_index]

    return jsonify({
        "concepts": paginated_concepts,
        "total_pages": total_pages,
        "current_page": page,
        "total_items": total_concepts
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

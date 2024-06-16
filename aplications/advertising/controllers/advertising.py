from aplications.advertising.instructions.advertising import IAdvertising
from flask import jsonify
import base64


class CAdvertising(IAdvertising):
    def __init__(self):
        super().__init__()

    def formating_create_advertising(self, http_data):
        if not http_data or 'image' not in http_data:
            return jsonify({"success": False, "message": "no image provided "}), 404

        image_b64 = http_data['image']

        try:
            image_data = base64.b64decode(image_b64)
        except Exception as e:
            return jsonify({"success": False, 'message': 'Invalid image data', 'error': str(e)}), 400

        http_data['image'] = image_data

        create = self.create_advertising(http_data)

        if create['success']:
            return jsonify({"success": True}), 200
        else:
            return jsonify({
                "success": False,
                "message": "was not entered into the database",
                "error": create['error']
            }), 409

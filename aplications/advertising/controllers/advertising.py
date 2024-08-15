from aplications.advertising.instructions.advertising import IAdvertising
from flask import jsonify
from aplications.advertising.models import Advertising
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

    def get_with_filter_advertising(self, filter_param):

        ads = self.get_all_advertising()
        active = True

        if filter_param.get('active'):
            active = filter_param['active']

        if filter_param.get('person_id'):
            ads = self.get_advertising_by_person_id(
                filter_param['person_id'], active)

        if filter_param.get("start_date") and filter_param.get('end_date'):
            ads = self.get_period_advertising(
                filter_param["start_date"], filter_param["end_date"], active
            )

        if filter_param.get('id'):
            ads = [self.get_advertising_by_id(filter_param['id'])]

        if filter_param.get('start_date') and not filter_param.get('end_date'):
            return jsonify({'message': 'preencha o campo de data final'}), 401

        if not filter_param.get('start_date') and filter_param.get('end_date'):
            return jsonify({'message': 'preencha o campo de data inicial'}), 401

        return_list = [self.create_object_json(ad) for ad in ads]

        if not return_list and filter_param:
            return jsonify({'message': 'não foi possível encontrar dados'}), 404

        return jsonify(return_list), 200

    def create_object_json(self, advertising: Advertising):

        start_date = 'null'
        if advertising.date_start:
            start_date = advertising.date_start.strftime('%Y-%m-%d %H:%M:%S')

        end_date = 'null'
        if advertising.date_end:
            end_date = advertising.date_end.strftime('%Y-%m-%d %H:%M:%S')

        image = ''
        if advertising.image:
            base64_encoded = base64.b64encode(advertising.image)
            image = base64_encoded.decode('utf-8')

        return {
            'id': advertising.id,
            'name': advertising.name,
            'image': image,
            'date_start': start_date,
            'date_end': end_date,
            'description': advertising.description,
            'video_url': advertising.video_url,
            'active': advertising.active,
            'person_id': advertising.person_id,
        }

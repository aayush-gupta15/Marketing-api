from flask_restful import Resource
from model.facebook import FacebookModel
from flask_jwt_extended import jwt_required
from application.utils.logger import create_logger
from application.facebook.facebook_campaign import FacebookCampaign


class Facebook(Resource):

    def __init__(self):
        self.__logger = create_logger()
        self.__campaign_obj = FacebookCampaign()

    def get(self, name):
        campaign = FacebookModel.find_by_name(name)
        if campaign:
            return campaign.json()
        return {'message': 'campaign not found'}, 404

    @jwt_required()  # Requires auth token
    def post(self, count=None):
        
        campaign_data = self.__campaign_obj.get_campaign_data(count)
        
        for single_campaign in campaign_data:
            campaign_db = FacebookModel(single_campaign.__dict__)
            try:
                campaign_db.save_to_db()
            except Exception as e:
                self.__logger.info(f"error: {e}")
                return {"message": "An error occurred adding the campaign."}, 500

        return campaign_db.json(), 201

class FacebookCampaignList(Resource):
    def get(self):
        return {'campaigns': [campaign.json() for campaign in FacebookModel.query.all()]}
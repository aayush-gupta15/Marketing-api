from config import Credentials
from application.facebook.campaign_dto import Campaign

class FacebookCampaign:
    def __init__(self):
        self.login()
    
    def login(self):
        pass

    def get_campaign_data(self, count=None):
        campaign_list = [] # need to fetch from third party api
        campaign_list = campaign_list if count == None else campaign_list[:count]
        campaigns = []
        for each in campaign_list:
            campaign_obj = Campaign()
            
            # fill details of campaigns
            campaigns.append(campaign_obj)

        return campaigns



# above code
#...

# Generating tables before first request is fetched
@app.before_first_request
def create_tables():

    db.create_all()

# Checking that token is in blacklist or not
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):

    jti = decrypted_token['jti']

    return models.RevokedTokenModel.is_jti_blacklisted(jti)

# Importing models and resources
import models, resources

# Api Endpoints

api.add_resource(resources.UserRegistration, '/registration')

api.add_resource(resources.UserLogin, '/login')

api.add_resource(resources.UserLogoutAccess, '/logout/access')

api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')

api.add_resource(resources.TokenRefresh, '/token/refresh')

api.add_resource(resources.AllUsers, '/users')

api.add_resource(resources.SecretResource, '/secret')

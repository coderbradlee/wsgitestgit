import routes
from view import wsgi
from view import versions
class API(wsgi.Router):
	def __init__(self,mapper=None):
		if(mapper==None):
			mapper=routes.Mapper()
		versions_resource=versions.create_resource()
		mapper.connect("/",controller=versions_resource,action="index")
		super(API,self).__init__(mapper)

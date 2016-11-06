def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('test','/test')
    config.add_route('login','/login')
    config.add_route('logout','/logout')
    config.add_route('addProject','/add_project')
    config.add_route('proposal','/add_proposal/{project_id}/{type_project}')
    config.add_route('myProject','/myProject')
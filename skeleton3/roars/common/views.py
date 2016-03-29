
def hello_world(request):
    srv = request.services
    user = srv.models.users.get_by_id(request.user_id)
    skeleton = srv.skeletons.get_skeleton('hello_world.xml')
    skeleton_template = srv.skeletons.get_html_template(skeleton)
    result = skeleton_template.render({'user': user, 'user_id': request.user_id})
    return result

from flask import render_template, request, jsonify, current_app
from app import db
from app.errors import errors
from app.api.errors import error_response as api_error_response
from  werkzeug.debug import get_current_traceback

app = current_app


def wants_json_response():
    return request.accept_mimetypes['application/json'] >= \
        request.accept_mimetypes['text/html']


@errors.app_errorhandler(404)
def not_found_error(error):
    if wants_json_response():
        return api_error_response(404)
    track= get_current_traceback(skip=1, show_hidden_frames=True,
            ignore_system_exceptions=False)
    _error = str(error) + str(track.log())
    app.logger.error('An Error occured : ' + _error)
    return render_template('404.html', error=error), 404


@errors.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    if wants_json_response():
        return api_error_response(500)
    track= get_current_traceback(skip=1, show_hidden_frames=True,
            ignore_system_exceptions=False)
    _error = str(error) + str(track.log())
    app.logger.error('An Error occured : ' + _error)
    return render_template('500.html', error=error ), 500
class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, error, link=None, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        self.error = error
        self.link = link
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['error'] = self.error
        rv['link'] = self.link
        return rv

@errors.app_errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    track= get_current_traceback(skip=1, show_hidden_frames=True,
            ignore_system_exceptions=False)
    _error = str(error) + str(track.log())
    app.logger.error('An Error occured : ' + _error)
    #print(str(error.to_dict()))
    return render_template('errors/400.html', error=error.to_dict()), response.status_code

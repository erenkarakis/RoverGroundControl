from flask import render_template, Blueprint, Response
from controllers import get_current_username, get_frame_cam1, get_frame_cam2

bp = Blueprint("cam_ops", __name__, template_folder="../templates")

@bp.route("/cams")
def cams():
    username, login_auth = get_current_username()
    return render_template("cams.html", username=username, login_auth=login_auth)

@bp.route("/video_stream1")
def video_stream1():
    return Response(get_frame_cam1(), mimetype='multipart/x-mixed-replace; boundary=frame')

@bp.route("/video_stream2")
def video_stream2():
    return Response(get_frame_cam2(), mimetype='multipart/x-mixed-replace; boundary=frame')

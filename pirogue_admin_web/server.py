import time

from flask import (
    Flask,
    jsonify,
    request,
    send_from_directory,
)
from datetime import datetime
from typing import Dict, Any
from grpc import RpcError
from pirogue_admin_client import PirogueAdminClientAdapter

TOKEN_HEADER = 'x-csrftoken'

app = Flask(
    __name__,
    static_url_path='',
)
app.url_map.strict_slashes = False


def _paca() -> PirogueAdminClientAdapter:
    token = request.headers.get(TOKEN_HEADER, "dummy-token")
    paca = PirogueAdminClientAdapter(token=token)
    return paca

def _json_answer(content) -> Dict[str, Any]:
    return {
        'success': False,
        'grpc_success': False,
        'content': content,
        'error': None,
    }
@app.route("/")
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/login-with-token")
def login_with_token():
    response = dict({ "success": False, "error": None })

    try:
        content = _paca().my_user_access()
    except RpcError as rpc_error:
        response['success'] = False
        response['grpc_success'] = True
        response['error'] = rpc_error.details()
        time.sleep(1)
    except Exception as exception:
        response['success'] = False
        response['grpc_success'] = False
        response['error'] = str(exception)
        time.sleep(1)
    else:
        response['success'] = True
        response['grpc_success'] = True
        response['content'] = content

    return jsonify(response)

@app.route("/status")
def status():
    response = dict({ "success": False, "error": None })

    response['reported_at'] = str(datetime.now())
    try:
        content = _paca().get_status()
    except RpcError as rpc_error:
        response['success'] = False
        response['grpc_success'] = True
        response['error'] = rpc_error.details()
    except Exception as exception:
        response['success'] = False
        response['grpc_success'] = False
        response['error'] = str(exception)
    else:
        response['success'] = True
        response['grpc_success'] = True
        response['content'] = content

    return jsonify([response])

@app.route("/configuration")
def configuration():
    response = dict({ "success": False, "error": None })

    try:
        content = _paca().get_configuration()
    except RpcError as rpc_error:
        response['success'] = False
        response['grpc_success'] = True
        response['error'] = rpc_error.details()
    except Exception as exception:
        response['success'] = False
        response['grpc_success'] = False
        response['error'] = str(exception)
    else:
        response['success'] = True
        response['grpc_success'] = True
        response['content'] = content

    return jsonify(response)


@app.route("/packages_info")
def packages_info():
    response = dict({ "success": False, "error": None })

    try:
        content = _paca().get_packages_info()
    except RpcError as rpc_error:
        response['success'] = False
        response['grpc_success'] = True
        response['error'] = rpc_error.details()
    except Exception as exception:
        response['success'] = False
        response['grpc_success'] = False
        response['error'] = str(exception)
    else:
        response['success'] = True
        response['grpc_success'] = True
        response['content'] = content

    return jsonify(response)


@app.route("/isolated/connected_devices")
def isolated_connected_devices_list():
    response = dict({ "success": False, "error": None })

    try:
        content = _paca().list_connected_devices()
    except RpcError as rpc_error:
        response['success'] = False
        response['grpc_success'] = True
        response['error'] = rpc_error.details()
    except Exception as exception:
        response['success'] = False
        response['grpc_success'] = False
        response['error'] = str(exception)
    else:
        response['success'] = True
        response['grpc_success'] = True
        response['content'] = content

    return jsonify(response)

@app.route("/isolated/ports")
def isolated_ports_list():
    response = dict({ "success": False, "error": None })

    try:
        content = _paca().list_isolated_open_ports()
    except RpcError as rpc_error:
        response['success'] = False
        response['grpc_success'] = True
        response['error'] = rpc_error.details()
    except Exception as exception:
        response['success'] = False
        response['grpc_success'] = False
        response['error'] = str(exception)
    else:
        response['success'] = True
        response['grpc_success'] = True
        response['content'] = content

    return jsonify(response)

@app.route("/access")
def access_list():
    response = dict({ "success": False, "error": None })

    try:
        content = _paca().list_user_accesses()
    except RpcError as rpc_error:
        response['success'] = False
        response['grpc_success'] = True
        response['error'] = rpc_error.details()
    except Exception as exception:
        response['success'] = False
        response['grpc_success'] = False
        response['error'] = str(exception)
    else:
        response['success'] = True
        response['grpc_success'] = True
        response['content'] = content

    return jsonify(response)

@app.route("/access/create")
def access_create():
    response = dict({ "success": False, "error": None })

    try:
        content = _paca().create_user_access()
    except RpcError as rpc_error:
        response['success'] = False
        response['grpc_success'] = True
        response['error'] = rpc_error.details()
    except Exception as exception:
        response['success'] = False
        response['grpc_success'] = False
        response['error'] = str(exception)
    else:
        response['success'] = True
        response['grpc_success'] = True
        response['content'] = content

    return jsonify(response)

@app.route("/access/<int:user_access_id>", methods=["GET", "DELETE"])
def access_get_or_delete(user_access_id):
    response = dict({ "success": False, "error": None })

    try:
        if request.method == 'DELETE':
            content = _paca().delete_user_access(user_access_id)
        else:
            content = _paca().get_user_access(user_access_id)
    except RpcError as rpc_error:
        response['success'] = False
        response['grpc_success'] = True
        response['error'] = rpc_error.details()
    except Exception as exception:
        response['success'] = False
        response['grpc_success'] = False
        response['error'] = str(exception)
    else:
        response['success'] = True
        response['grpc_success'] = True
        response['content'] = content

    return jsonify(response)

@app.route("/access/<int:user_access_id>/reset-token")
def access_reset_token(user_access_id):
    response = dict({ "success": False, "error": None })

    try:
        content = _paca().reset_user_access_token(user_access_id)
    except RpcError as rpc_error:
        response['success'] = False
        response['grpc_success'] = True
        response['error'] = rpc_error.details()
    except Exception as exception:
        response['success'] = False
        response['grpc_success'] = False
        response['error'] = str(exception)
    else:
        response['success'] = True
        response['grpc_success'] = True
        response['content'] = content

    return jsonify(response)

@app.route("/access/<int:user_access_id>/set-permissions/", methods=["POST"])
def access_set_permissions(user_access_id):
    response = dict({ "success": False, "error": None })

    try:
        permission_list = request.get_json()
        content = _paca().set_user_access_permissions(user_access_id, permission_list)
    except RpcError as rpc_error:
        response['success'] = False
        response['grpc_success'] = True
        response['error'] = rpc_error.details()
    except Exception as exception:
        response['success'] = False
        response['grpc_success'] = False
        response['error'] = str(exception)
    else:
        response['success'] = True
        response['grpc_success'] = True
        response['content'] = content

    return jsonify(response)

@app.route("/access/permissions")
def access_permissions():
    response = dict({ "success": False, "error": None })

    try:
        content = _paca().get_permission_list()
    except RpcError as rpc_error:
        response['success'] = False
        response['grpc_success'] = True
        response['error'] = rpc_error.details()
    except Exception as exception:
        response['success'] = False
        response['grpc_success'] = False
        response['error'] = str(exception)
    else:
        response['success'] = True
        response['grpc_success'] = True
        response['content'] = content

    return jsonify(response)

@app.route("/access/me")
def my_user_access():
    response = dict({ "success": False, "error": None })

    try:
        content = _paca().my_user_access()
    except RpcError as rpc_error:
        response['success'] = False
        response['grpc_success'] = True
        response['error'] = rpc_error.details()
        time.sleep(1)
    except Exception as exception:
        response['success'] = False
        response['grpc_success'] = False
        response['error'] = str(exception)
        time.sleep(1)
    else:
        response['success'] = True
        response['grpc_success'] = True
        if content['token'] == '[admin token redacted]':
            content['permissions']['services']['Access'] = {},
        response['content'] = content

    return jsonify(response)

@app.route("/vpn_peer")
def vpn_peer_list():
    response = dict({ "success": False, "error": None })

    try:
        content = _paca().list_vpn_peers()
    except RpcError as rpc_error:
        response['success'] = False
        response['grpc_success'] = True
        response['error'] = rpc_error.details()
    except Exception as exception:
        response['success'] = False
        response['grpc_success'] = False
        response['error'] = str(exception)
    else:
        response['success'] = True
        response['grpc_success'] = True
        response['content'] = content

    return jsonify(response)

@app.route("/vpn_peer/create")
def vpn_peer_create():
    response = dict({ "success": False, "error": None })

    try:
        content = _paca().add_vpn_peer()
    except RpcError as rpc_error:
        response['success'] = False
        response['grpc_success'] = True
        response['error'] = rpc_error.details()
    except Exception as exception:
        response['success'] = False
        response['grpc_success'] = False
        response['error'] = str(exception)
    else:
        response['success'] = True
        response['grpc_success'] = True
        response['content'] = content

    return jsonify(response)

@app.route("/vpn_peer/<int:peer_id>", methods=["GET", "DELETE"])
def vpn_peer_detail_or_delete(peer_id):
    response = dict({ "success": False, "error": None })

    try:
        if request.method == 'DELETE':
            content = _paca().delete_vpn_peer(peer_id)
        else:
            content = _paca().get_vpn_peer_config(peer_id)
    except RpcError as rpc_error:
        response['success'] = False
        response['grpc_success'] = True
        response['error'] = rpc_error.details()
    except Exception as exception:
        response['success'] = False
        response['grpc_success'] = False
        response['error'] = str(exception)
    else:
        response['success'] = True
        response['grpc_success'] = True
        response['content'] = content

    return jsonify(response)

@app.route("/suricata_rules_source", methods=['GET', 'PUT', 'POST', 'DELETE'])
def suricata_rules_source_list():
    response = dict({ "success": False, "error": None })

    try:
        if request.method == 'DELETE':
            data = request.get_json()
            content = _paca().delete_suricata_rules_source(data.get('name'))
        elif request.method in ['PUT', 'POST']:
            data = request.get_json()
            content = _paca().add_suricata_rules_source(
                data.get('name'),
                data.get('url', None),
                data.get('parameters', None)
            )
        else:
            content = _paca().list_suricata_rules_sources()

    except RpcError as rpc_error:
        response['success'] = False
        response['grpc_success'] = True
        response['error'] = rpc_error.details()
    except Exception as exception:
        response['success'] = False
        response['grpc_success'] = False
        response['error'] = str(exception)
    else:
        response['success'] = True
        response['grpc_success'] = True
        response['content'] = content

    return jsonify(response)
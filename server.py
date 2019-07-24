import flask
import pandas as pd
from tsfresh import extract_features

server = flask.Flask(__name__)

@server.route('/api', methods=['POST'])
def serve():
    json = str(flask.request.get_json(force=True)).replace("'", '"')

    df = pd.read_json(json)

    retval = extract_features(df, column_sort='level_0', column_id='level_1')

    return flask.jsonify(retval.to_json())

if __name__ == '__main__':
    server.run(port=5000, debug=True)

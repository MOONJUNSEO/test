from flask import Flask, request, jsonify

app = Flask(__name__)

# 위치 정보를 저장할 리스트
locations = []

# 위치 정보를 수신하는 엔드포인트
@app.route('/location', methods=['POST'])
def receive_location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    
    if latitude is not None and longitude is not None:
        # 위치 정보를 리스트에 저장
        locations.append({'latitude': latitude, 'longitude': longitude})
        print(f"Received location: Latitude={latitude}, Longitude={longitude}")
        return jsonify({"status": "Location received", "data": locations}), 200
    else:
        return jsonify({"error": "Invalid data"}), 400

# 위치 정보 리스트를 조회하는 엔드포인트
@app.route('/locations', methods=['GET'])
def get_locations():
    return jsonify({"locations": locations}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

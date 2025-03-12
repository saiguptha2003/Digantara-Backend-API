from flask import Blueprint, request, jsonify
from services import binarySearch, quickSort, bfs, logAlgorithm

algorithmBp = Blueprint('algorithm', __name__)

def validate_json(keys, data, expected_types):
    """Validates request JSON structure."""
    if not isinstance(data, dict):
        return False, "Invalid JSON format"
    
    for key, expected_type in zip(keys, expected_types):
        if key not in data:
            return False, f"Missing required field: {key}"
        if not isinstance(data[key], expected_type):
            return False, f"Invalid type for {key}, expected {expected_type.__name__}"
    
    return True, None

@algorithmBp.route('/binarySearch', methods=['POST'])
def binarySearchApi():
    try:
        data = request.get_json()
        valid, error = validate_json(["array", "target"], data, [list, int])
        if not valid:
            return jsonify({'error': error}), 400
        
        arr = sorted(data['array'])
        target = data['target']
        result = binarySearch(arr, target)

        logAlgorithm('BinarySearch', data, result)
        return jsonify({'index': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@algorithmBp.route('/quickSort', methods=['POST'])
def quickSortApi():
    try:
        data = request.get_json()
        valid, error = validate_json(["array"], data, [list])
        if not valid:
            return jsonify({'error': error}), 400
        
        sortedArr = quickSort(data['array'])
        logAlgorithm('QuickSort', data['array'], sortedArr)

        return jsonify({'sortedArray': sortedArr})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@algorithmBp.route('/bfs', methods=['POST'])
def bfsApi():
    try:
        data = request.get_json()
        valid, error = validate_json(["graph", "start_node"], data, [dict, str])
        if not valid:
            return jsonify({'error': error}), 400

        result = bfs(data['graph'], data['start_node'])
        logAlgorithm('BFS', data, result)

        return jsonify({'bfsTraversal': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

from flask import Flask, request, jsonify
import coffee_advisor
import warnings

warnings.simplefilter("ignore")

app = Flask(__name__)

@app.route('/recommendation', methods=['POST'])
def parse_json():
    try:
        print(request)
        # Get JSON data from the request
        data = request.get_json()
        
        # Extract the required values
        machine = data.get('machine')
        coffee_type = data.get('coffee_type')
        grinder = data.get('grinder')
        coffee_beans = data.get('coffee_beans')
        
        # Check for missing fields
        if not all([machine, coffee_type, grinder, coffee_beans]):
            return jsonify({"error": "Missing one or more required fields: machine, coffee_type, grinder"}), 400
        
        #coffee_advisor.set_api_key()

        # Get coffee advice
        advice = coffee_advisor.get_coffee_advice(coffee_type, coffee_beans, machine, grinder)

        # Return the parsed values
        return jsonify({
            "machine": machine,
            "coffee_type": coffee_type,
            "grinder": grinder,
            "coffee_beans": coffee_beans,
            "advice":advice
        }), 200
    except Exception as e:
        # Handle errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the server
    app.run(debug=True, host='0.0.0.0', port=4000)

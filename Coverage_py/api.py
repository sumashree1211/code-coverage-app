"""
API module for mathematical operations and code coverage.
This module provides an endpoint to generate and download a code coverage report.
"""
import os
import unittest
import time
from flask import Flask, send_file, jsonify
import coverage

app = Flask(__name__)

@app.route('/coverage', methods=['GET'])
def get_coverage():
    """
    Generate and return a code coverage report.
    """
    coverage_file = 'coverage.xml'
    try:
        cov = coverage.Coverage()
        cov.start()

        loader = unittest.TestLoader()
        start_dir = os.path.join(os.path.dirname(__file__), 'tests')
        tests = loader.discover(start_dir=start_dir)
        test_runner = unittest.TextTestRunner(verbosity=2)
        result = test_runner.run(tests)

        if not result.wasSuccessful():
            return jsonify({"error": "Tests failed. Coverage report may be incomplete."}), 500

        cov.stop()
        cov.save()

        cov.xml_report(outfile=coverage_file)

        return send_file(coverage_file, as_attachment=True)
    except FileNotFoundError as e:
        app.logger.error("File not found: %s", e)
        return jsonify({"error": f"File not found: {e}"}), 404
    except IOError as e:
        app.logger.error("I/O error: %s", e)
        return jsonify({"error": f"I/O error: {e}"}), 500
    except RuntimeError as e:
        app.logger.error("Runtime error: %s", e)
        return jsonify({"error": f"Runtime error: {e}"}), 500
    except coverage.CoverageException as e:
        app.logger.error("Coverage error: %s", e)
        return jsonify({"error": f"Coverage error: {e}"}), 500
    except Exception as e:
        app.logger.error("An unexpected error occurred: %s", e)
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500
    finally:
        if os.path.exists(coverage_file):
            try:
                time.sleep(1)
                os.remove(coverage_file)
            except (IOError, OSError) as e:
                app.logger.error("Error removing file: %s", e)

if __name__ == '__main__':
    app.run(debug=True)

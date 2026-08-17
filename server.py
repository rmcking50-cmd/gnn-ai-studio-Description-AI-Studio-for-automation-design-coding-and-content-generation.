"""
Ai-BRAIN-STUDIO Server
A Flask-based server for AI Brain operations with TTS support
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from tts_service import TTSService
import json
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize TTS Service
tts_service = TTSService()

# Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Ai-BRAIN-STUDIO'
    }), 200

# Text to Speech endpoint
@app.route('/api/tts', methods=['POST'])
def text_to_speech():
    """
    Convert text to speech
    
    Request body:
    {
        "text": "Hello world",
        "language": "en",
        "speed": 1.0
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({
                'error': 'Missing required field: text'
            }), 400
        
        text = data.get('text')
        language = data.get('language', 'en')
        speed = data.get('speed', 1.0)
        
        logger.info(f"Processing TTS request: {text[:50]}...")
        
        # Process TTS
        audio_data = tts_service.synthesize(text, language, speed)
        
        return jsonify({
            'status': 'success',
            'audio': audio_data,
            'timestamp': datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        logger.error(f"TTS error: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

# AI Brain Analysis endpoint
@app.route('/api/brain/analyze', methods=['POST'])
def analyze_brain():
    """
    Analyze user input using AI Brain
    
    Request body:
    {
        "input": "user query or text",
        "mode": "chat/analyze/process"
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'input' not in data:
            return jsonify({
                'error': 'Missing required field: input'
            }), 400
        
        user_input = data.get('input')
        mode = data.get('mode', 'chat')
        
        logger.info(f"Brain analysis requested: {user_input[:50]}...")
        
        # Placeholder for AI analysis
        response = {
            'status': 'success',
            'input': user_input,
            'mode': mode,
            'output': f"Processed: {user_input}",
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        logger.error(f"Analysis error: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

# Status endpoint
@app.route('/api/status', methods=['GET'])
def status():
    """Get server and service status"""
    return jsonify({
        'status': 'running',
        'service': 'Ai-BRAIN-STUDIO',
        'version': '1.0.0',
        'tts_available': tts_service.is_available(),
        'timestamp': datetime.now().isoformat()
    }), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Endpoint not found',
        'status': 404
    }), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({
        'error': 'Internal server error',
        'status': 500
    }), 500

if __name__ == '__main__':
    logger.info("Starting Ai-BRAIN-STUDIO server...")
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
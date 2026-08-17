"""
Text-to-Speech Service for Ai-BRAIN-STUDIO
Handles speech synthesis operations
"""

import logging
import base64
from typing import Optional
from gtts import gTTS
from io import BytesIO

logger = logging.getLogger(__name__)

class TTSService:
    """
    Text-to-Speech Service using Google TTS
    Supports multiple languages and speech speeds
    """
    
    # Supported languages
    SUPPORTED_LANGUAGES = {
        'en': 'English',
        'bn': 'Bengali',
        'hi': 'Hindi',
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German',
        'ja': 'Japanese',
        'zh': 'Chinese',
        'ar': 'Arabic',
        'pt': 'Portuguese'
    }
    
    def __init__(self):
        """Initialize TTS Service"""
        self.available = True
        logger.info("TTS Service initialized")
    
    def is_available(self) -> bool:
        """Check if TTS service is available"""
        return self.available
    
    def synthesize(
        self, 
        text: str, 
        language: str = 'en', 
        speed: float = 1.0,
        return_format: str = 'base64'
    ) -> Optional[str]:
        """
        Synthesize text to speech
        
        Args:
            text (str): Text to convert to speech
            language (str): Language code (default: 'en')
            speed (float): Speech speed multiplier (default: 1.0)
            return_format (str): Format for audio data (base64 or bytes)
        
        Returns:
            str or bytes: Audio data in specified format
        """
        try:
            # Validate language
            if language not in self.SUPPORTED_LANGUAGES:
                logger.warning(f"Language '{language}' not supported, using English")
                language = 'en'
            
            # Validate speed
            if not (0.5 <= speed <= 2.0):
                logger.warning(f"Speed {speed} out of range, setting to 1.0")
                speed = 1.0
            
            logger.info(f"Synthesizing text: {text[:50]}... (lang={language}, speed={speed})")
            
            # Generate speech using gTTS
            tts = gTTS(text=text, lang=language, slow=(speed < 1.0))
            
            # Save to BytesIO buffer
            audio_buffer = BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)
            audio_data = audio_buffer.read()
            
            # Return in requested format
            if return_format == 'base64':
                audio_b64 = base64.b64encode(audio_data).decode('utf-8')
                logger.info(f"Successfully synthesized audio (base64 length: {len(audio_b64)})")
                return audio_b64
            else:
                logger.info(f"Successfully synthesized audio (bytes length: {len(audio_data)})")
                return audio_data
        
        except Exception as e:
            logger.error(f"TTS synthesis error: {str(e)}")
            self.available = False
            raise Exception(f"TTS synthesis failed: {str(e)}")
    
    def get_supported_languages(self) -> dict:
        """Get list of supported languages"""
        return self.SUPPORTED_LANGUAGES
    
    def validate_text(self, text: str) -> bool:
        """
        Validate if text is suitable for TTS
        
        Args:
            text (str): Text to validate
        
        Returns:
            bool: True if valid, False otherwise
        """
        if not text:
            logger.warning("Empty text provided")
            return False
        
        if len(text) > 5000:
            logger.warning(f"Text too long ({len(text)} characters)")
            return False
        
        return True
    
    def batch_synthesize(self, texts: list, language: str = 'en') -> list:
        """
        Synthesize multiple texts
        
        Args:
            texts (list): List of texts to synthesize
            language (str): Language code
        
        Returns:
            list: List of audio data in base64 format
        """
        try:
            results = []
            for text in texts:
                if self.validate_text(text):
                    audio = self.synthesize(text, language)
                    results.append({
                        'text': text,
                        'audio': audio,
                        'status': 'success'
                    })
                else:
                    results.append({
                        'text': text,
                        'audio': None,
                        'status': 'invalid'
                    })
            
            logger.info(f"Batch synthesis completed: {len(results)} items processed")
            return results
        
        except Exception as e:
            logger.error(f"Batch synthesis error: {str(e)}")
            raise Exception(f"Batch synthesis failed: {str(e)}")

# Test function
if __name__ == "__main__":
    # Configure logging for testing
    logging.basicConfig(level=logging.INFO)
    
    # Initialize service
    tts = TTSService()
    
    # Test synthesis
    try:
        print("Testing TTS Service...")
        result = tts.synthesize("Hello, this is a test message", language='en')
        print(f"✓ Synthesis successful (audio length: {len(result)} characters)")
        
        # Test supported languages
        langs = tts.get_supported_languages()
        print(f"✓ Supported languages: {len(langs)}")
        
    except Exception as e:
        print(f"✗ Test failed: {str(e)}")
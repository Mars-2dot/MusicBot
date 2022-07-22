from exception.errors.VoiceConnectionError import VoiceConnectionError


class InvalidVoiceChannel(VoiceConnectionError):
    """Exception for cases of invalid Voice Channels."""

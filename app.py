from streamlit_webrtc import webrtc_streamer

webrtc_streamer(
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": True, "audio": False},
    key="neural-style-transfer",
)

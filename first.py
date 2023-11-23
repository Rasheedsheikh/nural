import requests
import neuralspace as ns

filename = 'audio.wav'

# Download the sample audio file
print('Downloading sample audio file...')
resp = requests.get('https://github.com/Rasheedsheikh/nural/blob/main/audio.wav')
with open(filename, 'wb') as fp:
    fp.write(resp.content)


vai = ns.VoiceAI(api_key='sk_357d17f7bb2c960d2d08c0184fece779a8633334d28d930b558ad0577925192d')
# or,
# vai = ns.VoiceAI(api_key='YOUR_API_KEY')

# Setup job configuration
config = {
    'file_transcription': {
        'language_id': 'en',
        'mode': 'fast',
    },
}

# Create a new file transcription job
job_id = vai.transcribe(file=filename, config=config)
print(f'Created job: {job_id}')
# kjhgfcx
# print("asdfg")


# result = vai.get_job_status("4ab734a7-2b1e-496b-9435-802f1489749e")
# print(f'Current status:\n{result}')

# # This should finish in a minute for the sample audio used here.
# # It will depend on the duration of the audio file and other config options.
# print('Waiting for completion...')
# result = vai.poll_until_complete("4ab734a7-2b1e-496b-9435-802f1489749e")
# print(result)
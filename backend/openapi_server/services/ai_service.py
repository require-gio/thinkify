from openai import OpenAI
import os


prompt_map = {
    'summarize': 'Summarize the following notes that I made: \n\n{}',
    'listAsBulletsPoints': 'Summarize the following notes as bullet points: \n\n{}'
}


def transcribe_audio_file(audio_file):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )
    return transcript


def apply_prompt(raw_note, prompt):
    if prompt in prompt_map:
        complete_prompt = prompt_map[prompt].format(raw_note)
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant, skilled in logical combination and writing summaries."},
                {"role": "user", "content": complete_prompt}
            ]
        )
        return response.choices[0].message.content
    else:
        # exception
        raise Exception("Invalid prompt")

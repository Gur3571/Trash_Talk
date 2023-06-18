import get_user_recording
import speech_to_text
import text_model
import text_to_speech
import image_classifier

welcome_speech = "Hi! Welcome to TrashTalk. Enter 1 for speech input. Enter 2 for image input. Enter 3 for text input"

text_to_speech.textToSpeech(welcome_speech)

opt = input(
    "Hi! Welcome to TrashTalk. Enter 1 for speech input. Enter 2 for image input. Enter 3 for text input: ")

colour = ""

if (opt == "1"):
    # audio input

    # get recording of user speaking
    get_user_recording.getUserRecording()

    # convert user speech into text
    item = speech_to_text.getUserSpeechToText('out.wav')

    # get colour from model
    colour = text_model.getBinColourFromText(item)

elif (opt == "2"):
    img = input("Enter image file name: ")

    # image classification output
    colour = image_classifier.image_categorizer(
        r"C:\Users\ambar\Desktop\\" + img + ".jpg")

elif (opt == "3"):
    text = input("Enter garbage item: ")

    colour = text_model.getBinColourFromText(text)


speech = "You should pick the " + colour + " bin."

# convert to speech
text_to_speech.textToSpeech(speech)
print("You should pick the " + colour + " bin.")

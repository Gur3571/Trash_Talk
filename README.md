# Trash-Talk
This is a project my team built for Qhacks 2023 hackathon in Queens University, Kingston, Ontario.

As a newcomer to Canada, one of the difficulties I faced was not preoperly understanding which waste bins to put particular garbage items in.
So we built an application that helps people understanding just that - correct waste segregation.

The app allows users to either describe the object using speech or text, or by taking an image. The output indicates which bin the particular object belongs to.

For the text and speech input, we trained a Natural Language Processing model using Cohere.
For the images, we built a Multi-class Classification Convolutional Neural Network using Keras to detect objects and put them in one of 12 different groups.

To increase accessibilty to users with visual and dexterity impairment, we used Google Text-to-Speech API to input speech and generate audio output

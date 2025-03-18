from transformers import pipeline, Conversation

conversational_pipeline = pipeline("conversational")

conversation_1 = Conversation("Going to the movies tonight - any recommendations?")
conversation_2 = Conversation("What's the weather like in Paris?")

conversational_pipeline([conversation_1, conversation_2])

print(conversation_1)
print(conversation_2)

new_user_input = "and what is the best movie of the year?"

conversation_1.add_user_input(new_user_input)

conversational_pipeline(conversation_1)

print(conversation_1)
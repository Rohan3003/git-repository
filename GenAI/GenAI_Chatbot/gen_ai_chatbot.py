from docx import Document

def read_word_file(file_path):
    doc = Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
        return "\n".join(text)

from transformers import pipeline

qa_pipeline = pipeline("question-answering")

def answer_question(context, question):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

def chatbot():
    file_path = input('Enter file path for your word document : ')
    
    context = read_word_file(file_path)

    print('Chatbot is ready! Ask any questions (type exit to stop.)')


    while True:
        question = input("You: ")
        if question.lower() == 'exit':
            print('Chatbot is shutting down.')
            break
        
        answer = answer_question(context, question)
        print(f"Chatbot: {answer}")

if __name__ == "__main__":
    chatbot()

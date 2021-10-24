from project.document import Document
from project.topic import Topic
from project.category import Category


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        result = '\n'.join([document.__repr__() for document in self.documents])
        return result

    def add_category(self, category:Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self,topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document:Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name:str):
        try:
            searched_category = [category for category in self.categories if category.id == category_id][0]
            searched_category.name = new_name
        except IndexError:
            pass

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        try:
            searched_topic = [topic for topic in self.topics if topic.id == topic_id][0]
            searched_topic.topic = new_topic
            searched_topic.storage_folder = new_storage_folder
        except IndexError:
            pass

    def edit_document(self, document_id: int, new_file_name: str):
        try:
            searched_document = [document for document in self.documents if document_id == document.id][0]
            searched_document.file_name = new_file_name
        except IndexError:
            pass

    def delete_category(self, category_id):
        self.categories = [category for category in self.categories if not category_id == category.id]

    def delete_topic(self, topic_id):
        self.topics = [topic for topic in self.topics if not topic.id == topic_id]

    def delete_document(self, document_id):
        self.documents = [document for document in self.documents if not document.id == document_id]

    def get_document(self, document_id):
        searched_document = [document for document in self.documents if document.id == document_id][0]
        return searched_document.__repr__()





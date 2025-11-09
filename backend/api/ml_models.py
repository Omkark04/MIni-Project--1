import pickle
import pandas as pd

# Load the model and vectorizer
clf_path = "D:\\Mini Project\\MIni-Project--1\\backend\\api\\clf.pkl"
tfidf_path = "D:\\Mini Project\\MIni-Project--1\\backend\\api\\tfidf.pkl"

with open(clf_path, 'rb') as f:
    clf = pickle.load(f)
with open(tfidf_path, 'rb') as f:
    tfidf = pickle.load(f)

class Job_Prediction:
    def __init__(self, data):
        self.data = str(data)
        self.vector = tfidf.transform([self.data])

    def predict(self):
    # Convert sparse matrix to dense if needed
        if hasattr(self.vector, 'toarray'):
            vector_dense = self.vector.toarray()
        else:
            vector_dense = self.vector
        category_mapping = {
            0:"Advocate",
            1: "Arts",
            2: "Automation Testing",
            3: "BlockChain",
            4: "Business Analyst",
            5: "Ciil Engineer",
            6:"Data Science",
            7:"Database Engineer",
            8:"DevOps Engineer",
            9:".Net Engineer",
            10:"ETL Developer",
            11:"Electrical Engineer",
            12:"HR",
            13:"Hadoop",
            14:"Healt and Fitness",
            15:"Java Developer",
            16:"Mechanical Engineer",
            17:"Network Security Engineer",
            18:"Operations Manager",
            19:"PMO",
            20:"Python Developer",
            21:"SAP Developer",
            22:"Sales",
            23:"Tetsing",
            24:"Web Designing",
        }
        return category_mapping.get(clf.predict(vector_dense)[0])
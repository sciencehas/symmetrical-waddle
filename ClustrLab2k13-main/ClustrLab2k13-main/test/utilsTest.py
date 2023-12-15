"""Unit tests for utility functions in the file /symmetrical-waddle/ClustrLab2k13-main/utils.py"""
import unittest
import numpy as np
from .. import utils

class TestUtils(unittest.TestCase):
    def setUp(self):
        pass

    def test_extract_keywords2(self):
        text = "Sample text for test"
        num_keywords = 5
        result = utils.extract_keywords2(text, num_keywords)
        self.assertIsNotNone(result, "Should not be None")

    def test_get_sentence_embeddings(self):
        model = None  # Assuming some model has been trained and available for usage.
        sentences = ["Text sentence one.", "Text sentence two.", "Text sentence three."]
        result = utils.get_sentence_embeddings(model, sentences)
        self.assertIsNotNone(result, "Should not be None")

    def test_get_sentences_from_file(self):
        # Assuming 'test.csv' is an existent single-column CSV file in the application root
        st = None # Streamlit instance should be used here
        with open('test.csv', 'r') as file:
            result = utils.get_sentences_from_file(st, file)
            self.assertIsNotNone(result, "Should not be None")

    def test_get_embeddings_from_sentences(self):
        st = None  # Streamlit instance should be used here
        model = None  # Assuming some model has been trained and available for usage.
        sentences = ["Text sentence one.", "Text sentence two.", "Text sentence three."]
        batch_size = 2
        result = utils.get_embeddings_from_sentences(st, model, sentences, batch_size)
        self.assertIsInstance(result, np.ndarray, "output should be a numpy array")

    def test_get_sentence_chunks(self):
        embeddings = np.array([[1, 1], [2, 2], [3, 3]])
        sentences = ["Text sentence one.", "Text sentence two.", "Text sentence three."]
        threshold = 0.5
        result = utils.get_sentence_chunks(embeddings, sentences, threshold)
        self.assertIsInstance(result, list)

    def test_get_cluster_descriptions(self):
        n_visual_clusters = 2
        cluster_labels = [0, 1, 0, 1, 0]
        chunks = ['chunk1', 'chunk2', 'chunk3']
        result = utils.get_cluster_descriptions(n_visual_clusters, cluster_labels, chunks)
        self.assertIsInstance(result, list)
        
    def test_plot_data(self):
        pass  # This function is related to drawing using matplotlib, no return for testing

    def test_order_scores(self):
        scores = [0.5, 0.2, 0.8]
        score_labels = [0, 1, 2]
        ordered_labels = [0, 2, 1]
        result = utils.order_scores(scores, score_labels, ordered_labels)
        expected = [0.5, 0.8, 0.2]
        self.assertEqual(result, expected)

    def test_calculate_one_shot_embeddings(self):
        st = None  # Streamlit instance should be used here
        texts = ["Text one.", "Text two.", "Text three."]
        labels = ["label1", "label2", "label3"]
        batch_size = 2
        result = utils.calculate_one_shot_embeddings(st, texts, labels, batch_size)
        self.assertIsInstance(result, np.ndarray)

    def test_get_visual_clusters(self):
        chunk_embeddings = np.array([[1, 1], [2, 2], [3, 3]])
        n_visual_clusters = 2
        result = utils.get_visual_clusters(chunk_embeddings, n_visual_clusters)
        self.assertIsInstance(result, np.ndarray)

if __name__ == '__main__':
    unittest.main()
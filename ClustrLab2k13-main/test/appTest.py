import unittest
from twisted.python.test.test_ionotify import ProcessEnvironment
from symmetrical_waddle.ClustrLab2k13_main.app import process_file, main 

class AppTest(unittest.TestCase):

    def setUp(self):
        self.app = ProcessEnvironment(App)
        self.sample_file = "./sample_file.txt"

    def test_process_file(self):
        with open(self.sample_file, 'w') as f:
            f.write("This is a test file for the app.\n")
            f.write("Another line in the test file.\n")
        
        input_file = open(self.sample_file, 'r')
        use_zero_shot_embeddings = False
        zero_shot_labels = None
        batch_size = 64
        threshold = 0.1
        n_visual_clusters = 8
        status_message = "status_message"
        result = process_file(input_file, use_zero_shot_embeddings, zero_shot_labels, batch_size, threshold, n_visual_clusters, status_message)
        self.assertIsInstance(result, type(None))

    def test_main(self):
        result = main()
        self.assertIsInstance(result, type(None))

    def tearDown(self):
        self.app.dispose()
        os.remove(self.sample_file)

if __name__ == '__main__':
    unittest.main()

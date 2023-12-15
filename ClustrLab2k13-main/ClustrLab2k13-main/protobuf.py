# This is a new file created as per instruction catering the task related to protobuf
import google.protobuf.text_format as txtfmt

class ProtoBufHandler:

    def __init__(self, file_name):
        self.file_name = file_name

    def write_to_protobuf(self, protobuf_obj):
        """
        This function writes to protobuf file from given protobuf object
        """
        with open(self.file_name, 'w') as f:
            txtfmt.Print(protobuf_obj, f)

    def read_from_protobuf(self, message):
        """
        This function reads from protobuf file into given message object
        """
        with open(self.file_name, 'r') as f:
            txtfmt.Merge(f.read(), message)
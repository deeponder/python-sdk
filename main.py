import logging
import os
import json

import deepwisdom as dw


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    dataset = dw.Dataset.create_from_file("/Users/up/Downloads/data_upload_test.csv", 0)
    print(dataset.dataset_id)






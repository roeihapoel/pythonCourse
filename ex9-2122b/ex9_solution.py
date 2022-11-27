''' Exercise #9. Python for Engineers.'''

import numpy as np
import imageio
import matplotlib.pyplot as plt


#########################################
# Question 1 - do not delete this comment
#########################################

def load_training_data(weights_file, heights_file):
    try:

        weights_file = open(weights_file, "r")
        heights_file = open(heights_file, "r")

        #weights file
        weights_dict = {}
        weights_text = weights_file.read()
        if weights_text.endswith(""):
            weights_text = weights_text[:-1]
        weights_lists = [row.split(",") for row in weights_text.split("\n")]
        weights_mat = np.array(weights_lists, dtype="object")
        weights_dict["data"] = weights_mat[1:, 1:]
        weights_dict["column_names"] = weights_mat[0, 1:]
        weights_dict["row_names"] = weights_mat[1:, 0]

        #heights file
        heights_text = heights_file.read()
        if heights_text.endswith(""):
            heights_text = heights_text[:-1]
        heights_lists = [row.split(",") for row in heights_text.split("\n")]
        heights_mat = np.array(heights_lists, dtype="object")
        heights_dict = {arr[0]: arr[1] for arr in heights_mat[1:]}

        heights_file.close()
        weights_file.close()
        return weights_dict, heights_dict
    except :
        return {}, {}

def get_highest_weight_loss(data_dict):
    return data_dict["row_names"][((data_dict["data"][:, 0].astype(float) - data_dict["data"][:, -1].astype(float)).argmax())]


def get_bmi(weights_data, heights_data):
    all_bmis = []
    for i, name in enumerate(weights_data["row_names"]):
        height = int(heights_data[name])
        bmis = []
        for weight in weights_data["data"][i]:
            bmis.append(round(float(weight) / ((height / 100) ** 2), 2))
        all_bmis.append(bmis)
    return np.array(all_bmis)


def get_bmi_diff(weights_data, heights_data):

    first_bmis = get_bmi(weights_data, heights_data)
    zeros = np.zeros(first_bmis.shape[0])
    second_bmis = np.c_[first_bmis, zeros][:, 1:]
    return (second_bmis - first_bmis)[:, :-1]


def get_highest_bmi_loss_month(weights_data, heights_data):
    all_diff = get_bmi_diff(weights_data, heights_data)
    idx = np.apply_along_axis(np.sum, 0, all_diff).argmin()
    return weights_data["data"][idx].astype(float)

def get_relative_diff_table(weights_data, heights_data):
    first_bmis = get_bmi(weights_data, heights_data)
    zeros = np.zeros(first_bmis.shape[0])
    second_bmis = np.c_[first_bmis, zeros][:, 1:]
    return np.around(((second_bmis - first_bmis)/first_bmis)[:, :-1], decimals=3)



#########################################
# Question 2 - do not delete this comment
#########################################

def compute_entropy(img):
    image = imageio.imread(img)
    arr = np.arange(256)
    unique, counts = np.unique(image, return_counts=True)
    value_counts = np.array((unique, counts)).T
    dict_counts = {}
    for value in arr:
        # find_count
        ok = False
        for count in value_counts:
            if count[0] == value:
                dict_counts[value] = count[1]
                ok = True
        if not ok:
            dict_counts[value] = 0

    sum_all = image.shape[0] * image.shape[1]
    sum_pi = 0
    for num in arr:
        pi = dict_counts[num] / sum_all
        if pi > 0:
            sum_pi += - (pi * np.log2(pi))
    return round(sum_pi, 4)


#########################################
# Question 3 - do not delete this comment
#########################################

def load_image_as_matrix(img_path):
    return imageio.imread(img_path)

def binarize_matrix(mat):
    new_mat = np.zeros(mat.shape, np.uint8)
    new_mat[mat > 128] = 1
    return new_mat

def compress_flatten_rle(mat):

    mat_flatten = mat.flatten()
    vector = []
    if mat_flatten[0] == 1:
        vector.append(0)
    last = mat_flatten[0]
    counter = 1
    for val in mat_flatten[1:]:
        if last == val:
            counter += 1
        else:
            vector.append(counter)
            last = val
            counter = 1
    vector.append(counter)
    return np.array(vector), mat.shape
 
def decompress_flatten_rle(mat_rle_compressed, shape):
    vector = []
    value = 0
    for counter in mat_rle_compressed:
        vector.extend([value] * counter)
        if value == 0:
            value = 1
        else:
            value = 0
    return np.array(vector).reshape(shape)


def calc_compression_ratio(mat_rle_compressed, mat):
    return round(len(mat_rle_compressed) / len(mat), 2)

    
if __name__ == '__main__':

      print('==== Q1: Basic tests/output====')
      weights, heights = load_training_data("weights.csv", "heights.csv")
      print(f'load_training_data:\n {weights}\nheight_data: {heights}\n======')
      print(f'get_highest_weight_loss:\n {get_highest_weight_loss(weights)}\n======')
      print(f'get_bmi:\n {get_bmi(weights, heights)}\n======')
      print(f'get_bmi_diff:\n {get_bmi_diff(weights, heights)}\n======')
      print(f'get_highest_bmi_loss_month:\n {get_highest_bmi_loss_month(weights, heights)}\n======')
      print(f'get_relative_diff_table:\n {get_relative_diff_table(weights, heights)}\n======')


      print('==== Q2: Write your sanity check/output here!====')
      print(compute_entropy('rick_and_morty_gray.png'))

      print('==== Q3: Basic/output====')

      img_original=load_image_as_matrix('rick_and_morty_gray.png')
      img=binarize_matrix(img_original)
      mat_rle_compressed, shape=compress_flatten_rle(img)
      mat_rle_decompressed=decompress_flatten_rle(mat_rle_compressed, shape)

      fig, axs= plt.subplots(1, 3, figsize=(30,10))
      axs[0].set_title("original_image")
      axs[0].imshow(img_original,cmap = plt.cm.gray)
      axs[1].set_title("binarized_image")
      axs[1].imshow(img,cmap = plt.cm.gray)
      axs[2].set_title("decompressed_image")
      axs[2].imshow(mat_rle_decompressed,cmap = plt.cm.gray)
      plt.show()

      print(f'Are decompreseed and original matrices identical? {np.all((img==mat_rle_decompressed))}')
      print(f'calc_compression_ratio: {calc_compression_ratio(mat_rle_compressed, img)}')


      img_original=np.array([[0,0,0,0,200,200,0,0,0,0,0,200,200,0,0,0,0],
                    [0,0,0,200,200,200,200,0,0,0,200,201,200,200,0,0,0],
                    [0,0,200,1,1,1,1,200,0,200,200,200,1,1,200,0,0],
                    [0,200,1,100,1,101,1,200,200,1,1,1,1,101,1,200,0],
                    [0,200,1,1,1,200,1,1,1,21,1,101,1,150,1,200,0],
                    [0,200,1,101,100,1,100,1,10,1,1,100,100,1,1,200,0],
                    [0,200,1,200,1,201,1,1,1,1,201,1,1,100,1,200,0],
                    [0,200,1,1,1,1,1,21,1,1,1,1,21,1,1,200,0],
                    [0,0,200,1,101,1,1,1,250,1,200,1,1,1,200,0,0],
                    [0,0,0,200,200,1,200,1,1,1,1,10,1,200,0,0,0],
                    [0,0,0,0,200,1,1,1,1,10,1,1,200,0,0,0,0],
                    [0,0,0,0,0,170,1,10,1,1,1,200,0,0,0,0,0],
                    [0,0,0,0,0,0,230,1,1,1,200,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,200,1,200,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,200,0,0,0,0,0,0,0,0]])

      img=binarize_matrix(img_original)
      mat_rle_compressed, shape=compress_flatten_rle(img)
      mat_rle_decompressed=decompress_flatten_rle(mat_rle_compressed, shape)
      print(f'Are decompreseed and original matrices identical? {np.all((img==mat_rle_decompressed))}')
      print(f'calc_compression_ratio: {calc_compression_ratio(mat_rle_compressed, img)}')

      fig, axs= plt.subplots(1, 3, figsize=(30,10))
      axs[0].set_title("original_image")
      axs[0].imshow(img_original,cmap = plt.cm.gray)
      axs[1].set_title("binarized_image")
      axs[1].imshow(img,cmap = plt.cm.gray)
      axs[2].set_title("decompressed_image")
      axs[2].imshow(mat_rle_decompressed,cmap = plt.cm.gray)
      plt.show()

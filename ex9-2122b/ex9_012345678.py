''' Exercise #9. Python for Engineers.'''

import numpy as np
import imageio
import matplotlib.pyplot as plt


#########################################
# Question 1 - do not delete this comment
#########################################

def load_training_data(weights_file, heights_file):
    pass


def get_highest_weight_loss(data_dict):
    pass


def get_bmi(weights_data, heights_data):
    pass     


def get_bmi_diff(weights_data, heights_data):
    pass


def get_highest_bmi_loss_month(weights_data, heights_data):
    pass

def get_relative_diff_table(weights_data, heights_data):
    pass



#########################################
# Question 2 - do not delete this comment
#########################################

def compute_entropy(img):
    pass


#########################################
# Question 3 - do not delete this comment
#########################################

def load_image_as_matrix(img_path):
    pass

def binarize_matrix(mat):
    pass

def compress_flatten_rle(mat):
    pass
 
def decompress_flatten_rle(mat_rle_compressed, shape):
    pass

def calc_compression_ratio(mat_rle_compressed, mat):
    pass

    
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

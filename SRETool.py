from skimage.metrics import structural_similarity
from skimage.io import imread
from skimage.transform import rescale, resize, downscale_local_mean
from skimage.viewer import ImageViewer
import pandas as pd
import numpy
import time


class SRETool:
    def __convert_similarity_score(self, score):
        """
        Converts the similarity score from a scale of [-1,1] to [2,0]
        """
        if 0 < score <= 1:
            new_score = (score - 1) * (-1)
        elif score <= 0:
            new_score = abs(score) + 1
        return new_score

    def compare_images(self, df):
        """
        Compare the images by their similarity and calculate the cost of computing them
        """
        score_list = []
        elapsed_list = []
        for index,row in df.iterrows():
            start_time = time.time()
            image1 = imread(row['image1'],as_gray="True")
            image2 = imread(row['image2'],as_gray="True")
            if(image1.shape != image2.shape):
                image2 = resize(image2, (image1.shape)) # if images are of different dimensions, crop the second image based on first
            score = structural_similarity(image1, image2)
            new_score = self.__convert_similarity_score(score)
            elapsed_time = (time.time() - start_time)
            score_list.append(round(new_score,2))
            elapsed_list.append(elapsed_time)
        output_df = self.__create_output_csv(df, score_list, elapsed_list)
        return output_df

    def __create_output_csv(self, df, score_list, elapsed_list):
        """
        Create output csv file with similarity score and elapsed time 
        """
        df['Similar']=score_list
        df['Elapsed']=elapsed_list
        df.to_csv('Output.csv',index=False)
        return df

def main():
    df = pd.read_csv('Input.csv')
    obj = SRETool()
    obj.compare_images(df)


if __name__ == "__main__":
    main()

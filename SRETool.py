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
        old_scale = [-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
        new_scale = [2.0,1.9,1.8,1.7,1.6,1.5,1.4,1.3,1.2,1.1,1.0,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0]
        score_dict = dict(zip(old_scale, new_scale))
        new_score = score_dict[score]
        return new_score

    def compute_similarity_score(self, df):
        """
        Compute the structural similarity score and elapsed time for the image pairs and create output csv file
        """
        score_list = []
        elapsed_list = []
        for index,row in df.iterrows():
            print("index is :", index)
            print("row is :", row)
            start_time = time.time()
            image1 = imread(row['image1'],as_gray="True")
            image2 = imread(row['image2'],as_gray="True")
            print("Array 1 is :" ,image1)
            print("Array 2 is :", image2)
            print()
            print(image1.shape)
            print(image2.shape)
            if(image1.shape != image2.shape):
                image2 = resize(image2, (image1.shape)) # if images are of different dimensions, crop the second image based on first
            score = structural_similarity(image1, image2)
            new_score = self.__convert_similarity_score(round(score,1))
            print()
            print(new_score)
            elapsed_time = (time.time() - start_time)
            print(elapsed_time)
            score_list.append(new_score)
            elapsed_list.append(elapsed_time)
        output_df = self.__create_output_csv(df, score_list, elapsed_list)
        return output_df

    def __create_output_csv(self, df, score_list, elapsed_list):
        """
        Add the similarity score and elapsed time as columns to the dataframe and convert it to a csv
        """
        df['Similar']=score_list
        df['Elapsed']=elapsed_list
        df.to_csv('Output.csv',index=False)
        return df

def main():
    df = pd.read_csv('Input.csv')
    obj = SRETool()
    obj.compute_similarity_score(df)


if __name__ == "__main__":
    main()

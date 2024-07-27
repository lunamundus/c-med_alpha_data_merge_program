import os
import glob
import datetime
import pandas as pd

def process_files(directory_path):
    output_file_path = directory_path + '/' + 'modified_files'
    
    # if output folder is not exist, make new folder
    if not os.path.exists(output_file_path):
        os.makedirs(output_file_path)
    
    # modify all files in directory path
    for filename in os.listdir(directory_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory_path, filename)
                        
        # read file and remove unnecessary commas
        with open(file_path, 'r') as file:
            modified_lines = [line.rstrip(',\n') for line in file]
        
        # save the modified file to a new file
        modified_file_path = os.path.join(output_file_path, filename)
        with open(modified_file_path, 'w') as modified_file:
            modified_file.write('\n'.join(modified_lines))
    
    return output_file_path

def merge_files_in_directory(directory_path, progress_bar):
    files_path = process_files(directory_path)
    
    # get all csv files path in modified_files directory
    csv_files = glob.glob(os.path.join(files_path, "*.csv"))
    
    # initialize dataframes list
    dataframes = []
    
    # read csv files and add to dataframes list
    for file in csv_files:
        df = pd.read_csv(file)
        dataframes.append(df)
    
    # find base dataframe
    max_length_df = max(dataframes, key=lambda df: len(df['time']))
    
    # initialize progress bar
    progress_bar.setMaximum(len(max_length_df))
    
    # merge dataframes
    merge_df = max_length_df
    for i, df in enumerate(dataframes):
        if not df.equals(max_length_df):
            merge_df = pd.merge(merge_df, df, on='time', how='outer', sort=True)
        progress_bar.setValue(i + 1)
    
    # save merged dataframe to csv file
    current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    save_output_file_path = f'./result/{current_time}_output.csv'
    
    # if output folder is not exist, make new folder
    if not os.path.exists('./result'):
        os.makedirs('./result')
        
    merge_df.to_csv(save_output_file_path, index=False)

# test function code    
# directory_path = './sample_data/'
# merge_files_in_directory(directory_path)

# print("파일 병합이 완료되었습니다.")
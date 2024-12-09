import pandas as pd

def create_df(dataset, metadata_col):
    columns = dataset.columns.tolist()
    cells = []
    metadata_dict = {}
    for idx, col in enumerate(metadata_col):
        col_split = col.split(", ")
        cell = col_split[2].split(" [")[0]
        label = col_split[1]
        if cell in columns:
            metadata_dict[idx] = ["cell_"+cell, label]
            cells += [cell]
    metadata_df = pd.DataFrame(metadata_dict).T
    dataset_df = dataset.add_prefix("cell_")
    return dataset_df, metadata_df


def get_subset_dataframes(dataset, metadata, labels):
    subset_metadata = metadata[metadata['Label'].isin(labels)]
    subset_dataset = dataset[['cell_ID_REF'] + subset_metadata['Cell Name'].values.tolist()]
    return subset_dataset, subset_metadata


if __name__ == "__main__":
    dataset = pd.read_csv("GSE140829_final_normalized_data.csv")
    metadata = pd.read_csv("GSE140829_final_normalized_metadata.csv")
    dataset_df, metadata_df = create_df(dataset, metadata['Title'].to_list())
    
    dataset_df.to_csv("RNA_data.csv", index=False)
    metadata_df.to_csv("Metadata.csv", index=False)

    '''
    new_metadata_df = pd.read_csv("Metadata.csv")
    new_rna_df = pd.read_csv("RNA_data.csv")
    
    new_metadata_df = new_metadata_df.rename(columns={'0': 'Cell Name', '1': 'Label'})

    pairs_dict = {"MCI_comparison": ['Control', 'MCI'],
                  "AD_comparison": ['Control', 'AD'],
                  }
    
    for pair in pairs_dict:
        subset_df, subset_metadata_df = get_subset_dataframes(new_rna_df, new_metadata_df, pairs_dict[pair])
        subset_df.to_csv(f"RNA_data_{pair}.csv", index=False)
        subset_metadata_df.to_csv(f"metadata_{pair}.csv", index=False)
    '''
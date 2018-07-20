import config
from transporter import s3_process


def get_inv_input_folders():
    """
    """
    # dict_folders = {}
    folders = s3_process.get_folder_listing(config.INV_BUCKET, config.PREFIX_INV_IN_FOLDER)
    return [(folder, folder) for folder in folders]

    # for fo in folders:
    #     dict_folders[fo] = fo
    #
    # return dict_folders

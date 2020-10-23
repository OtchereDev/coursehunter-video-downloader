
from tqdm import tqdm

def download_and_save_iterator(r, chunk_size, total_size, title, isGUI=False, window=None, element={}):
    with open(title, 'wb') as f:
        if isGUI:
            curr_chunk = 0
            for data in r.iter_content(chunk_size=chunk_size):
                curr_chunk += 1
                # Calculate the current percentage
                download_percentage = ((chunk_size * (curr_chunk + 1)) / total_size) * 100
                window[element['progress_bar_key']].update(download_percentage)
                window[element['percent_key']].update(download_percentage)
                f.write(data)

        else:
            for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size),
                total= total_size/chunk_size, unit='KB'):

                f.write(data)
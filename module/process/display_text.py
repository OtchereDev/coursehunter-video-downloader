def display_text(text, window=None, information_field=None):
    if window:
        window[information_field].update(text)
    else:
        print(text)
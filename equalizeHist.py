def df(img):  # to make a histogram (count distribution frequency)
    values = [0]*256
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            values[img[i,j]]+=1
    return values


def cdf(hist):  # cumulative distribution frequency
    cdf = [0] * len(hist)   #len(hist) is 256
    cdf[0] = hist[0]
    for i in range(1, len(hist)):
        cdf[i]= cdf[i-1]+hist[i]
    # Now we normalize the histogram
    cdf = [ele*255/cdf[-1] for ele in cdf]      # What your function h was doing before
    return cdf

def equalize_image(image):
    my_cdf = cdf(df(image))
    # use linear interpolation of cdf to find new pixel values. Scipy alternative exists
    import numpy as np
    image_equalized = np.interp(image, range(0,256), my_cdf)
    return image_equalized

import torch
import torch.nn as nn


def image_normalization(norm_type):
    def _inner(tensor: torch.Tensor):
        if norm_type == 'nomalization':
            return tensor / 255.0
        elif norm_type == 'denormalization':
            return (tensor * 255.0).type(torch.FloatTensor)
        else:
            raise Exception('Unknown type of normalization')
    return _inner

def get_psnr(image,gt,max=255):
    psnr = 10 * torch.log10(max**2 / torch.mean((image - gt)**2))
    return psnr
    
#include <stdio.h>
#include "c_img.h"
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include"c_img.c"

void change_img_brightness(struct rgb_img *im, float brightness_factor){
    int height = im->height;
    int width = im->width;
    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            int r = get_pixel(im, i, j, 0);
            int g = get_pixel(im, i, j, 1);
            int b = get_pixel(im, i, j, 2);
            set_pixel(im, i, j, r * brightness_factor, g * brightness_factor, b * brightness_factor);
        }
    }
}

int main(){
    struct rgb_img *im;
    read_in_img(&im, "image.bin");
    int height = im->height;
    int width = im->width;
    change_img_brightness(im, 0.1);
    write_img(im, "new_image.bin");
}
clear;
close all;

image_name = 'img093';

image_dir = {'DRCN'};
% image_dir = {'BFLP'};

patch_position = [118,111]; %1
patch_scalar = 0.15;


if ~isdir(image_name)
    mkdir(image_name);
end 

for ii = 1:numel(image_dir)
    image = imread(fullfile(image_dir{ii},[image_name '.png']));
    
    if ndims(image)== 2
        image = cat(3, image, image, image);
    end
    patch_size = [round(patch_scalar*size(image,1)),round(patch_scalar*size(image,1))];
    patch = image(patch_position(1):patch_position(1)+patch_size(1),patch_position(2):patch_position(2)+patch_size(2),:);
    patch_big = imresize(patch,[round(size(image,1)*0.6),round(size(image,2)*0.6)],'bicubic');
    
    figure;
    imshow(patch);
    title([image_dir{ii} '_patch']);
    
    mark_image = image;
    mark_image(patch_position(1)-2:patch_position(1)+patch_size(1)+2,patch_position(2)-2:patch_position(2)+patch_size(2)+2,1) = 255;
    mark_image(patch_position(1)-2:patch_position(1)+patch_size(1)+2,patch_position(2)-2:patch_position(2)+patch_size(2)+2,2) = 0;
    mark_image(patch_position(1)-2:patch_position(1)+patch_size(1)+2,patch_position(2)-2:patch_position(2)+patch_size(2)+2,3) = 0;
    mark_image(patch_position(1):patch_position(1)+patch_size(1),patch_position(2):patch_position(2)+patch_size(2),:) = patch;
    figure;
    imshow(mark_image);
    title([image_dir{ii} '_markimage']);
    
    imwrite(patch,fullfile(image_name,[image_dir{ii} '_patch.bmp']));
    imwrite(mark_image,fullfile(image_name,[image_dir{ii} '.bmp']));
end

% close all
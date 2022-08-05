clear all
%close all

% initial scan
bag_init    = rosbag('2022-08-05-13-28-46.bag');

bSel_init   = select(bag_init,'Topic','/point_cloud_data2');

msgStructs_init = readMessages(bSel_init,'DataFormat','struct');

k_init = 1;
X_init = [];
for i = 1:size(msgStructs_init)
    for j = 1:3:(size(msgStructs_init{i}.Data)-3)
        X_init(k_init) = msgStructs_init{i}.Data(j);
        Y_init(k_init) = msgStructs_init{i}.Data(j+1);
        Z_init(k_init) = msgStructs_init{i}.Data(j+2);
        k_init= k_init+1;
    end
end

figure
ptCloud = pointCloud([-X_init(:),-Y_init(:),Z_init(:)]);
ptCloudIn = ptCloud;
ptCloudOut = pcdownsample(ptCloudIn,'gridAverage',0.0005);
pcshow(ptCloudOut)
pcwrite(ptCloudOut,'Brick_Cloud_5.ply')




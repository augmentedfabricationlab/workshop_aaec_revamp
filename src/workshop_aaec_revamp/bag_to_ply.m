function p = bag_to_ply(bagpath, plypath)
%     bagfile = "C:\Users\Gido\Documents\workspace\development\workshop_aaec_revamp\matlab_file\2022-08-05-13-28-46.bag";
%     plyfile = "C:\Users\Gido\Documents\workspace\development\workshop_aaec_revamp\matlab_file\test_bag_to.ply";
    bagfile = bagpath;
    plyfile = plypath;
    bag = rosbag(bagfile);
    pc_data = select(bag,'Topic','/point_cloud_data2');
    msg_structs = readMessages(pc_data,'DataFormat','struct');

    k = 1;
    for i = 1:size(msg_structs)
        for j = 1:3:(size(msg_structs{i}.Data)-3)
            xvals(k) = msg_structs{i}.Data(j);
            yvals(k) = msg_structs{i}.Data(j+1);
            zvals(k) = msg_structs{i}.Data(j+2);
            k= k+1;
        end
    end
    ptCloud = pointCloud([-xvals(:),-yvals(:),zvals(:)]);
    ptCloudOut = pcdownsample(ptCloud,'gridAverage',0.0005);
    pcwrite(ptCloudOut,plyfile);
    p = true;
end
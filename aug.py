import cv2 

marker_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)

# MARKER_SIZE = 400

# for id in range(20):
#     marker_image = cv2.aruco.drawMarker(marker_dict, id, MARKER_SIZE)
#     cv2.imshow("img", marker_image)
#     cv2.imwrite(f"markers/marker_{id}.png", marker_image)
#     # cv2.waitKey(0)
#     # break


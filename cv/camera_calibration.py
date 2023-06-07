# camera have distorsion
# - radial from non perfect pinhole lens
# - tangential because lens and image plane are not parallel

# 3d points are object points
# 2d points are image points

import numpy as np
import cv2 as cv
import glob
# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob("data/left*.jpg")
for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (7,6), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (7,6), corners2, ret)
        # cv.imshow('img', img)
        # cv.waitKey(1000)
        # cv.destroyAllWindows()
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

img = cv.imread('data/left12.jpg')
h,  w = img.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

# undistort
dst = cv.undistort(img, mtx, dist, None, newcameramtx)
# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv.imwrite('data/calibresult.png', dst)

img = cv.imread('data/ow2.png')
img = cv.resize(img, (480,680))
h,  w = img.shape[:2]
mtx2 = np.array([(355.1282804447468, 0, 320.71130519009984),
                   (0, 353.7572158125747, 260.3658563222029),
                   (0, 0, 1)])
dist2 = np.array([-0.3446166115387546,
0.16181089795150944,
-0.00025668894243022233,
0.0017897240418724865,
-0.04944665232808982])
newcameramtx2, roi = cv.getOptimalNewCameraMatrix(mtx2, dist2, (w,h), 1, (w,h))
dst = cv.undistort(img, mtx2, dist2)
print(h, w)
cv.imwrite('data/calibresult2.png', dst)
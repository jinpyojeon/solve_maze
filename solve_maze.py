import cv2
import numpy as np

def find_maze_wall(mat):
	mat = cv2.GaussianBlur(mat, (5,5), 1)

	grey = cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)	

	_, white_thres = cv2.threshold(grey, 0, 255, cv2.THRESH_OTSU)

	
	# cv2.imshow('e', white_thres)
	# cv2.waitKey(0)
	
	thresholded = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 0)

	thresholded = cv2.bitwise_and(thresholded, white_thres)

	edges = cv2.Canny(thresholded, 0, 30)

	cv2.imshow('e', edges)
	cv2.waitKey(0)

	_ret, contours, hierarchy  = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	# hull = cv2.convexHull(contours)

	# print contours

	# contour_area_list = [[cv2.boundingRect(contours[i]).size , i] for i, x in enumerate(hierarchy[0])]

	# #print contour_area_list

	# largest = max(contour_area_list, key=lambda p: p[0])

	# print largest[1]

	# print cv2.contourArea(contours[largest[0]])

	black = np.zeros(mat.shape, dtype="uint8")
	
	cv2.drawContours(black, contours, -1, (255, 255, 255), 3)	

	cv2.imshow('d',black)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	cv2.waitKey(1)

def main():
	input_mat = cv2.imread('img.jpeg')
	find_maze_wall(input_mat)

if __name__ == "__main__":
	main()
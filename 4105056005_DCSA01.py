import cv2
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

filename = input('請輸入檔案名稱(例如:dog.bmp):')
try:
	im = cv2.imread(filename)
	#讀取RGB中0-255的數據
	BHist = cv2.calcHist([im], [0], None,[256],[0,256])
	GHist = cv2.calcHist([im], [1], None,[256],[0,256])
	RHist = cv2.calcHist([im], [2], None,[256],[0,256])
	#繪製曲線圖
	plt.plot(BHist,color='b')
	plt.plot(GHist,color='g')
	plt.plot(RHist,color='r')
	plt.show()

	#轉為一維陣列與整數
	RHist = np.hstack(RHist.astype(np.int64))
	GHist = np.hstack(GHist.astype(np.int64))
	BHist = np.hstack(BHist.astype(np.int64))

	#讀取平均值和標準差
	mean, std = cv2.meanStdDev(im)
	mean = np.hstack(np.around(mean, decimals=2))
	std = np.hstack(np.around(std, decimals=2))

	#儲存為CSV檔案
	csvName = filename.split('.')[0]+".csv"
	with open(csvName, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['Index', 'R', 'G', 'B'])
		for i in range(256):
			writer.writerow([i, RHist[i], GHist[i], BHist[i]])
		writer.writerow(["Mean", mean[2], mean[1], mean[0]])
		writer.writerow(["STD", std[2], std[1], std[0]])
	print("CSV檔產生")

except:
	print("檔案不存在")
os.system('pause')
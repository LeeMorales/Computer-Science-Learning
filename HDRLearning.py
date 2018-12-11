def readImagesAndTimes():
  # 曝光时间列表
  times = np.array([ 1/30.0, 0.25, 2.5, 15.0 ], dtype=np.float32)

  # 图像文件名称列表
  filenames = ["img_0.033.jpg", "img_0.25.jpg", "img_2.5.jpg", "img_15.jpg"]
  images = []
  for filename in filenames:
    im = cv2.imread(filename)
    images.append(im)

  return images, times

# 对齐输入图像
alignMTB = cv2.createAlignMTB()
alignMTB.process(images, images)

# 获取图像响应函数 (CRF)
calibrateDebevec = cv2.createCalibrateDebevec()
responseDebevec = calibrateDebevec.process(images, times)
# 将图像合并为HDR线性图像
mergeDebevec = cv2.createMergeDebevec()
hdrDebevec = mergeDebevec.process(images, times, responseDebevec)
# 保存图像
cv2.imwrite("hdrDebevec.hdr", hdrDebevec).0
createTonemapDrago
(
float   gramma = 1.0f,
float   saturation = 1.0f,
float   bias = 0.85f 
)   
# 使用Drago色调映射算法获得24位彩色图像
tonemapDrago = cv2.createTonemapDrago(1.0, 0.7)
ldrDrago = tonemapDrago.process(hdrDebevec)
ldrDrago = 3 * ldrDrago
cv2.imwrite("ldr-Drago.jpg", ldrDrago * 255)
  createTonemapDurand 
(   
  float     gamma = 1.0f, 
  float     contrast = 4.0f,
  float     saturation = 1.0f,
  float     sigma_space = 2.0f,
  float     sigma_color = 2.0f 
);
# 使用Durand色调映射算法获得24位彩色图像
 tonemapDurand = cv2.createTonemapDurand(1.5,4,1.0,1,1)
 ldrDurand = tonemapDurand.process(hdrDebevec)
 ldrDurand = 3 * ldrDurand
 cv2.imwrite("ldr-Durand.jpg", ldrDurand * 255)
createTonemapReinhard
(
float   gamma = 1.0f,
float   intensity = 0.0f,
float   light_adapt = 1.0f,
float   color_adapt = 0.0f 
)
# 使用Reinhard色调映射算法获得24位彩色图像
tonemapReinhard = cv2.createTonemapReinhard(1.5, 0,0,0)
ldrReinhard = tonemapReinhard.process(hdrDebevec)
cv2.imwrite("ldr-Reinhard.jpg", ldrReinhard * 255)
createTonemapMantiuk
(   
float   gamma = 1.0f,
float   scale = 0.7f,
float   saturation = 1.0f 
)   
# 使用Mantiuk色调映射算法获得24位彩色图像
tonemapMantiuk = cv2.createTonemapMantiuk(2.2,0.85, 1.2)
ldrMantiuk = tonemapMantiuk.process(hdrDebevec)
ldrMantiuk = 3 * ldrMantiuk
cv2.imwrite("ldr-Mantiuk.jpg", ldrMantiuk * 255)

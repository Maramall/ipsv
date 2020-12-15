def Find_Object(img):
    ret, im = cv2.threshold(img, 127, 255, 0)
    con, hie = cv2.findContours(im, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for cnt in con:
        #print(con[0])
        #ctp = con [0]
        per = cv2.arcLength(cnt, True)
        area = cv2.contourArea(cnt)
       # print('perimetr: ', per)
       # print('area: ', area)
        cv2.imshow("Bin", im) 
        stci = math.sqrt(area/math.pi)
        stsq = math.sqrt(area)
        sttr = math.sqrt(area*2)
        perci = stci*math.pi*2
        persq = stsq*4
        pertr = sttr*(2+math.sqrt(2))
        if abs(per - perci) < 12:
            print ('1')
        elif abs(per - pertr) < 12:
            print('3')
        elif abs(per - persq) < 12:
            print ('2')
        else:
            print("-1")
   #    print ('circle: ', perci)
   #     print ('triangle: ',pertr)
  #      print ('square: ', persq)

def cross(p1,p2,p3): # 叉积判定
    x1=p2[0]-p1[0]
    y1=p2[1]-p1[1]
    x2=p3[0]-p1[0]
    y2=p3[1]-p1[1]
    return x1*y2-x2*y1     

 def segment(p1,p2,p3,p4): #判断两线段是否相交
  #矩形判定，以l1、l2为对角线的矩形必相交，否则两线段不相交
   if(max(p1[0],p2[0])>=min(p3[0],p4[0]) #矩形1最右端大于矩形2最左端
   and max(p3[0],p4[0])>=min(p1[0],p2[0]) #矩形2最右端大于矩形1最左端
   and max(p1[1],p2[1])>=min(p3[1],p4[1]) #矩形1最高端大于矩形2最低端
   and max(p3[1],p4[1])>=min(p1[1],p2[1])): #矩形2最高端大于矩形1最低端
     if(cross(p1,p2,p3)*self.cross(p1,p2,p4)<=0  
       and cross(p3,p4,p1)*self.cross(p3,p4,p2)<=0):
       D=1
     else:
        D=0
   else:
      D=0
   return D

def check(l1,l2,sq):
  # step 1 check if end point is in the square
  if ( l1[0] >= sq[0] and l1[1] >= sq[1] and  l1[0] <= sq[2] and  l1[1] <= sq[3]) or 
    ( l2[0] >= s1[0] and l2[1] >= s1[1] and  l2[0] <= sq[2] and  l2[1] <= sq[3]):
  return 1
  else:
    # step 2 check if diagonal cross the segment
    p1 = [sq[0],sq[1]]
    p2 = [sq[2],sq[3]]
    p3 = [sq[2],sq[1]]
    p4 = [sq[0],sq[3]]
    if segment(l1,l2,p1,p2) or segment(l1,l2,p3,p4):
      return 1
    else:
      return 0



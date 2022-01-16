###
#setwd("C:\\Users\\phuang\\Documents\\Personal\\Kumon")

digit = 4
q_type = '-'

pdf_w <- 8.5
pdf_h <- 11
n_row <- 6
n_col <- 5
cell_w = pdf_w/n_col
cell_h = pdf_h/n_row

pdf(file="foo.pdf",w=pdf_w,h=pdf_h)
par(mar=c(0, 0, 0, 0))

plot(x = -1,y=-1,xlim=c(0,pdf_w),ylim=c(0,pdf_h))
#plot(x=x,y=y,type="l",xlim=c(0,pdf_w),ylim=c(0,pdf_h))

###

for (row_idx in 1:n_row)
{ 
  for (col_idx in 1:n_col)
  {
    
    
    
    origin_x = cell_w*(col_idx-1)
    print(origin_x)
    origin_y = cell_h*(row_idx-1)+cell_h*0.1
    x1 = origin_x+cell_w/10
    x2 = x1+cell_w/5*4
    y1 = origin_y+cell_h/5
    y2 = y1
    a = sample(1:(10**digit-1), 1)
    b = sample(1:(10**digit-1), 1)
    
    if (q_type == "-")
    {
      num1 = max(a,b)
      num2 = min(a,b)
      a = num1
      b = num2
    }
     
    lines(x=c(x1,x2),y=c(y1,y2),type="l",xlim=c(0,pdf_w),ylim=c(0,pdf_h))
    text(x=origin_x+cell_w/2,y=origin_y+cell_h/5*2.5,labels=sprintf('%s%5d',' ',a),cex=2,family="mono")
    text(x=origin_x+cell_w/2,y=origin_y+cell_h/5*1.5,labels=sprintf('%s%5d',q_type,b),cex=2,family="mono")
    
    
    
  }
  
}
dev.off()


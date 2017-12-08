setwd("D:/Dropbox/working memory/output/exp2")
getwd()
csvpath = "D:/Dropbox/working memory/output/exp2/"
csvfilesn = list.files( path = csvpath, pattern="*.csv")
tmprt = function(rtcsv){
  read.csv( rtcsv, stringsAsFactors = FALSE, header = TRUE)
}
lhudata = lapply(paste(csvpath,csvfilesn, sep = ""), tmprt)
csvfilesn
data = lhudata[[1]]
data['pID'] = NaN
for (sz in seq(18)){
  start = (sz-1) * 480 + 1
  end = sz * 480
  for (i in seq(start,end)){
    data$pID[i] = sz
  }
}
summary(data)
data['ProbeSeq'] = NaN
data['ProbeSeq'] <- c(1, 2)
data$Setsize = data$SZ/2
data$Feedback <-data$PC
data$RT[data$Feedback == 0] = NaN
summary(data)
data$PC[data$RT >= 5] = NaN
summary(data)
data$RT[data$RT >= 5] = NaN
summary(data)
data$PC[data$RT <= 0.3] = NaN
summary(data)
data$RT[data$RT <= 0.3] = NaN
summary(data)
data$Setsize <-data$setsize
data$Setsize <- factor(data$Setsize)
data <- data.frame(aggregate(list(data$Feedback, data$RT), 
                             list(data$pID, data$Setsize, data$ProbeType, data$CSI, data$ProbeSeq)#,data$SZchange,                                  data$CSIchange,data$trialvalid),
                             ,mean, na.rm = TRUE))
names(data) <- c('pID', 'Setsize', 'ProbeType', 'CSI', 'ProbeSeq','PC', 'RT')#,'SZchange','CSIchange','trailvalid', 
summary(data)
tapply(data$PC, data$Setsize, summary)
tapply(data$PC, data$ProbeType, summary)
tapply(data$PC, data$CSI, summary)
tapply(data$PC, data$ProbeSeq, summary)
tapply(data$RT, data$Setsize, summary)
tapply(data$RT, data$ProbeType, summary)
tapply(data$RT, data$CSI, summary)
tapply(data$RT, data$ProbeSeq, summary)


library(BayesFactor)
# Multiple plot function
#
# ggplot objects can be passed in ..., or to plotlist (as a list of ggplot objects)
# - cols:   Number of columns in layout
# - layout: A matrix specifying the layout. If present, 'cols' is ignored.
#
# If the layout is something like matrix(c(1,2,3,3), nrow=2, byrow=TRUE),
# then plot 1 will go in the upper left, 2 will go in the upper right, and
# 3 will go all the way across the bottom.
#
multiplot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
  library(grid)
  
  # Make a list from the ... arguments and plotlist
  plots <- c(list(...), plotlist)
  
  numPlots = length(plots)
  
  # If layout is NULL, then use 'cols' to determine layout
  if (is.null(layout)) {
    # Make the panel
    # ncol: Number of columns of plots
    # nrow: Number of rows needed, calculated from # of cols
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                     ncol = cols, nrow = ceiling(numPlots/cols))
  }
  
  if (numPlots==1) {
    print(plots[[1]])
    
  } else {
    # Set up the page
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))
    
    # Make each plot, in the correct location
    for (i in 1:numPlots) {
      # Get the i,j matrix positions of the regions that contain this subplot
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))
      
      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}


data$ProbeType <- as.character(data$ProbeType)
data$ProbeType[data$ProbeType == '0'] <- 'Positive'
data$ProbeType[data$ProbeType == '1'] <- 'Intrusion'
data$ProbeType[data$ProbeType == '2'] <- 'New'

data$pID <- factor(data$pID)
data$Setsize <-factor(data$Setsize)
data$ProbeType <- factor(data$ProbeType)
summary(data)
head(data)
sz.pt2 <- anovaBF(PC ~ Setsize* ProbeType + pID, data = data, whichRandom = 'pID')
sz.pt2
sz.pt2[4]/sz.pt2[3]
data$CSI <- factor(data$CSI)
sz.CSI2 <- anovaBF(PC ~ Setsize* CSI + pID, data = data, whichRandom = 'pID')
sz.CSI2
sz.CSI2[4]/sz.CSI2[3]
pt.CSI2 <- anovaBF(PC ~ ProbeType* CSI + pID, data = data, whichRandom = 'pID')
pt.CSI2
pt.CSI2[4]/pt.CSI2[3]
data$ProbeSeq <-factor(data$ProbeSeq)
ps.CSI2 <- anovaBF(PC ~ ProbeSeq* CSI + pID, data = data, whichRandom = 'pID')
ps.CSI2
ps.CSI2[4]/ps.CSI2[3]
ps.pt2 <-anovaBF(PC ~ProbeSeq*ProbeType +pID, data = data, whichRandom = 'pID')
ps.pt2
ps.pt2[4]/ps.pt2[3]
sz.probetype.cueinterval <- anovaBF(PC ~ ProbeType * Setsize * CSI, data = data, whichRandom = 'pID')

sz2 <-sz.probetype.cueinterval/max(sz.probetype.cueinterval)
sz2
sz2[16]/sz2[5]
sz.probetype.cueinterval
sz.probetype.cueinterval[17]/sz.probetype.cueinterval[18]
sz.pt2 <- anovaBF(RT ~ Setsize* ProbeType + pID, data = data, whichRandom = 'pID')
sz.pt2
sz.pt2[4]/sz.pt2[3]
sz.probetype.cueinterval <- anovaBF(RT ~ ProbeType * Setsize * CSI, data = data, whichRandom = 'pID')
data$CSI <- factor(data$CSI)
sz.CSI2 <- anovaBF(RT ~ Setsize* CSI + pID, data = data, whichRandom = 'pID')
sz.CSI2
sz.CSI2[4]/sz.CSI2[3]
pt.CSI2 <- anovaBF(RT ~ ProbeType* CSI + pID, data = data, whichRandom = 'pID')
pt.CSI2
pt.CSI2[4]/pt.CSI2[3]
data$ProbeSeq <-factor(data$ProbeSeq)
ps.CSI2 <- anovaBF(RT ~ ProbeSeq* CSI + pID, data = data, whichRandom = 'pID')
ps.CSI2
ps.CSI2[4]/ps.CSI2[3]
ps.pt2 <-anovaBF(RT ~ProbeSeq*ProbeType +pID, data = data, whichRandom = 'pID')
ps.pt2
ps.pt2[4]/ps.pt2[3]
tmp_data <- data.frame(aggregate(list(data$RT), list(data$ProbeType, data$CSI), mean, na.rm = TRUE))
tmp_data_sd <- data.frame(aggregate(list(data$RT), list(data$ProbeType, data$CSI), sd, na.rm = TRUE))
tmp_data[, 4] <- tmp_data_sd[, 3] / sqrt(18)
names(tmp_data) <- c('ProbeType', 'CSI', 'RT', 'SD')
tmp_data$CSI <- factor(tmp_data$CSI)
tmp_data$ProbeType <- factor(tmp_data$ProbeType)
pd <- position_dodge(.1)
f2.1.RT <-ggplot(data=tmp_data) + 
  aes(x=CSI, y = RT, linetype = ProbeType, group = ProbeType) + 
  geom_line(position = pd) + 
  geom_errorbar(aes(ymin=RT-SD, ymax=RT+SD), width=.1, position = pd) + 
  geom_point(position = pd)+
  theme_bw()+
  ylim(0,2)+
  theme(panel.border = element_blank(), panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))
f2.1.RT
tmp_data <- data.frame(aggregate(list(data$RT), list(data$ProbeType, data$CSI), mean, na.rm = TRUE))
tmp_data_sd <- data.frame(aggregate(list(data$RT), list(data$ProbeType, data$CSI), sd, na.rm = TRUE))
tmp_data[, 4] <- tmp_data_sd[, 3] / sqrt(18)
names(tmp_data) <- c('ProbeType', 'CSI', 'RT', 'SD')
tmp_data$ProbeType <- factor(tmp_data$ProbeType)
tmp_data$CSI <- factor(tmp_data$CSI)
pd <- position_dodge(.1)
f2.3.RT <-ggplot(data=tmp_data) + 
  aes(x=CSI, y = RT, linetype = ProbeType, group = ProbeType) + 
  geom_line(position = pd) + 
  geom_errorbar(aes(ymin=RT-SD, ymax=RT+SD), width=.1, position = pd) + 
  geom_point(position = pd)+
  theme_bw()+
  ylim(0,2)+
  theme(panel.border = element_blank(), panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))
f2.3.RT

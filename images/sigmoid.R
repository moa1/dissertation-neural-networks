library(ggplot2)

sigmoid <- function(x) {
	return (1/(1+exp(-x)))
}

tanhyp <- function(x) {
       return ((1-exp(-2*x))/(1+exp(-2*x)))
}

x <- seq(-7,7,.1)
#x <- seq(-3,3,.1)
y_sigmoid <- sigmoid(x)
y_tanhyp <- tanhyp(x)


# plot
df_sigmoid <- data.frame(x=x, y=y_sigmoid, fun="sigmoid")
df_tanhyp <- data.frame(x=x, y=y_tanhyp, fun="tanhyp")
df <- rbind(df_sigmoid, df_tanhyp)

#ggplot(df) + geom_line(aes(x=x,y=y,group=fun)) + scale_x_continuous(breaks=-10:10)

pdf("plot-sigmoid.pdf")
ggplot(df_sigmoid) + geom_line(aes(x=x,y=y)) + scale_x_continuous(breaks=-10:10) + theme(text=element_text(size=20))
dev.off()

library(data.table)
library(tseries)


#Load our data into the console
forex_df <- read.csv(file.choose())

#check the data type (optional)
class(forex_df)

#concatenate the DF to use the relevant column
forex_df_con <- data.table(forex_df[,2])

#convert the concatenated data into a time tseries
forex_ts <-as.ts(forex_df_con)

#plot the time series to confirm validity
plot(forex_ts)

#Differencing the data & prepare for ADF test (Stationary or non sationary data?)
plot(diff(forex_ts))

plot(diff(log(forex_ts)))

adf.test(diff(log(forex_ts)))

#Perform an ACF test  
acf(log(forex_ts))
acf(diff(log(forex_ts)))
pacf(diff(log(forex_ts)))
par(mfrow=c(1,2))

#Estimate
fit<-arima(log(forex_ts), c(0,1,1))

#Predict prices for for the next five years (No of years * months in a year)
pred <- predict(fit, n.ahead = 5*12)

#Print the prediction
pred

# plot this predictions
ts.plot(forex_ts, 2.718^pred$pred)

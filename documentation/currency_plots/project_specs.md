##  Data Observations

When looking at the seven individual currency charts, we can see three clear patterns from 2001 to 2026:

 **The Kenyan Shilling has weakened over time:** For almost all currencies (especially the US Dollar, Euro, British Pound, and Swiss Franc), the lines move upward. This means it takes more Kenyan Shillings to buy 1 unit of foreign currency today than it did in 2001.
 **Currencies move together during big crises:** If you look closely at the charts around the years 2008 and 2023, all the lines show sharp changes at the exact same time. This happens because major global economic events affect all currencies together.
 **The US Dollar and Saudi Riyal look identical:** The charts for `usd_ksh` and `sar_ksh` have the exact same shape. This is because the Saudi Riyal is officially locked  to the value of the US Dollar.







---

## simple returns analytics  Findings Comment

---

## Lab 1 - Question 4: Simple Returns Findings Comment (Updated with Live Data)

Based on our generated daily simple returns table, we can observe the following findings about the currency behavior against the Kenyan Shilling (KES):

* **Daily averages are incredibly close to zero:** The average daily returns (`Mean` and `Median`) for all seven currencies are extremely tiny (ranging between 0.000020 and 0.000215). This tells us that on a regular day, exchange rates only drift by a fraction of a percent.
 **The Swiss Franc has the highest upward drift:** The `SWF/KSH` pair has the highest daily mean return (0.000215), which matches our earlier observation that it has steadily gained the most value over time.
 **The Saudi Riyal and Japanese Yen are the most volatile:** Looking at `Std Deviation` (daily risk), the Saudi Riyal (0.010949) and Japanese Yen (0.009150) exhibit the highest daily price variance, while the US Dollar (0.004596) is the most stable.
 **Extreme price jumps are common (Heavy Tails):** Every single currency has a highly positive `Excess Kurtosis` score (led by USD at 34.48 and CHY at 26.53). In standard bell-curve statistics, excess kurtosis should be close to 0. These high numbers prove that the market experiences sudden, massive single-day shocks (like the Swiss Franc spiking 13.76% or dropping 9.48% in a single day) much more frequently than text-book models predict.
*





---

##  - : Log Returns analytics Findings Comment (Updated with Live Data)

Based on the generated daily continuous log returns table, we can observe the following findings after applying the log transformation:

 **Log returns clip extreme positive price shocks:** Changing to log returns has slightly shifted the values compared to simple returns. The logarithm scales down large positive jumps. For example, the maximum single-day return for the Swiss Franc (`SWF/KSH`) dropped from **13.76%** down to **12.89%**.
 **Negative skewness has increased:** Most currencies (like USD, GBP, EUR, CHY, and SAR) show a negative `Skewness` value. The `USD/KSH` shifted from **-0.395** to **-0.651**. This tells us that when large changes happen, they lean more heavily toward sudden, sharp downward drops for these foreign currency values against the Shilling.
 **The Saudi Riyal has a negative mean log return:** Interestingly, `SAR/KSH` dropped to a negative average log return (**-0.000040**). This shows how log returns calculate true continuous growth over long horizons more accurately than simple arithmetic means.
 **Extreme volatility clusters remain (Heavy Tails):** Even with log smoothing, the `Excess Kurtosis` numbers remain massive (USD is still extremely high at **36.07**, and CHY is at **27.73**). This proves mathematically that the underlying exchange rates still have "fat tails" and are not normally distributed, meaning sharp risk spikes are a permanent feature of this financial data.
*






---

## Hypothesis Testing: Mean Daily Log Returns Findings Comment

We performed a formal statistical one-sample \(t\)-test on the daily log returns of all seven currencies. The goal was to test the Null Hypothesis (\(H_0: \mu = 0\)) against the Alternative Hypothesis (\(H_a: \mu \neq 0\)) at a 5% significance level (\(\alpha = 0.05\)).

### Core Discoveries:
* **Six out of seven currencies have a daily mean of zero:** For the US Dollar, Euro, British Pound, Japanese Yen, Chinese Yuan, and Saudi Riyal, the \(p\)-values are all much larger than 0.05 (ranging from 0.076 to 0.801). Because of this, we **Fail to Reject \(H_0\)**. This means that on a daily basis, their average price change is statistically indistinguishable from zero.
* **The Swiss Franc is the only exception:** The `SWF/KSH` pair generated a \(p\)-value of **0.048829**, which is just below our 0.05 threshold. Therefore, we **Reject \(H_0\)** for the Swiss Franc. This proves mathematically that its positive upward drift (0.000186 per day) is strong and steady enough to be statistically different from zero.

### Practical and Actuarial Implications:
In financial engineering and actuarial practice, these findings have massive real-world value:
1. **Validates Random Walk Theory:** For 6 of the 7 major currency pairs, the true expected daily return is effectively zero. This heavily supports the "Random Walk Hypothesis," which states that short-term asset price movements are largely random and unpredictable day-to-day.
2. **Simplifies Volatility Modeling (ARCH/GARCH):** Because the daily mean returns are statistically zero, data scientists can safely set the mean parameter (\(\mu\)) to zero when building advanced risk management frameworks, such as Value-at-Risk (VaR) or ARCH/GARCH volatility forecasting models, without losing model accuracy.
3. **Highlights Swiss Franc Strength:** The Swiss Franc's unique rejection shows its persistent behavior as a global safe-haven asset. Over long horizons, it maintains a statistically significant structural premium over the Kenyan Shilling compared to all other tracked currency pairs.
4.






---

##  Simple & Log Returns vs. Normal Curves Findings

 plots of  the daily distribution histograms for all seven currency return types side-by-side with a theoretical normal distribution curve (the dashed line). 

### Core Visual Discoveries from the Charts:
 **The "Spike" Effect (Extreme Center Peaks):** In every single plot—especially for the Japanese Yen (`JYN/KSH`) and the US Dollar (`USD/KSH`)—the actual data forms an incredibly tall, thin needle-like spike right at `0.00`. This means that on a large majority of days, the exchange rate barely moves at all. The standard normal curve completely fails to capture how high this center spike actually is.
 **The "Fat Tails" are Highly Visible:** If you look at the bottom edges of the histograms (especially for the Swiss Franc `SWF/KSH` and Chinese Yuan `CHY/KSH`), the actual bars extend much further out to the left and right than the smooth dashed normal curve line. This shows that extreme market shifts happen regularly in the real world, even though standard textbook models assume they are impossible.
 **The Saudi Riyal is the closest to normal:** The `SAR/KSH` histograms show a slightly wider, more rounded hill shape that tracks the shape of the normal curve better than the others. However, it still features a higher peak at zero and thicker tails than a true normal curve.
 **Log transformation creates structural symmetry:** Comparing the blue charts (Simple) to the green charts (Log) shows that the log transformation compresses extreme right-side jumps. This makes the distribution look cleaner and more statistically balanced, which is vital for building stable financial models.
*






---

## Stationarity Testing: Augmented Dickey-Fuller (ADF) Diagnostic Findings

Formal conduction of  Augmented Dickey-Fuller (ADF) test on the daily log returns of all seven currencies to evaluate their stationarity. 

### Core Discoveries:
* **All seven log return series are perfectly stationary:** Every currency pair achieved a `p-Value` of exactly **0.0** (which is well below our 0.05 threshold). 
* **Strong statistical rejection:** The calculated `ADF Statistics` for all rows (such as **-12.28** for USD and **-64.42** for EUR) are massively negative and sit far below the 5% critical benchmark value of **-2.862**. Because of this, we strongly **Reject the Null Hypothesis (\(H_0\))**.

### Practical Data Science Implications:
1. **The power of log transformations:** While raw exchange rate charts trend upward over 25 years (making them non-stationary and unstable), converting them into continuous log returns successfully stripped out those trends. This stabilizes the mean and variance of the data over time.
2. **Green light for forecasting models:** Achieving perfect stationarity across all seven metrics satisfies the most critical prerequisite for time-series modeling. This data is now completely safe and prepared to be fed into advanced statistical algorithms, such as Autoregressive (AR) frameworks or ARCH/GARCH volatility forecasting models.
3.





---

##  - Simulation Live Chart Findings & Analysis

Looking directly at the six generated simulation runs in our chart, we can draw three critical conclusions about how a Random Walk with Drift behaves in the real world:

* **Random noise can mimic fake structural trends:** Even though all six runs used the exact same mathematical rules, the blue paths look completely different. For example, **Realization Run #2** experienced a string of early positive shocks, causing it to climb drastically up to a value of nearly 80. Meanwhile, **Realization Run #4** suffered negative shocks, plunging below 0 and staying negative for hundreds of steps. This proves that cumulative random noise easily mimics structural trends that do not actually exist.
* **Ordinary Linear Regression (OLS) is highly deceptive on raw data:** The red dashed lines show what standard linear regression thinks the trend is. In **Run #2**, the regression line is incredibly steep ($\hat{\beta} = 0.0804$), making it look like the drift is 8 times stronger than it actually is. In **Run #4**, the regression line slants downward, falsely implying a negative trend. This demonstrates that standard linear regression cannot be trusted when applied directly to raw, unstable time-series data.
* **Paths rarely return to the theoretical mean:** The solid black line shows the true theoretical expected path ($\mu_t = 0.01t$). In almost all 6 runs, once a blue line wanders away from the black line, it stays away for a very long time. It does not pull back toward the average. This visually demonstrates the property of "infinite memory" in non-stationary data, which is exactly why we must use log transformations to stabilize our real-world exchange rates before trying to forecast them.
*





---

## ARIMA Modeling -  Fixed 8-Lag Unit Root Diagnostics with Constant & Trend

A highly specific  a Augmented Dickey-Fuller (ADF) diagnostic test was perfomed on the daily log returns of all seven currencies. Following strict model specifications, we forced the regression framework to include exactly 8 lags, a constant intercept, and a deterministic time trend.

### Core Discoveries:
* **Absolute Stationarity Maintained:** Every single currency pair easily achieved a `p-Value` of exactly **0.000000** (well below the 0.05 testing threshold).
* **Massive Margin of Safety:** The calculated `ADF Statistics` (ranging roughly from -12 to over -60) are far more negative than the strict 5% critical value benchmark for a trend model (which sits near **-3.41**). Because of this, we strongly **Reject the Null Hypothesis (\(H_0\))**.
* **Verdict:** All 7 log return series are declared perfectly stationary. They are fully prepared to be modeled using ARIMA algorithms without any additional differencing (\(d=0\)).

### Simple English Explanation of the Findings:
1. **The Trend is Accounted For:** Even when we mathematically force a time trend into our test model, the daily log returns do not drift. This proves that any visible long-term trends from the original raw price charts have been completely stripped away by switching to log returns.
2. **Short-Term Memory is Managed:** By forcing the test to include 8 lags, we check if the last 8 business days of data are affecting today's returns. Even with these past days included, the market returns always snap back to a stable baseline structure. 
3. **Green Light for ARIMA Model Fitting:** Because the data is confirmed stable under strict constant and trend parameters, we are 100% safe to move to the next phase: picking the right Autoregressive (\(p\)) and Moving Average (\(q\)) structural lag parameters to start forecasting.
4.




---

## ARIMA Modeling - : Residual Autocorrelation Analysis Findings (Lag 20)

We ran a formal Ljung-Box Q-test up to the 20th lag on the leftovers (residuals) of our baseline model. This tests if forcing exactly 8 lags in our initial framework was enough to clear away short-term internal timeline patterns.

### Core Discoveries:
* **Five out of seven currencies are fully cleaned:** For the Euro (`EUR/KSH`), British Pound (`UKP/KSH`), Swiss Franc (`SWF/KSH`), Japanese Yen (`JYN/KSH`), and Saudi Riyal (`SAR/KSH`), the \(p\)-values are all significantly higher than 0.05 (ranging from 0.313 to 0.968). For these currencies, we achieve a verdict of **Sufficient Lags (White Noise)**.
* **The US Dollar and Chinese Yuan still contain patterns:** The `USD/KSH` pair (\(p\)-value = 0.000005) and the `CHY/KSH` pair (\(p\)-value = 0.009237) have \(p\)-values well below 0.05. Their verdict is **Insufficient Lags (Patterns Left)**. 

### Practical and Actuarial Implications:
1. **8 Lags work well for major free-floating currencies:** For European pairs, the Swiss Franc, and the Japanese Yen, an 8-lag framework captures short-term market updates. The leftover noise is purely random, meaning no hidden, basic linear memory remains unaddressed.
2. **US Dollar and Chinese Yuan need dynamic lag management:** Because the US Dollar and Chinese Yuan still show significant residual patterns at lag 20, a simple static 8-lag model leaves predictive information out. This highlights why these two specific currency series require a customized ARIMA parameter selection approach rather than a standard, one-size-fits-all model framework.
3.









---

## ARIMA Modeling -  Automated ARMA(p,q) Order Selection Findings

We executed an automated grid search optimization matrix across all seven currency log return series. The algorithm tested every lag combination from order 0 to 3 and selected the optimal Autoregressive terms (\(p\)) and Moving Average terms (\(q\)) by identifying the model with the lowest Akaike Information Criterion (AIC) score.

### Core Discoveries:
* **The Majority Favor Pure AR(2) Frameworks:** For the Euro (`EUR/KSH`), British Pound (`UKP/KSH`), Swiss Franc (`SWF/KSH`), and Chinese Yuan (`CHY/KSH`), the optimization engine selected an **ARMA(2, 0)** structure. This means these currencies require exactly **2 AR terms** and **0 MA terms** to explain their daily variations.
* **The US Dollar requires a Balanced Mix:** The `USD/KSH` pair selected an **ARMA(2, 2)** structure, incorporating exactly **2 AR terms** and **2 MA terms**. This more complex setup directly mirrors our earlier finding that the US Dollar held onto leftover short-term patterns that a simple lag model couldn't clean up.
* **The Japanese Yen operates on a pure Moving Average:** The `JYN/KSH` pair optimized cleanly at an **ARMA(0, 2)** structure, using **0 AR terms** and **2 MA terms**. This reveals that the Yen's daily changes are driven entirely by recent random market shocks (shocks from today and yesterday) rather than its own past prices.
* **The Saudi Riyal demands the maximum lag complexity:** The `SAR/KSH` pair optimized at the maximum boundary of our search matrix with an **ARMA(3, 3)** structure (**3 AR terms** and **3 MA terms**). 

### Simple English Explanation of the Findings:
1. **What the AR Terms (p) Mean:** When a model includes 2 AR terms (like the Euro or Dollar), it proves that the price change today is actively influenced by what happened yesterday and the day before yesterday. There is a short, 2-day linear "memory" in these exchange rates.
2. **What the MA Terms (q) Mean:** When a model includes MA terms (like the Dollar or Yen), it means the currency is highly sensitive to immediate, unpredicted news or market shocks from the last 48 hours. The model uses these leftover error spikes to correct its next forecast.
3. **Massive Information Compression:** The negative AIC values (ranging from -40,996 to -52,550) are exceptionally large and negative. In statistics, this confirms that the selected models are extracting a massive amount of hidden structural patterns from the noise while keeping the model clean and unbloated.
4.




---

## ARIMA Modeling -  ARCH-LM Volatility Clustering Findings

We executed a formal Engle's Lagrange Multiplier (ARCH-LM) test on the residuals of our optimized ARMA models. The test evaluated every critical lag milestone requested: the first 10 lags, and then every lag that is a multiple of 5 up to 40 lags.

### Core Discoveries:
* **Universal Rejection of Constant Variance:** Across all seven currencies and all tested lag checkpoints (10, 15, 20, 25, 30, 35, 40), the calculated `p-Value` is exactly **0.000000**.
* **Massive Test Statistics:** The LM test statistics are exceptionally large (ranging from **176.97** for the Swiss Franc up to an incredible **863.66** for the Saudi Riyal). This far exceeds any standard chi-square critical boundary.
* **Verdict:** We strongly reject the Null Hypothesis (\(H_0\): No ARCH effects) and confirm that all 7 currency series choose option **(A) Display conditional heteroskedasticity**.

### Simple English Explanation of the Findings:
1. **What Conditional Heteroskedasticity Means:** In plain English, this proves that the volatility (the risk/variance) of the Kenyan Shilling exchange rates is not constant over time. Instead, it moves in loops and waves. 
2. **The "Banding" and "Clustering" Phenonmenon:** Quiet market days are followed by more quiet days, and wild, highly volatile market days are followed by more wild days. When a big shock hits the Kenyan Shilling, the ripples linger in the variance structure for at least 40 business days.
3. **The Limitation of Pure ARIMA Models:** Because these massive ARCH effects exist, a standard ARIMA model is incomplete on its own. While ARIMA successfully models the *average direction* (mean) of the exchange rates, it completely ignores the changing *risk waves* (variance).

### Actuarial and Data Science Implications:
For an actuarial student portfolio, this is the ultimate transition point. It proves mathematically that to successfully forecast or simulate currency risk, you must expand your work beyond simple linear models. This outcome provides a perfect quantitative justification for layering on non-linear volatility algorithms—specifically **ARCH** and **GARCH** models—to successfully track, price, and hedge portfolio risk waves.






---

## Advanced Volatility Modeling: Live Predictive Findings & Discussion

We successfully modeled asymmetric risk and generated five-day out-of-sample volatility projections. Based on the output table, we can draw the following core conclusions:

* **The Leverage Effect is Positively Confirmed:** The `EGARCH Leverage Coef` column is positive across all seven currencies. The US Dollar (`USD/KSH` at 0.285) and the Chinese Yuan (`CHY/KSH` at 0.229) show the highest sensitivity to market shocks. In financial markets, this proves that news shocks exert an asymmetric impact on exchange rate risk variance, which standard GARCH models fail to capture.
* **Risk is Expanding Across the Horizon:** Looking closely at the projections from Day 1 to Day 5, the predicted volatility climbs higher every single day for all seven currencies. For instance, the Japanese Yen (`JYN/KSH`) expands from a risk level of **0.9887** on Day 1 up to **1.0860** by Day 5. This expansion proves that uncertainty scales upward the further out into the future we try to predict.
* **The Japanese Yen and Saudi Riyal Carry the Highest Risk Baseline:** The Japanese Yen and Saudi Riyal exhibit the highest baseline predicted volatility metrics (both hovering near or above 0.93–1.08). Conversely, the US Dollar remains the most tightly managed and stable currency instrument, maintaining a low, steady daily risk progression starting at **0.1220** on Day 1.
* **Direct Actuarial Application:** These multi-step standard deviation projections serve as a foundational element for computing Value-at-Risk (VaR) or setting capital safety margins. Knowing exactly how these risk waves propagate over a 5-day trading window allows portfolio managers to successfully price options and hedge currency exposure down to a fraction of a percent.
*
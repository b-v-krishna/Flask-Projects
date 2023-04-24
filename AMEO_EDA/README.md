<h1>Aspiring Mind Employment Outcome 2015 (AMEO)</h1>
The dataset was released by Aspiring Minds from the Aspiring Mind Employment Outcome 2015 (AMEO). The study is primarily limited only to students with engineering disciplines. The dataset contains the employment outcomes of engineering graduates as dependent variables (Salary, Job Titles, and Job Locations) along with the standardized scores from three different areas – cognitive skills, technical skills and personality skills. The dataset also contains demographic features. The dataset contains around 40 independent variables and 4000 data points. The independent variables are both continuous and categorical in nature. The dataset contains a unique identifier for each candidate.

<h3>Implementation</h3>
In this file, we have conducted exploratory data analysis, univariate analysis, and bivariate analysis to find the relationships between variables and answers to research questions.

<h4>Times of India article dated Jan 18, 2019 states that “After doing your Computer Science
Engineering if you take up jobs as a Programming Analyst, Software Engineer,
Hardware Engineer and Associate Engineer you can earn up to 2.5-3 lakhs as a fresh
graduate.” Test this claim with the data given to you.<br></h4>
<h5>H0: Null Hypothesis < 3lacs<br></h5>
<h5>H1: Alternative Hypothesis > 3 lacs</h5>

```
Mean=df_filtered['Salary'].mean()
print(int(Mean))
```
```
if int(Mean)>=250000 and int(Mean)<=300000:
    print('Fail to reject null hypothesis')
else:
    print('Reject null hypothesis')
```
Reject null hypothesis<br>
Therefore,the claim is flase<br>



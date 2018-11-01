import math
import statistics

#l = [13,9,17,21,14,18,29,60,85,52,47,118,250,109]
#l = [6751,9908,3461,2336,21147,2332,189,1185,370,1414,4668,1953,10034,735,802,618,180,1657]
l = [13,9,17,21,14,18,29,60,85,13,47,118,250,109]
##############################################################################################################

def mean(l):
    #finds the mean of a given list
    x = 0
    for i in l:
        x += i
    mean = x / len(l)
    return mean

def median(l):
    #finds the median of a given list
    sorted_list = sorted(l)
    sorted_length = len(l)
    if len(sorted_list) % 2 == 0:
        even_list_first_num = (sorted_length / 2) - 1
        even_list_second_num = (sorted_length / 2) 
        middle_num = (sorted_list[int(even_list_first_num)] + sorted_list[int(even_list_second_num)]) / 2
        return middle_num
    else:
        middle_number = (len(sorted_list) + 1) / 2
        return sorted_list[int(middle_number) - 1]
    
def mode(l):
    #finds the mode of a given list
    try:
        most_occuring = statistics.mode(l)
        return most_occuring
    except:
        return 'No Mode'

def rangee(l):
    #finds the range of a given list
    max_num = max(l)
    min_num = min(l)
    the_range = max_num - min_num
    return the_range

##############################################################################################################

def sample_standard(l):
    #finds the standard deviation of a sample list
    sum_num = 0
    for i in l:
        x = (i - mean(l))**2
        sum_num += x
    y = math.sqrt((sum_num / (len(l) - 1)))
    return y

def pop_standard(l):
    #finds the standard deviation of a population list
    sum_num = 0
    for i in l:
        x = (i - mean(l))**2
        sum_num += x
    y = math.sqrt((sum_num / len(l)))
    return y

def variance(sd):
    #finds the variance when a standard deviation is given
    variance_num = sd**2
    return variance_num

##############################################################################################################

def quantile_one(l):
    #finds Q1 in a list
    x = sorted(l)
    if len(l) % 2 == 0:
        split = int((len(l) / 2))
        y = x[:split]
        return median(y)
    else:
        split = int((len(l) + 1) / 2)
        y = x[:split]
        return median(y)

def quantile_three(l):
    #finds Q3 in a list
    x = sorted(l)
    if len(l) % 2 == 0:
        split = int((len(l) / 2))
        y = x[split:]
        return median(y)
    else:
        split = int((len(l) / 2))
        y = x[split:]
        return median(y)

def interquantile_range(l):
    #finds the interquantile range of a list
    iqr = quantile_three(l) - quantile_one(l)
    return iqr

def upper_fence(l):
    #finds the upper fence of a list
    uf = quantile_three(l) + (1.5 * interquantile_range(l))
    return uf

def lower_fence(l):
    #finds the lower fence
    lf = quantile_one(l) - (1.5 * interquantile_range(l))
    return lf

def the_outliers(l):
    #finds the outlier of a list
    x = []
    for i in l:
        if i < lower_fence(l) or i > upper_fence(l):
            x.append(i)
        else:
            None
    return x
            
##############################################################################################################

def z_score_sample(x,l):
    z = (x - mean(l)) / sample_standard(l)
    return z
    
def z_score_pop(x,l):
    z = (x - mean(l)) / pop_standard(l)
    return z    

##############################################################################################################

def sample_answer(l):
    print('Sample Data')
    print('mean:', mean(l))
    print('median:', median(l))
    print('mode:', mode(l))
    print('range:', rangee(l))
    print('standard deviation:' , sample_standard(l))
    print('variance:', variance(sample_standard(l)))
    print('Q1:' , quantile_one(l))
    print('Q3:' , quantile_three(l))
    print('IQR:', interquantile_range(l))
    print('lower fence:', lower_fence(l))
    print('upper fence:', upper_fence(l))
    print('outliers:', the_outliers(l))

def pop_answer(l):
    print('Population Data')
    print('mean', mean(l))
    print('median', median(l))
    print('mode', mode(l))
    print('range', rangee(l))
    print('standard deviation' , pop_standard(l))
    print('variance', variance(pop_standard(l)))
    print('Q1', quantile_one(l))
    print('Q3' , quantile_three(l))
    print(sorted(l))


print(pop_standard(l))
print('mode', mode(l))
print('mean',mean(l))
print('median',median(l))
print('variance:', variance(pop_standard(l)))
print('range', rangee(l))



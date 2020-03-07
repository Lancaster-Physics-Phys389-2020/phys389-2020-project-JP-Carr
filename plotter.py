"""
Provides functions to produce graphs with single and multiple plots
"""
import matplotlib.pyplot as plt


#PLOTS PARTICLE POSITION AS STATIC GRAPH
def plot(x,y,title,x_lab,y_lab,path=None):
    """
    

    Parameters
    ----------
    x : list/numpy.ndarray
        Values to be plotted along the x-axis.
    y : list/numpy.ndarray
        Values to be plotted along the y-axis.
    title : str
        Title of the plot.
    x_lab : str
        x-axis label.
    y_lab : str
        y-axis label.
    path : str, optional
        Directory for saving plot as a png. The default is None.

    Returns
    -------
    None.

    """
    #Outputs or saves a single Cartesian plot from 2 arrays
    plt.figure(figsize=(7,7))
    """
    plt.ylim(bottom=0)
    plt.ylim(top=max(y))
    """
    plt.xlim(left=min(x)*1.1)
    plt.xlim(right=max(x)*1.1)
    plt.title(title)
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)
    plt.plot(x,y)

  
    if path==None:
        plt.show()
    else:
        plt.savefig("plots\\"+path+"\\"+title+".png")
    

def multiplot(x_list,y_list,title,x_lab,y_lab,legend_list=None,path=None,marker_list=None):
    #Outputs or saves a multiple plots on a single Cartesian axis from 2 nested arrays
    max_x=max([max(i) for i in x_list])
    if marker_list==None:
        marker_list=[None for i in range(len(x_list))]
    
    plt.figure(figsize=(7,7))
    plt.xlim(left=0)
    plt.xlim(right=max_x*1.1)
    plt.title(title)
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)
    for i in range(len(x_list)):
        if marker_list[i]!=None:
            plt.plot(x_list[i], y_list[i],marker=marker_list[i],linewidth=0)
        else:
            plt.plot(x_list[i], y_list[i],marker=marker_list[i])
    if legend_list != None:
        plt.legend(legend_list)
        
    if path==None:
        plt.show()
    else:
        plt.savefig("plots\\"+path+"\\"+title+".png")
    return
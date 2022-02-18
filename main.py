def dfGroupMean(dfSource,columnsList=None,groupbyColumns=None,floatFormatter='{:.2f}'):
    try:
        if groupbyColumns == None:
            print(f'the var groupbyColumns is empty')
        else:
            if columnsList!= None:
                dataFrame = dfSource[columnsList]
                dataFrame = dataFrame.groupby(groupbyColumns).mean()
                dataFrame = dataFrame.reset_index()
                for i in (dataFrame.columns):
                    if dataFrame[i].dtypes == 'float64':
                        dataFrame.loc[:, i] = dataFrame[i].map(floatFormatter.format)
            else:
                dataFrame = dfSource
                dataFrame = dataFrame.groupby(groupbyColumns).mean()
                dataFrame = dataFrame.reset_index()
                for i in (dataFrame.columns):
                    if dataFrame[i].dtypes == 'float64':
                        dataFrame.loc[:, i] = dataFrame[i].map(floatFormatter.format)
            return dataFrame
    except Exception as exc:
        print(exc)

def dfGroupStd(dfSource,columnsList=None,groupbyColumns=None,floatFormatter='{:.2f}'):
    try:
        if groupbyColumns == None:
            print(f'the var groupbyColumns is empty')
        else:
            if columnsList!= None:
                dataFrame = dfSource[columnsList]
                dataFrame = dataFrame.groupby(groupbyColumns).std()
                dataFrame = dataFrame.reset_index()
                for i in (dataFrame.columns):
                    if dataFrame[i].dtypes == 'float64':
                        dataFrame.loc[:, i] = dataFrame[i].map(floatFormatter.format)
            else:
                dataFrame = dfSource
                dataFrame = dataFrame.groupby(groupbyColumns).std()
                dataFrame = dataFrame.reset_index()
                for i in (dataFrame.columns):
                    if dataFrame[i].dtypes == 'float64':
                        dataFrame.loc[:, i] = dataFrame[i].map(floatFormatter.format)
            return dataFrame
    except Exception as exc:
        print(exc)
        
def dfGroupMin(dfSource,columnsList=None,groupbyColumns=None,floatFormatter='{:.2f}'):
    try:
        if groupbyColumns == None:
            print(f'the var groupbyColumns is empty')
        else:
            if columnsList!= None:
                dataFrame = dfSource[columnsList]
                dataFrame = dataFrame.groupby(groupbyColumns).min()
                dataFrame = dataFrame.reset_index()
                for i in (dataFrame.columns):
                    if dataFrame[i].dtypes == 'float64':
                        dataFrame.loc[:, i] = dataFrame[i].map(floatFormatter.format)
            else:
                dataFrame = dfSource
                dataFrame = dataFrame.groupby(groupbyColumns).min()
                dataFrame = dataFrame.reset_index()
                for i in (dataFrame.columns):
                    if dataFrame[i].dtypes == 'float64':
                        dataFrame.loc[:, i] = dataFrame[i].map(floatFormatter.format)
            return dataFrame
    except Exception as exc:
        print(exc)
        
def dfGroupMax(dfSource,columnsList=None,groupbyColumns=None,floatFormatter='{:.2f}'):
    try:
        if groupbyColumns == None:
            print(f'the var groupbyColumns is empty')
        else:
            if columnsList!= None:
                dataFrame = dfSource[columnsList]
                dataFrame = dataFrame.groupby(groupbyColumns).max()
                dataFrame = dataFrame.reset_index()
                for i in (dataFrame.columns):
                    if dataFrame[i].dtypes == 'float64':
                        dataFrame.loc[:, i] = dataFrame[i].map(floatFormatter.format)
            else:
                dataFrame = dfSource
                dataFrame = dataFrame.groupby(groupbyColumns).max()
                dataFrame = dataFrame.reset_index()
                for i in (dataFrame.columns):
                    if dataFrame[i].dtypes == 'float64':
                        dataFrame.loc[:, i] = dataFrame[i].max(floatFormatter.format)
            return dataFrame
    except Exception as exc:
        print(exc)
        
def dfGroupVar(dfSource,columnsList=None,groupbyColumns=None,floatFormatter='{:.2f}'):
    try:
        if groupbyColumns == None:
            print(f'the var groupbyColumns is empty')
        else:
            if columnsList!= None:
                dataFrame = dfSource[columnsList]
                dataFrame = dataFrame.groupby(groupbyColumns).var()
                dataFrame = dataFrame.reset_index()
                for i in (dataFrame.columns):
                    if dataFrame[i].dtypes == 'float64':
                        dataFrame.loc[:, i] = dataFrame[i].map(floatFormatter.format)
            else:
                dataFrame = dfSource
                dataFrame = dataFrame.groupby(groupbyColumns).var()
                dataFrame = dataFrame.reset_index()
                for i in (dataFrame.columns):
                    if dataFrame[i].dtypes == 'float64':
                        dataFrame.loc[:, i] = dataFrame[i].map(floatFormatter.format)
            return dataFrame
    except Exception as exc:
        print(exc)
        
def dfGroupSum(dfSource,columnsList=None,groupbyColumns=None,floatFormatter='{:.2f}'):
    try:
        if groupbyColumns == None:
            print(f'the var groupbyColumns is empty')
        else:
            if columnsList!= None:
                dataFrame = dfSource[columnsList]
                dataFrame = dataFrame.groupby(groupbyColumns).sum()
                dataFrame = dataFrame.reset_index()
                for i in (dataFrame.columns):
                    if dataFrame[i].dtypes == 'float64':
                        dataFrame.loc[:, i] = dataFrame[i].map(floatFormatter.format)
            else:
                dataFrame = dfSource
                dataFrame = dataFrame.groupby(groupbyColumns).sum()
                dataFrame = dataFrame.reset_index()
                for i in (dataFrame.columns):
                    if dataFrame[i].dtypes == 'float64':
                        dataFrame.loc[:, i] = dataFrame[i].map(floatFormatter.format)
            return dataFrame
    except Exception as exc:
        print(exc)
        
def dfGroupCount(dfSource,columnsList=None,groupbyColumns=None):
    try:
        if groupbyColumns == None:
            print(f'the var groupbyColumns is empty')
        else:
            if columnsList!= None:
                dataFrame = dfSource[columnsList]
                dataFrame = dataFrame.groupby(groupbyColumns).count()
                dataFrame = dataFrame.reset_index()
            else:
                dataFrame = dfSource
                dataFrame = dataFrame.groupby(groupbyColumns).count()
                dataFrame = dataFrame.reset_index()
            return dataFrame
    except Exception as exc:
        print(exc)
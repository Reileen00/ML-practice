{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"Copy of first.py","provenance":[{"file_id":"1w9U6pjY0Osm79zbphhHulo3KJd54ywDz","timestamp":1641776167808}],"authorship_tag":"ABX9TyPe9zWs3mBzxwlJqASy2exh"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"markdown","source":["Importing Libraries"],"metadata":{"id":"D1KbP7_OqAC0"}},{"cell_type":"code","source":["import pandas as pd\n","import matplotlib.pyplot as plt\n","import seaborn as sns\n","from pandas import read_csv\n","from sklearn.model_selection import train_test_split\n","from sklearn.linear_model import LinearRegression\n","from sklearn.linear_model import Lasso\n","from sklearn import metrics"],"metadata":{"id":"EtQiHD5gqIBD","executionInfo":{"status":"ok","timestamp":1641755588968,"user_tz":-330,"elapsed":2281,"user":{"displayName":"Baisnabi Rout","photoUrl":"https://lh3.googleusercontent.com/a/default-user=s64","userId":"11308424730219323998"}}},"execution_count":2,"outputs":[]},{"cell_type":"markdown","source":["Importing the data "],"metadata":{"id":"PPxEvTDpqoIy"}},{"cell_type":"code","source":["url1='/content/a1-x-test.txt'\n","url2='/content/a1-x-train.txt'\n","url3='/content/a1-y-test.txt'\n","url4='/content/a1-y-train.txt'\n","dxtt=read_csv(url1, header=None)\n","dxtn=read_csv(url2, header=None)\n","dytt=read_csv(url3, header=None)\n","dytn=read_csv(url4, header=None)\n","data_X_test=dxtt.values\n","data_X_train=dxtn.values\n","data_Y_test=dytt.values\n","data_Y_train=dytn.values\n","X_test=data_X_test[: , :]\n","X_train=data_X_train[: , :]\n","y_test=data_Y_test[: , :]\n","y_train=data_Y_train[: , :]"],"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":449},"id":"M3NtBxghqtwq","executionInfo":{"status":"error","timestamp":1641755593852,"user_tz":-330,"elapsed":510,"user":{"displayName":"Baisnabi Rout","photoUrl":"https://lh3.googleusercontent.com/a/default-user=s64","userId":"11308424730219323998"}},"outputId":"724483ad-df6a-4ca5-a5f4-0f544359a128"},"execution_count":3,"outputs":[{"output_type":"error","ename":"FileNotFoundError","evalue":"ignored","traceback":["\u001b[0;31m---------------------------------------------------------------------------\u001b[0m","\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)","\u001b[0;32m<ipython-input-3-23adcfda65e1>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0murl3\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'/content/a1-y-test.txt'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0murl4\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'/content/a1-y-train.txt'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m \u001b[0mdxtt\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl1\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheader\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m \u001b[0mdxtn\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl2\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheader\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0mdytt\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl3\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheader\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;32m/usr/local/lib/python3.7/dist-packages/pandas/io/parsers.py\u001b[0m in \u001b[0;36mread_csv\u001b[0;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, dialect, error_bad_lines, warn_bad_lines, delim_whitespace, low_memory, memory_map, float_precision)\u001b[0m\n\u001b[1;32m    686\u001b[0m     )\n\u001b[1;32m    687\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 688\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0m_read\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    689\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    690\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;32m/usr/local/lib/python3.7/dist-packages/pandas/io/parsers.py\u001b[0m in \u001b[0;36m_read\u001b[0;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[1;32m    452\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    453\u001b[0m     \u001b[0;31m# Create the parser.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 454\u001b[0;31m     \u001b[0mparser\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mTextFileReader\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfp_or_buf\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    455\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    456\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mchunksize\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0miterator\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;32m/usr/local/lib/python3.7/dist-packages/pandas/io/parsers.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[1;32m    946\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"has_index_names\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mkwds\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"has_index_names\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    947\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 948\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_make_engine\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mengine\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    949\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    950\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mclose\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;32m/usr/local/lib/python3.7/dist-packages/pandas/io/parsers.py\u001b[0m in \u001b[0;36m_make_engine\u001b[0;34m(self, engine)\u001b[0m\n\u001b[1;32m   1178\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_make_engine\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mengine\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"c\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1179\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mengine\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m\"c\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1180\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_engine\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mCParserWrapper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mf\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1181\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1182\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mengine\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m\"python\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;32m/usr/local/lib/python3.7/dist-packages/pandas/io/parsers.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, src, **kwds)\u001b[0m\n\u001b[1;32m   2008\u001b[0m         \u001b[0mkwds\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"usecols\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0musecols\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2009\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2010\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_reader\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mparsers\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mTextReader\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msrc\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2011\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0munnamed_cols\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_reader\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0munnamed_cols\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2012\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;32mpandas/_libs/parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader.__cinit__\u001b[0;34m()\u001b[0m\n","\u001b[0;32mpandas/_libs/parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader._setup_parser_source\u001b[0;34m()\u001b[0m\n","\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: '/content/a1-x-test.txt'"]}]},{"cell_type":"code","source":["print(X_test.shape,X_train.shape,y_test.shape,y_train.shape)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"7VzY-Olp0NtN","executionInfo":{"status":"ok","timestamp":1641580442594,"user_tz":-330,"elapsed":521,"user":{"displayName":"Baisnabi Rout","photoUrl":"https://lh3.googleusercontent.com/a/default-user=s64","userId":"11308424730219323998"}},"outputId":"4c738544-a411-4514-9b51-bfec73eed494"},"execution_count":5,"outputs":[{"output_type":"stream","name":"stdout","text":["(1000, 0) (200, 0) (1000, 0) (200, 0)\n"]}]},{"cell_type":"markdown","source":["Model training"],"metadata":{"id":"ttzpSPHb04ti"}},{"cell_type":"markdown","source":["1.Linear Regression"],"metadata":{"id":"qkPxgXLf1BMh"}},{"cell_type":"code","source":["#loading the linear Regression model\n","linear_reg_model=LinearRegression()"],"metadata":{"id":"lMWzIapd1D3D","executionInfo":{"status":"ok","timestamp":1641580702101,"user_tz":-330,"elapsed":431,"user":{"displayName":"Baisnabi Rout","photoUrl":"https://lh3.googleusercontent.com/a/default-user=s64","userId":"11308424730219323998"}}},"execution_count":6,"outputs":[]},{"cell_type":"code","source":["linear_reg_model.fit(X_train,y_train)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":328},"id":"RU8IX6cE1S0x","executionInfo":{"status":"error","timestamp":1641584423572,"user_tz":-330,"elapsed":522,"user":{"displayName":"Baisnabi Rout","photoUrl":"https://lh3.googleusercontent.com/a/default-user=s64","userId":"11308424730219323998"}},"outputId":"fdfd400e-789e-423d-c198-1aa503bd5983"},"execution_count":8,"outputs":[{"output_type":"error","ename":"ValueError","evalue":"ignored","traceback":["\u001b[0;31m---------------------------------------------------------------------------\u001b[0m","\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)","\u001b[0;32m<ipython-input-8-2ab6825679bf>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mlinear_reg_model\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX_train\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0my_train\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m","\u001b[0;32m/usr/local/lib/python3.7/dist-packages/sklearn/linear_model/_base.py\u001b[0m in \u001b[0;36mfit\u001b[0;34m(self, X, y, sample_weight)\u001b[0m\n\u001b[1;32m    661\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    662\u001b[0m         X, y = self._validate_data(\n\u001b[0;32m--> 663\u001b[0;31m             \u001b[0mX\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maccept_sparse\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0maccept_sparse\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my_numeric\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmulti_output\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    664\u001b[0m         )\n\u001b[1;32m    665\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;32m/usr/local/lib/python3.7/dist-packages/sklearn/base.py\u001b[0m in \u001b[0;36m_validate_data\u001b[0;34m(self, X, y, reset, validate_separately, **check_params)\u001b[0m\n\u001b[1;32m    574\u001b[0m                 \u001b[0my\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcheck_array\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0my\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mcheck_y_params\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    575\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 576\u001b[0;31m                 \u001b[0mX\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcheck_X_y\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mcheck_params\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    577\u001b[0m             \u001b[0mout\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mX\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    578\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;32m/usr/local/lib/python3.7/dist-packages/sklearn/utils/validation.py\u001b[0m in \u001b[0;36mcheck_X_y\u001b[0;34m(X, y, accept_sparse, accept_large_sparse, dtype, order, copy, force_all_finite, ensure_2d, allow_nd, multi_output, ensure_min_samples, ensure_min_features, y_numeric, estimator)\u001b[0m\n\u001b[1;32m    966\u001b[0m         \u001b[0mensure_min_samples\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mensure_min_samples\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    967\u001b[0m         \u001b[0mensure_min_features\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mensure_min_features\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 968\u001b[0;31m         \u001b[0mestimator\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mestimator\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    969\u001b[0m     )\n\u001b[1;32m    970\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;32m/usr/local/lib/python3.7/dist-packages/sklearn/utils/validation.py\u001b[0m in \u001b[0;36mcheck_array\u001b[0;34m(array, accept_sparse, accept_large_sparse, dtype, order, copy, force_all_finite, ensure_2d, allow_nd, ensure_min_samples, ensure_min_features, estimator)\u001b[0m\n\u001b[1;32m    807\u001b[0m                 \u001b[0;34m\"Found array with %d feature(s) (shape=%s) while\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    808\u001b[0m                 \u001b[0;34m\" a minimum of %d is required%s.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 809\u001b[0;31m                 \u001b[0;34m%\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mn_features\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0marray\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mensure_min_features\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    810\u001b[0m             )\n\u001b[1;32m    811\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;31mValueError\u001b[0m: Found array with 0 feature(s) (shape=(200, 0)) while a minimum of 1 is required."]}]}]}
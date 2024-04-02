from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import MinMaxScaler
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.ml.recommendation import ALS
import numpy as np
import findspark
findspark.init()
MYSQL_PARAMS = {
        'host': '10.8.16.253',
        'port': 3306,
        'user': 'root',
        'password': 'fiang123',
        'db':'foods',
        'table':'recommendforallusers'
    }


spark = SparkSession.builder \
    .appName("model") \
    .master('local[*]') \
    .config("spark.sql.catalogImplementation","hive") \
    .getOrCreate()

def euclidean_distance(a, b):
    a=np.array(a)
    b=np.array(b)
    distance = np.linalg.norm(a - b)
    return 1-float(distance)
def train_run():
    euclidean_distance_udf=udf(euclidean_distance, DoubleType())
    # 加载用户画像数据
    user_df = spark.sql('select user_id,type1,type2, type3  from dwd_foods.dwd_foods_db_foods_t_resume;')
    foods_df = spark.sql('SELECT cast(id  as int) as foods_id,type_code as type1, type_code as type2, type_code as type3 FROM dwd_foods.dwd_foods_db_spider_t_foods ')
    # 合并用户画像特征为一个向量列
    assembler = VectorAssembler(inputCols=user_df.columns[1:], outputCol="features")
    user_df = assembler.transform(user_df)

    # 合并景点信息特征为一个向量列
    assembler = VectorAssembler(inputCols=foods_df.columns[1:], outputCol="features")
    foods_df = assembler.transform(foods_df)
    # 标准化向量列
    minmax = MinMaxScaler(inputCol="features", outputCol="foods_features_norm")
    minmax_model=minmax.fit(foods_df)
    foods_df =minmax_model.transform(foods_df)
    minmax =MinMaxScaler(inputCol="features", outputCol="user_features_norm")
    minmax_model=minmax.fit(foods_df)
    user_df = minmax_model.transform(user_df)
    cartesian_df = user_df.crossJoin(foods_df)

    # # 计算相似度
    cartesian_df = cartesian_df.withColumn("similarity", euclidean_distance_udf(cartesian_df['user_features_norm'],cartesian_df['foods_features_norm']) )

    # # 假设筛选条件为相似度大于0.9的用户-信息对
    filtered_df = cartesian_df.filter("similarity> 0.7")
    # # 根据相似度值进行降序排序
    sorted_df = filtered_df.orderBy("similarity", ascending=False)

    rating_matrix_df=sorted_df.selectExpr('user_id','foods_id','similarity')
    # 创建ALS模型实例
    als = ALS(userCol="user_id", itemCol="foods_id", ratingCol="similarity", coldStartStrategy="drop",implicitPrefs=True,maxIter=10,regParam=0.01)
    # 拆分数据集为训练集和测试集
    (training_data, test_data) = rating_matrix_df.randomSplit([0.8, 0.2])
    # 训练ALS模型
    model = als.fit(training_data)


    from pyspark.ml.evaluation import RegressionEvaluator
    # 使用测试集评估模型
    predictions = model.transform(test_data)

    # 创建 RegressionEvaluator 评估器
    evaluator = RegressionEvaluator(labelCol="similarity", predictionCol="prediction", metricName="rmse")
    # 计算 RMSE
    rmse = evaluator.evaluate(predictions)
    # 输出评估结果
    print("Root Mean Squared Error (RMSE):", rmse)
    df=model.recommendForAllUsers(200).selectExpr('user_id','cast(recommendations as string)')
    df.write.format('jdbc') \
            .mode('overwrite') \
            .option('url',
                    f"jdbc:mysql://{MYSQL_PARAMS.get('host')}:{MYSQL_PARAMS.get('port')}/{MYSQL_PARAMS.get('db')}?useSSL=false&useUnicode=true") \
            .option('dbtable', MYSQL_PARAMS.get('table')) \
            .option('user', MYSQL_PARAMS.get('user')) \
            .option('driver', 'com.mysql.jdbc.Driver') \
            .option('password', MYSQL_PARAMS.get('password')) \
            .save()

if __name__ == '__main__':
    train_run()
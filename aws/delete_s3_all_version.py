# edit by sakana - 2019/10/31
# 這個 python 是實驗刪除 bucket 內所有 versioning 的檔案, 然後嘗試刪除 bucket
# 還待修正內容
import boto3

# 定義 BUCKET, 要執行的 bucket
BUCKET = 'sakanatest'

# 定義使用 s3 resource
s3 = boto3.resource('s3')

# 使用 for 迴圈列出所有 bucket 的名稱
for bucket in s3.buckets.all():
  print(bucket.name)

# 定義 bucket, 爲剛剛定義的 bucket
bucket = s3.Bucket(BUCKET)

# 檢查相關資訊
print("bucket is :", bucket)

# 將該 bucket 內的所有 versioning 刪除
bucket.object_versions.all().delete()

# 刪除 bucket
bucket.delete()

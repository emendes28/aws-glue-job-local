import pandas
import localstack_client.session as boto3
from behave import when, then

s3_client = boto3.client('s3')

FONTE_DADOS_PATH = '../../fonte_dados/'
BUCKET_NAME = 'origem'

@when("quando o bucket for criado")
def criacao_do_bucket(context):
    response = s3_client.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={
            'LocationConstraint': 'sa-east-1'
        }
    )
    print(response)
    pass

@when("ouver um arquivo csv na pasta de fonte de dados")
def criar_arquivo_para_upload(context):
    data_frame_pandas = pandas.ead_excel(FONTE_DADOS_PATH+'WEOApr2021all.xls')
    data_frame_pandas.to_csv(FONTE_DADOS_PATH+'dados_fmi_abril_2021.csv')
    pass

@then("deverá haver um arquivo csv no bucket para estudo")
def upload_arquivo_s3(context):
    file = open(FONTE_DADOS_PATH+'dados_fmi_abril_2021.csv')
    response = s3_client.put_object(
        ACL='public-read',
        Body=file,
        Bucket=BUCKET_NAME,
        Key='a/origem'
    )
    print(response)
    pass

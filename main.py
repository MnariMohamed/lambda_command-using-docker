import subprocess
import os
import time
import json

S3_BUCKET = os.environ['S3_BUCKET']
AFRICA_S3_BUCKET = os.environ['AFRICA_S3_BUCKET']

timestamp = time.strftime('%Y-%m-%d-%I:%M')


def backup(event, context):
    print("Function started")

    dbHost = os.environ['DB_HOST']
    dbName = os.environ['DB_NAME']
    dbUser = os.environ['DB_USER']
    dbPass = os.environ['DB_PASS']
    africaDbHost = os.environ['AFRICA_DB_HOST']
    africaDbName = os.environ['AFRICA_DB_NAME']
    africaDbUser = os.environ['AFRICA_DB_USER']
    africaDbPass = os.environ['AFRICA_DB_PASS']

    print("%s %s ".format(dbHost, dbName))
    #FT db
    command = "mysqldump --host %s --user %s -p%s %s --no-tablespaces | gzip -c | aws s3 cp - s3://%s/%s.gz" % (
        dbHost, dbUser, dbPass, dbName, S3_BUCKET, dbName + "_" + timestamp)
    subprocess.Popen(command, shell=True).wait()

    print("%s %s ".format(africaDbHost, africaDbName))
    #africa db
    command2 = "mysqldump --host %s --user %s -p%s %s --no-tablespaces | gzip -c | aws s3 cp - s3://%s/%s.gz" % (
        africaDbHost, africaDbUser, africaDbPass, africaDbName, AFRICA_S3_BUCKET, africaDbName + "_" + timestamp)
    subprocess.Popen(command2, shell=True).wait()

    print("MySQL backup finished")
    return "backup finished"
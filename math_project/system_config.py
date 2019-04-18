import os
import configparser

config_parser = configparser.ConfigParser()
config_file = os.path.dirname(os.path.abspath(__file__)) + "/system.conf"
config_parser.read(config_file)


def get_business_server_host():
    return config_parser.get("business_server", "host")


def get_kafka_bootstrap_server(kf_type='installment'):
    """ There are two kafka cluster, one is for original business, the other
    is for risk control, named as risk. If you want to use risk kafka, assign
    `kf_type` to string 'risk' and add "risk.bootstrap.servers" to the 'kafka'
    section of your system.conf file.

    :param kf_type: specify which kafka to use. Default is 'installment'
    """
    if kf_type == 'risk':
        return config_parser.get("kafka", "risk.bootstrap.servers")
    else:
        return config_parser.get("kafka", "bootstrap.servers")


def get_logger_base_path():
    return config_parser.get("logger", "base_path")


def get_mysql_server_ip():
    return config_parser.get("mysql", "host")


def get_mysql_server_user():
    return config_parser.get("mysql", "user")


def get_mysql_passwd():
    return config_parser.get("mysql", "passwd")


def get_mysql_rule_db():
    return config_parser.get("mysql", "db")


def get_mysql_test_server_ip():
    try:
        return config_parser.get("mysql", "test_host")
    except:
        pass


def get_mysql_test_server_user():
    try:
        return config_parser.get("mysql", "test_user")
    except:
        pass


def get_mysql_test_passwd():
    try:
        return config_parser.get("mysql", "test_passwd")
    except:
        pass


def get_mysql_test_rule_db():
    try:
        return config_parser.get("mysql", "test_rule_db")
    except:
        pass

def get_mysql_default_db():
    return config_parser.get("mysql", "db")


def get_mysql_charset():
    return config_parser.get("mysql", "charset")


def get_mysql_master_server_ip():
    return config_parser.get("mysql", "master_host")


# def get_mysql_master_server_user():
#     return config_parser.get("mysql", "master_user")
#
#
# def get_mysql_master_passwd():
#     return config_parser.get("mysql", "master_passwd")
#
#
# def get_mysql_master_default_db():
#     return config_parser.get("mysql", "master_db")
#
#
# def get_mysql_recommd_server_ip():
#     return config_parser.get("mysql", "recommd_host")
#
#
# def get_mysql_recommd_server_user():
#     return config_parser.get("mysql", "recommd_user")
#
#
# def get_mysql_recommd_passwd():
#     return config_parser.get("mysql", "recommd_passwd")
#
#
# def get_mysql_recommd_default_db():
#     return config_parser.get("mysql", "recommd_db")
#
#
# def get_mysql_backup_server_ip():
#     return config_parser.get("mysql", "backup_host")
#
#
# def get_mysql_backup_server_user():
#     return config_parser.get("mysql", "backup_user")
#
#
# def get_mysql_backup_passwd():
#     return config_parser.get("mysql", "backup_passwd")
#
#
# def get_mysql_backup_default_db():
#     return config_parser.get("mysql", "backup_db")
#
#
# def get_mysql_aurora_backup_server_ip():
#     return config_parser.get("mysql", "aurora_backup_host")
#
#
# def get_mysql_aurora_backup_server_user():
#     return config_parser.get("mysql", "aurora_backup_user")
#
#
# def get_mysql_aurora_backup_passwd():
#     return config_parser.get("mysql", "aurora_backup_passwd")
#
#
# def get_mysql_aurora_backup_default_db():
#     return config_parser.get("mysql", "aurora_backup_db")
#
#
# def get_mysql_tidb_server_ip():
#     return config_parser.get("mysql", "tidb_host")
#
#
# def get_mysql_tidb_server_user():
#     return config_parser.get("mysql", "tidb_user")
#
#
# def get_mysql_tidb_passwd():
#     return config_parser.get("mysql", "tidb_passwd")
#
#
# def get_mysql_tidb_default_db():
#     return config_parser.get("mysql", "tidb_db")
#
#
# def get_mysql_tidb_port():
#     return config_parser.getint("mysql", "tidb_port")
#
#
# def get_mysql_feature_default_db():
#     return config_parser.get("mysql", "feature_db")
#
#
# def get_mysql_feature_host():
#     return config_parser.get("mysql", "feature_host")
#
#
# def get_mysql_feature_user():
#     return config_parser.get("mysql", "feature_user")
#
#
# def get_mysql_feature_passwd():
#     return config_parser.get("mysql", "feature_passwd")
#
#
# def get_mysql_feature_port():
#     return config_parser.get("mysql", "feature_port")
#
#
# def get_mysql_reptile_server_ip():
#     return config_parser.get("mysql", "reptile_host")
#
#
# def get_mysql_reptile_user():
#     return config_parser.get("mysql", "reptile_user")
#
#
# def get_mysql_reptile_passwd():
#     return config_parser.get("mysql", "reptile_passwd")
#

# def get_project_path():
#     return config_parser.get("system", "project_path")
#
#
# def get_neo4j_host():
#     try:
#         return config_parser.get("neo4j", "host")
#     except:
#         return ''
#
#
# def get_neo4j_username():
#     try:
#         return config_parser.get("neo4j", "username")
#     except:
#         return ''
#
#
# def get_neo4j_password():
#     try:
#         return config_parser.get("neo4j", "password")
#     except:
#         return ''
#
#
# def get_vn_neo4j_host():
#     try:
#         return config_parser.get("neo4j", "vn.host")
#     except:
#         return ''
#
#
# def get_vn_neo4j_username():
#     try:
#         return config_parser.get("neo4j", "vn.username")
#     except:
#         return ''
#
#
# def get_vn_neo4j_password():
#     try:
#         return config_parser.get("neo4j", "vn.password")
#     except:
#         return ''
#
#
# def get_s3_voice_bucket():
#     return config_parser.get("s3", "risk_voice_bucket")
#
#
# def get_s3_commit_voice_bucket():
#     return config_parser.get("s3", "commit_voice_bucket")
#
#
# def get_s3_auth_pic_bucket():
#     return config_parser.get("s3", "auth_pic_bucket")
#
#
# def get_aerospike_host():
#     return config_parser.get("aerospike", "host")
#
#
# def get_aerospikeitem_host():
#     return config_parser.get("aerospike", "host_item")
#
#
# def get_authzk_hosts():
#     return config_parser.get("authzk", "hosts")
#
#
# def get_redis_host():
#     try:
#         return config_parser.get("redis", "host")
#     except:
#         return 'localhost'
#
#
# def get_es_host():
#     return config_parser.get("elasticsearch", "es_host")
#
#
# def get_es_port():
#     return config_parser.get("elasticsearch", "es_port")
#
#
# def get_server_type():
#     try:
#         return config_parser.get("environment", "server_type")
#     except:
#         return 'local'
#
#
# def get_is_gpu_server():
#     return config_parser.getboolean("server_type", "is_gpu_server")
#
#
# def feature_data_service_host():
#     try:
#         return config_parser.get("inner_service_api", "feature_data_service_host")
#     except:
#         return 'localhost'
#
# def feature_data_test_service_host():
#     try:
#         return config_parser.get("inner_service_api", "feature_data_service_host_test")
#     except:
#         return 'localhost'


if __name__ == '__main__':
    print(get_server_type())

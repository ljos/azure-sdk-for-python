# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .migrate_sql_server_sql_mi_sync_task_output_py3 import MigrateSqlServerSqlMISyncTaskOutput


class MigrateSqlServerSqlMISyncTaskOutputMigrationLevel(MigrateSqlServerSqlMISyncTaskOutput):
    """MigrateSqlServerSqlMISyncTaskOutputMigrationLevel.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Result identifier
    :vartype id: str
    :param result_type: Required. Constant filled by server.
    :type result_type: str
    :ivar database_count: Count of databases
    :vartype database_count: int
    :ivar state: Current state of migration. Possible values include: 'None',
     'InProgress', 'Failed', 'Warning', 'Completed', 'Skipped', 'Stopped'
    :vartype state: str or ~azure.mgmt.datamigration.models.MigrationState
    :ivar started_on: Migration start time
    :vartype started_on: datetime
    :ivar ended_on: Migration end time
    :vartype ended_on: datetime
    :ivar source_server_name: Source server name
    :vartype source_server_name: str
    :ivar source_server_version: Source server version
    :vartype source_server_version: str
    :ivar source_server_brand_version: Source server brand version
    :vartype source_server_brand_version: str
    :ivar target_server_name: Target server name
    :vartype target_server_name: str
    :ivar target_server_version: Target server version
    :vartype target_server_version: str
    :ivar target_server_brand_version: Target server brand version
    :vartype target_server_brand_version: str
    :ivar database_error_count: Number of database level errors
    :vartype database_error_count: int
    """

    _validation = {
        'id': {'readonly': True},
        'result_type': {'required': True},
        'database_count': {'readonly': True},
        'state': {'readonly': True},
        'started_on': {'readonly': True},
        'ended_on': {'readonly': True},
        'source_server_name': {'readonly': True},
        'source_server_version': {'readonly': True},
        'source_server_brand_version': {'readonly': True},
        'target_server_name': {'readonly': True},
        'target_server_version': {'readonly': True},
        'target_server_brand_version': {'readonly': True},
        'database_error_count': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
        'database_count': {'key': 'databaseCount', 'type': 'int'},
        'state': {'key': 'state', 'type': 'str'},
        'started_on': {'key': 'startedOn', 'type': 'iso-8601'},
        'ended_on': {'key': 'endedOn', 'type': 'iso-8601'},
        'source_server_name': {'key': 'sourceServerName', 'type': 'str'},
        'source_server_version': {'key': 'sourceServerVersion', 'type': 'str'},
        'source_server_brand_version': {'key': 'sourceServerBrandVersion', 'type': 'str'},
        'target_server_name': {'key': 'targetServerName', 'type': 'str'},
        'target_server_version': {'key': 'targetServerVersion', 'type': 'str'},
        'target_server_brand_version': {'key': 'targetServerBrandVersion', 'type': 'str'},
        'database_error_count': {'key': 'databaseErrorCount', 'type': 'int'},
    }

    def __init__(self, **kwargs) -> None:
        super(MigrateSqlServerSqlMISyncTaskOutputMigrationLevel, self).__init__(**kwargs)
        self.database_count = None
        self.state = None
        self.started_on = None
        self.ended_on = None
        self.source_server_name = None
        self.source_server_version = None
        self.source_server_brand_version = None
        self.target_server_name = None
        self.target_server_version = None
        self.target_server_brand_version = None
        self.database_error_count = None
        self.result_type = 'MigrationLevelOutput'
# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.cloud.servicecontrol_v1.types import http_request as gas_http_request
from google.logging.type import log_severity_pb2 as log_severity  # type: ignore
from google.protobuf import any_pb2 as gp_any  # type: ignore
from google.protobuf import struct_pb2 as struct  # type: ignore
from google.protobuf import timestamp_pb2 as gp_timestamp  # type: ignore


__protobuf__ = proto.module(
    package="google.api.servicecontrol.v1",
    manifest={"LogEntry", "LogEntryOperation", "LogEntrySourceLocation",},
)


class LogEntry(proto.Message):
    r"""An individual log entry.

    Attributes:
        name (str):
            Required. The log to which this log entry belongs. Examples:
            ``"syslog"``, ``"book_log"``.
        timestamp (google.protobuf.timestamp_pb2.Timestamp):
            The time the event described by the log entry
            occurred. If omitted, defaults to operation
            start time.
        severity (google.logging.type.log_severity_pb2.LogSeverity):
            The severity of the log entry. The default value is
            ``LogSeverity.DEFAULT``.
        http_request (google.cloud.servicecontrol_v1.types.HttpRequest):
            Optional. Information about the HTTP request
            associated with this log entry, if applicable.
        trace (str):
            Optional. Resource name of the trace associated with the log
            entry, if any. If this field contains a relative resource
            name, you can assume the name is relative to
            ``//tracing.googleapis.com``. Example:
            ``projects/my-projectid/traces/06796866738c859f2f19b7cfb3214824``
        insert_id (str):
            A unique ID for the log entry used for deduplication. If
            omitted, the implementation will generate one based on
            operation_id.
        labels (Sequence[google.cloud.servicecontrol_v1.types.LogEntry.LabelsEntry]):
            A set of user-defined (key, value) data that
            provides additional information about the log
            entry.
        proto_payload (google.protobuf.any_pb2.Any):
            The log entry payload, represented as a protocol buffer that
            is expressed as a JSON object. The only accepted type
            currently is [AuditLog][google.cloud.audit.AuditLog].
        text_payload (str):
            The log entry payload, represented as a
            Unicode string (UTF-8).
        struct_payload (google.protobuf.struct_pb2.Struct):
            The log entry payload, represented as a
            structure that is expressed as a JSON object.
        operation (google.cloud.servicecontrol_v1.types.LogEntryOperation):
            Optional. Information about an operation
            associated with the log entry, if applicable.
        source_location (google.cloud.servicecontrol_v1.types.LogEntrySourceLocation):
            Optional. Source code location information
            associated with the log entry, if any.
    """

    name = proto.Field(proto.STRING, number=10)

    timestamp = proto.Field(proto.MESSAGE, number=11, message=gp_timestamp.Timestamp,)

    severity = proto.Field(proto.ENUM, number=12, enum=log_severity.LogSeverity,)

    http_request = proto.Field(
        proto.MESSAGE, number=14, message=gas_http_request.HttpRequest,
    )

    trace = proto.Field(proto.STRING, number=15)

    insert_id = proto.Field(proto.STRING, number=4)

    labels = proto.MapField(proto.STRING, proto.STRING, number=13)

    proto_payload = proto.Field(
        proto.MESSAGE, number=2, oneof="payload", message=gp_any.Any,
    )

    text_payload = proto.Field(proto.STRING, number=3, oneof="payload")

    struct_payload = proto.Field(
        proto.MESSAGE, number=6, oneof="payload", message=struct.Struct,
    )

    operation = proto.Field(proto.MESSAGE, number=16, message="LogEntryOperation",)

    source_location = proto.Field(
        proto.MESSAGE, number=17, message="LogEntrySourceLocation",
    )


class LogEntryOperation(proto.Message):
    r"""Additional information about a potentially long-running
    operation with which a log entry is associated.

    Attributes:
        id (str):
            Optional. An arbitrary operation identifier.
            Log entries with the same identifier are assumed
            to be part of the same operation.
        producer (str):
            Optional. An arbitrary producer identifier. The combination
            of ``id`` and ``producer`` must be globally unique. Examples
            for ``producer``: ``"MyDivision.MyBigCompany.com"``,
            ``"github.com/MyProject/MyApplication"``.
        first (bool):
            Optional. Set this to True if this is the
            first log entry in the operation.
        last (bool):
            Optional. Set this to True if this is the
            last log entry in the operation.
    """

    id = proto.Field(proto.STRING, number=1)

    producer = proto.Field(proto.STRING, number=2)

    first = proto.Field(proto.BOOL, number=3)

    last = proto.Field(proto.BOOL, number=4)


class LogEntrySourceLocation(proto.Message):
    r"""Additional information about the source code location that
    produced the log entry.

    Attributes:
        file (str):
            Optional. Source file name. Depending on the
            runtime environment, this might be a simple name
            or a fully-qualified name.
        line (int):
            Optional. Line within the source file.
            1-based; 0 indicates no line number available.
        function (str):
            Optional. Human-readable name of the function or method
            being invoked, with optional context such as the class or
            package name. This information may be used in contexts such
            as the logs viewer, where a file and line number are less
            meaningful. The format can vary by language. For example:
            ``qual.if.ied.Class.method`` (Java), ``dir/package.func``
            (Go), ``function`` (Python).
    """

    file = proto.Field(proto.STRING, number=1)

    line = proto.Field(proto.INT64, number=2)

    function = proto.Field(proto.STRING, number=3)


__all__ = tuple(sorted(__protobuf__.manifest))

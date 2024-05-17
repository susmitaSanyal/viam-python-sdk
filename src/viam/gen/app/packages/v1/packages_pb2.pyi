"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _PackageType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PackageTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PackageType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PACKAGE_TYPE_UNSPECIFIED: _PackageType.ValueType
    PACKAGE_TYPE_ARCHIVE: _PackageType.ValueType
    PACKAGE_TYPE_ML_MODEL: _PackageType.ValueType
    PACKAGE_TYPE_MODULE: _PackageType.ValueType
    PACKAGE_TYPE_SLAM_MAP: _PackageType.ValueType
    PACKAGE_TYPE_ML_TRAINING: _PackageType.ValueType

class PackageType(_PackageType, metaclass=_PackageTypeEnumTypeWrapper):
    ...
PACKAGE_TYPE_UNSPECIFIED: PackageType.ValueType
PACKAGE_TYPE_ARCHIVE: PackageType.ValueType
PACKAGE_TYPE_ML_MODEL: PackageType.ValueType
PACKAGE_TYPE_MODULE: PackageType.ValueType
PACKAGE_TYPE_SLAM_MAP: PackageType.ValueType
PACKAGE_TYPE_ML_TRAINING: PackageType.ValueType
global___PackageType = PackageType

@typing.final
class FileInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    IS_DIRECTORY_FIELD_NUMBER: builtins.int
    name: builtins.str
    size: builtins.int
    is_directory: builtins.bool

    def __init__(self, *, name: builtins.str=..., size: builtins.int=..., is_directory: builtins.bool | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_is_directory', b'_is_directory', 'is_directory', b'is_directory']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_is_directory', b'_is_directory', 'is_directory', b'is_directory', 'name', b'name', 'size', b'size']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing.Literal['_is_directory', b'_is_directory']) -> typing.Literal['is_directory'] | None:
        ...
global___FileInfo = FileInfo

@typing.final
class PackageInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    PLATFORM_FIELD_NUMBER: builtins.int
    FILES_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    name: builtins.str
    version: builtins.str
    type: global___PackageType.ValueType
    platform: builtins.str

    @property
    def files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FileInfo]:
        ...

    @property
    def metadata(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, organization_id: builtins.str=..., name: builtins.str=..., version: builtins.str=..., type: global___PackageType.ValueType=..., platform: builtins.str | None=..., files: collections.abc.Iterable[global___FileInfo] | None=..., metadata: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_platform', b'_platform', 'metadata', b'metadata', 'platform', b'platform']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_platform', b'_platform', 'files', b'files', 'metadata', b'metadata', 'name', b'name', 'organization_id', b'organization_id', 'platform', b'platform', 'type', b'type', 'version', b'version']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing.Literal['_platform', b'_platform']) -> typing.Literal['platform'] | None:
        ...
global___PackageInfo = PackageInfo

@typing.final
class CreatePackageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INFO_FIELD_NUMBER: builtins.int
    CONTENTS_FIELD_NUMBER: builtins.int
    contents: builtins.bytes
    '.tar.gz file'

    @property
    def info(self) -> global___PackageInfo:
        ...

    def __init__(self, *, info: global___PackageInfo | None=..., contents: builtins.bytes=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['contents', b'contents', 'info', b'info', 'package', b'package']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['contents', b'contents', 'info', b'info', 'package', b'package']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing.Literal['package', b'package']) -> typing.Literal['info', 'contents'] | None:
        ...
global___CreatePackageRequest = CreatePackageRequest

@typing.final
class CreatePackageResponse(google.protobuf.message.Message):
    """Returns the package ID and version which are populated in GetPackageRequest and DeletePackageRequest to
    retrieve or delete this package.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    id: builtins.str
    version: builtins.str

    def __init__(self, *, id: builtins.str=..., version: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['id', b'id', 'version', b'version']) -> None:
        ...
global___CreatePackageResponse = CreatePackageResponse

@typing.final
class DeletePackageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    id: builtins.str
    version: builtins.str
    type: global___PackageType.ValueType

    def __init__(self, *, id: builtins.str=..., version: builtins.str=..., type: global___PackageType.ValueType=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['id', b'id', 'type', b'type', 'version', b'version']) -> None:
        ...
global___DeletePackageRequest = DeletePackageRequest

@typing.final
class DeletePackageResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___DeletePackageResponse = DeletePackageResponse

@typing.final
class Package(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INFO_FIELD_NUMBER: builtins.int
    URL_FIELD_NUMBER: builtins.int
    CREATED_ON_FIELD_NUMBER: builtins.int
    CHECKSUM_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    url: builtins.str
    checksum: builtins.str
    id: builtins.str

    @property
    def info(self) -> global___PackageInfo:
        ...

    @property
    def created_on(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    def __init__(self, *, info: global___PackageInfo | None=..., url: builtins.str=..., created_on: google.protobuf.timestamp_pb2.Timestamp | None=..., checksum: builtins.str=..., id: builtins.str=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['created_on', b'created_on', 'info', b'info']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['checksum', b'checksum', 'created_on', b'created_on', 'id', b'id', 'info', b'info', 'url', b'url']) -> None:
        ...
global___Package = Package

@typing.final
class GetPackageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    INCLUDE_URL_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    PLATFORM_FIELD_NUMBER: builtins.int
    id: builtins.str
    version: builtins.str
    include_url: builtins.bool
    type: global___PackageType.ValueType
    platform: builtins.str

    def __init__(self, *, id: builtins.str=..., version: builtins.str=..., include_url: builtins.bool | None=..., type: global___PackageType.ValueType | None=..., platform: builtins.str | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_include_url', b'_include_url', '_platform', b'_platform', '_type', b'_type', 'include_url', b'include_url', 'platform', b'platform', 'type', b'type']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_include_url', b'_include_url', '_platform', b'_platform', '_type', b'_type', 'id', b'id', 'include_url', b'include_url', 'platform', b'platform', 'type', b'type', 'version', b'version']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_include_url', b'_include_url']) -> typing.Literal['include_url'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_platform', b'_platform']) -> typing.Literal['platform'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_type', b'_type']) -> typing.Literal['type'] | None:
        ...
global___GetPackageRequest = GetPackageRequest

@typing.final
class GetPackageResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PACKAGE_FIELD_NUMBER: builtins.int

    @property
    def package(self) -> global___Package:
        ...

    def __init__(self, *, package: global___Package | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['package', b'package']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['package', b'package']) -> None:
        ...
global___GetPackageResponse = GetPackageResponse

@typing.final
class ListPackagesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    INCLUDE_URL_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    name: builtins.str
    version: builtins.str
    type: global___PackageType.ValueType
    include_url: builtins.bool

    def __init__(self, *, organization_id: builtins.str=..., name: builtins.str | None=..., version: builtins.str | None=..., type: global___PackageType.ValueType | None=..., include_url: builtins.bool | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_include_url', b'_include_url', '_name', b'_name', '_type', b'_type', '_version', b'_version', 'include_url', b'include_url', 'name', b'name', 'type', b'type', 'version', b'version']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_include_url', b'_include_url', '_name', b'_name', '_type', b'_type', '_version', b'_version', 'include_url', b'include_url', 'name', b'name', 'organization_id', b'organization_id', 'type', b'type', 'version', b'version']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_include_url', b'_include_url']) -> typing.Literal['include_url'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_name', b'_name']) -> typing.Literal['name'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_type', b'_type']) -> typing.Literal['type'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_version', b'_version']) -> typing.Literal['version'] | None:
        ...
global___ListPackagesRequest = ListPackagesRequest

@typing.final
class ListPackagesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PACKAGES_FIELD_NUMBER: builtins.int

    @property
    def packages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Package]:
        ...

    def __init__(self, *, packages: collections.abc.Iterable[global___Package] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['packages', b'packages']) -> None:
        ...
global___ListPackagesResponse = ListPackagesResponse
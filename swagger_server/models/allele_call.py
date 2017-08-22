# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.feature import Feature
from swagger_server.models.typing import Typing
from swagger_server.models.typing_status import TypingStatus
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class AlleleCall(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, typing: List[Typing]=None, features: List[Feature]=None, ihiw_ref: List[Typing]=None, full_gene: Feature=None, typing_status: TypingStatus=None, gfe: str=None, act_version: str=None, gfe_version: str=None, gfedb_version: str=None, imgtdb_version: str=None):
        """
        AlleleCall - a model defined in Swagger

        :param typing: The typing of this AlleleCall.
        :type typing: List[Typing]
        :param features: The features of this AlleleCall.
        :type features: List[Feature]
        :param ihiw_ref: The ihiw_ref of this AlleleCall.
        :type ihiw_ref: List[Typing]
        :param full_gene: The full_gene of this AlleleCall.
        :type full_gene: Feature
        :param typing_status: The typing_status of this AlleleCall.
        :type typing_status: TypingStatus
        :param gfe: The gfe of this AlleleCall.
        :type gfe: str
        :param act_version: The act_version of this AlleleCall.
        :type act_version: str
        :param gfe_version: The gfe_version of this AlleleCall.
        :type gfe_version: str
        :param gfedb_version: The gfedb_version of this AlleleCall.
        :type gfedb_version: str
        :param imgtdb_version: The imgtdb_version of this AlleleCall.
        :type imgtdb_version: str
        """
        self.swagger_types = {
            'typing': List[Typing],
            'features': List[Feature],
            'ihiw_ref': List[Typing],
            'full_gene': Feature,
            'typing_status': TypingStatus,
            'gfe': str,
            'act_version': str,
            'gfe_version': str,
            'gfedb_version': str,
            'imgtdb_version': str
        }

        self.attribute_map = {
            'typing': 'typing',
            'features': 'features',
            'ihiw_ref': 'ihiw_ref',
            'full_gene': 'full_gene',
            'typing_status': 'typing_status',
            'gfe': 'gfe',
            'act_version': 'act_version',
            'gfe_version': 'gfe_version',
            'gfedb_version': 'gfedb_version',
            'imgtdb_version': 'imgtdb_version'
        }

        self._typing = typing
        self._features = features
        self._ihiw_ref = ihiw_ref
        self._full_gene = full_gene
        self._typing_status = typing_status
        self._gfe = gfe
        self._act_version = act_version
        self._gfe_version = gfe_version
        self._gfedb_version = gfedb_version
        self._imgtdb_version = imgtdb_version

    @classmethod
    def from_dict(cls, dikt) -> 'AlleleCall':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AlleleCall of this AlleleCall.
        :rtype: AlleleCall
        """
        return deserialize_model(dikt, cls)

    @property
    def typing(self) -> List[Typing]:
        """
        Gets the typing of this AlleleCall.

        :return: The typing of this AlleleCall.
        :rtype: List[Typing]
        """
        return self._typing

    @typing.setter
    def typing(self, typing: List[Typing]):
        """
        Sets the typing of this AlleleCall.

        :param typing: The typing of this AlleleCall.
        :type typing: List[Typing]
        """

        self._typing = typing

    @property
    def features(self) -> List[Feature]:
        """
        Gets the features of this AlleleCall.

        :return: The features of this AlleleCall.
        :rtype: List[Feature]
        """
        return self._features

    @features.setter
    def features(self, features: List[Feature]):
        """
        Sets the features of this AlleleCall.

        :param features: The features of this AlleleCall.
        :type features: List[Feature]
        """

        self._features = features

    @property
    def ihiw_ref(self) -> List[Typing]:
        """
        Gets the ihiw_ref of this AlleleCall.

        :return: The ihiw_ref of this AlleleCall.
        :rtype: List[Typing]
        """
        return self._ihiw_ref

    @ihiw_ref.setter
    def ihiw_ref(self, ihiw_ref: List[Typing]):
        """
        Sets the ihiw_ref of this AlleleCall.

        :param ihiw_ref: The ihiw_ref of this AlleleCall.
        :type ihiw_ref: List[Typing]
        """

        self._ihiw_ref = ihiw_ref

    @property
    def full_gene(self) -> Feature:
        """
        Gets the full_gene of this AlleleCall.

        :return: The full_gene of this AlleleCall.
        :rtype: Feature
        """
        return self._full_gene

    @full_gene.setter
    def full_gene(self, full_gene: Feature):
        """
        Sets the full_gene of this AlleleCall.

        :param full_gene: The full_gene of this AlleleCall.
        :type full_gene: Feature
        """

        self._full_gene = full_gene

    @property
    def typing_status(self) -> TypingStatus:
        """
        Gets the typing_status of this AlleleCall.

        :return: The typing_status of this AlleleCall.
        :rtype: TypingStatus
        """
        return self._typing_status

    @typing_status.setter
    def typing_status(self, typing_status: TypingStatus):
        """
        Sets the typing_status of this AlleleCall.

        :param typing_status: The typing_status of this AlleleCall.
        :type typing_status: TypingStatus
        """

        self._typing_status = typing_status

    @property
    def gfe(self) -> str:
        """
        Gets the gfe of this AlleleCall.

        :return: The gfe of this AlleleCall.
        :rtype: str
        """
        return self._gfe

    @gfe.setter
    def gfe(self, gfe: str):
        """
        Sets the gfe of this AlleleCall.

        :param gfe: The gfe of this AlleleCall.
        :type gfe: str
        """

        self._gfe = gfe

    @property
    def act_version(self) -> str:
        """
        Gets the act_version of this AlleleCall.

        :return: The act_version of this AlleleCall.
        :rtype: str
        """
        return self._act_version

    @act_version.setter
    def act_version(self, act_version: str):
        """
        Sets the act_version of this AlleleCall.

        :param act_version: The act_version of this AlleleCall.
        :type act_version: str
        """

        self._act_version = act_version

    @property
    def gfe_version(self) -> str:
        """
        Gets the gfe_version of this AlleleCall.

        :return: The gfe_version of this AlleleCall.
        :rtype: str
        """
        return self._gfe_version

    @gfe_version.setter
    def gfe_version(self, gfe_version: str):
        """
        Sets the gfe_version of this AlleleCall.

        :param gfe_version: The gfe_version of this AlleleCall.
        :type gfe_version: str
        """

        self._gfe_version = gfe_version

    @property
    def gfedb_version(self) -> str:
        """
        Gets the gfedb_version of this AlleleCall.

        :return: The gfedb_version of this AlleleCall.
        :rtype: str
        """
        return self._gfedb_version

    @gfedb_version.setter
    def gfedb_version(self, gfedb_version: str):
        """
        Sets the gfedb_version of this AlleleCall.

        :param gfedb_version: The gfedb_version of this AlleleCall.
        :type gfedb_version: str
        """

        self._gfedb_version = gfedb_version

    @property
    def imgtdb_version(self) -> str:
        """
        Gets the imgtdb_version of this AlleleCall.

        :return: The imgtdb_version of this AlleleCall.
        :rtype: str
        """
        return self._imgtdb_version

    @imgtdb_version.setter
    def imgtdb_version(self, imgtdb_version: str):
        """
        Sets the imgtdb_version of this AlleleCall.

        :param imgtdb_version: The imgtdb_version of this AlleleCall.
        :type imgtdb_version: str
        """

        self._imgtdb_version = imgtdb_version


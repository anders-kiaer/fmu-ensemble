# -*- coding: utf-8 -*-
"""Module for parsing an ensemble from FMU. This class represents an
ensemble, which is nothing but a collection of realizations.

The typical task of this class is book-keeping of each realization,
and abilities to aggregate any information that each realization can
provide.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from fmu.config import etc


xfmu = etc.Interaction()
logger = xfmu.functionlogger(__name__)


class Delta(object):

    def __init__(self, ref, adds=None, subs=None):
        """
        The Delta object is used to substract or add Ensembles.

        Args:
            ref (obj): Name identifier for the ensemble ref case.
            ior (obj): Name identifier for the ensemble ior case.
        """

        self.ref = ref
        self.adds = []
        self.subs = []
        if adds:
            self.adds.append(adds)
        if subs:
            self.subs.append(subs)
        self.combined = self.find_combined()

    def find_combined(self):
        ref_ok = set(self.ref.get_ok().query('OK == True')['REAL'].tolist())
        operations = self.subs + self.adds
        for operator in operations:
            ior_ok = set(operator.get_ok().query('OK == True')['REAL'].tolist())
            ref_ok = list(ref_ok & ior_ok)
        return ref_ok

    def get_smmry(self, column_keys=None):
        time_index = self.ref.get_smry_dates(freq='daily')
        ref = self.ref.get_smry(time_index=time_index, column_keys=column_keys,
                                stacked=True)
        ref = ref[ref['REAL'].isin(self.combined)]
        if self.subs:
            for sub in self.subs:
                ior = sub.get_smry(time_index=time_index,
                                   column_keys=column_keys,
                                   stacked=True)
                ior = ior[ior['REAL'].isin(self.combined)]
                ref = ior - ref
        if self.adds:
            for add in self.adds:
                ior = add.get_smry(time_index=time_index,
                                   column_keys=column_keys,
                                   stacked=True)
                ior = ior[ior['REAL'].isin(self.combined)]
                # must drop the date axis as you cannot add time, only sub
                if 'DATE' in ref.columns:
                    ref = ior.drop(columns=['DATE'])+ref.drop(columns=['DATE'])
                else:
                    ref = ior.drop(columns=['DATE'])+ref

        ref['DATE'] = ior['DATE']
        ref['REAL'] = ior['REAL']

        return ref

    def __sub__(self, other):
        self.subs.append(other)
        return self

    def __add__(self, other):
        self.adds.append(other)
        return self

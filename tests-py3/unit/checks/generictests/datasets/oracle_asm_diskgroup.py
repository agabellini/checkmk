#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore
checkname = 'oracle_asm_diskgroup'

info = [
    [
        None, 'MOUNTED', 'NORMAL', 'N', '512', '4096', '1048576', '3072',
        '2146', '309', '918', '0', 'Y', 'OCR_VOTE/'
    ],
    [
        None, 'MOUNTED', 'EXTERN', 'FRA', '4096', '4194304', '0', '10236',
        '4468', 'FRA01', 'N', 'REGULAR', '0', '8640000', '1'
    ],
    [
        None, 'DISMOUNTED', 'EXTERN', 'GRID', '4096', '4194304', '0', '5112',
        '5016', 'GRID01', 'N', 'REGULAR', '0', '8640000', '1'
    ],
    [
        None, 'MOUNTED', 'NORMAL', 'DATA', '4096', '4194304', '102396',
        '614376', '476280', 'NS1', 'N', 'REGULAR', '0', '8640000', '3'
    ]
]

discovery = {'': [('DATA', {}), ('FRA', {}), ('GRID', {}), ('OCR_VOTE', {})]}

checks = {
    '': [
        (
            'DATA', {
                'levels': (80.0, 90.0),
                'magic_normsize': 20,
                'levels_low': (50.0, 60.0),
                'trend_range': 24,
                'trend_perfdata': True,
                'req_mir_free': False
            }, [
                (
                    0,
                    '22.48% used (134.86 of 599.98 GB), normal redundancy, 3 disks in 1 failgroups',
                    [
                        ('fs_used', 138096, 491500.8, 552938.4, 0, 614376),
                        ('fs_size', 614376, None, None, None, None),
                        (
                            'fs_used_percent', 22.47744052502051, None, None,
                            None, None
                        )
                    ]
                )
            ]
        ),
        (
            'FRA', {
                'levels': (80.0, 90.0),
                'magic_normsize': 20,
                'levels_low': (50.0, 60.0),
                'trend_range': 24,
                'trend_perfdata': True,
                'req_mir_free': False
            }, [
                (
                    0,
                    '56.35% used (5.63 of 10.00 GB), extern redundancy, 1 disks',
                    [
                        ('fs_used', 5768, 8188.8, 9212.4, 0, 10236),
                        ('fs_size', 10236, None, None, None, None),
                        (
                            'fs_used_percent', 56.35013677217663, None, None,
                            None, None
                        )
                    ]
                )
            ]
        ),
        (
            'GRID', {
                'levels': (80.0, 90.0),
                'magic_normsize': 20,
                'levels_low': (50.0, 60.0),
                'trend_range': 24,
                'trend_perfdata': True,
                'req_mir_free': False
            }, [(2, 'Diskgroup dismounted', [])]
        ),
        (
            'OCR_VOTE', {
                'levels': (80.0, 90.0),
                'magic_normsize': 20,
                'levels_low': (50.0, 60.0),
                'trend_range': 24,
                'trend_perfdata': True,
                'req_mir_free': False
            }, [
                (
                    0,
                    '30.18% used (309.00 MB of 1.00 GB), normal redundancy, old plugin data, possible wrong used and free space',
                    [
                        ('fs_used', 309, 819.2, 921.6, 0, 1024),
                        ('fs_size', 1024, None, None, None, None),
                        (
                            'fs_used_percent', 30.17578125, None, None, None,
                            None
                        )
                    ]
                )
            ]
        )
    ]
}

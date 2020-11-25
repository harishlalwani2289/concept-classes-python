import matplotlib.pyplot as plt

coronaData = {
    "AN": {
        "delta": {
            "confirmed": 3
        },
        "districts": {
            "North and Middle Andaman": {
                "total": {
                    "confirmed": 1,
                    "recovered": 1
                }
            },
            "South Andaman": {
                "meta": {
                    "population": 238142
                },
                "total": {
                    "confirmed": 51,
                    "recovered": 32
                }
            },
            "Unknown": {
                "delta": {
                    "confirmed": 3
                },
                "total": {
                    "confirmed": 67,
                    "recovered": 21
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-04T09:44:28+05:30",
            "population": 397000,
            "tested": {
                "last_updated": "2020-07-01",
                "source": "https://dhs.andaman.gov.in/NewEvents/313.pdf"
            }
        },
        "total": {
            "confirmed": 119,
            "recovered": 54,
            "tested": 15982
        }
    },
    "AP": {
        "delta": {
            "confirmed": 765,
            "deceased": 12,
            "recovered": 376,
            "tested": 24962
        },
        "districts": {
            "Anantapur": {
                "delta": {
                    "confirmed": 127,
                    "recovered": 28
                },
                "meta": {
                    "population": 4081148,
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 2099,
                    "deceased": 9,
                    "recovered": 1139,
                    "tested": 64442
                }
            },
            "Chittoor": {
                "delta": {
                    "confirmed": 67,
                    "deceased": 2,
                    "recovered": 52
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 1250,
                    "deceased": 10,
                    "recovered": 463,
                    "tested": 69789
                }
            },
            "East Godavari": {
                "delta": {
                    "confirmed": 102,
                    "recovered": 28
                },
                "meta": {
                    "population": 5154296,
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 1489,
                    "deceased": 8,
                    "recovered": 416,
                    "tested": 96237
                }
            },
            "Foreign Evacuees": {
                "delta": {
                    "confirmed": 6,
                    "recovered": 25
                },
                "total": {
                    "confirmed": 415,
                    "recovered": 185
                }
            },
            "Guntur": {
                "delta": {
                    "confirmed": 60
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 1670,
                    "deceased": 19,
                    "recovered": 713,
                    "tested": 79349
                }
            },
            "Krishna": {
                "delta": {
                    "confirmed": 70,
                    "recovered": 16
                },
                "meta": {
                    "population": 4517398,
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 1681,
                    "deceased": 68,
                    "recovered": 669,
                    "tested": 94199
                }
            },
            "Kurnool": {
                "delta": {
                    "confirmed": 118,
                    "deceased": 3,
                    "recovered": 58
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 2354,
                    "deceased": 76,
                    "recovered": 1147,
                    "tested": 86170
                }
            },
            "Other State": {
                "delta": {
                    "confirmed": 32,
                    "recovered": 40
                },
                "total": {
                    "confirmed": 2143,
                    "recovered": 1386
                }
            },
            "Prakasam": {
                "delta": {
                    "confirmed": 57,
                    "recovered": 38
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 673,
                    "deceased": 2,
                    "recovered": 305,
                    "tested": 61021
                }
            },
            "S.P.S. Nellore": {
                "delta": {
                    "confirmed": 27
                },
                "meta": {
                    "population": 558548,
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 685,
                    "deceased": 6,
                    "recovered": 374,
                    "tested": 55644
                }
            },
            "Srikakulam": {
                "delta": {
                    "deceased": 3
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 93,
                    "deceased": 6,
                    "recovered": 54,
                    "tested": 92579
                }
            },
            "Visakhapatnam": {
                "delta": {
                    "confirmed": 9,
                    "deceased": 2,
                    "recovered": 43
                },
                "meta": {
                    "population": 4290589,
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 633,
                    "deceased": 5,
                    "recovered": 359,
                    "tested": 67682
                }
            },
            "Vizianagaram": {
                "delta": {
                    "confirmed": 13,
                    "deceased": 1,
                    "recovered": 7
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 197,
                    "deceased": 3,
                    "recovered": 63,
                    "tested": 37774
                }
            },
            "West Godavari": {
                "delta": {
                    "confirmed": 4,
                    "recovered": 41
                },
                "meta": {
                    "population": 3936966,
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 1124,
                    "deceased": 4,
                    "recovered": 309,
                    "tested": 59217
                }
            },
            "Y.S.R. Kadapa": {
                "delta": {
                    "confirmed": 73,
                    "deceased": 1
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 1193,
                    "deceased": 2,
                    "recovered": 426,
                    "tested": 66138
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-04T14:46:27+05:30",
            "notes": "Total includes patients from other states and a new category \"Foreign Evacuees\" which is now reported in AP bulletin.",
            "population": 52221000,
            "tested": {
                "last_updated": "2020-07-04",
                "source": "https://twitter.com/ArogyaAndhra/status/1279329071755714560?s=20"
            }
        },
        "total": {
            "confirmed": 17699,
            "deceased": 218,
            "recovered": 8008,
            "tested": 996573
        }
    },
    "AR": {
        "districts": {
            "Anjaw": {
                "meta": {
                    "population": 21167,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 178
                }
            },
            "Capital Complex": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 7500
                }
            },
            "Changlang": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 89,
                    "recovered": 37,
                    "tested": 4556
                }
            },
            "Dibang Valley": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 10
                }
            },
            "East Kameng": {
                "meta": {
                    "population": 78690,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 215
                }
            },
            "East Siang": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 10,
                    "recovered": 10,
                    "tested": 2011
                }
            },
            "Kamle": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 54
                }
            },
            "Kra-Daadi": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 13
                }
            },
            "Kurung Kumey": {
                "meta": {
                    "population": 92076,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 11
                }
            },
            "Lepa Rada": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 1,
                    "tested": 162
                }
            },
            "Lohit": {
                "meta": {
                    "population": 145726,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 4,
                    "recovered": 3,
                    "tested": 1145
                }
            },
            "Longding": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 4,
                    "recovered": 1,
                    "tested": 701
                }
            },
            "Lower Dibang Valley": {
                "meta": {
                    "population": 54080,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 3,
                    "recovered": 2,
                    "tested": 855
                }
            },
            "Lower Siang": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 3,
                    "tested": 479
                }
            },
            "Lower Subansiri": {
                "meta": {
                    "population": 83030,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 530
                }
            },
            "Namsai": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 13,
                    "recovered": 3,
                    "tested": 1520
                }
            },
            "Pakke Kessang": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 1,
                    "recovered": 1,
                    "tested": 255
                }
            },
            "Papum Pare": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 89,
                    "recovered": 8,
                    "tested": 689
                }
            },
            "Shi Yomi": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 80
                }
            },
            "Siang": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 122
                }
            },
            "Tawang": {
                "meta": {
                    "population": 49977,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 2,
                    "tested": 742
                }
            },
            "Tirap": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 3,
                    "recovered": 2,
                    "tested": 1410
                }
            },
            "Upper Siang": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 1,
                    "recovered": 1,
                    "tested": 457
                }
            },
            "Upper Subansiri": {
                "meta": {
                    "population": 83448,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 488
                }
            },
            "West Kameng": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 27,
                    "deceased": 1,
                    "recovered": 6,
                    "tested": 1188
                }
            },
            "West Siang": {
                "meta": {
                    "population": 112274,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 2,
                    "recovered": 1,
                    "tested": 546
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-04T00:26:29+05:30",
            "population": 1504000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
            }
        },
        "total": {
            "confirmed": 252,
            "deceased": 1,
            "recovered": 75,
            "tested": 25917
        }
    },
    "AS": {
        "districts": {
            "Airport Quarantine": {
                "total": {
                    "confirmed": 4
                }
            },
            "Baksa": {
                "total": {
                    "confirmed": 85
                }
            },
            "Barpeta": {
                "meta": {
                    "population": 1693622
                },
                "total": {
                    "confirmed": 150,
                    "recovered": 55
                }
            },
            "Biswanath": {
                "total": {
                    "confirmed": 58,
                    "recovered": 16
                }
            },
            "Bongaigaon": {
                "meta": {
                    "population": 738804
                },
                "total": {
                    "confirmed": 24,
                    "recovered": 7
                }
            },
            "Cachar": {
                "total": {
                    "confirmed": 98,
                    "recovered": 82
                }
            },
            "Charaideo": {
                "total": {
                    "confirmed": 16
                }
            },
            "Chirang": {
                "total": {
                    "confirmed": 52
                }
            },
            "Darrang": {
                "meta": {
                    "population": 928500
                },
                "total": {
                    "confirmed": 102
                }
            },
            "Dhemaji": {
                "total": {
                    "confirmed": 96,
                    "recovered": 6
                }
            },
            "Dhubri": {
                "meta": {
                    "population": 1949258
                },
                "total": {
                    "confirmed": 334,
                    "recovered": 5
                }
            },
            "Dibrugarh": {
                "total": {
                    "confirmed": 77,
                    "recovered": 5
                }
            },
            "Dima Hasao": {
                "meta": {
                    "population": 214102
                },
                "total": {
                    "confirmed": 89,
                    "recovered": 9
                }
            },
            "Goalpara": {
                "total": {
                    "confirmed": 57,
                    "recovered": 4
                }
            },
            "Golaghat": {
                "meta": {
                    "population": 1066888
                },
                "total": {
                    "confirmed": 272,
                    "recovered": 88
                }
            },
            "Hailakandi": {
                "total": {
                    "confirmed": 78,
                    "deceased": 1,
                    "recovered": 5
                }
            },
            "Hojai": {
                "total": {
                    "confirmed": 267
                }
            },
            "Jorhat": {
                "total": {
                    "confirmed": 145,
                    "recovered": 54
                }
            },
            "Kamrup": {
                "meta": {
                    "population": 1517542
                },
                "total": {
                    "confirmed": 215,
                    "recovered": 21
                }
            },
            "Kamrup Metropolitan": {
                "total": {
                    "confirmed": 2419,
                    "deceased": 6,
                    "recovered": 383
                }
            },
            "Karbi Anglong": {
                "meta": {
                    "population": 956313
                },
                "total": {
                    "confirmed": 41,
                    "recovered": 7
                }
            },
            "Karimganj": {
                "total": {
                    "confirmed": 106,
                    "recovered": 20
                }
            },
            "Kokrajhar": {
                "meta": {
                    "population": 887142
                },
                "total": {
                    "confirmed": 86,
                    "recovered": 10
                }
            },
            "Lakhimpur": {
                "total": {
                    "confirmed": 85,
                    "recovered": 6
                }
            },
            "Majuli": {
                "total": {
                    "confirmed": 21
                }
            },
            "Morigaon": {
                "total": {
                    "confirmed": 49,
                    "recovered": 28
                }
            },
            "Nagaon": {
                "meta": {
                    "population": 2823768
                },
                "total": {
                    "confirmed": 330,
                    "recovered": 25
                }
            },
            "Nalbari": {
                "total": {
                    "confirmed": 28,
                    "recovered": 9
                }
            },
            "Other State": {
                "total": {
                    "confirmed": 1,
                    "recovered": 1
                }
            },
            "Sivasagar": {
                "total": {
                    "confirmed": 29,
                    "recovered": 26
                }
            },
            "Sonitpur": {
                "meta": {
                    "population": 1924110
                },
                "total": {
                    "confirmed": 122,
                    "recovered": 35
                }
            },
            "South Salmara Mankachar": {
                "total": {
                    "confirmed": 7,
                    "recovered": 1
                }
            },
            "Tinsukia": {
                "total": {
                    "confirmed": 114,
                    "recovered": 6
                }
            },
            "Udalguri": {
                "meta": {
                    "population": 831668
                },
                "total": {
                    "confirmed": 105,
                    "recovered": 2
                }
            },
            "Unknown": {
                "total": {
                    "confirmed": 4010,
                    "deceased": 7,
                    "migrated": 3,
                    "recovered": 5412
                }
            },
            "West Karbi Anglong": {
                "total": {
                    "confirmed": 28
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-04T00:26:27+05:30",
            "notes": "Includes one case from Nagaland.\nTotal of 3 patients who migrated to other states has been reduced from Active count",
            "population": 34293000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/nhm_assam/status/1279085918721171456?s=20"
            }
        },
        "total": {
            "confirmed": 9800,
            "deceased": 14,
            "migrated": 3,
            "recovered": 6328,
            "tested": 438882
        }
    },
    "BR": {
        "districts": {
            "Araria": {
                "meta": {
                    "population": 2811569
                },
                "total": {
                    "confirmed": 133,
                    "deceased": 1,
                    "recovered": 111
                }
            },
            "Arwal": {
                "total": {
                    "confirmed": 117,
                    "deceased": 1,
                    "recovered": 94
                }
            },
            "Aurangabad": {
                "total": {
                    "confirmed": 281,
                    "deceased": 1,
                    "recovered": 198
                }
            },
            "Banka": {
                "total": {
                    "confirmed": 238,
                    "recovered": 227
                }
            },
            "Begusarai": {
                "meta": {
                    "population": 2970541,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DM_Begusarai/status/1278980126282182657?s=20"
                    }
                },
                "total": {
                    "confirmed": 476,
                    "deceased": 4,
                    "recovered": 364,
                    "tested": 9308
                }
            },
            "Bhagalpur": {
                "total": {
                    "confirmed": 554,
                    "deceased": 1,
                    "recovered": 360
                }
            },
            "Bhojpur": {
                "meta": {
                    "population": 2728407
                },
                "total": {
                    "confirmed": 253,
                    "deceased": 3,
                    "recovered": 157
                }
            },
            "Buxar": {
                "total": {
                    "confirmed": 230,
                    "recovered": 209
                }
            },
            "Darbhanga": {
                "meta": {
                    "population": 3937385
                },
                "total": {
                    "confirmed": 337,
                    "deceased": 5,
                    "recovered": 264
                }
            },
            "East Champaran": {
                "total": {
                    "confirmed": 242,
                    "deceased": 4,
                    "recovered": 201
                }
            },
            "Gaya": {
                "meta": {
                    "population": 4391418
                },
                "total": {
                    "confirmed": 232,
                    "deceased": 3,
                    "recovered": 167
                }
            },
            "Gopalganj": {
                "total": {
                    "confirmed": 291,
                    "recovered": 224
                }
            },
            "Jamui": {
                "meta": {
                    "population": 1760405
                },
                "total": {
                    "confirmed": 93,
                    "deceased": 1,
                    "recovered": 66
                }
            },
            "Jehanabad": {
                "total": {
                    "confirmed": 257,
                    "deceased": 3,
                    "recovered": 219
                }
            },
            "Kaimur": {
                "total": {
                    "confirmed": 205,
                    "deceased": 1,
                    "recovered": 147
                }
            },
            "Katihar": {
                "total": {
                    "confirmed": 355,
                    "deceased": 1,
                    "recovered": 251
                }
            },
            "Khagaria": {
                "meta": {
                    "population": 1666886,
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://twitter.com/KhagariaDm/status/1278717329908486145/photo/1"
                    }
                },
                "total": {
                    "confirmed": 305,
                    "deceased": 3,
                    "recovered": 293,
                    "tested": 5932
                }
            },
            "Kishanganj": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-09",
                        "source": "https://twitter.com/DKishanganj/status/1270336890378563584?s=20"
                    }
                },
                "total": {
                    "confirmed": 190,
                    "deceased": 1,
                    "recovered": 146,
                    "tested": 1432
                }
            },
            "Lakhisarai": {
                "meta": {
                    "population": 1000912
                },
                "total": {
                    "confirmed": 135,
                    "recovered": 124
                }
            },
            "Madhepura": {
                "total": {
                    "confirmed": 210,
                    "deceased": 1,
                    "recovered": 157
                }
            },
            "Madhubani": {
                "meta": {
                    "population": 4487379
                },
                "total": {
                    "confirmed": 492,
                    "deceased": 2,
                    "recovered": 356
                }
            },
            "Munger": {
                "total": {
                    "confirmed": 391,
                    "deceased": 1,
                    "recovered": 298
                }
            },
            "Muzaffarpur": {
                "meta": {
                    "population": 4801062,
                    "tested": {
                        "last_updated": "2020-06-07",
                        "source": "https://twitter.com/DM_Muzaffarpur/status/1269674059085811712?s=20"
                    }
                },
                "total": {
                    "confirmed": 400,
                    "deceased": 4,
                    "recovered": 262,
                    "tested": 2893
                }
            },
            "Nalanda": {
                "total": {
                    "confirmed": 328,
                    "deceased": 5,
                    "recovered": 176
                }
            },
            "Nawada": {
                "meta": {
                    "population": 2219146
                },
                "total": {
                    "confirmed": 333,
                    "deceased": 3,
                    "recovered": 223
                }
            },
            "Patna": {
                "total": {
                    "confirmed": 941,
                    "deceased": 11,
                    "recovered": 443
                }
            },
            "Purnia": {
                "meta": {
                    "population": 3264619,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/dmpurnea/status/1279101539139936257?s=20"
                    }
                },
                "total": {
                    "confirmed": 310,
                    "recovered": 277,
                    "tested": 6938
                }
            },
            "Rohtas": {
                "total": {
                    "confirmed": 363,
                    "deceased": 5,
                    "recovered": 320
                }
            },
            "Saharsa": {
                "meta": {
                    "population": 1900661
                },
                "total": {
                    "confirmed": 203,
                    "recovered": 158
                }
            },
            "Samastipur": {
                "total": {
                    "confirmed": 366,
                    "deceased": 3,
                    "recovered": 277
                }
            },
            "Saran": {
                "meta": {
                    "population": 3951862
                },
                "total": {
                    "confirmed": 238,
                    "deceased": 5,
                    "recovered": 188
                }
            },
            "Sheikhpura": {
                "total": {
                    "confirmed": 166,
                    "recovered": 128
                }
            },
            "Sheohar": {
                "meta": {
                    "population": 656246
                },
                "total": {
                    "confirmed": 96,
                    "deceased": 1,
                    "recovered": 78
                }
            },
            "Sitamarhi": {
                "total": {
                    "confirmed": 149,
                    "deceased": 3,
                    "recovered": 126
                }
            },
            "Siwan": {
                "meta": {
                    "population": 3330464
                },
                "total": {
                    "confirmed": 472,
                    "deceased": 2,
                    "recovered": 391
                }
            },
            "Supaul": {
                "total": {
                    "confirmed": 272,
                    "recovered": 233
                }
            },
            "Unknown": {
                "total": {
                    "confirmed": 3
                }
            },
            "Vaishali": {
                "meta": {
                    "population": 3495021
                },
                "total": {
                    "confirmed": 211,
                    "deceased": 3,
                    "recovered": 136
                }
            },
            "West Champaran": {
                "total": {
                    "confirmed": 243,
                    "deceased": 2,
                    "recovered": 162
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T23:16:27+05:30",
            "population": 119520000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/PIB_Patna/status/1279032483967692801"
            }
        },
        "total": {
            "confirmed": 11111,
            "deceased": 84,
            "recovered": 8211,
            "tested": 243167
        }
    },
    "CH": {
        "districts": {
            "Chandigarh": {
                "meta": {
                    "population": 1055450,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DDnewschd/status/1279041940923678722?s=20"
                    }
                },
                "total": {
                    "confirmed": 454,
                    "deceased": 6,
                    "recovered": 393,
                    "tested": 8074
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-02T20:06:50+05:30",
            "population": 1179000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://t.me/Covid19india_Auxiliary_Test_Data/867"
            }
        },
        "total": {
            "confirmed": 454,
            "deceased": 6,
            "recovered": 393,
            "tested": 8074
        }
    },
    "CT": {
        "districts": {
            "Balod": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 52,
                    "recovered": 45,
                    "tested": 2749
                }
            },
            "Baloda Bazar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 248,
                    "recovered": 225,
                    "tested": 3816
                }
            },
            "Balrampur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 145,
                    "recovered": 115,
                    "tested": 2276
                }
            },
            "Bametara": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 62,
                    "recovered": 48,
                    "tested": 3113
                }
            },
            "Bastar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-23",
                        "source": "http://cghealth.nic.in/cghealth17/Information/content/CORONA/MediaBulletinHindi_23052020.pdf"
                    }
                },
                "total": {
                    "confirmed": 21,
                    "deceased": 1,
                    "recovered": 7,
                    "tested": 4522
                }
            },
            "Bijapur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 2,
                    "recovered": 1,
                    "tested": 1239
                }
            },
            "Bilaspur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 200,
                    "deceased": 2,
                    "recovered": 175,
                    "tested": 9823
                }
            },
            "Dakshin Bastar Dantewada": {
                "meta": {
                    "population": 533638,
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 23,
                    "recovered": 4,
                    "tested": 1168
                }
            },
            "Dhamtari": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 8,
                    "deceased": 1,
                    "recovered": 7,
                    "tested": 1501
                }
            },
            "Durg": {
                "meta": {
                    "population": 3343872,
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 167,
                    "deceased": 3,
                    "recovered": 117,
                    "tested": 5020
                }
            },
            "Gariaband": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 41,
                    "recovered": 27,
                    "tested": 2096
                }
            },
            "Gaurela Pendra Marwahi": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 3,
                    "recovered": 3,
                    "tested": 273
                }
            },
            "Janjgir Champa": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 239,
                    "deceased": 1,
                    "recovered": 217,
                    "tested": 4016
                }
            },
            "Jashpur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 189,
                    "recovered": 110,
                    "tested": 2542
                }
            },
            "Kabeerdham": {
                "meta": {
                    "population": 822526,
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 110,
                    "recovered": 94,
                    "tested": 2829
                }
            },
            "Kondagaon": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 3,
                    "recovered": 3,
                    "tested": 1607
                }
            },
            "Korba": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 308,
                    "recovered": 290,
                    "tested": 10034
                }
            },
            "Koriya": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 59,
                    "recovered": 54,
                    "tested": 2689
                }
            },
            "Mahasamund": {
                "meta": {
                    "population": 1032754,
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 88,
                    "deceased": 1,
                    "recovered": 81,
                    "tested": 2183
                }
            },
            "Mungeli": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 123,
                    "recovered": 121,
                    "tested": 2922
                }
            },
            "Narayanpur": {
                "meta": {
                    "population": 139820,
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 15,
                    "recovered": 10,
                    "tested": 804
                }
            },
            "Other State": {
                "total": {
                    "confirmed": 1,
                    "recovered": 1
                }
            },
            "Raigarh": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 129,
                    "deceased": 1,
                    "recovered": 102,
                    "tested": 5084
                }
            },
            "Raipur": {
                "meta": {
                    "population": 4063872,
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 380,
                    "deceased": 2,
                    "recovered": 211,
                    "tested": 12704
                }
            },
            "Rajnandgaon": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 298,
                    "deceased": 2,
                    "recovered": 222,
                    "tested": 5571
                }
            },
            "Sukma": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 5,
                    "recovered": 3,
                    "tested": 1723
                }
            },
            "Surajpur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 24,
                    "recovered": 21,
                    "tested": 1830
                }
            },
            "Surguja": {
                "meta": {
                    "population": 2359886,
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 56,
                    "recovered": 49,
                    "tested": 2008
                }
            },
            "Uttar Bastar Kanker": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-14",
                        "source": "https://twitter.com/TS_SinghDeo/status/1272218591396368385/photo/1"
                    }
                },
                "total": {
                    "confirmed": 66,
                    "recovered": 51,
                    "tested": 2051
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-02T22:21:33+05:30",
            "population": 28724000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/HealthCgGov/status/1279062111981727750?s=20"
            }
        },
        "total": {
            "confirmed": 3065,
            "deceased": 14,
            "recovered": 2414,
            "tested": 177554
        }
    },
    "DL": {
        "districts": {
            "Central Delhi": {
                "total": {
                    "confirmed": 184
                }
            },
            "East Delhi": {
                "total": {
                    "confirmed": 38
                }
            },
            "New Delhi": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-08",
                        "source": "https://t.me/indiacovid/6717?single"
                    }
                },
                "total": {
                    "confirmed": 37,
                    "tested": 31455
                }
            },
            "North Delhi": {
                "total": {
                    "confirmed": 60
                }
            },
            "North East Delhi": {
                "total": {
                    "confirmed": 25
                }
            },
            "North West Delhi": {
                "total": {
                    "confirmed": 32,
                    "deceased": 1
                }
            },
            "Shahdara": {
                "total": {
                    "confirmed": 48
                }
            },
            "South Delhi": {
                "total": {
                    "confirmed": 70
                }
            },
            "South East Delhi": {
                "total": {
                    "confirmed": 130
                }
            },
            "South West Delhi": {
                "total": {
                    "confirmed": 42
                }
            },
            "Unknown": {
                "total": {
                    "confirmed": 93907,
                    "deceased": 2922,
                    "recovered": 65624
                }
            },
            "West Delhi": {
                "total": {
                    "confirmed": 122
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T21:49:28+05:30",
            "notes": "Delhi bulletins in the morning, containing data of the previous day. We will add that data to the date on which the report is released, rather than the previous day.\n[June 16]: 344 deceased cases have been retroactively added to DL bulletin.",
            "population": 19814000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://t.me/Covid19india_Auxiliary_Test_Data/879"
            }
        },
        "total": {
            "confirmed": 94695,
            "deceased": 2923,
            "recovered": 65624,
            "tested": 596695
        }
    },
    "DN": {
        "delta": {
            "confirmed": 23,
            "recovered": 9
        },
        "districts": {
            "Dadra and Nagar Haveli": {
                "total": {
                    "confirmed": 159,
                    "migrated": 1,
                    "recovered": 68
                }
            },
            "Daman": {
                "delta": {
                    "confirmed": 23,
                    "recovered": 9
                },
                "meta": {
                    "population": 191173
                },
                "total": {
                    "confirmed": 153,
                    "recovered": 63
                }
            },
            "Diu": {
                "total": {
                    "confirmed": 15,
                    "recovered": 11
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-04T15:09:28+05:30",
            "population": 959000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/DnhPublicity/status/1279118072901599232?s=20"
            }
        },
        "total": {
            "confirmed": 327,
            "migrated": 1,
            "recovered": 142,
            "tested": 33618
        }
    },
    "GA": {
        "districts": {
            "North Goa": {
                "meta": {
                    "population": 818008
                },
                "total": {
                    "confirmed": 127,
                    "deceased": 2,
                    "recovered": 38
                }
            },
            "Other State": {
                "total": {
                    "confirmed": 125,
                    "recovered": 9
                }
            },
            "South Goa": {
                "total": {
                    "confirmed": 827,
                    "deceased": 2,
                    "recovered": 260
                }
            },
            "Unknown": {
                "total": {
                    "confirmed": 497,
                    "recovered": 465
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T20:38:37+05:30",
            "population": 1540000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://www.goa.gov.in/wp-content/uploads/2020/07/Status-Of-COVID-19-In-Goa-Dated-03-07-2020.pdf"
            }
        },
        "total": {
            "confirmed": 1576,
            "deceased": 4,
            "recovered": 772,
            "tested": 72691
        }
    },
    "GJ": {
        "districts": {
            "Ahmedabad": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 21543,
                    "deceased": 1466,
                    "recovered": 16385,
                    "tested": 141299
                }
            },
            "Amreli": {
                "meta": {
                    "population": 1514190,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 95,
                    "deceased": 8,
                    "recovered": 42,
                    "tested": 5622
                }
            },
            "Anand": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 241,
                    "deceased": 13,
                    "recovered": 202,
                    "tested": 5754
                }
            },
            "Aravalli": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 217,
                    "deceased": 19,
                    "recovered": 172,
                    "tested": 4125
                }
            },
            "Banaskantha": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 210,
                    "deceased": 12,
                    "recovered": 155,
                    "tested": 9064
                }
            },
            "Bharuch": {
                "meta": {
                    "population": 1551019,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 266,
                    "deceased": 10,
                    "recovered": 131,
                    "tested": 4684
                }
            },
            "Bhavnagar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 302,
                    "deceased": 13,
                    "recovered": 152,
                    "tested": 10569
                }
            },
            "Botad": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 97,
                    "deceased": 3,
                    "recovered": 65,
                    "tested": 3250
                }
            },
            "Chhota Udaipur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 60,
                    "deceased": 2,
                    "recovered": 43,
                    "tested": 6006
                }
            },
            "Dahod": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 65,
                    "deceased": 1,
                    "recovered": 47,
                    "tested": 6620
                }
            },
            "Dang": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 4,
                    "recovered": 4,
                    "tested": 1449
                }
            },
            "Devbhumi Dwarka": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 25,
                    "deceased": 2,
                    "recovered": 16,
                    "tested": 4038
                }
            },
            "Gandhinagar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 693,
                    "deceased": 29,
                    "recovered": 518,
                    "tested": 8673
                }
            },
            "Gir Somnath": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 81,
                    "deceased": 1,
                    "recovered": 49,
                    "tested": 4633
                }
            },
            "Jamnagar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 258,
                    "deceased": 4,
                    "recovered": 118,
                    "tested": 9540
                }
            },
            "Junagadh": {
                "meta": {
                    "population": 2743082,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 147,
                    "deceased": 3,
                    "recovered": 57,
                    "tested": 15106
                }
            },
            "Kheda": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 186,
                    "deceased": 11,
                    "recovered": 119,
                    "tested": 6290
                }
            },
            "Kutch": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 175,
                    "deceased": 5,
                    "recovered": 96,
                    "tested": 7543
                }
            },
            "Mahisagar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 147,
                    "deceased": 2,
                    "recovered": 118,
                    "tested": 5170
                }
            },
            "Mehsana": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 300,
                    "deceased": 13,
                    "recovered": 156,
                    "tested": 4883
                }
            },
            "Morbi": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 31,
                    "deceased": 1,
                    "recovered": 17,
                    "tested": 4208
                }
            },
            "Narmada": {
                "meta": {
                    "population": 590297,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 94,
                    "recovered": 59,
                    "tested": 3808
                }
            },
            "Navsari": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 131,
                    "deceased": 1,
                    "recovered": 61,
                    "tested": 5102
                }
            },
            "Other State": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-27",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/700?single"
                    }
                },
                "total": {
                    "confirmed": 86,
                    "deceased": 1,
                    "recovered": 8,
                    "tested": 108
                }
            },
            "Panchmahal": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 200,
                    "deceased": 15,
                    "recovered": 145,
                    "tested": 6624
                }
            },
            "Patan": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 229,
                    "deceased": 16,
                    "recovered": 119,
                    "tested": 5017
                }
            },
            "Porbandar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 21,
                    "deceased": 2,
                    "recovered": 13,
                    "tested": 3205
                }
            },
            "Rajkot": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 320,
                    "deceased": 9,
                    "recovered": 128,
                    "tested": 9803
                }
            },
            "Sabarkantha": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 187,
                    "deceased": 8,
                    "recovered": 117,
                    "tested": 5988
                }
            },
            "Surat": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 5461,
                    "deceased": 172,
                    "recovered": 3706,
                    "tested": 49790
                }
            },
            "Surendranagar": {
                "meta": {
                    "population": 1756268,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 180,
                    "deceased": 10,
                    "recovered": 84,
                    "tested": 7006
                }
            },
            "Tapi": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 12,
                    "recovered": 8,
                    "tested": 3999
                }
            },
            "Vadodara": {
                "meta": {
                    "population": 4165626,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 2443,
                    "deceased": 49,
                    "recovered": 1768,
                    "tested": 20981
                }
            },
            "Valsad": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/881?single"
                    }
                },
                "total": {
                    "confirmed": 179,
                    "deceased": 4,
                    "recovered": 63,
                    "tested": 5916
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T20:38:27+05:30",
            "population": 67936000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/DDNewsGujarati/status/1279075625592975360?s=20"
            }
        },
        "total": {
            "confirmed": 34686,
            "deceased": 1905,
            "recovered": 24941,
            "tested": 395873
        }
    },
    "HP": {
        "delta": {
            "recovered": 6
        },
        "districts": {
            "Bilaspur": {
                "total": {
                    "confirmed": 47,
                    "recovered": 28
                }
            },
            "Chamba": {
                "total": {
                    "confirmed": 54,
                    "migrated": 1,
                    "recovered": 46
                }
            },
            "Hamirpur": {
                "total": {
                    "confirmed": 256,
                    "deceased": 2,
                    "recovered": 175
                }
            },
            "Kangra": {
                "meta": {
                    "notes": "Death of Tibetan refugee on March 22 included in Kangra district's tally"
                },
                "total": {
                    "confirmed": 282,
                    "deceased": 3,
                    "recovered": 185
                }
            },
            "Kinnaur": {
                "meta": {
                    "population": 84121
                },
                "total": {
                    "confirmed": 34,
                    "recovered": 3
                }
            },
            "Kullu": {
                "total": {
                    "confirmed": 5,
                    "recovered": 5
                }
            },
            "Lahaul and Spiti": {
                "total": {
                    "confirmed": 4
                }
            },
            "Mandi": {
                "total": {
                    "confirmed": 34,
                    "deceased": 2,
                    "recovered": 22
                }
            },
            "Shimla": {
                "delta": {
                    "recovered": 5
                },
                "meta": {
                    "population": 814010
                },
                "total": {
                    "confirmed": 47,
                    "deceased": 2,
                    "migrated": 1,
                    "recovered": 32
                }
            },
            "Sirmaur": {
                "delta": {
                    "recovered": 1
                },
                "total": {
                    "confirmed": 40,
                    "migrated": 7,
                    "recovered": 26
                }
            },
            "Solan": {
                "meta": {
                    "population": 580320
                },
                "total": {
                    "confirmed": 111,
                    "migrated": 4,
                    "recovered": 61
                }
            },
            "Una": {
                "total": {
                    "confirmed": 119,
                    "recovered": 94
                }
            },
            "Unknown": {
                "total": {
                    "migrated": -3
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-04T13:56:28+05:30",
            "notes": "HP has 14 Migrated cases which are reduced from Active #. Also, death of Tibetan refugee is included in deceased numbers, but not in confirmed",
            "population": 7300000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/nhm_hp/status/1279090572263698438?s=20"
            }
        },
        "total": {
            "confirmed": 1033,
            "deceased": 9,
            "migrated": 13,
            "recovered": 677,
            "tested": 85116
        }
    },
    "HR": {
        "districts": {
            "Ambala": {
                "total": {
                    "confirmed": 348,
                    "deceased": 3,
                    "recovered": 311
                }
            },
            "Bhiwani": {
                "meta": {
                    "population": 1634445
                },
                "total": {
                    "confirmed": 441,
                    "deceased": 3,
                    "recovered": 185
                }
            },
            "Charkhi Dadri": {
                "total": {
                    "confirmed": 87,
                    "deceased": 1,
                    "recovered": 45
                }
            },
            "Faridabad": {
                "meta": {
                    "population": 1809733,
                    "tested": {
                        "last_updated": "2020-06-19",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/551"
                    }
                },
                "total": {
                    "confirmed": 4184,
                    "deceased": 87,
                    "recovered": 3174,
                    "tested": 19110
                }
            },
            "Fatehabad": {
                "total": {
                    "confirmed": 122,
                    "recovered": 94
                }
            },
            "Foreign Evacuees": {
                "total": {
                    "confirmed": 21,
                    "recovered": 21
                }
            },
            "Gurugram": {
                "meta": {
                    "population": 902112,
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://cdn.s3waas.gov.in/s325b2822c2f5a3230abfadd476e8b04c9/uploads/2020/07/2020070393.pdf"
                    }
                },
                "total": {
                    "confirmed": 5699,
                    "deceased": 96,
                    "recovered": 4426,
                    "tested": 36419
                }
            },
            "Hisar": {
                "total": {
                    "confirmed": 253,
                    "deceased": 7,
                    "recovered": 188
                }
            },
            "Italians": {
                "total": {
                    "confirmed": 14,
                    "recovered": 14
                }
            },
            "Jhajjar": {
                "total": {
                    "confirmed": 313,
                    "deceased": 4,
                    "recovered": 209
                }
            },
            "Jind": {
                "meta": {
                    "population": 1334152
                },
                "total": {
                    "confirmed": 114,
                    "deceased": 4,
                    "recovered": 88
                }
            },
            "Kaithal": {
                "total": {
                    "confirmed": 110,
                    "recovered": 54
                }
            },
            "Karnal": {
                "meta": {
                    "population": 1505324
                },
                "total": {
                    "confirmed": 367,
                    "deceased": 8,
                    "recovered": 244
                }
            },
            "Kurukshetra": {
                "total": {
                    "confirmed": 137,
                    "recovered": 107
                }
            },
            "Mahendragarh": {
                "meta": {
                    "population": 922088
                },
                "total": {
                    "confirmed": 285,
                    "deceased": 1,
                    "recovered": 191
                }
            },
            "Nuh": {
                "total": {
                    "confirmed": 227,
                    "recovered": 171
                }
            },
            "Palwal": {
                "total": {
                    "confirmed": 339,
                    "deceased": 3,
                    "recovered": 252
                }
            },
            "Panchkula": {
                "meta": {
                    "population": 561293
                },
                "total": {
                    "confirmed": 120,
                    "recovered": 92
                }
            },
            "Panipat": {
                "total": {
                    "confirmed": 220,
                    "deceased": 7,
                    "recovered": 133
                }
            },
            "Rewari": {
                "meta": {
                    "population": 900332
                },
                "total": {
                    "confirmed": 352,
                    "deceased": 5,
                    "recovered": 114
                }
            },
            "Rohtak": {
                "total": {
                    "confirmed": 641,
                    "deceased": 8,
                    "recovered": 533
                }
            },
            "Sirsa": {
                "meta": {
                    "population": 1295189
                },
                "total": {
                    "confirmed": 119,
                    "recovered": 90
                }
            },
            "Sonipat": {
                "total": {
                    "confirmed": 1385,
                    "deceased": 18,
                    "recovered": 860
                }
            },
            "Yamunanagar": {
                "meta": {
                    "population": 1214205
                },
                "total": {
                    "confirmed": 105,
                    "recovered": 95
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T20:38:29+05:30",
            "population": 28672000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "http://www.nhmharyana.gov.in/WriteReadData/userfiles/file/CoronaVirus/Daily%20Bulletin%20of%20COVID%2019%20as%20on%2003-07-20%20Evening.pdf"
            }
        },
        "total": {
            "confirmed": 16003,
            "deceased": 255,
            "recovered": 11691,
            "tested": 288478
        }
    },
    "JH": {
        "districts": {
            "Bokaro": {
                "total": {
                    "confirmed": 48,
                    "deceased": 2,
                    "recovered": 34
                }
            },
            "Chatra": {
                "meta": {
                    "population": 1042886
                },
                "total": {
                    "confirmed": 54,
                    "recovered": 45
                }
            },
            "Deoghar": {
                "total": {
                    "confirmed": 47,
                    "recovered": 35
                }
            },
            "Dhanbad": {
                "meta": {
                    "population": 2684487
                },
                "total": {
                    "confirmed": 179,
                    "recovered": 111
                }
            },
            "Dumka": {
                "total": {
                    "confirmed": 13,
                    "recovered": 7
                }
            },
            "East Singhbhum": {
                "total": {
                    "confirmed": 466,
                    "recovered": 232
                }
            },
            "Garhwa": {
                "total": {
                    "confirmed": 111,
                    "recovered": 97
                }
            },
            "Giridih": {
                "meta": {
                    "population": 2445474
                },
                "total": {
                    "confirmed": 102,
                    "deceased": 2,
                    "recovered": 80
                }
            },
            "Godda": {
                "total": {
                    "confirmed": 11,
                    "recovered": 8
                }
            },
            "Gumla": {
                "meta": {
                    "population": 1025213
                },
                "total": {
                    "confirmed": 126,
                    "deceased": 1,
                    "recovered": 81
                }
            },
            "Hazaribagh": {
                "total": {
                    "confirmed": 202,
                    "deceased": 3,
                    "recovered": 168
                }
            },
            "Jamtara": {
                "meta": {
                    "population": 791042
                },
                "total": {
                    "confirmed": 28,
                    "recovered": 28
                }
            },
            "Khunti": {
                "total": {
                    "confirmed": 31,
                    "recovered": 27
                }
            },
            "Koderma": {
                "total": {
                    "confirmed": 188,
                    "deceased": 1,
                    "recovered": 151
                }
            },
            "Latehar": {
                "total": {
                    "confirmed": 57,
                    "recovered": 53
                }
            },
            "Lohardaga": {
                "meta": {
                    "population": 461790
                },
                "total": {
                    "confirmed": 59,
                    "recovered": 45
                }
            },
            "Pakur": {
                "total": {
                    "confirmed": 33,
                    "recovered": 30
                }
            },
            "Palamu": {
                "meta": {
                    "population": 1939869
                },
                "total": {
                    "confirmed": 61,
                    "recovered": 53
                }
            },
            "Ramgarh": {
                "total": {
                    "confirmed": 122,
                    "recovered": 115
                }
            },
            "Ranchi": {
                "meta": {
                    "population": 2914253
                },
                "total": {
                    "confirmed": 254,
                    "deceased": 4,
                    "recovered": 167
                }
            },
            "Sahibganj": {
                "total": {
                    "confirmed": 16,
                    "deceased": 1,
                    "recovered": 3
                }
            },
            "Saraikela-Kharsawan": {
                "meta": {
                    "population": 1065056
                },
                "total": {
                    "confirmed": 78,
                    "recovered": 35
                }
            },
            "Simdega": {
                "total": {
                    "confirmed": 353,
                    "deceased": 1,
                    "recovered": 348
                }
            },
            "West Singhbhum": {
                "total": {
                    "confirmed": 58,
                    "recovered": 48
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T22:47:30+05:30",
            "population": 37403000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/FOBGumla/status/1279090376842686465?s=20"
            }
        },
        "total": {
            "confirmed": 2697,
            "deceased": 15,
            "recovered": 2001,
            "tested": 151699
        }
    },
    "JK": {
        "districts": {
            "Anantnag": {
                "total": {
                    "confirmed": 713,
                    "deceased": 9,
                    "recovered": 554
                }
            },
            "Bandipora": {
                "total": {
                    "confirmed": 298,
                    "deceased": 1,
                    "recovered": 265
                }
            },
            "Baramulla": {
                "total": {
                    "confirmed": 949,
                    "deceased": 19,
                    "recovered": 412
                }
            },
            "Budgam": {
                "total": {
                    "confirmed": 439,
                    "deceased": 9,
                    "recovered": 237
                }
            },
            "Doda": {
                "total": {
                    "confirmed": 89,
                    "deceased": 2,
                    "recovered": 60
                }
            },
            "Ganderbal": {
                "meta": {
                    "population": 297446
                },
                "total": {
                    "confirmed": 118,
                    "recovered": 62
                }
            },
            "Jammu": {
                "total": {
                    "confirmed": 376,
                    "deceased": 8,
                    "recovered": 295
                }
            },
            "Kathua": {
                "meta": {
                    "population": 616435
                },
                "total": {
                    "confirmed": 242,
                    "deceased": 1,
                    "recovered": 177
                }
            },
            "Kishtwar": {
                "total": {
                    "confirmed": 29,
                    "recovered": 21
                }
            },
            "Kulgam": {
                "meta": {
                    "population": 424483
                },
                "total": {
                    "confirmed": 851,
                    "deceased": 16,
                    "recovered": 598
                }
            },
            "Kupwara": {
                "total": {
                    "confirmed": 577,
                    "deceased": 6,
                    "recovered": 418
                }
            },
            "Pulwama": {
                "meta": {
                    "population": 560440
                },
                "total": {
                    "confirmed": 518,
                    "deceased": 4,
                    "recovered": 257
                }
            },
            "Punch": {
                "total": {
                    "confirmed": 123,
                    "deceased": 1,
                    "recovered": 111
                }
            },
            "Rajouri": {
                "meta": {
                    "population": 642415
                },
                "total": {
                    "confirmed": 118,
                    "deceased": 1,
                    "recovered": 65
                }
            },
            "Ramban": {
                "total": {
                    "confirmed": 226,
                    "recovered": 187
                }
            },
            "Reasi": {
                "meta": {
                    "population": 314667
                },
                "total": {
                    "confirmed": 45,
                    "recovered": 31
                }
            },
            "Samba": {
                "total": {
                    "confirmed": 158,
                    "recovered": 114
                }
            },
            "Shopiyan": {
                "total": {
                    "confirmed": 802,
                    "deceased": 13,
                    "recovered": 611
                }
            },
            "Srinagar": {
                "total": {
                    "confirmed": 1062,
                    "deceased": 28,
                    "recovered": 407
                }
            },
            "Udhampur": {
                "meta": {
                    "population": 554985
                },
                "total": {
                    "confirmed": 286,
                    "deceased": 1,
                    "recovered": 193
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T20:18:29+05:30",
            "population": 13203000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/diprjk/status/1279058022296252417?s=20"
            }
        },
        "total": {
            "confirmed": 8019,
            "deceased": 119,
            "recovered": 5075,
            "tested": 385501
        }
    },
    "KA": {
        "districts": {
            "Bagalkote": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 226,
                    "deceased": 5,
                    "recovered": 123,
                    "tested": 10663
                }
            },
            "Ballari": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/868"
                    }
                },
                "total": {
                    "confirmed": 1081,
                    "deceased": 34,
                    "recovered": 495,
                    "tested": 17526
                }
            },
            "Belagavi": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/883"
                    }
                },
                "total": {
                    "confirmed": 356,
                    "deceased": 4,
                    "recovered": 303,
                    "tested": 26337
                }
            },
            "Bengaluru Rural": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/c/1238093174/6713"
                    }
                },
                "total": {
                    "confirmed": 207,
                    "deceased": 5,
                    "recovered": 46,
                    "tested": 5173
                }
            },
            "Bengaluru Urban": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/887"
                    }
                },
                "total": {
                    "confirmed": 7173,
                    "deceased": 105,
                    "migrated": 1,
                    "recovered": 771,
                    "tested": 120557
                }
            },
            "Bidar": {
                "meta": {
                    "population": 1703300,
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 675,
                    "deceased": 22,
                    "recovered": 500,
                    "tested": 35599
                }
            },
            "Chamarajanagara": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 78,
                    "recovered": 1,
                    "tested": 5156
                }
            },
            "Chikkaballapura": {
                "meta": {
                    "population": 1255104,
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 233,
                    "deceased": 5,
                    "migrated": 1,
                    "recovered": 167,
                    "tested": 15089
                }
            },
            "Chikkamagaluru": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 82,
                    "deceased": 1,
                    "recovered": 43,
                    "tested": 5467
                }
            },
            "Chitradurga": {
                "meta": {
                    "population": 1659456,
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 80,
                    "recovered": 43,
                    "tested": 4393
                }
            },
            "Dakshina Kannada": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/885"
                    }
                },
                "total": {
                    "confirmed": 1012,
                    "deceased": 16,
                    "migrated": 2,
                    "recovered": 487,
                    "tested": 14710
                }
            },
            "Davanagere": {
                "meta": {
                    "population": 1945497,
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 338,
                    "deceased": 9,
                    "recovered": 285,
                    "tested": 17483
                }
            },
            "Dharwad": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/886"
                    }
                },
                "total": {
                    "confirmed": 465,
                    "deceased": 8,
                    "recovered": 201,
                    "tested": 26739
                }
            },
            "Gadag": {
                "meta": {
                    "population": 1064570,
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 199,
                    "deceased": 4,
                    "recovered": 81,
                    "tested": 8904
                }
            },
            "Hassan": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 453,
                    "deceased": 6,
                    "recovered": 253,
                    "tested": 10800
                }
            },
            "Haveri": {
                "meta": {
                    "population": 1597668,
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 124,
                    "deceased": 2,
                    "recovered": 35,
                    "tested": 11714
                }
            },
            "Kalaburagi": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/888"
                    }
                },
                "total": {
                    "confirmed": 1560,
                    "deceased": 22,
                    "recovered": 1143,
                    "tested": 66955
                }
            },
            "Kodagu": {
                "meta": {
                    "population": 554519,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/889"
                    }
                },
                "total": {
                    "confirmed": 76,
                    "recovered": 3,
                    "tested": 9078
                }
            },
            "Kolar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 150,
                    "deceased": 2,
                    "recovered": 62,
                    "tested": 9797
                }
            },
            "Koppal": {
                "meta": {
                    "population": 1389920,
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 105,
                    "deceased": 2,
                    "recovered": 67,
                    "tested": 8708
                }
            },
            "Mandya": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 473,
                    "recovered": 354,
                    "tested": 14874
                }
            },
            "Mysuru": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/848"
                    }
                },
                "total": {
                    "confirmed": 371,
                    "deceased": 4,
                    "recovered": 217,
                    "tested": 21331
                }
            },
            "Other State": {
                "total": {
                    "confirmed": 36,
                    "deceased": 3,
                    "recovered": 32
                }
            },
            "Raichur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 518,
                    "deceased": 3,
                    "recovered": 404,
                    "tested": 21011
                }
            },
            "Ramanagara": {
                "meta": {
                    "population": 1082636,
                    "tested": {
                        "last_updated": "2020-06-29",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 225,
                    "deceased": 5,
                    "recovered": 76,
                    "tested": 8997
                }
            },
            "Shivamogga": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 222,
                    "deceased": 4,
                    "recovered": 117,
                    "tested": 12739
                }
            },
            "Tumakuru": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-01",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/832"
                    }
                },
                "total": {
                    "confirmed": 196,
                    "deceased": 6,
                    "recovered": 49,
                    "tested": 18461
                }
            },
            "Udupi": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/884"
                    }
                },
                "total": {
                    "confirmed": 1258,
                    "deceased": 3,
                    "recovered": 1093,
                    "tested": 16498
                }
            },
            "Uttara Kannada": {
                "meta": {
                    "population": 1437169,
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 298,
                    "deceased": 1,
                    "recovered": 151,
                    "tested": 13833
                }
            },
            "Vijayapura": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 470,
                    "deceased": 11,
                    "recovered": 350,
                    "tested": 25108
                }
            },
            "Yadgir": {
                "meta": {
                    "population": 1174271,
                    "tested": {
                        "last_updated": "2020-06-28",
                        "source": "https://covid19.karnataka.gov.in/storage/pdf-files/COVID%20Report%2027062020_0500PM_English.pdf"
                    }
                },
                "total": {
                    "confirmed": 970,
                    "deceased": 1,
                    "recovered": 855,
                    "tested": 22590
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T20:38:31+05:30",
            "notes": "4 cases are classified as non-covid related deaths in KA bulletin. They have been reduced from active cases",
            "population": 65798000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/DHFWKA/status/1279062744201703426?s=20"
            }
        },
        "total": {
            "confirmed": 19710,
            "deceased": 293,
            "migrated": 4,
            "recovered": 8807,
            "tested": 671934
        }
    },
    "KL": {
        "districts": {
            "Alappuzha": {
                "meta": {
                    "population": 2127789
                },
                "total": {
                    "confirmed": 345,
                    "deceased": 1,
                    "recovered": 145
                }
            },
            "Ernakulam": {
                "total": {
                    "confirmed": 291,
                    "deceased": 1,
                    "migrated": 1,
                    "recovered": 113
                }
            },
            "Idukki": {
                "total": {
                    "confirmed": 119,
                    "recovered": 72
                }
            },
            "Kannur": {
                "total": {
                    "confirmed": 529,
                    "deceased": 5,
                    "recovered": 308
                }
            },
            "Kasaragod": {
                "meta": {
                    "population": 1307375
                },
                "total": {
                    "confirmed": 474,
                    "recovered": 384
                }
            },
            "Kollam": {
                "total": {
                    "confirmed": 379,
                    "deceased": 2,
                    "recovered": 160
                }
            },
            "Kottayam": {
                "meta": {
                    "population": 1974551
                },
                "total": {
                    "confirmed": 248,
                    "deceased": 1,
                    "recovered": 134
                }
            },
            "Kozhikode": {
                "total": {
                    "confirmed": 289,
                    "deceased": 2,
                    "recovered": 196
                }
            },
            "Malappuram": {
                "meta": {
                    "population": 4112920
                },
                "total": {
                    "confirmed": 594,
                    "deceased": 4,
                    "recovered": 346
                }
            },
            "Palakkad": {
                "total": {
                    "confirmed": 578,
                    "deceased": 1,
                    "migrated": 1,
                    "recovered": 378
                }
            },
            "Pathanamthitta": {
                "meta": {
                    "population": 1197412
                },
                "total": {
                    "confirmed": 329,
                    "recovered": 137
                }
            },
            "Thiruvananthapuram": {
                "total": {
                    "confirmed": 241,
                    "deceased": 5,
                    "recovered": 146
                }
            },
            "Thrissur": {
                "meta": {
                    "population": 3121200
                },
                "total": {
                    "confirmed": 449,
                    "deceased": 3,
                    "recovered": 256
                }
            },
            "Wayanad": {
                "total": {
                    "confirmed": 100,
                    "deceased": 1,
                    "recovered": 64
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T18:56:30+05:30",
            "notes": "Mahe native who expired in Kannur included in Kerala's tally.\nOne patient who absconded from Palakkad to TN and one patient who returned back to Maharashtra has been reduced from active count",
            "population": 35125000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://dhs.kerala.gov.in/wp-content/uploads/2020/07/Bulletin-HFWD-English-July-3.pdf"
            }
        },
        "total": {
            "confirmed": 4965,
            "deceased": 26,
            "migrated": 2,
            "recovered": 2839,
            "tested": 253011
        }
    },
    "LA": {
        "districts": {
            "Kargil": {
                "meta": {
                    "population": 140802,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://www.facebook.com/114874993303412/photos/pcb.194577081999869/194577055333205/?type=3&theater"
                    }
                },
                "total": {
                    "confirmed": 714,
                    "recovered": 583,
                    "tested": 6700
                }
            },
            "Leh": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://www.facebook.com/114874993303412/photos/pcb.194577081999869/194577055333205/?type=3&theater"
                    }
                },
                "total": {
                    "confirmed": 288,
                    "deceased": 1,
                    "recovered": 193,
                    "tested": 7661
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T17:52:29+05:30",
            "population": 293000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://www.facebook.com/114874993303412/photos/pcb.194577081999869/194577055333205/?type=3&__tn__=HH-R&eid=ARDSIgt7gA4DAQiH782EI015hrzP1BJnHtm_tAjZnxGsUUhHV86Qe_2sdPsp1015TqBiyE2JvSeP4RhQ&__xts__%5B0%5D=68.ARBqqZ3Nowj-wzencx9B9KKnvJ6ATzrIT6Wd3oZKPQ1FZKwUgS0HF-hmwXel-OZY7nesZvZc1ep39WubcTobYTmaC2wT9NM4rpJy-IWX1lXETRNpcXn4jbfVEbjMdV7mXlFQuKpn6lJUafqcmqT5rQtsBxqN0eYwNq9ZKideLPkNvhfhkSLKZH-9OXUUHv_OERg1R8RenJYccps6ebrLBhKtk1nrgUw-zttNNKj6cmHeYrSezRCbk2yD3rBwtuePxOtlHwZEEAKldrTg_YVr4I-ToH__Ks_MwC0vUJA79JNIN6pgI-8xToanx5JODiI8GXnudKQcTm4pxW-eZglmTDI"
            }
        },
        "total": {
            "confirmed": 1002,
            "deceased": 1,
            "recovered": 776,
            "tested": 14361
        }
    },
    "LD": {
        "meta": {
            "last_updated": "2020-03-26T07:19:29+05:30"
        }
    },
    "MH": {
        "delta": {
            "tested": 32517
        },
        "districts": {
            "Ahmednagar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HANR_20200704_1_3&width=71px"
                    }
                },
                "total": {
                    "confirmed": 506,
                    "deceased": 15,
                    "recovered": 340,
                    "tested": 4900
                }
            },
            "Akola": {
                "meta": {
                    "population": 1813906
                },
                "total": {
                    "confirmed": 1599,
                    "deceased": 83,
                    "migrated": 1,
                    "recovered": 1106
                }
            },
            "Amravati": {
                "total": {
                    "confirmed": 625,
                    "deceased": 30,
                    "recovered": 434
                }
            },
            "Aurangabad": {
                "meta": {
                    "population": 3701282,
                    "tested": {
                        "last_updated": "2020-05-30",
                        "source": "https://www.facebook.com/Aurangabad/photos/a.234441904720/10158414823344721/?type=3&theater"
                    }
                },
                "total": {
                    "confirmed": 6061,
                    "deceased": 277,
                    "recovered": 2614,
                    "tested": 11800
                }
            },
            "Beed": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HBED_20200704_1_3&width=71px"
                    }
                },
                "total": {
                    "confirmed": 126,
                    "deceased": 3,
                    "recovered": 95,
                    "tested": 3223
                }
            },
            "Bhandara": {
                "meta": {
                    "population": 1200334,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HBHN_20200704_1_3&width=74px"
                    }
                },
                "total": {
                    "confirmed": 87,
                    "recovered": 77,
                    "tested": 4348
                }
            },
            "Buldhana": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HBUL_20200704_1_3&width=70px"
                    }
                },
                "total": {
                    "confirmed": 277,
                    "deceased": 13,
                    "recovered": 160,
                    "tested": 3062
                }
            },
            "Chandrapur": {
                "meta": {
                    "population": 2204307,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HCPR_20200704_1_3&width=71px"
                    }
                },
                "total": {
                    "confirmed": 97,
                    "recovered": 61,
                    "tested": 4718
                }
            },
            "Dhule": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HDHL_20200704_1_3&width=72px"
                    }
                },
                "total": {
                    "confirmed": 1182,
                    "deceased": 58,
                    "migrated": 2,
                    "recovered": 680,
                    "tested": 9813
                }
            },
            "Gadchiroli": {
                "meta": {
                    "population": 1072942,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HGAD_20200704_1_3&width=71px"
                    }
                },
                "total": {
                    "confirmed": 71,
                    "deceased": 1,
                    "recovered": 58,
                    "tested": 7324
                }
            },
            "Gondia": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HGND_20200704_1_3&width=72px"
                    }
                },
                "total": {
                    "confirmed": 155,
                    "deceased": 2,
                    "recovered": 104,
                    "tested": 3636
                }
            },
            "Hingoli": {
                "meta": {
                    "population": 1177345,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HHNG_20200704_1_3&width=71px"
                    }
                },
                "total": {
                    "confirmed": 270,
                    "deceased": 1,
                    "recovered": 250,
                    "tested": 4447
                }
            },
            "Jalgaon": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-22",
                        "source": "https://twitter.com/InfoJalgaon/status/1275087825013219330"
                    }
                },
                "total": {
                    "confirmed": 3856,
                    "deceased": 261,
                    "recovered": 2194,
                    "tested": 14369
                }
            },
            "Jalna": {
                "meta": {
                    "population": 1959046,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HJAN_20200704_1_3&width=73px"
                    }
                },
                "total": {
                    "confirmed": 619,
                    "deceased": 24,
                    "recovered": 363,
                    "tested": 5467
                }
            },
            "Kolhapur": {
                "total": {
                    "confirmed": 886,
                    "deceased": 12,
                    "recovered": 724
                }
            },
            "Latur": {
                "meta": {
                    "population": 2454196
                },
                "total": {
                    "confirmed": 396,
                    "deceased": 20,
                    "recovered": 204
                }
            },
            "Mumbai": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/mybmc/status/1279067244845166594?s=20"
                    }
                },
                "total": {
                    "confirmed": 82074,
                    "deceased": 4762,
                    "migrated": 8,
                    "recovered": 52392,
                    "tested": 344968
                }
            },
            "Nagpur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-24",
                        "source": "https://twitter.com/InfoNagpur/status/1275712879304548353/photo/1"
                    }
                },
                "total": {
                    "confirmed": 1624,
                    "deceased": 15,
                    "recovered": 1241,
                    "tested": 22863
                }
            },
            "Nanded": {
                "meta": {
                    "population": 3361292,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HNGG_20200704_1_5&width=76px"
                    }
                },
                "total": {
                    "confirmed": 371,
                    "deceased": 14,
                    "recovered": 241,
                    "tested": 25305
                }
            },
            "Nandurbar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HNDB_20200704_1_3&width=72px"
                    }
                },
                "total": {
                    "confirmed": 179,
                    "deceased": 9,
                    "recovered": 79,
                    "tested": 2032
                }
            },
            "Nashik": {
                "meta": {
                    "population": 6107187,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/InfoNashik/status/1279038659061145601?s=20"
                    }
                },
                "total": {
                    "confirmed": 4656,
                    "deceased": 223,
                    "recovered": 2616,
                    "tested": 23266
                }
            },
            "Osmanabad": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HOBD_20200704_1_3&width=72px"
                    }
                },
                "total": {
                    "confirmed": 241,
                    "deceased": 12,
                    "recovered": 180,
                    "tested": 3201
                }
            },
            "Other State": {
                "total": {
                    "confirmed": 106,
                    "deceased": 25
                }
            },
            "Palghar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HTHA_20200704_2_10&width=72px"
                    }
                },
                "total": {
                    "confirmed": 6837,
                    "deceased": 117,
                    "recovered": 2866,
                    "tested": 38445
                }
            },
            "Parbhani": {
                "meta": {
                    "population": 1836086,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HPBN_20200704_1_3&width=70px"
                    }
                },
                "total": {
                    "confirmed": 110,
                    "deceased": 4,
                    "recovered": 83,
                    "tested": 2677
                }
            },
            "Pune": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/Info_Pune/status/1279107746688667648?s=20"
                    }
                },
                "total": {
                    "confirmed": 25454,
                    "deceased": 826,
                    "recovered": 12218,
                    "tested": 155631
                }
            },
            "Raigad": {
                "meta": {
                    "population": 2634200,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HRGD_20200704_1_11&width=72px"
                    }
                },
                "total": {
                    "confirmed": 5238,
                    "deceased": 106,
                    "migrated": 2,
                    "recovered": 2536,
                    "tested": 4812
                }
            },
            "Ratnagiri": {
                "total": {
                    "confirmed": 677,
                    "deceased": 27,
                    "recovered": 449
                }
            },
            "Sangli": {
                "meta": {
                    "population": 2822143
                },
                "total": {
                    "confirmed": 376,
                    "deceased": 11,
                    "recovered": 239
                }
            },
            "Satara": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HSTH_20200704_1_11&width=72px"
                    }
                },
                "total": {
                    "confirmed": 1222,
                    "deceased": 48,
                    "migrated": 1,
                    "recovered": 757,
                    "tested": 13972
                }
            },
            "Sindhudurg": {
                "meta": {
                    "population": 849651
                },
                "total": {
                    "confirmed": 234,
                    "deceased": 5,
                    "recovered": 155
                }
            },
            "Solapur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HSOL_20200704_1_3&width=72px"
                    }
                },
                "total": {
                    "confirmed": 2695,
                    "deceased": 283,
                    "migrated": 1,
                    "recovered": 1631,
                    "tested": 17158
                }
            },
            "Thane": {
                "meta": {
                    "population": 11060148,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HTHA_20200704_1_8&width=73px"
                    }
                },
                "total": {
                    "confirmed": 43634,
                    "deceased": 1075,
                    "migrated": 1,
                    "recovered": 17227,
                    "tested": 120002
                }
            },
            "Wardha": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HWAD_20200704_1_4&width=70px"
                    }
                },
                "total": {
                    "confirmed": 16,
                    "deceased": 1,
                    "recovered": 12,
                    "tested": 4587
                }
            },
            "Washim": {
                "meta": {
                    "population": 1197160
                },
                "total": {
                    "confirmed": 115,
                    "deceased": 3,
                    "recovered": 80
                }
            },
            "Yavatmal": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "http://epaper.lokmat.com/articlepage.php?articleid=LOK_HYTL_20200704_1_3&width=72px"
                    }
                },
                "total": {
                    "confirmed": 318,
                    "deceased": 10,
                    "recovered": 221,
                    "tested": 5137
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T22:43:26+05:30",
            "notes": "16 cases were marked as non-covid deaths in MH bulletin. These have been reduced from deceased and active counts\n[June 16] : 1328 deceased cases have been retroactively added to MH bulletin.\n[June 20]: 69 deceased cases have been reduced based on state bulletin.",
            "population": 122153000,
            "tested": {
                "last_updated": "2020-07-04",
                "source": "https://t.co/AOKLdHSxQe?amp=1"
            }
        },
        "total": {
            "confirmed": 192990,
            "deceased": 8376,
            "migrated": 16,
            "recovered": 104687,
            "tested": 1085160
        }
    },
    "ML": {
        "delta": {
            "confirmed": 4
        },
        "districts": {
            "East Jaintia Hills": {
                "total": {
                    "confirmed": 1
                }
            },
            "East Khasi Hills": {
                "meta": {
                    "population": 825922
                },
                "total": {
                    "confirmed": 33,
                    "deceased": 1,
                    "recovered": 17
                }
            },
            "North Garo Hills": {
                "total": {
                    "confirmed": 1,
                    "recovered": 1
                }
            },
            "Ribhoi": {
                "delta": {
                    "confirmed": 4
                },
                "meta": {
                    "population": 258840
                },
                "total": {
                    "confirmed": 8
                }
            },
            "South West Garo Hills": {
                "total": {
                    "confirmed": 7,
                    "recovered": 4
                }
            },
            "Unknown": {
                "total": {
                    "confirmed": 3,
                    "recovered": 12
                }
            },
            "West Garo Hills": {
                "meta": {
                    "population": 643291
                },
                "total": {
                    "confirmed": 7,
                    "recovered": 4
                }
            },
            "West Jaintia Hills": {
                "total": {
                    "confirmed": 5,
                    "recovered": 5
                }
            },
            "West Khasi Hills": {
                "meta": {
                    "population": 383461
                },
                "total": {
                    "confirmed": 1
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-04T10:36:29+05:30",
            "notes": "[June 17]:\nOne case was identified to be false positive and has been removed from the confirmed cases by ML authorities.",
            "population": 3224000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://t.me/Covid19india_Auxiliary_Test_Data/877"
            }
        },
        "total": {
            "confirmed": 66,
            "deceased": 1,
            "recovered": 43,
            "tested": 19940
        }
    },
    "MN": {
        "districts": {
            "Bishnupur": {
                "meta": {
                    "population": 237399
                },
                "total": {
                    "confirmed": 80,
                    "recovered": 58
                }
            },
            "Chandel": {
                "total": {
                    "confirmed": 38,
                    "recovered": 6
                }
            },
            "Churachandpur": {
                "meta": {
                    "population": 274143
                },
                "total": {
                    "confirmed": 139,
                    "recovered": 58
                }
            },
            "Imphal East": {
                "total": {
                    "confirmed": 39,
                    "recovered": 16
                }
            },
            "Imphal West": {
                "meta": {
                    "population": 517992
                },
                "total": {
                    "confirmed": 91,
                    "recovered": 82
                }
            },
            "Jiribam": {
                "total": {
                    "confirmed": 32,
                    "recovered": 2
                }
            },
            "Kakching": {
                "total": {
                    "confirmed": 89,
                    "recovered": 44
                }
            },
            "Kamjong": {
                "total": {
                    "confirmed": 89,
                    "recovered": 17
                }
            },
            "Kangpokpi": {
                "total": {
                    "confirmed": 137,
                    "recovered": 19
                }
            },
            "Noney": {
                "total": {
                    "confirmed": 24,
                    "recovered": 18
                }
            },
            "Pherzawl": {
                "total": {
                    "confirmed": 32,
                    "recovered": 15
                }
            },
            "Senapati": {
                "total": {
                    "confirmed": 114,
                    "recovered": 21
                }
            },
            "Tamenglong": {
                "total": {
                    "confirmed": 178,
                    "recovered": 32
                }
            },
            "Tengnoupal": {
                "total": {
                    "confirmed": 14,
                    "recovered": 13
                }
            },
            "Thoubal": {
                "meta": {
                    "population": 422168
                },
                "total": {
                    "confirmed": 59,
                    "recovered": 23
                }
            },
            "Ukhrul": {
                "total": {
                    "confirmed": 161,
                    "recovered": 26
                }
            },
            "Unknown": {
                "total": {
                    "recovered": 189
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T20:48:30+05:30",
            "population": 3103000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/DiprManipur/status/1279060651025920002?s=20"
            }
        },
        "total": {
            "confirmed": 1316,
            "recovered": 639,
            "tested": 53608
        }
    },
    "MP": {
        "districts": {
            "Agar Malwa": {
                "total": {
                    "confirmed": 16,
                    "deceased": 1,
                    "recovered": 14
                }
            },
            "Alirajpur": {
                "total": {
                    "confirmed": 4,
                    "recovered": 3
                }
            },
            "Anuppur": {
                "meta": {
                    "population": 749237,
                    "tested": {
                        "last_updated": "2020-06-28"
                    }
                },
                "total": {
                    "confirmed": 29,
                    "recovered": 29,
                    "tested": 991
                }
            },
            "Ashoknagar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-33-bhopal-edition-bhopal-page-11.html"
                    }
                },
                "total": {
                    "confirmed": 48,
                    "deceased": 1,
                    "recovered": 42,
                    "tested": 2215
                }
            },
            "Balaghat": {
                "meta": {
                    "population": 1701698,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-59-jabalpur-edition-jabalpur-page-6.html"
                    }
                },
                "total": {
                    "confirmed": 33,
                    "recovered": 20,
                    "tested": 1461
                }
            },
            "Barwani": {
                "total": {
                    "confirmed": 119,
                    "deceased": 4,
                    "recovered": 100
                }
            },
            "Betul": {
                "meta": {
                    "population": 1575362,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-33-bhopal-edition-bhopal-page-11.html"
                    }
                },
                "total": {
                    "confirmed": 69,
                    "recovered": 47,
                    "tested": 2895
                }
            },
            "Bhind": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-52-gwalior-edition-gwalior-page-7.html"
                    }
                },
                "total": {
                    "confirmed": 265,
                    "recovered": 169,
                    "tested": 5330
                }
            },
            "Bhopal": {
                "meta": {
                    "population": 2371061,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-74-indore-edition-indore-page-9.html"
                    }
                },
                "total": {
                    "confirmed": 2933,
                    "deceased": 105,
                    "recovered": 2366,
                    "tested": 96083
                }
            },
            "Burhanpur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-74-indore-edition-indore-page-9.html"
                    }
                },
                "total": {
                    "confirmed": 402,
                    "deceased": 23,
                    "recovered": 367,
                    "tested": 6688
                }
            },
            "Chhatarpur": {
                "meta": {
                    "population": 1762375,
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://epaper.naidunia.com/mepaper/03-jul-2020-54-bundelkhand-edition-bundelkhand-page-5.html"
                    }
                },
                "total": {
                    "confirmed": 59,
                    "recovered": 54,
                    "tested": 2228
                }
            },
            "Chhindwara": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-33-bhopal-edition-bhopal-page-11.html"
                    }
                },
                "total": {
                    "confirmed": 65,
                    "deceased": 2,
                    "recovered": 33,
                    "tested": 3146
                }
            },
            "Damoh": {
                "meta": {
                    "population": 1264219,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-59-jabalpur-edition-jabalpur-page-6.html"
                    }
                },
                "total": {
                    "confirmed": 46,
                    "recovered": 30,
                    "tested": 152
                }
            },
            "Datia": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-52-gwalior-edition-gwalior-page-7.html"
                    }
                },
                "total": {
                    "confirmed": 43,
                    "deceased": 1,
                    "recovered": 20,
                    "tested": 399
                }
            },
            "Dewas": {
                "meta": {
                    "population": 1563715,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/PROJSDewas/status/1279034059046318080?s=19"
                    }
                },
                "total": {
                    "confirmed": 226,
                    "deceased": 10,
                    "recovered": 190,
                    "tested": 7903
                }
            },
            "Dhar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-23",
                        "source": "https://epaper.naidunia.com/mepaper/24-jun-2020-11-dhar-edition-dhar-page-9.html"
                    }
                },
                "total": {
                    "confirmed": 179,
                    "deceased": 6,
                    "recovered": 154,
                    "tested": 3070
                }
            },
            "Dindori": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-59-jabalpur-edition-jabalpur-page-6.html"
                    }
                },
                "total": {
                    "confirmed": 31,
                    "recovered": 30,
                    "tested": 2929
                }
            },
            "Guna": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-33-bhopal-edition-bhopal-page-11.html"
                    }
                },
                "total": {
                    "confirmed": 19,
                    "deceased": 1,
                    "recovered": 10,
                    "tested": 2494
                }
            },
            "Gwalior": {
                "meta": {
                    "population": 2032036,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-74-indore-edition-indore-page-9.html"
                    }
                },
                "total": {
                    "confirmed": 436,
                    "deceased": 3,
                    "recovered": 290,
                    "tested": 32687
                }
            },
            "Harda": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-33-bhopal-edition-bhopal-page-11.html"
                    }
                },
                "total": {
                    "confirmed": 39,
                    "deceased": 2,
                    "recovered": 25,
                    "tested": 888
                }
            },
            "Hoshangabad": {
                "meta": {
                    "population": 1241350,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-33-bhopal-edition-bhopal-page-11.html"
                    }
                },
                "total": {
                    "confirmed": 41,
                    "deceased": 3,
                    "recovered": 38,
                    "tested": 781
                }
            },
            "Indore": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/tarun28988/status/1279111223506636800?s=20"
                    }
                },
                "total": {
                    "confirmed": 4776,
                    "deceased": 238,
                    "recovered": 3664,
                    "tested": 90188
                }
            },
            "Jabalpur": {
                "meta": {
                    "population": 2463289,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/jabalpurdm/status/1279072399338565633?s=20"
                    }
                },
                "total": {
                    "confirmed": 423,
                    "deceased": 14,
                    "recovered": 336,
                    "tested": 14367
                }
            },
            "Jhabua": {
                "total": {
                    "confirmed": 17,
                    "deceased": 1,
                    "recovered": 14
                }
            },
            "Katni": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-59-jabalpur-edition-jabalpur-page-6.html"
                    }
                },
                "total": {
                    "confirmed": 19,
                    "deceased": 2,
                    "recovered": 12,
                    "tested": 814
                }
            },
            "Khandwa": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-74-indore-edition-indore-page-9.html"
                    }
                },
                "total": {
                    "confirmed": 322,
                    "deceased": 17,
                    "recovered": 265,
                    "tested": 6593
                }
            },
            "Khargone": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-74-indore-edition-indore-page-9.html"
                    }
                },
                "total": {
                    "confirmed": 300,
                    "deceased": 15,
                    "recovered": 261,
                    "tested": 4197
                }
            },
            "Mandla": {
                "total": {
                    "confirmed": 6,
                    "deceased": 1,
                    "recovered": 4
                }
            },
            "Mandsaur": {
                "meta": {
                    "population": 1340411,
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://epaper.naidunia.com/mepaper/21-jun-2020-10-mandsaur-edition-mandsaur-page-11.html"
                    }
                },
                "total": {
                    "confirmed": 129,
                    "deceased": 9,
                    "recovered": 92,
                    "tested": 2967
                }
            },
            "Morena": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-74-indore-edition-indore-page-9.html"
                    }
                },
                "total": {
                    "confirmed": 540,
                    "deceased": 5,
                    "recovered": 194,
                    "tested": 6669
                }
            },
            "Narsinghpur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-59-jabalpur-edition-jabalpur-page-6.html"
                    }
                },
                "total": {
                    "confirmed": 32,
                    "recovered": 27,
                    "tested": 2700
                }
            },
            "Neemuch": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-74-indore-edition-indore-page-9.html"
                    }
                },
                "total": {
                    "confirmed": 448,
                    "deceased": 7,
                    "recovered": 424,
                    "tested": 5865
                }
            },
            "Niwari": {
                "total": {
                    "confirmed": 10,
                    "recovered": 7
                }
            },
            "Panna": {
                "meta": {
                    "population": 1016520
                },
                "total": {
                    "confirmed": 37,
                    "recovered": 29
                }
            },
            "Raisen": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-33-bhopal-edition-bhopal-page-11.html"
                    }
                },
                "total": {
                    "confirmed": 112,
                    "deceased": 5,
                    "recovered": 95,
                    "tested": 2088
                }
            },
            "Rajgarh": {
                "meta": {
                    "population": 1545814,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-33-bhopal-edition-bhopal-page-11.html"
                    }
                },
                "total": {
                    "confirmed": 98,
                    "deceased": 6,
                    "recovered": 57,
                    "tested": 2393
                }
            },
            "Ratlam": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-74-indore-edition-indore-page-9.html"
                    }
                },
                "total": {
                    "confirmed": 170,
                    "deceased": 6,
                    "recovered": 138,
                    "tested": 4316
                }
            },
            "Rewa": {
                "meta": {
                    "population": 2365106
                },
                "total": {
                    "confirmed": 61,
                    "deceased": 1,
                    "recovered": 42
                }
            },
            "Sagar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-33-bhopal-edition-bhopal-page-11.html"
                    }
                },
                "total": {
                    "confirmed": 396,
                    "deceased": 21,
                    "recovered": 286,
                    "tested": 10776
                }
            },
            "Satna": {
                "meta": {
                    "population": 2228935,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-59-jabalpur-edition-jabalpur-page-6.html"
                    }
                },
                "total": {
                    "confirmed": 40,
                    "deceased": 2,
                    "recovered": 21,
                    "tested": 2419
                }
            },
            "Sehore": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-33-bhopal-edition-bhopal-page-11.html"
                    }
                },
                "total": {
                    "confirmed": 21,
                    "deceased": 2,
                    "recovered": 10,
                    "tested": 1357
                }
            },
            "Seoni": {
                "meta": {
                    "population": 1379131,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-59-jabalpur-edition-jabalpur-page-6.html"
                    }
                },
                "total": {
                    "confirmed": 15,
                    "recovered": 11,
                    "tested": 1088
                }
            },
            "Shahdol": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-59-jabalpur-edition-jabalpur-page-6.html"
                    }
                },
                "total": {
                    "confirmed": 24,
                    "recovered": 16,
                    "tested": 1098
                }
            },
            "Shajapur": {
                "meta": {
                    "population": 1512681,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/PROJSShajapur/status/1279063929210073089?s=20"
                    }
                },
                "total": {
                    "confirmed": 65,
                    "deceased": 3,
                    "recovered": 50,
                    "tested": 3380
                }
            },
            "Sheopur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-52-gwalior-edition-gwalior-page-7.html"
                    }
                },
                "total": {
                    "confirmed": 81,
                    "deceased": 2,
                    "recovered": 62,
                    "tested": 2070
                }
            },
            "Shivpuri": {
                "meta": {
                    "population": 1726050,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-52-gwalior-edition-gwalior-page-7.html"
                    }
                },
                "total": {
                    "confirmed": 38,
                    "recovered": 28,
                    "tested": 3642
                }
            },
            "Sidhi": {
                "total": {
                    "confirmed": 21,
                    "deceased": 1,
                    "recovered": 17
                }
            },
            "Singrauli": {
                "meta": {
                    "population": 1178273
                },
                "total": {
                    "confirmed": 19,
                    "recovered": 13
                }
            },
            "Tikamgarh": {
                "total": {
                    "confirmed": 48,
                    "deceased": 1,
                    "recovered": 20
                }
            },
            "Ujjain": {
                "meta": {
                    "population": 1986864,
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://epaper.naidunia.com/mepaper/03-jul-2020-74-indore-edition-indore-page-7.html"
                    }
                },
                "total": {
                    "confirmed": 863,
                    "deceased": 71,
                    "recovered": 772,
                    "tested": 21835
                }
            },
            "Umaria": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-59-jabalpur-edition-jabalpur-page-6.html"
                    }
                },
                "total": {
                    "confirmed": 11,
                    "deceased": 1,
                    "recovered": 9,
                    "tested": 1418
                }
            },
            "Vidisha": {
                "meta": {
                    "population": 1458875,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://epaper.naidunia.com/mepaper/04-jul-2020-33-bhopal-edition-bhopal-page-11.html"
                    }
                },
                "total": {
                    "confirmed": 53,
                    "recovered": 42,
                    "tested": 2470
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T19:25:27+05:30",
            "population": 82232000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/healthminmp/status/1279045394119315456?s=20"
            }
        },
        "total": {
            "confirmed": 14297,
            "deceased": 593,
            "recovered": 11049,
            "tested": 389180
        }
    },
    "MZ": {
        "districts": {
            "Aizawl": {
                "total": {
                    "confirmed": 39,
                    "recovered": 32
                }
            },
            "Champhai": {
                "meta": {
                    "population": 125745
                },
                "total": {
                    "confirmed": 10,
                    "recovered": 5
                }
            },
            "Khawzawl": {
                "total": {
                    "confirmed": 3,
                    "recovered": 1
                }
            },
            "Kolasib": {
                "total": {
                    "confirmed": 11,
                    "recovered": 11
                }
            },
            "Lawngtlai": {
                "meta": {
                    "population": 117894
                },
                "total": {
                    "confirmed": 8,
                    "recovered": 8
                }
            },
            "Lunglei": {
                "meta": {
                    "population": 161428
                },
                "total": {
                    "confirmed": 47,
                    "recovered": 46
                }
            },
            "Mamit": {
                "total": {
                    "confirmed": 20,
                    "recovered": 10
                }
            },
            "Saiha": {
                "meta": {
                    "population": 56574
                },
                "total": {
                    "confirmed": 18,
                    "recovered": 8
                }
            },
            "Saitual": {
                "total": {
                    "confirmed": 3,
                    "recovered": 3
                }
            },
            "Serchhip": {
                "meta": {
                    "population": 64937
                },
                "total": {
                    "confirmed": 3,
                    "recovered": 3
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T17:15:30+05:30",
            "population": 1192000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://dipr.mizoram.gov.in/post/status-of-state-surveillance-of-covid-19-time-272020-500pm-372020-500-pm"
            }
        },
        "total": {
            "confirmed": 162,
            "recovered": 127,
            "tested": 14370
        }
    },
    "NL": {
        "delta": {
            "confirmed": 23
        },
        "districts": {
            "Dimapur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-27",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/184"
                    }
                },
                "total": {
                    "confirmed": 87,
                    "recovered": 29,
                    "tested": 896
                }
            },
            "Kiphire": {
                "meta": {
                    "population": 74004,
                    "tested": {
                        "last_updated": "2020-05-27",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/184"
                    }
                },
                "total": {
                    "confirmed": 4,
                    "tested": 18
                }
            },
            "Kohima": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-27",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/184"
                    }
                },
                "total": {
                    "confirmed": 49,
                    "recovered": 14,
                    "tested": 485
                }
            },
            "Longleng": {
                "meta": {
                    "population": 50484
                },
                "total": {
                    "confirmed": 2
                }
            },
            "Mokokchung": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-27",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/184"
                    }
                },
                "total": {
                    "confirmed": 1,
                    "tested": 63
                }
            },
            "Mon": {
                "meta": {
                    "population": 250260,
                    "tested": {
                        "last_updated": "2020-05-27",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/184"
                    }
                },
                "total": {
                    "confirmed": 66,
                    "tested": 45
                }
            },
            "Others": {
                "total": {
                    "confirmed": 46
                }
            },
            "Peren": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-27",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/184"
                    }
                },
                "total": {
                    "confirmed": 229,
                    "recovered": 16,
                    "tested": 11
                }
            },
            "Phek": {
                "meta": {
                    "population": 163418,
                    "tested": {
                        "last_updated": "2020-05-27",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/184"
                    }
                },
                "total": {
                    "confirmed": 10,
                    "recovered": 1,
                    "tested": 28
                }
            },
            "Tuensang": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-27",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/184"
                    }
                },
                "total": {
                    "confirmed": 30,
                    "tested": 1
                }
            },
            "Unknown": {
                "delta": {
                    "confirmed": 23
                },
                "total": {
                    "confirmed": 23,
                    "recovered": 168
                }
            },
            "Wokha": {
                "meta": {
                    "population": 166343,
                    "tested": {
                        "last_updated": "2020-05-27",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/184"
                    }
                },
                "total": {
                    "confirmed": 10,
                    "tested": 7
                }
            },
            "Zunheboto": {
                "total": {
                    "confirmed": 5
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-04T09:54:27+05:30",
            "population": 2150000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/MyGovNagaland/status/1279047412707819521?s=20"
            }
        },
        "total": {
            "confirmed": 562,
            "recovered": 228,
            "tested": 18635
        }
    },
    "OR": {
        "delta": {
            "confirmed": 495,
            "deceased": 6
        },
        "districts": {
            "Angul": {
                "delta": {
                    "confirmed": 24
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 95,
                    "deceased": 1,
                    "recovered": 57,
                    "tested": 2830
                }
            },
            "Balangir": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 213,
                    "recovered": 153,
                    "tested": 2237
                }
            },
            "Balasore": {
                "delta": {
                    "confirmed": 13
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 390,
                    "deceased": 1,
                    "recovered": 309,
                    "tested": 9843
                }
            },
            "Bargarh": {
                "delta": {
                    "confirmed": 2
                },
                "total": {
                    "confirmed": 133,
                    "deceased": 1,
                    "recovered": 64
                }
            },
            "Bhadrak": {
                "delta": {
                    "confirmed": 12
                },
                "meta": {
                    "population": 1506337,
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 245,
                    "recovered": 224,
                    "tested": 5539
                }
            },
            "Boudh": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 45,
                    "recovered": 40,
                    "tested": 496
                }
            },
            "Cuttack": {
                "delta": {
                    "confirmed": 13,
                    "deceased": 1
                },
                "meta": {
                    "population": 2624470,
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 715,
                    "deceased": 6,
                    "recovered": 509,
                    "tested": 5720
                }
            },
            "Deogarh": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 62,
                    "recovered": 42,
                    "tested": 682
                }
            },
            "Dhenkanal": {
                "delta": {
                    "confirmed": 1
                },
                "meta": {
                    "population": 1192811,
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 84,
                    "recovered": 66,
                    "tested": 1545
                }
            },
            "Gajapati": {
                "delta": {
                    "confirmed": 7
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 449,
                    "recovered": 231,
                    "tested": 715
                }
            },
            "Ganjam": {
                "delta": {
                    "confirmed": 216,
                    "deceased": 3
                },
                "meta": {
                    "population": 3529031,
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 2066,
                    "deceased": 21,
                    "recovered": 1128,
                    "tested": 6632
                }
            },
            "Jagatsinghpur": {
                "delta": {
                    "confirmed": 12
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 317,
                    "recovered": 227,
                    "tested": 2138
                }
            },
            "Jajpur": {
                "delta": {
                    "confirmed": 1
                },
                "meta": {
                    "population": 1827192,
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 541,
                    "recovered": 391,
                    "tested": 10621
                }
            },
            "Jharsuguda": {
                "delta": {
                    "confirmed": 8
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 128,
                    "recovered": 49,
                    "tested": 1663
                }
            },
            "Kalahandi": {
                "meta": {
                    "population": 1576869,
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 76,
                    "recovered": 70,
                    "tested": 1458
                }
            },
            "Kandhamal": {
                "delta": {
                    "confirmed": 8
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 186,
                    "recovered": 178,
                    "tested": 1516
                }
            },
            "Kendrapara": {
                "delta": {
                    "confirmed": 11
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 264,
                    "recovered": 226,
                    "tested": 2637
                }
            },
            "Kendujhar": {
                "delta": {
                    "confirmed": 5
                },
                "total": {
                    "confirmed": 157,
                    "recovered": 96
                }
            },
            "Khordha": {
                "delta": {
                    "confirmed": 50,
                    "deceased": 2
                },
                "total": {
                    "confirmed": 944,
                    "deceased": 9,
                    "recovered": 703
                }
            },
            "Koraput": {
                "delta": {
                    "confirmed": 5
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 57,
                    "recovered": 25,
                    "tested": 1401
                }
            },
            "Malkangiri": {
                "delta": {
                    "confirmed": 5
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 111,
                    "recovered": 53,
                    "tested": 1841
                }
            },
            "Mayurbhanj": {
                "delta": {
                    "confirmed": 28
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 253,
                    "deceased": 1,
                    "recovered": 160,
                    "tested": 3307
                }
            },
            "Nabarangapur": {
                "delta": {
                    "confirmed": 11
                },
                "total": {
                    "confirmed": 53,
                    "deceased": 1,
                    "recovered": 13
                }
            },
            "Nayagarh": {
                "delta": {
                    "confirmed": 1
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 164,
                    "recovered": 129,
                    "tested": 1104
                }
            },
            "Nuapada": {
                "meta": {
                    "population": 610382,
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 82,
                    "recovered": 78,
                    "tested": 310
                }
            },
            "Others": {
                "meta": {
                    "notes": "Includes NDRF-ODRF returnees after West Bengal Amphan duty"
                }
            },
            "Puri": {
                "delta": {
                    "confirmed": 18
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 291,
                    "deceased": 2,
                    "recovered": 215,
                    "tested": 2577
                }
            },
            "Rayagada": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 115,
                    "recovered": 22,
                    "tested": 578
                }
            },
            "Sambalpur": {
                "delta": {
                    "confirmed": 6
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-05-17",
                        "source": "https://health.odisha.gov.in/covid19-dashboard.html"
                    }
                },
                "total": {
                    "confirmed": 70,
                    "recovered": 36,
                    "tested": 2007
                }
            },
            "Subarnapur": {
                "delta": {
                    "confirmed": 2
                },
                "meta": {
                    "population": 610183
                },
                "total": {
                    "confirmed": 39,
                    "recovered": 35
                }
            },
            "Sundargarh": {
                "delta": {
                    "confirmed": 36
                },
                "total": {
                    "confirmed": 256,
                    "recovered": 176
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-04T12:46:27+05:30",
            "notes": "Three non-covid deaths reported in state dashboard are included in the deceased count\n[June 22nd]: NDRF/ODRF cases have been redistributed to districts based on state dashboard",
            "population": 43671000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://t.me/Covid19india_Auxiliary_Test_Data/876?single"
            }
        },
        "total": {
            "confirmed": 8601,
            "deceased": 43,
            "recovered": 5705,
            "tested": 281523
        }
    },
    "PB": {
        "districts": {
            "Amritsar": {
                "meta": {
                    "population": 2490656,
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 938,
                    "deceased": 47,
                    "recovered": 740,
                    "tested": 21011
                }
            },
            "Barnala": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 64,
                    "deceased": 2,
                    "recovered": 41,
                    "tested": 7616
                }
            },
            "Bathinda": {
                "meta": {
                    "population": 1388525,
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 100,
                    "deceased": 3,
                    "recovered": 76,
                    "tested": 10770
                }
            },
            "Faridkot": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 111,
                    "recovered": 99,
                    "tested": 9015
                }
            },
            "Fatehgarh Sahib": {
                "meta": {
                    "population": 600163,
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 121,
                    "recovered": 101,
                    "tested": 9391
                }
            },
            "Fazilka": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 101,
                    "recovered": 74,
                    "tested": 8883
                }
            },
            "Ferozepur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 102,
                    "deceased": 3,
                    "recovered": 55,
                    "tested": 9206
                }
            },
            "Gurdaspur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 240,
                    "deceased": 5,
                    "recovered": 191,
                    "tested": 13482
                }
            },
            "Hoshiarpur": {
                "meta": {
                    "population": 1586625,
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 185,
                    "deceased": 6,
                    "recovered": 160,
                    "tested": 12276
                }
            },
            "Jalandhar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 774,
                    "deceased": 21,
                    "recovered": 537,
                    "tested": 21896
                }
            },
            "Kapurthala": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 106,
                    "deceased": 5,
                    "recovered": 78,
                    "tested": 9615
                }
            },
            "Ludhiana": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 971,
                    "deceased": 24,
                    "recovered": 570,
                    "tested": 33412
                }
            },
            "Mansa": {
                "meta": {
                    "population": 769751,
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 48,
                    "recovered": 40,
                    "tested": 7743
                }
            },
            "Moga": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 114,
                    "deceased": 2,
                    "recovered": 91,
                    "tested": 14272
                }
            },
            "Pathankot": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 222,
                    "deceased": 6,
                    "recovered": 183,
                    "tested": 6842
                }
            },
            "Patiala": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 351,
                    "deceased": 9,
                    "recovered": 168,
                    "tested": 20275
                }
            },
            "Rupnagar": {
                "meta": {
                    "population": 684627,
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 113,
                    "deceased": 1,
                    "recovered": 95,
                    "tested": 10691
                }
            },
            "S.A.S. Nagar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 281,
                    "deceased": 4,
                    "recovered": 210,
                    "tested": 11155
                }
            },
            "Sangrur": {
                "meta": {
                    "population": 1655169,
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 511,
                    "deceased": 14,
                    "recovered": 328,
                    "tested": 15183
                }
            },
            "Shahid Bhagat Singh Nagar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 147,
                    "deceased": 1,
                    "recovered": 125,
                    "tested": 9407
                }
            },
            "Sri Muktsar Sahib": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 133,
                    "recovered": 123,
                    "tested": 8084
                }
            },
            "Tarn Taran": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-27"
                    }
                },
                "total": {
                    "confirmed": 204,
                    "deceased": 4,
                    "recovered": 181,
                    "tested": 9503
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T19:25:29+05:30",
            "population": 29859000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "http://pbhealth.gov.in/Media%20Bulletin%20COVID-19%2003-07-2020.pdf"
            }
        },
        "total": {
            "confirmed": 5937,
            "deceased": 157,
            "recovered": 4266,
            "tested": 324054
        }
    },
    "PY": {
        "delta": {
            "confirmed": 80,
            "deceased": 1,
            "recovered": 21
        },
        "districts": {
            "Karaikal": {
                "delta": {
                    "confirmed": 2,
                    "recovered": 3
                },
                "meta": {
                    "population": 200222,
                    "tested": {
                        "last_updated": "2020-07-03"
                    }
                },
                "total": {
                    "confirmed": 45,
                    "recovered": 17,
                    "tested": 2700
                }
            },
            "Mahe": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03"
                    }
                },
                "total": {
                    "confirmed": 18,
                    "recovered": 10,
                    "tested": 888
                }
            },
            "Puducherry": {
                "delta": {
                    "confirmed": 76,
                    "deceased": 1,
                    "recovered": 18
                },
                "meta": {
                    "population": 950289,
                    "tested": {
                        "last_updated": "2020-07-03"
                    }
                },
                "total": {
                    "confirmed": 837,
                    "deceased": 14,
                    "recovered": 378,
                    "tested": 14965
                }
            },
            "Yanam": {
                "delta": {
                    "confirmed": 2
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03"
                    }
                },
                "total": {
                    "confirmed": 4,
                    "tested": 1007
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-04T12:00:28+05:30",
            "population": 1504000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://health.py.gov.in/sites/default/files/NEET-PDF/03.07.2020%20bulletin.pdf"
            }
        },
        "total": {
            "confirmed": 904,
            "deceased": 14,
            "recovered": 405,
            "tested": 19560
        }
    },
    "RJ": {
        "delta": {
            "confirmed": 204,
            "deceased": 3,
            "recovered": 71
        },
        "districts": {
            "Ajmer": {
                "meta": {
                    "population": 2583052,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 561,
                    "deceased": 19,
                    "recovered": 452,
                    "tested": 26483
                }
            },
            "Alwar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 602,
                    "deceased": 6,
                    "recovered": 340,
                    "tested": 19512
                }
            },
            "BSF Camp": {
                "total": {
                    "confirmed": 52,
                    "recovered": 50
                }
            },
            "Banswara": {
                "meta": {
                    "population": 1797485,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 99,
                    "deceased": 2,
                    "recovered": 95,
                    "tested": 4744
                }
            },
            "Baran": {
                "meta": {
                    "population": 1222755,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 67,
                    "deceased": 4,
                    "recovered": 59,
                    "tested": 5525
                }
            },
            "Barmer": {
                "delta": {
                    "confirmed": 36
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 428,
                    "deceased": 4,
                    "recovered": 205,
                    "tested": 16181
                }
            },
            "Bharatpur": {
                "delta": {
                    "confirmed": 3,
                    "deceased": 1,
                    "recovered": 12
                },
                "meta": {
                    "population": 2548462,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 1708,
                    "deceased": 39,
                    "recovered": 1463,
                    "tested": 25523
                }
            },
            "Bhilwara": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 264,
                    "deceased": 6,
                    "recovered": 239,
                    "tested": 33992
                }
            },
            "Bikaner": {
                "delta": {
                    "confirmed": 25
                },
                "meta": {
                    "population": 2363937,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 414,
                    "deceased": 16,
                    "recovered": 175,
                    "tested": 31213
                }
            },
            "Bundi": {
                "meta": {
                    "population": 1110906,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 15,
                    "recovered": 11,
                    "tested": 4971
                }
            },
            "Chittorgarh": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 211,
                    "deceased": 6,
                    "recovered": 203,
                    "tested": 11859
                }
            },
            "Churu": {
                "meta": {
                    "population": 2039547,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 331,
                    "deceased": 2,
                    "recovered": 257,
                    "tested": 11918
                }
            },
            "Dausa": {
                "delta": {
                    "confirmed": 3
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 169,
                    "deceased": 3,
                    "recovered": 118,
                    "tested": 11927
                }
            },
            "Dholpur": {
                "delta": {
                    "confirmed": 21
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 722,
                    "deceased": 7,
                    "recovered": 475,
                    "tested": 15122
                }
            },
            "Dungarpur": {
                "delta": {
                    "confirmed": 13,
                    "recovered": 7
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 461,
                    "deceased": 1,
                    "recovered": 418,
                    "tested": 21891
                }
            },
            "Evacuees": {
                "total": {
                    "confirmed": 61,
                    "recovered": 61
                }
            },
            "Ganganagar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 59,
                    "deceased": 3,
                    "recovered": 28,
                    "tested": 6510
                }
            },
            "Hanumangarh": {
                "meta": {
                    "population": 1774692,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 80,
                    "recovered": 47,
                    "tested": 8609
                }
            },
            "Italians": {
                "total": {
                    "confirmed": 2,
                    "recovered": 2
                }
            },
            "Jaipur": {
                "delta": {
                    "confirmed": 17
                },
                "meta": {
                    "population": 6626178,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 3456,
                    "deceased": 163,
                    "recovered": 2779,
                    "tested": 118374
                }
            },
            "Jaisalmer": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 115,
                    "recovered": 105,
                    "tested": 15580
                }
            },
            "Jalore": {
                "delta": {
                    "confirmed": 11
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 320,
                    "deceased": 2,
                    "recovered": 240,
                    "tested": 31549
                }
            },
            "Jhalawar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 375,
                    "recovered": 369,
                    "tested": 24930
                }
            },
            "Jhunjhunu": {
                "delta": {
                    "confirmed": 11,
                    "deceased": 1,
                    "recovered": 8
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 386,
                    "deceased": 3,
                    "recovered": 355,
                    "tested": 16080
                }
            },
            "Jodhpur": {
                "delta": {
                    "recovered": 15
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 2919,
                    "deceased": 53,
                    "recovered": 2457,
                    "tested": 148712
                }
            },
            "Karauli": {
                "delta": {
                    "confirmed": 3
                },
                "meta": {
                    "population": 1458248,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 108,
                    "deceased": 4,
                    "recovered": 77,
                    "tested": 6519
                }
            },
            "Kota": {
                "delta": {
                    "confirmed": 8,
                    "recovered": 5
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 722,
                    "deceased": 23,
                    "recovered": 570,
                    "tested": 58374
                }
            },
            "Nagaur": {
                "delta": {
                    "confirmed": 23
                },
                "meta": {
                    "population": 3307743,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 693,
                    "deceased": 12,
                    "recovered": 590,
                    "tested": 24772
                }
            },
            "Other State": {
                "delta": {
                    "confirmed": 3,
                    "deceased": 1
                },
                "total": {
                    "confirmed": 130,
                    "deceased": 30,
                    "recovered": 41
                }
            },
            "Pali": {
                "delta": {
                    "confirmed": 21
                },
                "meta": {
                    "population": 2037573,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 1167,
                    "deceased": 9,
                    "recovered": 1027,
                    "tested": 34676
                }
            },
            "Pratapgarh": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 74,
                    "deceased": 1,
                    "recovered": 13,
                    "tested": 4179
                }
            },
            "Rajsamand": {
                "delta": {
                    "confirmed": 1
                },
                "meta": {
                    "population": 1156597,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 275,
                    "deceased": 1,
                    "recovered": 210,
                    "tested": 9646
                }
            },
            "Sawai Madhopur": {
                "delta": {
                    "confirmed": 1
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 109,
                    "deceased": 7,
                    "recovered": 78,
                    "tested": 7707
                }
            },
            "Sikar": {
                "meta": {
                    "population": 2677333,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 597,
                    "deceased": 6,
                    "recovered": 496,
                    "tested": 37318
                }
            },
            "Sirohi": {
                "delta": {
                    "recovered": 24
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 546,
                    "deceased": 7,
                    "recovered": 386,
                    "tested": 23405
                }
            },
            "Tonk": {
                "meta": {
                    "population": 1421326,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 202,
                    "deceased": 1,
                    "recovered": 199,
                    "tested": 12617
                }
            },
            "Udaipur": {
                "delta": {
                    "confirmed": 4
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
                    }
                },
                "total": {
                    "confirmed": 756,
                    "deceased": 3,
                    "recovered": 662,
                    "tested": 35316
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-04T10:49:27+05:30",
            "population": 77264000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://t.me/Covid19india_Auxiliary_Test_Data/873"
            }
        },
        "total": {
            "confirmed": 19256,
            "deceased": 443,
            "recovered": 15352,
            "tested": 869602
        }
    },
    "SK": {
        "districts": {
            "East Sikkim": {
                "total": {
                    "confirmed": 41,
                    "recovered": 14
                }
            },
            "North Sikkim": {
                "total": {
                    "confirmed": 1,
                    "recovered": 1
                }
            },
            "South Sikkim": {
                "total": {
                    "confirmed": 38,
                    "recovered": 26
                }
            },
            "Unknown": {
                "total": {
                    "confirmed": 1
                }
            },
            "West Sikkim": {
                "total": {
                    "confirmed": 21,
                    "recovered": 11
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T23:08:32+05:30",
            "population": 664000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://t.me/Covid19india_Auxiliary_Test_Data/878"
            }
        },
        "total": {
            "confirmed": 102,
            "recovered": 52,
            "tested": 11072
        }
    },
    "TG": {
        "districts": {
            "Adilabad": {
                "meta": {
                    "population": 2741239
                },
                "total": {
                    "confirmed": 47,
                    "recovered": 15
                }
            },
            "Bhadradri Kothagudem": {
                "total": {
                    "confirmed": 38,
                    "recovered": 4
                }
            },
            "Foreign Evacuees": {
                "total": {
                    "confirmed": 33
                }
            },
            "Hyderabad": {
                "meta": {
                    "population": 3943323
                },
                "total": {
                    "confirmed": 16078,
                    "deceased": 23,
                    "recovered": 305
                }
            },
            "Jagtial": {
                "total": {
                    "confirmed": 29,
                    "recovered": 2
                }
            },
            "Jangaon": {
                "total": {
                    "confirmed": 81,
                    "recovered": 1
                }
            },
            "Jayashankar Bhupalapally": {
                "total": {
                    "confirmed": 9
                }
            },
            "Jogulamba Gadwal": {
                "total": {
                    "confirmed": 53,
                    "deceased": 1,
                    "recovered": 25
                }
            },
            "Kamareddy": {
                "total": {
                    "confirmed": 51,
                    "recovered": 8
                }
            },
            "Karimnagar": {
                "meta": {
                    "population": 3776269
                },
                "total": {
                    "confirmed": 107,
                    "recovered": 16
                }
            },
            "Khammam": {
                "total": {
                    "confirmed": 65,
                    "recovered": 3
                }
            },
            "Komaram Bheem": {
                "total": {
                    "confirmed": 26,
                    "recovered": 2
                }
            },
            "Mahabubabad": {
                "total": {
                    "confirmed": 26,
                    "recovered": 1
                }
            },
            "Mahabubnagar": {
                "total": {
                    "confirmed": 99,
                    "recovered": 8
                }
            },
            "Mancherial": {
                "total": {
                    "confirmed": 68,
                    "deceased": 1
                }
            },
            "Medak": {
                "meta": {
                    "population": 3033288
                },
                "total": {
                    "confirmed": 62,
                    "recovered": 4
                }
            },
            "Medchal Malkajgiri": {
                "total": {
                    "confirmed": 701,
                    "deceased": 1,
                    "recovered": 9
                }
            },
            "Mulugu": {
                "total": {
                    "confirmed": 23,
                    "recovered": 2
                }
            },
            "Nagarkurnool": {
                "total": {
                    "confirmed": 25,
                    "recovered": 2
                }
            },
            "Nalgonda": {
                "meta": {
                    "population": 3488809
                },
                "total": {
                    "confirmed": 103,
                    "recovered": 12
                }
            },
            "Narayanpet": {
                "total": {
                    "confirmed": 5,
                    "deceased": 1
                }
            },
            "Nirmal": {
                "total": {
                    "confirmed": 36,
                    "recovered": 13
                }
            },
            "Nizamabad": {
                "total": {
                    "confirmed": 97,
                    "recovered": 30
                }
            },
            "Other State": {
                "total": {
                    "confirmed": 250
                }
            },
            "Peddapalli": {
                "total": {
                    "confirmed": 6,
                    "recovered": 1
                }
            },
            "Rajanna Sircilla": {
                "total": {
                    "confirmed": 36,
                    "recovered": 2
                }
            },
            "Ranga Reddy": {
                "total": {
                    "confirmed": 1226,
                    "deceased": 2,
                    "recovered": 17
                }
            },
            "Sangareddy": {
                "total": {
                    "confirmed": 170,
                    "recovered": 6
                }
            },
            "Siddipet": {
                "total": {
                    "confirmed": 29,
                    "recovered": 1
                }
            },
            "Suryapet": {
                "total": {
                    "confirmed": 97,
                    "recovered": 24
                }
            },
            "Unknown": {
                "total": {
                    "confirmed": 456,
                    "deceased": 253,
                    "recovered": 9644
                }
            },
            "Vikarabad": {
                "total": {
                    "confirmed": 49,
                    "deceased": 1,
                    "recovered": 15
                }
            },
            "Wanaparthy": {
                "total": {
                    "confirmed": 11
                }
            },
            "Warangal Rural": {
                "total": {
                    "confirmed": 119
                }
            },
            "Warangal Urban": {
                "total": {
                    "confirmed": 129,
                    "recovered": 23
                }
            },
            "Yadadri Bhuvanagiri": {
                "total": {
                    "confirmed": 22
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T23:25:27+05:30",
            "population": 37220000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/Eatala_Rajender/status/1279105961479729152?s=20"
            }
        },
        "total": {
            "confirmed": 20462,
            "deceased": 283,
            "recovered": 10195,
            "tested": 104118
        }
    },
    "TN": {
        "districts": {
            "Airport Quarantine": {
                "total": {
                    "confirmed": 765,
                    "deceased": 1,
                    "recovered": 317
                }
            },
            "Ariyalur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 463,
                    "recovered": 425,
                    "tested": 5442
                }
            },
            "Chengalpattu": {
                "meta": {
                    "population": 2560000,
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 6139,
                    "deceased": 106,
                    "recovered": 3113,
                    "tested": 20050
                }
            },
            "Chennai": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 64689,
                    "deceased": 993,
                    "recovered": 40111,
                    "tested": 170701
                }
            },
            "Coimbatore": {
                "meta": {
                    "population": 3458045,
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 645,
                    "deceased": 1,
                    "recovered": 252,
                    "tested": 33522
                }
            },
            "Cuddalore": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 1143,
                    "deceased": 5,
                    "recovered": 813,
                    "tested": 14192
                }
            },
            "Dharmapuri": {
                "meta": {
                    "population": 1506843,
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 107,
                    "recovered": 41,
                    "tested": 12251
                }
            },
            "Dindigul": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 618,
                    "deceased": 7,
                    "recovered": 310,
                    "tested": 9963
                }
            },
            "Erode": {
                "meta": {
                    "population": 2251744,
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 206,
                    "deceased": 5,
                    "recovered": 80,
                    "tested": 19203
                }
            },
            "Kallakurichi": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 1102,
                    "deceased": 3,
                    "recovered": 443,
                    "tested": 11460
                }
            },
            "Kancheepuram": {
                "meta": {
                    "population": 3998252,
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 2272,
                    "deceased": 26,
                    "recovered": 925,
                    "tested": 12983
                }
            },
            "Kanyakumari": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 489,
                    "deceased": 1,
                    "recovered": 180,
                    "tested": 28453
                }
            },
            "Karur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 153,
                    "deceased": 2,
                    "recovered": 124,
                    "tested": 9796
                }
            },
            "Krishnagiri": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 170,
                    "deceased": 2,
                    "recovered": 52,
                    "tested": 8290
                }
            },
            "Madurai": {
                "meta": {
                    "population": 3038252,
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 3423,
                    "deceased": 51,
                    "recovered": 967,
                    "tested": 23092
                }
            },
            "Nagapattinam": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 273,
                    "recovered": 106,
                    "tested": 10789
                }
            },
            "Namakkal": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 101,
                    "deceased": 1,
                    "recovered": 90,
                    "tested": 9825
                }
            },
            "Nilgiris": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 119,
                    "recovered": 41,
                    "tested": 9334
                }
            },
            "Other State": {
                "total": {
                    "deceased": 3
                }
            },
            "Perambalur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 164,
                    "recovered": 156,
                    "tested": 4379
                }
            },
            "Pudukkottai": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 252,
                    "deceased": 4,
                    "recovered": 79,
                    "tested": 9393
                }
            },
            "Railway Quarantine": {
                "total": {
                    "confirmed": 413,
                    "recovered": 234
                }
            },
            "Ramanathapuram": {
                "meta": {
                    "population": 1353445,
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 1143,
                    "deceased": 17,
                    "recovered": 318,
                    "tested": 9723
                }
            },
            "Ranipet": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 978,
                    "deceased": 3,
                    "recovered": 535,
                    "tested": 6879
                }
            },
            "Salem": {
                "meta": {
                    "population": 3482056,
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 1127,
                    "deceased": 4,
                    "recovered": 311,
                    "tested": 31019
                }
            },
            "Sivaganga": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 376,
                    "deceased": 4,
                    "recovered": 118,
                    "tested": 7156
                }
            },
            "Tenkasi": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 391,
                    "deceased": 1,
                    "recovered": 207,
                    "tested": 11804
                }
            },
            "Thanjavur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 478,
                    "deceased": 2,
                    "recovered": 293,
                    "tested": 24097
                }
            },
            "Theni": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 927,
                    "deceased": 5,
                    "recovered": 234,
                    "tested": 23138
                }
            },
            "Thiruvallur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 4343,
                    "deceased": 82,
                    "recovered": 2793,
                    "tested": 13981
                }
            },
            "Thiruvarur": {
                "meta": {
                    "population": 1264277,
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 513,
                    "recovered": 283,
                    "tested": 11313
                }
            },
            "Thoothukkudi": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 1055,
                    "deceased": 4,
                    "recovered": 758,
                    "tested": 19085
                }
            },
            "Tiruchirappalli": {
                "meta": {
                    "population": 2722290,
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 803,
                    "deceased": 4,
                    "recovered": 456,
                    "tested": 19347
                }
            },
            "Tirunelveli": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 921,
                    "deceased": 8,
                    "recovered": 619,
                    "tested": 26438
                }
            },
            "Tirupathur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 216,
                    "recovered": 80,
                    "tested": 12453
                }
            },
            "Tiruppur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 197,
                    "recovered": 124,
                    "tested": 12536
                }
            },
            "Tiruvannamalai": {
                "meta": {
                    "population": 2464875,
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 2181,
                    "deceased": 12,
                    "recovered": 1050,
                    "tested": 27284
                }
            },
            "Vellore": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 1667,
                    "deceased": 4,
                    "recovered": 443,
                    "tested": 21909
                }
            },
            "Viluppuram": {
                "meta": {
                    "population": 3458873,
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 1020,
                    "deceased": 17,
                    "recovered": 601,
                    "tested": 18440
                }
            },
            "Virudhunagar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-20",
                        "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-20-06-20-COVID-19-6-PM.pdf"
                    }
                },
                "total": {
                    "confirmed": 679,
                    "deceased": 7,
                    "recovered": 296,
                    "tested": 14024
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T18:47:28+05:30",
            "notes": "2 deaths cross notified to other states from Chennai and Coimbatore.\n1 patient died after turning negative for infection in Chengalpattu.\nThese cases have been added to TN deceased tally",
            "population": 75695000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://stopcorona.tn.gov.in/wp-content/uploads/2020/07/Media-Bulletin-03.07.2020-25-Pages-English-469-KB.pdf"
            }
        },
        "total": {
            "confirmed": 102721,
            "deceased": 1385,
            "recovered": 58378,
            "tested": 1270720
        }
    },
    "TR": {
        "districts": {
            "Dhalai": {
                "meta": {
                    "population": 378230,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://covid19.tripura.gov.in/Visitor/ViewStatus.aspx"
                    }
                },
                "total": {
                    "confirmed": 242,
                    "recovered": 201,
                    "tested": 6838
                }
            },
            "Gomati": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://covid19.tripura.gov.in/Visitor/ViewStatus.aspx"
                    }
                },
                "total": {
                    "confirmed": 179,
                    "recovered": 110,
                    "tested": 6876
                }
            },
            "Khowai": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://covid19.tripura.gov.in/Visitor/ViewStatus.aspx"
                    }
                },
                "total": {
                    "confirmed": 79,
                    "recovered": 32,
                    "tested": 3209
                }
            },
            "North Tripura": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://covid19.tripura.gov.in/Visitor/ViewStatus.aspx"
                    }
                },
                "total": {
                    "confirmed": 47,
                    "recovered": 16,
                    "tested": 13310
                }
            },
            "Sipahijala": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://covid19.tripura.gov.in/Visitor/ViewStatus.aspx"
                    }
                },
                "total": {
                    "confirmed": 579,
                    "recovered": 522,
                    "tested": 7960
                }
            },
            "South Tripura": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://covid19.tripura.gov.in/Visitor/ViewStatus.aspx"
                    }
                },
                "total": {
                    "confirmed": 138,
                    "recovered": 79,
                    "tested": 7408
                }
            },
            "Unknown": {
                "total": {
                    "recovered": 53
                }
            },
            "Unokoti": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://covid19.tripura.gov.in/Visitor/ViewStatus.aspx"
                    }
                },
                "total": {
                    "confirmed": 73,
                    "recovered": 65,
                    "tested": 2712
                }
            },
            "West Tripura": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://covid19.tripura.gov.in/Visitor/ViewStatus.aspx"
                    }
                },
                "total": {
                    "confirmed": 196,
                    "deceased": 1,
                    "recovered": 121,
                    "tested": 20321
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T23:37:27+05:30",
            "population": 3992000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://t.me/Covid19india_Auxiliary_Test_Data/874"
            }
        },
        "total": {
            "confirmed": 1533,
            "deceased": 1,
            "recovered": 1199,
            "tested": 68634
        }
    },
    "TT": {
        "delta": {
            "confirmed": 565,
            "deceased": 22,
            "recovered": 483
        },
        "meta": {
            "last_updated": "2020-07-04T15:09:25+05:30",
            "population": 1332900000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/ICMRDELHI/status/1279256992754790405?s=20)"
            }
        },
        "total": {
            "confirmed": 650454,
            "deceased": 18691,
            "migrated": 66,
            "recovered": 394802,
            "tested": 9540132
        }
    },
    "UN": {
        "delta": {
            "confirmed": -1032
        },
        "meta": {
            "last_updated": "2020-07-04T10:13:27+05:30",
            "notes": "MoHFW website reports that these are the 'cases that are being reassigned to states'. 1032 cases were decreased in this category today by MoHFW. We have removed these cases from this category"
        },
        "total": {
            "confirmed": 4999
        }
    },
    "UP": {
        "districts": {
            "Agra": {
                "meta": {
                    "population": 4418797,
                    "tested": {
                        "last_updated": "2020-05-30",
                        "source": "https://twitter.com/OfficeOfDMAgra/status/1266778212211650561"
                    }
                },
                "total": {
                    "confirmed": 1264,
                    "deceased": 92,
                    "recovered": 1039,
                    "tested": 13162
                }
            },
            "Aligarh": {
                "total": {
                    "confirmed": 569,
                    "deceased": 23,
                    "recovered": 321
                }
            },
            "Ambedkar Nagar": {
                "meta": {
                    "population": 2397888
                },
                "total": {
                    "confirmed": 126,
                    "deceased": 4,
                    "recovered": 103
                }
            },
            "Amethi": {
                "total": {
                    "confirmed": 290,
                    "deceased": 1,
                    "recovered": 273
                }
            },
            "Amroha": {
                "total": {
                    "confirmed": 147,
                    "deceased": 3,
                    "recovered": 99
                }
            },
            "Auraiya": {
                "total": {
                    "confirmed": 106,
                    "deceased": 2,
                    "recovered": 89
                }
            },
            "Ayodhya": {
                "total": {
                    "confirmed": 305,
                    "deceased": 4,
                    "recovered": 199
                }
            },
            "Azamgarh": {
                "total": {
                    "confirmed": 263,
                    "deceased": 7,
                    "recovered": 184
                }
            },
            "Baghpat": {
                "meta": {
                    "population": 1303048
                },
                "total": {
                    "confirmed": 303,
                    "deceased": 5,
                    "recovered": 217
                }
            },
            "Bahraich": {
                "total": {
                    "confirmed": 129,
                    "deceased": 1,
                    "recovered": 121
                }
            },
            "Ballia": {
                "meta": {
                    "population": 3239774
                },
                "total": {
                    "confirmed": 155,
                    "deceased": 1,
                    "recovered": 100
                }
            },
            "Balrampur": {
                "total": {
                    "confirmed": 87,
                    "deceased": 2,
                    "recovered": 51
                }
            },
            "Banda": {
                "meta": {
                    "population": 1799410
                },
                "total": {
                    "confirmed": 47,
                    "recovered": 39
                }
            },
            "Barabanki": {
                "total": {
                    "confirmed": 394,
                    "deceased": 2,
                    "recovered": 290
                }
            },
            "Bareilly": {
                "meta": {
                    "population": 4448359,
                    "tested": {
                        "last_updated": "2020-06-17",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/531"
                    }
                },
                "total": {
                    "confirmed": 316,
                    "deceased": 11,
                    "recovered": 170,
                    "tested": 4251
                }
            },
            "Basti": {
                "total": {
                    "confirmed": 371,
                    "deceased": 15,
                    "recovered": 312
                }
            },
            "Bhadohi": {
                "total": {
                    "confirmed": 152,
                    "deceased": 1,
                    "recovered": 110
                }
            },
            "Bijnor": {
                "total": {
                    "confirmed": 306,
                    "deceased": 6,
                    "recovered": 221
                }
            },
            "Budaun": {
                "meta": {
                    "population": 3681896,
                    "tested": {
                        "last_updated": "2020-06-17",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/531"
                    }
                },
                "total": {
                    "confirmed": 153,
                    "deceased": 2,
                    "recovered": 98,
                    "tested": 3643
                }
            },
            "Bulandshahr": {
                "total": {
                    "confirmed": 650,
                    "deceased": 22,
                    "recovered": 465
                }
            },
            "Chandauli": {
                "meta": {
                    "population": 1952756
                },
                "total": {
                    "confirmed": 171,
                    "deceased": 3,
                    "recovered": 75
                }
            },
            "Chitrakoot": {
                "total": {
                    "confirmed": 100,
                    "deceased": 2,
                    "recovered": 86
                }
            },
            "Deoria": {
                "meta": {
                    "population": 3100946
                },
                "total": {
                    "confirmed": 241,
                    "deceased": 4,
                    "recovered": 172
                }
            },
            "Etah": {
                "total": {
                    "confirmed": 140,
                    "deceased": 8,
                    "recovered": 69
                }
            },
            "Etawah": {
                "meta": {
                    "population": 1581810
                },
                "total": {
                    "confirmed": 322,
                    "deceased": 14,
                    "recovered": 181
                }
            },
            "Farrukhabad": {
                "total": {
                    "confirmed": 182,
                    "deceased": 7,
                    "recovered": 109
                }
            },
            "Fatehpur": {
                "meta": {
                    "population": 2632733
                },
                "total": {
                    "confirmed": 152,
                    "deceased": 1,
                    "recovered": 113
                }
            },
            "Firozabad": {
                "total": {
                    "confirmed": 521,
                    "deceased": 26,
                    "recovered": 450
                }
            },
            "Gautam Buddha Nagar": {
                "meta": {
                    "population": 1648115
                },
                "total": {
                    "confirmed": 2569,
                    "deceased": 23,
                    "recovered": 1541
                }
            },
            "Ghaziabad": {
                "meta": {
                    "population": 4681645
                },
                "total": {
                    "confirmed": 1937,
                    "deceased": 59,
                    "recovered": 833
                }
            },
            "Ghazipur": {
                "total": {
                    "confirmed": 360,
                    "deceased": 4,
                    "recovered": 293
                }
            },
            "Gonda": {
                "meta": {
                    "population": 3433919
                },
                "total": {
                    "confirmed": 173,
                    "deceased": 5,
                    "recovered": 147
                }
            },
            "Gorakhpur": {
                "total": {
                    "confirmed": 395,
                    "deceased": 13,
                    "recovered": 247
                }
            },
            "Hamirpur": {
                "total": {
                    "confirmed": 84,
                    "deceased": 1,
                    "recovered": 69
                }
            },
            "Hapur": {
                "total": {
                    "confirmed": 654,
                    "deceased": 14,
                    "recovered": 518
                }
            },
            "Hardoi": {
                "meta": {
                    "population": 4092845
                },
                "total": {
                    "confirmed": 239,
                    "deceased": 4,
                    "recovered": 185
                }
            },
            "Hathras": {
                "total": {
                    "confirmed": 191,
                    "deceased": 3,
                    "recovered": 143
                }
            },
            "Jalaun": {
                "total": {
                    "confirmed": 196,
                    "deceased": 7,
                    "recovered": 132
                }
            },
            "Jaunpur": {
                "total": {
                    "confirmed": 551,
                    "deceased": 9,
                    "recovered": 469
                }
            },
            "Jhansi": {
                "meta": {
                    "population": 1998603
                },
                "total": {
                    "confirmed": 214,
                    "deceased": 22,
                    "recovered": 83
                }
            },
            "Kannauj": {
                "total": {
                    "confirmed": 249,
                    "deceased": 1,
                    "recovered": 215
                }
            },
            "Kanpur Dehat": {
                "meta": {
                    "population": 1796184
                },
                "total": {
                    "confirmed": 68,
                    "deceased": 1,
                    "recovered": 50
                }
            },
            "Kanpur Nagar": {
                "total": {
                    "confirmed": 1251,
                    "deceased": 54,
                    "recovered": 901
                }
            },
            "Kasganj": {
                "total": {
                    "confirmed": 90,
                    "recovered": 53
                }
            },
            "Kaushambi": {
                "total": {
                    "confirmed": 103,
                    "deceased": 1,
                    "recovered": 65
                }
            },
            "Kushinagar": {
                "meta": {
                    "population": 3564544
                },
                "total": {
                    "confirmed": 154,
                    "deceased": 3,
                    "recovered": 78
                }
            },
            "Lakhimpur Kheri": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-17",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/531"
                    }
                },
                "total": {
                    "confirmed": 119,
                    "recovered": 105,
                    "tested": 4933
                }
            },
            "Lalitpur": {
                "meta": {
                    "population": 1221592
                },
                "total": {
                    "confirmed": 10,
                    "deceased": 3,
                    "recovered": 2
                }
            },
            "Lucknow": {
                "total": {
                    "confirmed": 1261,
                    "deceased": 22,
                    "recovered": 770
                }
            },
            "Maharajganj": {
                "total": {
                    "confirmed": 181,
                    "deceased": 3,
                    "recovered": 132
                }
            },
            "Mahoba": {
                "total": {
                    "confirmed": 62,
                    "deceased": 1,
                    "recovered": 51
                }
            },
            "Mainpuri": {
                "meta": {
                    "population": 1868529
                },
                "total": {
                    "confirmed": 258,
                    "deceased": 8,
                    "recovered": 203
                }
            },
            "Mathura": {
                "total": {
                    "confirmed": 391,
                    "deceased": 13,
                    "recovered": 230
                }
            },
            "Mau": {
                "meta": {
                    "population": 2205968
                },
                "total": {
                    "confirmed": 154,
                    "deceased": 4,
                    "recovered": 86
                }
            },
            "Meerut": {
                "total": {
                    "confirmed": 1096,
                    "deceased": 88,
                    "recovered": 742
                }
            },
            "Mirzapur": {
                "meta": {
                    "population": 2496970
                },
                "total": {
                    "confirmed": 120,
                    "deceased": 1,
                    "recovered": 72
                }
            },
            "Moradabad": {
                "total": {
                    "confirmed": 504,
                    "deceased": 24,
                    "recovered": 357
                }
            },
            "Muzaffarnagar": {
                "meta": {
                    "population": 4143512
                },
                "total": {
                    "confirmed": 302,
                    "deceased": 8,
                    "recovered": 233
                }
            },
            "Pilibhit": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-17",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/531"
                    }
                },
                "total": {
                    "confirmed": 141,
                    "recovered": 104,
                    "tested": 6293
                }
            },
            "Pratapgarh": {
                "total": {
                    "confirmed": 120,
                    "deceased": 7,
                    "recovered": 103
                }
            },
            "Prayagraj": {
                "total": {
                    "confirmed": 326,
                    "deceased": 11,
                    "recovered": 223
                }
            },
            "Rae Bareli": {
                "meta": {
                    "population": 3405559
                },
                "total": {
                    "confirmed": 142,
                    "deceased": 3,
                    "recovered": 116
                }
            },
            "Rampur": {
                "total": {
                    "confirmed": 371,
                    "deceased": 3,
                    "recovered": 309
                }
            },
            "Saharanpur": {
                "meta": {
                    "population": 3466382
                },
                "total": {
                    "confirmed": 433,
                    "recovered": 348
                }
            },
            "Sambhal": {
                "total": {
                    "confirmed": 362,
                    "deceased": 7,
                    "recovered": 277
                }
            },
            "Sant Kabir Nagar": {
                "meta": {
                    "population": 1715183
                },
                "total": {
                    "confirmed": 256,
                    "deceased": 7,
                    "recovered": 188
                }
            },
            "Shahjahanpur": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-06-17",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/531"
                    }
                },
                "total": {
                    "confirmed": 140,
                    "recovered": 99,
                    "tested": 4287
                }
            },
            "Shamli": {
                "total": {
                    "confirmed": 160,
                    "deceased": 2,
                    "recovered": 117
                }
            },
            "Shrawasti": {
                "total": {
                    "confirmed": 70,
                    "deceased": 1,
                    "recovered": 52
                }
            },
            "Siddharthnagar": {
                "meta": {
                    "population": 2559297
                },
                "total": {
                    "confirmed": 270,
                    "deceased": 9,
                    "recovered": 197
                }
            },
            "Sitapur": {
                "total": {
                    "confirmed": 63,
                    "recovered": 56
                }
            },
            "Sonbhadra": {
                "meta": {
                    "population": 1862559
                },
                "total": {
                    "confirmed": 45,
                    "recovered": 34
                }
            },
            "Sultanpur": {
                "total": {
                    "confirmed": 206,
                    "deceased": 4,
                    "recovered": 162
                }
            },
            "Unnao": {
                "meta": {
                    "population": 3108367
                },
                "total": {
                    "confirmed": 196,
                    "deceased": 3,
                    "recovered": 119
                }
            },
            "Varanasi": {
                "total": {
                    "confirmed": 598,
                    "deceased": 24,
                    "recovered": 332
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T19:56:27+05:30",
            "population": 224979000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/UPGovt/status/1279053155863416834?s=20"
            }
        },
        "total": {
            "confirmed": 25797,
            "deceased": 749,
            "recovered": 17597,
            "tested": 810991
        }
    },
    "UT": {
        "districts": {
            "Almora": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/PIBDehradun/status/1279207392450732032?s=20"
                    }
                },
                "total": {
                    "confirmed": 190,
                    "deceased": 2,
                    "migrated": 1,
                    "recovered": 163,
                    "tested": 3358
                }
            },
            "Bageshwar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/PIBDehradun/status/1279207392450732032?s=20"
                    }
                },
                "total": {
                    "confirmed": 86,
                    "deceased": 1,
                    "recovered": 74,
                    "tested": 1561
                }
            },
            "Chamoli": {
                "meta": {
                    "population": 391605,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/PIBDehradun/status/1279207392450732032?s=20"
                    }
                },
                "total": {
                    "confirmed": 76,
                    "recovered": 65,
                    "tested": 2766
                }
            },
            "Champawat": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/PIBDehradun/status/1279207392450732032?s=20"
                    }
                },
                "total": {
                    "confirmed": 59,
                    "deceased": 1,
                    "recovered": 49,
                    "tested": 1783
                }
            },
            "Dehradun": {
                "meta": {
                    "population": 1696694,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/PIBDehradun/status/1279207392450732032?s=20"
                    }
                },
                "total": {
                    "confirmed": 734,
                    "deceased": 25,
                    "migrated": 18,
                    "recovered": 579,
                    "tested": 21370
                }
            },
            "Haridwar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/PIBDehradun/status/1279207392450732032?s=20"
                    }
                },
                "total": {
                    "confirmed": 317,
                    "migrated": 7,
                    "recovered": 281,
                    "tested": 10788
                }
            },
            "Nainital": {
                "meta": {
                    "population": 954605,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/PIBDehradun/status/1279207392450732032?s=20"
                    }
                },
                "total": {
                    "confirmed": 526,
                    "deceased": 3,
                    "migrated": 1,
                    "recovered": 345,
                    "tested": 8406
                }
            },
            "Pauri Garhwal": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/PIBDehradun/status/1279207392450732032?s=20"
                    }
                },
                "total": {
                    "confirmed": 143,
                    "deceased": 3,
                    "recovered": 107,
                    "tested": 4916
                }
            },
            "Pithoragarh": {
                "meta": {
                    "population": 483439,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/PIBDehradun/status/1279207392450732032?s=20"
                    }
                },
                "total": {
                    "confirmed": 67,
                    "recovered": 61,
                    "tested": 1848
                }
            },
            "Rudraprayag": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/PIBDehradun/status/1279207392450732032?s=20"
                    }
                },
                "total": {
                    "confirmed": 66,
                    "deceased": 1,
                    "recovered": 60,
                    "tested": 1925
                }
            },
            "Tehri Garhwal": {
                "meta": {
                    "population": 618931,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/PIBDehradun/status/1279207392450732032?s=20"
                    }
                },
                "total": {
                    "confirmed": 420,
                    "deceased": 2,
                    "recovered": 415,
                    "tested": 4101
                }
            },
            "Udham Singh Nagar": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/PIBDehradun/status/1279207392450732032?s=20"
                    }
                },
                "total": {
                    "confirmed": 289,
                    "deceased": 3,
                    "recovered": 223,
                    "tested": 8645
                }
            },
            "Uttarkashi": {
                "meta": {
                    "population": 330086,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/PIBDehradun/status/1279207392450732032?s=20"
                    }
                },
                "total": {
                    "confirmed": 75,
                    "deceased": 1,
                    "recovered": 59,
                    "tested": 2271
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T20:38:35+05:30",
            "notes": "27 Migrated cases reduced from Active count",
            "population": 11141000,
            "tested": {
                "last_updated": "2020-07-03"
            }
        },
        "total": {
            "confirmed": 3048,
            "deceased": 42,
            "migrated": 27,
            "recovered": 2481,
            "tested": 73738
        }
    },
    "WB": {
        "districts": {
            "Alipurduar": {
                "total": {
                    "confirmed": 186,
                    "recovered": 177
                }
            },
            "Bankura": {
                "total": {
                    "confirmed": 259,
                    "recovered": 210
                }
            },
            "Birbhum": {
                "total": {
                    "confirmed": 305,
                    "deceased": 3,
                    "recovered": 285
                }
            },
            "Cooch Behar": {
                "total": {
                    "confirmed": 305,
                    "recovered": 304
                }
            },
            "Dakshin Dinajpur": {
                "total": {
                    "confirmed": 218,
                    "recovered": 183
                }
            },
            "Darjeeling": {
                "total": {
                    "confirmed": 554,
                    "deceased": 10,
                    "recovered": 419
                }
            },
            "Hooghly": {
                "total": {
                    "confirmed": 1118,
                    "deceased": 26,
                    "recovered": 755
                }
            },
            "Howrah": {
                "meta": {
                    "population": 4850029
                },
                "total": {
                    "confirmed": 2928,
                    "deceased": 104,
                    "recovered": 1974
                }
            },
            "Jalpaiguri": {
                "total": {
                    "confirmed": 386,
                    "deceased": 1,
                    "recovered": 310
                }
            },
            "Jhargram": {
                "total": {
                    "confirmed": 19,
                    "recovered": 19
                }
            },
            "Kalimpong": {
                "total": {
                    "confirmed": 55,
                    "deceased": 1,
                    "recovered": 48
                }
            },
            "Kolkata": {
                "meta": {
                    "population": 4496694
                },
                "total": {
                    "confirmed": 6622,
                    "deceased": 402,
                    "recovered": 4142
                }
            },
            "Malda": {
                "total": {
                    "confirmed": 740,
                    "deceased": 2,
                    "recovered": 445
                }
            },
            "Murshidabad": {
                "total": {
                    "confirmed": 256,
                    "deceased": 4,
                    "recovered": 200
                }
            },
            "Nadia": {
                "total": {
                    "confirmed": 328,
                    "deceased": 5,
                    "recovered": 250
                }
            },
            "North 24 Parganas": {
                "meta": {
                    "population": 10009781
                },
                "total": {
                    "confirmed": 3382,
                    "deceased": 111,
                    "recovered": 1913
                }
            },
            "Other State": {
                "total": {
                    "confirmed": 66,
                    "deceased": 3,
                    "recovered": 63
                }
            },
            "Paschim Bardhaman": {
                "total": {
                    "confirmed": 155,
                    "deceased": 3,
                    "recovered": 120
                }
            },
            "Paschim Medinipur": {
                "meta": {
                    "population": 5913457
                },
                "total": {
                    "confirmed": 385,
                    "deceased": 5,
                    "recovered": 328
                }
            },
            "Purba Bardhaman": {
                "total": {
                    "confirmed": 182,
                    "deceased": 2,
                    "recovered": 149
                }
            },
            "Purba Medinipur": {
                "meta": {
                    "population": 5095875
                },
                "total": {
                    "confirmed": 376,
                    "deceased": 4,
                    "recovered": 273
                }
            },
            "Purulia": {
                "total": {
                    "confirmed": 95,
                    "recovered": 87
                }
            },
            "South 24 Parganas": {
                "total": {
                    "confirmed": 1254,
                    "deceased": 30,
                    "recovered": 662
                }
            },
            "Uttar Dinajpur": {
                "total": {
                    "confirmed": 314,
                    "deceased": 1,
                    "recovered": 255
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-03T20:05:27+05:30",
            "population": 96906000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://www.wbhealth.gov.in/uploaded_files/corona/WB_DHFW_Bulletin_3rd_JULY_REPORT_FINAL.pdf"
            }
        },
        "total": {
            "confirmed": 20488,
            "deceased": 717,
            "recovered": 13571,
            "tested": 519054
        }
    }
}

states = []
confirmed = []
for state in coronaData:
    if state != 'TT':
        states.append(state)
        if "total" in coronaData[state]:
            confirmed.append(coronaData[state]["total"]["confirmed"])
        else:
            confirmed.append(0)

print(confirmed)

plt.bar(states, confirmed)
plt.show()


coronaData1 = {
    "AN": {
        "delta": {
            "confirmed": 3
        },
        "districts": {
            "North and Middle Andaman": {
                "total": {
                    "confirmed": 1,
                    "recovered": 1
                }
            },
            "South Andaman": {
                "meta": {
                    "population": 238142
                },
                "total": {
                    "confirmed": 51,
                    "recovered": 32
                }
            },
            "Unknown": {
                "delta": {
                    "confirmed": 3
                },
                "total": {
                    "confirmed": 67,
                    "recovered": 21
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-04T09:44:28+05:30",
            "population": 397000,
            "tested": {
                "last_updated": "2020-07-01",
                "source": "https://dhs.andaman.gov.in/NewEvents/313.pdf"
            }
        },
        "total": {
            "confirmed": 119,
            "recovered": 54,
            "tested": 15982
        }
    },
    "AP": {
        "delta": {
            "confirmed": 765,
            "deceased": 12,
            "recovered": 376,
            "tested": 24962
        },
        "districts": {
            "Anantapur": {
                "delta": {
                    "confirmed": 127,
                    "recovered": 28
                },
                "meta": {
                    "population": 4081148,
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 2099,
                    "deceased": 9,
                    "recovered": 1139,
                    "tested": 64442
                }
            },
            "Chittoor": {
                "delta": {
                    "confirmed": 67,
                    "deceased": 2,
                    "recovered": 52
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 1250,
                    "deceased": 10,
                    "recovered": 463,
                    "tested": 69789
                }
            },
            "East Godavari": {
                "delta": {
                    "confirmed": 102,
                    "recovered": 28
                },
                "meta": {
                    "population": 5154296,
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 1489,
                    "deceased": 8,
                    "recovered": 416,
                    "tested": 96237
                }
            },
            "Foreign Evacuees": {
                "delta": {
                    "confirmed": 6,
                    "recovered": 25
                },
                "total": {
                    "confirmed": 415,
                    "recovered": 185
                }
            },
            "Guntur": {
                "delta": {
                    "confirmed": 60
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 1670,
                    "deceased": 19,
                    "recovered": 713,
                    "tested": 79349
                }
            },
            "Krishna": {
                "delta": {
                    "confirmed": 70,
                    "recovered": 16
                },
                "meta": {
                    "population": 4517398,
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 1681,
                    "deceased": 68,
                    "recovered": 669,
                    "tested": 94199
                }
            },
            "Kurnool": {
                "delta": {
                    "confirmed": 118,
                    "deceased": 3,
                    "recovered": 58
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 2354,
                    "deceased": 76,
                    "recovered": 1147,
                    "tested": 86170
                }
            },
            "Other State": {
                "delta": {
                    "confirmed": 32,
                    "recovered": 40
                },
                "total": {
                    "confirmed": 2143,
                    "recovered": 1386
                }
            },
            "Prakasam": {
                "delta": {
                    "confirmed": 57,
                    "recovered": 38
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 673,
                    "deceased": 2,
                    "recovered": 305,
                    "tested": 61021
                }
            },
            "S.P.S. Nellore": {
                "delta": {
                    "confirmed": 27
                },
                "meta": {
                    "population": 558548,
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 685,
                    "deceased": 6,
                    "recovered": 374,
                    "tested": 55644
                }
            },
            "Srikakulam": {
                "delta": {
                    "deceased": 3
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 93,
                    "deceased": 6,
                    "recovered": 54,
                    "tested": 92579
                }
            },
            "Visakhapatnam": {
                "delta": {
                    "confirmed": 9,
                    "deceased": 2,
                    "recovered": 43
                },
                "meta": {
                    "population": 4290589,
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 633,
                    "deceased": 5,
                    "recovered": 359,
                    "tested": 67682
                }
            },
            "Vizianagaram": {
                "delta": {
                    "confirmed": 13,
                    "deceased": 1,
                    "recovered": 7
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 197,
                    "deceased": 3,
                    "recovered": 63,
                    "tested": 37774
                }
            },
            "West Godavari": {
                "delta": {
                    "confirmed": 4,
                    "recovered": 41
                },
                "meta": {
                    "population": 3936966,
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 1124,
                    "deceased": 4,
                    "recovered": 309,
                    "tested": 59217
                }
            },
            "Y.S.R. Kadapa": {
                "delta": {
                    "confirmed": 73,
                    "deceased": 1
                },
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-02",
                        "source": "https://t.me/Covid19india_Auxiliary_Test_Data/839"
                    }
                },
                "total": {
                    "confirmed": 1193,
                    "deceased": 2,
                    "recovered": 426,
                    "tested": 66138
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-04T14:46:27+05:30",
            "notes": "Total includes patients from other states and a new category \"Foreign Evacuees\" which is now reported in AP bulletin.",
            "population": 52221000,
            "tested": {
                "last_updated": "2020-07-04",
                "source": "https://twitter.com/ArogyaAndhra/status/1279329071755714560?s=20"
            }
        },
        "total": {
            "confirmed": 17699,
            "deceased": 218,
            "recovered": 8008,
            "tested": 996573
        }
    },
    "AR": {
        "districts": {
            "Anjaw": {
                "meta": {
                    "population": 21167,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 178
                }
            },
            "Capital Complex": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 7500
                }
            },
            "Changlang": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 89,
                    "recovered": 37,
                    "tested": 4556
                }
            },
            "Dibang Valley": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 10
                }
            },
            "East Kameng": {
                "meta": {
                    "population": 78690,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 215
                }
            },
            "East Siang": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 10,
                    "recovered": 10,
                    "tested": 2011
                }
            },
            "Kamle": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 54
                }
            },
            "Kra-Daadi": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 13
                }
            },
            "Kurung Kumey": {
                "meta": {
                    "population": 92076,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 11
                }
            },
            "Lepa Rada": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 1,
                    "tested": 162
                }
            },
            "Lohit": {
                "meta": {
                    "population": 145726,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 4,
                    "recovered": 3,
                    "tested": 1145
                }
            },
            "Longding": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 4,
                    "recovered": 1,
                    "tested": 701
                }
            },
            "Lower Dibang Valley": {
                "meta": {
                    "population": 54080,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 3,
                    "recovered": 2,
                    "tested": 855
                }
            },
            "Lower Siang": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 3,
                    "tested": 479
                }
            },
            "Lower Subansiri": {
                "meta": {
                    "population": 83030,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 530
                }
            },
            "Namsai": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 13,
                    "recovered": 3,
                    "tested": 1520
                }
            },
            "Pakke Kessang": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 1,
                    "recovered": 1,
                    "tested": 255
                }
            },
            "Papum Pare": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 89,
                    "recovered": 8,
                    "tested": 689
                }
            },
            "Shi Yomi": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 80
                }
            },
            "Siang": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 122
                }
            },
            "Tawang": {
                "meta": {
                    "population": 49977,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 2,
                    "tested": 742
                }
            },
            "Tirap": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 3,
                    "recovered": 2,
                    "tested": 1410
                }
            },
            "Upper Siang": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 1,
                    "recovered": 1,
                    "tested": 457
                }
            },
            "Upper Subansiri": {
                "meta": {
                    "population": 83448,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "tested": 488
                }
            },
            "West Kameng": {
                "meta": {
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 27,
                    "deceased": 1,
                    "recovered": 6,
                    "tested": 1188
                }
            },
            "West Siang": {
                "meta": {
                    "population": 112274,
                    "tested": {
                        "last_updated": "2020-07-03",
                        "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
                    }
                },
                "total": {
                    "confirmed": 2,
                    "recovered": 1,
                    "tested": 546
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-04T00:26:29+05:30",
            "population": 1504000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/DirectorateofHS/status/1279117565969567744?s=20"
            }
        },
        "total": {
            "confirmed": 252,
            "deceased": 1,
            "recovered": 75,
            "tested": 25917
        }
    },
    "AS": {
        "districts": {
            "Airport Quarantine": {
                "total": {
                    "confirmed": 4
                }
            },
            "Baksa": {
                "total": {
                    "confirmed": 85
                }
            },
            "Barpeta": {
                "meta": {
                    "population": 1693622
                },
                "total": {
                    "confirmed": 150,
                    "recovered": 55
                }
            },
            "Biswanath": {
                "total": {
                    "confirmed": 58,
                    "recovered": 16
                }
            },
            "Bongaigaon": {
                "meta": {
                    "population": 738804
                },
                "total": {
                    "confirmed": 24,
                    "recovered": 7
                }
            },
            "Cachar": {
                "total": {
                    "confirmed": 98,
                    "recovered": 82
                }
            },
            "Charaideo": {
                "total": {
                    "confirmed": 16
                }
            },
            "Chirang": {
                "total": {
                    "confirmed": 52
                }
            },
            "Darrang": {
                "meta": {
                    "population": 928500
                },
                "total": {
                    "confirmed": 102
                }
            },
            "Dhemaji": {
                "total": {
                    "confirmed": 96,
                    "recovered": 6
                }
            },
            "Dhubri": {
                "meta": {
                    "population": 1949258
                },
                "total": {
                    "confirmed": 334,
                    "recovered": 5
                }
            },
            "Dibrugarh": {
                "total": {
                    "confirmed": 77,
                    "recovered": 5
                }
            },
            "Dima Hasao": {
                "meta": {
                    "population": 214102
                },
                "total": {
                    "confirmed": 89,
                    "recovered": 9
                }
            },
            "Goalpara": {
                "total": {
                    "confirmed": 57,
                    "recovered": 4
                }
            },
            "Golaghat": {
                "meta": {
                    "population": 1066888
                },
                "total": {
                    "confirmed": 272,
                    "recovered": 88
                }
            },
            "Hailakandi": {
                "total": {
                    "confirmed": 78,
                    "deceased": 1,
                    "recovered": 5
                }
            },
            "Hojai": {
                "total": {
                    "confirmed": 267
                }
            },
            "Jorhat": {
                "total": {
                    "confirmed": 145,
                    "recovered": 54
                }
            },
            "Kamrup": {
                "meta": {
                    "population": 1517542
                },
                "total": {
                    "confirmed": 215,
                    "recovered": 21
                }
            },
            "Kamrup Metropolitan": {
                "total": {
                    "confirmed": 2419,
                    "deceased": 6,
                    "recovered": 383
                }
            },
            "Karbi Anglong": {
                "meta": {
                    "population": 956313
                },
                "total": {
                    "confirmed": 41,
                    "recovered": 7
                }
            },
            "Karimganj": {
                "total": {
                    "confirmed": 106,
                    "recovered": 20
                }
            },
            "Kokrajhar": {
                "meta": {
                    "population": 887142
                },
                "total": {
                    "confirmed": 86,
                    "recovered": 10
                }
            },
            "Lakhimpur": {
                "total": {
                    "confirmed": 85,
                    "recovered": 6
                }
            },
            "Majuli": {
                "total": {
                    "confirmed": 21
                }
            },
            "Morigaon": {
                "total": {
                    "confirmed": 49,
                    "recovered": 28
                }
            },
            "Nagaon": {
                "meta": {
                    "population": 2823768
                },
                "total": {
                    "confirmed": 330,
                    "recovered": 25
                }
            },
            "Nalbari": {
                "total": {
                    "confirmed": 28,
                    "recovered": 9
                }
            },
            "Other State": {
                "total": {
                    "confirmed": 1,
                    "recovered": 1
                }
            },
            "Sivasagar": {
                "total": {
                    "confirmed": 29,
                    "recovered": 26
                }
            },
            "Sonitpur": {
                "meta": {
                    "population": 1924110
                },
                "total": {
                    "confirmed": 122,
                    "recovered": 35
                }
            },
            "South Salmara Mankachar": {
                "total": {
                    "confirmed": 7,
                    "recovered": 1
                }
            },
            "Tinsukia": {
                "total": {
                    "confirmed": 114,
                    "recovered": 6
                }
            },
            "Udalguri": {
                "meta": {
                    "population": 831668
                },
                "total": {
                    "confirmed": 105,
                    "recovered": 2
                }
            },
            "Unknown": {
                "total": {
                    "confirmed": 4010,
                    "deceased": 7,
                    "migrated": 3,
                    "recovered": 5412
                }
            },
            "West Karbi Anglong": {
                "total": {
                    "confirmed": 28
                }
            }
        },
        "meta": {
            "last_updated": "2020-07-04T00:26:27+05:30",
            "notes": "Includes one case from Nagaland.\nTotal of 3 patients who migrated to other states has been reduced from Active count",
            "population": 34293000,
            "tested": {
                "last_updated": "2020-07-03",
                "source": "https://twitter.com/nhm_assam/status/1279085918721171456?s=20"
            }
        },
        "total": {
            "confirmed": 9800,
            "deceased": 14,
            "migrated": 3,
            "recovered": 6328,
            "tested": 438882
        }
    }
}
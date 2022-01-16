from app.models import EtlRequest

CASE1 = EtlRequest.parse_obj({
    "results": [
        {
            "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
            "date": "2021-01-01",
            "start": 1609484400000,
            "finish": 1609527600000,
            "cost": 12,
            "breaks": [
                {
                    "id": "c1ccfad9-50f6-417d-a52e-afb0d18f6763",
                    "start": 1609498800000,
                    "finish": 1609502400000,
                    "paid": False,
                }
            ],
            "allowances": [
                {
                    "id": "7cf3d3a8-1ac1-4616-afa8-dcf3ae4b0474",
                    "value": 1.0,
                    "cost": 11.8,
                },
                {
                    "id": "76fa2b79-a4ad-4a5d-8fc1-ef19cdc3d7af",
                    "value": 1.0,
                    "cost": 15.0,
                },
            ],
            "award_interpretations": [
                {
                    "id": "81b2430d-60be-40b0-ba66-b736027e4572",
                    "date": "2021-01-01",
                    "units": 1.0,
                    "cost": 8.43,
                }
            ],
        }
    ],
})

CASE2 = EtlRequest.parse_obj({
    "results": [
        {
            "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
            "date": "2022-05-01",
            "start": 1609484400000,
            "finish": 1609527600000,
            "cost": 12,
            "breaks": [
                {
                    "id": "c1ccfad9-50f6-417d-a52e-afb0d18f6763",
                    "start": 1609498810000,
                    "finish": 1609502490000,
                    "paid": False,
                },
                {
                    "id": "c1ccfad9-50f6-417d-a52e-afb0d18f6763",
                    "start": 1609498830000,
                    "finish": 1609502450000,
                    "paid": True,
                },
                {
                    "id": "c1ccfad9-50f6-417d-a52e-afb0d18f6763",
                    "start": 1609498890000,
                    "finish": 1609502480000,
                    "paid": True,
                }
            ],
            "allowances": [
                {
                    "id": "7cf3d3a8-1ac1-4616-afa8-dcf3ae4b0474",
                    "value": 1.0,
                    "cost": 11.8,
                },
                {
                    "id": "76fa2b79-a4ad-4a5d-8fc1-ef19cdc3d7af",
                    "value": 1.0,
                    "cost": 15.0,
                },
            ],
            "award_interpretations": [
                {
                    "id": "81b2430d-60be-40b0-ba66-b736027e4572",
                    "date": "2021-01-01",
                    "units": 1.0,
                    "cost": 8.43,
                }
            ],
        },
        {
            "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
            "date": "2021-05-01",
            "start": 1609484200000,
            "finish": 1609522000000,
            "cost": 11,
            "breaks": [
                {
                    "id": "c1ccfad9-50f6-417d-a52e-afb0d18f6763",
                    "start": 1609498800000,
                    "finish": 1609502400000,
                    "paid": True,
                }
            ],
            "allowances": [
                {
                    "id": "7cf3d3a8-1ac1-4616-afa8-dcf3ae4b0474",
                    "value": 1.0,
                    "cost": 17.8,
                },
                {
                    "id": "76fa2b79-a4ad-4a5d-8fc1-ef19cdc3d7af",
                    "value": 1.0,
                    "cost": 2.3,
                },
            ],
            "award_interpretations": [
                {
                    "id": "81b2430d-60be-40b0-ba66-b736027e4572",
                    "date": "2021-01-01",
                    "units": 1.0,
                    "cost": 8.43,
                }
            ],
        }
    ],
})

CASE3 = EtlRequest.parse_obj([])

CASE4 = EtlRequest.parse_obj({
    "results": [
        {
            "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
            "date": "2022-05-01",
            "start": 1609484400000,
            "finish": 1609527600000,
            "breaks": [],
            "allowances": [],
            "award_interpretations": [],
        },
        {
            "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
            "date": "2021-05-01",
            "start": 1609484200000,
            "finish": 1609522000000,
            "breaks": [],
            "allowances": [],
            "award_interpretations": [],
        }
    ],
})

CASE5 = EtlRequest.parse_obj({
    "results": [
        {
            "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
            "date": "2020-05-01",
            "start": 1609484400000,
            "finish": 1609527600000,
            "breaks": [],
            "allowances": [],
            "award_interpretations": [],
        },
        {
            "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
            "date": "2020-05-04",
            "start": 1609484200000,
            "finish": 1609522000000,
            "breaks": [],
            "allowances": [],
            "award_interpretations": [],
        },
        {
            "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
            "date": "2020-05-07",
            "start": 1609484200000,
            "finish": 1609522000000,
            "breaks": [
                {
                    "id": "c1ccfad9-50f6-417d-a52e-afb0d18f6763",
                    "start": 0,
                    "finish": 0,
                    "paid": True,
                }
            ],
            "allowances": [],
            "award_interpretations": [],
        },
        {
            "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
            "date": "2020-05-09",
            "start": 1609484200000,
            "finish": 1609522000000,
            "breaks": [],
            "allowances": [],
            "award_interpretations": [],
        },
        {
            "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
            "date": "2021-05-01",
            "start": 1609484200000,
            "finish": 1609522000000,
            "breaks": [],
            "allowances": [],
            "award_interpretations": [],
        },
        {
            "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
            "date": "2021-05-03",
            "start": 1609484200000,
            "finish": 1609522000000,
            "breaks": [],
            "allowances": [],
            "award_interpretations": [],
        },
        {
            "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
            "date": "2021-05-06",
            "start": 1609484200000,
            "finish": 1609522000000,
            "breaks": [
                {
                    "id": "c1ccfad9-50f6-417d-a52e-afb0d18f6763",
                    "start": 0,
                    "finish": 0,
                    "paid": True,
                }
            ],
            "allowances": [],
            "award_interpretations": [],
        },
        {
            "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
            "date": "2021-05-09",
            "start": 1609484200000,
            "finish": 1609522000000,
            "breaks": [],
            "allowances": [],
            "award_interpretations": [],
        },
        {
            "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
            "date": "2021-05-11",
            "start": 1609484200000,
            "finish": 1609522000000,
            "breaks": [],
            "allowances": [],
            "award_interpretations": [],
        },
        {
            "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
            "date": "2021-05-12",
            "start": 1609484200000,
            "finish": 1609522000000,
            "breaks": [],
            "allowances": [],
            "award_interpretations": [],
        },
        {
            "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
            "date": "2022-05-01",
            "start": 1609484200000,
            "finish": 1609522000000,
            "breaks": [],
            "allowances": [],
            "award_interpretations": [],
        },
        {
            "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
            "date": "2022-7-01",
            "start": 1609484200000,
            "finish": 1609522000000,
            "breaks": [],
            "allowances": [],
            "award_interpretations": [],
        }
    ],
})

"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["F0(t}"],
            "answer": 0,
        },
        {
            "input": ["Utc&g"],
            "answer": None,
        },
        {
            "input": ["-aB%|_-+2ADS.12+3.ADS1.2"],
            "answer": 2.12312,
        },
        {
            "input": ["-aB%|_+-2ADS.12+3.ADS1.2"],
            "answer": -2.12312,
        },
        {
            "input": ["zV№1}3;o.vEf``C.WqTY0"],
            "answer": 13.0,
        },
        {
            "input": ["!3B'j=(}89JQ6aWvN*%5@uy.r)B<?pZ.!545ZD^KF9Sx@gqfa*"],
            "answer": 38965.5459,
        },
    ],
    "Extra": [
        {
            "input": ["J-8:Z0"],
            "answer": -80,
        },
        {
            "input": ["zD{pQ"],
            "answer": None,
        },
        {
            "input": ["A4a!nq?XrA8Whdbn#VND"],
            "answer": 48,
        },
        {
            "input": ["^P!0Njz.Tz:GxC}№I.v);y1"],
            "answer": 0.1,
        },
        {
            "input": ["^B4-zq93GEM--4S}yi5d"],
            "answer": 49345,
        },
        {
            "input": ["v-Iu*B&9viteApr=0k}="],
            "answer": -90,
        },
        {
            "input": ["!#iHL}wcI?KR=X!gF0d&S-1zj&LgJ!`tzbn#mEPV7mL&R2f)W"],
            "answer": 172,
        },
        {
            "input": [">Xf;T-2WKI1lTv~duZp:qzowhNQ+#g?№^I?;hK#Y.sUsu7№%W:"],
            "answer": -21.7,
        },
    ]
}

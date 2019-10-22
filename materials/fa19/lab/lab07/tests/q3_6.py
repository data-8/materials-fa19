test = {
  'name': 'q3_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> rate_means.num_rows
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> test = False;
          >>> try:
          ...     test = round(rate_means.where("Death Penalty", "False").column(1).item(0), 3) == 8.12;
          >>> except:
          ...     test = round(rate_means.where("Death Penalty", False).column(1).item(0), 3) == 8.12;
          >>> test
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> test = False;
          >>> try:
          ...     test = round(rate_means.where("Death Penalty", "True").column(1).item(0), 3) == 7.514;
          >>> except:
          ...     test = round(rate_means.where("Death Penalty", True).column(1).item(0), 3) == 7.514;
          >>> test
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

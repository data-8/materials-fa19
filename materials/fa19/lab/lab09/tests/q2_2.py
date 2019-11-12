test = {
  'name': 'q2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(we_ssa_happiness.labels)
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> we_ssa_happiness.num_rows
          59
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(we_ssa_happiness.group("Region").column("Region")) == set(["Western Europe", "Sub-Saharan Africa"])
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

test = {
  'name': 'q2_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> lower_bound > 80
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> upper_bound < 120
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> lower_bound > 80 and upper_bound < 101
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

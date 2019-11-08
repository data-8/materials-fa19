test = {
  'name': 'q1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(lower_bound) in set([float, np.float32, np.float64])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(upper_bound) in set([float, np.float32, np.float64])
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

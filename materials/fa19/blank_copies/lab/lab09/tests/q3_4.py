test = {
  'name': 'q3_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(bootstrap_ci_left_end) in set([float, np.float32, np.float64])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(bootstrap_ci_right_end) in set([float, np.float32, np.float64])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 7.4 <= bootstrap_ci_left_end <= 7.5 and 7.5 <= bootstrap_ci_right_end <= 7.6
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

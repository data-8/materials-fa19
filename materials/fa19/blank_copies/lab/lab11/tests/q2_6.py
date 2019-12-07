test = {
  'name': 'q2_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(faithful_statements) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> faithful_statements.item(0) == 3
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

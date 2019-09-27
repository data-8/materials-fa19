test = {
  'name': 'q1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> exercise_time.num_rows
          31
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> exercise_time.take(range(5))
          Day (in January) | yoga | walking | sprinting | volleyball | Total Exercise Time
          1                | 50   | 0       | 0         | 0          | 50
          2                | 0    | 65      | 0         | 65         | 130
          3                | 50   | 70      | 0         | 0          | 120
          4                | 0    | 0       | 0         | 75         | 75
          5                | 0    | 0       | 0         | 0          | 0
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

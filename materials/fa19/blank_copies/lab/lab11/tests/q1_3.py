test = {
  'name': 'q1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(fit_line(Table().with_columns('x', make_array(0, 1), 'y', make_array(1, 3)))) == 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(fit_line(faithful), np.array([ 5.43881507 ,  56.64896878]))
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

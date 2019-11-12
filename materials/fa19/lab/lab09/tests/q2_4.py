test = {
  'name': 'q2_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # The order of the "Happiness Score" column should not change in your permuatations;
          >>> sample = shuffle_regions();
          >>> all(sample.column("Happiness Score") == we_ssa_happiness.column("Happiness Score"))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The order of the "Region" column should be shuffled in your permuatations;
          >>> sample = shuffle_regions();
          >>> not all(sample.column("Region") == we_ssa_happiness.column("Region"))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The number of times that each region shows up in your permuatation should not be different than in the original table;
          >>> grouped_original = we_ssa_happiness.group("Region");
          >>> grouped_sample = shuffle_regions().group("Region");
          >>> all(grouped_original.column("count") == grouped_sample.column("count"))
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

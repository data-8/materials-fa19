test = {
  'name': 'q3_2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(0, 5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(0, 11)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(1, 5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(1, 11)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(2, 5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(2, 11)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(3, 5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(3, 11)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(4, 5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(4, 11)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(5, 5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(5, 11)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(6, 5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(6, 11)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(7, 5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(7, 11)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(8, 5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(8, 11)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(9, 5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(9, 11)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(10, 5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_20.row(r)
          ...     return classify(t, train_20, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:k])).most_common(1)[0][0];
          >>> check(10, 11)
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

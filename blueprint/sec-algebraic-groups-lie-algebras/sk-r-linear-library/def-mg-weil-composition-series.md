+++
id = "def-mg-weil-composition-series"
kind = "definition"
title = "Composition series of a Weil representation"
lean = ["Representation.CompositionSeries", "Representation.CompositionSeries.factor"]
order = 3752
uses = ["d-monodromy"]
+++
Let $V$ be a Weil representation of a degree datum ([d-monodromy]),
that is, a finite-dimensional representation of $W$.
A *composition series* is a finite filtration by Weil-stable
subspaces

$$
0=V_0\subsetneq V_1\subsetneq\cdots\subsetneq V_t=V
$$

such that every quotient $V_i/V_{i-1}$ is a *simple Weil
representation*: it is nonzero and has no nonzero proper Weil-stable
subspace. These
quotients, with repetitions retained, are the *composition factors*
of the chosen series.

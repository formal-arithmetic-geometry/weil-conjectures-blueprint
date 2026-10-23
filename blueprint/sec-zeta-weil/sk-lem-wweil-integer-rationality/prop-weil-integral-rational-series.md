+++
id = "prop-weil-integral-rational-series"
kind = "theorem"
title = "Normalized integral fraction for an integral rational series"
lean = ["PowerSeries.existsUnique_isNormalizedIntegralFraction"]
order = 4110
tags = ["latex:proposition"]
uses = ["def-weil-normalized-integral-fraction", "lem-weil-finite-coordinate-detection", "prop-weil-rationality-criterion"]
+++
Let $Z(T)\in1+T\mathbf Z[[T]]$ be rational over $\mathbf Q$.
Then $Z$ has a unique
normalized reduced
integral presentation: there are unique $A,B\in\mathbf Z[T]$
such that $A(0)=B(0)=1$, $\gcd(A,B)=1$ in $\mathbf Q[T]$,
and $BZ=A$.

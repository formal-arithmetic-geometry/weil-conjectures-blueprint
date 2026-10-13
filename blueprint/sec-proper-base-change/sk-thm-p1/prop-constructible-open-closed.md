+++
id = "prop-constructible-open-closed"
kind = "theorem"
title = "Open–closed criterion"
order = 1228
lean = ["AlgebraicGeometry.Scheme.Stratification.openClosed", "AlgebraicGeometry.Scheme.isConstructibleSheaf_iff_upperStar"]
tags = ["latex:proposition"]
uses = ["def-constructible-constructible", "def-constructible-stratification"]
+++
Let $j\colon U\to X$ be an open immersion and $i\colon Z\to X$ a closed
immersion whose range is the complement of the range of $j$. Stratifications
of $U$ and of $Z$ concatenate to a stratification of $X$, whose strata are the
images of the strata of $U$ and of $Z$. A sheaf $\mathcal F\in\shv{\et X}$
is constructible if and only if $j^*\mathcal F$ and $i^*\mathcal F$ are
constructible.

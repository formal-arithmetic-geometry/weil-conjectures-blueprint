+++
id = "sk-thm-smooth-base-change"
kind = "theorem"
title = "Smooth base change"
order = 1471
uses = ["sk-def-bc", "sk-def-smooth", "sk-prop-input-spreading", "sk-prop-input-torsors"]
lean = ["AlgebraicGeometry.Etale.isIso_baseChangeHomologyMap_of_smooth"]
tags = ["sketch"]
+++
Let

$$
\begin{array}{ccc}
X & \xleftarrow{\;h\;} & Y\\
f\downarrow & & \downarrow e\\
S & \xleftarrow{\;g\;} & T
\end{array}
$$

be Cartesian with $f$ smooth and $g$ quasi-compact
quasi-separated, and let $\Lambda$ be a commutative ring. Then for
every $q$ and every sheaf $\mathcal F$ of $\Lambda$-modules on $T_{\Et}$
all of whose geometric stalks are torsion of orders invertible on $S$
(each element killed by a positive integer invertible on $S$),

$$
f^{-1}R^qg_*\mathcal F\ \xrightarrow{\ \sim\ }\ R^qh_*e^{-1}\mathcal F,
$$

the map being the base-change map of [sk-def-bc].

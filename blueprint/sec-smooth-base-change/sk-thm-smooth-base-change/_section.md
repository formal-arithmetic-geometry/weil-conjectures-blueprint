+++
id = "sk-thm-smooth-base-change"
kind = "theorem"
title = "Smooth base change for classical torsion sheaves"
order = 1425
uses = ["sk-def-bc", "sk-def-smooth", "sk-prop-input-spreading", "sk-prop-input-torsors", "sk-lem-sbc-exchange-compatibility", "sk-thm-pe-direct-image-comparison", "sk-prop-deg0", "sk-lem-universal-datum", "sk-thm-vanishing", "sk-lem-induction", "sk-prop-normal-form"]
lean = ["AlgebraicGeometry.Etale.isIso_baseChangeHomologyMap_of_smooth"]
tags = ["sketch"]
+++
Consider a cartesian square

$$
\begin{array}{ccc}
X' & \xrightarrow{\ u\ } & X\\
{\scriptstyle f'}\downarrow & & \downarrow{\scriptstyle f}\\
Y' & \xrightarrow{\ g\ } & Y
\end{array}
$$

and the exchange map $\operatorname{Ex}_{g,f}:g^*Rf_*\to Rf'_*u^*$ of
[sk-lem-sbc-exchange-compatibility].
Suppose $g$ is smooth and $f$ is
quasi-compact and quasi-separated. Let $F$ be a classical torsion
abelian sheaf on $X_{\mathrm{pro\acute et}}$ which is the filtered union of its
subsheaves $F[n]$ for the positive integers $n$ invertible on $Y$.
Then for every $q\geq0$ the degree-$q$ exchange map induced by
$\operatorname{Ex}_{g,f}$, a morphism of abelian sheaves on $Y'_{\mathrm{pro\acute et}}$,

$$
 g^*R^qf_*F\longrightarrow R^qf'_*u^*F
$$

is an isomorphism.

*Complement.* In the notation of [sk-def-bc], where the smooth morphism is called $f$ and the
qcqs one $g$, let

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

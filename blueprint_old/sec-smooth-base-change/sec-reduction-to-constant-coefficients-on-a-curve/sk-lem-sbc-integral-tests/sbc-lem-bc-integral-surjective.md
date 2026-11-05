+++
id = "sbc-lem-bc-integral-surjective"
kind = "lemma"
title = "Integral surjective base change on the target"
lean = ["AlgebraicGeometry.Etale.nonempty_arrowIso_baseChangeHomologyMap_lowerStar", "AlgebraicGeometry.Etale.isIso_baseChangeHomologyMap_of_isIntegralHom_of_surjective", "AlgebraicGeometry.Etale.mono_unit_app_of_surjective"]
order = 2174
uses = ["lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-five-lemma-transfer", "sbc-def-base-change-map", "sbc-def-base-change-property", "sbc-lem-bc-injectivity", "sbc-lem-integral-etale-direct-image-exact"]
+++
With $f:X\to S$ and $n$ as in [sbc-def-base-change-property] assume for
some $q\geq1$ that $\mathrm{BC}(f,n,q-1)$ holds universally (in the
single degree $q-1$).
Consider commutative
diagrams

$$
\begin{array}{ccccccc}
X & \xleftarrow{\;\;} & X' & \xleftarrow{\;\;} & Y & \xleftarrow{\pi'} & Y'\\
f\big\downarrow & & \big\downarrow f' & & \big\downarrow e & &
\big\downarrow e'\\
S & \xleftarrow{\;\;} & S' & \xleftarrow{\;\;} & T
\xleftarrow{\;\pi\;} & T' &
\end{array}
\quad\text{and}\quad
\begin{array}{ccccc}
X' & &\xrightarrow{h'=h\circ\pi'}& &Y'\\
f'\big\downarrow & & & & \big\downarrow e'\\
S' & &\xrightarrow{g'=g\circ\pi}& &T'
\end{array}
$$

where all squares are Cartesian, $g$ is quasi-compact and
quasi-separated, and $\pi:T'\to T$ is integral surjective. Let
$\mathcal F$ be an abelian sheaf on $T_{\Et}$ annihilated by $n$ and set
$\mathcal F'=\pi^{-1}\mathcal F$. If

$$
f'^{-1}R^qg'_*\mathcal F'\xrightarrow{\ \sim\ }
R^qh'_*(e')^{-1}\mathcal F'
$$

is an isomorphism, then
$f'^{-1}R^qg_*\mathcal F\to R^qh_*e^{-1}\mathcal F$ is an isomorphism.

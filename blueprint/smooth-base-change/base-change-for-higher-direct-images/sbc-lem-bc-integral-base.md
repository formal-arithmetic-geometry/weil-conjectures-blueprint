+++
id = "sbc-lem-bc-integral-base"
kind = "lemma"
title = "Integral base change on the source"
order = 2780
uses = ["lemma-weil-pbc-finite-direct-image-exact", "sbc-def-base-change-map", "sbc-def-base-change-property", "sbc-lem-integral-etale-direct-image-exact"]
+++
With $f:X\to S$ and $n$ as in [sbc-def-base-change-property] assume for
some $q\geq1$ that $\mathrm{BC}(f,n,q-1)$ holds. Consider commutative
diagrams

$$
\begin{array}{ccccccc}
X & \xleftarrow{\;\;} & X' & \xleftarrow{\pi'} & X'' & &
Y\\
f\big\downarrow & & \big\downarrow f' & & \big\downarrow f'' & &
\big\downarrow e\\
S & \xleftarrow{\;\;} & S' & \xleftarrow{\;\pi\;} & S'' & &
T
\end{array}
$$

and the diagram with the outer
$h=h'\circ\pi''$, $g=g'\circ\pi$ (as horizontal composites), all squares
Cartesian, $g'$ quasi-compact and quasi-separated, and $\pi$ integral.
Let $\mathcal F$ be an abelian sheaf on $T_{\Et}$ annihilated by $n$.
If

$$
f'^{-1}R^qg_*\mathcal F\xrightarrow{\ \sim\ }R^qh_*e^{-1}\mathcal F
$$

is an isomorphism, then
$f''^{-1}R^qg'_*\mathcal F\to R^qh'_*e^{-1}\mathcal F$ is an
isomorphism.
(*Stacks Project, Lemma 59.88.4, [Tag `0F05`](https://stacks.math.columbia.edu/tag/0F05).*)

## Proof

Since $\pi$ and $\pi'$ are integral, $\pi_*$ and $\pi'_*$ are exact
by [sbc-lem-integral-etale-direct-image-exact] (finite case
[lemma-weil-pbc-finite-direct-image-exact]) and
$(f')^{-1}\pi_*=\pi'_*(f'')^{-1}$, so
$\pi'_*(f'')^{-1}R^qg'_*\mathcal F=(f')^{-1}R^qg_*\mathcal F$ and
$\pi'_*R^qh'_*e^{-1}\mathcal F=R^qh_*e^{-1}\mathcal F$; hence the
assumption says that the map for $f''$ becomes an isomorphism after
$\pi'_*$, and since $\pi'_*$ is exact and faithful for integral
surjective (in particular surjective, hence stalkwise injective) maps
it is an isomorphism.

+++
id = "lemma-change-coefficients--1"
kind = "lemma"
title = "Base change under a flat change of coefficients"
name_showing = false
order = 698001
aliases = ["bp-r209-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_map_exchangeRight_derivedExtendScalars", "AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_boundedConstructibleBaseChange_extendScalars"]
uses = ["definition-change-of-coefficients-maps", "definition-pro-etale-base-change-map", "definition-constructible-sheaves"]
+++
Let $a:\Lambda\to\Lambda'$ be a map of commutative condensed rings such
that extension of scalars along $\Lambda_Z\to\Lambda'_Z$ is exact for
every scheme $Z$. Write $T_Z(M)=M_{\Lambda'}$ for derived extension of
scalars. Consider a commutative square

$$
\begin{CD}
X' @>{g'}>> X\\
@V{f'}VV @VV{f}V\\
Y' @>{g}>> Y.
\end{CD}
$$

Let $\alpha_h:(h^*M)_{\Lambda'}\simeq h^*(M_{\Lambda'})$ be the
pullback comparison of [definition-change-of-coefficients-maps], and let
$\rho_h:(Rh_*M)_{\Lambda'}\to Rh_*(M_{\Lambda'})$ be its adjoint
transpose. Assume that the comparisons $\alpha_h$ are compatible with
composition of pullbacks: for every pair $p:U\to V$, $q:V\to W$, the
comparison for $q\circ p$ agrees with the composite of those for $q$ and
$p$ under $(q\circ p)^*\simeq p^*q^*$.

For $K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$, assume that
$\rho_f(K)$ and $\rho_{f'}(g'^*K)$ are isomorphisms. Then the arrows

$$
T_{Y'}(g^*Rf_*K)\longrightarrow T_{Y'}(Rf'_*g'^*K),
\qquad
g^*Rf_*(T_XK)\longrightarrow Rf'_*g'^*(T_XK)
$$

are isomorphic as objects of the arrow category of
$D(Y'_{\mathrm{pro}\acute{e}t},\Lambda')$. The first arrow is $T_{Y'}$
applied to the base change map of [definition-pro-etale-base-change-map],
and the second is the base change map with coefficients $\Lambda'$.

There is also a bounded constructible version. Fix a prime $\ell$ and a
field $k$ of characteristic $p>0$, with $p\ne\ell$, and suppose that the
square consists of separated schemes of finite type over $k$ and
$k$-morphisms. Here $\Dbc(Z,\Lambda)$ denotes the full subcategory of
bounded complexes whose cohomology sheaves admit a finite stratification
on whose strata they are pro-étale locally finitely presented over the
coefficient sheaf. Assume that $Rf_*$ and $Rf'_*$ preserve these
subcategories for both coefficient rings, and that $T_X$ and $T_{Y'}$
preserve them. Take the base change maps on these subcategories to be the
exchange morphisms of the restricted adjunctions and pullback comparison.
Then, for $K\in\Dbc(X,\Lambda)$ satisfying the two assumptions on
$\rho$, the same two arrows are isomorphic in the arrow category of
$\Dbc(Y',\Lambda')$.

+++
id = "lemma-change-coefficients-internal-hom--1"
kind = "lemma"
title = "Internal Hom for reduction and field coefficients"
name_showing = false
order = 642001
aliases = ["bp-r196-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_ihomComparison_leftDerivedIntegersModPowReduction", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_ihomComparison_constructibleExtendScalars", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_ihomComparison_boundedConstructibleExtendScalars", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_ihomComparison_constructibleToPadicAlgCl", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_ihomComparison_boundedConstructibleIntegersToPadicAlgCl"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves", "definition-change-of-coefficients-maps"]
+++
Let $\ell$ be a prime. The comparison of
Definition [definition-change-of-coefficients-maps](6) is an isomorphism
in the following cases.

1. Let $E\subset\overline{\mathbf Q}_\ell$ be a subfield, let $X$ be any
   scheme, and let $n\geq 0$. For arbitrary
   $K,L\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$, the map
   $$
   \cHom(K,L)_{\mathcal O_E/\ell^n}
   \longrightarrow
   \cHom(K_{\mathcal O_E/\ell^n},L_{\mathcal O_E/\ell^n})
   $$
   is an isomorphism. Here the coefficient sheaves are pulled back from
   the corresponding condensed rings. There is no boundedness or
   constructibility hypothesis on $K$ or $L$, and $E$ need not be finite
   over $\mathbf Q_\ell$.
2. Let $k$ be a field of positive characteristic different from $\ell$,
   let $X$ be separated of finite type over $k$, and let
   $E\subset F\subset\overline{\mathbf Q}_\ell$ be finite extensions of
   $\mathbf Q_\ell$. For any of the maps
   $$
   E\longrightarrow F,\qquad
   \mathcal O_E\longrightarrow E,\qquad
   E\longrightarrow\overline{\mathbf Q}_\ell,\qquad
   \mathcal O_E\longrightarrow\overline{\mathbf Q}_\ell
   $$
   and all $K,L\in\Dbc(X,\Lambda)$, the map
   $$
   \cHom(K,L)_{\Lambda'}
   \longrightarrow\cHom(K_{\Lambda'},L_{\Lambda'})
   $$
   is an isomorphism.

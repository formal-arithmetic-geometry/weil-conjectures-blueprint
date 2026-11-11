+++
id = "lemma-frobenius-fixed-scheme--3"
kind = "lemma"
title = "Reducedness"
order = 960006
aliases = ["bp-r292-3"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.IsModelFrobenius.exists_isOpenImmersion_rationalPoint_of_isLimit", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.FixedLocus.isReduced"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "definition-correspondence--2", "definition-correspondence--3", "definition-frobenius-correspondences-their-operators--1", "definition-frobenius-correspondences-their-operators--5"]
+++
Let $k_0=\Fq$, let $k$ be an algebraically closed extension of $k_0$, and
let $X=X_0\times_{k_0}k$ be locally of finite type over $k$. For the
Frobenius $\Phi_X$ and $m\geq1$, let $T\to X$ be any equalizer
of $\id_X$ and $\Phi_X^m$ over $s=\Spec k$, such as $\Fix(\Phi_X^m)$.

For every point $z\in T$, there is a $k$-rational open immersion
$s\to T$ with image $\{z\}$. In particular, $T$ is reduced.

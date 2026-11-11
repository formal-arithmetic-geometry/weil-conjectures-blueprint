+++
id = "lemma-frobenius-fixed-scheme--1"
kind = "lemma"
title = "Description of the fixed scheme"
order = 960002
aliases = ["bp-r292-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.IsModelFrobenius.fixedPointEquiv", "AlgebraicGeometry.ProEtale.CondensedRing.IsModelFrobenius.nonempty_isLimit_fixedPointsFork", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.FixedLocus.isoSigmaPointFixedFieldPoints"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "definition-correspondence--2", "definition-correspondence--3", "definition-frobenius-correspondences-their-operators--1", "definition-frobenius-correspondences-their-operators--5"]
+++
Let $k_0=\Fq$, let $k$ be an algebraically closed extension of $k_0$, and
let $X=X_0\times_{k_0}k$ be locally of finite type over $k$. Write
$s=\Spec k$, let $\Phi_X$ be the model Frobenius, and let $m\geq1$.
Put

$$
I_m=\{x:s\to X\text{ over }k\mid \Phi_X^m\circ x=x\}.
$$

The morphism $\coprod_{x\in I_m}s\to X$ given on each component by $x$
is an equalizer of $\id_X$ and $\Phi_X^m$ over $s$.

If $p:X\to X_0$ is the projection and $\sigma(a)=a^q$ on $k$, then
$x\mapsto p\circ x$ identifies $I_m$ with the $k_0$-morphisms
$g:s\to X_0$ satisfying $g\circ\Spec(\sigma^m)=g$. These are the
$\mathbf F_{q^m}$-rational points of $X_0$, so

$$
\Fix(\Phi_X^m)\simeq\coprod_{x\in X_0(\mathbf F_{q^m})}s.
$$

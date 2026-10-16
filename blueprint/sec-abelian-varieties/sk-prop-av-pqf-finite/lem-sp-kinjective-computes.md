+++
id = "lem-sp-kinjective-computes"
kind = "lemma"
title = "K-injective resolutions compute derived functors"
lean = ["CochainComplex.KInjectiveResolution.rightDerivedHomologyIsoRightDerived", "CochainComplex.KInjectiveResolution.homotopyEquiv", "CochainComplex.KInjectiveResolution.rightDerivedIso", "CochainComplex.KInjectiveResolution.rightDerivedMap", "CochainComplex.KInjectiveResolution.shift", "CochainComplex.KInjectiveResolution.rightDerivedShiftIso", "CochainComplex.KInjectiveResolution.rightDerivedShiftIso'", "CategoryTheory.InjectiveResolution.kInjectiveResolution"]
order = 525
uses = ["def-sp-grothendieck-abelian", "def-sp-injective-resolutions", "def-sp-kinjective-bridge", "def-sp-left-exact-additive"]
+++
Let $v:\mathcal A\to\mathcal B$ be a left exact additive
[def-sp-left-exact-additive] functor between Grothendieck abelian categories
[def-sp-grothendieck-abelian] and let $K\in\operatorname{Ch}^+(\mathcal A)$.
Then:

1. **(Well-definedness.)** Any two K-injective resolutions
[def-sp-kinjective-bridge] $f:K\to I$ and $g:K\to J$ are homotopy equivalent
under $K$, by a homotopy equivalence unique up to homotopy. Hence
$v(I)\cong v(J)$ by a canonical isomorphism in the homotopy category, the
object $RvK$ of [def-sp-kinjective-bridge] is well defined up to canonical
isomorphism, and it is functorial in $K$.

2. **(Agreement on objects.)** A bounded-below complex of injective objects
is K-injective. In particular an injective resolution
[def-sp-injective-resolutions] $X\to I^\bullet$ of an object $X$ is a
K-injective resolution of $X[0]$, and

$$
 \mathcal H^p\bigl(Rv(X[0])\bigr)\cong R^pv(X)
$$

for every $p$, the right-hand side being the derived functor of
[def-sp-left-exact-additive].

3. **(Shift.)** $Rv(K[n])\cong(RvK)[n]$ for every $n\in\mathbb Z$.

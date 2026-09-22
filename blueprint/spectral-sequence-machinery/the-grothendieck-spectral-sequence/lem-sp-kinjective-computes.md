+++
id = "lem-sp-kinjective-computes"
kind = "lemma"
title = "K-injective resolutions compute derived functors"
order = 1740
lean = ["CategoryTheory.Functor.rightDerived_of_kInjectiveResolution"]
uses = ["def-sp-left-exact-additive", "def-sp-kinjective-bridge", "def-sp-grothendieck-abelian"]
+++
Let $v$ be a left exact additive [def-sp-left-exact-additive] functor and let
$K\to I$ be a K-injective resolution [def-sp-kinjective-bridge] of a
bounded-below complex $K$. Then

$$
 RvK\cong v(I),
$$

compatibly with the injective resolution
[def-sp-left-exact-additive] computation of the derived functors and with the
Cartan--Eilenberg computation below.

## Proof

In a Grothendieck category every bounded-below complex has a K-injective
resolution ([def-sp-kinjective-bridge]), and the derived functor of a left
exact additive functor is the functor applied to the K-injective resolution
([def-sp-left-exact-additive]): the two routes agree because K-injective
resolutions and injective resolutions of bounded below complexes compute the
same derived functor (a Cartan--Eilenberg resolution as in
[thm-sp-if-e1] refines both, cf. [def-sp-truncation-couple]).

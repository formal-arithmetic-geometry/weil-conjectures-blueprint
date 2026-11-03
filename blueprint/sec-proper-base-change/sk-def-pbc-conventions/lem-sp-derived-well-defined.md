+++
id = "lem-sp-derived-well-defined"
kind = "lemma"
title = "Well-definedness of right derived functors"
order = 1358
lean = ["CategoryTheory.InjectiveResolution.isoRightDerivedObj", "CategoryTheory.Functor.rightDerivedZeroIsoSelf", "CategoryTheory.IsGrothendieckAbelian.enoughInjectives"]
uses = ["def-sp-grothendieck-abelian", "def-sp-injective-resolutions", "def-sp-left-exact-additive", "lem-sp-grothendieck-enough-injectives"]
+++
Let $v$ be a left exact additive [def-sp-left-exact-additive] functor and let
$X$ be an object of a Grothendieck abelian category
[def-sp-grothendieck-abelian]. Then $R^nv(X)$ is well defined, independent of
the chosen injective resolution [def-sp-injective-resolutions], and
$R^0v(X)\cong v(X)$ naturally in $X$.

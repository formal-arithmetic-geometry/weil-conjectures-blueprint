+++
id = "lem-a1-mixed-direct-summand"
kind = "lemma"
title = "Mixedness passes to subobjects, quotients, extensions and direct summands"
lean = ["AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.of_shortExact", "AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.of_retract", "FrobeniusModule.HasWeightsAtMost.of_injective", "FrobeniusModule.HasWeightsAtMost.of_surjective", "FrobeniusModule.HasWeightsAtMost.of_exact"]
order = 3988
uses = ["def-weil-frobenius-module-weights", "def-weil-punctual-weights", "def-weil-weil-sheaf-complex", "lem-a1-extension-bounds", "lem-a1-subquotient-extension-bounds", "sk-def-sf-weil-complexes", "sk-lem-coefficient-heart"]
+++
Fix a field embedding $\iota:\Qlb\hookrightarrow\mathbf C$ and $w\in\mathbf R$, and let
$Y_0$ be a finite-type $k_0$-scheme. In the abelian category of
constructible $\Qlb$-Weil sheaves on $Y_0$ ([def-weil-weil-sheaf-complex]),
that is, of pairs $(\mathcal G,\phi)$ with $\mathcal G\in\Cons(Y,\Qlb)$
([sk-lem-coefficient-heart]) and $\phi$ a Weil structure
([sk-def-sf-weil-complexes]):

1. every Weil subsheaf and every Weil quotient sheaf of a sheaf that is
   $\iota$-mixed of weights at most $w$ in the sense of
   [def-weil-punctual-weights] is $\iota$-mixed of weights at most $w$;
2. if $0\to\mathcal G'\to\mathcal G\to\mathcal G''\to0$ is an exact
   sequence of constructible Weil sheaves and $\mathcal G'$,
   $\mathcal G''$ are $\iota$-mixed of weights at most $w$, then so is
   $\mathcal G$;
3. in particular, a direct summand of an $\iota$-mixed constructible
   Weil sheaf of weights at most $w$ is $\iota$-mixed of weights at most
   $w$.

The analogous statements hold for Frobenius modules in the sense of
[def-weil-frobenius-module-weights].

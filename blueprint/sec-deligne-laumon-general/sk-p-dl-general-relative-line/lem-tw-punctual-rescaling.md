+++
id = "lem-tw-punctual-rescaling"
kind = "lemma"
title = "Punctual purity on a closed fibre"
order = 3180
lean = ["AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.upperStar"]
uses = ["def-weil-finite-field-fiber", "def-weil-punctual-weights", "def-weil-scheme-morphism-properties", "def-weil-weil-sheaf-complex", "sk-lem-coefficient-heart"]
+++
Fix the finite-field datum $(p,a,q,k_0,k)$. Let $\varphi:X'_0\to X_0$
be a morphism of $k_0$-schemes and let $\mathcal F$ be a constructible $\Qlb$-Weil sheaf on
$X_0$ (an object of $\Cons(X,\Qlb)$ [sk-lem-coefficient-heart] with a Weil
structure [def-weil-weil-sheaf-complex]), punctually $\iota$-pure of weight $w$. Then the pullback
$\varphi^*\mathcal F$, with its induced Weil structure, is punctually
$\iota$-pure of weight $w$.

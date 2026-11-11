+++
id = "theorem-proper-pushforward-lefschetz-verdier--1"
kind = "theorem"
title = "Proper pushforward and Lefschetz–Verdier (1)"
name_showing = false
order = 926001
aliases = ["bp-r281-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.traceClassPushforward_eq"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "lemma-constructible-sheaves--8", "theorem-f-shriek-ell-adic-coefficients--5", "proposition-six-operations-dctf--14", "definition-correspondence--2", "definition-correspondence--3", "definition-trace-class-local-terms--1", "definition-pushforward-correspondence--1", "definition-pushforward-correspondence--2", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
+++
Let $f:X\to Y$ and $g:C\to C'$ be proper, and let
$c'=(c'_1,c'_2):C'\to Y\times Y$ satisfy $c'_ig=fc_i$. Set $K'=Rf_*K$, and
let $u'$ be the pushforward of $u$ to $(Y,K')$ of
Definition [definition-pushforward-correspondence]. With
the induced proper map $h:\Fix(c)\to \Fix(c')$ one has

$$
\operatorname{Tr}_{c'}(u')=h_*\operatorname{Tr}_c(u).
$$

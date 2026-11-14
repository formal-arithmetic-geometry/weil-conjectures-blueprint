+++
id = "theorem-proper-pushforward-lefschetz-verdier"
kind = "theorem"
title = "Proper pushforward and Lefschetz–Verdier"
order = 926
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.trace_globalOperator_eq_sum_localTerm", "AlgebraicGeometry.ProEtale.CondensedRing.BorelMooreSection.integral_eq_sum_localTerm"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-inverse-image-tensor-product", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "definition-categorical-trace", "definition-correspondence", "definition-trace-class-local-terms", "definition-action-correspondence", "definition-pushforward-correspondence", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $f:X\to Y$ and $g:C\to C'$ be proper, and let
$c'=(c'_1,c'_2):C'\to Y\times Y$ satisfy $c'_ig=fc_i$. Set $K'=Rf_*K$, and
let $u'$ be the pushforward of $u$ to $(Y,K')$ of
Definition [definition-pushforward-correspondence]. With
the induced proper map $h:\Fix(c)\to \Fix(c')$ one has

$$
\operatorname{Tr}_{c'}(u')=h_*\operatorname{Tr}_c(u).
$$

If $X$ and $C$ are proper over $k$, this gives

$$
\operatorname{tr}_A(T_c(u)\mid R\Gamma(X,K))
=\int_{\Fix(c)}\operatorname{Tr}_c(u)
=\sum_B\operatorname{LT}_B(u),
$$

for any finite open-and-closed decomposition $\Fix(c)=\coprod B$.

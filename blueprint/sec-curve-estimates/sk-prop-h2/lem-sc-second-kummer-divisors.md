+++
id = "lem-sc-second-kummer-divisors"
kind = "lemma"
title = "Second Kummer cohomology of a curve"
order = 991
uses = ["def-sc-curves", "def-sc-kummer-sequence", "def-sc-picard-group", "def-weil-pbc-etale-cohomology", "lem-sc-brauer-zero-all-curves", "lem-sc-divisor-class-curve", "lem-sc-function-field-cd-one", "lem-sc-generic-kummer-residues", "lem-sc-h1-gm-pic", "lem-sc-kummer-les", "lem-sc-smooth-normal", "thm-sp-grothendieck"]
+++
Let $C$ be a curve over algebraically closed $k$ in the sense of
[def-sc-curves]. It may be singular, non-reduced, disconnected or
have zero-dimensional components. Let $n>0$ be invertible in $k$.
Then

$$
H^2(C,\mu_n)\simeq\operatorname{Pic}(C)/n,
$$

where $\mu_n$, the Picard group, and cohomology are as in
[def-sc-kummer-sequence], [def-sc-picard-group], [def-weil-pbc-etale-cohomology].
The isomorphism is induced by the coboundary of the Kummer sequence,
$\operatorname{Pic}(C)=H^1(C,\mathbf G_m)\to H^2(C,\mu_n)$
([lem-sc-h1-gm-pic]). In particular $H^2(C_{\Et},\mathbf G_m)=0$
for every such $C$ ([lem-sc-brauer-zero-all-curves]).

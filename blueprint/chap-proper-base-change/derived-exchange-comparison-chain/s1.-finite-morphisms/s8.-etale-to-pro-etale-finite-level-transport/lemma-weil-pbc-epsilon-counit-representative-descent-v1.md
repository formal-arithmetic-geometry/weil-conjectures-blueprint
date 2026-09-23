+++
id = "lemma-weil-pbc-epsilon-counit-representative-descent-v1"
kind = "lemma"
title = "Representative descent for the comparison counit"
order = 1685
uses = ["def-weil-pbc-epsilon-factorization-index-v1", "def-weil-pbc-epsilon-unit-counit", "lemma-weil-pbc-epsilon-geometric-morphism-construction-v1"]
+++
The rule $(W\xrightarrow a\iota_XU,s)\mapsto G(a)(s)$ respects the
left-Kan-extension relations, restriction in $W$, and local equality, hence
factors uniquely through pro-etale sheafification.

## Proof

If $h:U'\to U$ is a transition and $a=\iota_X(h)a'$, then
functoriality of $G$ gives

$$
G(a')G(\iota_Xh)(s)=G(a)(s),
$$

so the rule is constant on the colimit relation. For $b:W'\to W$, both
restriction before evaluation and evaluation before restriction send
$(a,s)$ to $G(ab)(s)$. If two representatives agree after a pro-etale
cover, their images agree on that cover; the sheaf equalizer for $G$ makes
the images equal. Thus the presheaf map is local and has a unique factor
through sheafification. This factor is precisely the counit attached to the
adjunction constructed above.

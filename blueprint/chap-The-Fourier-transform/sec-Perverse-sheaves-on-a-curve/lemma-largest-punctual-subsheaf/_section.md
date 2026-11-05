+++
id = "lemma-largest-punctual-subsheaf"
kind = "lemma"
title = "The largest punctual subsheaf"
order = 1245
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.eq_zero_of_support_finite", "AlgebraicGeometry.WeilSheaf.support_finite_kernel_unit_app"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-constructible-sheaves", "definition-lisse-sheaves", "definition-punctual-sheaf"]
+++
A lisse sheaf on $C$ has no nonzero punctual subsheaf. Let $F$ be a
constructible sheaf on $C$, let $j:U\hookrightarrow C$ be a dense open
on which $F$ is lisse, and put

$$
F_{\rm p}=\ker(F\longrightarrow j_*j^*F).
$$

Then $F_{\rm p}$ is the largest punctual subsheaf of $F$, and
$F/F_{\rm p}$ has no nonzero punctual subsheaf. In particular,
$F_{\rm p}$ does not depend on $U$.

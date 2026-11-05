+++
id = "lemma-largest-punctual-subsheaf"
kind = "lemma"
title = "The largest punctual subsheaf"
order = 1245
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.eq_zero_of_support_finite", "AlgebraicGeometry.WeilSheaf.support_finite_kernel_unit_app", "AlgebraicGeometry.WeilSheaf.isZero_upperStar_of_isLisse"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness"]
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

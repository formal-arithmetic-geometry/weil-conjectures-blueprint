+++
id = "lemma-largest-punctual-subsheaf"
kind = "lemma"
title = "The largest punctual subsheaf"
order = 1248
lean = ["AlgebraicGeometry.WeilSheaf.support_finite_kernel_unit_app"]
uses = ["lemma-stability", "lemma-schematic-closure-uniqueness"]
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

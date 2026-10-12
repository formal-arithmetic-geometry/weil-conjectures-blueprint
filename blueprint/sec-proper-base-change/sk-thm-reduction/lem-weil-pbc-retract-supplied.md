+++
id = "lem-weil-pbc-retract-supplied"
kind = "lemma"
title = "Retract supplied by a proper surjection"
order = 1187
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let $f:X\to Y$ be proper and surjective, let $I$ be injective on $Y_{\Et}$,
and choose a monomorphism $f^{-1}I\hookrightarrow J$ with $J$ injective on
$X_{\Et}$. The adjoint map

$$
 I\longrightarrow f_*J
$$

of the direct image adjunction is a monomorphism. Injectivity of $I$ supplies
a retraction $f_*J\to I$, so $I$ is a direct summand of $f_*J$.

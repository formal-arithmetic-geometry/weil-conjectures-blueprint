+++
id = "det-l-dl-general-excision"
kind = "lemma"
title = "Open–closed reduction"
lean = ["AlgebraicGeometry.HasDirectImageWeightBound.of_openClosed"]
order = 4072
uses = ["sk-d-real-weights", "sk-r-real-linear", "sk-prop-sf-open-closed-triangle", "sk-prop-sf-cbc", "sk-thm-sf-comp-composition", "lem-zl-morphism-open-closed-reduction"]
+++
Let $f_0:X_0\to Y_0$ be a separated finite-type morphism of
$k_0$-schemes, with $Y_0$ quasi-separated of finite type over $k_0$.

1. *(Source.)* Let $j_0:U_0\hookrightarrow X_0$ be a quasi-compact open
   immersion and $i_0:Z_0\hookrightarrow X_0$ a closed immersion whose
   image is the complement of the image of $j_0$. If the direct-image
   assertion holds for $f_0j_0$ and $f_0i_0$, it holds for $f_0$.
1. *(Target.)* Let $V_0\subseteq Y_0$ be open with closed complement
   $T_0$. If the direct-image assertion holds for the restrictions of
   $f_0$ over $V_0$ and over $T_0$, it holds for $f_0$.

Consequently the assertion can be checked on the pieces of finite
stratifications of source and target built from successive open–closed
decompositions, and on the graded pieces of a finite filtration of the
coefficient sheaf.

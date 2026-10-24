+++
id = "lem-weil-pbc-comparison-injective-acyclicity"
kind = "lemma"
title = "Acyclicity of the pulled-back etale injectives"
order = 1006
lean = ["AlgebraicGeometry.ProEtale.isZero_rightDerived_sectionsFunctor_comparisonUpperStar_obj", "AlgebraicGeometry.Scheme.ProEt.subsingleton_ext_sheafPullback_injective"]
uses = ["def-weil-pbc-cover-cech", "def-weil-pbc-site-comparison-morphism", "lem-weil-pbc-cech-criterion", "lem-weil-pbc-comparison-sections", "lem-weil-pbc-etale-finite-data-descent", "lem-weil-pbc-ind-etale-basis", "lem-weil-pbc-ind-etale-stability", "lem-weil-pbc-proetale-restriction-injectives"]
+++
Let $X$ be a scheme, $\Lambda$ a ring, and $I$ an injective sheaf of
$\Lambda$-modules on $X_{\Et}$. Let $U$ be an object of the affine pro-etale
site of $X$, that is, an object of $X_{\Proet}$ which is a cofiltered limit of
affine etale $X$-schemes. Then the derived functors of evaluation at $U$ vanish
on $\nu_X^*I$ in positive degrees:

$$
 H^q(U,\nu_X^*I)=0\quad(q>0).
$$

By [lem-weil-pbc-proetale-restriction-injectives] this is equivalently
$H^q(U_{\Proet},(\nu_X^*I)|_U)=0$ for $q>0$.

+++
kind  = "proof"
of    = "thm-sf-dual-base-change"
+++
The map $\operatorname{Ex}_!$ is the canonical exchange of
[def-exchange-projection]; that it is an isomorphism is axiom (A2), and
in the concrete setting it is the compact-support base change on
$\Dctf(X,\Lambda)$ for the admissible condensed coefficient ring $\Lambda$
([sk-prop-sf-cbc]). For finite $\Lambda$ this is
[thm-cbc-finite-torsion] and [thm-cbc-finite-level-proetale], with the proper
case supplied by [lemma-weil-pbc-prime-proper-base-change],
[thm-weil-pbc-bounded-below] and [thm-weil-pbc-finite-level-proetale]; for
$\Lambda=E,\Qlb$ it is [sk-thm-sfb-shriek-base-change]; for
$\Lambda=\mathcal O_E$ it combines the proper base change of
[sk-thm-sfb-proper-base-change], valid on $\Dctf$ for every admissible
$\Lambda$, with extension by zero, as recorded in [sk-prop-sf-cbc]. The
smooth case is also given by the smooth-base-change theorem
([sbc-thm-smooth-base-change]). The right adjoint of the composite
$Lg^*Rf_!$ is the composite of the right adjoints in the reverse order,
$Rf^!Rg_*$, and the right adjoint of $Rf'_!Lg'^*$ is $Rg'_*Rf'^!$: both
adjunctions are the ones of [def-sf-datum](A1), and they are the
adjunctions proved in [fix-prop-adjunctions]. An isomorphism of
functors induces an isomorphism between their right adjoints by the
uniqueness of adjoints, and the induced map is the mate of
$\operatorname{Ex}_!$ along the two pasted adjunctions, hence natural and
compatible with pasting by [lem-sf-mate]. The second assertion
substitutes the properness identification $Rg_!=Rg_*$ of
[fix-prop-adjunctions], which is stable under base change because
properness is ([lemma-weil-pbc-prime-proper-base-change] for the square).

+++
kind  = "proof"
of    = "sk-thm-sf-compatibility"
uses = ["sk-def-sf-exchanges", "sk-lem-sf-mate", "sk-prop-cohsm", "sk-prop-sf-cbc", "sk-prop-sf-comp-coherence", "sk-prop-sf-comp-proper", "sk-prop-sf-pf-coherence", "sk-prop-sfb-module-derived-factorization", "sk-thm-sf-comp-composition", "sk-thm-sf-kunneth-relative", "sk-thm-sf-package", "sk-thm-sf-tensor-hom", "sk-thm-sf-verdier-exchange"]
+++
Each clause collects compatibilities proved with the individual
isomorphisms. Clause (1) is [sk-prop-sfb-module-derived-factorization] (4)
for $Lf^*$, [sk-thm-sf-comp-composition] (1) and
[sk-prop-sf-comp-coherence] for $Rf_!$, and [sk-lem-sf-mate] (1) for
$Rf^!$; the isomorphisms for $Rf_*$ and $Rf^!$ are mates of those for
$Lf^*$ and $Rf_!$, and mates of associative and unital isomorphisms are
associative and unital, with units and counits compatible
([sk-lem-sf-mate]). Clause (2) is the identity and pasting equations of the
exchange transformations ([fix-lem-exchanges], under [sk-prop-sf-cbc]),
[sk-prop-sf-comp-proper] for proper $f$, [thm-sf-dual-base-change] for the
mate of $\operatorname{Ex}_!$, which is natural and compatible with pasting
by the mate calculus, and [sk-prop-cohsm] (G12). Clause (3) is
[sk-prop-sf-pf-coherence]. Clause (4) is [sk-thm-sf-tensor-hom],
[sk-thm-sf-verdier-exchange] and the composition clause of
[sk-thm-sf-package] (6); passing to right adjoints in
$\mathbb D_YRf_!\cong Rf_*\mathbb D_X$, with $\mathbb D$ its own adjoint by
biduality, gives [cor-sf-duality-pullback]. Clause (5) is the composition and
base-change compatibility of the orientation in [sk-thm-sf-package] (5).
Clause (6) is [sk-thm-sf-kunneth-relative]. Clause (7) is
[fix-prop-coherence]: the coefficient comparisons preserve tensor
reassociation, evaluation and the units and counits of the adjunctions, so
every map built from them, and every mate of such a map, commutes with
finite reduction and scalar extension, and is Weil-equivariant at field
coefficients.

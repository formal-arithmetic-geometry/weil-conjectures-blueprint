+++
kind = "proof"
of = "proposition-composition-open-restriction-compactifications-f--5"
order = 530014
uses = ["proposition-composition-base-change-rf-shriek", "proposition-extension-zero-restriction-closed-subscheme"]
+++
Let $\mathrm{Ex}_!:v^*Rf_!\xrightarrow\sim Rf_{V,!}u^*$ be compact-support
base change. Under $u_!\dashv u^*$ and $v_!\dashv v^*$, form the mate
$$
\gamma:v_!Rf_{V,!}\longrightarrow Rf_!u_!
$$
of $\mathrm{Ex}_!^{-1}$. The exceptional base-change map is the conjugate
of $\gamma$ under the composite exceptional adjunctions.

Check that $\gamma$ is invertible after restriction to $V$ and to its
closed complement in $Y$. Over $V$, it is a composite of the invertible
open-immersion units and $\mathrm{Ex}_!^{-1}$. On the closed complement,
both sides vanish: extension by zero restricts to zero, and compact-support
base change reduces the other side to restriction to a subscheme disjoint
from $X_V$. These two restrictions detect isomorphisms. Taking conjugates
therefore proves the claim.

The detection step is
`AlgebraicGeometry.Etale.isIso_of_isIso_leftDerivedUpperStar_closedComplement_map`;
the identification with the conjugate uses
`CategoryTheory.iterated_mateEquiv_conjugateEquiv`.

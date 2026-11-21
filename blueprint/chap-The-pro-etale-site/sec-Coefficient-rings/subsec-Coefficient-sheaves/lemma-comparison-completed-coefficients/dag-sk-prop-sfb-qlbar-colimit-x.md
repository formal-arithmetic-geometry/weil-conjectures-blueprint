+++
id = "dag-sk-prop-sfb-qlbar-colimit-x"
kind = "dag-lemma"
title = "Comparison with completed coefficients"
name_showing = false
order = 178505
tags = ["sheaf-dag"]
split_from = "lemma-comparison-completed-coefficients--2"
dag_id = "sk-prop-sfb-qlbar-colimit-x"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.completedCoefficient", "AlgebraicGeometry.ProEtale.completedCoefficientMap", "AlgebraicGeometry.ProEtale.completedConstantRing", "AlgebraicGeometry.ProEtale.completedConstantMap", "AlgebraicGeometry.ProEtale.completedResidue", "AlgebraicGeometry.ProEtale.completedReduction", "AlgebraicGeometry.ProEtale.completedResidueTransition", "AlgebraicGeometry.ProEtale.completedRationalModule", "AlgebraicGeometry.ProEtale.completedPointSubfieldDiagram", "AlgebraicGeometry.ProEtale.completedPointSubfieldCocone", "AlgebraicGeometry.ProEtale.completedSubfieldCocone", "AlgebraicGeometry.ProEtale.completedCondensedIntegral", "AlgebraicGeometry.ProEtale.completedCondensedRational", "AlgebraicGeometry.ProEtale.completedCondensedAlgebraicClosure", "AlgebraicGeometry.ProEtale.completedPadicReduction", "AlgebraicGeometry.ProEtale.completedPadicRationalModule", "AlgebraicGeometry.ProEtale.completedCondensedPadicRational"]
uses = ["dag-def-sfb-finite-upper-star", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $\ell$ be a prime, let $X$ be a scheme, and let $E\subseteq\Qlb$ be a finite extension
of $\mathbf Q_\ell$ with ring of integers $\cO_E$ and uniformizer $\pi_E$. For a condensed
ring $\Lambda$ write $\Lambda_X=p_X^*\Lambda$ for its pullback to $X_{\mathrm{proét}}$
along $p_X\colon\Sh(X_{\mathrm{proét}})\to\Sh(*_{\mathrm{proét}})$
(`sk-def-sfb-pullback-from-point`, `sk-def-sfb-pulled-back-coefficients`). Write
$\cO_{E,X}$, $E_X$ and $\QbarX$ for the pullbacks to $X_{\mathrm{proét}}$ of the condensed
rings $\underline{\cO_E}$, $\underline E$ (`sk-def-sfb-condensed-ring`) and
$\underline{\Qlb}$ (`sk-def-sfb-qlbar-condensed`). There are canonical isomorphisms of
sheaves of rings

$$
\cO_{E,X}\cong\varprojlim_n(\cO_E/\pi_E^n)_X,
\qquad E_X\cong\cO_{E,X}[1/\ell],
\qquad \QbarX\cong\varinjlim_E E_X,
$$

where $(\cO_E/\pi_E^n)_X$ is the constant sheaf, $\cO_{E,X}[1/\ell]$ is the colimit in sheaves of $\cO_{E,X}$-modules of
$\cO_{E,X}\xrightarrow{\ell}\cO_{E,X}\xrightarrow{\ell}\cdots$, equipped with its
localization ring structure, and the last colimit runs
over the filtered poset of finite subextensions $\mathbf Q_\ell\subseteq E\subseteq\Qlb$,
with transition maps induced by the inclusions $\underline E\to\underline F\to\underline{\Qlb}$.
They are compatible with inverse image along every morphism of schemes.

For $E=\mathbf Q_\ell$ this gives
$\mathbf Z_{\ell,X}\simeq\varprojlim_n(\mathbf Z/\ell^n)_X$ and
$\mathbf Q_{\ell,X}\simeq\mathbf Z_{\ell,X}[1/\ell]$.

(SHEAF DAG node `sk-prop-sfb-qlbar-colimit-x`; machine-alignment layer.) Split from [lemma-comparison-completed-coefficients--2]. DAG kind: statement. DAG status: split. Lean names not on master: `AlgebraicGeometry.ProEtale.completedSubfieldInclusion`, `AlgebraicGeometry.ProEtale.completedSubfieldLeg`, `AlgebraicGeometry.ProEtale.completedCondensedPullback`, `AlgebraicGeometry.ProEtale.completedPadicTransition`, `AlgebraicGeometry.ProEtale.completedCondensedPadicIntegral`. Statement dependencies not drawn: `def-sfb-integers-to-subfield-point`, `def-sfb-padic-condensed-ring`, `def-sfb-padic-int-condensed-ring`, `def-sfb-padic-integers-condensed-ring`, `def-sfb-padic-subfield-condensed-ring`, `def-weil-l-adic-numbers`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `det-def-sfb-sheaf-tensor-presheaf`, `lem-coef-grothendieck-locally-presentable`, `lem-sfb-finite-upper-star-braided`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `sk-def-sfb-coefficient-morphisms`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`.

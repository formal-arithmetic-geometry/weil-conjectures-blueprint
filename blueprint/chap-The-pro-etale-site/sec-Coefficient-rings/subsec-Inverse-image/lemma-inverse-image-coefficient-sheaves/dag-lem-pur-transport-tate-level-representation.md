+++
id = "dag-lem-pur-transport-tate-level-representation"
kind = "dag-lemma"
title = "Finite etale representation of one integral Tate level"
name_showing = false
order = 187541
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-transport-tate-level-representation"
dag_kind = "statement"
dag_status = "split"
serial = false
uses = ["dag-def-pur-roots-of-unity-sheaf", "dag-def-pur-condensed-tate-twists"]
+++
Let $Y$ be a scheme, $\ell$ a prime invertible in every residue field of $Y$, and $n\in\mathbf N$. Put $R_Y=p_Y^*\underline{\mathbf Z}_\ell$ and $F_n=R_Y\otimes_{\mathbf Z}\mu_{\ell^n,Y}$, the existing free internal Tate level of [dag-def-pur-condensed-tate-twists], using [dag-def-pur-roots-of-unity-sheaf]. There exists $V\in Y_{\mathrm{proet}}$ such that $V\to Y$ is finite and etale and its lifted representable set sheaf is isomorphic to the underlying set sheaf of $F_n$. This includes $n=0$ and the empty base. No compatibility between distinct levels is asserted.

(SHEAF DAG node `lem-pur-transport-tate-level-representation`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Lean names not on master: `AlgebraicGeometry.ProEtale.PurityTransport.tateLevelRepresentation`.

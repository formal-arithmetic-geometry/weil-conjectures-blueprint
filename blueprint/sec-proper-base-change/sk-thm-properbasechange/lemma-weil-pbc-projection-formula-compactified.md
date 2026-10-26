+++
id = "lemma-weil-pbc-projection-formula-compactified"
kind = "lemma"
title = "Compactified finite-level projection formula"
order = 1959
lean = ["AlgebraicGeometry.Etale.hasProjectionFormulaOfCompactification_of_isDualizable", "AlgebraicGeometry.Etale.projectionMapOfCompactification", "AlgebraicGeometry.Etale.projectionMapOfCompactification_app_app"]
uses = ["def-weil-pbc-projection-compactification", "lemma-weil-pbc-projection-formula-open-piece", "lemma-weil-pbc-projection-formula-proper-piece"]
+++
For a chosen compactification $f=pj$
[def-weil-pbc-projection-compactification], every $E$ in the derived category
of sheaves on $X_{\Et}$ and every dualizable object $Q$ of the derived
category of sheaves on $Y_{\Et}$ (for instance a perfect complex), the ordered
composite

$$
\begin{aligned}
(Rf_!^{(j,p)}E)\otimes^LQ
&=(Rp_*j_!E)\otimes^LQ\\
&\xrightarrow{\pi_{p,j_!E,Q}}
Rp_*(j_!E\otimes^LLp^*Q)\\
&\xrightarrow{Rp_*\theta_j}
Rp_*j_!(E\otimes^LLj^*Lp^*Q)
\cong Rp_*j_!(E\otimes^LLf^*Q)
=Rf_!^{(j,p)}(E\otimes^LLf^*Q)
\end{aligned}
$$

is an isomorphism. Here $\pi_{p,j_!E,Q}$ is the projection map of
[lemma-weil-pbc-projection-formula-proper-piece], $\theta_j$ is the
open-piece isomorphism [lemma-weil-pbc-projection-formula-open-piece] for
$F=Lp^*Q$, and the last isomorphism is $Lj^*Lp^*\cong Lf^*$.

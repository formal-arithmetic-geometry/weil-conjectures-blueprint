+++
id = "sk-prop-sf-pf-reduction"
kind = "section"
title = "Projection formula: compatibility with finite reduction"
order = 1880
uses = ["sk-thm-sf-pf-finite"]
lean = ["AlgebraicGeometry.Etale.isIso_projectionFormulaMap_iff_reduction"]
+++
*Proposition (sketch).*

Let $m\le n$ and let $K\in\Dctf(X,A_{E,n})$, $L\in\Dctf(Y,A_{E,n})$ with
reductions $K_m,L_m$. Then the square comparing
$\operatorname{PF}_{f,K,L}$ and $\operatorname{PF}_{f,K_m,L_m}$ through the
finite-reduction compatibilities of $Rf_!$, $-\otimes^L$ and $Lf^*$ commutes;
hence $\operatorname{PF}_{f,K,L}$ is an isomorphism if and only if
$\operatorname{PF}_{f,K_m,L_m}$ is.

## Proof

Both composites are natural transformations between the same pair of exact
functors of $(K,L)$, and both are isomorphisms where [sk-thm-sf-pf-finite]
applies. On geometric fibres the reduction of the level-$n$ map is the
level-$m$ map composed with the flat comparison, and the level-$n$ map is
characterised as the unique natural transformation of exact functors of $P$
that is the unit identification at $P=A_{E,n}$; reduction carries that
identification to the unit identification at $A_{E,m}$. Geometric stalks are
conservative.

Uses: `\Cref{thm:sf-pf-finite}`, `prop:functor-package`

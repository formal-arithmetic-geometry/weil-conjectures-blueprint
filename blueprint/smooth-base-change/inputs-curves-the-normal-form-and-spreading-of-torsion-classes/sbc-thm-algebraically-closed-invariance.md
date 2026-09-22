+++
id = "sbc-thm-algebraically-closed-invariance"
kind = "theorem"
title = "Invariance under extension of algebraically closed fields"
order = 5139
lean = ["AlgebraicGeometry.Curve.etaleCohomology_baseChange_algClosed_iso"]
+++
Let $k\subseteq k'$ be algebraically closed, let $C$ be a smooth separated
curve over $k$, and let $d\geq1$ be prime to $\operatorname{char}k$. For
every $q\geq0$ the pullback map
$$
H^q(C_{\Et},\mathbf Z/d\mathbf Z)\xrightarrow{\ \sim\ }H^q((C_{k'})_{\Et},\mathbf Z/d\mathbf Z)
$$
is an isomorphism.

(*The Jacobian chapter's base-change invariance for constant sheaves; the
corresponding Stacks statement is Lemma 59.83.12, [Tag
0A5E](https://stacks.math.columbia.edu/tag/0A5E).*)

## Proof

This is the base-change invariance theorem of the Jacobian chapter (applied
with $n=d$), which proves the same assertion for the constant sheaf
$\mathbf F_d$; this is the displayed pullback map by the definition of étale
cohomology.

Unresolved dependencies: thm:sc-constant-invariance, def:weil-pbc-scheme-conventions, def:weil-pbc-etale-cohomology

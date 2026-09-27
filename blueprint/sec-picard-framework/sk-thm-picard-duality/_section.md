+++
id = "sk-thm-picard-duality"
kind = "section"
title = "Serre duality"
order = 683
uses = ["sk-def-av-jacobian", "sk-def-av-pic"]
lean = ["AlgebraicGeometry.Scheme.serreDuality"]
+++
*Theorem (sketch).*

Let $X$ be a smooth proper curve over $k$, of pure dimension
$n\le1$, and $\cF$ a finite locally free $\cO_X$-module. With
$\omega_X=\Omega^n_{X/k}$ the canonical module, the trace pairing is
perfect for every $q$:

$$
H^q(X,\cF)^{\vee}\ \cong\ H^{n-q}\bigl(X,\cF^{\vee}\otimes\omega_X\bigr).
$$

## Proof

(Important) For curves it can be deduced from [sk-thm-picard-pn] and
the adjunction of the canonical sheaf with the Cartier picture of
divisors (the residue sequence). Only the curve case is used in this
blueprint (for Riemann–Roch); the analogue for smooth proper $X$ of
any dimension holds as well but is not needed. Local freeness cannot be
dropped in this form: for the skyscraper $\cF=\kappa(x)$ at a closed
point of $\mathbf P^1$ one has $H^0(\cF)^\vee\neq0$ but
$\cF^\vee=\mathcal Hom(\kappa(x),\cO)=0$; for coherent $\cF$ the right
side must be replaced by $\operatorname{Ext}^{n-q}(\cF,\omega_X)$.

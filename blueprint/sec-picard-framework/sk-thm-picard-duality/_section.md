+++
id = "sk-thm-picard-duality"
kind = "section"
title = "Serre duality"
order = 691
+++
*Theorem (sketch).*

Let $X$ be smooth proper of dimension $n$ over $k$ and $\cF$
coherent on $X$. With $\omega_X=\Omega^n_{X/k}$ the canonical
module, the trace pairing is perfect:

$$
H^q(X,\cF)^{\vee}\ \cong\ H^{n-q}\bigl(X,\cF^{\vee}\otimes\omega_X\bigr).
$$

## Proof

(Important) For smooth projective $X$ the standard proof uses the
local-to-global spectral sequence
$E_2^{p,q}=H^p(X,\mathcal Ext^q(\cF,\omega_X))$; for curves, it can be
deduced from [sk-thm-picard-pn] and the adjunction of the canonical sheaf
with the Cartier picture of divisors (the residue sequence).

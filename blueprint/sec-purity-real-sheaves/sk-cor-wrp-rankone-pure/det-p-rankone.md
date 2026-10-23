+++
id = "det-p-rankone"
kind = "proposition"
title = "Rank-one factorization"
lean = ["SemidirectProduct.eq_finitePart_mul_degreeCharacter", "SemidirectProduct.finitePart_inrOfAddOne", "SemidirectProduct.range_finitePart", "SemidirectProduct.finite_range_finitePart"]
order = 3857
uses = ["d-ab-rankone"]
+++
Let $\chi:W\to A$ be a homomorphism into a commutative group $A$ (for a
rank-one character, $A=E^\times$), and $z=\chi(\gamma)$.
The functions $\chi_z$ and
$\chi_{\mathrm{fin}}$ are homomorphisms, and

$$
\chi(w)=\chi_{\mathrm{fin}}(w)z^{\deg(w)}
$$

for every $w\in W$. Moreover,
$\chi_{\mathrm{fin}}(\gamma)=1$ and
$\chi_{\mathrm{fin}}(W)=\chi(P)$; in particular, if $\chi$ has finite
geometric image, then $\chi_{\mathrm{fin}}$ has finite image.

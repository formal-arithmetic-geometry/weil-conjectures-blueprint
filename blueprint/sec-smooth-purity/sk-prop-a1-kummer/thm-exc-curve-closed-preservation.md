+++
id = "thm-exc-curve-closed-preservation"
kind = "theorem"
title = "Closed points on a smooth curve preserve finite Tor amplitude"
order = 1970
uses = ["def-sc-curves", "def-weil-derived-tensor", "def-weil-finite-tor-amplitude", "def-weil-pbc-constructible-complexes", "def-weil-pbc-scheme-conventions", "lem-exc-closed-ambient", "lem-exc-closed-amplitude", "lem-exc-closed-support-triangle", "lem-exc-constant-tensor", "lem-exc-direct-image-coproducts", "prop-exc-closed-tor", "thm-exc-curve-open-finiteness"]
+++
Let $T$ be a smooth connected curve over a finite
field or its algebraic closure, and let $i:Z\hookrightarrow T$
be the reduced closed
immersion of finitely many closed points. For
$A=A_{E,n}$, with $\ell$ invertible on $T$, the ambient
etale right adjoint satisfies

$$
Ri^!D_c^{[a,b]}(T_{\mathrm{et}},A)
\subseteq D_c^{[a,b+2]}(Z_{\mathrm{et}},A).
$$

The subscript refers to
constructible cohomology.
It sends Tor amplitude
$[a,b]$ into $[a,b+2]$. For $m\leq n$, the
derived coefficient map

$$
(Ri_A^!K)\otimes_A^L A_{E,m}
\longrightarrow Ri_{A_{E,m}}^!(K\otimes_A^L A_{E,m})
$$

is an isomorphism for finite-Tor bounded constructible $K$.
All bounds are uniform in the coefficient level.

## Proof

By [thm-exc-curve-open-finiteness], the open complement
satisfies both direct-image hypotheses with $c=1$.
[lem-exc-closed-amplitude], [prop-exc-closed-tor] now give
bounded constructibility and the Tor bound $[a,b+2]$.
There is no preservation hypothesis on $Ri^!$ in this application.

For the coefficient comparison, apply
[lem-exc-direct-image-coproducts], [lem-exc-constant-tensor]
with the finite module $A_{E,m}$. Tensor the triangle of
[lem-exc-closed-support-triangle], for the right adjoint $Ri^!$
of [lem-exc-closed-ambient], with this module. Its second and
third terms are exactly those of the closed-support triangle over
$A_{E,m}$, and exact closed direct image commutes with the
constant coefficient tensor, as its etale stalks are either unchanged
or zero. The resulting map of triangles identifies their first terms;
full faithfulness of $i_*$ gives the asserted comparison on $Z$.
All calculations used $c=1$, independently of $n$ and $m$.

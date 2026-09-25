+++
id = "sk-prop-jacobian-descent"
kind = "section"
title = "The Jacobian over a general base field, by Galois descent"
order = 860
uses = ["sk-def-av-jacobian", "sk-def-av-pic", "sk-def-picard-pic", "sk-prop-jacobian"]
+++
*Proposition (sketch).*

Let $k_0$ be any field, $k_s$ a separable closure and $\bar k_0$ an
algebraic closure containing it, and let $C_0$ be a proper smooth
geometrically connected curve of genus $g$ over $k_0$; put
$C=C_0\times_{k_0}\bar k_0$. The Jacobian $J(C)$ and its representing
isomorphism in [sk-prop-jacobian] descend canonically to $k_0$,
compatibly with base change; write $J_0$ for this descended abelian
variety. The induced identification $J_0(\bar k_0)=\Pic^0(C)$ is
*equivariant* for the natural actions of
$\operatorname{Gal}(k_s/k_0)$: on the left through the $k_0$-structure of
$J_0$, on the right through that of $C_0$. In particular, for every $n$
and every $\ell$, restricting to $\ell^n$-torsion gives a
$\operatorname{Gal}(k_s/k_0)$-equivariant isomorphism
$J_0[\ell^n](\bar k_0)\cong\Pic^0(C)[\ell^n]$. No rational point of
$C_0$ is assumed; the finite-field case $k_0=\mathbf F_q$ is the one used
downstream.

## Proof

*Step 1 (the geometric case).* Over $\bar k_0$ the functor $\Pic^0$
of $C$ is represented by an abelian variety $J(C)$ of dimension $g$ with
$\Pic^0(C)=J(C)(\bar k_0)$: this is [sk-prop-jacobian]. Its
construction rigidifies the Picard functor along a rational point, which
is available over an algebraically closed field.

*Step 2 (a separable point).* $C_0$ is smooth over $k_0$, hence
geometrically reduced, and the closed points whose residue field is finite
*separable* over $k_0$ are dense in it. Choose such a point $x$ and
let $k_1/k_0$ be a finite Galois extension containing $k(x)$. Over $k_1$
the curve acquires a rational point, so the rigidified construction of
Step 1 applies verbatim and represents $\Pic^0$ of $C_0\times_{k_0}k_1$ by
an abelian variety $J_1$ over $k_1$. (Equivalently: $J(C)$ and the
isomorphism of Step 1 are given by finitely many equations and hence are
already defined over a finite subextension of $k_s/k_0$, which one may
enlarge to be Galois over $k_0$.)

*Step 3 (Galois descent).* Since $C_0$ is defined over $k_0$ and the
Picard functor commutes with base change, $\operatorname{Gal}(k_1/k_0)$
acts semilinearly on $\Pic^0$ of $C_0\times_{k_0}k_1$; transporting that
action through the isomorphism of Step 2 gives a descent datum on $J_1$
relative to $k_1/k_0$. An abelian variety is projective, and Galois
descent is effective for quasi-projective schemes, so the datum descends:
it produces $J_0$ over $k_0$ with $J_0\times_{k_0}k_1\cong J_1$, and the
isomorphism of functors descends with it. This is the step that dispenses
with a rational point of $C_0$: one is used over $k_1$ only, never over
$k_0$.

*Step 4 (properties).* Smoothness, properness, geometric
connectedness, the group structure and the dimension descend along the
faithfully flat finite $k_0\to k_1$, so $J_0$ is an abelian variety of
dimension $g$; base-change compatibility of the Picard functor gives
$J_0\times_{k_0}\bar k_0\cong J(C)$ and $J_0(\bar k_0)=\Pic^0(C)$, and the
$\operatorname{Gal}(k_s/k_0)$-action is the induced one. Equivariance
needs no separate argument: the descent datum of Step 3 *is* the
Galois action, so the isomorphism of functors produced by descending it is
$\operatorname{Gal}$-equivariant by construction, and so is its
restriction to $\ell^n$-torsion.

The detailed form, stated over an arbitrary base field, is Blueprint 06b,
`thm:sc-jacobian-representability`; the rigidified construction of
Step 1–2 is Blueprint 50, `thm:pc-picard-representable`, carried
out there over separably closed fields, and the passage from those to a
general base is exactly the descent of Step 3.

Uses: [sk-def-picard-pic], [sk-prop-jacobian]

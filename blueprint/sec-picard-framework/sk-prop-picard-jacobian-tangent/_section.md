+++
id = "sk-prop-picard-jacobian-tangent"
kind = "section"
title = "The tangent space of the Jacobian"
order = 855
uses = ["sk-def-av-jacobian", "sk-def-picard-pic", "sk-lem-picard-cech-computes", "sk-prop-picard-degree-decomposition"]
+++
*Proposition (sketch).*

The tangent space of the group scheme $\underline{\Pic}^0_{C/k}$ of
[sk-prop-picard-degree-decomposition] at the unit is

$$
T_e\underline{\Pic}^0_{C/k}\cong H^1(C,\cO_C),
$$

a $k$-vector space of dimension $g$.

## Proof

Let $k[\varepsilon]=k[x]/(x^2)$. The tangent space at $e$ is the set of
$k[\varepsilon]$-points of $\underline{\Pic}^0_{C/k}$ reducing to $e$, that is, by
[sk-def-picard-pic] and the normalization along $P$, the set of
invertible modules on $C_{k[\varepsilon]}$ whose restriction to $C$ is
trivial, up to isomorphism (a degree-$0$ condition that is automatic,
since the degree is locally constant). Fix a finite affine open cover
$\mathfrak U=\{U_i\}$ of $C$. Such a module is trivial on every
$U_i\times_kk[\varepsilon]$ (an invertible module trivial modulo the
nilpotent $\varepsilon$ on an affine scheme is trivial), so it is given
by transition functions in
$\ker\bigl(\cO(U_{ij}\times k[\varepsilon])^\times\to\cO(U_{ij})^\times\bigr) =\{1+\varepsilon g_{ij}\}$. Since
$(1+\varepsilon a)(1+\varepsilon b)=1+\varepsilon(a+b)$, the cocycle
condition reads $g_{ij}+g_{jk}=g_{ik}$, and changing the trivializations
by $1+\varepsilon h_i$ changes $g_{ij}$ by $h_j-h_i$. The tangent space
is therefore $\Cech^1(\mathfrak U,\cO_C)$, which is $H^1(C,\cO_C)$ by
[sk-lem-picard-cech-computes]; its dimension is the genus $g$ by the
conventions.

Uses: [sk-prop-picard-degree-decomposition], [sk-def-picard-pic], [sk-lem-picard-cech-computes]

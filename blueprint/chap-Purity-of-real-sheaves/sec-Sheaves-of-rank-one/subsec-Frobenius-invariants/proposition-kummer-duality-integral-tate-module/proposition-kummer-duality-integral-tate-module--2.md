+++
id = "proposition-kummer-duality-integral-tate-module--2"
kind = "proposition"
title = "Compatible finite-level torsor pairings"
name_showing = false
order = 1094002
aliases = ["bp-r335-2"]
lean = ["AlgebraicGeometry.Scheme.EtaleTorsor.exists_picTorsionPairing"]
uses = []
+++
The inverse-limit identification is bypassed by Lean; the argument uses
the following finite-level characters.

Let $C_0/k_0$ be a smooth proper geometrically connected curve over a
finite field, put $k=\bar k_0$ and $C=C_0\times_{k_0}k$, and let
$\ell\ne\operatorname{char}k_0$ be prime. Choose a geometric point $s$ of
the connected curve $C$ and a compact topological group $G$ presenting
$\pi_1(C,s)$. Put $A_n=\mathbf Z/\ell^n$ and let $g$ be the geometric
Galois Frobenius of $C$.

There are maps assigning to every finite étale $A_n$-torsor $t$ on $C$
an additive character

$$
\Psi_n(t):\operatorname{Pic}(C)[\ell^n]\longrightarrow A_n
\qquad(n\geq0)
$$

with the following properties. If $\Psi_n(t)=0$, then $t$ has a section.
Isomorphic torsors have the same character. If $g_*t$ denotes the torsor
obtained by composing its structure map with $g$, then

$$
\Psi_n(g_*t)(y)=\Psi_n(t)(g^*y).
$$

Finally, suppose that the monodromy of an $A_{n+1}$-torsor $t'$ reduces
modulo $\ell^n$ to that of an $A_n$-torsor $t$, as characters of $G$.
For $y\in\operatorname{Pic}(C)[\ell^{n+1}]$ one has

$$
\Psi_n(t)(\ell y)=\Psi_{n+1}(t')(y)\bmod\ell^n.
$$

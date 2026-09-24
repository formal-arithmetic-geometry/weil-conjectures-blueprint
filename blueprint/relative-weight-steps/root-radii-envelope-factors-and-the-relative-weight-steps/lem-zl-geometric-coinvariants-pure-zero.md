+++
id = "lem-zl-geometric-coinvariants-pure-zero"
kind = "lemma"
title = "Weight zero of geometric coinvariants"
order = 4325
uses = ["def-weil-frobenius-module-weights", "def-weil-punctual-weights", "def-wf-fundamental-representation"]
+++
Let $C_0$ be a nonempty smooth geometrically connected curve over
$\mathbf F_q$, and let $\mathcal E$ be a lisse Weil sheaf which is
punctually $\iota$-pure of weight zero.
For its geometric fundamental
representation $V$, the coinvariant quotient
$W=V_{\pi_1(C)}$, with its induced Frobenius, is
$\iota$-pure of weight zero.

## Proof

The geometric subgroup in the Weil group of
[def-wf-fundamental-representation] is normal. Therefore the
subspace spanned by $gv-v$, for geometric $g$, is Weil-stable,
and $V\twoheadrightarrow W$ is a quotient Weil representation.
On $W$ the geometric subgroup acts trivially, so the induced
degree-one Frobenius $F_W$ is independent of the lift chosen in
the Weil group. A closed point of degree $d$ consequently acts
on the stalk of this quotient by $F_W^d$.

Choose a closed point $x\in C_0$. Such a point exists: choose a
nonempty affine open of finite type over $\mathbf F_q$, a maximal
ideal of its coordinate ring, and use the fact that its residue field
is a finite extension of $\mathbf F_q$. Put
$d=[\kappa(x):\mathbf F_q]$. The quotient stalk $W$ at $x$ is
a Frobenius-equivariant quotient of $\mathcal E_{\bar x}$.
In a basis extending a basis of its kernel, the Frobenius matrix
is block upper triangular, so the eigenvalues of $F_W^d$ occur
among those of $F_x$ on $\mathcal E_{\bar x}$. They all have
$\iota$-modulus one by [def-weil-punctual-weights].
For each eigenvalue $\lambda$ of $F_W$, its power $\lambda^d$
is an eigenvalue of $F_W^d$; hence
$\lvert\iota(\lambda)\rvert^d=1$ and
$\lvert\iota(\lambda)\rvert=1$. This is weight zero in
[def-weil-frobenius-module-weights].

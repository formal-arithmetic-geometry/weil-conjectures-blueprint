+++
id = "lem-a1-exceptional-constituents"
kind = "lemma"
title = "Exceptional rank-one constituents"
order = 3007
uses = ["def-fd-artin-schreier-sheaf", "def-weil-extension-by-zero", "def-weil-open-closed-recollement", "def-weil-ordinary-compact-cohomology", "def-weil-punctual-weights", "def-wf-constant-weil-twist", "lem-a1-finite-boundary-cohomology", "lem-a1-finite-boundary-weights", "lem-a1-subquotient-extension-bounds", "lem-fd-as-purity", "lem-fd-cohomology-affine-line-character", "lem-fd-stalk-formula", "lem-wf-constant-twist-weight", "lem-zl-affine-curve-range", "thm-weil-poincare-duality"]
+++
Let $\mathcal E$ be either a rank-one constant
Weil sheaf or its tensor product
with an Artin–Schreier sheaf
$\mathcal L_{\psi,ax}$ for some $a\in k_0^\times$. If $\mathcal E$
is punctually $\iota$-pure of weight $w$ on a dense open
$U_0\hookrightarrow\mathbf A^1_{k_0}$, then the compactly supported
cohomology groups $H_c^i(U,\mathcal E)$ have weights at most $w+i$
for every $i$.

## Proof

Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be the given dense open
immersion with finite closed complement $i:Z\hookrightarrow\mathbf A^1$,
and let $\mathcal E_0$ be the lisse extension of $\mathcal E$ to the
line: $\mathcal E_0=\mathcal B_b\otimes\mathcal L_{\psi,ax}$ (a rank-one
lisse $\Qlb$-sheaf on $\mathbf A^1_{k_0}$, since both factors are
lisse there — the linear phase $ax$ has no pole on the line —
with the constant [def-wf-constant-weil-twist] of the Weil twist
$\mathcal B_b$ and
the convention $\mathcal L_{\psi,0}=1$), so that
$j_*\mathcal E=\mathcal E_0$ and $i^*j_*\mathcal E= i^*\mathcal E_0$.

Step 1 (the cohomology of the line). The compactly supported cohomology
of $\mathcal E_0$ on the affine line is concentrated in degree $2$
for $a=0$ and vanishes altogether for $a\neq0$: for $a\neq0$,
the vanishing of the ordinary cohomology of $\mathcal L_{\psi,ax}$ is
[lem-fd-cohomology-affine-line-character], and its compactly
supported cohomology vanishes by the Frobenius-equivariant Poincare
duality [thm-weil-poincare-duality] of the Poincare-duality chapter (the dual of a
lisse sheaf is lisse, and the ordinary cohomology of the dual vanishes by
the same computation); the tensor with the constant twist
$\mathcal B_b$ only scales the Frobenius eigenvalues by a constant of
weight $w$ ([lem-wf-constant-twist-weight]), so it does not
affect vanishing. For $a=0$, $j_*\mathcal E=\mathcal E_0= \mathcal B_b$ is lisse and constant, and the compactly supported
cohomology of the affine line computed in the proof of
[lem-fd-stalk-formula] (Poincare duality: $R\Gamma_c(\mathbf A^1, \overline{\mathbf Q}_\ell)\cong\overline{\mathbf Q}_\ell(-1)[-2]$) gives
$H_c^0=H_c^1=0$ and $H_c^2=\mathcal B_b(-1)$ with weights
$w+2$ by the weight-shift and constant-twist rules. Hence, in all
cases, $H_c^i(\mathbf A^1,\mathcal E_0)=0$ for $i\neq0,2$ and
$H_c^2(\mathbf A^1,\mathcal E_0)$ has weights at most $w+2$.

Step 2 (the boundary). The boundary sheaf $B=i^*\mathcal E_0$ is
supported on the finite set $Z$ and has weights at most $w$: at a
point $z\in Z$ the stalk is the stalk of the lisse rank-one
$\mathcal E_0$, whose Frobenius eigenvalue has modulus
$q_z^{w/2}$ (the twist-scaled root of unity, weights by
[lem-fd-as-purity] and [lem-wf-constant-twist-weight]). By
the finite-boundary computation [lem-a1-finite-boundary-cohomology],
$H_c^r(Z,B)=0$ for $r\neq0$, and $H_c^0(Z,B)$ has weights at most
$w$ by [lem-a1-finite-boundary-weights].

Step 3 (the localization sequence). The open–closed recollement
triangle of [def-weil-open-closed-recollement], applied with
$K=j_*\mathcal E=\mathcal E_0$ and the extension-by-zero functor
[def-weil-extension-by-zero] of the framework chapter, gives the exact
sequence

$$
H_c^0(Z,B)\longrightarrow H_c^1(U,\mathcal E)\longrightarrow
H_c^1(\mathbf A^1,\mathcal E_0)\longrightarrow H_c^1(Z,B)=0,
$$

and $H_c^0(U,\mathcal E)=0$ (it injects into $H_c^0(\mathbf A^1, \mathcal E_0)=0$). Hence $H_c^1(U,\mathcal E)$ is a quotient of the
weight-$w$ group $H_c^0(Z,B)$ and has weights at most $w$ (in
particular at most $w+1$); the group $H_c^2(U,\mathcal E)$ is a
subobject of $H_c^2(\mathbf A^1,\mathcal E_0)$, of weights at most
$w+2$ by the subquotient bound of
[lem-a1-subquotient-extension-bounds]. This is the asserted bound
$w+i$ for $i=0,1,2$; the degrees outside $\{0,1,2\}$ have no
cohomology (the compact-support range of
[lem-zl-affine-curve-range] of this chapter, or directly from the
concentration of the two terms of the triangle).

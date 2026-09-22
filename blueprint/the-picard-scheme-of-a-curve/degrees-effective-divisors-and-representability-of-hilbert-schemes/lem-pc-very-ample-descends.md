+++
id = "lem-pc-very-ample-descends"
kind = "lemma"
title = "Very ampleness descends along field extensions"
order = 4363
lean = ["AlgebraicGeometry.isVeryAmple_of_isVeryAmple_baseChange"]
uses = ["def-pc-base-change", "def-pc-morphism-conventions", "def-pc-picard-presheaf", "lem-pc-very-ample-ample"]
+++
Let $k$ be a field, $X$ a scheme of finite type over $k$ and
$\mathcal{L}$ an invertible module on $X$ such that $\mathcal{L}_K$ is very
ample on $X_K$ for a field extension $K/k$. Then $\mathcal{L}$ is very ample
on $X$; in particular $\mathcal{L}$ is ample if $\mathcal{L}_K$ is.

## Proof

By definition of very ampleness there is an immersion
$i:X_K\to\mathbf P^N_K$ with $i^*\mathcal{O}_{\mathbf P^N}(1)=\mathcal{L}_K$;
equivalently, $i$ is given by base-point-free sections
$t_0,\dots,t_N\in H^0(X_K,\mathcal{L}_K)$ separating points and tangent
directions.

By flat base change for coherent cohomology,
$H^0(X_K,\mathcal{L}_K)=H^0(X,\mathcal{L})\otimes_kK$. Hence each $t_j$ is a
finite combination $\sum_ac_{ja}u_a$ of elements
$u_a\in H^0(X,\mathcal{L})$. Let $V\subseteq H^0(X,\mathcal{L})$ be the
$k$-subspace spanned by the finitely many $u_a$, and let
$\psi:X\to\mathbf P(V)$ be the morphism it defines. Then $V\otimes_kK$
contains all the $t_j$, so the base change $\psi_K:X_K\to\mathbf P(V_K)$ is
(up to the linear embedding of the corresponding projective spaces) the
morphism $i$; in particular $\psi_K$ is an immersion.

Being an immersion descends along the faithfully flat field extension
$k\to K$: for the closed part this is Descent, Lemma 35.37.2, and open
immersions descend likewise, since both properties are fpqc-local on the
base. Hence $\psi$ is an immersion, and
$\psi^*\mathcal{O}_{\mathbf P(V)}(1)=\mathcal{L}$ by construction, so
$\mathcal{L}$ is very ample over $k$. A very ample module is ample by the
affine-basis property of the sets $X_s$ ([lem-pc-very-ample-ample]).

*Import note.* The source's proof of this lemma is interrupted by several
abandoned attempts (a stray "$H^0(X,\mathcal{L})^{\otimes}_k$", a parenthesis
about "different powers twist to", and a half-finished discussion of
effective descent of ideals). The argument above keeps the route the source
settles on — descend the linear system to a $k$-subspace $V$, then descend
the immersion property — and drops the false starts.

Unresolved dependencies: def:sc-ample, def:sc-invertible-module, lem:sc-flat-base-change-coherent

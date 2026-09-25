+++
id = "sk-prop-normal-form"
kind = "section"
title = "Étale-local normal form and slicing"
order = 1397
uses = ["sk-def-smooth"]
+++
*Proposition (sketch).*

Let $g:X\to Y$ be smooth at $x\in X$, of relative dimension $d$
there. Then, after replacing $X$ and $Y$ by affine neighbourhoods,
$g$ factors as

$$
X\ \xrightarrow{\ e\ }\ \Aaf^d_Y\ \xrightarrow{\ p_d\ }\ Y
$$

with $e$ étale and $p_d$ the projection. Moreover, for any smooth
$f:X\to S$ there is an étale covering $\{U_i\to X\}_{i\in I}$ such
that each $U_i\to S$ factors as

$$
U_i\longrightarrow V_i\longrightarrow S
$$

with $V_i\to S$ étale and $U_i\to V_i$ smooth affine with
geometrically connected fibres and a section.
(Stacks Project, Tags `054L` and `0EY4`.)

## Proof

*Normal form.* Shrinking to affines, write $X=\Spec B$,
$Y=\Spec A$ with $B=A[t_1,\dots,t_n]/(g_1,\dots,g_c)$ and the
Jacobian $(\partial g_i/\partial t_j)$ of rank $c=n-d$ at $x$. Pick
$d$ of the coordinates whose differentials complete the $c$ rows of
the Jacobian to a basis of
$\Omega_{A[t]/A}\otimes\kappa(x)$; they define a $Y$-morphism
$e:X\to\Aaf^d_Y$ with $\Omega_{X/\Aaf^d_Y}=0$ near $x$, i.e. $e$
unramified. Source and target are smooth over $Y$ of the same
relative dimension, so the fibres of $e$ are $0$-dimensional; miracle
flatness (regular source, regular target, fibre dimension $=\dim$
source $-\dim$ target) makes $e$ flat, and flat $+$ unramified $=$
étale. Composing with $p_d$ returns $g$ by construction.

*Slicing and relative connectedness.* Let $x\in X$ be a point
*closed in its own fibre* $X_s$, $s=f(x)$. Then
$\mathfrak m_x/\mathfrak m_x^2$ computed in the smooth
$\kappa(s)$-scheme $X_s$ has dimension $d=\dim_xX_s$, so one may cut
$X$ near $x$ by $d$ sections of $\mathcal O_X$ vanishing at $x$ whose
differentials are a basis of it; the resulting closed subscheme
$V\subseteq X$ is flat and unramified over $S$ at $x$ by the Jacobian
criterion, hence étale there, so after shrinking $V\to S$ is
étale and $(\iota,\mathrm{id}):V\to X\times_SV$ is a section of the
smooth $X\times_SV\to V$. Let $U\subseteq X\times_SV$ be the
relative connected component of that section, i.e. the set of points
lying in the same connected component of their own fibre as the
section; it is open by the open representability of the relative
connected-component functor for a flat, finitely presented morphism
with geometrically unibranch (here: smooth) fibres. Then $U\to V$
is smooth with geometrically connected fibres and a section, $V\to S$
is étale, and $U\to X\times_SV\to X$ is étale. These $U$ cover
$X$: their images are open, and an open of $X$ containing every
point closed in its fibre is all of $X$, because each fibre $X_s$ is
Jacobson, so a nonempty closed subset of $X_s$ contains a point
closed in $X_s$.

Uses: [sk-def-smooth]

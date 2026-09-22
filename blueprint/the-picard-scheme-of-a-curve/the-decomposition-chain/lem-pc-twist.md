+++
id = "lem-pc-twist"
kind = "lemma"
title = "The twist lemma"
order = 4387
lean = ["AlgebraicGeometry.Curve.exists_twist_h0_one_h1_zero"]
uses = ["def-pc-separably-closed", "def-pc-smooth-projective-curve", "def-pc-genus", "def-pc-derived-category", "def-pc-degree-line-bundle", "def-pc-curve", "def-pc-rational-point", "def-pc-zero-scheme", "lem-pc-flat-base-change-cohom", "lem-pc-very-ample-ample", "lem-pc-dim-base-change", "lem-pc-closed-imm-base-change", "lem-pc-ample-positive-degree", "lem-pc-degree-base-change", "lem-pc-serre-vanishing", "lem-pc-euler-additive", "prop-pc-XK-integral", "lem-pc-vanishing-above-dim", "lem-pc-rational-points-dense"]
+++
(Picard Schemes of Curves, Lemma 44.6.5, [Tag
0B9Y](https://stacks.math.columbia.edu/tag/0B9Y); the proof is a variant of
Varieties, Lemma 33.44.16, [Tag
0B8Z](https://stacks.math.columbia.edu/tag/0B8Z).) Let $k$ be a separably
closed field [def-pc-separably-closed], let $X$ be a smooth projective
curve of genus $g$ over $k$, let $K/k$ be a field extension and let
$\mathcal{L}$ be an invertible sheaf on $X_K$. Then there exists an
invertible sheaf $\mathcal{L}_0$ on $X$ such that
$$
\dim_KH^0\bigl(X_K,\;\mathcal{L}\otimes\mathcal{L}_0|_{X_K}\bigr)=1
\qquad\text{and}\qquad
\dim_KH^1\bigl(X_K,\;\mathcal{L}\otimes\mathcal{L}_0|_{X_K}\bigr)=0.
$$

## Proof

*Step 1: an ample polarisation.* The smooth projective curve $X$ carries a
closed immersion $i:X\to\mathbf{P}^n_k$; by [lem-pc-very-ample-ample] the
module $\mathcal{L}_0^{\bullet}:=i^*\mathcal{O}_{\mathbf{P}^n}(1)$ is ample
on $X$ and, by [lem-pc-dim-base-change] and the same argument applied to
$i_K:X_K\to\mathbf{P}^n_K$ (base change of $i$ along $K$,
[lem-pc-closed-imm-base-change]), the base change
$\mathcal{L}_0^{\bullet}|_{X_K}$ is ample on $X_K$. By
[lem-pc-ample-positive-degree], $\deg_X(\mathcal{L}_0^{\bullet})>0$, and by
[lem-pc-degree-base-change],
$\deg_{X_K}(\mathcal{L}_0^{\bullet}|_{X_K})=\deg_X(\mathcal{L}_0^{\bullet})>0$.

*Step 2: achieve $H^0\neq0$, $H^1=0$.* For $n\ge0$ put
$\mathcal{L}^{(n)}:=\mathcal{L}\otimes\mathcal{L}_0^{\bullet\otimes n}|_{X_K}$.
Serre vanishing [lem-pc-serre-vanishing] (with the field $K$, $X=X_K$, the
ample module $\mathcal{L}_0^{\bullet}|_{X_K}$ and
$\mathcal{F}=\mathcal{L}$) shows $H^p(X_K,\mathcal{L}^{(n)})=0$ for all
$p\ge1$ once $n\gg0$. On the other hand
$$
\chi(X_K,\mathcal{L}^{(n)})=\deg(\mathcal{L}^{(n)})+\chi(X_K,\mathcal{O})
=\deg_K(\mathcal{L})+n\deg_X(\mathcal{L}_0^{\bullet})+(1-g)
$$
by [lem-pc-degree-base-change] and the additivity of $\chi$
[lem-pc-euler-additive]; here $\chi(X_K,\mathcal{O})=1-g$: indeed
$\dim_KH^0(X_K,\mathcal{O})=\dim_k(H^0(X,\mathcal{O})\otimes_kK)=1$ and
$\dim_KH^1(X_K,\mathcal{O})=g$ by [lem-pc-flat-base-change-cohom] and
[prop-pc-XK-integral], and the higher cohomology vanishes by
[lem-pc-vanishing-above-dim] ($\dim X_K=1$, [lem-pc-dim-base-change]). For
$n\gg0$ the right-hand side is $\ge1$, hence, since $H^p=0$ for $p\ge1$,
$$
\dim_KH^0(X_K,\mathcal{L}^{(n)})=\chi(X_K,\mathcal{L}^{(n)})\geq1
\qquad\text{and}\qquad
H^1(X_K,\mathcal{L}^{(n)})=0.
$$
Replace $\mathcal{L}$ by $\mathcal{L}^{(n)}$ for such an $n$; then
$t:=\dim_KH^0(X_K,\mathcal{L})\geq1$ and $H^1(X_K,\mathcal{L})=0$.

*Step 3: descending induction on $t$.* For $t=1$ there is nothing to prove.
Assume $t>1$. By [lem-pc-rational-points-dense] (the smooth scheme $X$ over
the separably closed field $k$), $X(k)$ is dense in $X$, and since $X$ is a
variety of dimension $1$ a finite set of points is not dense: there are
infinitely many $k$-rational points of $X$. For $x\in X(k)$ the pullback
$x_K=\operatorname{Spec}(K)\times_kx$ is a $K$-rational point of $X_K$ and
the family $(x_K)_{x\in X(k)}$ is Zariski dense in $X_K$ (it is infinite,
and a closed subset of the integral curve $X_K$ containing infinitely many
closed points is all of $X_K$; $X_K$ is integral by
[prop-pc-XK-integral]).

Choose a non-zero $s\in H^0(X_K,\mathcal{L})$. Since $s\neq0$ and $X_K$ is
integral, $s_\eta\neq0$ at the generic point, so the zero scheme $Z(s)$ is
a proper closed subset of $X_K$, hence finite; by density there is an
$x\in X(k)$ with $s(x_K)\neq0$, i.e.
$s_{x_K}\notin\mathfrak m_{x_K}\mathcal{L}_{x_K}$.

Let $\mathcal{I}$ be the ideal sheaf of the closed immersion
$i:x_K\hookrightarrow X_K$; $\mathcal{I}$ is invertible ($X_K$ is smooth
over $K$, $x_K$ is a closed point with $\kappa(x_K)=K$, so the closed-point
lemma of the divisors chapter applies). The sequence
$$
0\longrightarrow\mathcal{I}\otimes\mathcal{L}\longrightarrow\mathcal{L}\longrightarrow
i_*i^*\mathcal{L}\longrightarrow0
$$
is exact (exactness on the right:
$i_*i^*\mathcal{L}\cong\mathcal{L}/\mathcal{I}\mathcal{L}$ since $\mathcal{I}$
is an invertible ideal). We have
$H^0(X_K,i_*i^*\mathcal{L})=H^0(x_K,i^*\mathcal{L})\cong\kappa(x_K)=K$ of
dimension $1$, and $H^0(X_K,\mathcal{L})\to H^0(X_K,i_*i^*\mathcal{L})$ is
surjective (its image contains $s(x_K)\neq0$, and the target is
$1$-dimensional). The long exact sequence
$$
0\to H^0(\mathcal{I}\otimes\mathcal{L})\to H^0(\mathcal{L})\to H^0(i_*i^*\mathcal{L})\to
H^1(\mathcal{I}\otimes\mathcal{L})\to H^1(\mathcal{L})=0
$$
then gives $\dim_KH^0(X_K,\mathcal{I}\otimes\mathcal{L})=t-1$ and
$H^1(X_K,\mathcal{I}\otimes\mathcal{L})=0$.

Iterating (for $j=1,\dots,t-1$: pick any $x_j\in X(k)$ with the property of
Step 3 — there are infinitely many, so distinct ones may be chosen; the
ideal sheaves $\mathcal{I}_{x_j}$ are invertible, and
$\mathcal{I}_{x_j,K}=\mathcal{I}_{x_j}\otimes\mathcal{O}_{X_K}$ by
[lem-pc-closed-imm-base-change]) we reach a module
$$
\mathcal{L}\otimes\mathcal{L}_0^{\bullet\otimes n}|_{X_K}\otimes
\mathcal{I}_{x_1,K}\otimes\cdots\otimes\mathcal{I}_{x_{t-1},K}
=\mathcal{L}\otimes\mathcal{L}_0|_{X_K}
$$
with
$\mathcal{L}_0:=\mathcal{L}_0^{\bullet\otimes n}\otimes\mathcal{I}_{x_1}\otimes\cdots\otimes\mathcal{I}_{x_{t-1}}$,
an invertible sheaf on $X$, and with $\dim_KH^0=1$, $H^1=0$. This proves
the lemma.

*Import note.* In the source the condition
"$s_{x_K}\notin\mathfrak m_{x_K}\mathcal{L}_{x_K}$" appears with the
backslash of `\notin` lost to a line break; it is restored above.

Unresolved dependencies: def:sc-invertible-module, def:sc-ample, def:sc-effective-cartier-divisor, lem:sc-point-cartier

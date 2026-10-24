+++
id = "def-pd-fibrewise-degree"
kind = "definition"
title = "Fibrewise degree of an invertible module on a proper family"
lean = ["AlgebraicGeometry.picardPresheafDegree"]
order = 862
uses = ["def-pc-base-change", "def-pc-degree-line-bundle", "def-pc-euler-characteristic", "def-pc-fppf-site", "def-sc-invertible-module"]
+++
Let $f:X\to S$ be a proper morphism of schemes which is locally of finite
presentation. Let $T$ be an $S$-scheme (in the fppf site of
[def-pc-fppf-site]) and let $\mathcal{L}$ be an
invertible $\mathcal{O}_{X_T}$-module,
with $X_T=X\times_ST$ the base change of $X$ along
$T\to S$ and $f_T:X_T\to T$ the projection. For a point $t\in T$ with
residue field $\kappa(t)$, the fibre
$X_t:=X_T\times_T\Spec\kappa(t)$ of $f_T$ over $t$ is a proper scheme over
the field $\kappa(t)$, the *fibre* $\mathcal{L}_t$ of $\mathcal{L}$ is the
pullback of $\mathcal{L}$ to $X_t$, an invertible $\mathcal{O}_{X_t}$-module,
and the *fibrewise degree* of $\mathcal{L}$ at $t$ is the integer

$$
\deg_T(\mathcal{L})(t):=\deg_{X_t}\bigl(\mathcal{L}_t\bigr)
:=\chi\bigl(X_t,\mathcal{L}_t\bigr)
-\chi\bigl(X_t,\mathcal{O}_{X_t}\bigr),
$$

with $\chi$ the Euler characteristic over $\kappa(t)$ and
$\deg$ the degree of an invertible module
on a proper scheme over a field.

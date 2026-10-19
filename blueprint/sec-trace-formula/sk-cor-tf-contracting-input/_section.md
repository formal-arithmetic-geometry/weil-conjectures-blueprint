+++
id = "sk-cor-tf-contracting-input"
kind = "corollary"
title = "Contracting local terms at a point"
order = 2659
uses = ["sk-thm-tf-contracting-local-term", "sk-d-trace-class"]
tags = ["sketch"]
+++
Here $c=(c_1,c_2):C\to X\times X$ is a correspondence of separated finite-type schemes over the
algebraically closed field $k$ with fixed scheme $F_c$, $I_y$ is the ideal of the point $y$, and
$\operatorname{LT}_\beta(u)$ is the local term of [sk-d-trace-class] of $u$ on a proper
open-and-closed component $\beta$ of $F_c$.

Let $y\in X(k)$, and suppose $c_1^{-1}(y)$ is a single reduced point
$z$, with $c_2(z)=y$. Suppose $\beta=\{z\}$ is an isolated reduced
open-and-closed component of $F_c$, and on a neighbourhood of $\beta$
the ideal $I_y$ satisfies

$$
 c_2^\cdot(I_y)\mathcal O_C\subset c_1^\cdot(I_y)\mathcal O_C,
 \qquad
 \bigl(c_2^\cdot(I_y)\mathcal O_C\bigr)^n
  \subset\bigl(c_1^\cdot(I_y)\mathcal O_C\bigr)^{n+1}
 \quad\text{for some }n\geq1.
$$

Then for every $K\in\Dctf(X,A)$ and every morphism
$u:c_2^*K\to c_1^!K$, the local term at $\beta$ is the categorical
trace of the restricted morphism $u_Z$ of
Theorem [sk-thm-tf-contracting-local-term] with $Z=\{y\}$. In particular, for
$c=(\operatorname{id}_X,h)$,

$$
 \operatorname{LT}_y(u)
      =\operatorname{tr}_A(u_{\bar y}\mid K_{\bar y}).
$$

Here $X$ may be singular.

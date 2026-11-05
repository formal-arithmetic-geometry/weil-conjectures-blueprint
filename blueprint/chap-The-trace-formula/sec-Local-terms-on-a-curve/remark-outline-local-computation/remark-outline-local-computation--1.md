+++
id = "remark-outline-local-computation--1"
kind = "remark"
title = "Outline of the local computation (1)"
name_showing = false
order = 963001
aliases = ["bp-r293-1"]
+++
Let $X_0$ be a smooth curve and $y\in X_0(\mathbf F_{q^m})$. The
trace formula on $\mathbf P^1$ needs Proposition [proposition-frobenius-local-term-curve]
below, which says that the local term at $y$ of any morphism
$\psi:(\Phi_X^m)^*K\to K$ is the naive trace
$\operatorname{tr}_A(\psi_{\bar y}\mid K_{\bar y})$, also when $K$ is not
lisse at $y$. We filter $K$ by the open complement of $y$ and the
point $y$. By additivity of traces this reduces the proposition to two cases:
the point itself, where Lemma [lemma-local-terms-point] applies, and the case
$K_{\bar y}=0$, where we must show that the local term vanishes.

The second case needs a geometric argument. The local term is defined on a
neighbourhood of $(y,y)$ in $X\times X$, where the Frobenius graph
meets the diagonal, and the vanishing of the stalk at $y$ does not
by itself control it. We follow [sga5, III B, §§2–4]. The local term is a restriction
map from the graph to the diagonal. Blowing up $(y,y)$ separates
the two curves. After the blowup the local term becomes a restriction to punctured curves
near the point where two transverse divisors meet. There it vanishes when the monodromy is an
$\ell$-group. We reduce to that case by passing to finite covers of degree prime to $\ell$
(Appendix [chap-Cohomology-of-torsion-sheaves-on-curves]); for such a cover the trace map
splits the pullback.

What vanishes is a morphism in $D(A)$, before any trace is taken. For this
reason the vanishing holds for every $\psi$, for every finite $\ell$-primary
ring $A$, and for every $K$ with $K_{\bar y}=0$.

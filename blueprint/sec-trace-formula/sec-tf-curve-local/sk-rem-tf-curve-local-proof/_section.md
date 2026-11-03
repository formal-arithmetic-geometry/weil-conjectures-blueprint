+++
id = "sk-rem-tf-curve-local-proof"
kind = "remark"
title = "Outline of the local computation"
order = 577
tags = ["sketch"]
+++
Let $X_0$ be a smooth curve and $y\in X_0(\mathbf F_{q^m})$. The
trace formula on $\mathbf P^1$ needs Proposition [sk-p-frob]
below, which says that the local term at $y$ of any morphism
$\psi:(\Phi_X^m)^*K\to K$ is the naive trace
$\operatorname{tr}_A(\psi_{\bar y}\mid K_{\bar y})$, also when $K$ is not
lisse at $y$. Filtering $K$ by the open complement of $y$ and the
point $y$, and using additivity of traces, we reduce to the point,
where Lemma [sk-p-pairing] applies, and to the case
$K_{\bar y}=0$, where we must show that the local term vanishes. This
second case needs a geometric argument, because the local term is defined on a
neighbourhood of $(y,y)$ in $X\times X$, where the Frobenius graph
meets the diagonal, and the vanishing of the stalk at $y$ does not
by itself control it. The argument is that of [sga5, III B, §§2–4]. The local term is a restriction
map from the graph to the diagonal, and blowing up $(y,y)$ separates
the two curves, so that it becomes a restriction to punctured curves
near the point where two transverse divisors meet; there it vanishes when the monodromy is an
$\ell$-group, and finite covers of degree prime to $\ell$
(Appendix [sec-curve-estimates]) reduce to that case. What vanishes is a
morphism in $D(A)$, before any trace is taken, so the vanishing holds
for every $\psi$ and every $K$ with $K_{\bar y}=0$, in particular for
$j_!K$ on $\mathbf P^1$, which is not lisse at infinity, and for every
finite $\ell$-primary ring $A$. We forget the $A$-action only to detect
a zero object, in Lemma [sk-lem-tf-transverse-boundary], and the trace of
a cover of degree prime to $\ell$ splits the pullback.

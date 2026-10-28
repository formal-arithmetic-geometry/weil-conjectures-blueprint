+++
id = "sk-rem-tf-curve-local-proof"
kind = "remark"
title = "Route of the local calculation"
order = 3624
tags = ["sketch"]
+++
Let $X_0$ be a smooth curve and $y\in X_0(\mathbf F_{q^m})$. The goal
is [sk-p-frob] below: the local term at
$y$ of a morphism $v:(\Phi_X^m)^*K\to K$ is
$\operatorname{tr}_A(v_{\bar y}\mid K_{\bar y})$. The open–closed
filtration at $y$ and filtered trace-class additivity reduce this to
the point, where [sk-p-pairing] applies, and to
the case $K_{\bar y}=0$, where one has to show that the local term
vanishes. This vanishing carries the geometric content; the reduction
to it is formal. The argument is the restriction-map and blowup
argument of (SGA 5, III B, §§2–4), in the following steps.

- [sk-lem-tf-curve-supported-pairing]: the local term is the
  supported restriction map from the Frobenius graph to the diagonal,
  followed by evaluation and integration.
- [sk-lem-tf-curve-restriction-zero]: if $K_{\bar y}=0$, this
  supported restriction map is zero in $D(A)$. Localization turns it
  into a restriction to the punctured diagonal, and finite covers of
  degree prime to $\ell$ (the appendix on curves) reduce to
  monodromy through finite $\ell$-groups.
- [sk-i-curve-zero] combines the two
  lemmas, and [sk-p-frob] adds the point.
- The geometric vanishing used in
  [sk-lem-tf-curve-restriction-zero] is proved in the
  subsubsection after it. Blowing up $(y,y)$ in the surface $X\times X$
  separates the Frobenius graph from the diagonal, and the restriction
  splits into restrictions to the punctured strictly local curves that
  make up the strict transform of the diagonal
  ([sk-lem-tf-blowup-restriction]). Each of these curves meets the exceptional divisor
  transversely at one point, and its restriction is zero ([sk-lem-tf-punctured-restriction])
  by the transverse calculation of [sk-lem-tf-transverse-boundary], which
  uses Kummer residues, smooth purity and tame ramification along a
  regular divisor.

The vanishing is a vanishing of a morphism in $D(A)$, before any
trace is taken. Hence it holds for every finite $\ell$-primary ring
$A$, regular or not, and for every $v$ and every $K$ with
$K_{\bar y}=0$; for instance it covers $j_!K$ on $\mathbf P^1$, which
is not lisse at infinity. In [sk-lem-tf-transverse-boundary],
forgetting the $A$-action serves only to detect a zero object; the
vanishing of morphisms comes from the generization square there and
from the prime-to-$\ell$ trace splitting.

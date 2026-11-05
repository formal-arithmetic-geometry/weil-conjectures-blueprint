+++
kind = "proof"
of = "proposition-no-frobenius-fixed-vector"
order = 1513
uses = ["definition-compactification-refinement", "proposition-multiplication-n", "proposition-integral-tate-module"]
+++
A fixed vector is a compatible system of torsion points, each rational
over $\mathbf F_{q^m}$. But the rational points form a finite group, so the orders of the $\ell$-power torsion points in it are bounded, and
compatibility under $[\ell]$ then forces the system to vanish. The statement for $V_\ell A$ then follows by clearing denominators.

Since an automorphism and its inverse have the same fixed vectors, we
may use arithmetic Frobenius instead. On $A(\overline{\mathbf F}_q)$
its $m$th power fixes exactly $A_0(\mathbf F_{q^m})$. This group is
finite, because on each affine open of a finite affine cover a rational
point is determined by finitely many coordinates in the finite field.
Hence the $\ell$-primary part of $A_0(\mathbf F_{q^m})$ is killed by
some $\ell^e$. Let $(t_n)$ be a fixed compatible sequence. Each
$t_{n+e}$ lies in this $\ell$-primary part, and since the transition
maps are $[\ell]$, we find

$$
t_n=\ell^e t_{n+e}=0
$$

for every $n$. This proves that $(T_\ell A)^{F^m}=0$.

Since $T_\ell A$ is free by
Proposition [proposition-integral-tate-module], it injects into
$V_\ell A$. A suitable power of $\ell$ times a fixed vector of
$V_\ell A$ is a fixed vector of $T_\ell A$, and so it vanishes. Hence
$(V_\ell A)^{F^m}=0$. In other words, $F^m-1$ is injective on the
finite-dimensional space $V_\ell A$, and therefore bijective.

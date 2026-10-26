+++
kind  = "proof"
of    = "sk-p-tate"
uses = ["sk-prop-av-tate-rank"]
+++
Since an automorphism and its inverse have the same fixed vectors, we
may use arithmetic Frobenius instead. On $A(\overline{\mathbf F}_q)$
its $m$th power fixes exactly $A_0(\mathbf F_{q^m})$. This group is
finite, because on each affine open of a finite affine cover a rational
point is determined by finitely many coordinates in the finite field.
Hence the $\ell$-primary part of $A_0(\mathbf F_{q^m})$ is killed by
some $\ell^e$. If $(t_n)$ is a fixed compatible sequence, then each
$t_{n+e}$ lies in this $\ell$-primary part, and since the transition maps
are $[\ell]$,

$$
 t_n=\ell^e t_{n+e}=0
$$

for every $n$. This proves that $(T_\ell A)^{F^m}=0$. By
[sk-prop-av-tate-rank], the module $T_\ell A$ is free, so
the map $T_\ell A\to V_\ell A$ is injective. Multiplying a fixed vector
of $V_\ell A$ by a power of $\ell$, we obtain a fixed vector of
$T_\ell A$, which vanishes; hence $(V_\ell A)^{F^m}=0$. Thus $F^m-1$ is
injective on the finite-dimensional space $V_\ell A$, and therefore
bijective.

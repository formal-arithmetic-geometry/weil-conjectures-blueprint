+++
id = "prose-A4-01"
kind = "hidden"
title = "Plan of the appendix on curve cohomology"
order = 1422
+++
The proof of proper base change reduces to facts about the cohomology of
torsion sheaves on curves over an algebraically closed field
(Theorem [sk-thm-curve-package]). This appendix proves Theorem [sk-thm-curve-package], from which
[sk-cor-curve-invariance] follows by $(C_7)$. Remark [sk-rem-curve-twists] fixes the
normalization of the Kummer class of $\mathcal O(1)$ on $\mathbf P^1$. Since
proper base change is needed for all torsion coefficients, we treat
both the primes invertible in $k$ and the characteristic prime. The
argument uses, from the main text, only the comparison of cohomology
(Theorem [sk-prop-sf-comparison]) and the stalks of finite direct
images (Lemma [sk-lem-pbc-finite]), both proved before proper base change.

We now prove Theorem [sk-thm-curve-package], which is the pro-étale form of [Stacks, Tag 03SC](https://stacks.math.columbia.edu/tag/03SC). In
characteristic zero the hypotheses in $(C_4)$ and $(C_6)$ that $F$ be
prime to the characteristic hold automatically.

Let $p\ge0$ be the characteristic of $k$. In this appendix $\ell$ is
an arbitrary prime, possibly equal to $p$. We reduce to the constant sheaf
$\mathbf F_\ell$ on a
smooth connected curve. There the cohomology is computed explicitly, by
the Kummer sequence and the Jacobian of Section “Picard schemes and Jacobians” if $\ell$
is invertible in $k$, and by the Artin–Schreier sequence and coherent
cohomology if $\ell=p$. Two observations make this
reduction possible. First, a sheaf supported on finitely many points has
no cohomology in positive degrees. Hence passing to the normalization of
a curve, or extending a sheaf by zero from a dense open subset, changes
cohomology only in degrees zero and one, and only by finite groups when
the stalks are finite. Second, a finite $\mathbf F_\ell$-local system has
finite monodromy, and after a finite étale cover of degree prime to
$\ell$ it becomes a successive extension of constant sheaves. Dividing the
trace of the cover by its degree, we see that the local system is a
direct summand of the pushforward of its pullback to the cover.

Let $C$ be a smooth curve over an algebraically closed field $k$, and
let $\nu_C^*\mathbf G_m$ be the
pullback of the multiplicative group $\mathbf G_m$ of $C_{\mathrm{\acute et}}$ to $C_{\mathrm{pro\acute et}}$. For $n$ invertible
in $k$ we use the Kummer sequence to reduce the cohomology of $\mu_n$ to
that of $\nu_C^*\mathbf G_m$, which we compute first.

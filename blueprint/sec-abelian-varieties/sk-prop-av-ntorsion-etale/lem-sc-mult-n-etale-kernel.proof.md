+++
kind  = "proof"
of    = "lem-sc-mult-n-etale-kernel"
+++
*Reference: Stacks Project, Groupoid Schemes, Lemma 39.9.9,
[Tag 0BFH](https://stacks.math.columbia.edu/tag/0BFH).*

**Step 1: $A[d]$ is finite etale.** By [lem-sc-mult-n-finite-flat],
$[d]$ is finite, flat and locally free of rank $d^{2g}$, and its kernel
$A[d]$ is a finite group scheme of order $d^{2g}$. Since
$\operatorname{char}k\nmid d$, also $\operatorname{char}k\nmid d^{2g}$,
so $A[d]$ is etale over $k$ by [lem-sc-fg-order-prime-etale].

**Step 2: $[d]$ is etale.** The morphism $[d]$ is flat and of finite
presentation, so it is etale as soon as each fibre $[d]^{-1}(y)$,
$y\in A$, is etale over $\kappa(y)$; and a finite $\kappa(y)$-scheme is
etale if and only if its base change to an algebraically closed field
$\Omega\supseteq\kappa(y)$ is etale (the module of differentials
commutes with this faithfully flat base change). The geometric fibre
$[d]^{-1}(y)\times_{\kappa(y)}\Omega$ is the fibre of $[d]_\Omega$
over the $\Omega$-point $y_\Omega$ of $A_\Omega$. It is nonempty, since
$[d]$ is finite locally free of positive rank $d^{2g}$, hence
surjective; so it has an $\Omega$-point $x$, and translation by $x$ is
an isomorphism of $\Omega$-schemes from $A[d]_\Omega$ onto it. As
$A[d]_\Omega$ is etale over $\Omega$ by Step 1, every fibre of $[d]$ is
etale, and $[d]$ is etale.

**Step 3: the base change to $\bar k$.** The base change
$A_{\bar k}$ is an abelian variety of dimension $g$ over $\bar k$ with
$A_{\bar k}[d]=A[d]_{\bar k}$, and Steps 1 and 2 apply to it. A finite
etale scheme over the algebraically closed field $\bar k$ is the
disjoint union of copies of $\Spec\bar k$, one for each $\bar k$-point,
and their number is the order. Hence $A[m]_{\bar k}$ has exactly
$m^{2g}$ points over $\bar k$ for every $m\geq1$ with
$\operatorname{char}k\nmid m$, and $A[d]_{\bar k}$ is the constant
group scheme on the finite group $H:=A[d](\bar k)=A(\bar k)[d]$. The
group $A(\bar k)$ is commutative, since the group law of an abelian
variety is commutative, so $H$ is a finite abelian group of exponent
dividing $d$ and of order $d^{2g}$. Let $\ell$ be a prime dividing $d$,
with $\ell^e$ the exact power of $\ell$ in $d$. The $\ell$-primary part
$H_\ell$ of $H$ has order $\ell^{2ge}$ and exponent dividing $\ell^e$,
and its $\ell$-torsion $H_\ell[\ell]=A(\bar k)[\ell]$ has $\ell^{2g}$
elements. Write $H_\ell\cong\bigoplus_{i=1}^r\mathbf Z/\ell^{a_i}\mathbf Z$
with $1\le a_i\le e$; then $|H_\ell[\ell]|=\ell^r$ gives $r=2g$, and
$\sum_ia_i=2ge$ with all $a_i\le e$ forces $a_i=e$. Hence
$H_\ell\cong(\mathbf Z/\ell^e\mathbf Z)^{2g}$, and by the Chinese
remainder theorem $H=\prod_\ell H_\ell\cong(\mathbf Z/d\mathbf Z)^{2g}$.

+++
kind  = "proof"
of    = "thm-sc-constant-invariance"
uses = ["lem-sc-base-change-curve", "lem-sc-compactification", "lem-sc-affine-open-proper", "lem-sc-genus-invariant", "thm-sc-proper-cohomology", "thm-sc-affine-cohomology", "lem-sc-pic-affine", "lem-sc-pic-proper-ntorsion"]
+++
By [lem-sc-base-change-curve], $C_{k'}$ is a smooth separated
connected curve over $k'$, and by [lem-sc-compactification] and
[lem-sc-affine-open-proper] the curve $C$ is proper or affine.

*Injectivity.* Each $\rho^q_{k'/k}(C,\mathbf F_n)$ is injective. Write $k'$
as the filtered union of its finitely generated $k$-subalgebras $A$. Then
$C_{k'}$ is the limit of the schemes $C_A=C\times_k\operatorname{Spec}A$
along affine transition maps, so the étale cohomology of $C_{k'}$ is the
colimit of that of the $C_A$. Since $k$ is algebraically closed, each $A$
has a $k$-algebra map $A\to k$ (Nullstellensatz), which gives a section
$C\to C_A$ of the projection $C_A\to C$; hence each map
$H^q(C,\mathbf F_n)\to H^q(C_A,\mathbf F_n)$ is injective, and so is the
colimit map.

*Equal orders.* It remains to see that source and target are finite of the
same order. If $C$ is proper, [thm-sc-proper-cohomology] over $k$ and over
$k'$ gives the groups $\mathbf Z/n\mathbf Z$, $(\mathbf Z/n\mathbf Z)^{2g}$,
$\mathbf Z/n\mathbf Z$ in degrees $0,1,2$ and $0$ above, and
$g(C_{k'})=g(C)$ by [lem-sc-genus-invariant]. If $C$ is affine,
[thm-sc-affine-cohomology] over $k$ and over $k'$ gives $\mathbf Z/n\mathbf Z$
in degree $0$ and $0$ in degrees $q\geq2$. In degree one,
$\overline C_{k'}$ is a smooth proper connected compactification of $C_{k'}$
([lem-sc-base-change-curve]) of the same genus ([lem-sc-genus-invariant]),
and its points at infinity are the $r$ points $x\otimes k'$, since every
point at infinity is $k$-rational. By the order formula proved next, both
groups have order $n^{2g+r-1}$.

*The order of $H^1$ in the affine case.* Let $S=\overline C\setminus C$, so
$r=\#S\geq1$, and let $D$, $a$ be the maps of [lem-sc-pic-affine], with
$\operatorname{im}D=\ker a$, $\ker D$ consisting of $n$-th powers, and
$\operatorname{Pic}(C)\cong\operatorname{Pic}(\overline C)/\Lambda$ for
$\Lambda=\operatorname{im}a$. The group $M=\operatorname{im}D\subseteq\mathbf Z^S$
is free of some rank $m$, and since $\ker D$ consists of $n$-th powers,

$$
\#\bigl(\mathcal O_C(C)^\times/\mathcal O_C(C)^{\times n}\bigr)=\#(M/nM)=n^m.
$$

Multiplication by $n$ on $0\to\Lambda\to\operatorname{Pic}(\overline C)\to
\operatorname{Pic}(C)\to0$ gives, by the snake lemma, the exact sequence

$$
0\to\Lambda[n]\to\operatorname{Pic}(\overline C)[n]\to\operatorname{Pic}(C)[n]
\to\Lambda/n\Lambda\to\operatorname{Pic}(\overline C)/n\to\operatorname{Pic}(C)/n\to0.
$$

Here $\operatorname{Pic}(\overline C)[n]\cong(\mathbf Z/n\mathbf Z)^{2g}$ and
$\operatorname{Pic}(\overline C)/n\cong\mathbf Z/n\mathbf Z$
([lem-sc-pic-proper-ntorsion]), and $\operatorname{Pic}(C)/n=0$ as
$\operatorname{Pic}(C)$ is $n$-divisible ([lem-sc-pic-affine]). The finitely
generated group $\Lambda\cong\mathbf Z^S/M$ has rank $r-m$, so
$\#(\Lambda/n\Lambda)=n^{r-m}\,\#\Lambda[n]$. Hence
$\#\operatorname{Pic}(C)[n]=n^{2g}\cdot n^{r-m}/n=n^{2g+r-m-1}$, and the short
exact sequence of [thm-sc-affine-cohomology] gives

$$
\#H^1(C_{\Et},\mathbf F_n)=n^m\cdot n^{2g+r-m-1}=n^{2g+r-1}.
$$

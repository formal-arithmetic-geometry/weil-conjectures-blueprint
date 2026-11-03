+++
kind = "proof"
of = "sk-prop-curve-affine-kummer"
uses = ["sk-thm-br", "sk-thm-curveestimate", "sk-cor-jacobian-torsion"]
+++
Since $\overline C$ is regular, we may use divisors to see that

$$
\operatorname{Pic}(U)=\operatorname{Pic}(\overline C)/
\langle\mathcal O_{\overline C}(x):x\in D\rangle.
$$

One of these line bundles has degree one, and hence $J(\overline C)(k)$
surjects onto $\operatorname{Pic}(U)$. As $J(\overline C)(k)$ is
$n$-divisible (Corollary [sk-cor-jacobian-torsion]), so is
$\operatorname{Pic}(U)$.
By the Kummer sequence and Lemma [sk-thm-br], we have
$H^2(U,\mu_n)=\operatorname{Pic}(U)/n=0$ and $H^q(U,\mu_n)=0$ for
$q\geq3$, which is the vanishing above degree one.

We construct the sequence (D.1) using line
bundles. A $\mu_n$-torsor on $U$ is given by a pair
$(L,\alpha:L^{\otimes n}\simeq\mathcal O_U)$ of a line bundle and a
trivialization of its $n$th power. We extend $L$ to a line
bundle $\overline L$ on $\overline C$ and let $s=\alpha^{-1}(1)$ be the
corresponding rational section of $\overline L^{\otimes n}$. The
divisor of $s$ is supported on $D$. Its orders modulo $n$ do not depend on
the extension, and they define $\partial(L,\alpha)$. Their sum is zero
modulo $n$, since the divisor of $s$ has degree
$\deg\overline L^{\otimes n}=n\deg\overline L$. If all orders are
divisible by $n$, write $\operatorname{div}(s)=nE$ with $E$ supported on
$D$. Then $s$ is a nowhere vanishing section of
$(\overline L(-E))^{\otimes n}=\overline L^{\otimes n}(-nE)$, so the
trivialization extends to the torsor $\overline L(-E)$ on
$\overline C$, which restricts to $(L,\alpha)$ on $U$. This proves exactness at $H^1(U,\mu_n)$. To prove
injectivity, note that a trivialization on $U$ of a torsor on $\overline C$
gives a rational section of its line bundle whose $n$th power has no
zero or pole on $\overline C$. Therefore the divisor of the section is
zero, and the section trivializes the torsor on $\overline C$.

To see that $\partial$ maps onto the kernel of $\sum$, we lift a
residue vector with sum zero modulo $n$ to an integral divisor $B$
supported on $D$; its degree is divisible by $n$ because the residues sum
to zero. There is a line bundle $\overline L$ with
$\overline L^{\otimes n}\simeq\mathcal O_{\overline C}(B)$. To find it, choose
$P\in\overline C(k)$ and put $L_1=\mathcal O_{\overline C}((\deg B/n)P)$. The
line bundle $\mathcal O_{\overline C}(B)\otimes L_1^{\otimes-n}$ has degree
zero, so by divisibility of $J(\overline C)(k)$ it is $N^{\otimes n}$
for some $N$ of degree zero, and $\overline L=L_1\otimes N$ works. The
canonical section of $\mathcal O_{\overline C}(B)$ has divisor $B$ and is
nowhere zero on $U$, so it defines a trivialization of
$\overline L^{\otimes n}|_U$, that is, a Kummer torsor on $U$ whose
residues are the orders of $B$. The
summation map is surjective since $D$ is nonempty. This proves that the
sequence is exact (see also [Stacks, Tag 03RR](https://stacks.math.columbia.edu/tag/03RR)).

The left term and the kernel of summation are free $\mathbf Z/n$-modules of
ranks $2g$ and $\#D-1$, and hence the resulting short exact sequence
splits noncanonically. For naturality, note that the formation of the
compactification, the boundary points, the line bundles and the orders
of vanishing commutes with base change. The
leftmost pullback map is an isomorphism by
Proposition [sk-thm-curveestimate], and the residue groups and their
summation maps are unchanged. By the five lemma applied to the two
exact sequences, the middle pullback map is an isomorphism.

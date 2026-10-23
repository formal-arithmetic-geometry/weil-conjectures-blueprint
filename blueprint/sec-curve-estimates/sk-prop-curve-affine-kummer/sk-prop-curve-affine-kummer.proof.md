+++
kind = "proof"
of = "sk-prop-curve-affine-kummer"
uses = ["sk-thm-br", "sk-thm-curveestimate", "sk-cor-jacobian-torsion"]
+++
Since $\overline C$ is regular, divisors give

$$
\operatorname{Pic}(U)=\operatorname{Pic}(\overline C)/
\langle\cO_{\overline C}(x):x\in D\rangle.
$$

One of these line bundles has degree one, so $J(\overline C)(k)$ surjects
onto $\operatorname{Pic}(U)$. As $J(\overline C)(k)$ is $n$-divisible
([sk-cor-jacobian-torsion]), so is $\operatorname{Pic}(U)$. The vanishing
above degree one now follows from the Kummer sequence
([lem-sc-kummer-exact]) and [sk-thm-br].

The residue sequence comes from line bundles. A $\mu_n$-torsor on $U$ is a
pair $(L,\alpha\colon L^{\otimes n}\simeq\cO_U)$. Extend $L$ to a line bundle
$\overline L$ on $\overline C$ and let $s=\alpha^{-1}(1)$ be the
corresponding rational section of $\overline L^{\otimes n}$. Its divisor is
supported on $D$. Its orders modulo $n$ do not depend on the extension, and
they define $\partial(L,\alpha)$. Their sum is zero modulo $n$, since the
divisor has degree divisible by $n$. If all orders are divisible by $n$,
twist $\overline L$ by the negative of that divisor divided by $n$; the
trivialization then extends without zero or pole. This proves exactness at
$H^1(U,\mu_n)$. For injectivity, a trivialization on $U$ of a torsor on
$\overline C$ gives a rational section of its line bundle whose $n$th power
has no zero or pole on $\overline C$. The divisor of the section is therefore
zero, and it trivializes the torsor on $\overline C$.

For surjectivity of $\partial$ onto the kernel of $\sum$, lift a residue
vector with sum zero modulo $n$ to an integral divisor $B$ supported on $D$
whose degree is divisible by $n$. There is a line bundle $\overline L$ with
$\overline L^{\otimes n}\simeq\cO_{\overline C}(B)$: choose the degree first
and then use divisibility of $J(\overline C)(k)$ to correct the degree-zero
difference. On $U$ this is a Kummer torsor with the prescribed
residues. The summation map is surjective since $D$ is nonempty. This proves
the sequence; see also (Stacks, Tag 03RR).

The left term and the kernel of summation are free $\Z/n$-modules of ranks
$2g$ and $r-1$, so the resulting short exact sequence splits noncanonically.
For naturality, the compactification, boundary points, line bundles and
valuation orders all base change. The leftmost pullback map is an
isomorphism by [sk-thm-curveestimate], and the residue groups and their
summation maps are unchanged. The five lemma applied to the two exact
sequences shows that the middle pullback map is an isomorphism. In
particular no descent of line bundles from $U_{k'}$ to $U$ is needed.

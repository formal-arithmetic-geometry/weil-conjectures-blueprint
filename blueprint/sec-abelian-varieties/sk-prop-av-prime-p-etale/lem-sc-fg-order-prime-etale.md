+++
id = "lem-sc-fg-order-prime-etale"
kind = "lemma"
title = "Group schemes of order prime to $p$ are etale"
lean = ["AlgebraicGeometry.etale_of_not_dvd_finrankΓ"]
order = 578
uses = ["def-sc-group-scheme", "lem-sc-connected-finite-order", "lem-sc-finite-etale-algebra-criterion"]
+++
Let $G$ be a finite group
scheme over a field $k$ of characteristic
$p\geq0$, of order $m$ with $p\nmid m$ (for $p=0$, any
$m$). Then $G$ is etale over $k$.

## Proof

We first reduce to $k$ algebraically closed. Let $\bar k$ be an
algebraic closure of $k$ and $B$ the coordinate ring of $G$. Then
$G_{\bar k}$ is a finite group scheme over $\bar k$ with coordinate
ring $B\otimes_k\bar k$, so its order
$\dim_{\bar k}(B\otimes_k\bar k)=\dim_kB=m$ is unchanged, and the
characteristic of $\bar k$ is still $p$. Moreover $G$ is etale over $k$
if and only if $G_{\bar k}$ is etale over $\bar k$: a finite
$k$-algebra $B$ is etale if and only if $\Omega_{B/k}=0$, and
$\Omega_{B\otimes_k\bar k/\bar k}=\Omega_{B/k}\otimes_k\bar k$ vanishes
if and only if $\Omega_{B/k}$ does, since $\bar k$ is faithfully flat
over $k$. Hence it suffices to treat $G_{\bar k}$, and from now on we
assume that $k$ is algebraically closed.

Write the coordinate ring of $G$ as $B=\prod_iB_i$ with the $B_i$
finite local $k$-algebras, one for each point of the finite discrete
space $G$. By [lem-sc-finite-etale-algebra-criterion], $G$ is etale
if and only if $B$ is a finite product of finite separable field
extensions of $k$. Since the decomposition of the Artinian ring $B$
into local factors is unique, this holds if and only if each $B_i$ is
a finite separable field extension of $k$; as $k$ is algebraically
closed, this means $B_i=k$ for every $i$.

Write $G=G^0\sqcup G^{\mathrm{et}}$, where $G^0$ is the connected
component of the identity and $G^{\mathrm{et}}$ the disjoint union
of the remaining components. The component $G^0$ is a closed
subgroup scheme: it is open and closed (a component of a finite
scheme), the multiplication $G\times_kG\to G$ maps the connected
scheme $G^0\times_kG^0$ into $G^0$ (its image contains
$e\cdot e=e$ and is connected), so the multiplication restricts to
$G^0$, and the same argument for the inverse shows $G^0$ is a
subgroup scheme. By the first paragraph, $G$ is not etale exactly
when some connected component of $G$ is not $\operatorname{Spec}k$.
Every component contains a $k$-point $g$ (its residue field is finite
over the algebraically closed field $k$), and translation by $g$ is an
automorphism of the $k$-scheme $G$ carrying $G^0$ onto that
component. Hence $G$ is not etale exactly when
$G^0\neq\operatorname{Spec}k$. If $p>0$ and $G^0\neq\operatorname{Spec}k$, then by
[lem-sc-connected-finite-order] the order of $G^0$ is a
positive power of $p$, contradicting $p\nmid m$ (the order of
the subgroup scheme $G^0$ divides the order of $G$: the
coordinate ring of $G$ is the product of the coordinate rings of
its connected components). For $p=0$, every finite group scheme
over $k$ is etale: this is the theorem of Cartier, and it is the
recorded classical interface of this proof
(*Stacks Project, Groupoid Schemes, Lemma 39.8.2,
[Tag 047N](https://stacks.math.columbia.edu/tag/047N) – every
locally algebraic group scheme over a field of characteristic zero is
smooth, and a finite smooth group scheme over $k$ is etale;
classical sources: Waterhouse, Introduction to Affine Group Schemes,
§11.4; Milne, Algebraic Groups, Ch. 3*). The Cartier argument
sketched in loc. cit. is not reproduced as a proof here: let $A$ be
the Hopf algebra of a finite group scheme over a field of
characteristic zero, and let $x\in\mathfrak m$ be a nonzero nilpotent
of maximal order with $x^2=0$ (replace $x$ by a power); then
$\Delta(x)=x\otimes1+1\otimes x+\sum_iy_i\otimes z_i$ with
$y_i,z_i\in\mathfrak m$; applying the antipode-twisted
multiplication iteratively, the standard Cartier argument produces
from $x$ a nonzero primitive element, whose $n$-th divided
power is nonzero for every $n$, contradicting the finite
dimension of $A$; hence $\mathfrak m=0$ and $G$ is etale.

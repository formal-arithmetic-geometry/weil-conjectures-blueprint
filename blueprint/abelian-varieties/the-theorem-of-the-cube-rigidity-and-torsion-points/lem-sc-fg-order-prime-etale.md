+++
id = "lem-sc-fg-order-prime-etale"
kind = "lemma"
title = "Group schemes of order prime to $p$ are etale"
order = 2419
uses = ["def-sc-group-scheme", "lem-sc-connected-finite-order"]
+++
Let $G$ be a finite flat group
scheme over an algebraically closed field $k$ of characteristic
$p\geq0$, of order $m$ with $p\nmid m$ (for $p=0$, any
$m$). Then $G$ is etale over $k$.

## Proof

A finite scheme over $k$ is etale if and only if it is reduced:
write the coordinate ring as $B=\prod_iB_i$ with the $B_i$
finite local $k$-algebras; then $\Omega_{B/k}=0$ if and only if
each $B_i$ is a finite separable field extension of $k$ –
indeed $\Omega_{B/k}=\bigoplus_i\Omega_{B_i/k}$, and for a finite
local $k$-algebra $B_i$ with maximal ideal $\mathfrak m_i$:
if $\mathfrak m_i\neq0$, then
$\mathfrak m_i^2\subsetneq\mathfrak m_i$ (if
$\mathfrak m_i^2=\mathfrak m_i$, Nakayama's lemma would give
$\mathfrak m_i=0$), so an element
$x\in\mathfrak m_i\setminus\mathfrak m_i^2$ has nonzero image in
$\Omega_{B_i/k}\otimes k$, whence $\Omega_{B_i/k}\neq0$; and if
$\mathfrak m_i=0$, then $B_i$ is a field with
$\Omega_{B_i/k}=0$, i.e. $B_i/k$ is finite separable. Since
$k$ is algebraically closed, a finite separable extension of $k$
is $k$ itself.

Write $G=G^0\sqcup G^{\mathrm{et}}$, where $G^0$ is the connected
component of the identity and $G^{\mathrm{et}}$ the disjoint union
of the remaining components. The component $G^0$ is a closed
subgroup scheme: it is open and closed (a component of a finite
scheme), the multiplication $G\times_kG\to G$ maps the connected
scheme $G^0\times_kG^0$ into $G^0$ (its image contains
$e\cdot e=e$ and is connected), so the multiplication restricts to
$G^0$, and the same argument for the inverse shows $G^0$ is a
subgroup scheme. By the first paragraph, $G$ is not etale exactly
when $G^0\neq\operatorname{Spec}k$ (a finite reduced local
$k$-algebra over the algebraically closed field $k$ is $k$
itself). If $p>0$ and $G^0\neq\operatorname{Spec}k$, then by
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
dimension of $A$; hence $\mathfrak m=0$ and $G$ is etale. The
interface is used exactly once in this chapter, namely for the
characteristic-zero half of this lemma; the characteristic-$p$ half
is proved above from [lem-sc-connected-finite-order].

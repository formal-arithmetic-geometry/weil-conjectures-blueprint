+++
kind  = "proof"
of    = "lem-zl-spread-normalization"
uses = ["lem-zl-noether-normalization-field"]
+++
Put $K=\operatorname{Frac}A$ and fix algebra generators
$b_1,\ldots,b_m$ of $B$ over $A$.
If $B\otimes_AK=0$, the equality $1=0$ in the localization
means $s_0\cdot1=0$ in $B$ for some $0\neq s_0\in A$.
Then $B_s=0$ for every nonzero multiple $s$ of $s_0$, a finite
$A_s$-module, and $d=0$ works; the injectivity clause is vacuous, as
$A\to B$ kills $s_0$.

Otherwise [lem-zl-noether-normalization-field] supplies
$t_1,\ldots,t_d\in B\otimes_AK$ such that
$K[T_1,\ldots,T_d]\to B\otimes_AK$, $T_i\mapsto t_i$, is injective and
$B\otimes_AK$ is finite over $K[t_1,\ldots,t_d]$. Multiplying each
$t_i$ by a nonzero element of $A$ changes neither the subalgebra
$K[t_1,\ldots,t_d]$ nor the algebraic independence, so we may assume
that every $t_i$ is the image of an element of $B$, again denoted
$t_i$.
Each $b_j$ therefore satisfies a monic equation

$$
b_j^{e_j}+\sum_{r<e_j}c_{jr}(t_1,\ldots,t_d)b_j^r=0,
\qquad c_{jr}\in K[T_1,\ldots,T_d].
$$

This uses the elementary determinant argument for an element acting
on a finite module. Choose a nonzero product $s_1\in A$ of
denominators so that every coefficient of every $c_{jr}$ lies in
$A_{s_1}$.
The finitely many displayed equations hold after localization to
$K$; each of their left-hand sides is consequently killed by some
nonzero element of $A$. Enlarge $s_1$ by the product of these
elements, obtaining $s_0$, so the equations already hold in
$B_{s_0}$, and hence in $B_s$ for every nonzero multiple $s$ of
$s_0$. Reducing powers with the monic equations shows that the
finitely many monomials

$$
b_1^{r_1}\cdots b_m^{r_m},\qquad 0\leq r_j<e_j,
$$

generate $B_s=A_s[b_1,\ldots,b_m]$ as an
$A_s[t_1,\ldots,t_d]$-module. Thus the map $\nu_t$
of [def-zl-localized-coordinates] is finite.

Finally suppose $A\to B$ injective. Then $B\otimes_AK\neq0$, so we are
in the second case. The composite
$A_s[T_1,\ldots,T_d]\to B_s\to B\otimes_AK$ equals the inclusion
$A_s[T_1,\ldots,T_d]\subseteq K[T_1,\ldots,T_d]$ ($A$ is a domain)
followed by the injective map $K[T_1,\ldots,T_d]\to B\otimes_AK$, so it
is injective, and therefore so is $A_s[T_1,\ldots,T_d]\to B_s$.

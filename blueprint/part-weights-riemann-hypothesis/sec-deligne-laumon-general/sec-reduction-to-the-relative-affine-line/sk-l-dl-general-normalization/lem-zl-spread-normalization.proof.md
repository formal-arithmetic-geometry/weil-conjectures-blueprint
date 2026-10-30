+++
kind = "proof"
of = "lem-zl-spread-normalization"
uses = ["def-zl-localized-coordinates", "lem-zl-noether-normalization-field"]
+++
Put $K=\operatorname{Frac}A$ and fix algebra generators
$b_1,\ldots,b_m$ of $B$ over $A$.
If $B\otimes_AK=0$, the equality $1=0$ in the localization
means $s\cdot1=0$ in $B$ for some $0\neq s\in A$.
Then $B_s=0$, a finite $A_s$-module, and $d=0$ works.

Otherwise [lem-zl-noether-normalization-field] supplies
$t_1,\ldots,t_d\in B\otimes_AK$ such that $B\otimes_AK$
is finite over $K[t_1,\ldots,t_d]$.
Each $b_j$ therefore satisfies a monic equation

$$
b_j^{e_j}+\sum_{r<e_j}c_{jr}(t_1,\ldots,t_d)b_j^r=0,
\qquad c_{jr}\in K[T_1,\ldots,T_d].
$$

This uses the elementary determinant argument for an element acting
on a finite module. Choose a nonzero product $s_0\in A$ of
denominators so that all $t_i$ lie in $B_{s_0}$ and every
coefficient of every $c_{jr}$ lies in $A_{s_0}$.
The finitely many displayed equations hold after localization to
$K$; each of their left-hand sides is consequently killed by some
nonzero element of $A$. Enlarge $s_0$ by the product of these
elements, obtaining $s$, so the equations already hold in $B_s$.
Reducing powers with the monic equations shows that the finitely
many monomials

$$
b_1^{r_1}\cdots b_m^{r_m},\qquad 0\leq r_j<e_j,
$$

generate $B_s=A_s[b_1,\ldots,b_m]$ as an
$A_s[t_1,\ldots,t_d]$-module. Thus the map $\nu_t$
of [def-zl-localized-coordinates] is finite.

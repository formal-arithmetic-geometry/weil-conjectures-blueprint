+++
id = "lem-wf-dominant-affine-open-piece"
kind = "lemma"
title = "A dominant affine morphism hits an open set"
order = 4033
+++
Let $f:X\to Y$ be a dominant morphism of nonempty irreducible affine
varieties of finite type over an algebraically closed field. Then
$f(X)$ contains a nonempty principal open subset of $Y$.

## Proof

Write $A=k[Y]$ and $B=k[X]$. Dominance says that $A\to B$ is
injective. Put $K=\operatorname{Frac}(A)$. The nonzero algebra
$B_K=B\otimes_AK$ is finitely generated over $K$; choose a maximal
ideal $\mathfrak m\subset B_K$. Zariski's lemma says that

$$
L:=B_K/\mathfrak m
$$

is a finite algebraic extension of $K$.

Choose algebra generators $b_1,\ldots,b_r$ of $B$ over $A$, and
write $\bar b_i$ for their images in $L$. Each $\bar b_i$ obeys
a monic polynomial over $K$. Clearing the finitely many denominators
in all these polynomials gives $0\ne s\in A$ such that every
$\bar b_i$ is integral over $A_s$. Consequently

$$
C:=A_s[\bar b_1,\ldots,\bar b_r]\subseteq L
$$

is finite, hence integral, over $A_s$, and the natural map
$B_s\to C$ is surjective. For every prime
$\mathfrak p\subset A_s$, lying-over for the integral extension
$A_s\subseteq C$ supplies a prime of $C$ above $\mathfrak p$;
its inverse image in $B_s$ is a point of $X$ mapping to
$\mathfrak p$. Thus the principal open set
$D(s)=\operatorname{Spec}(A_s)$ is contained in $f(X)$.

+++
id = "lem-sc-constant-locus-closed"
kind = "lemma"
title = "The locus of parameters with constant fibre is closed"
order = 486
+++
Let $k$ be a field, $X$ a $k$-scheme proper over $k$, $Z$ a
$k$-scheme separated over $k$, $Y$ a $k$-scheme and
$f:X\times_kY\to Z$ a morphism. Then

$$
L:=\{y\in Y: f(X\times_k\{y\})\ \text{is a single point}\}
$$

is closed in $Y$.

## Proof

Consider the morphism

$$
\Phi:X\times_kX\times_kY\longrightarrow Z\times_kZ,\qquad
\Phi(x_1,x_2,y)=(f(x_1,y),f(x_2,y)),
$$

and the diagonal $\Delta_Z\subseteq Z\times_kZ$. Since $Z$ is
separated over $k$, $\Delta_Z$ is a closed subscheme, so
$\Phi^{-1}(\Delta_Z)$ is closed in $X\times_kX\times_kY$. Now
$f(X\times_k\{y\})$ is a single point if and only if
$f(x_1,y)=f(x_2,y)$ for all $x_1,x_2\in X$, that is, if and only if
$X\times_kX\times_k\{y\}\subseteq\Phi^{-1}(\Delta_Z)$. The
projection $\pi:X\times_kX\times_kY\to Y$ is the base change of the
proper morphism $X\times_kX\to\Spec k$ along $Y\to\Spec k$, hence
is proper, hence closed. Therefore
$L=\pi\bigl(\Phi^{-1}(\Delta_Z)\bigr)$ is closed in $Y$.

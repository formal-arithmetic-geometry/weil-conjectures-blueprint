+++
id = "lem-sc-points-detect-morphisms"
kind = "lemma"
title = "Morphisms are detected on rational points"
order = 2048
+++
Let $k$ be an algebraically closed field, $X$ a reduced $k$-scheme
of finite type, $Y$ a separated $k$-scheme, and let
$\varphi,\psi:X\to Y$ be $k$-morphisms. If
$\varphi(x)=\psi(x)$ for every $x\in X(k)$, then $\varphi=\psi$.

## Proof

Since $Y$ is separated, the diagonal
$\Delta_Y\subseteq Y\times_kY$ is a closed subscheme, so
$E:=(\varphi,\psi)^{-1}(\Delta_Y)$ is a closed subscheme of $X$
containing $X(k)$. Write $X=\Spec A$ first; then $E=\Spec A/I$
for an ideal $I$, and every maximal ideal $\mathfrak m$ of $A$ has
residue field $A/\mathfrak m=k$ (the field $k$ being algebraically
closed and $A$ of finite type over $k$), so it corresponds to a
$k$-point of $X$. The hypothesis gives $I\subseteq\mathfrak m$ for
every maximal ideal $\mathfrak m$, and $\bigcap\mathfrak m$ is the
nilradical of $A$, which is zero because $A$ is reduced; hence
$I=0$ and $E=X$, so $(\varphi,\psi)$ lands in the diagonal, i.e. $\varphi=\psi$. For general $X$, cover $X$ by finitely many
affine open subschemes $U$; each $U$ is reduced of finite type, $U(k) \subseteq E$, so $E\supseteq U$ by the affine case, and the $U$
cover $X$.

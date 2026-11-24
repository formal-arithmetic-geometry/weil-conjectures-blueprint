+++
id = "definition-tate-module"
kind = "definition"
title = "Tate module"
order = 1511
uses = ["definition-abelian-variety", "lemma-abelian-variety-commutative", "definition-relative-picard-functor"]
+++
Let $A$ be an [abelian variety](@definition-abelian-variety) over $k$ and let $\ell$ be a prime
invertible in $k$. The *Tate module* of $A$ is

$$
T_\ell A=\varprojlim_n \href{@definition-abelian-variety}{A[\ell^n](\bar k)},
$$

the limit taken along the maps $\href{@definition-abelian-variety}{[\ell]}:\href{@definition-abelian-variety}{A[\ell^{n+1}](\bar k)}\to
\href{@definition-abelian-variety}{A[\ell^n](\bar k)}$, and we put $V_\ell A=T_\ell A\otimes_{\mathbf Z_\ell}\mathbf Q_\ell$.

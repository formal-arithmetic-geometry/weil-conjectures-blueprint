+++
id = "sk-prop-jacobian-descent"
kind = "proposition"
title = "The Jacobian over the ground field"
order = 875
uses = ["sk-prop-picard-pic-split", "sk-thm-picard-main", "sk-def-picard-pic", "sk-prop-av-mult-n-pullback", "sec-abelian-varieties", "sec-nagata-compactification", "sk-thm-picard-rr", "sk-thm-picard-twist", "sk-thm-picard-f-representable"]
lean = ["AlgebraicGeometry.exists_jacobian_descent"]
tags = ["sketch"]
+++
Let $C_0/k$ be a smooth proper geometrically connected curve of genus
$g$, put $C=C_0\times_k\bar k$, and let $k_s\subseteq\bar k$ be the
separable closure of $k$.
There is an abelian variety $J_0/k$ of dimension $g$ representing the
degree-zero relative Picard fppf sheaf of $C_0$. For every field
extension $k'/k$, the base change $J_0\times_kk'$ represents the degree-zero
Picard sheaf of $C_0\times_kk'$; in particular $J_0\times_k\bar k$ represents
$\Pic^0_{C/\bar k}$, and the canonical identification

$$
 J_0(\bar k)=\Pic^0(C)
$$

is $\operatorname{Gal}(k_s/k)$-equivariant; in particular so is
$J_0[\ell^n](\bar k)\simeq\Pic^0(C)[\ell^n]$ for every prime
$\ell$ and every $n\geq1$.

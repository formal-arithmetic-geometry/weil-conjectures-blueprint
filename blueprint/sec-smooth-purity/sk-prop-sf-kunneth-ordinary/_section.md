+++
id = "sk-prop-sf-kunneth-ordinary"
kind = "proposition"
title = "Künneth and the projection formula in ordinary étale cohomology"
order = 3026
lean = ["AlgebraicGeometry.Etale.nonempty_iso_kunneth"]
tags = ["sketch"]
+++
Let $k$ be a separably closed field, let $\Lambda$ be a finite commutative
ring, and let $X,Y$ be $k$-schemes locally of finite type on which the
exponent of $\Lambda$ is invertible. Let $W$ be a scheme with morphisms
$p_1:W\to X$, $p_2:W\to Y$ exhibiting $W$ as the fibre product
$X\times_kY$. Then for all $E\in D(X_{\Et},\Lambda)$ and
$K\in D(Y_{\Et},\Lambda)$ (*unbounded, and with no properness
hypothesis*) there is an isomorphism

$$
\RG(X_{\Et},E)\otimes^L_{\Lambda}\RG(Y_{\Et},K)
\;\cong\;\RG\bigl(W_{\Et},Lp_1^{*}E\otimes^L_{\Lambda}Lp_2^{*}K\bigr).
$$

Moreover, for a proper morphism $f:X\to Y$ of schemes on which the
exponent of $\Lambda$ is invertible, there is an isomorphism
$Rf_*E\otimes^L_\Lambda L\cong Rf_*(E\otimes^L_\Lambda Lf^{*}L)$ for all
$E\in D(X_{\Et},\Lambda)$ and $L\in D(Y_{\Et},\Lambda)$ (the projection
formula).

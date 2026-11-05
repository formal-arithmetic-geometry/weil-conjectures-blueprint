+++
id = "example-running-example-duality"
kind = "example"
title = "The running example: duality"
order = 889
+++
Let $C_0\colon y^2=x^3-x$ over $\mathbf F_3$ be the elliptic curve of
the introduction, and $C=C_0\times_{\mathbf F_3}k$. Since $C$ has genus
one, $H^1(C,\mathbf Q_\ell)$ is a plane. Indeed, by the Kummer sequence it is the dual of
the rational Tate module $V_\ell J$ of the Jacobian, a $\mathbf Q_\ell$-vector space of
dimension $2g=2$
(Corollary [corollary-torsion-jacobian-field-extension] and Proposition [proposition-kummer-duality-integral-tate-module]).
For $d=1$ the middle pairing on $H^1$ is alternating and perfect, with values
in $\mathbf Q_\ell(-1)$ (Corollary [corollary-cup-product-pairing]). By
Theorem [theorem-poincare-duality-frobenius] it satisfies
$\langle Fx,Fy\rangle=3\langle x,y\rangle$. On a plane an alternating
form is unique up to a scalar, so $\langle Fx,Fy\rangle=\det(F)\langle
x,y\rangle$. Hence $\det(F\mid H^1)=3$. If $\alpha,\beta$ are the
eigenvalues, then $\alpha\beta=3$, and
$\det(1-TF\mid H^1)=1-(\alpha+\beta)T+3T^2$. This is the functional
equation of a curve of genus one: replacing $T$ by $1/(3T)$ multiplies
the polynomial by $(3T^2)^{-1}$.

Duality alone does not give $|\alpha|=3^{1/2}$. For example, the pair $\alpha=3$, $\beta=1$, with $\det(1-TF)=1-4T+3T^2$, consists of algebraic integers and
satisfies $\alpha\beta=3$. Here the count $N_1=4$ gives $\alpha+\beta=0$ and excludes it; in general only purity does.

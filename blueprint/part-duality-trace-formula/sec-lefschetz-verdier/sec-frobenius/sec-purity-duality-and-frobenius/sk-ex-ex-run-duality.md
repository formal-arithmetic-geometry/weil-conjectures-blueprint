+++
id = "sk-ex-ex-run-duality"
kind = "remark"
title = "The running example: duality"
order = 539
tags = ["sketch", "latex:example"]
+++
Let $C_0\colon y^2=x^3-x$ over $\mathbf F_3$ be the elliptic curve of
the introduction, and $C=C_0\times_{\mathbf F_3}k$. Since $C$ has genus
one, $H^1(C,\Ql)$ is a plane: by the Kummer sequence it is the rational
Tate module of the Jacobian, of dimension $2g=2$
(Corollary [sk-cor-jacobian-torsion] and Proposition [sk-d-real-jacobian]).
For $d=1$ the middle pairing on $H^1$ is alternating and perfect
(Corollary [sk-cor-pd-cup-product]),
with values in $\Ql(-1)$, and by Theorem [sk-thm-frobenius] it satisfies
$\langle Fx,Fy\rangle=3\langle x,y\rangle$. On a plane an alternating
form is unique up to a scalar, so $\langle Fx,Fy\rangle=\det(F)\langle x,y\rangle$, and hence $\det(F\mid H^1)=3$. If $\alpha,\beta$ are the
eigenvalues, then $\alpha\beta=3$, and
$\det(1-TF\mid H^1)=1-(\alpha+\beta)T+3T^2$. This is the functional
equation of a curve of genus one: replacing $T$ by $1/(3T)$ multiplies
the polynomial by $(3T^2)^{-1}$. Duality alone does not give
$|\alpha|=3^{1/2}$: the pair $\alpha=3$, $\beta=1$, with
$\det(1-TF)=1-4T+3T^2$, consists of algebraic integers and satisfies
$\alpha\beta=3$. Excluding it is the content of purity.

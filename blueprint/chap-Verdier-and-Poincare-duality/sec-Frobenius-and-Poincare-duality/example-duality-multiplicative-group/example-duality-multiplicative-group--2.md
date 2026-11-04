+++
id = "example-duality-multiplicative-group--2"
kind = "example"
title = "Duality on the punctured line (2)"
name_showing = false
order = 881002
aliases = ["bp-r267-2"]
+++
Thus
$H^1(X,\Lambda)=\Lambda(-1)$, and the other groups vanish. For compact support
we write $X=\mathbf P^1\setminus\{0,\infty\}$. The long exact sequence of
$j_!\Lambda_X\to\Lambda_{\mathbf P^1}\to\Lambda_{\{0,\infty\}}\to$ reads

$$
0\to H^0_c(X)\to\Lambda\xrightarrow{\ \text{diag}\ }\Lambda^2\to H^1_c(X)
\to H^1(\mathbf P^1)=0\to0\to H^2_c(X)\to H^2(\mathbf P^1)\to0,
$$

so $H^0_c=0$, $H^1_c=\Lambda^2/\Lambda\simeq\Lambda$ and
$H^2_c=H^2(\mathbf P^1,\Lambda)=\Lambda(-1)$. Poincaré duality with $d=1$
pairs $H^1_c$ with $H^1$ and $H^2_c$ with $H^0$, and the dimensions match.

The Frobenius eigenvalues show the twist at work. On $H^1_c$, which comes from
the two rational points $0$ and $\infty$, Frobenius acts by $1$. On
$H^1=\Lambda(-1)$ it acts by $q$. The product is $1\cdot q=q^d$, as
Theorem [theorem-poincare-duality-frobenius] requires. Without the twist,
duality would predict the eigenvalue $1/1=1$ on $H^1$ instead of $q$.
Likewise $H^0$ and $H^2_c$ have eigenvalues $1$ and $q$.

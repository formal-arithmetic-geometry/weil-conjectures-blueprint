+++
id = "example-derived-reduction-point"
kind = "example"
title = "Reducing cohomology modulo $\\ell$"
order = 630
+++
Let $X=\operatorname{Spec}\mathbf F_q$ and consider $\mathbf Z/\ell^2\to\mathbf F_\ell$.
Let $K$ be the lisse sheaf $\mathbf Z/\ell^2$ on which Frobenius, the
topological generator of $\operatorname{Gal}(\overline{\mathbf F}_q/\mathbf F_q)
\simeq\widehat{\mathbf Z}$, acts by multiplication by the unit $1+\ell$.
Recall that for a finite module $M$ with a continuous action of $\widehat{\mathbf Z}$, cohomology is computed by the complex $M\xrightarrow{F-1}M$ in degrees $0$
and $1$, where $F$ is the action of the generator. For $K$ this differential is multiplication by $\ell$. Hence $H^0(X,K)=\ell\mathbf Z/\ell^2$
and $H^1(X,K)=(\mathbf Z/\ell^2)/\ell$, both of order $\ell$. On the other
hand, $K_{\mathbf F_\ell}=K/\ell K$ is $\mathbf F_\ell$ with trivial action,
and $H^0(X,K/\ell K)=\mathbf F_\ell$. The map $H^0(X,K)\otimes\mathbf F_\ell\to H^0(X,K/\ell K)$ is zero, since the
generator $\ell$ of $H^0(X,K)$ reduces to $0$.

The derived comparison is nevertheless an isomorphism. The terms of the
complex are free over $\mathbf Z/\ell^2$. Therefore
$R\Gamma(X,K)\otimes^{\mathbf L}\mathbf F_\ell$ is
$\mathbf F_\ell\xrightarrow{0}\mathbf F_\ell$, which is
$R\Gamma(X,K/\ell K)$. The class $1\in H^0(X,K/\ell K)$ comes from the
element $1$ of the degree-zero term, which is not a cocycle before
reduction.

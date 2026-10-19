+++
id = "sk-d-weil"
kind = "definition"
title = "Frobenius correspondences and their operators"
order = 2619
uses = ["sk-d-corr", "sk-d-operator", "sk-d-setup", "sk-d-six", "sk-d-trace-class"]
lean = ["AlgebraicGeometry.ProEtale.WeilComplex"]
tags = ["sketch"]
+++
Throughout, $k_0=\mathbf F_q$, $k=\overline{\mathbf F}_q$ and $s=\operatorname{Spec}k$, and $A$
is a finite commutative $\ell$-primary ring with $\ell\ne\operatorname{char}k$.

Let $X_0/k_0$ be separated and of finite type, and put
$X=X_0\times_{k_0}k$. Denote by $\Phi_X:X\to X$ the base change
of the $q$-power scheme Frobenius of $X_0$; it is a finite
$k$-morphism and a universal homeomorphism. A *Frobenius
correspondence* on $K$ is a morphism in $\Dctf(X,A)$, not necessarily
invertible,

$$
 \psi:\Phi_X^*K\longrightarrow K,
 \qquad K\in\Dctf(X,A).
$$

Its iterates are the morphisms in
$\Dctf(X,A)$

$$
 \psi_m=\psi\circ\Phi_X^*\psi\circ\cdots\circ
 (\Phi_X^{m-1})^*\psi:(\Phi_X^m)^*K\longrightarrow K.
$$

Let $c_m=(\operatorname{id}_X,\Phi_X^m):X\to X\times_sX$ be the graph
of $\Phi_X^m$. Its first leg is the identity, so $\psi_m$ is a
cohomological correspondence on $(X,K)$ for $c_m$. Its operator on
compactly supported cohomology, defined after
[sk-d-trace-class], is the endomorphism in $D^b(A)$

$$
 T_{c_m}(\psi_m)
 =R\Gamma_c(X,\psi_m)\circ(\Phi_X^m)^\sharp,
$$

where $(\Phi_X^m)^\sharp$ is the compact-support pullback induced
by the unit of $(\Phi_X^m)^*\dashv R(\Phi_X^m)_*$.
For $x\in X_0(\mathbf F_{q^m})$ let $\bar x:s\to X$ be the
associated fixed point. Its local operator is the endomorphism
$\psi_{m,\bar x}:K_{\bar x}\to K_{\bar x}$ in $D^b(A)$.

*Complement.* More generally, let $X$ be a scheme over $s$. A *Weil complex* on $X$
consists of an endomorphism $\Phi_1:X\to X$ over $s$ (so it fixes the scalar field $k$), a
complex $K\in D(X,A)$, and a *Frobenius coefficient morphism*
$\varphi:\Phi_1^*K\to K$, an arbitrary map without an invertibility
requirement. Its Frobenius is *the model Frobenius* if
$X=X_0\times_{\mathbf F_q}k$ is the base change of a scheme $X_0$ over
$\mathbf F_q$ and $\Phi_1$ is the base change of the $q$-power scheme Frobenius
of $X_0$, that is, $\Phi_1=\Phi_X$. A *Weil datum* is a Weil complex with $X_0/\mathbf F_q$
separated of finite type, the model Frobenius, $K\in\Dctf(X,A)$ and $\varphi$ an
isomorphism $\Phi_1^*K\simeq K$.
Put $\Phi_m=\Phi_1^m$, and define the iterate $\varphi_m:\Phi_m^*K\to K$
by composing the pulled-back copies of $\varphi$ using
pullback composition ($\varphi_0$ is the identification $\mathrm{id}^*K\simeq K$); for the
model Frobenius and $K\in\Dctf(X,A)$, $\varphi$ is a Frobenius correspondence and $\varphi_m$ is its $m$-th
iterate as above. The graph correspondence is
$c_m=(\operatorname{id}_X,\Phi_m)$, with coefficient map $\varphi_m$.
Write $F_{c,m}=T_{c_m}(\varphi_m)$ for the
global operator. For a point $\bar x:s\to X$ over $s$ fixed by $\Phi_m$ (for the model
Frobenius, the geometric point attached to some $x\in X_0(\mathbf F_{q^m})$), the stalk
endomorphism is $F_{x,m}=(\varphi_m)_{\bar x}:\bar x^*K\simeq\bar x^*\Phi_m^*K\to\bar x^*K$.

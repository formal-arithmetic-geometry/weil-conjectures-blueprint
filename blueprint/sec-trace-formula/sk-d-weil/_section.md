+++
id = "sk-d-weil"
kind = "definition"
title = "Frobenius and Weil data"
order = 2634
uses = ["sk-d-corr", "sk-d-operator", "sk-d-setup", "sk-d-six"]
lean = ["AlgebraicGeometry.ProEtale.WeilComplex"]
tags = ["sketch"]
+++
Let $X$ be a scheme over $s$. A *Weil complex* on $X$ consists of an
endomorphism $\Phi_1:X\to X$ over $s$ (so it fixes the scalar field $k$), a
complex $K\in D(X,A)$, and a *Frobenius coefficient morphism*
$\varphi:\Phi_1^*K\to K$, an arbitrary map without an invertibility
requirement. Its Frobenius is *the model Frobenius* if
$X=X_0\times_{\mathbf F_q}k$ is the base change of a scheme $X_0$ over
$\mathbf F_q$ and $\Phi_1$ is the base change of the $q$-power scheme Frobenius
of $X_0$. A *Weil datum* is a Weil complex with $X_0/\mathbf F_q$ separated of
finite type, the model Frobenius, $K\in D^b_{ctf}(X,A)$ and $\varphi$ an
isomorphism $\Phi_1^*K\simeq K$.

Put $\Phi_m=\Phi_1^m$; for the model Frobenius it is the base change of the
$q^m$-power scheme Frobenius of $X_0$.
Define the iterate $\varphi_m:\Phi_m^*K\to K$
by composing the pulled-back copies of $\varphi$ using
pullback composition ($\varphi_0$ is the identification $\mathrm{id}^*K\simeq K$).
Its graph correspondence is
$c_m=(\operatorname{id}_X,\Phi_m)$, with coefficient map $\varphi_m$.
Write $F_{c,m}=T_{c_m}(\varphi_m)$ for the
global operator; Frobenius finiteness is checked below.
For a point $\bar x:s\to X$ over $s$ fixed by $\Phi_m$ (for the model Frobenius,
the geometric point attached to some $x\in X_0(\mathbf F_{q^m})$), the stalk
endomorphism is $F_{x,m}=(\varphi_m)_{\bar x}:\bar x^*K\simeq\bar x^*\Phi_m^*K\to\bar x^*K$.

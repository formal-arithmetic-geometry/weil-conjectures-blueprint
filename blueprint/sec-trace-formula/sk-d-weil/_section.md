+++
id = "sk-d-weil"
kind = "section"
title = "Frobenius and Weil data"
order = 2442
uses = ["sk-d-corr", "sk-d-operator", "sk-d-setup", "sk-d-six"]
+++
*Definition (sketch).*

Let $X_0/\mathbf F_q$ be separated of finite type, and use the
base change $X=X_0\times_{\mathbf F_q}k$.
Let $\Phi_m:X\to X$ be the base change of the $q^m$-power scheme Frobenius
of $X_0$; it fixes the scalar field $k$.
A Weil datum is $K\in D^b_{ctf}(X,A)$ with
$\varphi:\Phi_1^*K\simeq K$. Define its iterate $\varphi_m:\Phi_m^*K\simeq K$
by composing the pulled-back copies of $\varphi$ using
pullback composition.
Its graph correspondence is
$c_m=(\operatorname{id}_X,\Phi_m)$, with coefficient map $\varphi_m$.
Write $F_{c,m}=T_{c_m}(\varphi_m)$ for the
global operator; Frobenius finiteness is checked below.
For $x\in X_0(\mathbf F_{q^m})$, its associated geometric fixed point
$\bar x$ gives the stalk endomorphism $F_{x,m}=(\varphi_m)_{\bar x}$.
For the coefficient continuation, a *Frobenius coefficient morphism*
means an arbitrary map $\varphi:\Phi_1^*K\to K$, without an invertibility
requirement. Its iterates, graph map and global operator are defined by
the same composites.

Uses: [sk-d-corr], [sk-d-operator], [sk-d-setup], [sk-d-six]

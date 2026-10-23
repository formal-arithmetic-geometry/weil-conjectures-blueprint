+++
id = "sk-def-ops"
kind = "definition"
title = "Verdier dual and evaluation"
order = 3284
uses = ["sk-prop-sf-open-closed-triangle", "sk-lem-finite"]
lean = ["AlgebraicGeometry.ProEtale.dualizingComplex", "AlgebraicGeometry.ProEtale.verdierDual", "AlgebraicGeometry.ProEtale.derivedDual", "AlgebraicGeometry.ProEtale.cohomology"]
tags = ["sketch"]
+++
Let $\Lambda$ be an admissible coefficient ring, and for a scheme $X$ let
$a_X\colon X\to s=\operatorname{Spec}k$ be its structure morphism.

The *dualizing complex* and the *Verdier dual* are

$$
 \omega_{X,\Lambda}=a_X^!\Lambda_s,\qquad
 \mathbb D_XK=\cHom_{\Lambda_X}(K,\omega_{X,\Lambda}).
$$

We write $\omega_X$ for $\omega_{X,\Lambda}$ when $\Lambda$ is
fixed. Thus $\mathbb D_X\colon D(X_{\mathrm{pro\acute et}},\Lambda)^{\mathrm{op}}\to
D(X_{\mathrm{pro\acute et}},\Lambda)$ is an exact functor; it preserves
$\Dctf(X,\Lambda)$ by Lemma [sk-lem-pd-preservation]. The evaluation
pairing $K\otimes^{\mathbf L}\mathbb D_XK\to\omega_X$ in
$D(X_{\mathrm{pro\acute et}},\Lambda)$, followed by tensor–Hom adjunction, defines
the *double-dual morphism*, a natural transformation of
endofunctors of $D(X_{\mathrm{pro\acute et}},\Lambda)$,

$$
 \delta_K:K\longrightarrow\mathbb D_X\mathbb D_XK.
$$

The tensor symmetry in this definition includes the Koszul signs.
On the geometric point $\omega_s=\Lambda_s$, so $\delta$ is the
evaluation map of Lemma [sk-lem-finite].

*Complement.* On $\Dctf(X,\Lambda)$, the bounded constructible finite-Tor
category on the small pro-étale site, one has the operations
$Lf^*,Rf_*,Rf_!,Rf^!,\otimes^L_\Lambda,R\mathcal H om_\Lambda$, where
$Rf_!$ is defined by a compactification and $Rf^!$ is its right
adjoint on $\Dctf$ (the constructible exceptional adjoint of
[det-def-sf-operations](vi), which exists for every separated finite-type morphism;
no ambient adjoint on the full derived category is required). Put

$$
K^\vee=\RHomX(K,\Lambda_X),
$$

and $\RGammac(X,K)=\Fib_s(Ra_{X!}K)$,
$\RGamma(X,K)=\Fib_s(Ra_{X*}K)$, with cohomology $H^i_c,H^i$.

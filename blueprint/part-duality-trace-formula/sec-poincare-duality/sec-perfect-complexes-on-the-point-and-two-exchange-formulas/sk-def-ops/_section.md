+++
id = "sk-def-ops"
kind = "definition"
title = "Verdier dual and evaluation"
order = 503
lean = ["AlgebraicGeometry.ProEtale.dualizingComplex", "AlgebraicGeometry.ProEtale.verdierDual", "AlgebraicGeometry.ProEtale.derivedDual", "AlgebraicGeometry.ProEtale.cohomology"]
uses = ["sk-prop-sf-open-closed-triangle", "sk-lem-finite"]
tags = ["sketch"]
+++
The *dualizing complex* and the *Verdier dual* are

$$
\omega_X=a_X^!\Lambda_s,\qquad
\mathbb D_XK=\cHom_{\Lambda_X}(K,\omega_X).
$$

Thus $\mathbb D_X:D(X_{\mathrm{pro}\acute{e}t},\Lambda)^{\mathrm{op}}\to D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ is an exact functor, and it preserves
$D^b_{\mathrm{ctf}}(X,\Lambda)$ by Lemma [sk-lem-pd-preservation]. The evaluation
pairing $K\otimes^{\mathbf L}\mathbb D_XK\to\omega_X$, followed by
tensor–Hom adjunction, defines the natural *double-dual morphism*

$$
\delta_K:K\longrightarrow\mathbb D_X\mathbb D_XK.
$$

The symmetry of the tensor product used in this definition includes the Koszul signs.
On the geometric point we have $\omega_s=\Lambda_s$, so $\delta$ is the
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

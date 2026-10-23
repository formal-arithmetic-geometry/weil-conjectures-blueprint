+++
id = "sk-prop-tf-nearby-duality-foundation"
kind = "proposition"
title = "Nearby cycles commute with Verdier duality"
order = 3596
uses = ["sk-prop-tf-nearby-external-kunneth", "sk-lem-tf-nearby-mate-coherences", "sk-lem-pd-generic-restriction"]
tags = ["sketch"]
+++
Let $S$ be the excellent strictly henselian trait of
[sk-prop-tf-nearby-external-kunneth], with separably closed residue field $k$,
special point $s$, generic point $\eta$ and geometric generic point $\bar\eta$, and let $A$ be
a finite commutative $\ell$-primary ring with $\ell$ invertible on $S$. For a
separated finite-type $S$-scheme $X$ write $S_X=R\Psi_{X/S}$ for its nearby-cycle
functor, $\mu_X:S_XM\dt S_XN\to S_X(M\dt N)$ for the lax tensor map and
$\theta_X=\beta_{a_X}(A):S_X\omega_{X_\eta}\to\omega_{X_s}$ for the map defined by the
exceptional exchange $\beta$ of the structure map $a_X$, as in
[sk-lem-tf-nearby-mate-coherences]. The duality functors on the geometric generic and
special fibres are relative to these fields. For $M\in D^b_{\mathrm{ctf}}(X_\eta,A)$,
the morphism $\delta_{X,M}:S_X\mathbb D_{X_\eta}M\to\mathbb D_{X_s}(S_XM)$ in
$D^b_c(X_{s,\mathrm{\acute et}},A)$ is the tensor–Hom adjoint of the pairing

$$
 S_XM\otimes S_X\mathbb D_{X_\eta}M
 \xrightarrow{\mu_X}S_X(M\otimes \mathbb D_{X_\eta}M)
 \xrightarrow{S_X\operatorname{ev}}S_X\omega_{X_\eta}
 \xrightarrow{\theta_X}\omega_{X_s}.
 \tag{1}
$$

For every separated finite-type $S$-scheme $X$ and
$M\in D^b_{\mathrm{ctf}}(X_\eta,A)$, the normalized map

$$
 \delta_{X,M}:S_X\mathbb D_{X_\eta}M
       \xrightarrow{\sim}\mathbb D_{X_s}(S_XM)
$$

is an isomorphism in $D^b_c(X_{s,\mathrm{\acute et}},A)$.

The same holds for a constructible complex of finite Tor dimension given
initially on $X_{\bar\eta}$: such a complex descends to a finite
extension of $\eta$, and trait-change invariance identifies the
resulting assertion with the one just stated.

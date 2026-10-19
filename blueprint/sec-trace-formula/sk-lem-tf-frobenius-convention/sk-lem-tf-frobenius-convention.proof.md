+++
kind = "proof"
of = "sk-lem-tf-frobenius-convention"
uses = ["sk-def-sf-weil-complexes"]
+++
On coordinate rings the two maps are

$$
 \Phi_X^\#(a\otimes b)=a^q\otimes b,
 \qquad \operatorname{Fr}_X^\#(a\otimes b)=a\otimes b^{1/q}.
$$

Consequently $\Phi_X=F_X^{\mathrm{abs}}\operatorname{Fr}_X$, where
$F_X^{\mathrm{abs}}$ is the absolute $q$-power Frobenius of $X$. On the
classical constructible category, pullback along absolute Frobenius is
naturally isomorphic to the identity, because for an étale object
its relative Frobenius is an isomorphism, functorial in that object. The
proétale comparison transports this natural isomorphism to
$\Dctf(X,A)$, which gives $\kappa_m$ and its compatibility with
iteration.

It remains to see that $\kappa_m$ preserves the pullback units. A natural
isomorphism of left adjoints has a unique adjoint mate, an
isomorphism of the right adjoints, and the unit and counit identities
identify the two pullback maps on compact cohomology. Applying this
to $\kappa_m$ and composing with the Frobenius correspondence proves the
operator equality; iteration follows by pasting the pullback units.
In particular, for the constant Weil complex, $T_{c_1}(\psi)$ acts by $q^d$
on the top untwisted compact cohomology of a smooth $d$-fold, in
agreement with the normalization of geometric Frobenius recorded after
[sk-def-sf-weil-complexes].

+++
kind = "proof"
of = "sk-lem-tf-frobenius-convention"
uses = ["sk-def-sf-weil-complexes"]
+++
The maps $\Phi_X$ and $\operatorname{Fr}_X$ differ by the
absolute Frobenius, and pullback along the absolute Frobenius is
naturally the identity on étale sheaves.
On coordinate rings the two maps are

$$
\Phi_X^\#(a\otimes b)=a^q\otimes b,
\qquad \operatorname{Fr}_X^\#(a\otimes b)=a\otimes b^{1/q}.
$$

Consequently, $\Phi_X=F_X\operatorname{Fr}_X$, where
$F_X$ is the absolute $q$-power Frobenius of $X$. On the
classical constructible category, pullback along absolute Frobenius is
naturally isomorphic to the identity, because for an étale object
its relative Frobenius is an isomorphism, functorial in that object.
Transporting this natural isomorphism to $D^b_{\mathrm{ctf}}(X,A)$ by the
comparison with the pro-étale site, we obtain $\kappa_m$ together with its compatibility with
iteration.

It remains to compare the pullback maps $(\Phi_X^m)^*$ and
$(\operatorname{Fr}_X^m)^*$ on compact cohomology. Recall that a natural
isomorphism of left adjoints has a unique mate, which is an
isomorphism of the right adjoints, and the unit and counit identities
then show that $\kappa_m$ carries one pullback map to the other. Composing
with $\phi_m$, or with an arbitrary morphism
$(\operatorname{Fr}_X^m)^*K\to K$, we obtain the equality of operators.
The identity $\psi_m=\phi_m\kappa_m$ follows from the compatibility
of $\kappa_m$ with iteration.
For example, if $X_0$ is smooth and geometrically connected of
dimension $d$ and $K=A_X$ with its constant Weil structure, then
$T_{c_1}(\psi)$ acts on $H^{2d}_c(X,A)=A(-d)$ by $q^d$, which agrees
with the action of geometric Frobenius on $A(-d)$ recorded after
Definition [sk-def-sf-weil-complexes].

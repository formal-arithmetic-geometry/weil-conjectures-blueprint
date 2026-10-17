+++
kind = "proof"
of = "det-sp-thick-origin-homotopy"
uses = ["det-sp-dnc-base-change", "det-sp-nearby-cycles-exchanges", "thm-weil-pbc-universal-homeomorphism-invariance", "lem-pur-a1-direct-image"]
+++
Since $H_1=\operatorname{id}$, its lift is the identity and $\phi_1=\operatorname{id}_E$.

*The family of endomorphisms.* Let $H\colon X\times\mathbf A^1\to X$, $H(x,a)=ax$, and let
$\operatorname{pr}\colon X\times\mathbf A^1\to X$ be the projection. Both map
$Z\times\mathbf A^1$ schematically into $Z$, since $H^{\cdot}(x^m)=a^mx^m\in(x^m)$. The projection
is flat, so by [det-sp-dnc-base-change] its deformation is
$\mathcal D_{Z\times\mathbf A^1}(X\times\mathbf A^1)\simeq\mathcal D_ZX\times\mathbf A^1$, and the
lift of $\operatorname{pr}$ is smooth. Apply the pullback exchange of
[det-sp-nearby-cycles-exchanges] for the lift of $H$, and then invert the smooth exchange for the
lift of $\operatorname{pr}$. After restriction to the zero section this gives a map
$H_Z^*E\to\operatorname{pr}_Z^*E$ on $Z\times\mathbf A^1$. The restrictions $H_Z$ and
$\operatorname{pr}_Z$ of $H$ and $\operatorname{pr}$ to $Z\times\mathbf A^1$ induce the same
reduced map to $Z$, so nilpotent invariance [thm-weil-pbc-universal-homeomorphism-invariance]
identifies $H_Z^*E$ with $\operatorname{pr}_Z^*E$, naturally in $E$. This turns the map into one
endomorphism $\phi$ of $\operatorname{pr}_Z^*E$. Restricting along $a\colon Z\to Z\times\mathbf A^1$,
the compatibility of the pullback exchange with composition identifies the fibre of $\phi$ at $a$
with $\phi_a$.

*Constancy.* Since $Z_{\mathrm{red}}$ is a point, nilpotent invariance identifies
$D^b_c(Z_{\mathrm{\acute et}},A)$ with the bounded derived category of finite $A$-modules, and
$Z\times\mathbf A^1$ with $\mathbf A^1_k$ up to nilpotents. For $p=\operatorname{pr}_Z$ and every
such bounded complex $B$, the affine-line calculation [lem-pur-a1-direct-image]
($H^0(\mathbf A^1_k,M)=M$ and $H^r(\mathbf A^1_k,M)=0$ for $r>0$) and the hypercohomology spectral
sequence give $R\Gamma(\mathbf A^1,p^*B)=B$, that is, the unit $B\to Rp_*p^*B$ is an isomorphism.
By adjunction $p^*$ is fully faithful. Hence $\phi=p^*\phi'$ for a single endomorphism $\phi'$ of
$E$, and its restrictions at $a=0$ and $a=1$ both equal $\phi'$. Thus $\phi_0=\phi_1$.

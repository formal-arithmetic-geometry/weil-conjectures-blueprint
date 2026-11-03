+++
kind = "proof"
of = "det-sf-mate-compactification"
uses = ["det-sf-mate-open-restriction", "det-sf-existence-brown", "det-sf-comp-coherence-single"]
+++
For a proper $p$, the identity is an open immersion compactifying it, so
$Rp_!=Rp_*$ on $\Loc(\Dctf(\overline X,\Lambda))$ ([det-sf-comp-coherence-single]),
and $p^!$ is its right adjoint ([det-sf-existence-brown]). By
[det-sf-mate-open-restriction] (1), $j^*$ is right adjoint to $j_!$ on the
localizing categories. A composite of adjunctions is an adjunction: for
$M\in\Loc(\Dctf(X,\Lambda))$ and $N\in\Loc(\Dctf(Y,\Lambda))$,

$$
\Hom(Rp_*j_!M,N)\simeq\Hom(j_!M,p^!N)\simeq\Hom(M,j^*p^!N),
$$

naturally in $M$ and $N$, with counit the composite of the counits. Since
$Rf_!=Rp_*j_!$ by definition (for this compactification), $j^*p^!$ is a right
adjoint of $Rf_!$; by the uniqueness of right adjoints
([det-sf-existence-brown] (3)) there is a unique isomorphism
$f^!\simeq j^*p^!$ compatible with the two adjunctions, which is the claim
about counits.

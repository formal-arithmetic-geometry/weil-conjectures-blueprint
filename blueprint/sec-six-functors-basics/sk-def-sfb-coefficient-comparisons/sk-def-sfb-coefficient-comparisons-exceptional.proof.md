+++
kind = "proof"
of = "det-sfb-coefficient-comparisons-exceptional"
+++
*Definition.* $f^!K\in\Dctf(X,\Lambda)$ by [sk-def-sfb-dc-upper-shriek], so the comparison
[det-sfb-coefficient-comparisons-compact-support] applies to it and $\beta_{f,K}$ is defined. Since the counit
of a composite adjunction is the composite of the counits, and the $Rf_!$-comparisons are compatible with
composition, $\beta_{gf,K}=f^!(\beta_{g,K})\circ\beta_{f,g^!K}$ under $(gf)^!=f^!g^!$; for an open
immersion $f^!=f^*$ and $\beta$ is the pullback identification.

*Closed immersions.* Let $i$ be closed with open complement $j$. The triangle
$i_*i^!K\to K\to Rj_*j^*K\to$ in $\Dctf(Y,\Lambda)$ is carried by extension of scalars to a triangle; extension of
scalars commutes with $i_*$, $j^*$ and $Rj_*$ ([det-sfb-coefficient-comparisons-direct-image]), so the image is
identified with the triangle $i_*i^!(K_{\Lambda'})\to K_{\Lambda'}\to Rj_*j^*(K_{\Lambda'})$, the second and third
comparisons being isomorphisms. The induced map on fibres is $i_*\beta_{i,K}$ because the first map of the
triangle is the counit. Hence $i_*\beta_{i,K}$ and so $\beta_{i,K}$ ($i_*$ is fully faithful) is an isomorphism.

*The projective line.* For $q\colon\mathbf P^1_Y\to Y$, $q^!=q^*(1)[2]$ via the adjunction defined by the diagonal class
and trace ([sk-prop-geo-p1-adjunction], [sk-prop-diagonal-tower]). These classes commute with the listed
coefficient maps: the finite ones come from Kummer theory and derived scalar extension, the integral ones are
their compatible limits (for $\mathcal O_E\to A$, $A_X$ is perfect over $\mathcal O_{E,X}$, so its tensor commutes with
these limits and gives the finite classes), and the field ones are their scalar extensions. Hence
$\beta_{q,K}$ is the pullback-and-twist identification, an isomorphism.

*General $f$.* Open restriction and composition give $\mathbf A^n_Y\to Y$ (open in $(\mathbf P^1)^n_Y$). Locally on $X$ (a
finite affine cover; $\beta$ is compatible with open restriction and isomorphisms can be checked locally),
$f$ factors as a closed immersion into some $\mathbf A^n_Y$ followed by the projection, and compatibility with
composition gives the claim.

+++
id = "prose-09-20"
kind = "hidden"
title = "Change of finite coefficients (3)"
order = 771
+++
It follows that the isomorphisms $\gamma_{f,A}$ are compatible with change of coefficients: for
$K\in D^b_{\mathrm{ctf}}(Y_{\mathrm{pro}\acute{e}t},A)$,

$$
c_{A,B}(K)\circ(\gamma_{f,A}(K))_B=\gamma_{f,B}(K_B),
\tag{9.17}
$$

the sources being identified by $(f_A^*K(d)[2d])_B\simeq f_B^*(K_B)(d)[2d]$.
Indeed, $\gamma_{f,A}$ is the map $\mu_{f,K}$ composed with the inverse of the
orientation, and each factor commutes with change of coefficients.

The map $\mu_{f,K}$ is built from the projection formula and
the counit. The projection formula commutes with extension of scalars,
which is itself a tensor product, and (9.16) relates
the counits over $A$ and $B$. Hence $\mu_{f,K}$ commutes
with change of coefficients.

The orientation is a map between invertible sheaves placed in degree $-2d$,
so its compatibility is local. For vector bundles it follows from the
construction via the projective line
(Proposition [proposition-purity-vector-bundles]), since the Kummer
class and the splitting (9.8) are compatible
with extension of scalars. On the deformation family we use the uniqueness
in Lemma [lemma-section-normal-bundle] over the base of the family.
It applies once we know that the extended comparison is a comparison of the
kind considered there, and this holds because $c$ commutes with smooth
exceptional base change and with composition with étale maps. Indeed,
both sides are transposes of counits, and by the proof of
Lemma [lemma-sp-reduction] they agree on charts. Since the original
comparison is the identity at $t=1$, so is the extended one, and by
uniqueness the extended comparison is the comparison of
Lemma [lemma-section-normal-bundle] over $B$.

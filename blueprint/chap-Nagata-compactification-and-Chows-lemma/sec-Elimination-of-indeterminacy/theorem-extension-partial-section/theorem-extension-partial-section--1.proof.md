+++
kind = "proof"
of = "theorem-extension-partial-section--1"
order = 1438002
uses = ["lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "lemma-making-open-schematically-dense", "lemma-products-composites-u-admissible-blow", "proposition-relative-form-zariski-s-main"]
+++
First consider the case where $p$ is quasi-affine as a morphism.
The result for two nested opens is
`AlgebraicGeometry.exists_isAdmissible_extend_of_isQuasiAffineHom_of_le`;
it does not require the smaller open to be dense. Its construction first
replaces the base by a $V$-admissible blow-up. The closure of the
base-changed section then lies over the complement of the closure of
the difference of the two pulled-back opens. One can restrict to a
quasi-compact open of the new base on which the inverse images of $U$
and $V$ coincide.
The case of equal opens is obtained by clearing denominators over affine
opens of the base, making the inverse image of the domain schematically
dense by [lemma-making-open-schematically-dense], and gluing the local
extensions by [lemma-uniqueness-maps-dense-open]. The local centre extends
to the whole base with support disjoint from the inverse image of $V$;
composing the blow-ups gives the quasi-affine case for the original pair
of opens, using [lemma-products-composites-u-admissible-blow].

For general $p$, choose a finite affine open cover $Y=\bigcup_iY_i$.
Each morphism $Y_i\to T$ is quasi-affine, so apply the preceding case to
$f^{-1}(Y_i)\subseteq V$ and the restricted section. Take the product of
the resulting centres, giving a $V$-admissible blow-up $q:T_1\to T$
which maps to each of these blow-ups. Let $\sigma:U\to T_1$ be the
inverse of $q$ over $U$, followed by the open immersion into $T_1$, and
put

$$
F=(f,\sigma):U\longrightarrow Y\times_TT_1,\qquad
Z=\overline{F(U)}.
$$

Here $Z$ is the scheme-theoretic image, as in
[lemma-schematic-closure-uniqueness]. Over each $Y_i$, the closure of
$F(U)$ lies in the pullback of the closed graph of the local extension.
This graph is a section over an open of $T_1$, so its intersection with
each fibre has at most one point. The finite cover therefore shows that
$Z\to T_1$ has finite fibres. It is also separated, quasi-compact and
locally of finite type, hence locally quasi-finite. This is the
construction in
`AlgebraicGeometry.exists_isAdmissible_locallyQuasiFinite_image_graph`.

By [proposition-relative-form-zariski-s-main], the morphism
$r:Z\to T_1$ is quasi-affine. Set $U_1=q^{-1}(U)$ and $V_1=q^{-1}(V)$.
The isomorphism $U_1\simeq U$ identifies the base-changed section with
a section $f_1:U_1\to Z$. Its image is closed in $r^{-1}(V_1)$:
closedness of the original image is preserved by base change, and then
by inverse image along the closed immersion $Z\hookrightarrow Y\times_TT_1$.
Apply the quasi-affine case to $r$, $U_1\subseteq V_1$ and $f_1$.
It gives a $V_1$-admissible blow-up $q_2:T_2\to T_1$, an open $W$
containing $q_2^{-1}(U_1)$, and a map $h:W\to Z$ extending $f_1$ with
closed graph.

Composing $h$ with $Z\hookrightarrow Y\times_TT_1$ preserves
closedness of the graph, since the comparison of graphs is a base
change of this closed immersion. This is
`AlgebraicGeometry.exists_isAdmissible_extend_partialSection_of_isClosedImmersion`.
Finally [lemma-products-composites-u-admissible-blow] identifies
$q\circ q_2$ with a single $V$-admissible blow-up of $T$. Project the
extension to $Y$ and transport it along this identification. The
identity

$$
(Y\times_TT_1)\times_{T_1}T_2\simeq Y\times_TT_2
$$

preserves the closed graph, and the restriction over $U$ is still $f$.
This last reduction is
`AlgebraicGeometry.exists_isAdmissible_extend_partialSection_of_blowup`.
The density hypothesis on $U$ is retained in the theorem's statement,
although this assembly does not use it.

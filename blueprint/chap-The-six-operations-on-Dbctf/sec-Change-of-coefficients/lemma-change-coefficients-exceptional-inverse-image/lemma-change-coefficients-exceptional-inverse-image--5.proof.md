+++
kind = "proof"
of = "lemma-change-coefficients-exceptional-inverse-image--5"
order = 641011
uses = ["lemma-change-coefficients-direct-image--4", "proposition-ell-adic-cycle-class-diagonal--5", "proposition-ell-adic-cycle-class-diagonal--6"]
+++
Assume $\Lambda=\mathcal O_E$ and $\Lambda'=E$.

Use clause [lemma-change-coefficients-direct-image--4] in the localization argument. On the projective line, the $E$-valued diagonal class and trace are obtained by scalar extension from $\mathcal O_E$. The local factorization then proves the assertion.

*Closed immersions.* For a closed immersion $i$ with open complement
$j$, the functor $i^!$ is determined by the localization triangle

$$
i_*i^!K\longrightarrow K\longrightarrow Rj_*j^*K.
$$

It expresses $i_*i^!K$ as the fibre of a map between objects whose
behaviour under extension of scalars we already know. Extension of scalars
commutes with $i_*$, $j^*$ and, by
Lemma [lemma-change-coefficients-direct-image], $Rj_*$. Hence the
extension of scalars of this triangle is the triangle for $K_{\Lambda'}$
over $\Lambda'$. Since the first map is the counit, the comparison on
fibres is $i_*\beta_{i,K}$. The comparisons on the other two terms are
isomorphisms, and therefore $i_*\beta_{i,K}$ is one as well. Since $i_*$
is fully faithful, $\beta_{i,K}$ is an isomorphism.

*The projective line.* Let $q:\mathbf P^1_Y\to Y$. The adjunction
$Rq_*\dashv q^*(1)[2]$ between $D^b_{\mathrm{ctf}}(\mathbf P^1_Y,\Lambda)$ and
$D^b_{\mathrm{ctf}}(Y,\Lambda)$ is defined by the diagonal class and the trace. Through
these two maps, $q^!$ is identified with $q^*(1)[2]$. It therefore
suffices to know that the two maps commute with all the maps of
coefficient rings listed above.
This holds by construction
(Propositions [proposition-adjunction-projective-line]
and [proposition-ell-adic-cycle-class-diagonal]). The classes with
finite coefficients are constructed from the Kummer sequence and derived
extension of scalars. The integral classes are their compatible limits, and
the classes over fields are obtained from these by extension of scalars.
Only one map in the list needs a further remark. For $\mathcal O_E\to A$,
the proof of Lemma [lemma-change-coefficients-direct-image] shows that
$A_X$ is perfect. Hence the derived tensor product with $A_X$ commutes with
the inverse limits defining the integral classes. The resulting classes
are exactly the classes with finite coefficients. Hence the identification $q^!\simeq q^*(1)[2]$ is
compatible with extension of scalars. Under this identification
$\beta_{q,K}$ becomes the isomorphism of
Definition [definition-change-of-coefficients-maps](1) for $q^*$,
twisted by $(1)[2]$.

*General $f$.* The open immersion
$\mathbf A^1_Y\hookrightarrow\mathbf P^1_Y$ is a case of restriction to
opens, and so $\beta$ is an isomorphism for $\mathbf A^1_Y\to Y$. The
projection $\mathbf A^d_Y\to Y$ is a composite of $d$ projections of this
kind. The compatibility of $\beta$ with composition gives the case of
affine space. In general, whether $\beta_{f,K}$ is an isomorphism may be
checked locally on $X$. Using a finite affine cover, we may therefore
assume that $f$ factors as a closed immersion into an affine space over
$Y$ followed by the projection. Then the two cases already treated and
compatibility with composition give the claim.

*Source:* the proof of Lemma [lemma-change-coefficients-exceptional-inverse-image].

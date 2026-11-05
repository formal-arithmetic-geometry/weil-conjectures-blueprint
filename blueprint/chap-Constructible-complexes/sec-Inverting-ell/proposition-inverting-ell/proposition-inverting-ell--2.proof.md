+++
kind = "proof"
of = "proposition-inverting-ell--2"
order = 303002
uses = ["lemma-continuity-ext-out-constructible-complex", "lemma-lattices-after-finite-stratification", "lemma-integral-models--5", "proposition-extension-zero-restriction-closed-subscheme", "proposition-inverting-ell--1"]
+++
The coefficient sheaf $E_X$ is the sequential colimit of multiplication
by $\ell$ on $\mathcal O_{E,X}$. Indeed, a continuous function from a
profinite set to $E$ has a bounded denominator, and inverse image from
the point preserves this colimit. Exactness of filtered colimits makes
extension of scalars exact. Its derived functor preserves bounded
constructibility and distinguished triangles.

For $K,L\in\Dbc(X,\mathcal O_E)$, tensor the coefficient sequence with
a complex representing $L$. Its colimit is the restriction of $F(L)$,
and its first map is the adjunction unit. The sequential integral
continuity used in [proposition-inverting-ell--1] factors the adjoint
of any morphism $u:F(K)\to F(L)$ through a finite stage. Consequently,
there are $n\geq0$ and $v:K\to L$ with $\ell^n u=F(v)$.

Every bounded constructible $E$-complex has an integral model. For a
constructible sheaf in degree zero, finite local presentations over
$E_X$ become finite free after passing to pro-étale charts on the
strata. Apply [lemma-lattices-after-finite-stratification], extend the
integral models by zero as in [lemma-integral-models--5], and glue them
using the open and closed exact sequences of
[proposition-extension-zero-restriction-closed-subscheme]. Clearing
denominators lifts the extension classes. More generally, the
essential image of $F$ is closed under shifts and cones: clear the
denominator of a morphism between two images and take its integral
cone. Multiplication by a power of $\ell$ is invertible over $E$, so
this has the required rational cone. Induction along the bounded
truncation triangles now gives an integral model for every complex.

Finally, multiplication by $\ell$ is invertible on every complex of
$E_X$-modules, so $F$ kills complexes annihilated by a power of $\ell$
and inverts the morphisms with such a cone. It therefore factors
through the rationalization. Clearing denominators and
[proposition-inverting-ell--1] make the induced functor full and
faithful, and the integral models make it essentially surjective.
This proves the localization assertion. Uniqueness of localization
gives the equivalence and its natural isomorphism with extension of
scalars.

+++
id = "proof/theorem-cohomology-curves/2"
kind = "proof"
of = "theorem-cohomology-curves"
order = 1618
+++
For constructible sheaves we reduce to the explicit calculations, and
arbitrary torsion sheaves are filtered colimits of these. The reduction
has four steps: dévissage to constructible $\mathbf F_\ell$-sheaves,
extension by zero from an open on which the sheaf is locally constant,
a cover of degree prime to $\ell$ that makes it unipotent, and
normalization, which leaves constant coefficients on smooth curves.

By Theorem [theorem-bounded-below-cohomology-comparison], we may work on $C_{\acute{e}t}$, and
since a universal homeomorphism does not change the étale topos, we may
replace $C$ by $C_{\mathrm{red}}$.  A constructible torsion sheaf has a
finite exponent, because it has finitely many isomorphism types of
finite stalks.  It is therefore the direct sum of its finitely many primary
parts, and a finite filtration of an $\ell$-primary part has constructible
$\mathbf F_\ell$-sheaves as graded pieces.  By the stability under
extensions just proved, it suffices to treat such sheaves.

Choose a dense smooth open $j:U\hookrightarrow C$ on which the
sheaf is finite locally constant.  By Lemma [lemma-removing-finitely-many-points]
we may replace the sheaf by its extension by zero.  On the connected
components of $U$, Lemma [lemma-reduction-unipotent-local-system] and finite
direct images reduce us to constant $\mathbf F_\ell$ extended by zero on
curves finite over $C$; this is allowed because the assertions pass to
direct summands and because, by Lemma [lemma-finite-morphisms-cohomology], finite
direct images are exact and do not change cohomology.  Finally, normalization and Lemma [lemma-sheaves-finite-support-finite-morphisms] reduce these sheaves to the
calculations with constant coefficients on smooth curves, namely the
Kummer sequence for $\ell\ne p$ and the Artin–Schreier
sequence for $\ell=p$.  Since all reductions preserve the
hypothesis that $C$ is proper or affine, the theorem holds for
constructible torsion sheaves.

An arbitrary torsion sheaf on the qcqs scheme $C$ is a filtered
colimit of constructible torsion sheaves, and cohomology commutes with
filtered colimits [Stacks, [03SA](https://stacks.math.columbia.edu/tag/03SA), [03Q5](https://stacks.math.columbia.edu/tag/03Q5)].  For torsion prime to
the characteristic or $p$-primary torsion, we may take the constructible
sheaves with the same kind of torsion, by splitting off primary
parts before passing to the colimit. Pullback and restriction also
commute with filtered colimits. Hence vanishing and the pullback
isomorphisms pass to the colimit. So does surjectivity in $(C_8)$,
because a representative of a class already occurs at some
stage. Finiteness is asserted only for constructible sheaves.
Finally, Theorem [theorem-bounded-below-cohomology-comparison] carries these conclusions and their maps over to $C_{\mathrm{pro}\acute{e}t}$.

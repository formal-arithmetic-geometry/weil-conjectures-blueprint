+++
id = "proof/sk-thm-curve-package/2"
kind = "proof"
of = "sk-thm-curve-package"
order = 2
uses = ["sk-lem-curve-sylow-trace", "sk-lem-curve-finite-support"]
+++
By Theorem [sk-prop-sf-comparison], we may work on $C_{\acute{e}t}$. A
universal homeomorphism does not change the étale topos, and hence we may
replace $C$ by $C_{\mathrm{red}}$. A constructible torsion sheaf has a
finite exponent, because it has finitely many isomorphism types of
finite stalks. Such a sheaf is the direct sum of its finitely many primary
parts, and a finite filtration of an $\ell$-primary part has constructible
$\mathbf F_\ell$-sheaves as graded pieces. By the stability under
extensions just proved, it suffices to treat such sheaves.

Choose a dense smooth open $j:U\hookrightarrow C$ on which the
sheaf is finite locally constant. By Lemma [sk-lem-curve-dense-open]
we may replace the sheaf by its extension by zero. On the connected
components of $U$ we use Lemma [sk-lem-curve-sylow-trace] and finite
direct images to reduce to constant $\mathbf F_\ell$ extended by zero on
curves finite over $C$. We may do so because the assertions pass to
direct summands, and because finite direct images are exact and do not
change cohomology (Lemma [sk-lem-curve-finite-support]). Using normalization and
Lemma [sk-lem-curve-finite-support], we reduce these sheaves to the
calculations with constant coefficients on smooth curves, namely the
Kummer sequence for $\ell\ne p$ and the Artin–Schreier
sequence for $\ell=p$. All reductions preserve the
hypothesis that $C$ is proper or affine. This proves the theorem for
constructible torsion sheaves.

An arbitrary torsion sheaf on the qcqs scheme $C$ is a filtered
colimit of constructible torsion sheaves, and cohomology commutes with
filtered colimits [Stacks, Tag 03SA](https://stacks.math.columbia.edu/tag/03SA), [Stacks, Tag 03Q5](https://stacks.math.columbia.edu/tag/03Q5). For torsion prime to
the characteristic or $p$-primary torsion, we may take the constructible
sheaves with the same kind of torsion, by splitting off primary
parts before passing to the colimit. Pullback and restriction also
commute with filtered colimits, and hence vanishing and the pullback
isomorphisms pass to the colimit. Surjectivity in $(C_8)$ passes to
the colimit because a representative of a class already occurs at some
stage. Finiteness is asserted only for constructible sheaves. Finally,
by Theorem [sk-prop-sf-comparison] these conclusions and their
maps carry over to $C_{\mathrm{pro}\acute{e}t}$.

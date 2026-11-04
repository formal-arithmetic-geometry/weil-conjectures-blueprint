+++
kind  = "proof"
of    = "lem-pc-rf-perfect-base-change"
+++
Assertion (2) is [lem-pc-rf-base-change-flat-module]; proper morphisms
are quasi-compact and separated.

For (3), let $A$ be Noetherian. The cohomology modules
$\Gamma(S,R^qf_*\mathcal G)$ of the Cech complex are finite over $A$
([lem-pc-coherent-hi]), and by [lem-pc-rf-base-change-flat-module] the Cech
complex is quasi-isomorphic to a bounded complex of flat $A$-modules, so
[lem-pc-noetherian-flat-complex-perfect] shows that $Rf_*\mathcal G$ is
perfect; if $f$ is projective this is
[lem-pc-projective-noetherian-rf-perfect]. Perfectness of
$Rf_{T,*}\mathcal G_T\cong Lg^*Rf_*\mathcal G$ then follows as in
[cor-pc-projective-noetherian-rf-perfect-base-change]: the derived
pullback of a bounded complex of finite projective $A$-modules is its
termwise base change, again bounded with finite projective terms.

Assertion (1) is the recorded classical input: Derived Categories of
Schemes, Lemma 36.30.4 (Tag [0B91](https://stacks.math.columbia.edu/tag/0B91))
reads, in clause (2), ``Let $S$ be a scheme. Let $f:X\to S$ be a
proper morphism of finite presentation. ... Let $\mathcal{G}$ be an
$\mathcal{O}_X$-module of finite presentation, flat over $S$. Then
$Rf_*\mathcal{G}$ is a perfect object of $D(\mathcal{O}_S)$ and its
formation commutes with arbitrary base change.''; locally on $S$ a perfect
object is represented by a bounded complex of finite free modules, and
the compatibility with base change gives the isomorphisms on cohomology
sheaves. Its proof is the cohomology-and-base-change theorem of the same
section (Lemma 36.30.1, Tag [0A1H](https://stacks.math.columbia.edu/tag/0A1H)),
via reduction to a Noetherian base by absolute Noetherian approximation.

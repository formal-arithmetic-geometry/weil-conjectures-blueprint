+++
kind  = "proof"
of    = "thm-zl-relative-line-step"
+++
By [lem-zl-sheaves-to-complexes], it suffices to treat a mixed
sheaf of weights at most $w$. Its finite weight filtration and the
extension bounds of [lem-a1-extension-bounds]
(propagated through the long exact sequences) reduce to a pure graded
piece. Apply [thm-zl-relative-line-stratification]: on a
relative-curve stratum the assertion is
[thm-zl-relative-affine-curve-core] (which gives the sheaf-level
bound $R^ap_!\mathcal F$ mixed of weights at most $w+a$, for pure
$\mathcal F$); on a quasi-finite stratum it is
[lem-zl-quasi-finite]. The composition constraint
[lem-zl-shriek-composition] identifies these stratumwise direct
images with the corresponding pieces of $Rp_!$. Noetherian induction,
using the one-way localization gluing rule [lem-zl-open-closed-weight]
for an open–closed decomposition of the strata, in the morphism-level
form [lem-zl-morphism-open-closed-reduction], reassembles the source
and target strata.

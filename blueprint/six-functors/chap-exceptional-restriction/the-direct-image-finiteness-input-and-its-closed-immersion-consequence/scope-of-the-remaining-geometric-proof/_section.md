+++
id = "scope-of-the-remaining-geometric-proof"
kind = "section"
title = "Scope of the remaining geometric proof"
order = 3350
uses = ["def-exc-open-complement-bound", "def-weil-finite-tor-amplitude", "def-weil-pbc-constructible-complexes", "def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "lem-exc-closed-ambient", "lem-exc-closed-amplitude", "lem-kun-cd-sep-closed-point", "lemma-weil-pbc-geometric-stalk-conservative", "obl-fin-comparison", "prop-exc-closed-tor", "prop-weil-pbc-strict-henselization-stalk-formula", "sbc-thm-finiteness-finite-type", "thm-dg-finite-type-constructibility", "thm-exc-curve-open-constructible-general", "thm-exc-curve-open-dimension-general", "thm-sc-finite-type-torsion-cd"]
+++
The preceding propositions prove preservation, including a uniform
finite-level coefficient comparison, for open immersions and finite
etale morphisms. Their proofs apply to the actual ambient pro-etale
right adjoints. For arbitrary closed immersions into finite-type schemes of dimension
at most one over a finite field or its algebraic closure,
[thm-exc-curve-open-dimension-general], [thm-exc-curve-open-constructible-general]
now verify the open-complement conditions by the normalization of
strictly local curve branches. Thus
[thm-exc-curve-closed-preservation-general], [cor-exc-curve-proetale-preservation-general]
prove preservation with uniform upper shift two, including singular
and nonreduced curves. Preservation is not a hypothesis of these results.
The closed-support comparison above also identifies
the two ambient closed-immersion functors, using the earlier site
comparison and closed-recollement inputs. The closed-support
constructibility argument isolates independent direct-image assertions;
it does not establish them for every open immersion. The finite-level
comparison and the comparison of direct images used here now have
their own foundational proofs in
prop:weil-pbc-site-comparison-finite-level, prop:weil-pbc-comparison-direct-image:
the former uses ind-etale refinements and Cech acyclicity, and the
latter checks the adjunction mate on derived sections of basis objects.
These proofs settle those two inputs. The closed-recollement
input is now proved in
thm:exc-proetale-open-closed-exact, thm:exc-proetale-recollement
from explicit lifts of affine ind-etale coverings. Thus the
ambient closed comparison and the closed-curve preservation
corollary above no longer rely on an unproved closed-site input.
In arbitrary dimension, thm:fin-open-degree-zero proves
degree-zero open direct-image constructibility by a separate
Noetherian argument, and the boundary-sheaf consequence is proved
in lem:fin-boundary-sheaf. The two clauses of the
direct-image finiteness input of [def-exc-direct-image-input] are now
theorems of this blueprint: the constructibility of the higher direct
images of a constructible sheaf under a morphism of finite type is
thm:dg-finite-type-constructibility of the constructibility chapter, proved by
Deligne's finite-boundary induction, whose smooth-with-locally-constant-
coefficients step goes through duality from the compact-support theory
rather than through constructibility of the ordinary direct image itself;
and the cohomological-dimension bound over a separably closed field is
thm:sc-finite-type-torsion-cd of the Jacobian chapter, for arbitrary
torsion sheaves. [thm-exc-direct-image-input-holds] records that both
clauses hold, and [lem-exc-open-complement-known] draws the
open-complement condition with $c=2d$ from them, whence
[cor-exc-closed-preservation-datum] proves preservation for an
arbitrary closed immersion, without an amplitude or constructibility
hypothesis.

For a general separated finite-type morphism over a finite field, the
usual etale proof proceeds on affine charts by a closed immersion into
$\mathbf A^d_Y$, followed by the smooth projection. The smooth
adjunction $Rg^!K=g^*K(d)[2d]$ is now available without assuming
constructible preservation: it is the smooth purity of the smooth-purity chapter, and
with it both preservation clauses for smooth morphisms
([cor-pur-smooth-admissibility] there). The assembly is therefore
carried out in that chapter, as
[thm-pur-general-admissibility]: on affine charts the closed-support
calculation of the present section gives the local bound
$[a-2d,b-2d+c+1]$, a finite cover gives a uniform two-sided bound, and
the same calculation with the residue field gives finite Tor amplitude.
This explains precisely which earlier geometric theorems supply the
hypotheses, rather than calling preservation part of the definition of
$f^!$.

The smooth-purity chapter no longer assumes the preservation clauses of
def:weil-exceptional-adjoint-admissibility: its conventions assume
only the ambient exceptional right adjoint datum of
def:weil-ambient-exceptional-adjoint — the existence of
$Rf_n^{\times}$, i.e. clause (1) — and it proves *both*
preservation clauses for smooth morphisms from its own purity theorem
([cor-pur-smooth-admissibility]). For closed immersions clauses (2)
and (3) are the results of the present section
([lem-exc-closed-ambient], [lem-exc-closed-amplitude], [prop-exc-closed-tor]),
which use no purity input. There is accordingly no circular citation
between the two chapters, and the smooth case of the preservation problem
is closed. For a general separated finite-type morphism the assembly
needs the open-complement condition of
[def-exc-open-complement-bound] for the complements of its affine
charts, and that condition is no longer an input: by
[lem-exc-open-complement-known] it holds with $c=2d$ for every
quasi-compact open immersion in a finite-type scheme of dimension at most
$d$ over the separably closed field $k$. Consequently both
preservation clauses hold for every separated finite-type morphism carrying the
ambient exceptional right adjoint datum of
def:weil-ambient-exceptional-adjoint — whose vanishing half is a
theorem on the blueprint's coefficient class, [thm-sf-fullcd-used-class],
the general all-sheaves form being false,
[prop-sf-fullcd-general-form-false], and whose existence half on that
class is the theorem [thm-sf-ambient-adjoint-class], so that the interface
[open-sf-ambient-adjoint-input] names only the adjunction for the
complexes outside the class — as
[cor-pur-general-admissibility-datum] of the smooth-purity chapter records, and for
every closed immersion as [cor-exc-closed-preservation-datum] here.

The open-complement condition in dimension at least two is therefore
proved: it follows from the two theorems quoted above by
[lem-exc-open-complement-known], and it is the hypothesis of neither
[cor-exc-closed-preservation-datum] nor
[thm-pur-general-admissibility] of the smooth-purity chapter any longer.

The second obligation formerly recorded here, the identification of the
ambient right adjoint with the one obtained by transporting an etale
adjunction, no longer stands separately. For closed immersions it is
[prop-exc-closed-site-comparison], whose proof identifies the two
ambient right adjoints by Yoneda on all ambient objects, without assuming
their constructible restrictions. For smooth morphisms no site
comparison is needed at all: the trace–diagonal criterion
[thm-pur-td-criterion] of the smooth-purity chapter identifies the ambient right
adjoint with $Lf^{*}(-)(d)[2d]$ directly, the trace–diagonal datum
being supplied there by the affine-line and affine-space computations, so
the identification is made inside the pro-etale ambient category. The
test [lem-exc-ambient-comparison-test] remains available for any
further case in which a transported adjunction must be compared with the
ambient Brown right adjoint, and
[ex-exc-comparison-not-formal] remains the reason why such a
comparison needs an argument. The open-complement condition used
throughout this section is proved above, so no statement of the smooth-purity
chapter or of the exceptional-restriction chapter rests on it as a hypothesis.

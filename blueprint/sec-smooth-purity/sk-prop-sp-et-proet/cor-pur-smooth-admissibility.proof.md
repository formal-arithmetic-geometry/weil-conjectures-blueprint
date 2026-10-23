+++
kind  = "proof"
of    = "cor-pur-smooth-admissibility"
+++
By [cor-pur-dualizing-object-purity] the right adjoint $Rf^!$, whose
existence on the coefficients used here is the theorem
[cor-sf-ambient-adjoint-discharge], is
identified with $Lf^*(-)(d)[2d]$ on finite-Tor objects. For a
bounded constructible complex $L$ without finite Tor amplitude, use
the tensor formula on all ordinary etale complexes of
[thm-asd-smooth-tensor], the orientation at $\Lambda$ of
[thm-pur-diagonal-dualizing-object], and the comparison
[thm-sf-ambient-adjoint-class]. They give the same identification
for $L$; no site-perfectness of $L$ is assumed. The criterion below is
applied at the finite etale level and transported to the small pro-etale
site along [thm-cbc-finite-level-proetale], as elsewhere in this
chapter.
Step 1: (1). The inverse image of [prop-weil-pbc-inverse-image-exact] is exact.
It preserves constructibility: pull back each finite stratification
and each finite locally constant sheaf on its strata, as in
[def-weil-finite-torsion-constructibility]. Thus for
$L\in D_c^{[a,b]}(Y,A)$ the complex $Lf^*L$ is bounded constructible
with $\mathcal H^r(Lf^*L)\cong f^*\mathcal H^r(L)$, which vanishes for
$r\notin[a,b]$; the [def-coefficient-twists-detailed] twist preserves the
vanishing degrees by [prop-weil-twist-preserves], and the shift moves them, by the convention
$\mathcal H^r(C[2d])=\mathcal H^{r+2d}(C)$, to $[a-2d,b-2d]$.
Step 2: (2). Test the finite Tor amplitude of $Rf^!K$ by the residue
field criterion of [lem-exc-residue-tor-test]: it is equivalent to
the complex $\mathcal H^\bullet\bigl(Rf^!K\otimes^L_A\kappa\bigr)$ being
concentrated in $[a-2d,b-2d]$. Substituting the purity
identification and the associativity of the derived tensor product,

$$
Rf^!K\otimes^L_A\kappa
\;\cong\;\bigl(Lf^*K\otimes^L_A\kappa\bigr)(d)[2d]
\;\cong\;Lf^*\bigl(K\otimes^L_A\kappa\bigr)(d)[2d].
$$

By the same criterion applied to $K$, the complex
$K\otimes^L_A\kappa$ has cohomology in $[a,b]$; the inverse image
$Lf^*$ is exact, so $Lf^*(K\otimes^L_A\kappa)$ has cohomology in
$[a,b]$, and the twist by the locally constant free rank-one sheaf
$\Lambda(d)$ preserves the vanishing degrees. The shift therefore puts
the cohomology in $[a-2d,b-2d]$, which is the assertion. At field
coefficients the assertion is the case already recorded in
[lem-integral-ctf-equals-bc].

+++
kind  = "proof"
of    = "lemma-weil-pbc-curve-normalization-constant"
+++
Let $\nu:X^\nu\to X$ be the finite normalization and $j^\nu:U^\nu\hookrightarrow X^\nu$
the pullback of $j$. The normalization $X^\nu$ is a finite disjoint union of smooth curves and
points. On a component disjoint from $U^\nu$ the extension-by-zero sheaf is
zero and every assertion is immediate; on every other component $U^\nu$ is
dense. The dense-open localization lemma on $X^\nu$ therefore reduces
$j^\nu_!\underline{\mathbf F_\ell}$ to the constant sheaf on each remaining
smooth component, with the five-term sequence and all comparison maps
already specified there. If $\ell\ne\operatorname{char}k$, apply the Kummer and
localization calculation; if $\ell=\operatorname{char}k$, apply the
Artin–Schreier calculation. Thus all applicable eight assertions hold for
$j^\nu_!\underline{\mathbf F_\ell}$.

Exact finite direct image transfers them to
$\nu_*j^\nu_!\underline{\mathbf F_\ell}$. The normalization exact sequence
$0\to j_!\underline{\mathbf F_\ell}\to\nu_*j^\nu_!\underline{\mathbf F_\ell}\to Q\to0$
has a constructible cokernel $Q$ vanishing on a dense open, hence supported on
finitely many closed points; its cohomology is finite, concentrated in degree
zero, and invariant under algebraically closed field extension. The long exact
sequence therefore transfers the assertions to
$j_!\underline{\mathbf F_\ell}$: in degrees at least two the maps are
isomorphisms, and in degrees zero and one the five lemma applies; this
includes assertion (8). Properness is preserved by
finite normalization; affineness is preserved because a finite morphism
over an affine is affine. This completes the normalization, proper/affine
localization, prime-to-characteristic, and characteristic-$\ell$ branches.

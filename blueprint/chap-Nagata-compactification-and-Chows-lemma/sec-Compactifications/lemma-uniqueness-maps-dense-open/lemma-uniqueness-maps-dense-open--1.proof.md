+++
kind = "proof"
of = "lemma-uniqueness-maps-dense-open--1"
order = 1409002
+++
The equality $g\circ a=g\circ b$ defines a map
$(a,b):T\to Y\times_S Y$. Pulling back the diagonal of $Y/S$ gives
a closed immersion $e:E\to T$, since $g$ is separated, and
$a\circ e=b\circ e$. The equality $a\circ v=b\circ v$ gives a
factorization $v=e\circ w$ through $E$.

The kernel ideal sheaf of $e$ is contained in that of $v$
(`AlgebraicGeometry.Scheme.Hom.le_ker_comp`), which is zero by
scheme-theoretic dominance. Thus $e$ is a closed immersion with zero
kernel and hence an isomorphism
(`AlgebraicGeometry.IsClosedImmersion.isIso_iff_ker_eq_bot`). Cancelling
$e$ in $a\circ e=b\circ e$ gives $a=b$.

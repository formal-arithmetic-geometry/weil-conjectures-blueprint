+++
id = "lemma-weil-pbc-epsilon-direct-image-naturality"
kind = "lemma"
title = "Naturality of direct-image comparison"
order = 824
uses = ["def-weil-pbc-epsilon-direct-image-comparison", "lemma-weil-pbc-epsilon-scheme-naturality", "lemma-weil-pbc-epsilon-unit-counit-naturality"]
+++
The maps $D_f(L)$ are natural in $L$, equal the identity for $f=1_X$, and
respect composition of quasi-compact quasi-separated morphisms. For a
Cartesian square

$$
\begin{CD}
X'@>{v}>>X\\
@V{f'}VV @VV{f}V\\
Y'@>{u}>>Y,
\end{CD}
$$

the square formed by $u^*D_f(L)$, $D_{f'}(v^*L)$, and the two canonical
base-change transformations commutes.

## Proof

The underived map is adjoint to $f_*\eta^X$. Naturality of $\eta^X$ gives
naturality in $F$, its identity formula gives the identity case, and the
triangle identity shows that the adjoint for a composite is the ordered
composite of the two adjoints. Deriving preserves these equations.

For the Cartesian square, expand both routes before taking adjoints. Scheme
naturality identifies $v^*\eta^X_L$ with $\eta^{X'}_{v^*L}$, and both routes
then consist of this unit followed by restriction along the same projection
$X'\to X$ and the same base-change map. They are equal before derivation,
hence the derived base-change square commutes.
